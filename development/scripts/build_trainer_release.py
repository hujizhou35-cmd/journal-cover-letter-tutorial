#!/usr/bin/env python3
"""Build the three standalone Trainer release assets from a public Git tag."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUBLIC_TO_SEMVER = {"trainer-v0.2.0": "0.2.0"}
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def add_bytes(bundle: zipfile.ZipFile, data: bytes, archive_name: str) -> None:
    info = zipfile.ZipInfo(archive_name.replace("\\", "/"), date_time=FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    bundle.writestr(info, data)


def skill_files(skill_root: Path):
    return sorted(
        path
        for path in skill_root.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
        and path.name not in {"README.md", "CHANGELOG.md"}
    )


def build_skill(skill_root: Path, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for source in skill_files(skill_root):
            add_bytes(bundle, source.read_bytes(), source.relative_to(skill_root).as_posix())


def plugin_manifest(version: str) -> bytes:
    manifest = {
        "name": "journal-cover-letter-skill-trainer",
        "version": version,
        "description": "Improves the Journal Cover Letter Skill by comparing blind AI drafts with permitted expert letters.",
        "author": {"name": "Jizhou Hu", "url": "https://github.com/hujizhou35-cmd"},
        "homepage": "https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial",
        "repository": "https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial",
        "license": "MIT",
        "keywords": ["agent-skills", "benchmarking", "cover-letter", "skill-development"],
        "skills": "./skills/",
        "interface": {
            "displayName": "Cover Letter Skill Trainer",
            "shortDescription": "Improve a cover-letter Skill from expert examples.",
            "longDescription": "Generates a blind baseline, compares it with a permitted expert letter, extracts reusable rules, and tests a revised Skill in fresh contexts.",
            "developerName": "Jizhou Hu",
            "category": "Productivity",
            "capabilities": ["Research", "Write"],
            "defaultPrompt": "Use my current Skill and permitted manuscript-letter cases to build and test an improved version.",
        },
    }
    return (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def build_plugin(skill_root: Path, version: str, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        add_bytes(bundle, plugin_manifest(version), ".codex-plugin/plugin.json")
        for source in skill_files(skill_root):
            relative = source.relative_to(skill_root).as_posix()
            add_bytes(bundle, source.read_bytes(), f"skills/journal-cover-letter-skill-trainer/{relative}")


def build_portable(skill_root: Path, destination: Path) -> None:
    sections = [(skill_root / "SKILL.md").read_text(encoding="utf-8").rstrip()]
    sections.append(
        "\n\n# Inlined reference material\n\n"
        "This portable file contains the Trainer's decision and evaluation references. "
        "Deterministic validation scripts remain available in the Skill and Plugin packages."
    )
    for source in sorted((skill_root / "references").glob("*.md")):
        sections.append(f"\n\n---\n\n## Reference: {source.name}\n\n")
        sections.append(source.read_text(encoding="utf-8").rstrip())
    destination.write_text("".join(sections) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", required=True, choices=sorted(PUBLIC_TO_SEMVER))
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "release-assets")
    args = parser.parse_args()
    version = PUBLIC_TO_SEMVER[args.ref]
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="journal-cover-letter-trainer-") as raw:
        temp = Path(raw)
        source_zip = temp / "source.zip"
        subprocess.run(["git", "archive", "--format=zip", "-o", str(source_zip), args.ref], cwd=ROOT, check=True)
        source = temp / "source"
        source.mkdir()
        with zipfile.ZipFile(source_zip) as bundle:
            bundle.extractall(source)
        skill_root = source / "skills" / "journal-cover-letter-skill-trainer"
        if not (skill_root / "SKILL.md").exists():
            raise SystemExit(f"{args.ref} does not contain the Trainer Skill")

        skill_out = output / f"journal-cover-letter-skill-trainer-v{version}.skill"
        plugin_out = output / f"journal-cover-letter-skill-trainer-plugin-v{version}.zip"
        portable_out = output / "SKILL.md"
        build_skill(skill_root, skill_out)
        build_plugin(skill_root, version, plugin_out)
        build_portable(skill_root, portable_out)

    result = {
        path.name: {"sha256": sha256(path), "bytes": path.stat().st_size}
        for path in (skill_out, plugin_out, portable_out)
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
