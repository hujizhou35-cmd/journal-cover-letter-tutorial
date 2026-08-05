---
name: journal-cover-letter-skill
description: Create, revise, benchmark, or check a cover letter for an academic journal submission from manuscript files. Use whenever a user wants a journal submission letter, asks to tailor a cover letter to a target journal, provides manuscript materials and asks for a letter, wants an existing academic cover letter improved, or submits a bibliometric/science-mapping manuscript. Route empirical research around one finding, evidence syntheses around what the synthesis changes in understanding, and bibliometric studies around what the map reveals about a field's structure or evolution. Do not use for job applications, recommendation letters, or business correspondence.
---

# Journal Cover Letter Skill v3.0

Turn verified manuscript facts into a clear editorial decision aid. Default to English unless the user requests another language. Prioritize biomedical and life-science submissions while remaining useful across disciplines.

## Core architecture: evidence anchor -> editorial meaning

Every persuasive claim must contain both parts:

- `empirical_anchor`: the concrete, manuscript-traceable observation selected for the editor;
- `editorial_meaning`: what that observation changes in understanding, interpretation, coordination, practice, or the next research decision.

A letter fails when it offers facts without meaning or meaning without a traceable factual anchor. This is the central v3.0 rule.

## Core rules

- Treat the manuscript and author-confirmed materials as the factual source of truth. Never invent titles, results, registrations, declarations, author details, editor names, or journal requirements.
- Separate facts into `verified`, `conflict`, `missing`, and `not_applicable`. Separate factual claims from interpretation.
- Use the strongest wording the evidence supports. Accuracy should sharpen the pitch, not make it timid.
- Separate the journal's official submission label from the manuscript's intellectual route. They may differ.
- Treat previous letters as user-controlled. Reuse or analyze them only within explicit permission.
- Treat an expert-authored letter as evidence of selection and editorial judgment, not as a gold standard or factual authority.
- Verify current journal information from official sources after the factual foundation is stable.
- Use bounded revision loops. Reaching a loop limit is not success.
- Use scripts for deterministic extraction, validation, auditing, and DOCX generation. Keep scientific meaning and editorial judgment in model reasoning.

## 1. Intake, routing, and fact sheet

Inventory the manuscript, title page, supplements, correspondence, previous cover letters, and user instructions. Record each important item with its source.

Set:

```text
official_article_type: exact journal label | UNRESOLVED
intellectual_route: ORIGINAL_RESEARCH | REVIEW_SYNTHESIS | BIBLIOMETRICS | OTHER_OR_UNRESOLVED
submission_branch: INITIAL | REVISION | RESUBMISSION | TRANSFER | INVITED | OTHER
fact_status: verified | conflict | missing | not_applicable
previous_letter_permission: FORMAT_ONLY | FORMAT_AND_TONE | MAXIMUM_SUITABLE_WORDING | FACT_CHECK_ONLY | ANONYMOUS_EXPERT_BENCHMARK | NONE
```

### Route by the primary evidence object

- `ORIGINAL_RESEARCH`: the central evidence comes from participants, specimens, experiments, observations, surveys, clinical records, models, or other primary empirical data.
- `REVIEW_SYNTHESIS`: the central evidence comes from the substantive findings of included studies, and the contribution is a changed interpretation, boundary, taxonomy, or evidence-based agenda.
- `BIBLIOMETRICS`: the central evidence comes from bibliographic metadata, citations, terms, authorship, affiliations, journals, or networks, and the contribution is a map of field structure, evolution, concentration, connectivity, or emerging attention.

Do not infer the intellectual route from the journal's article-type label. A bibliometric manuscript may be submitted under `Original Research`, `Review`, `Systematic Review`, or another journal-specific label. Record both fields explicitly.

For hybrid manuscripts, choose the route that carries the main editorial contribution. If bibliometric analyses merely support a substantive evidence synthesis, use `REVIEW_SYNTHESIS`. If the map itself is the main result, use `BIBLIOMETRICS`.

Never resolve conflicting values by guessing. Ask a focused question or mark the item unresolved.

## 2. Previous-letter permission and benchmark extraction

Ask whether a previous cover letter exists and how it may be used:

- `FORMAT_ONLY`: copy layout properties only;
- `FORMAT_AND_TONE`: learn layout and general voice, not distinctive wording;
- `MAXIMUM_SUITABLE_WORDING`: retain suitable language only after rechecking every fact and journal detail;
- `FACT_CHECK_ONLY`: use solely to identify facts that must be verified elsewhere;
- `ANONYMOUS_EXPERT_BENCHMARK`: compare editorial decisions without copying private facts or wording;
- `NONE`: do not inspect or reuse it.

