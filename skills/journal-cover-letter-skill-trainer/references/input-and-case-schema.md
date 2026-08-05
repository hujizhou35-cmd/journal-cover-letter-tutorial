# Input and case schema

## Preferred ZIP layout

```text
training-manifest.json
target-skill/
  SKILL.md
  references/
  scripts/
  assets/
cases/
  case-001/
    case.json
    manuscript/
    expert/expert-letter.docx
    journal/
  case-002/
    ...
```

The target Skill is supplied once. Each case folder is independent and must not rely on filenames in another case.

## Manifest fields

```json
{
  "schema_version": "1.1",
  "run_id": "2026-08-05-research-001",
  "target_skill": {
    "name": "journal-cover-letter-skill",
    "version": "2.2.0",
    "path": "target-skill"
  },
  "training_intent": "STRENGTHEN_EXISTING_ROUTE",
  "target_route": "ORIGINAL_RESEARCH",
  "storage_mode": "SESSION_ONLY",
  "requested_isolation": "FRESH_CONTEXT_BLIND_GENERATION",
  "context_memory_policy": "DISABLED_OR_SEPARATE_SCOPE",
  "promotion_policy": "HUMAN_APPROVAL",
  "cases": []
}
```

Each case contains:

```json
{
  "id": "case-001",
  "role": "TRAIN",
  "article_type": "ORIGINAL_RESEARCH",
  "manuscript_paths": ["cases/case-001/manuscript/manuscript.docx"],
  "expert_letter_path": "cases/case-001/expert/expert-letter.docx",
  "benchmark_permission": "ANONYMOUS_EXPERT_BENCHMARK",
  "journal_context_mode": "CAPTURED_AS_OF_SUBMISSION",
  "journal_context_paths": [],
  "author_confirmations": {},
  "sensitive_terms": []
}
```

Allowed roles are `TRAIN`, `HOLDOUT`, and `REGRESSION`. At least one `TRAIN` case is required. A benchmark file requires `ANONYMOUS_EXPERT_BENCHMARK`; possession alone is not permission.

`journal_context_mode` values:

- `CURRENT_LIVE`: verify the journal now and assess the new letter against current requirements;
- `CAPTURED_AS_OF_SUBMISSION`: use supplied dated guidance for a historical comparison;
- `NOT_SCORED`: exclude volatile journal details from the quality comparison.

Do not silently compare a historical expert letter against current journal rules and attribute the difference to writing skill.

## Context-control fields

`requested_isolation` accepts:

- `STRICT_AGENT_ISOLATED`: host-managed separate contexts or API requests;
- `FRESH_CONTEXT_BLIND_GENERATION`: a new human-controlled context for every generation round;
- `HUMAN_GATED_REVEAL`: the expert is delayed until the first baseline is sealed, but later rounds remain in the revealed conversation;
- `REFERENCE_CONTAMINATED`: expert material has already entered a claimed-blind generator;
- legacy `PROCEDURAL_DELAYED_READ`, normalized to `HUMAN_GATED_REVEAL` in reports.

For `FRESH_CONTEXT_BLIND_GENERATION`, `context_memory_policy` must be `DISABLED_OR_SEPARATE_SCOPE` or `HOST_MANAGED`. A separate scope means a generator-only project or workspace that does not contain evaluator chats or expert files; merely enabling project-only memory inside a shared project is insufficient. Use `UNKNOWN` only for human-gated or contaminated runs. This field records the requested setup; the training report must separately record what was actually achieved in every round.

Keep the context ledger evaluator-side. Never include it in a generator packet because even an empty benchmark flag reveals that a benchmark exists.

## Storage modes

### SESSION_ONLY

Use attachments only for the current run. Deliver a portable candidate, report, and optional manifest containing hashes and derived findings. Do not claim future regression coverage unless the user supplies the cases again.

### LOCAL_PRIVATE_CORPUS

Store raw cases only below an ignored directory such as `local-only/trainer-corpus/`. Never include raw cases in Git, `.skill` files, plugin ZIPs, public eval viewers, screenshots, or logs. Public-safe records may contain:

- opaque case ID and file hashes;
- permission and route labels;
- scores and gate outcomes;
- paraphrased, generalizable hypotheses;
- no author names, contact details, titles, journal submission identifiers, or long source excerpts.

## New-route evidence

One case can create an `EXPERIMENTAL` route. Public promotion normally requires:

- two independent learning cases supporting the route distinction;
- one untouched holdout case;
- regression coverage for Research, Review, and shared gates;
- human approval.
