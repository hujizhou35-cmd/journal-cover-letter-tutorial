# Journal Cover Letter Skill v2.0

[简体中文](README.zh-CN.md)

An open-source Skill and Codex Plugin for writing academic journal cover letters from manuscript files.

Version 2.0 keeps the fact and journal checks from v1.0, but changes how different article types are presented to editors.

> **Status:** Legacy. New users should normally choose v2.1.

## The key idea behind v2.0

Original Research and Reviews should not follow the same writing logic.

- **Original Research often needs a story.** The letter should move from the problem to what the study did differently, the central finding, and why it matters.
- **A Review does not have to imitate that story.** Its job is to explain what becomes clearer when existing evidence is combined and reorganized.

This idea grew from comparing careful but flat AI drafts with more selective expert-authored cover letters. Version 2.0 also uses stronger language when the evidence supports it, while continuing to check causal, mechanistic, subgroup, and clinical claims.

## How it works

1. Reads manuscript files and any older cover letter.
2. Shows the author the facts and main selling points it found.
3. Asks how the older letter may be used.
4. Checks the target journal's current official guidance after author confirmation.
5. Chooses the Research or Review writing logic.
6. Drafts, checks, and revises the letter a limited number of times.
7. Returns the text, optional DOCX, and anything the author still needs to confirm.

## Quick start

> Read these manuscript files and help me write a cover letter for [Journal]. First show me the facts and main selling points. Then use the correct approach for an Original Research article or Review.

## Install

Download the v2.0 standalone Skill package or Plugin package from the matching GitHub Release. Do not mix it with files from another version.

## Privacy and limits

The examples are fictional. Real manuscripts, letters, journals, and source conversations used during development are not included.

The Skill cannot guarantee acceptance. Authors remain responsible for facts, declarations, ethics, conflicts of interest, journal policy, and final submission.

## Contributing

Only share published or fictional materials that you have the right to make public. Remove personal, confidential, and unpublished submission information first. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Author and license

Created by **Jizhou Hu (China Medical University)**. Released under the [MIT License](LICENSE). Citation information is in [CITATION.cff](CITATION.cff).
