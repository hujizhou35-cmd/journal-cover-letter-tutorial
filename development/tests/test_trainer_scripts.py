from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRAINER = ROOT / "skills" / "journal-cover-letter-skill-trainer"
SCRIPT_DIR = TRAINER / "scripts"


def load(name: str):
    spec = importlib.util.spec_from_file_location(f"trainer_{name}", SCRIPT_DIR / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_example_training_manifest_is_valid():
    validator = load("validate_training_manifest")
    data = json.loads((TRAINER / "assets" / "training-manifest.example.json").read_text(encoding="utf-8"))
    assert validator.validate(data) == []


def test_manifest_requires_permission_for_expert_letter():
    validator = load("validate_training_manifest")
    data = json.loads((TRAINER / "assets" / "training-manifest.example.json").read_text(encoding="utf-8"))
    data["cases"][0]["benchmark_permission"] = None
    errors = validator.validate(data)
    assert any("ANONYMOUS_EXPERT_BENCHMARK" in error for error in errors)


def test_manifest_rejects_parent_path_escape():
    validator = load("validate_training_manifest")
    data = json.loads((TRAINER / "assets" / "training-manifest.example.json").read_text(encoding="utf-8"))
    data["cases"][0]["manuscript_paths"] = ["../private/manuscript.docx"]
    assert any("safe relative paths" in error for error in validator.validate(data))


def test_fresh_context_manifest_requires_isolated_memory_policy():
    validator = load("validate_training_manifest")
    data = json.loads((TRAINER / "assets" / "training-manifest.example.json").read_text(encoding="utf-8"))
    data["context_memory_policy"] = "UNKNOWN"
    errors = validator.validate(data)
    assert any("FRESH_CONTEXT_BLIND_GENERATION requires" in error for error in errors)


def test_v01_manifest_remains_valid_as_legacy_input():
    validator = load("validate_training_manifest")
    data = json.loads((TRAINER / "assets" / "training-manifest.example.json").read_text(encoding="utf-8"))
    data["schema_version"] = "1.0"
    data["requested_isolation"] = "PROCEDURAL_DELAYED_READ"
    data.pop("context_memory_policy")
    assert validator.validate(data) == []


def test_blind_packet_hides_identity_from_judge_manifest(tmp_path):
    blind = load("prepare_blind_packet")
    baseline = tmp_path / "baseline.txt"
    candidate = tmp_path / "candidate.txt"
    expert = tmp_path / "expert.txt"
    baseline.write_text("baseline", encoding="utf-8")
    candidate.write_text("candidate", encoding="utf-8")
    expert.write_text("expert", encoding="utf-8")
    output = tmp_path / "packet"
    sealed = tmp_path / "sealed" / "identity.json"
    result = blind.prepare(
        {"baseline": baseline, "candidate": candidate, "expert": expert},
        output,
        sealed,
        seed=7,
    )
    judge_text = (output / "judge_manifest.json").read_text(encoding="utf-8")
    assert "baseline" not in judge_text
    assert "candidate" not in judge_text
    assert "expert" not in judge_text
    assert not (output / "sealed_identity.json").exists()
    assert sealed.exists()
    assert set(result["sealed_map"]) == {"A", "B", "C"}


def test_generator_packet_excludes_reference_identity_and_paths():
    packet_builder = load("prepare_generator_packet")
    data = json.loads((TRAINER / "assets" / "training-manifest.example.json").read_text(encoding="utf-8"))
    packet = packet_builder.prepare(
        data,
        case_id="synthetic-train-research",
        round_id="candidate-r1",
        skill_version="2.2.0-candidate.synthetic.r1",
    )
    packet_text = json.dumps(packet, ensure_ascii=False).casefold()
    assert "expert" not in packet_text
    assert "benchmark" not in packet_text
    assert "teacher" not in packet_text
    assert packet["context_contract"]["fresh_context_required"]
    assert packet["context_contract"]["inherited_conversation_allowed"] is False
    assert packet["input_allowlist"]


def test_example_context_ledger_is_valid():
    validator = load("validate_context_ledger")
    data = json.loads((TRAINER / "assets" / "context-ledger.example.json").read_text(encoding="utf-8"))
    assert validator.validate(data) == []


def test_context_ledger_rejects_shared_or_unchecked_context():
    validator = load("validate_context_ledger")
    data = json.loads((TRAINER / "assets" / "context-ledger.example.json").read_text(encoding="utf-8"))
    entry = data["rounds"][0]
    entry["memory_or_project_boundary"] = "SHARED_PROJECT"
    entry["custom_instructions_checked"] = False
    errors = validator.validate(data)
    assert any("memory_or_project_boundary" in error for error in errors)
    assert any("custom_instructions_checked must be true" in error for error in errors)


def test_context_ledger_rejects_missing_expected_round():
    validator = load("validate_context_ledger")
    data = json.loads((TRAINER / "assets" / "context-ledger.example.json").read_text(encoding="utf-8"))
    data["expected_entries"].append({"round_id": "candidate-r1", "case_id": "synthetic-train-research"})
    errors = validator.validate(data)
    assert any("missing expected round/case entries" in error for error in errors)


def test_generator_packet_rejects_path_escape():
    packet_builder = load("prepare_generator_packet")
    data = json.loads((TRAINER / "assets" / "training-manifest.example.json").read_text(encoding="utf-8"))
    data["cases"][0]["manuscript_paths"] = ["../private/manuscript.docx"]
    try:
        packet_builder.prepare(data, "synthetic-train-research", "r0", "2.2.0")
    except ValueError as exc:
        assert "safe relative paths" in str(exc)
    else:
        raise AssertionError("path escape was not rejected")


def passing_result(**overrides):
    result = {
        "hard_gate_failures": [],
        "case_specific_leakage": False,
        "protected_routes_passed": True,
        "expert_benchmark_passed": True,
        "candidate_vs_baseline": [
            {"judge_id": "j1", "winner": "candidate"},
            {"judge_id": "j2", "winner": "candidate"},
            {"judge_id": "j3", "winner": "tie"},
        ],
        "median_rubric_delta": 0.5,
        "human_quality_review_passed": True,
        "holdout_available": True,
        "holdout_passed": True,
        "isolation_level": "STRICT_AGENT_ISOLATED",
        "human_approved": False,
        "human_isolation_override": False,
    }
    result.update(overrides)
    return result


def test_strict_pass_waits_for_human_approval():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(passing_result())
    assert result["eligible"]
    assert result["promotion_decision"] == "PROMOTION_RECOMMENDED"


def test_procedural_pass_requires_isolation_override():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(
        passing_result(isolation_level="PROCEDURAL_DELAYED_READ", human_approved=True)
    )
    assert result["promotion_decision"] == "HUMAN_ISOLATION_OVERRIDE_REQUIRED"


def test_procedural_override_can_be_human_promoted():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(
        passing_result(
            isolation_level="PROCEDURAL_DELAYED_READ",
            human_approved=True,
            human_isolation_override=True,
        )
    )
    assert result["promotion_decision"] == "PROMOTED_WITH_HUMAN_ISOLATION_OVERRIDE"


def test_human_gated_reveal_requires_override():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(
        passing_result(isolation_level="HUMAN_GATED_REVEAL", human_approved=True)
    )
    assert result["stop_reason"] == "CONTEXT_ISOLATION_INCOMPLETE"
    assert result["promotion_decision"] == "HUMAN_ISOLATION_OVERRIDE_REQUIRED"


def test_verified_fresh_context_uses_normal_human_gate():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(
        passing_result(
            isolation_level="FRESH_CONTEXT_BLIND_GENERATION",
            fresh_context_evidence_passed=True,
            human_approved=True,
        )
    )
    assert result["stop_reason"] == "PROMOTION_GATES_PASSED"
    assert result["promotion_decision"] == "PROMOTED_WITH_HUMAN_APPROVAL"


def test_unverified_fresh_context_is_downgraded_to_override():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(
        passing_result(
            isolation_level="FRESH_CONTEXT_BLIND_GENERATION",
            fresh_context_evidence_passed=False,
        )
    )
    assert result["stop_reason"] == "CONTEXT_ISOLATION_INCOMPLETE"
    assert result["promotion_decision"] == "HUMAN_ISOLATION_OVERRIDE_REQUIRED"


def test_missing_holdout_stays_candidate_only():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(passing_result(holdout_available=False))
    assert result["promotion_decision"] == "CANDIDATE_ONLY"
    assert result["stop_reason"] == "INSUFFICIENT_HOLDOUT"


def test_hard_gate_failure_blocks_promotion():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(passing_result(hard_gate_failures=["causal overclaim"]))
    assert not result["eligible"]
    assert result["promotion_decision"] == "REJECTED_OR_REVISE"


def test_contaminated_run_is_never_promotable_even_without_blind_comparison():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(
        passing_result(
            isolation_level="REFERENCE_CONTAMINATED",
            candidate_vs_baseline=[],
        )
    )
    assert not result["eligible"]
    assert result["promotion_decision"] == "CANDIDATE_ONLY"
    assert result["stop_reason"] == "REFERENCE_CONTAMINATED"


def test_unknown_isolation_level_is_rejected():
    promotion = load("evaluate_promotion")
    result = promotion.evaluate(passing_result(isolation_level="UNKNOWN"))
    assert not result["eligible"]
    assert result["stop_reason"] == "INVALID_ISOLATION"
    assert result["failures"] == ["invalid_isolation_level"]
