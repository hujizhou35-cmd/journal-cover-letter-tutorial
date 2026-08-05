---
name: journal-cover-letter-skill
description: Create, revise, or check a cover letter for an academic journal submission from manuscript files. Use whenever a user wants a journal submission letter, asks to tailor a cover letter to a target journal, provides manuscript materials and asks for a letter, or wants an existing academic cover letter improved. Route original research around one scientific finding and reviews around what the synthesis changes in the field's understanding. Do not use for job applications, recommendation letters, or business correspondence.
---

# Journal Cover Letter Skill v2.3

Turn verified manuscript facts into a clear, persuasive submission letter for an editor. Default to English unless the user requests another language. Prioritize biomedical and life-science submissions while remaining useful across disciplines.

## Core rules

- Treat the manuscript and author-confirmed materials as the factual source of truth. Never invent titles, results, registrations, declarations, author details, editor names, or journal requirements.
- Separate facts into `verified`, `conflict`, `missing`, and `not_applicable`. Separate factual claims from interpretation.
- Use the strongest wording the evidence supports. Accuracy should sharpen the pitch, not make it timid.
- Use different editorial logic for original research and evidence synthesis.
- Treat previous letters as user-controlled. Reuse or analyze them only within explicit permission.
- Treat an expert-authored letter as a benchmark for editorial choices, not a gold standard or factual authority.
- Verify current journal information from official sources after the author confirms the factual foundation.
- Use bounded revision loops. Reaching a loop limit is not success.
- Use scripts for deterministic extraction, validation, auditing, and DOCX generation. Keep scientific meaning and editorial judgment in model reasoning.

## 1. Intake and fact sheet

Inventory the manuscript, title page, supplements, correspondence, previous cover letters, and user instructions. Record each important item with its source:

- exact manuscript title and article type;
- study question, design, setting, population, sample size, and time frame;
- primary methods and what each method allows the study to establish;
- central findings, important null or mixed findings, sensitivity results, and stated limitations;
- registrations, ethics, funding, conflicts, preprint, data/code, and AI-use statements when applicable;
- authorship, corresponding-author details, and submission branch;
- candidate contributions and claim-boundary risks.

Set:

```text
article_type: ORIGINAL_RESEARCH | REVIEW_SYNTHESIS | OTHER_OR_UNRESOLVED
submission_branch: INITIAL | REVISION | RESUBMISSION | TRANSFER | OTHER
fact_status: verified | conflict | missing
previous_letter_permission: FORMAT_ONLY | FORMAT_AND_TONE | MAXIMUM_SUITABLE_WORDING | FACT_CHECK_ONLY | ANONYMOUS_EXPERT_BENCHMARK | NONE
```

Never resolve conflicting values by guessing. Ask a focused question or mark the item unresolved.

## 2. Previous-letter permission

Ask whether a previous cover letter exists and how it may be used:

- `FORMAT_ONLY`: copy layout properties only;
- `FORMAT_AND_TONE`: learn layout and general voice, not distinctive wording;
- `MAXIMUM_SUITABLE_WORDING`: retain suitable language only after rechecking every fact and journal detail;
- `FACT_CHECK_ONLY`: use solely to identify facts that must be verified elsewhere;
- `ANONYMOUS_EXPERT_BENCHMARK`: compare editorial decisions without copying private facts or wording;
- `NONE`: do not inspect or reuse it.

When benchmark analysis is allowed, compare problem foregrounding, gap definition, method abstraction, finding selection, implication, journal fit, omission discipline, claim strength, paragraph order, and required declarations. Learn transferable reasoning, not sentences. Never carry over names, titles, journal details, identifiers, metadata, or unsupported claims.

## 3. Author confirmation gate

Before journal research or final drafting, establish a compact confirmation record containing:

- the sourced fact sheet and unresolved items;
- article type and submission branch;
- up to six candidate contributions;
- up to three possible Research decision spines or Review editorial theses;
- declaration gaps and likely overclaim risks;
- the recorded permission for prior material.

Use `EXPLICIT_CONFIRMATION` when the user reviews that record. Use `EVIDENCE_COMPLETE_FAST_PATH` when the user has already supplied unambiguous instructions and every decision-changing fact is verified from the files or explicit prior messages. In the fast path, proceed without forcing a redundant confirmation turn, but surface any non-blocking assumptions in the audit. Ask only when a conflict, missing declaration, unclear article type, prior-letter permission issue, or other unresolved item could materially change the letter. Never use the fast path to convert a provisional fact into a confirmed one.

