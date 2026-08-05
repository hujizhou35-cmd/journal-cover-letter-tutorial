#!/usr/bin/env python3
"""Create an expert-free, allowlisted manifest for a fresh generator context."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Any

FORBIDDEN_TOKENS = ("expert", "benchmark", "teacher")


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _contains_forbidden_token(value: Any) -> bool:
    serialized = json.dumps(value, ensure_ascii=False).casefold()
    return any(token in serialized for token in FORBIDDEN_TOKENS)


def _is_safe_relative(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    path = PurePosixPath(value.replace("\\", "/"))
    return not path.is_absolute() and ".." not in path.parts


def prepare(
    data: dict[str, Any],
    case_id: str,
    round_id: str,
    skill_version: str,
) -> dict[str, Any]:
    cases = data.get("cases", [])
    case = next(
        (item for item in cases if isinstance(item, dict) and item.get("id") == case_id),
        None,
    )
    if case is None:
        raise ValueError(f"unknown case id: {case_id}")

    target = data.get("target_skill")
    if not isinstance(target, dict):
        raise ValueError("target_skill must be an object")

    manuscript_paths = case.get("manuscript_paths")
    journal_paths = case.get("journal_context_paths", [])
    if not isinstance(manuscript_paths, list) or not manuscript_paths:
        raise ValueError("case must contain manuscript_paths")
    if not isinstance(journal_paths, list):
        raise ValueError("journal_context_paths must be a list")
    allowlisted_paths = [target.get("path"), *manuscript_paths, *journal_paths]
    if any(not _is_safe_relative(path) for path in allowlisted_paths):
        raise ValueError("all generator input paths must be safe relative paths")

    packet = {
        "packet_schema_version": "1.0",
        "run_id": data.get("run_id"),
        "round_id": round_id,
        "case_id": case_id,
        "target_route": data.get("target_route"),
        "target_skill": {
            "name": target.get("name"),
            "version": skill_version,
            "path": target.get("path"),
        },
        "article_type": case.get("article_type"),
        "manuscript_paths": manuscript_paths,
        "journal_context_mode": case.get("journal_context_mode"),
        "journal_context_paths": journal_paths,
        "author_confirmations": case.get("author_confirmations", {}),
        "input_allowlist": allowlisted_paths,
        "context_contract": {
            "fresh_context_required": True,
            "inherited_conversation_allowed": False,
            "ambient_memory_or_project_scope_must_be_checked": True,
            "read_only_allowlisted_inputs": True,
        },
    }
    if _contains_forbidden_token(packet):
        raise ValueError(
            "generator packet contains a forbidden reference token; rename or remove the affected input"
        )
    return packet


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--round-id", required=True)
    parser.add_argument("--skill-version", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    if args.output.exists():
        raise SystemExit(f"refusing to overwrite sealed packet: {args.output}")
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    packet = prepare(data, args.case_id, args.round_id, args.skill_version)
    payload = (json.dumps(packet, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": _sha256_bytes(payload),
                "allowlisted_inputs": len(packet["input_allowlist"]),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
