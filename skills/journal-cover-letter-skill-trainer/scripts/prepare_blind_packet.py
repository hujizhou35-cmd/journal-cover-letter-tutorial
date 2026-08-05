#!/usr/bin/env python3
"""Create anonymous copies of candidate outputs and a sealed identity map."""

from __future__ import annotations

import argparse
import json
import random
import shutil
from pathlib import Path


def prepare(
    entries: dict[str, Path], output_dir: Path, sealed_map_path: Path, seed: int
) -> dict[str, object]:
    if len(entries) < 2:
        raise ValueError("at least two outputs are required")
    if len(entries) > 26:
        raise ValueError("at most 26 outputs are supported")
    missing = [str(path) for path in entries.values() if not path.is_file()]
    if missing:
        raise ValueError(f"missing output files: {missing}")

    output_dir.mkdir(parents=True, exist_ok=True)
    if any(output_dir.iterdir()):
        raise ValueError("output directory must be empty")
    sealed_map_path.parent.mkdir(parents=True, exist_ok=True)
    if sealed_map_path.exists():
        raise ValueError("sealed identity map already exists")
    try:
        sealed_map_path.resolve().relative_to(output_dir.resolve())
    except ValueError:
        pass
    else:
        raise ValueError("sealed identity map must be outside the judge packet directory")

    identities = list(entries.items())
    random.Random(seed).shuffle(identities)
    judge_outputs = []
    sealed_map: dict[str, dict[str, str]] = {}
    for index, (identity, source) in enumerate(identities):
        alias = chr(ord("A") + index)
        suffix = source.suffix.lower() or ".txt"
        neutral_name = f"{alias}{suffix}"
        destination = output_dir / neutral_name
        shutil.copyfile(source, destination)
        judge_outputs.append({"alias": alias, "file": neutral_name})
        sealed_map[alias] = {"identity": identity, "source": str(source.resolve())}

    judge_manifest = {"outputs": judge_outputs, "identity_disclosed": False}
    (output_dir / "judge_manifest.json").write_text(
        json.dumps(judge_manifest, indent=2), encoding="utf-8"
    )
    sealed_map_path.write_text(
        json.dumps({"seed": seed, "map": sealed_map}, indent=2), encoding="utf-8"
    )
    return {"judge_manifest": judge_manifest, "sealed_map": sealed_map}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--sealed-map", type=Path, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument(
        "--entry",
        action="append",
        required=True,
        help="identity=path, for example baseline=baseline.txt",
    )
    args = parser.parse_args()

    entries: dict[str, Path] = {}
    for raw in args.entry:
        if "=" not in raw:
            raise SystemExit(f"invalid --entry: {raw}")
        identity, path = raw.split("=", 1)
        if not identity or identity in entries:
            raise SystemExit(f"duplicate or empty identity: {identity}")
        entries[identity] = Path(path)

    result = prepare(entries, args.output_dir, args.sealed_map, args.seed)
    print(json.dumps(result["judge_manifest"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
