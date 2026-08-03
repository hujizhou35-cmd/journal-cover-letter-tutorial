# Journal Cover Letter Skill

[简体中文](README.zh-CN.md) · [How the project evolved](docs/evolution.md) · [Privacy](PRIVACY.md)

An open-source Skill and Codex Plugin for writing academic journal cover letters from manuscript files.

Upload your manuscript and related files. The Skill checks the facts, asks what it may reuse from an older cover letter, looks up the target journal's current official guidance, and drafts a letter for that submission.

It is designed for general academic publishing, with biomedical and life-science research as the main use case. English is the default output language, but you can request another language.

> **Recommended version:** v2.1. Earlier versions are kept so the project's development can be reviewed and reproduced.

## What you get

- A submission-ready cover letter draft
- An optional DOCX file
- A short check of the facts, journal requirements, and claim strength
- A clear list of anything the author still needs to confirm

The Skill will not mark a letter as ready when manuscript facts conflict, required statements are missing, or current journal guidance cannot be checked.

## How it works

1. Reads the manuscript, title page, supplements, and any previous cover letter.
2. Shows the author the facts and strongest contributions it found.
3. Asks how an older cover letter may be used: for facts, layout, tone, wording, or expert comparison.
4. After author confirmation, checks the target journal's current official information.
5. Writes a letter suited to the article type.
6. Checks for unsupported claims, missing statements, stale journal details, and unresolved placeholders.
7. Returns the letter, optional DOCX, and a short review note.

## Research and Review articles

For **Original Research**, the letter tells one clear discovery story: the problem, what the study did differently, the main finding, and why it matters to the journal's readers.

For **Reviews**, the letter explains what becomes clearer when the evidence is brought together. A systematic review may correct a misunderstanding or offer a new interpretation. A descriptive or scoping review is not forced to claim a controversy it cannot support.

## How this project was developed

The project began after comparing AI-written cover letters with cover letters written by an experienced academic expert.

The AI drafts were usually careful and complete, but they could read like short abstracts and sometimes sounded too cautious. The expert letters were more selective: they chose one main message, wrote from the editor's point of view, and used confident but measured promotion.

The Skill was revised to combine both strengths:

- the AI's fact checking and consistency;
- the expert's focus, story, rhythm, and editorial judgment;
- clear limits on causal, mechanistic, subgroup, and clinical claims.

An expert letter is used as a **benchmark, not an answer key**. Its writing choices can be studied, but its facts and claims must still be checked against the manuscript. Real manuscripts, letters, journals, and source conversations used during development are not included in this repository.

| Version | What changed | Status |
|---|---|---|
| v1.0 | Added manuscript fact checking, journal research, permission rules for older letters, and final checks. | Legacy |
| v2.0 | Recognized that Research often needs a discovery story, while a Review follows a different logic: it explains what the synthesis helps the field understand. | Legacy |
| v2.1 | Improved the Review route so it can present a clear new interpretation without overstating the evidence. | Recommended |

Read the [full, privacy-safe development story](docs/evolution.md).

## Quick start

Attach your files and ask in plain language:

> Read these manuscript files and help me write a cover letter for [Journal]. First show me the facts and main selling points you found. Wait for my confirmation before checking the journal and drafting the final letter.

If you have an older letter, state how it may be used:

> Use this previous cover letter only as a guide to layout and tone. Do not reuse its journal details or scientific claims without checking them.

## Install

Each GitHub Release provides:

- `journal-cover-letter-skill-vX.Y.skill` — standalone Skill package
- `journal-cover-letter-plugin-vX.Y.zip` — Codex Plugin package
- `SHA256SUMS.txt` — download checksums

For a project-level standalone installation, extract the Skill to:

```text
.agents/skills/journal-cover-letter-skill/
```

New users should normally install v2.1. Do not mix files from different releases.

## Examples, tests, and technical details

All examples are fictional. They test common risks such as overstated causality, missing declarations, unverified journal information, and accidental reuse of an older letter.

- [Synthetic examples](examples/synthetic/README.md)
- [Version comparison](evals/benchmark.md)
- [Simple workflow diagram](docs/architecture.md)
- [Detailed version specifications](docs/specs/)

## Limits

- The Skill cannot guarantee acceptance.
- Journal policies change and must be checked again for each submission.
- Authors remain responsible for the manuscript facts, declarations, ethics, conflicts of interest, and final submission.

## Contributing

Published articles and their related cover letters can help improve the project. Submit only materials you have the right to share, and remove personal, confidential, and unpublished submission information first. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Author and license

Created by **Jizhou Hu (China Medical University)**. Citation information is in [CITATION.cff](CITATION.cff). Released under the [MIT License](LICENSE).
