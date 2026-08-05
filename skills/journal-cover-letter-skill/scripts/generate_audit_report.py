#!/usr/bin/env python3
"""Convert a validated payload and deterministic letter audit into Markdown."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("payload", type=Path)
    parser.add_argument("letter_audit", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.payload.read_text(encoding="utf-8"))
    audit = json.loads(args.letter_audit.read_text(encoding="utf-8"))
    lines = [
        "# Cover Letter Audit",
        "",
        f"- Final status: `{payload.get('status', 'UNKNOWN')}`",
        f"- Article type: `{payload.get('article_type', 'UNKNOWN')}`",
        f"- Submission branch: `{payload.get('submission_branch', 'UNKNOWN')}`",
        f"- Fact status: `{payload.get('fact_status', 'UNKNOWN')}`",
        f"- Previous-letter permission: `{payload.get('previous_letter_permission', 'UNKNOWN')}`",
        f"- Confirmation mode: `{payload.get('confirmation_mode', 'NOT_RECORDED')}`",
        f"- Journal-fit basis: `{payload.get('journal_fit_basis', 'NOT_RECORDED')}`",
        f"- Controlled uplift: `{payload.get('controlled_uplift_level', 'UNKNOWN')}`",
        f"- Stop reason: `{payload.get('stop_reason', 'UNKNOWN')}`",
        "",
        "## Hard gate failures",
        "",
    ]
    failures = payload.get("hard_gate_failures") or []
    lines.extend([f"- {item}" for item in failures] or ["- None"])
    lines.extend(["", "## Quality gate failures", ""])
    quality = payload.get("quality_gate_failures") or []
    lines.extend([f"- {item}" for item in quality] or ["- None"])
    lines.extend(["", "## Deterministic letter checks", ""])
    lines.append(f"- Placeholders: {len(audit.get('placeholders', []))}")
    lines.append(f"- Structural failures: {len(audit.get('structural_failures', []))}")
    lines.append(f"- Risk-language categories requiring semantic review: {', '.join(audit.get('high_risk_language_for_semantic_review', {}).keys()) or 'None'}")
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
