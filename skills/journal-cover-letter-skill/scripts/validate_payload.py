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
REQUIRED = {"salutation", "paragraphs", "signoff", "corresponding_author", "status"}


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
