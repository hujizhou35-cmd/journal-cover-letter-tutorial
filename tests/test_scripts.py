from __future__ import annotations

import importlib.util
import zipfile
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
        "submission_branch": "INITIAL_SUBMISSION",
        "fact_status": "verified",
        "previous_letter_permission": "NONE",
        "selected_story_angle": "A synthetic story angle.",
        "journal_conversation": "A synthetic journal conversation.",
        "controlled_uplift_level": "1_CALIBRATED",
        "hard_gate_failures": [],
        "quality_gate_failures": [],
        "stop_reason": "ALL_GATES_PASSED",
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


def test_review_requires_thesis_and_intervention():
    validator = load("validate_payload")
    payload = {
        "salutation": "Dear Editorial Team,",
        "paragraphs": ["Synthetic review."],
        "signoff": "Sincerely,",
        "corresponding_author": "Alex Morgan",
        "article_type": "REVIEW_SYNTHESIS",
        "submission_branch": "INITIAL_SUBMISSION",
        "fact_status": "verified",
        "previous_letter_permission": "NONE",
        "journal_conversation": "Synthetic conversation.",
        "controlled_uplift_level": "1_CALIBRATED",
        "hard_gate_failures": [],
        "quality_gate_failures": [],
        "stop_reason": "ALL_GATES_PASSED",
        "status": "SUBMISSION_READY",
    }
    errors = validator.validate(payload)
    assert "editorial_thesis is required for REVIEW_SYNTHESIS" in errors
    assert "synthesis_intervention is required for REVIEW_SYNTHESIS" in errors


def test_submission_ready_rejects_unresolved_hard_gate():
    validator = load("validate_payload")
    payload = {
        "salutation": "Dear Editorial Team,",
        "paragraphs": ["Synthetic draft."],
        "signoff": "Sincerely,",
        "corresponding_author": "Alex Morgan",
        "article_type": "ORIGINAL_RESEARCH",
        "submission_branch": "INITIAL_SUBMISSION",
        "fact_status": "conflict",
        "previous_letter_permission": "NONE",
        "selected_story_angle": "Synthetic angle.",
        "journal_conversation": "Synthetic conversation.",
        "controlled_uplift_level": "1_CALIBRATED",
        "hard_gate_failures": ["sample size conflict"],
        "quality_gate_failures": [],
        "stop_reason": "LOOP_LIMIT_WITH_UNRESOLVED_ITEMS",
        "status": "SUBMISSION_READY",
    }
    errors = validator.validate(payload)
    assert any("verified facts" in error for error in errors)
    assert any("no hard gate failures" in error for error in errors)


def test_docx_build_scrubs_metadata_and_uses_business_letter_geometry(tmp_path):
    renderer = load("render_cover_letter_docx")
    payload = {
        "date": "2030-04-12",
        "salutation": "Dear Editorial Team,",
        "paragraphs": ["Synthetic letter content."],
        "signoff": "Sincerely,",
        "corresponding_author": "Alex Morgan",
    }
    output = tmp_path / "synthetic.docx"
    renderer.build(payload, output)
    assert output.exists()
    with zipfile.ZipFile(output) as bundle:
        assert "docProps/custom.xml" not in bundle.namelist()
        core = bundle.read("docProps/core.xml")
        document = bundle.read("word/document.xml")
        assert b"Jizhou" not in core
        assert b"rsid" not in document
    from docx import Document

    doc = Document(output)
    section = doc.sections[0]
    assert round(section.top_margin.inches, 3) == 1.0
    assert round(section.page_width.inches, 3) == 8.5
    assert doc.styles["Normal"].font.name == "Calibri"
