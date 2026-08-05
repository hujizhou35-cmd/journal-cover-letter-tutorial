#!/usr/bin/env python3
"""Aggregate explicit promotion gates without making subjective judgments."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _baseline_comparison_passes(data: dict[str, Any]) -> bool:
    judgments = data.get("candidate_vs_baseline", [])
    if not isinstance(judgments, list) or not judgments:
        return False
    winners = [item.get("winner") for item in judgments if isinstance(item, dict)]
    if len(winners) >= 3:
        candidate_wins = winners.count("candidate")
        ties = winners.count("tie")
        return candidate_wins >= 2 or (
            ties >= 2 and float(data.get("median_rubric_delta", -999)) >= 0
        )
    return bool(data.get("human_quality_review_passed"))


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    isolation = data.get("isolation_level")
    valid_isolation_levels = {
        "STRICT_AGENT_ISOLATED",
        "FRESH_CONTEXT_BLIND_GENERATION",
        "HUMAN_GATED_REVEAL",
        "PROCEDURAL_DELAYED_READ",
        "REFERENCE_CONTAMINATED",
    }
    hard_failures = data.get("hard_gate_failures", [])
    if hard_failures:
        failures.append("hard_gate_failures")
    if data.get("case_specific_leakage", False):
        failures.append("case_specific_leakage")
    if not data.get("protected_routes_passed", False):
        failures.append("protected_route_regression")
    if not data.get("expert_benchmark_passed", False):
        failures.append("expert_benchmark_not_met_or_explained")
    if isolation not in valid_isolation_levels:
        failures.append("invalid_isolation_level")

    if failures:
        return {
            "eligible": False,
            "stop_reason": (
                "BLOCKED_HARD_GATE"
                if hard_failures
                else "INVALID_ISOLATION"
                if "invalid_isolation_level" in failures
                else "DIMINISHING_RETURNS"
            ),
            "promotion_decision": "REJECTED_OR_REVISE",
            "failures": failures,
        }

    if isolation == "REFERENCE_CONTAMINATED":
        return {
            "eligible": False,
            "stop_reason": "REFERENCE_CONTAMINATED",
            "promotion_decision": "CANDIDATE_ONLY",
            "failures": ["reference_contaminated"],
        }

    if not _baseline_comparison_passes(data):
        return {
            "eligible": False,
            "stop_reason": "DIMINISHING_RETURNS",
            "promotion_decision": "REJECTED_OR_REVISE",
            "failures": ["candidate_did_not_beat_or_tie_baseline"],
        }

    if not data.get("holdout_available", False):
        return {
            "eligible": False,
            "stop_reason": "INSUFFICIENT_HOLDOUT",
            "promotion_decision": "CANDIDATE_ONLY",
            "failures": ["holdout_missing"],
        }
    if not data.get("holdout_passed", False):
        return {
            "eligible": False,
            "stop_reason": "DIMINISHING_RETURNS",
            "promotion_decision": "REJECTED_OR_REVISE",
            "failures": ["holdout_failed"],
        }

    human_approved = bool(data.get("human_approved", False))
    isolation_needs_override = isolation in {
        "HUMAN_GATED_REVEAL",
        "PROCEDURAL_DELAYED_READ",
    }
    if (
        isolation == "FRESH_CONTEXT_BLIND_GENERATION"
        and not data.get("fresh_context_evidence_passed", False)
    ):
        isolation_needs_override = True

    if isolation_needs_override:
        if not data.get("human_isolation_override", False):
            return {
                "eligible": True,
                "stop_reason": "CONTEXT_ISOLATION_INCOMPLETE",
                "promotion_decision": "HUMAN_ISOLATION_OVERRIDE_REQUIRED",
                "failures": ["isolation_evidence_incomplete"],
            }
        return {
            "eligible": human_approved,
            "stop_reason": "CONTEXT_ISOLATION_INCOMPLETE",
            "promotion_decision": (
                "PROMOTED_WITH_HUMAN_ISOLATION_OVERRIDE"
                if human_approved
                else "PROMOTION_RECOMMENDED"
            ),
            "failures": ["isolation_evidence_incomplete"],
        }

    return {
        "eligible": True,
        "stop_reason": "PROMOTION_GATES_PASSED",
        "promotion_decision": (
            "PROMOTED_WITH_HUMAN_APPROVAL" if human_approved else "PROMOTION_RECOMMENDED"
        ),
        "failures": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    data = json.loads(args.result.read_text(encoding="utf-8"))
    print(json.dumps(evaluate(data), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
