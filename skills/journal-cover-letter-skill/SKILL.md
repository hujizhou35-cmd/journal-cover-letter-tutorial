---
name: journal-cover-letter-skill
description: Create, revise, or audit a cover letter for an academic journal submission from manuscript files. Use whenever a user wants a journal submission letter, asks to tailor a cover letter to a target journal, provides a manuscript and asks for a letter, or wants an existing academic cover letter improved. Route original research through a scientific discovery story and reviews/syntheses through a field diagnosis and editorial thesis. Do not use for job applications, recommendation letters, or non-academic business correspondence.
---

# Journal Cover Letter Skill v2.1

Create an editor-facing submission argument from verified manuscript facts, current official journal information, and user-authorized benchmark material. Prioritize biomedical and life-science submissions while remaining discipline-general. Default to English unless the user requests another language.

## Non-negotiable principles

- Treat manuscript files as the factual source of truth. Never invent titles, results, registrations, declarations, author details, or journal requirements.
- Separate verified facts, conflicts, missing items, and interpretive claims.
- Use the strongest wording the evidence permits. Factual discipline should sharpen persuasion, not flatten it.
- Route original research and evidence synthesis through different editor-facing narratives.
- A review cover letter must sell a new interpretation, not merely report that a synthesis was performed.
- Treat a prior letter as user-controlled. Analyze or reuse only within the recorded permission.
- Treat an expert-authored or human-authored benchmark as evidence about editorial choices, not a gold standard.
- Research current journal information after human confirmation and distinguish official requirements from reasoned inferences.
- Use bounded loops with explicit state and stop reasons. Loop exhaustion never means success.
- Use scripts only for deterministic work. Keep scientific meaning, story selection, field diagnosis, and editorial thesis in model judgment.

## Phase 1: Intake, routing, and permissions

Read `references/intake-and-fact-sheet.md`. Inventory the manuscript, title page, supplements, previous letter, correspondence, and user instructions. Build a source-traceable fact sheet with `verified`, `conflict`, `missing`, and `not_applicable` states.

Set:

- `article_type`: `ORIGINAL_RESEARCH`, `REVIEW_SYNTHESIS`, or `OTHER_OR_UNRESOLVED`;
- `submission_branch`;
- `fact_status`;
- required declaration states.

Ask whether a previous cover letter exists and record exactly one `previous_letter_permission`: `FORMAT_ONLY`, `FORMAT_AND_TONE`, `MAXIMUM_SUITABLE_WORDING`, `FACT_CHECK_ONLY`, `ANONYMOUS_EXPERT_BENCHMARK`, or `NONE`.

If benchmark analysis is allowed, read `references/human-benchmark-protocol.md`. Extract decisions and reasoning patterns without importing private facts, outdated journal details, or unsupported wording.

## Phase 2: Human confirmation gate

Present:

- the fact sheet with sources and statuses;
- article type and submission branch;
- up to six candidate contributions;
- up to three candidate Research story angles or Review editorial theses;
- declaration gaps and evidence-boundary risks;
- the prior-letter permission and proposed use.

Wait for the user to confirm or correct this foundation before researching the journal or drafting the final letter.

## Phase 3: Current journal research

Read `references/journal-research-protocol.md`. Verify current official author instructions, aims/scope, readership, accepted article type, cover-letter requirements, required declarations, editor identity only when needed, and recent relevant content.

Build `journal_conversation`: what the journal's readers are currently discussing, where the conversation stops, and how this manuscript complements, challenges, reorganizes, or advances it. Cite direct official or journal sources in the working audit; do not use generic scope praise as fit.

If current official information cannot be accessed, set `NEEDS_JOURNAL_VERIFICATION`. Never mark the output submission-ready.

## Phase 4A: Original Research route

Read `references/research-playbook.md`. Select one `selected_story_angle`:

> Important problem -> knowledge gap -> design advantage -> central finding -> defensible meaning -> journal conversation

The design exists to make the finding credible; it is not the story by itself. Lead with one memorable discovery chain and use selective supporting results. Preserve causal, mechanistic, subgroup, proxy, and clinical boundaries.

## Phase 4B: Review/Synthesis route

Read `references/review-playbook.md`. Diagnose whether the literature contains a genuine field misreading, unresolved tension, hidden pattern, inferential gap, or only a descriptive mapping need.

Set:

- `synthesis_intervention`: what the review does to existing evidence;
- `editorial_thesis`: the memorable, evidence-supported interpretation the editor should retain;
- `journal_conversation`: the discussion this thesis enters and advances.

Use:

> Field misreading or unresolved tension -> synthesis intervention -> editorial thesis -> changed decision or research agenda -> journal conversation -> calibrated boundary

Do not manufacture controversy for a scoping or descriptive review. When the evidence supports mapping only, make the map, boundary, and research agenda concrete.

## Phase 5: Controlled editorial uplift

Read `references/controlled-uplift.md`. Set `controlled_uplift_level` and separate three zones:

- Zone A, scientific facts: no uplift;
- Zone B, synthesis or study interpretation: calibrated strengthening with direct evidence support;
- Zone C, editorial significance: the strongest reasonable language about changed understanding, decisions, or agenda.

For every high-promotional sentence, record the source, zone, risk, and keep/strengthen/weaken decision. Do not self-award "groundbreaking," "definitive," "authoritative," or "perfectly aligned."

## Phase 6: Bounded draft and audit loops

Read `references/loop-controller.md`. Maintain all state fields and run:

1. intake/fact loop until hard facts and routing stabilize;
2. candidate story/thesis loop with at most three alternatives;
3. draft-audit-targeted-revision loop with at most three rounds;
4. adaptive-length loop with at most two rounds after content stabilizes.

Revise failed dimensions only. Length priority is: explicit journal rule, explicit user request, submission-system limit, evidence-based journal convention, then the shortest length that completes the editorial job. Compress because of redundancy or diluted decision value, not an arbitrary universal word count.

## Phase 7: Final gates and delivery

Run the deterministic validators and perform semantic gates:

- fact and declaration traceability;
- current official journal verification;
- article-route fit;
- Research story clarity or Review thesis quality;
- claim strength and controlled uplift;
- specific journal-conversation value;
- permission compliance for prior material;
- editorial reading efficiency and non-duplication of the abstract.

Read `references/output-and-docx.md`. Deliver:

1. final cover-letter text;
2. DOCX when requested or feasible;
3. concise fact, journal, permission, story/thesis, and claim-strength audit;
4. remaining author-confirmation items;
5. exactly one final status.

Allowed statuses:

- `SUBMISSION_READY`;
- `NEEDS_AUTHOR_CONFIRMATION`;
- `NEEDS_JOURNAL_VERIFICATION`;
- `BEST_SAFE_DRAFT_WITH_UNRESOLVED_ITEMS`.

Never set `SUBMISSION_READY` if current journal information was unavailable, a fact conflict remains, declarations are incomplete, the article type is unresolved, or prior-letter use exceeded permission.

## Resource routing

- Facts and conflicts: `references/intake-and-fact-sheet.md`
- Current journal evidence: `references/journal-research-protocol.md`
- Research route: `references/research-playbook.md`
- Review route and editorial thesis: `references/review-playbook.md`
- Controlled persuasion: `references/controlled-uplift.md`
- Human benchmark analysis: `references/human-benchmark-protocol.md`
- State and stop conditions: `references/loop-controller.md`
- Branches and declarations: `references/submission-branches-and-declarations.md`
- Text, audit, and DOCX output: `references/output-and-docx.md`
