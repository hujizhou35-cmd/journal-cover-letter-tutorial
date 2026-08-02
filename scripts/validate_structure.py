#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ".codex-plugin/plugin.json",
    "skills/journal-cover-letter-skill/SKILL.md",
    "skills/journal-cover-letter-skill/agents/openai.yaml",
    "README.md",
    "README.zh-CN.md",
    "PRIVACY.md",
    "LICENSE",
    "CHANGELOG.md",
    "CITATION.cff",
    "docs/evolution.md",
    "docs/architecture.md",
    "docs/specs/v1.0-product-spec.md",
    "docs/specs/v2.0-product-spec.md",
    "docs/specs/v2.1-product-spec.md",
    "examples/synthetic/cases.json",
    "evals/evals.json",
]


def main() -> int:
    missing = [item for item in REQUIRED if not (ROOT / item).exists()]
    manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    errors = []
    if manifest.get("name") != "journal-cover-letter-skill":
        errors.append("plugin name must match the repository/plugin directory")
    if "skills" not in manifest:
        errors.append("plugin manifest must declare skills")
    if manifest.get("version") not in {"1.0.0", "2.0.0", "2.1.0"}:
        errors.append("plugin version must be a released semantic version")
    if manifest.get("author", {}).get("name") != "Jizhou Hu":
        errors.append("authorized public author metadata is missing")
    errors.extend(f"missing: {item}" for item in missing)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Repository structure is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
