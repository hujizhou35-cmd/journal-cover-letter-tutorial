---
name: journal-cover-letter-skill
description: Create, revise, or check a cover letter for an academic journal submission from manuscript files. Use whenever a user wants a journal submission letter, asks to tailor a cover letter to a target journal, provides a manuscript and asks for a letter, or wants an existing academic cover letter improved. For original research, organize the letter around one discovery story; for reviews, explain what the synthesis helps the field understand. Do not use for job applications, recommendation letters, or non-academic business correspondence.
---

# Journal Cover Letter Skill v2.0

Produce an editor-facing submission argument grounded in verified manuscript facts, current official journal information, and user-authorized benchmark material. Default to English unless another language is requested.

## Core commitments

- Treat manuscript files as the factual source of truth. Never invent facts, declarations, authorship details, or journal requirements.
- Use the strongest wording the evidence permits. Accuracy is not a reason to write a flat, defensive letter.
- Route `ORIGINAL_RESEARCH` and `REVIEW_SYNTHESIS` through different narratives. Never silently force other formats into either route.
- Treat any previous letter as user-controlled material. Obtain a permission mode before learning from it.
- Research current official journal information after the user confirms the factual foundation and route.
- Use bounded, state-based loops. Do not claim readiness merely because the loop limit was reached.
- Use deterministic scripts for extraction, payload validation, DOCX work, placeholders, and risk flags. Keep scientific interpretation and story selection in model judgment.

## Workflow

### 1. Intake and fact loop

Read `references/intake-and-fact-sheet.md`. Inventory the manuscript, title page, supplements, previous letter, correspondence, and user-provided instructions. Build a source-traceable fact sheet with `verified`, `conflict`, `missing`, and `not_applicable` states.

Classify `article_type` as `ORIGINAL_RESEARCH`, `REVIEW_SYNTHESIS`, or `OTHER_OR_UNRESOLVED`. Classify the submission branch. Resolve hard conflicts; never guess.

### 2. Previous-letter permission

Ask whether a previous cover letter exists. Record exactly one permission:

1. `FORMAT_ONLY`;
2. `FORMAT_AND_TONE`;
3. `MAXIMUM_SUITABLE_WORDING`;
4. `FACT_CHECK_ONLY`;
5. `ANONYMOUS_EXPERT_BENCHMARK`;
6. `NONE`.

Do not reuse wording, style, or layout outside the granted scope. A human-authored benchmark is a source of decisions to analyze, not a gold standard.

### 3. Human confirmation gate

Present the fact sheet, article type, submission branch, up to six contribution candidates, up to three candidate story angles, declaration gaps, and previous-letter permission. Wait for confirmation before journal research or final drafting.

### 4. Current journal research

Read `references/journal-research-protocol.md`. Verify official author instructions, aims/scope, readership, accepted article type, cover-letter requirements, declarations, current editor name only when needed, and recent relevant journal conversation. Record sources, access date, and whether each item is a requirement or an inference.

If official current information cannot be verified, use `NEEDS_JOURNAL_VERIFICATION`.

### 5. Select the route and story

For `ORIGINAL_RESEARCH`, read `references/research-playbook.md`. Select one scientific decision story:

> Important problem -> knowledge gap -> design advantage -> central finding -> defensible meaning -> journal-reader relevance

For `REVIEW_SYNTHESIS`, read `references/review-playbook.md`. Select one synthesis story:

> Field problem -> evidence base -> synthesis innovation -> new framework or insight -> evidence boundary -> implications

For `OTHER_OR_UNRESOLVED`, explain why neither route is reliable and request confirmation or use a clearly labeled fallback.

### 6. Draft with calibrated persuasion

Read `references/persuasion-calibration.md`. State concrete novelty and why the work deserves attention now. Put the central contribution before limitations. Use evidence boundaries where they prevent a plausible misreading; do not make every sentence timid.

### 7. Run bounded loops

Read `references/loop-controller.md` and maintain the state object. Use:

- intake/fact loop until hard facts and route are stable;
- story-selection loop for up to three candidate angles;
- draft-audit-targeted-revision loop for at most three rounds;
- compression loop for at most two rounds after content stabilizes.

Revise failed dimensions only. Stop on pass, required user input, missing current journal evidence, loop exhaustion, or diminishing returns.

### 8. Audit and deliver

Run deterministic validation and semantic gates. Check fact traceability, route fit, story clarity, claim strength, journal-reader value, required declarations, previous-letter permission, and editorial reading efficiency.

Read `references/output-and-docx.md`. Deliver final text, optional verified DOCX, a concise audit, author-confirmation items, and exactly one status:

- `SUBMISSION_READY`;
- `NEEDS_AUTHOR_CONFIRMATION`;
- `NEEDS_JOURNAL_VERIFICATION`;
- `BEST_SAFE_DRAFT_WITH_UNRESOLVED_ITEMS`.

Never mark `SUBMISSION_READY` when facts conflict, mandatory declarations are incomplete, article type is unresolved, previous-letter use exceeds permission, or official journal information was unavailable.

## Resource routing

- Intake, conflicts, and contribution candidates: `references/intake-and-fact-sheet.md`
- Official journal research: `references/journal-research-protocol.md`
- Original research narrative: `references/research-playbook.md`
- Review/synthesis narrative: `references/review-playbook.md`
- Persuasion and claim calibration: `references/persuasion-calibration.md`
- State and bounded loops: `references/loop-controller.md`
- Declarations and branches: `references/submission-branches-and-declarations.md`
- Output and DOCX: `references/output-and-docx.md`
