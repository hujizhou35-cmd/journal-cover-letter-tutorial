from __future__ import annotations

import importlib.util
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
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
        "official_article_type": "Original Research",
        "intellectual_route": "ORIGINAL_RESEARCH",
        "submission_branch": "INITIAL_SUBMISSION",
        "fact_status": "verified",
        "previous_letter_permission": "NONE",
        "empirical_anchor": "A synthetic calibration pattern.",
        "editorial_meaning": "The pattern supports a clearer interpretation.",
        "research_decision_spine": "Synthetic stakes -> limitation -> response -> finding -> consequence -> fit.",
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
    result = audit.audit("Dear Editor,\nThis groundbreaking study causes [OUTCOME]. We agree to pay the APC.\nSincerely,")
    assert not result["pass"]
    assert result["placeholders"]
    assert "causal" in result["high_risk_language_for_semantic_review"]
    assert "marketing" in result["high_risk_language_for_semantic_review"]
    assert "submission_system_only" in result["high_risk_language_for_semantic_review"]


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
        "official_article_type": "Review",
        "intellectual_route": "REVIEW_SYNTHESIS",
        "submission_branch": "INITIAL_SUBMISSION",
        "fact_status": "verified",
        "previous_letter_permission": "NONE",
        "empirical_anchor": "A synthetic cross-study pattern.",
        "editorial_meaning": "The synthesis changes the research decision.",
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
        "official_article_type": "Original Research",
        "intellectual_route": "ORIGINAL_RESEARCH",
        "submission_branch": "INITIAL_SUBMISSION",
        "fact_status": "conflict",
        "previous_letter_permission": "NONE",
        "empirical_anchor": "A synthetic calibration pattern.",
        "editorial_meaning": "The pattern supports a clearer interpretation.",
        "research_decision_spine": "Synthetic stakes -> limitation -> response -> finding -> consequence -> fit.",
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


def test_v30_keeps_research_and_review_and_adds_bibliometrics():
    skill = (ROOT / "skills" / "journal-cover-letter-skill" / "SKILL.md").read_text(encoding="utf-8")
    assert "research_decision_spine" in skill
    assert "Translate methods into capabilities" in skill
    assert "Review and synthesis route" in skill
    assert "Do not manufacture controversy" in skill
    assert "## 5C. Bibliometrics route" in skill
    assert "official_article_type" in skill
    assert "intellectual_route" in skill


def test_original_research_requires_decision_spine():
    validator = load("validate_payload")
    payload = {
        "salutation": "Dear Editorial Team,",
        "paragraphs": ["Synthetic research."],
        "signoff": "Sincerely,",
        "corresponding_author": "Alex Morgan",
        "official_article_type": "Original Research",
        "intellectual_route": "ORIGINAL_RESEARCH",
        "submission_branch": "INITIAL",
        "fact_status": "verified",
        "previous_letter_permission": "NONE",
        "empirical_anchor": "A synthetic calibration pattern.",
        "editorial_meaning": "The pattern supports a clearer interpretation.",
        "journal_conversation": "Synthetic conversation.",
        "controlled_uplift_level": "1_CALIBRATED",
        "hard_gate_failures": [],
        "quality_gate_failures": [],
        "stop_reason": "ALL_GATES_PASSED",
        "status": "SUBMISSION_READY",
    }
    assert "research_decision_spine is required for ORIGINAL_RESEARCH" in validator.validate(payload)


def test_bibliometrics_requires_route_specific_fields():
    validator = load("validate_payload")
    payload = {
        "salutation": "Dear Editorial Team,",
        "paragraphs": ["Synthetic bibliometric study."],
        "signoff": "Sincerely,",
        "corresponding_author": "Alex Morgan",
        "official_article_type": "Review",
        "intellectual_route": "BIBLIOMETRICS",
        "submission_branch": "INITIAL",
        "fact_status": "verified",
        "previous_letter_permission": "NONE",
        "empirical_anchor": "A synthetic field transition.",
        "editorial_meaning": "The field needs stronger coordination.",
        "journal_conversation": "Synthetic conversation.",
        "controlled_uplift_level": "1_CALIBRATED",
        "hard_gate_failures": [],
        "quality_gate_failures": [],
        "stop_reason": "ALL_GATES_PASSED",
        "status": "SUBMISSION_READY",
    }
    errors = validator.validate(payload)
    assert "bibliometric_mode is required and must be valid for BIBLIOMETRICS" in errors
    assert "mapping_thesis is required for BIBLIOMETRICS" in errors
    assert "journal_fit_bridge is required for BIBLIOMETRICS" in errors


def test_v31_preserves_bibliometric_specificity_and_blind_benchmarking():
    skill = (ROOT / "skills" / "journal-cover-letter-skill" / "SKILL.md").read_text(encoding="utf-8")
    assert "bibliometric_signature_packet" in skill
    assert "authorial_specificity_floor" in skill
    assert "benchmark_selection_granularity" in skill
    assert "blind-benchmark-loop.md" in skill


def test_v32_protects_benchmark_facts_and_requires_dual_bibliometric_evidence():
    skill = (ROOT / "skills" / "journal-cover-letter-skill" / "SKILL.md").read_text(encoding="utf-8")
    assert "Treat the manuscript and author-confirmed materials as the fact authority" in skill
    assert "performance_analysis_signal" in skill
    assert "science_mapping_signal" in skill
    assert "journal_fit_bridge" in skill
    assert "APC or publication-fee willingness" in skill


def test_bibliometric_example_passes_v32_contract():
    validator = load("validate_payload")
    payload = json.loads(
        (ROOT / "skills" / "journal-cover-letter-skill" / "assets" / "cover-letter-payload.bibliometrics.example.json").read_text(encoding="utf-8")
    )
    assert validator.validate(payload) == []
