---
name: journal-cover-letter-skill-trainer
description: Improve, extend, or benchmark the journal-cover-letter-skill from paired manuscript materials and expert-authored cover letters. Use whenever a user wants to train or iterate the Cover Letter Skill, compare an AI letter with an expert letter, strengthen the Research, Review, or Bibliometrics route, add a new writing route, process a batch of manuscript-letter pairs, control when an expert reference enters model context, or decide whether a candidate Skill version is genuinely better. Do not use merely to write one submission letter.
---

# Journal Cover Letter Skill Trainer v0.2.0

Improve the `journal-cover-letter-skill` through controlled experiments. Learn transferable editorial reasoning from expert letters without copying their wording, treating them as factual authorities, or overfitting one manuscript.

## Non-negotiable principles

- Treat the manuscript and author-confirmed case materials as the factual source of truth. An expert letter is a benchmark for editorial decisions, not a gold standard.
- Generate the baseline before exposing its generator to the expert letter.
- After the expert is revealed, never reuse that evaluator context for a claimed-blind candidate generation. Start a fresh generator context for every round.
- Change the target route for a stated reason. Do not patch only the current letter.
- A single case may create an experimental candidate, but cannot by itself prove a general improvement.
- Protect every route that was not targeted. A Research improvement must not silently weaken Review or Bibliometrics, and vice versa.
- Preserve the target Skill's name. Version the candidate and release; do not rename the Skill to encode a version.
- Keep private manuscripts and real letters outside public source trees and release packages.
- Never describe a comparison as objective proof. Report the rubric, judges, isolation level, evidence, uncertainty, and human decision.

## 1. Determine the run mode

Set:

```text
training_intent: STRENGTHEN_EXISTING_ROUTE | PROPOSE_NEW_ROUTE
target_route: ORIGINAL_RESEARCH | REVIEW_SYNTHESIS | BIBLIOMETRICS | user-defined route
storage_mode: SESSION_ONLY | LOCAL_PRIVATE_CORPUS
isolation_level: STRICT_AGENT_ISOLATED | FRESH_CONTEXT_BLIND_GENERATION | HUMAN_GATED_REVEAL | REFERENCE_CONTAMINATED
promotion_policy: HUMAN_APPROVAL
```

Use `STRICT_AGENT_ISOLATED` when host-managed workers or API requests enforce separate contexts and controlled inputs. Use `FRESH_CONTEXT_BLIND_GENERATION` when a human starts a new temporary chat or conversation for every baseline and candidate generation, supplies only the candidate Skill plus manuscript-side materials, and verifies that memory, project files, custom instructions, and inherited conversation do not expose the expert. Use `HUMAN_GATED_REVEAL` when the expert is withheld until the first baseline is sealed but later candidate generation remains in the revealed conversation. If any claimed-blind generator has already seen or been quoted material from the expert letter, use `REFERENCE_CONTAMINATED` for that round.

`PROCEDURAL_DELAYED_READ` from v0.1 manifests is a supported legacy alias for `HUMAN_GATED_REVEAL`. Human-gated reveal protects the first baseline only; it does not make the whole loop blind. It may still produce a publishable candidate when the user explicitly accepts the limitation. Record `HUMAN_ISOLATION_OVERRIDE`; never relabel it fresh or strict. A contaminated round may support qualitative rule discovery but not blind-comparison claims.

Read `references/portability-and-isolation.md` when the host's isolation capability is uncertain.
Use `references/worker-prompts.md` to dispatch internal roles without asking the user to repeat prompts.

## 2. Inventory inputs and permission

Accept either one case or a ZIP containing case folders. Prefer:

```text
training-manifest.json
target-skill/
cases/
  case-001/
    case.json
    manuscript/
    expert/
    journal/        # optional captured guidance
  case-002/
    ...
```

Required inputs:

- a snapshot of the current target Skill and its version;
- the training intent and target route;
- at least one training case with manuscript-side materials;
- exactly one identified expert benchmark per benchmark case;
- permission to analyze it as `ANONYMOUS_EXPERT_BENCHMARK`;
- whether journal requirements should use `CURRENT_LIVE`, `CAPTURED_AS_OF_SUBMISSION`, or `NOT_SCORED` evidence;
- any cases reserved as `HOLDOUT` or `REGRESSION`.

Infer obvious file groupings, but stop for a focused question when files cannot be paired safely or permission is missing. Never infer permission from possession. Validate a local manifest with `scripts/validate_training_manifest.py` when available.

For `LOCAL_PRIVATE_CORPUS`, keep raw cases in an ignored private directory. Store only case IDs, hashes, permissions, route labels, derived scores, and paraphrased lessons in public-safe reports. Read `references/input-and-case-schema.md` for the full contract.

