# Bounded loop controller v2.1

Maintain at least this state:

```yaml
article_type: ORIGINAL_RESEARCH | REVIEW_SYNTHESIS | OTHER_OR_UNRESOLVED
submission_branch: string
fact_status: verified | conflict | missing
previous_letter_permission: string
selected_story_angle: string | null
editorial_thesis: string | null
synthesis_intervention: string | null
journal_conversation: string | null
controlled_uplift_level: 0_MINIMAL | 1_CALIBRATED | 2_ASSERTIVE
hard_gate_failures: []
quality_gate_failures: []
draft_round: 0
length_round: 0
stop_reason: null
```

## Loop A: intake and fact stability

Resolve conflicts by checking supplied sources or asking focused questions. Stop for author confirmation when a hard conflict, missing declaration, or unresolved article type remains.

## Loop B: story or thesis selection

Generate at most three distinct candidates. Research candidates use story angles; Review candidates use editorial theses paired with synthesis interventions. Score manuscript centrality, evidential support, distinctiveness, editorial consequence, and journal-conversation relevance. Select one coherent route.

## Loop C: draft, audit, targeted revision

Maximum three rounds. Record hard and quality gate failures, revise failed dimensions only, and re-audit. Hard gates include factual conflicts, permission violations, unverified official requirements, claim overreach, unresolved article type, and missing mandatory declarations.

## Loop D: adaptive length

Maximum two rounds after content stabilizes. Apply constraints in this order:

1. explicit journal rule;
2. explicit user request;
3. submission-system limit;
4. evidence-based journal convention;
5. otherwise, the shortest length that performs every editorial function.

Compress when the thesis/story is diluted, the letter duplicates the abstract, methods/results become a list, the same contribution is repeated, or removing a sentence would not change editorial judgment. Do not compress merely to hit a universal word count.

## Stop reasons

- `ALL_GATES_PASSED`;
- `AUTHOR_CONFIRMATION_REQUIRED`;
- `JOURNAL_VERIFICATION_REQUIRED`;
- `LOOP_LIMIT_WITH_UNRESOLVED_ITEMS`;
- `DIMINISHING_RETURNS`.

Map stop reasons to the four allowed final statuses. Never map unresolved hard gates to `SUBMISSION_READY`.
