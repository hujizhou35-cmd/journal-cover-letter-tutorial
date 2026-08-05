#!/usr/bin/env python3
"""Validate evidence for fresh-context blind generation rounds."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

CONTEXT_MODES = {
    "FRESH_TEMPORARY_CONVERSATION",
    "NEW_API_CONVERSATION",
    "HOST_ISOLATED_WORKER",
}
MEMORY_BOUNDARIES = {"DISABLED_OR_SEPARATE_SCOPE", "HOST_MANAGED"}
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["context ledger must be a JSON object"]
    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if not isinstance(data.get("run_id"), str) or not data.get("run_id", "").strip():
        errors.append("run_id must be a non-empty string")

    rounds = data.get("rounds")
    if not isinstance(rounds, list) or not rounds:
        errors.append("rounds must be a non-empty list")
        return errors

    expected_entries = data.get("expected_entries")
    if not isinstance(expected_entries, list) or not expected_entries:
        errors.append("expected_entries must be a non-empty list")
        return errors
    expected_keys: set[tuple[str, str]] = set()
    for index, item in enumerate(expected_entries):
        if not isinstance(item, dict):
            errors.append(f"expected_entries[{index}] must be an object")
            continue
        key = (str(item.get("round_id", "")), str(item.get("case_id", "")))
        if not all(key):
            errors.append(
                f"expected_entries[{index}] must contain non-empty round_id and case_id"
            )
        expected_keys.add(key)

    seen: set[tuple[str, str]] = set()
    for index, item in enumerate(rounds):
        prefix = f"rounds[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        round_id = item.get("round_id")
        case_id = item.get("case_id")
        if not isinstance(round_id, str) or not round_id.strip():
            errors.append(f"{prefix}.round_id must be a non-empty string")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{prefix}.case_id must be a non-empty string")
        key = (str(round_id), str(case_id))
        if key in seen:
            errors.append(f"duplicate round/case entry: {key[0]} / {key[1]}")
        seen.add(key)

        if item.get("context_mode") not in CONTEXT_MODES:
            errors.append(f"{prefix}.context_mode must be one of {sorted(CONTEXT_MODES)}")
        if item.get("memory_or_project_boundary") not in MEMORY_BOUNDARIES:
            errors.append(
                f"{prefix}.memory_or_project_boundary must be one of {sorted(MEMORY_BOUNDARIES)}"
            )
        if item.get("custom_instructions_checked") is not True:
            errors.append(f"{prefix}.custom_instructions_checked must be true")
        if item.get("inherited_evaluator_history") is not False:
            errors.append(f"{prefix}.inherited_evaluator_history must be false")
        if item.get("benchmark_material_present") is not False:
            errors.append(f"{prefix}.benchmark_material_present must be false")
        for field in ("generator_packet_sha256", "output_sha256"):
            if not isinstance(item.get(field), str) or not SHA256.fullmatch(item[field]):
                errors.append(f"{prefix}.{field} must be a lowercase SHA-256 hex digest")
        for field in ("generator_context_id", "sealed_at", "verified_by"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{prefix}.{field} must be a non-empty string")
    if seen != expected_keys:
        missing = sorted(expected_keys - seen)
        unexpected = sorted(seen - expected_keys)
        if missing:
            errors.append(f"missing expected round/case entries: {missing}")
        if unexpected:
            errors.append(f"unexpected round/case entries: {unexpected}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()
    data = json.loads(args.ledger.read_text(encoding="utf-8"))
    errors = validate(data)
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