## 3. Snapshot the baseline

Before changing anything:

1. Snapshot the complete target Skill, including references, scripts, assets, description, and version.
2. Record the target route and protected routes.
3. Run the target Skill's existing deterministic tests and evals when available.
4. Create a run ID and immutable round-0 record.
5. Record any missing holdout coverage before learning begins.
6. Create an evaluator-only context ledger before the first generation. Record each round's context ID, input-packet hash, memory/project boundary, output hash, and reveal time.

Do not use a candidate as its own baseline. The default baseline for every round is the original version supplied at the start of the run; also retain the immediately previous round for diagnostic comparison.

## 4. Blind baseline generation

For every training case, give the isolated generator only:

- the baseline Skill snapshot;
- manuscript, title-page, supplement, author-confirmation, and permitted journal-side materials;
- the ordinary task: produce the same outputs the target Skill normally promises.

Do not mention that an expert letter exists. Do not pass its filename, location, extracted text, summary, or metadata. Save the baseline letter, audit, intermediate route choice, and timing before revealing the benchmark.

When a human controls file delivery, the first expert upload may occur only after the baseline output and its hash or timestamp are sealed. This is a valid reveal gate, but its achieved isolation is only `HUMAN_GATED_REVEAL` unless later rounds move to fresh contexts.

If the target Skill normally pauses for author confirmation, use confirmations explicitly stored in the case manifest. Do not bypass unresolved factual gates merely to obtain a letter.

## 5. Reveal, audit, and compare

After the baseline is sealed, allow the comparison phase to read the manuscript, baseline output, and expert letter.

First audit both letters against the manuscript. A persuasive expert letter can still lose a hard gate through factual drift, causal overreach, subgroup misuse, proxy inflation, stale journal details, or missing declarations.

Then compare editorial effects using randomized identities rather than author or version labels. Evaluate:

1. problem foregrounding;
2. gap or contrast quality;
3. route-specific reasoning;
4. method abstraction;
5. finding or synthesis selection;
6. implication level;
7. journal-fit specificity;
8. omission discipline and reading effort;
9. claim calibration;
10. administrative completeness.

Prefer three independent blind judgments when isolated workers are available. Record wins, ties, disagreement, evidence, and hard-gate failures. One model judgment is qualitative evidence, not a stable ranking. Read `references/blind-evaluation-rubric.md` before grading.

## 6. Extract transferable hypotheses

Explain why the outputs created different editorial decisions. Produce no more than three change hypotheses per round. Each hypothesis must include:

```text
hypothesis_id
target_route
observed_difference
underlying_editorial_principle
proposed_skill_change
why_it_should_generalize
likely_counterexample
regression_risk
evidence_cases
```

Reject a hypothesis when it encodes manuscript names, substances, outcomes, statistics, exact word counts, journal-specific wording, distinctive expert phrasing, or a preference that would not survive a different case. Prefer changes to decision logic, information selection, abstraction level, claim calibration, or stopping behavior.

If the expert's advantage comes from an unsupported claim, do not teach the overclaim. Extract the legitimate editorial intent and encode a safer way to achieve it.

## 7. Build one experimental candidate

Create a complete candidate copy of the target Skill. Preserve its name and unrelated behavior.

- For `STRENGTHEN_EXISTING_ROUTE`, edit the target route and only the cross-cutting rules demonstrably responsible for the failure.
- For `PROPOSE_NEW_ROUTE`, add a separate experimental playbook, routing rule, state fields, boundaries, and regression cases. Do not force the new article type into Research or Review.
- Explain why each changed instruction belongs in the Skill rather than only in the current output.
- Remove redundant rules when a clearer principle replaces them.

Use candidate versions such as `2.2.0-candidate.<run-id>.r1`. A route-strengthening release normally advances the minor version; a new public route or incompatible contract normally advances the major version.

## 8. Regenerate and iterate

After the evaluator creates a candidate Skill, close the generation phase in that context. Regenerate every training case using a new candidate-generator context that has never received the expert letter or any substantive expert-derived comparison. Give it only the complete candidate Skill, manuscript-side packet, author confirmations, and permitted journal evidence. The evaluator may continue to retain the expert, but the generator may not inherit the evaluator conversation.

For human-orchestrated use, apply this handshake on every round:

1. evaluator seals the candidate Skill;
2. human starts a new temporary chat or otherwise fresh conversation;
3. human supplies only the generator packet and candidate Skill;
4. generator seals its letter and audit;
5. human returns those outputs to the evaluator;
6. evaluator compares and produces the next candidate.

