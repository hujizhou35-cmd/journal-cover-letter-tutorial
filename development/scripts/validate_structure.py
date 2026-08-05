#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    ".codex-plugin/plugin.json",
    ".github/CONTRIBUTING.md",
    "skills/journal-cover-letter-skill/SKILL.md",
    "skills/journal-cover-letter-skill/agents/openai.yaml",
    "skills/journal-cover-letter-skill-trainer/SKILL.md",
    "skills/journal-cover-letter-skill-trainer/agents/openai.yaml",
    "skills/journal-cover-letter-skill-trainer/assets/training-manifest.example.json",
    "skills/journal-cover-letter-skill-trainer/assets/context-ledger.example.json",
    "skills/journal-cover-letter-skill-trainer/references/worker-prompts.md",
    "skills/journal-cover-letter-skill-trainer/scripts/validate_training_manifest.py",
    "skills/journal-cover-letter-skill-trainer/scripts/prepare_blind_packet.py",
    "skills/journal-cover-letter-skill-trainer/scripts/prepare_generator_packet.py",
    "skills/journal-cover-letter-skill-trainer/scripts/validate_context_ledger.py",
    "skills/journal-cover-letter-skill-trainer/scripts/evaluate_promotion.py",
    "README.md",
    "docs/README.zh-CN.md",
    "docs/privacy.md",
    "docs/evolution.md",
    "docs/evolution.zh-CN.md",
    "docs/changelog.md",
    "docs/trainer-changelog.md",
    "docs/trainer-guide.md",
    "docs/trainer-guide.zh-CN.md",
    "development/examples/synthetic/cases.json",
    "development/evals/evals.json",
    "development/evals/trainer-evals.json",
    "development/tests/test_scripts.py",
    "LICENSE",
    "CITATION.cff",
]


def main() -> int:
    missing = [item for item in REQUIRED if not (ROOT / item).exists()]
    manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    errors = []
    if manifest.get("name") != "journal-cover-letter-skill":
        errors.append("plugin name must match the Skill")
    if manifest.get("skills") != "./skills/":
        errors.append("plugin manifest must point to ./skills/")
    if manifest.get("version") != "3.2.0":
        errors.append("main must contain plugin version 3.2.0")
    if manifest.get("author", {}).get("name") != "Jizhou Hu":
        errors.append("authorized public author metadata is missing")
    if manifest.get("repository") != "https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial":
        errors.append("repository URL is stale")
    errors.extend(f"missing: {item}" for item in missing)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Repository structure is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
