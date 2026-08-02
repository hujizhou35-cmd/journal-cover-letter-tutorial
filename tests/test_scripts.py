from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "skills" / "journal-cover-letter-skill" / "scripts"


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPT_DIR / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_valid_payload():
    validator = load("validate_payload")
    payload = {
        "salutation": "Dear Editorial Team,",
        "paragraphs": ["Synthetic content."],
        "signoff": "Sincerely,",
        "corresponding_author": "Alex Morgan",
        "article_type": "ORIGINAL_RESEARCH",
        "previous_letter_permission": "NONE",
        "status": "SUBMISSION_READY",
    }
    assert validator.validate(payload) == []


def test_missing_payload_fields():
    validator = load("validate_payload")
    errors = validator.validate({"paragraphs": []})
    assert any("missing fields" in error for error in errors)
    assert any("non-empty" in error for error in errors)


def test_audit_detects_placeholder_and_risky_language():
    audit = load("audit_cover_letter")
    result = audit.audit("Dear Editor,\nThis groundbreaking study causes [OUTCOME].\nSincerely,")
    assert not result["pass"]
    assert result["placeholders"]
    assert "causal" in result["high_risk_language_for_semantic_review"]
    assert "marketing" in result["high_risk_language_for_semantic_review"]


def test_clean_synthetic_letter_passes_structure():
    audit = load("audit_cover_letter")
    result = audit.audit("Dear Editorial Team,\nThis synthetic study maps a pattern.\nSincerely,")
    assert result["pass"]
