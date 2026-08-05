#!/usr/bin/env python3
"""Validate v3.1 structured cover-letter payloads without judging scientific meaning."""

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
    "salutation", "paragraphs", "signoff", "corresponding_author", "status",
    "official_article_type", "intellectual_route", "submission_branch", "fact_status",
    "previous_letter_permission", "empirical_anchor", "editorial_meaning",
    "journal_conversation", "controlled_uplift_level", "hard_gate_failures",
    "quality_gate_failures", "stop_reason",
}
ROUTES = {"ORIGINAL_RESEARCH", "REVIEW_SYNTHESIS", "BIBLIOMETRICS", "OTHER_OR_UNRESOLVED"}
PERMISSIONS = {
    "FORMAT_ONLY", "FORMAT_AND_TONE", "MAXIMUM_SUITABLE_WORDING",
    "FACT_CHECK_ONLY", "ANONYMOUS_EXPERT_BENCHMARK", "NONE",
}
FACT_STATUSES = {"verified", "conflict", "missing", "not_applicable"}
UPLIFT_LEVELS = {"0_MINIMAL", "1_CALIBRATED", "2_ASSERTIVE"}
CONFIRMATION_MODES = {"EXPLICIT_CONFIRMATION", "EVIDENCE_COMPLETE_FAST_PATH", "PENDING"}
JOURNAL_FIT_BASES = {"ARTICLE_TYPE_CRITERION", "READERSHIP_NEED", "CURRENT_CONVERSATION", "UNVERIFIED"}
BIBLIOMETRIC_MODES = {"PERFORMANCE_ANALYSIS", "SCIENCE_MAPPING", "BOTH"}
STOP_REASONS = {
    "ALL_GATES_PASSED", "AUTHOR_CONFIRMATION_REQUIRED", "JOURNAL_VERIFICATION_REQUIRED",
    "LOOP_LIMIT_WITH_UNRESOLVED_ITEMS", "DIMINISHING_RETURNS", "BENCHMARK_CONVERGENCE_REACHED",
}


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


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
        errors.append("status is invalid")
    if payload.get("intellectual_route") not in ROUTES:
        errors.append("intellectual_route is invalid")
    if not nonempty(payload.get("official_article_type")):
        errors.append("official_article_type must be a non-empty exact journal label or UNRESOLVED")
    if payload.get("previous_letter_permission") not in PERMISSIONS:
        errors.append("previous_letter_permission is invalid")
    if payload.get("fact_status") not in FACT_STATUSES:
        errors.append("fact_status is invalid")
    if payload.get("controlled_uplift_level") not in UPLIFT_LEVELS:
        errors.append("controlled_uplift_level is invalid")
    if payload.get("stop_reason") not in STOP_REASONS:
        errors.append("stop_reason is invalid")
    if "confirmation_mode" in payload and payload.get("confirmation_mode") not in CONFIRMATION_MODES:
        errors.append("confirmation_mode is invalid")
    if "journal_fit_basis" in payload and payload.get("journal_fit_basis") not in JOURNAL_FIT_BASES:
        errors.append("journal_fit_basis is invalid")

    for field in ("hard_gate_failures", "quality_gate_failures"):
        if not isinstance(payload.get(field), list):
            errors.append(f"{field} must be a list")

    for field in ("empirical_anchor", "editorial_meaning"):
        if not nonempty(payload.get(field)):
            errors.append(f"{field} must be a non-empty string")

    route = payload.get("intellectual_route")
    if route == "ORIGINAL_RESEARCH" and not nonempty(payload.get("research_decision_spine")):
        errors.append("research_decision_spine is required for ORIGINAL_RESEARCH")
    if route == "REVIEW_SYNTHESIS":
        if not nonempty(payload.get("editorial_thesis")):
            errors.append("editorial_thesis is required for REVIEW_SYNTHESIS")
        if not nonempty(payload.get("synthesis_intervention")):
            errors.append("synthesis_intervention is required for REVIEW_SYNTHESIS")
    if route == "BIBLIOMETRICS":
        if payload.get("bibliometric_mode") not in BIBLIOMETRIC_MODES:
            errors.append("bibliometric_mode is required and must be valid for BIBLIOMETRICS")
        for field in ("mapping_intervention", "mapping_thesis", "bibliometric_signature_packet", "authorial_specificity_floor", "bibliometric_decision_spine", "metric_boundary"):
            if not nonempty(payload.get(field)):
                errors.append(f"{field} is required for BIBLIOMETRICS")

    if payload.get("status") == "SUBMISSION_READY":
        if payload.get("fact_status") != "verified":
            errors.append("SUBMISSION_READY requires verified facts")
        if payload.get("hard_gate_failures"):
            errors.append("SUBMISSION_READY requires no hard gate failures")
        if payload.get("stop_reason") != "ALL_GATES_PASSED":
            errors.append("SUBMISSION_READY requires ALL_GATES_PASSED")
        if not nonempty(payload.get("journal_conversation")):
            errors.append("SUBMISSION_READY requires verified journal conversation or reader relevance")
        if str(payload.get("official_article_type", "")).strip().upper() == "UNRESOLVED":
            errors.append("SUBMISSION_READY requires a resolved official_article_type")
        if route == "OTHER_OR_UNRESOLVED":
            errors.append("SUBMISSION_READY requires a resolved intellectual_route")
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