## 4. Current journal research

After confirmation, check current official journal or publisher sources for:

- aims, scope, readership, and accepted article type;
- cover-letter instructions and submission-system constraints;
- mandatory declarations;
- editor identity only when useful and verified;
- recent relevant articles or editorials that reveal the journal's current conversation.

Keep `official_requirement` separate from `reasoned_fit_inference`. Build journal fit in this order: (1) the journal's explicit article-type or editorial-priority criterion, (2) a concrete readership need, and only then (3) a current journal conversation when it materially sharpens the case. A specific criterion-to-contribution mapping is stronger than generic praise or a forced citation to recent content. Build a concise `journal_conversation`: what readers are discussing, where that discussion stops, and how this manuscript advances, challenges, complements, or reorganizes it. Avoid generic praise such as “perfectly aligned.” If official information cannot be checked, return `NEEDS_JOURNAL_VERIFICATION`, not `SUBMISSION_READY`.

## 5A. Original Research route

Treat the letter as a rapid editorial decision aid, not a shortened abstract. Build one `research_decision_spine`:

> Stakes -> unresolved limitation -> study response -> synthesized finding -> consequence -> journal fit

Apply these rules:

1. Start with the specific scientific, clinical, technical, environmental, or policy problem that makes the study worth attention.
2. Define what current evidence, assumptions, measurements, or routine analyses cannot resolve. “Few studies exist” is rarely enough.
3. Translate methods into capabilities. Explain what the design allowed the authors to distinguish or test; do not catalogue algorithms, software, instruments, or procedural steps unless the method itself is the innovation.
4. State one memorable conclusion or coherent finding cluster. Include supporting results only when they answer the same editorial question.
5. Explain one immediate, defensible consequence for understanding, measurement, practice, policy, or the next research decision.
6. Connect the advance to a concrete journal readership need or current conversation.

Use contrast when supported:

> Current evidence or routine analysis suggests X; this study reveals Y; therefore Z should be reconsidered, measured differently, or investigated next.

Do not manufacture opposition. Report at conclusion level rather than listing effect sizes. Include a number only when it carries the editorial argument or prevents ambiguity. Audit all null, mixed, sensitivity, subgroup, and exploratory results internally; include them only when omitting them would mislead the pitch.

Preserve boundaries through accurate verbs rather than routine limitation paragraphs:

- association is not causation;
- statistical mediation is not a proven biological mechanism;
- a proxy is not direct measurement;
- significance in one subgroup and non-significance in another is not proof of interaction;
- exploratory importance is not an individualized intervention or regulatory target.

If removing a technical detail does not change editorial judgment, remove it.

## 5B. Review and synthesis route

A Review letter should explain what becomes clearer when the evidence is brought together. Diagnose whether the literature contains:

- a genuine field misreading or conceptual confusion;
- an unresolved tension or contradictory pattern;
- a hidden cross-study pattern;
- an inferential gap;
- or only a descriptive mapping need.

Set:

```text
synthesis_intervention: what the review does to existing evidence
editorial_thesis: the memorable, evidence-supported interpretation
journal_conversation: the discussion the thesis advances
```

Build the letter around:

> Field problem -> synthesis intervention -> editorial thesis -> changed decision or research agenda -> journal fit -> calibrated boundary

Before drafting, write a one-sentence `synthesis_contrast`:

> The field commonly reads the evidence as X; the synthesis shows Y; therefore claim, practice, or research decision Z must be bounded or redirected.

Use the contrast only when the manuscript supports both X and Y. The final letter should contain one thesis and at most two supporting cross-study patterns. Counts, databases, appraisal tools, taxonomies, and named frameworks may establish credibility, but they should not become a catalogue. When a review maps evidence across stages, domains, or constructs, foreground the imbalance and its consequence rather than enumerating every cell.

Use methods, registration, search coverage, and quality appraisal to prove the synthesis is credible; do not make them the principal selling point. Prefer contributions that reorganize evidence, explain contradictions, clarify inference, create a useful taxonomy or framework, or change the field's decision logic. Do not manufacture controversy for a scoping or descriptive review. When mapping is all the evidence supports, make the map, boundary, and research agenda concrete.

