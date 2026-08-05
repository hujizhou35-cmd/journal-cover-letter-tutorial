#!/usr/bin/env python3
"""Deterministic structural and risk-language checks for a v3.2 draft letter."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PLACEHOLDER_PATTERNS = [r"\[[A-Za-z][^\]\n]{0,80}\]", r"\{\{[^}\n]+\}\}", r"\b(?:TODO|TBD|TK)\b"]
HIGH_RISK = {
    "causal": r"\b(?:causes?|causal effect|proves? causality)\b",
    "mechanism": r"\b(?:proves?|establishes?|confirms?) (?:the )?mechanism\b",
    "clinical": r"\b(?:should be implemented|clinical guidance|guarantees?)\b",
    "marketing": r"\b(?:groundbreaking|revolutionary|perfectly aligned|aligns perfectly|authoritative|ideal(?:ly)? suited)\b",
    "priority_claim": r"\b(?:the first|first-ever|only review|most comprehensive|unprecedented)\b",
    "generic_self_praise": r"\b(?:comprehensive synthesis|timely and authoritative|highly relevant)\b",
    "bibliometric_quality_equivalence": r"\b(?:highest quality|best research|most influential|scientific leadership|clinical leadership)\b",
    "bibliometric_forecast": r"\b(?:will dominate|will become|definitive future direction|certain future trend|predicts? the future)\b",
    "bibliometric_completeness": r"\b(?:complete landscape|complete map|entire field|all research in the field)\b",
    "bibliometric_causality": r"\b(?:centrality (?:causes?|drives?)|collaboration (?:causes?|proves?))\b",
    "submission_system_only": r"\b(?:agree to pay (?:the )?(?:apc|article processing charge)|opt(?:ing)? for open peer review|suggested reviewers?|publication fee willingness)\b",
}


def audit(text: str) -> dict:
    placeholders = sorted({m.group(0) for p in PLACEHOLDER_PATTERNS for m in re.finditer(p, text, re.I)})
    risks = {label: sorted({m.group(0) for m in re.finditer(pattern, text, re.I)}) for label, pattern in HIGH_RISK.items()}
    risks = {label: matches for label, matches in risks.items() if matches}
    structural = []
    if not re.search(r"\bDear\b", text, re.I):
        structural.append("missing salutation")
    if not re.search(r"\bSincerely\b|\bYours sincerely\b|\bKind regards\b", text, re.I):
        structural.append("missing signoff")
    return {
        "pass": not placeholders and not structural,
        "placeholders": placeholders,
        "high_risk_language_for_semantic_review": risks,
        "structural_failures": structural,
        "note": "High-risk terms require evidence review; their presence is not automatically an error.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("letter", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = audit(args.letter.read_text(encoding="utf-8"))
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
