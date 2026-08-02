#!/usr/bin/env python3
"""Scan tracked Git history, commit identities, and release archives."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".toml", ".cff", ".html"}
BUILT_INS = [
    ("credential", re.compile(rb"(?:ghp_|github_pat_|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})")),
    ("prohibited benchmark wording", re.compile(rb"teacher[- ](?:written|authored|style)|teacher's cover letter", re.I)),
]


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def patterns(extra_file: Path | None) -> list[tuple[str, re.Pattern[bytes]]]:
    result = list(BUILT_INS)
    if extra_file and extra_file.exists():
        for index, line in enumerate(extra_file.read_text(encoding="utf-8").splitlines()):
            if line.strip():
                result.append((f"local sensitive term {index + 1}", re.compile(re.escape(line.strip().encode("utf-8")), re.I)))
    return result


def scan_blob(label: str, content: bytes, checks: list[tuple[str, re.Pattern[bytes]]]) -> list[str]:
    return [f"{label}: {name}" for name, pattern in checks if pattern.search(content)]


def scan_history(checks: list[tuple[str, re.Pattern[bytes]]]) -> list[str]:
    findings: list[str] = []
    refs = git("rev-list", "--all").decode("ascii").splitlines()
    scanner_paths = {"scripts/privacy_scan.py", "scripts/privacy_scan_history.py"}
    for ref in refs:
        names = git("ls-tree", "-r", "--name-only", ref).decode("utf-8", errors="replace").splitlines()
        for name in names:
            if name in scanner_paths or Path(name).suffix.lower() not in TEXT_SUFFIXES:
                continue
            content = git("show", f"{ref}:{name}")
            findings.extend(scan_blob(f"{ref[:12]}:{name}", content, checks))
    identities = git("log", "--all", "--format=%an|%ae|%cn|%ce").decode("utf-8", errors="replace").splitlines()
    for identity in identities:
        fields = identity.split("|")
        emails = fields[1::2]
        if any(email and not email.endswith("@users.noreply.github.com") for email in emails):
            findings.append("Git history contains a non-noreply commit email")
    return findings


def scan_archives(directory: Path, checks: list[tuple[str, re.Pattern[bytes]]]) -> list[str]:
    findings: list[str] = []
    for archive in sorted(directory.glob("*")):
        if archive.suffix.lower() not in {".zip", ".skill"}:
            continue
        with zipfile.ZipFile(archive) as bundle:
            for member in bundle.namelist():
                if member.endswith("/") or Path(member).suffix.lower() not in TEXT_SUFFIXES:
                    continue
                if member.endswith("scripts/privacy_scan.py") or member.endswith("scripts/privacy_scan_history.py"):
                    continue
                findings.extend(scan_blob(f"{archive.name}:{member}", bundle.read(member), checks))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extra-term-file", type=Path)
    parser.add_argument("--archives", type=Path)
    args = parser.parse_args()
    checks = patterns(args.extra_term_file)
    findings = scan_history(checks)
    if args.archives:
        findings.extend(scan_archives(args.archives, checks))
    if findings:
        print("\n".join(sorted(set(findings))), file=sys.stderr)
        return 1
    print("Git history and release archive privacy scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
