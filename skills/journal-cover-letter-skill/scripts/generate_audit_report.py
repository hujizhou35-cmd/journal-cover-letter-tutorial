#!/usr/bin/env python3
"""Convert a validated v3.2 payload and deterministic letter audit into Markdown."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def add(lines: list[str], label: str, value: object) -> None:
    lines.append(f"- {label}: `{value if value not in (None, '') else 'NOT_RECORDED'}`")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("payload", type=Path)
    parser.add_argument("letter_audit", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.payload.read_text(encoding="utf-8"))
    audit = json.loads(args.letter_audit.read_text(encoding="utf-8"))
    lines = ["# Cover Letter Audit", ""]
    add(lines, "Final status", payload.get("status", "UNKNOWN"))
    add(lines, "Official article type", payload.get("official_article_type", "UNKNOWN"))
    add(lines, "Intellectual route", payload.get("intellectual_route", "UNKNOWN"))
    add(lines, "Submission branch", payload.get("submission_branch", "UNKNOWN"))
    add(lines, "Fact status", payload.get("fact_status", "UNKNOWN"))
    add(lines, "Previous-letter permission", payload.get("previous_letter_permission", "UNKNOWN"))
    add(lines, "Confirmation mode", payload.get("confirmation_mode"))
    add(lines, "Empirical anchor", payload.get("empirical_anchor"))
    add(lines, "Editorial meaning", payload.get("editorial_meaning"))
    add(lines, "Journal-fit basis", payload.get("journal_fit_basis"))
    add(lines, "Journal-fit bridge", payload.get("journal_fit_bridge"))
    add(lines, "Controlled uplift", payload.get("controlled_uplift_level", "UNKNOWN"))
    add(lines, "Stop reason", payload.get("stop_reason", "UNKNOWN"))
    if payload.get("intellectual_route") == "BIBLIOMETRICS":
        add(lines, "Bibliometric mode", payload.get("bibliometric_mode"))
        add(lines, "Mapping thesis", payload.get("mapping_thesis"))
        add(lines, "Metric boundary", payload.get("metric_boundary"))
    lines.extend(["", "## Hard gate failures", ""])
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
