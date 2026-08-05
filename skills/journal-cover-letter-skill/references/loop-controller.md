# Bounded loop controller v3.2

Maintain at least this state:

```yaml
official_article_type: string | UNRESOLVED
intellectual_route: ORIGINAL_RESEARCH | REVIEW_SYNTHESIS | BIBLIOMETRICS | OTHER_OR_UNRESOLVED
submission_branch: string
fact_status: verified | conflict | missing | not_applicable
previous_letter_permission: string
confirmation_mode: EXPLICIT_CONFIRMATION | EVIDENCE_COMPLETE_FAST_PATH | PENDING
empirical_anchor: string | null
editorial_meaning: string | null
selected_story_angle: string | null
research_decision_spine: string | null
editorial_thesis: string | null
synthesis_intervention: string | null
synthesis_contrast: string | null
bibliometric_mode: PERFORMANCE_ANALYSIS | SCIENCE_MAPPING | BOTH | null
performance_analysis_signal: string | null
science_mapping_signal: string | null
mapping_intervention: string | null
mapping_thesis: string | null
bibliometric_decision_spine: string | null
metric_boundary: string | null
journal_conversation: string | null
journal_fit_basis: ARTICLE_TYPE_CRITERION | READERSHIP_NEED | CURRENT_CONVERSATION | UNVERIFIED
journal_fit_bridge: string | null
controlled_uplift_level: 0_MINIMAL | 1_CALIBRATED | 2_ASSERTIVE
benchmark_empirical_signal: string | null
benchmark_editorial_logic: string | null
benchmark_selection_granularity: string | null
authorial_empirical_fingerprint: string | null
bibliometric_signature_packet: string | null
authorial_specificity_floor: string | null
blind_benchmark_mode: true | false
benchmark_dimensions: {}
hard_gate_failures: []
quality_gate_failures: []
draft_round: 0
length_round: 0
stop_reason: null
```


## Loop 0: blind baseline for skill benchmarking

Use only when the user requests a benchmark test.

1. Create an allowlist of manuscript, skill, and official journal sources.
2. Exclude the human benchmark from the generation context and file inputs.
3. Generate and freeze the baseline draft with a hash or immutable copy.
4. Reveal the benchmark only after freezing.
5. Compare editorial effects, empirical selection, selection granularity, and factual accuracy.
6. Convert each material difference into a transferable rule.
7. Regenerate from the original manuscript plus revised skill only; do not feed benchmark wording into the new draft.

In a conversation where the same model has already seen the benchmark, label the run `FILE_LEVEL_BLIND_ONLY`; do not claim cognitive isolation. Strict cognitive isolation requires a separate model session or external agent.

## Loop A: fact and route stability

Resolve conflicts by checking supplied sources or asking focused questions. Confirm exact official article type separately from intellectual route. Stop for author confirmation when a hard conflict, missing mandatory declaration, unresolved official label, unresolved route, or permission ambiguity remains.

When a benchmark conflicts with the manuscript, keep the manuscript value and record the benchmark item as stale, conflicting, or unverified. The benchmark may influence selection logic but not the fact sheet.

## Loop B: anchor and thesis selection

Generate at most three candidates. Each candidate must pair one `empirical_anchor` with one `editorial_meaning`.

- Research candidates use a decision spine.
- Review candidates pair a synthesis intervention, thesis, and contrast.
- Bibliometric candidates pair a mapping intervention, mapping thesis, decision spine, and metric boundary.

For `BOTH`, reject a candidate unless one performance-analysis signal and one science-mapping signal support the same mapping thesis.

Score manuscript centrality, evidential support, distinctiveness, authorial empirical fingerprint, editorial consequence, and journal relevance. Reject a candidate with a strong interpretation but weak factual anchor, or a strong fact with no changed decision.

## Loop C: draft, audit, targeted revision

Maximum three rounds. Hard gates include factual conflicts, permission violations, unverified official requirements, claim overreach, unresolved official type or route, metric overinterpretation, and missing mandatory declarations.

When a human benchmark is authorized, preserve the strongest transferable empirical signal and necessary selection granularity, then improve the editorial logic. Do not imitate wording. In blind mode, the regenerated draft must not receive benchmark text.

## Loop D: omission and length

Maximum two rounds after content stabilizes. Apply constraints in this order:

1. explicit journal rule;
2. explicit user request;
3. submission-system limit;
4. evidence-based journal convention;
5. otherwise, the shortest length that performs every editorial function.

Compress when the anchor is obscured, meaning is repeated, methods/results become lists, multiple implications compete, or metric catalogues replace interpretation. Do not compress merely to hit a universal word count.

## Stop reasons

- `ALL_GATES_PASSED`;
- `AUTHOR_CONFIRMATION_REQUIRED`;
- `JOURNAL_VERIFICATION_REQUIRED`;
- `LOOP_LIMIT_WITH_UNRESOLVED_ITEMS`;
- `DIMINISHING_RETURNS`;
- `BENCHMARK_CONVERGENCE_REACHED`.

Benchmark convergence requires no core effect dimension below 4/5 and an overall effect score of at least 85%, excluding factual errors or unsupported claims in the benchmark.

Never map unresolved hard gates to `SUBMISSION_READY`.