When benchmark analysis is allowed, extract two independent strengths:

1. `benchmark_empirical_signal`: which concrete manuscript facts, trends, or contrasts the human considered worth foregrounding;
2. `benchmark_editorial_logic`: how the letter converted selected evidence into a reason for editorial action.
Do not reduce benchmark analysis to sentence length, tone, or lexical similarity. Learn the human's selection intelligence and editorial reasoning. Combine the strongest factual signal with the clearest defensible meaning.

Never carry over names, titles, journal details, identifiers, metadata, declarations, or unsupported claims.

## 3. Author confirmation gate

Before journal research or final drafting, establish a compact confirmation record containing:

- the sourced fact sheet and unresolved items;
- exact `official_article_type` and selected `intellectual_route`;
- `empirical_anchor` and `editorial_meaning`;
- up to six candidate contributions;
- up to three route-specific decision spines or theses;
- declaration gaps and likely overclaim risks;
- the recorded permission for prior material.

Use `EXPLICIT_CONFIRMATION` when the user reviews that record. Use `EVIDENCE_COMPLETE_FAST_PATH` when the user has already supplied unambiguous instructions and every decision-changing fact is verified. Ask only when a conflict, missing declaration, unclear official article type, unclear route, prior-letter permission issue, or other unresolved item could materially change the letter.

## 4. Current journal research

After the factual foundation is stable, check current official journal or publisher sources for:

- aims, scope, readership, and accepted article types;
- the exact article-type label available in the target section;
- cover-letter instructions and submission-system constraints;
- mandatory declarations;
- editor identity only when useful and verified;
- recent relevant articles or editorials when they materially sharpen fit.

Keep `official_requirement` separate from `reasoned_fit_inference`. Do not rename the submission type to match the intellectual route. Build journal fit in this order: (1) explicit article-type or editorial-priority criterion, (2) concrete readership need, then (3) current journal conversation when useful.

If official information cannot be checked, return `NEEDS_JOURNAL_VERIFICATION`, not `SUBMISSION_READY`.

## 5A. Original Research route

Build one `research_decision_spine`:

> Stakes -> unresolved limitation -> study response -> empirical anchor -> synthesized finding -> editorial meaning -> journal fit

Rules:

1. Foreground the specific problem that makes the study worth attention.
2. Define the inference, measurement, or decision that current evidence cannot resolve.
3. Translate methods into capabilities rather than cataloguing tools.
4. Select one concrete finding anchor and one coherent conclusion.
5. State one immediate, defensible consequence.
6. Connect that consequence to a verified journal criterion or readership need.

Use contrast only when supported. Preserve design boundaries through accurate verbs.

## 5B. Review and synthesis route

Set:

```text
synthesis_intervention: what the review does to existing evidence
editorial_thesis: the memorable, evidence-supported interpretation
synthesis_contrast: the field reading that the synthesis confirms, bounds, or redirects
```

Build:

> Field problem -> synthesis intervention -> empirical anchor -> editorial thesis -> editorial meaning -> changed decision or research agenda -> journal fit -> calibrated boundary

Use one thesis and at most two supporting cross-study patterns. Methods, registration, search coverage, appraisal tools, and included-study counts establish credibility; they are not the intellectual contribution by themselves. Do not manufacture controversy for a descriptive or scoping review.

## 5C. Bibliometrics route

Use this route when the manuscript's principal contribution is field-level mapping from publication metadata, citation relations, term relations, collaboration networks, or temporal patterns.

Set:

```text
bibliometric_mode: PERFORMANCE_ANALYSIS | SCIENCE_MAPPING | BOTH
mapping_intervention: what previously invisible field structure or evolution the analysis makes visible
mapping_thesis: the one memorable field-level interpretation
bibliometric_decision_spine: field-scale uncertainty -> bounded corpus -> mapping capability -> empirical anchor -> mapping thesis -> coordination or research consequence -> journal fit -> metric boundary
metric_boundary: the database, time, metric, and inferential limits that constrain the interpretation
```

The letter should answer four questions:

1. What field-level uncertainty prevents researchers or clinicians from orienting their next work?
2. What structure, transition, concentration, fragmentation, or underconnection does the map reveal?
3. Why does that pattern change research coordination, validation priorities, collaboration, or topic selection?
4. Which metric boundary must be retained so that the map is not mistaken for quality, causality, or prediction?

Use one primary map-level conclusion and at most two supporting patterns. Publication counts, software names, centrality values, and country rankings remain credibility details unless they directly carry the interpretation.

Do not equate:

