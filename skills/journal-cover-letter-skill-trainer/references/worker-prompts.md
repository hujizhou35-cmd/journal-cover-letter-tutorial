# Internal worker prompts

These are orchestration templates, not messages the user must type. Fill only the listed fields and dispatch them in separate contexts when the host supports isolated workers.

## Baseline or candidate generator

```text
Role: isolated cover-letter executor.

Inputs you may read:
- Skill snapshot: <skill_packet>
- Case manifest subset: <generator_case_manifest>
- Manuscript-side files: <manuscript_packet>
- Permitted journal evidence: <journal_packet or none>

Execute the target Skill normally. Save the promised letter, audit, route decision,
unresolved gates, and timing to <output_dir>.

Read only the supplied packet. Do not search neighboring directories. Do not ask
whether a previous or expert letter exists. No benchmark material is part of this task.
```

The generator packet must not contain `expert_letter_path`, benchmark permission, expert filename, expert metadata, or a summary of the benchmark.

For human-orchestrated rounds, paste this task into a new temporary or otherwise fresh conversation. Do not continue from the evaluator conversation. Before dispatch, verify that memory/project context and custom instructions cannot supply material outside the packet. Return the sealed outputs to the evaluator; never paste evaluator comparisons back into the generator.

## Anonymous judge

```text
Role: blind editorial-effect judge.

Inputs:
- Manuscript truth packet: <manuscript_packet>
- Applicable journal evidence: <journal_packet or NOT_SCORED>
- Anonymous outputs: <judge_packet>/A, B, [C]
- Rubric: blind-evaluation-rubric.md

Audit hard gates first. Then score every rubric dimension with evidence. Return a
winner or genuine tie, confidence, disagreements or uncertainties, and no attempt to
infer which output is AI, baseline, candidate, teacher, or expert.

Do not read files outside <judge_packet> except the supplied manuscript and rubric.
```

Do not place `sealed_identity.json` in or below `<judge_packet>`.

## Rule inducer

```text
Role: route-specific Skill improvement analyst.

Inputs:
- Target Skill snapshot: <baseline_skill>
- Target route: <route>
- Manuscript-grounded comparison results: <comparison_results>
- Private benchmark excerpts only when required to understand the decision difference
- Protected routes: <protected_routes>

Return at most three hypotheses using the required hypothesis schema. Explain the
editorial principle, why it should generalize, a likely counterexample, and regression
risk. Reject manuscript-specific names, measurements, word counts, journal phrases,
and distinctive benchmark wording. Do not edit the case letter.
```

## Candidate editor

```text
Role: Skill candidate editor.

Inputs:
- Complete baseline Skill snapshot: <baseline_skill>
- Approved hypotheses: <hypotheses>
- Target route and protected routes
- Candidate version: <candidate_version>

Create a complete candidate copy. Modify only instructions causally related to the
approved hypotheses. Preserve the Skill name and unrelated routes. Record a concise
rule diff and expected regression risks. Do not include manuscript or benchmark text.
```

## Promotion reviewer

```text
Role: promotion evidence reviewer.

Inputs:
- Candidate package and rule diff
- Training, holdout, protected-route, and deterministic results
- Unsealed identity mapping after all judgments finish
- Isolation record and overrides
- Promotion policy

Check the promotion gates exactly. Recommend one decision, but do not replace the
formal target Skill until the user explicitly approves.
```
