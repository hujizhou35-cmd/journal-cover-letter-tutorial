#!/usr/bin/env python3
"""Validate structured cover-letter payloads without judging scientific meaning."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

STATUSES = {
    "SUBMISSION_READY",
    "NEEDS_AUTHOR_CONFIRMATION",
    "NEEDS_JOURNAL_VERIFICATION",
    "BEST_SAFE_DRAFT_WITH_UNRESOLVED_ITEMS",
}
REQUIRED = {
    "salutation",
    "paragraphs",
    "signoff",
    "corresponding_author",
    "status",
    "article_type",
    "submission_branch",
    "fact_status",
    "previous_letter_permission",
    "journal_conversation",
    "controlled_uplift_level",
    "hard_gate_failures",
    "quality_gate_failures",
    "stop_reason",
}
ARTICLE_TYPES = {"ORIGINAL_RESEARCH", "REVIEW_SYNTHESIS", "OTHER_OR_UNRESOLVED"}
PERMISSIONS = {
    "FORMAT_ONLY",
    "FORMAT_AND_TONE",
    "MAXIMUM_SUITABLE_WORDING",
    "FACT_CHECK_ONLY",
    "ANONYMOUS_EXPERT_BENCHMARK",
    "NONE",
}
FACT_STATUSES = {"verified", "conflict", "missing"}
UPLIFT_LEVELS = {"0_MINIMAL", "1_CALIBRATED", "2_ASSERTIVE"}
STOP_REASONS = {
    "ALL_GATES_PASSED",
    "AUTHOR_CONFIRMATION_REQUIRED",
    "JOURNAL_VERIFICATION_REQUIRED",
    "LOOP_LIMIT_WITH_UNRESOLVED_ITEMS",
    "DIMINISHING_RETURNS",
}


def validate(payload: dict) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED - payload.keys())
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if not isinstance(payload.get("paragraphs"), list) or not payload.get("paragraphs"):
        errors.append("paragraphs must be a non-empty list")
    elif any(not isinstance(item, str) or not item.strip() for item in payload["paragraphs"]):
        errors.append("every paragraph must be a non-empty string")
    if payload.get("status") not in STATUSES:
        errors.append("status must be one of: " + ", ".join(sorted(STATUSES)))
    if payload.get("article_type") not in ARTICLE_TYPES:
        errors.append("article_type must be one of: " + ", ".join(sorted(ARTICLE_TYPES)))
    if payload.get("previous_letter_permission") not in PERMISSIONS:
        errors.append("previous_letter_permission must be one of: " + ", ".join(sorted(PERMISSIONS)))
    if payload.get("fact_status") not in FACT_STATUSES:
        errors.append("fact_status must be verified, conflict, or missing")
    if payload.get("controlled_uplift_level") not in UPLIFT_LEVELS:
        errors.append("controlled_uplift_level is invalid")
    if payload.get("stop_reason") not in STOP_REASONS:
        errors.append("stop_reason is invalid")
    for field in ("hard_gate_failures", "quality_gate_failures"):
        if not isinstance(payload.get(field), list):
            errors.append(f"{field} must be a list")
    article_type = payload.get("article_type")
    if article_type == "ORIGINAL_RESEARCH" and not str(payload.get("selected_story_angle", "")).strip():
        errors.append("selected_story_angle is required for ORIGINAL_RESEARCH")
    if article_type == "REVIEW_SYNTHESIS":
        if not str(payload.get("editorial_thesis", "")).strip():
            errors.append("editorial_thesis is required for REVIEW_SYNTHESIS")
        if not str(payload.get("synthesis_intervention", "")).strip():
            errors.append("synthesis_intervention is required for REVIEW_SYNTHESIS")
    if payload.get("status") == "SUBMISSION_READY":
        if payload.get("fact_status") != "verified":
            errors.append("SUBMISSION_READY requires verified facts")
        if payload.get("hard_gate_failures"):
            errors.append("SUBMISSION_READY requires no hard gate failures")
        if payload.get("stop_reason") != "ALL_GATES_PASSED":
            errors.append("SUBMISSION_READY requires ALL_GATES_PASSED")
        if not str(payload.get("journal_conversation", "")).strip():
            errors.append("SUBMISSION_READY requires verified journal conversation or reader relevance")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("payload", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.payload.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        result = {"valid": False, "errors": [str(exc)]}
    else:
        errors = validate(payload)
        result = {"valid": not errors, "errors": errors}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
