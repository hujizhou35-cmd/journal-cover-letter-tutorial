#!/usr/bin/env python3
"""Validate a Journal Cover Letter Skill Trainer manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
from typing import Any

TRAINING_INTENTS = {"STRENGTHEN_EXISTING_ROUTE", "PROPOSE_NEW_ROUTE"}
STORAGE_MODES = {"SESSION_ONLY", "LOCAL_PRIVATE_CORPUS"}
SCHEMA_VERSIONS = {"1.0", "1.1"}
ISOLATION_LEVELS = {
    "STRICT_AGENT_ISOLATED",
    "FRESH_CONTEXT_BLIND_GENERATION",
    "HUMAN_GATED_REVEAL",
    "PROCEDURAL_DELAYED_READ",
    "REFERENCE_CONTAMINATED",
}
CONTEXT_MEMORY_POLICIES = {
    "DISABLED_OR_SEPARATE_SCOPE",
    "HOST_MANAGED",
    "UNKNOWN",
}
CASE_ROLES = {"TRAIN", "HOLDOUT", "REGRESSION"}
JOURNAL_MODES = {"CURRENT_LIVE", "CAPTURED_AS_OF_SUBMISSION", "NOT_SCORED"}


def _is_safe_relative(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    normalized = value.replace("\\", "/")
    path = PurePosixPath(normalized)
    return not path.is_absolute() and ".." not in path.parts


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["manifest must be a JSON object"]

    if data.get("schema_version") not in SCHEMA_VERSIONS:
        errors.append(f"schema_version must be one of {sorted(SCHEMA_VERSIONS)}")
    if not isinstance(data.get("run_id"), str) or not data.get("run_id", "").strip():
        errors.append("run_id must be a non-empty string")

    target = data.get("target_skill")
    if not isinstance(target, dict):
        errors.append("target_skill must be an object")
    else:
        if target.get("name") != "journal-cover-letter-skill":
            errors.append("target_skill.name must be journal-cover-letter-skill")
        if not isinstance(target.get("version"), str) or not target.get("version", "").strip():
            errors.append("target_skill.version must be a non-empty string")
        if not _is_safe_relative(target.get("path")):
            errors.append("target_skill.path must be a safe relative path")

    if data.get("training_intent") not in TRAINING_INTENTS:
        errors.append(f"training_intent must be one of {sorted(TRAINING_INTENTS)}")
    if not isinstance(data.get("target_route"), str) or not data.get("target_route", "").strip():
        errors.append("target_route must be a non-empty string")
    if data.get("storage_mode") not in STORAGE_MODES:
        errors.append(f"storage_mode must be one of {sorted(STORAGE_MODES)}")
    if data.get("requested_isolation") not in ISOLATION_LEVELS:
        errors.append(f"requested_isolation must be one of {sorted(ISOLATION_LEVELS)}")
    memory_policy = data.get("context_memory_policy", "UNKNOWN")
    if memory_policy not in CONTEXT_MEMORY_POLICIES:
        errors.append(
            f"context_memory_policy must be one of {sorted(CONTEXT_MEMORY_POLICIES)}"
        )
    if (
        data.get("requested_isolation") == "FRESH_CONTEXT_BLIND_GENERATION"
        and memory_policy not in {"DISABLED_OR_SEPARATE_SCOPE", "HOST_MANAGED"}
    ):
        errors.append(
            "FRESH_CONTEXT_BLIND_GENERATION requires context_memory_policy "
            "DISABLED_OR_SEPARATE_SCOPE or HOST_MANAGED"
        )
    if data.get("promotion_policy") != "HUMAN_APPROVAL":
        errors.append("promotion_policy must be HUMAN_APPROVAL")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("cases must be a non-empty list")
        return errors

    seen_ids: set[str] = set()
    train_count = 0
    for index, case in enumerate(cases):
        prefix = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{prefix}.id must be a non-empty string")
        elif case_id in seen_ids:
            errors.append(f"duplicate case id: {case_id}")
        else:
            seen_ids.add(case_id)

        role = case.get("role")
        if role not in CASE_ROLES:
            errors.append(f"{prefix}.role must be one of {sorted(CASE_ROLES)}")
        if role == "TRAIN":
            train_count += 1

        manuscript_paths = case.get("manuscript_paths")
        if not isinstance(manuscript_paths, list) or not manuscript_paths:
            errors.append(f"{prefix}.manuscript_paths must be a non-empty list")
        elif any(not _is_safe_relative(path) for path in manuscript_paths):
            errors.append(f"{prefix}.manuscript_paths must contain safe relative paths")

        expert_path = case.get("expert_letter_path")
        if expert_path is not None:
            if not _is_safe_relative(expert_path):
                errors.append(f"{prefix}.expert_letter_path must be a safe relative path")
            if case.get("benchmark_permission") != "ANONYMOUS_EXPERT_BENCHMARK":
                errors.append(
                    f"{prefix}.benchmark_permission must be ANONYMOUS_EXPERT_BENCHMARK when an expert letter is supplied"
                )
        elif role in {"TRAIN", "HOLDOUT"}:
            errors.append(f"{prefix}.expert_letter_path is required for {role} cases")

        if case.get("journal_context_mode") not in JOURNAL_MODES:
            errors.append(f"{prefix}.journal_context_mode must be one of {sorted(JOURNAL_MODES)}")
        journal_paths = case.get("journal_context_paths", [])
        if not isinstance(journal_paths, list) or any(not _is_safe_relative(path) for path in journal_paths):
            errors.append(f"{prefix}.journal_context_paths must contain safe relative paths")
        if not isinstance(case.get("author_confirmations", {}), dict):
            errors.append(f"{prefix}.author_confirmations must be an object")
        if not isinstance(case.get("sensitive_terms", []), list):
            errors.append(f"{prefix}.sensitive_terms must be a list")

    if train_count == 0:
        errors.append("at least one TRAIN case is required")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    errors = validate(data)
    result = {"valid": not errors, "errors": errors}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
