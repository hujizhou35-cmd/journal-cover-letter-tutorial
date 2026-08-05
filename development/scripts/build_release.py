#!/usr/bin/env python3
"""Build three deterministic release assets from a public Git tag."""

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
PUBLIC_TO_SEMVER = {
    "v1.0": "1.0.0",
    "v2.0": "2.0.0",
    "v2.1": "2.1.0",
    "v2.2": "2.2.0",
    "v2.3": "2.3.0",
    "v3.0": "3.0.0",
    "v3.1": "3.1.0",
    "v3.2": "3.2.0",
}
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def add_file(bundle: zipfile.ZipFile, source: Path, archive_name: str) -> None:
    info = zipfile.ZipInfo(archive_name.replace("\\", "/"), date_time=FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    bundle.writestr(info, source.read_bytes())


def archive_roots(destination: Path, roots: list[tuple[Path, str]]) -> None:
    entries: list[tuple[Path, str]] = []
    for source_root, archive_root in roots:
        for path in source_root.rglob("*"):
            if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                relative = path.relative_to(source_root).as_posix()
                name = f"{archive_root}/{relative}" if archive_root else relative
                entries.append((path, name))
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path, name in sorted(entries, key=lambda item: item[1]):
            add_file(bundle, path, name)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_portable_skill(skill_root: Path, ref: str, destination: Path) -> None:
    if ref == "v2.2":
        canonical = (skill_root / "SKILL.md").read_bytes().replace(b"\r\n", b"\n")
        destination.write_bytes(canonical)
        return

    main = (skill_root / "SKILL.md").read_text(encoding="utf-8").rstrip()
    sections = [
        main,
        "\n# Inlined reference material\n",
        "This portable file includes the reference documents used by this historical version. "
        "Executable DOCX and audit tools remain available only in the installation packages.\n",
    ]
    for reference in sorted((skill_root / "references").glob("*.md")):
        if reference.name.startswith("migration-"):
            continue
        sections.append(f"\n---\n\n## Reference: {reference.name}\n")
        sections.append(reference.read_text(encoding="utf-8").rstrip() + "\n")
    destination.write_text("\n".join(sections), encoding="utf-8")


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
        subprocess.run(
            ["git", "archive", "--format=zip", "-o", str(source_zip), args.ref],
            cwd=ROOT,
            check=True,
        )
        source = temp / "source"
        source.mkdir()
        with zipfile.ZipFile(source_zip) as bundle:
            bundle.extractall(source)

        manifest_path = source / ".codex-plugin" / "plugin.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("version") != expected:
            raise SystemExit(f"{args.ref} manifest is {manifest.get('version')}, expected {expected}")

        skill_root = source / "skills" / "journal-cover-letter-skill"
        skill_out = output / f"journal-cover-letter-skill-{args.ref}.skill"
        plugin_out = output / f"journal-cover-letter-plugin-{args.ref}.zip"
        portable_out = output / "SKILL.md"

        archive_roots(skill_out, [(skill_root, "")])
        archive_roots(
            plugin_out,
            [
                (source / ".codex-plugin", ".codex-plugin"),
                (skill_root, "skills/journal-cover-letter-skill"),
            ],
        )
        build_portable_skill(skill_root, args.ref, portable_out)

    result = {
        path.name: {"sha256": sha256(path), "bytes": path.stat().st_size}
        for path in (skill_out, plugin_out, portable_out)
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
