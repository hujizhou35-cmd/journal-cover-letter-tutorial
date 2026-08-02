# Bounded loop controller

Maintain a compact state object:

```yaml
article_type: ORIGINAL_RESEARCH | REVIEW_SYNTHESIS | OTHER_OR_UNRESOLVED
submission_branch: string
fact_status: verified | conflict | missing
previous_letter_permission: string
candidate_story_angles: []
selected_story_angle: string | null
hard_gate_failures: []
quality_gate_failures: []
draft_round: 0
compression_round: 0
stop_reason: null
```

## Loop A: intake and facts

Repeat only while a source conflict can be resolved by re-reading supplied files or asking a focused question. Stop for user input when a hard conflict remains.

## Loop B: story selection

Generate at most three distinct story angles. Score editorial importance, manuscript centrality, evidential support, distinctiveness, and journal-reader relevance. Select one; do not splice unrelated angles into a list.

## Loop C: draft, audit, targeted revision

Maximum three rounds. In each round, record hard and quality gate failures, revise only those failures, and re-audit. Hard gates include factual conflicts, permission violations, unverified journal requirements, claim overreach, and missing mandatory declarations.

## Loop D: compression

Maximum two rounds after content stabilizes. Compress when the story is diluted, the draft duplicates the abstract, methods/results become lists, or a sentence can be removed without changing editorial judgment.

Stop on all gates passed, author confirmation required, journal verification required, exhausted rounds with unresolved gates, or diminishing returns. Loop exhaustion never equals success.
