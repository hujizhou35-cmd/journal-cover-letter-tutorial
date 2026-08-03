---
name: journal-cover-letter-skill
description: Create, revise, or check a cover letter for an academic journal submission from manuscript files. Use whenever a user wants a journal submission letter, asks to tailor a cover letter to a target journal, provides a manuscript and asks for a letter, or wants an existing academic cover letter improved. Do not use for job applications, recommendation letters, or non-academic business correspondence.
---

# Journal Cover Letter Skill v1.0

Produce an editor-facing submission letter grounded in the manuscript, current official journal information, and the user's permissions. Default to English unless the user requests another language.

## Operating principles

- Treat manuscript files as the factual source of truth. Never invent a title, result, registration number, declaration, author detail, or journal requirement.
- Separate verified facts, conflicts, and missing information before drafting.
- Research current journal information only after the user confirms the fact sheet and contribution candidates.
- Prefer official journal and publisher sources. Record the access date and distinguish requirements from informed editorial inferences.
- Treat a previous cover letter as user-controlled material. Ask how it may be used before extracting wording, style, or formatting.
- Write an editorial decision summary, not a shortened abstract or a list of everything in the manuscript.
- Use the strongest wording the evidence permits, with explicit boundaries where overclaiming is plausible.
- Never promise acceptance. The author remains responsible for factual, declaration, and submission compliance.

## Required workflow

### 1. Inventory the inputs

Identify the main manuscript, title page, supplementary files, previous cover letter, revision correspondence, and any user-provided journal instructions. Read `references/intake-and-fact-sheet.md` and build the fact sheet defined there.

If the article type, title, core design, central findings, submission branch, or authorship/declaration information conflicts across files, pause and ask only the questions needed to resolve the conflict.

### 2. Confirm target and prior-letter permissions

Confirm the target journal's full name and the submission branch. Ask whether a previous cover letter exists and, if so, obtain one permission mode:

1. format only;
2. format and tone;
3. preserve wording where suitable;
4. fact checking only;
5. anonymous expert benchmark analysis.

Do not reuse wording or style when permission is absent or narrower than the proposed use.

### 3. Present a confirmation checkpoint

Show the user:

- the fact sheet with `verified`, `conflict`, and `missing` statuses;
- up to six candidate contributions, ranked by editorial importance;
- the article type and submission branch;
- unresolved declarations or author details.

Wait for confirmation before journal research or final drafting.

### 4. Research the target journal

Read `references/journal-research-protocol.md`. Find current official information about aims and scope, readership, accepted article type, explicit cover-letter requirements, relevant declarations, editorial contacts when required, and recent relevant scholarly conversations. Record sources and access date.

If official current information cannot be verified, continue only with a clearly labeled best safe draft and set the status to `NEEDS_JOURNAL_VERIFICATION`.

### 5. Draft and iterate with 1-5-1-1

Read `references/editorial-iteration-rubric.md`. Transform the evidence into:

- one central problem or decision;
- up to five layered contributions;
- one practical or scholarly implication with a defensible boundary;
- one journal-fit claim tied to readers or an ongoing conversation.

Use contribution labels only when they improve scanning. Each contribution should state the output and why it matters. Merge secondary details into stronger contributions rather than listing them at equal weight.

### 6. Audit

Run the deterministic payload validator and letter audit. Perform semantic checks that scripts cannot replace:

- Does every factual statement trace to a verified source?
- Does the novelty claim describe a real advance rather than routine execution?
- Is the causal, mechanistic, clinical, subgroup, and generalizability language justified?
- Does the journal-fit paragraph explain reader value rather than flatter the journal?
- Would removing a sentence change an editor's screening decision?

Revise only failed dimensions, then repeat the audit. Stop after three draft-audit rounds and two compression rounds. If a hard problem remains, return the best safe draft with unresolved items.

### 7. Deliver

Read `references/output-and-docx.md`. Provide:

1. final cover-letter text;
2. DOCX when requested or feasible;
3. a concise fact and journal-compliance audit;
4. items the author must confirm;
5. one final status: `SUBMISSION_READY`, `NEEDS_AUTHOR_CONFIRMATION`, `NEEDS_JOURNAL_VERIFICATION`, or `BEST_SAFE_DRAFT_WITH_UNRESOLVED_ITEMS`.

Never mark `SUBMISSION_READY` when facts conflict, declarations remain incomplete, or current official journal information was unavailable.

## Resources

- Intake and conflicts: `references/intake-and-fact-sheet.md`
- Current journal research: `references/journal-research-protocol.md`
- Editorial iteration: `references/editorial-iteration-rubric.md`
- Submission declarations: `references/submission-branches-and-declarations.md`
- Output and DOCX: `references/output-and-docx.md`
- Markdown letter template: `assets/cover-letter-template.md`
- Example structured payload: `assets/cover-letter-payload.example.json`

Use scripts only for deterministic work. Do not delegate story selection, contribution ranking, or scientific interpretation to keyword rules.
