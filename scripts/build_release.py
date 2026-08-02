#!/usr/bin/env python3
"""Build deterministic standalone Skill and Plugin archives from a Git ref."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_TO_SEMVER = {"v1.0": "1.0.0", "v2.0": "2.0.0", "v2.1": "2.1.0"}


def archive_tree(source: Path, destination: Path, prefix: str) -> None:
    files = sorted(path for path in source.rglob("*") if path.is_file())
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in files:
            relative = path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(f"{prefix}/{relative}", date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, path.read_bytes())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", required=True, choices=sorted(PUBLIC_TO_SEMVER))
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    expected = PUBLIC_TO_SEMVER[args.ref]
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="journal-cover-letter-release-") as raw:
        temp = Path(raw)
        source_zip = temp / "source.zip"
        subprocess.run(["git", "archive", "--format=zip", "-o", str(source_zip), args.ref], cwd=ROOT, check=True)
        source = temp / "source"
        source.mkdir()
        with zipfile.ZipFile(source_zip) as bundle:
            bundle.extractall(source)
        manifest = json.loads((source / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        if manifest.get("version") != expected:
            raise SystemExit(f"{args.ref} manifest is {manifest.get('version')}, expected {expected}")

        skill_name = f"journal-cover-letter-skill-{args.ref}.skill"
        plugin_name = f"journal-cover-letter-plugin-{args.ref}.zip"
        skill_out = output / skill_name
        plugin_out = output / plugin_name
        archive_tree(source / "skills" / "journal-cover-letter-skill", skill_out, "journal-cover-letter-skill")
        archive_tree(source, plugin_out, "journal-cover-letter-skill")
        sums = output / "SHA256SUMS.txt"
        sums.write_text(
            f"{sha256(skill_out)}  {skill_name}\n{sha256(plugin_out)}  {plugin_name}\n",
            encoding="ascii",
        )
    print(skill_out)
    print(plugin_out)
    print(sums)
    return 0


if __name__ == "__main__":
    sys.exit(main())