Do not place generator and evaluator chats in a shared project or memory scope that can surface the expert. Check custom instructions and attached project files before claiming `FRESH_CONTEXT_BLIND_GENERATION`. Use `scripts/prepare_generator_packet.py` when local tools are available.

Compare:

- candidate versus original baseline;
- candidate versus expert benchmark;
- candidate versus the immediately previous round when diagnosing progress.

Revise the candidate rule, not the case-specific letter. Run at most four candidate rounds. Stop early when:

- all promotion gates pass;
- two consecutive rounds fail to improve held-out performance;
- remaining differences are taste, cadence, or harmless wording;
- the proposed improvement requires unsupported factual or promotional inflation.

Allowed stop reasons:

```text
PROMOTION_GATES_PASSED
INSUFFICIENT_HOLDOUT
BLOCKED_HARD_GATE
REFERENCE_CONTAMINATED
CONTEXT_ISOLATION_INCOMPLETE
DIMINISHING_RETURNS
ROUND_LIMIT_REACHED
USER_STOPPED
```

## 9. Validate generalization and protected routes

Do not learn from holdout or regression cases. After the candidate stabilizes:

1. run at least one untouched case for the changed route;
2. rerun protected-route cases and deterministic tests;
3. use the same blind rubric and hard gates;
4. inspect whether the candidate merely became more similar to one expert;
5. compare quality, tokens, latency, and unnecessary workflow steps when available.

An existing route may be promoted only when the candidate has no hard-gate failures, wins or ties the baseline under the stated judging rule, and causes no material protected-route regression. A new route remains experimental after one example; normally require at least two independent learning cases plus one untouched holdout before public promotion.

Read `references/promotion-and-versioning.md` for exact decision gates.

## 10. Human promotion gate

Never silently replace the formal target Skill. Present:

- the full candidate Skill;
- a concise before/after rule diff;
- baseline, candidate, and expert comparisons with identities unsealed only after grading;
- hard-gate and protected-route results;
- isolation level and any override;
- the context ledger showing whether every claimed-blind round started fresh;
- holdout coverage and limitations;
- proposed version and changelog;
- one promotion recommendation.

Possible decisions:

```text
CANDIDATE_ONLY
PROMOTION_RECOMMENDED
HUMAN_ISOLATION_OVERRIDE_REQUIRED
PROMOTED_WITH_HUMAN_APPROVAL
PROMOTED_WITH_HUMAN_ISOLATION_OVERRIDE
REJECTED_OR_REVISE
```

`HUMAN_GATED_REVEAL`, legacy `PROCEDURAL_DELAYED_READ`, or an unverified fresh-context claim may be published only after the user explicitly accepts the limitation. Verified `FRESH_CONTEXT_BLIND_GENERATION` can proceed through the normal human approval gate, while remaining labeled human-orchestrated rather than host-enforced. `REFERENCE_CONTAMINATED`, unresolved permission, factual hard-gate failures, case-specific leakage, or missing required regression evidence cannot be hidden by an override.

## 11. Deliverables

Return or save:

1. the candidate or promoted Skill package;
2. `training-report.md` and a machine-readable result;
3. the change-hypothesis ledger;
4. blind judgment summaries and the sealed identity map separately;
5. holdout and protected-route results;
6. version/changelog entry;
7. privacy statement listing what raw material was retained;
8. exactly one stop reason and one promotion decision;
9. a context ledger or an explicit statement that no auditable context record was available.

Do not reproduce long passages from private expert letters. Paraphrase the editorial principle and preserve only the minimum evidence needed for audit.

## Bundled resources

- `references/input-and-case-schema.md`: ZIP layout, manifest fields, permissions, and storage modes.
- `references/portability-and-isolation.md`: strict local/Codex mode and portable-chat fallback.
- `references/blind-evaluation-rubric.md`: hard gates, randomized comparison, and judge aggregation.
- `references/promotion-and-versioning.md`: holdout, regression, override, and release rules.
- `references/worker-prompts.md`: ready-to-dispatch isolated worker templates.
- `scripts/validate_training_manifest.py`: deterministic manifest validation.
- `scripts/prepare_blind_packet.py`: randomized anonymous output packet creation.
- `scripts/prepare_generator_packet.py`: expert-free allowlisted input manifest for each fresh generation context.
- `scripts/validate_context_ledger.py`: deterministic validation of fresh-context evidence.
- `scripts/evaluate_promotion.py`: deterministic promotion-gate aggregation.
- `assets/training-manifest.example.json`: fully synthetic starter manifest.
- `assets/context-ledger.example.json`: evaluator-only record for generation-context evidence.
