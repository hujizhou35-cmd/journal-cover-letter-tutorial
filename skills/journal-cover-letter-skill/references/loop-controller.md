# Bounded loop controller v2.3

Maintain at least this state:

```yaml
article_type: ORIGINAL_RESEARCH | REVIEW_SYNTHESIS | OTHER_OR_UNRESOLVED
submission_branch: string
fact_status: verified | conflict | missing
previous_letter_permission: string
confirmation_mode: EXPLICIT_CONFIRMATION | EVIDENCE_COMPLETE_FAST_PATH | PENDING
selected_story_angle: string | null
research_decision_spine: string | null
editorial_thesis: string | null
synthesis_intervention: string | null
synthesis_contrast: string | null
journal_conversation: string | null
journal_fit_basis: ARTICLE_TYPE_CRITERION | READERSHIP_NEED | CURRENT_CONVERSATION | UNVERIFIED
controlled_uplift_level: 0_MINIMAL | 1_CALIBRATED | 2_ASSERTIVE
benchmark_dimensions: {}
hard_gate_failures: []
quality_gate_failures: []
draft_round: 0
length_round: 0
stop_reason: null
```

## Loop A: intake and fact stability

Resolve conflicts by checking supplied sources or asking focused questions. Use `EVIDENCE_COMPLETE_FAST_PATH` when the user's instructions and source files already verify every decision-changing fact; record assumptions in the audit. Stop for author confirmation when a hard conflict, missing mandatory declaration, unresolved article type, or permission ambiguity remains.

## Loop B: story or thesis selection

Generate at most three distinct candidates. Research candidates use decision spines; Review candidates pair a synthesis intervention with one editorial thesis and one synthesis contrast. Score manuscript centrality, evidential support, distinctiveness, editorial consequence, and journal-fit relevance. Select one coherent route.

For original research, the selected route must be expressible as:

> Stakes -> unresolved limitation -> study response -> synthesized finding -> consequence -> journal fit

For Review, the selected route must be expressible as:

> Field problem -> synthesis intervention -> editorial thesis -> changed decision or research agenda -> journal fit -> calibrated boundary

The Review draft may use at most two supporting cross-study patterns.

## Loop C: draft, audit, and targeted rule revision

Maximum three rounds. Record hard and quality gate failures, revise failed dimensions only, and re-audit. Hard gates include factual conflicts, permission violations, unverified official requirements, claim overreach, unresolved article type, and missing mandatory declarations.

When a human benchmark is authorized, compare decision effects using `references/human-benchmark-protocol.md`. If a material difference reflects a general route weakness, revise the transferable rule and regenerate. Do not merely imitate benchmark wording or patch the test draft.

## Loop D: adaptive length and omission discipline

Maximum two rounds after content stabilizes. Apply constraints in this order:

1. explicit journal rule;
2. explicit user request;
3. submission-system limit;
4. evidence-based journal convention;
5. otherwise, the shortest length that performs every editorial function.

For ordinary research submissions, use a focused one-page letter as the default convention when no contrary instruction exists. Compress when the decision spine is diluted, the letter duplicates the abstract, methods or results become a list, multiple implications compete, the same contribution is repeated, or removing a sentence would not alter editorial judgment.

Do not compress merely to hit a universal word count.

## Stop reasons

- `ALL_GATES_PASSED`;
- `AUTHOR_CONFIRMATION_REQUIRED`;
- `JOURNAL_VERIFICATION_REQUIRED`;
- `LOOP_LIMIT_WITH_UNRESOLVED_ITEMS`;
- `DIMINISHING_RETURNS`;
- `BENCHMARK_CONVERGENCE_REACHED`.

Map stop reasons to the four allowed final statuses. Never map unresolved hard gates to `SUBMISSION_READY`.