A typical Review letter performs four functions:

1. identify the submission using the journal's exact article-type label when verified, and state the field problem;
2. state the synthesis intervention, one editorial thesis, and no more than two supporting patterns;
3. explain the changed decision or research agenda and map it to a verified journal criterion or readership need;
4. provide required declarations and a professional close.

Fail the Review route when the pitch can only be summarized as “a comprehensive review of an important topic.” If removing a detail does not change the editor's understanding of the thesis, consequence, or credibility, remove it.

## 6. Persuasion without overclaiming

Use three zones:

- scientific facts: no promotional uplift;
- study or synthesis interpretation: measured strengthening tied to evidence;
- editorial significance: the strongest reasonable statement about changed understanding, decisions, or research direction.

Prefer precise verbs such as `identifies`, `reveals`, `clarifies`, `reframes`, or `establishes a research agenda` when supported. Avoid self-awarded labels such as `groundbreaking`, `definitive`, `authoritative`, and `perfectly aligned`. Treat `first`, `only`, `most comprehensive`, `unprecedented`, and equivalent priority claims as verification-dependent: independently verify them or omit them. Do not weaken every claim with repetitive `may`, `might`, and `potentially`; choose the strongest accurate rung.

## 7. Declarations

Verify declarations during intake, but include one in the letter only when:

1. the journal explicitly requires it there;
2. it is standard and decision-relevant for the submission branch, including originality, exclusive consideration, author approval, or competing interests;
3. the user requests it; or
4. an unusual circumstance must be disclosed to the editor.

Do not automatically insert funding, ethics, consent, data/code, preprint, or AI-use statements merely because they were verified. Never invent missing declarations.

## 8. Bounded revision loops

Maintain at least:

```text
article_type
submission_branch
fact_status
previous_letter_permission
confirmation_mode
research_decision_spine or editorial_thesis
synthesis_intervention
synthesis_contrast for Review
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

1. an intake loop until facts and routing stabilize;
2. a route-selection loop with no more than three alternatives;
3. a draft-audit-targeted-revision loop with no more than three rounds;
4. an omission and length loop with no more than two rounds after content stabilizes.

Revise failed dimensions only. With an authorized benchmark, compare editorial effects and revise the transferable rule responsible for a material difference, then regenerate from the manuscript. Do not patch only the test letter or imitate wording. Stop when hard gates pass and further editing changes taste rather than decision value.

Apply length constraints in this order: explicit journal rule, user request, submission-system limit, evidence-based journal convention, then the shortest length that performs every editorial function. A focused one-page letter is a useful default for ordinary Research submissions when no contrary instruction exists, not a universal limit.

## 9. Final gates and delivery

Before delivery, check:

- every factual statement is traceable;
- current official journal information was verified;
- the selected route matches the article type;
- the Research decision spine or Review thesis is memorable and recoverable after one reading;
- claim strength remains within the design;
- journal fit maps a verified journal criterion or readership need to the manuscript's contribution;
- previous material was used only as permitted;
- required declarations are complete;
- no placeholders, stale journal details, repeated claims, or abstract-like lists remain.

Deliver:

1. clean final cover-letter text;
2. DOCX when requested or feasible;
3. a separate concise audit of facts, journal evidence, permission, central route, and claim strength;
4. items still requiring author confirmation;
5. exactly one final status.

Allowed statuses:

- `SUBMISSION_READY`;
- `NEEDS_AUTHOR_CONFIRMATION`;
- `NEEDS_JOURNAL_VERIFICATION`;
- `BEST_SAFE_DRAFT_WITH_UNRESOLVED_ITEMS`.

Never use `SUBMISSION_READY` when official journal information was unavailable, a fact conflict remains, declarations are incomplete, the article type is unresolved, or prior-letter use exceeded permission.

## Bundled tools and optional detail

The rules above are sufficient for the writing and decision workflow. Use the bundled resources when available:

- `references/` provides expanded rubrics, schemas, and examples;
- `scripts/extract_docx_content.py` extracts DOCX text;
- `scripts/validate_payload.py` validates structured output;
- `scripts/audit_cover_letter.py` checks placeholders and risky wording;
- `scripts/generate_audit_report.py` creates the separate audit;
- `scripts/render_cover_letter_docx.py` produces a metadata-scrubbed DOCX;
- `assets/` contains the output template and example payload.
