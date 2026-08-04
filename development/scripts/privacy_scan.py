#!/usr/bin/env python3
"""Fail on secrets, private-material patterns, or prohibited benchmark wording."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXT_EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".toml", ".cff", ".html"}
PATTERNS = {
    "credential": re.compile(r"(?:ghp_|github_pat_|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})"),
    "private email": re.compile(r"(?i)\b(?!contact@example\.invalid\b)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"),
    "prohibited benchmark wording": re.compile(r"(?i)\bteacher[- ](?:written|authored|style)|teacher's cover letter\b"),
}


def tracked_files() -> list[Path]:
    try:
        output = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True, encoding="utf-8")
        names = [line for line in output.splitlines() if line]
    except (subprocess.CalledProcessError, FileNotFoundError):
        names = [
            str(path.relative_to(ROOT))
            for path in ROOT.rglob("*")
            if path.is_file() and not any(part in {".git", ".venv", "dist", "build", "tmp", ".tmp"} for part in path.parts)
        ]
    return [ROOT / name for name in names]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extra-term-file", type=Path)
    args = parser.parse_args()
    patterns = dict(PATTERNS)
    if args.extra_term_file and args.extra_term_file.exists():
        for index, term in enumerate(args.extra_term_file.read_text(encoding="utf-8").splitlines()):
            if term.strip():
                patterns[f"local sensitive term {index + 1}"] = re.compile(re.escape(term.strip()), re.I)
    findings: list[str] = []
    for path in tracked_files():
        if path.name in {"privacy_scan.py", "privacy_scan_history.py"} and path.parent.name == "scripts":
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS or not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in patterns.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{path.relative_to(ROOT)}:{line}: {label}")
    if findings:
        print("\n".join(findings), file=sys.stderr)
        return 1
    print("Privacy scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