- publication or citation volume with research quality;
- centrality with causal influence;
- co-occurrence with conceptual validity;
- a database-indexed corpus with the complete field;
- citation bursts with certain future trends;
- output concentration with clinical or scientific leadership.

Prefer `maps`, `shows concentration`, `identifies a thematic transition`, `reveals fragmentation`, `indicates emerging attention`, or `defines a coordination gap`. Use `predicts`, `proves`, `dominates`, `most influential`, or `future direction` only when the manuscript and metric design directly justify them.

A bibliometric letter fails when it is only a catalogue of databases, software, countries, institutions, journals, clusters, or keywords. The map must be converted into a field-level decision.

## 6. Evidence-to-meaning gate

Before drafting each substantive paragraph, record:

```text
empirical_anchor: source-traceable fact or pattern
editorial_meaning: defensible implication for understanding or decision
claim_zone: FACT | INTERPRETATION | EDITORIAL_SIGNIFICANCE
```

No free-floating abstractions. No uninterpreted fact lists. If the anchor changes, regenerate the meaning; if the meaning cannot be traced, weaken or remove it.

## 7. Persuasion without overclaiming

Use three zones:

- scientific facts: no promotional uplift;
- study, synthesis, or mapping interpretation: measured strengthening tied to evidence;
- editorial significance: the strongest reasonable statement about changed understanding or decisions.

Priority claims such as `first`, `only`, `most comprehensive`, `most influential`, or `unprecedented` require independent verification or omission. For bibliometrics, ranking and forecasting language receives additional scrutiny.

## 8. Declarations

Verify declarations during intake, but include one in the letter only when:

1. the journal explicitly requires it there;
2. it is standard and decision-relevant for the submission branch;
3. the user requests it; or
4. an unusual circumstance must be disclosed.

Do not automatically insert funding, ethics, consent, data/code, preprint, or AI-use statements merely because they were verified. Never invent missing declarations.

## 9. Bounded revision loops

Maintain at least:

```text
official_article_type
intellectual_route
submission_branch
fact_status
previous_letter_permission
confirmation_mode
empirical_anchor
editorial_meaning
research_decision_spine or editorial_thesis or mapping_thesis
synthesis_intervention and synthesis_contrast for Review
bibliometric_mode, mapping_intervention, bibliometric_decision_spine, and metric_boundary for Bibliometrics
journal_conversation
journal_fit_basis
controlled_uplift_level
hard_gate_failures
quality_gate_failures
draft_round
length_round
stop_reason
```

Run:

1. an intake and route-stability loop;
2. a route-selection loop with no more than three alternatives;
3. a draft-audit-targeted-revision loop with no more than three rounds;
4. an omission and length loop with no more than two rounds.

Revise failed dimensions only. With an authorized benchmark, preserve the strongest `benchmark_empirical_signal`, then improve the transferable editorial rule responsible for any material weakness. Do not imitate wording.

## 10. Final gates and delivery

Before delivery, check:

- every factual statement is traceable;
- current official journal information was verified;
- `official_article_type` is exact and does not conflict with the submission system;
- the intellectual route matches the primary evidence object;
- the empirical anchor and editorial meaning are both recoverable after one reading;
- route-specific spine or thesis is coherent;
- claim strength remains within the design or metric;
- journal fit maps a verified criterion or readership need to the contribution;
- previous material was used only as permitted;
- required declarations are complete;
- no placeholders, stale journal details, abstract-like lists, or metric catalogues remain.

Deliver:

1. clean final cover-letter text;
2. DOCX when requested or feasible;
3. a concise audit of facts, journal evidence, route, evidence anchor, editorial meaning, and claim strength;
4. items still requiring author confirmation;
5. exactly one final status.

Allowed statuses:

- `SUBMISSION_READY`;
- `NEEDS_AUTHOR_CONFIRMATION`;
- `NEEDS_JOURNAL_VERIFICATION`;
- `BEST_SAFE_DRAFT_WITH_UNRESOLVED_ITEMS`.

Never use `SUBMISSION_READY` when official journal information was unavailable, a fact conflict remains, declarations are incomplete, the official article type is unresolved, or prior-letter use exceeded permission.

## Bundled tools and optional detail

- `references/` provides route playbooks, benchmark rules, and audit rubrics;
- `scripts/extract_docx_content.py` extracts DOCX text;
- `scripts/validate_payload.py` validates structured output;
- `scripts/audit_cover_letter.py` checks placeholders and risky wording;
- `scripts/generate_audit_report.py` creates the separate audit;
- `scripts/render_cover_letter_docx.py` produces a metadata-scrubbed DOCX;
- `assets/` contains templates and example payloads.
