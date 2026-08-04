# Journal Cover Letter Skill｜投稿信撰写教程

[简体中文](docs/README.zh-CN.md) · [Latest release](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/latest) · [Privacy](docs/privacy.md)

Upload your manuscript, name the target journal, and let the Skill turn the paper's strongest contribution into a clear, checked cover letter.

**Recommended version: v2.2**

## Download

- [Codex Skill (.skill)](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/latest/download/journal-cover-letter-skill-v2.2.skill)
- [Codex Plugin (.zip)](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/latest/download/journal-cover-letter-plugin-v2.2.zip)
- [Portable SKILL.md for other AI tools](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/latest/download/SKILL.md)

| Choose this | If you want to... |
|---|---|
| `.skill` | Install the standalone Skill in Codex or another Agent Skills-compatible tool |
| Plugin `.zip` | Install the complete Codex Plugin |
| `SKILL.md` | Give the full writing and decision workflow to another AI |

The single Markdown file contains the complete writing logic. Automated DOCX creation and script-based checks require the Skill or Plugin package.

## Start in three steps

1. Download one of the three files above.
2. Upload your manuscript, title page, and any related material you want the AI to use.
3. Name the target journal and ask the AI to prepare a cover letter.

Example prompt:

> Read these manuscript files and help me write a cover letter for [Journal]. First show me the facts and main selling points you found. Wait for my confirmation before researching the journal and drafting the final letter.

If you provide an older letter, say whether it may be used for facts, layout, tone, wording, or expert comparison. The Skill will not assume permission.

## What the Skill does

1. Checks the manuscript facts and flags conflicts or missing information.
2. Confirms the article type, strongest contribution, and any previous-letter permission with you.
3. Checks the target journal's current official guidance.
4. Writes the letter using the right logic for the article type.
5. Checks claims, declarations, journal details, and unresolved placeholders.
6. Returns the final letter, an optional DOCX, a short audit, and anything you still need to confirm.

It will not call a letter submission-ready when facts conflict, required statements are missing, or current journal information cannot be verified.

## Research and Review need different letters

**Original Research** usually needs one scientific story: why the problem matters, what current work cannot resolve, what the study found, and what that finding changes.

**Review or Synthesis** follows a different logic. It should explain what becomes clearer when the evidence is brought together, reorganized, or reinterpreted. A descriptive review is not forced to invent a controversy.

## How I improve this skill

> Current Skill → privately provide manuscript materials → generate an AI letter → add an expert-authored letter → compare the two → extract the expert's reasoning → update the Skill → test again → release a new version

In practice:

1. I use the current version to generate a cover letter from manuscript materials.
2. I then provide a cover letter written by an experienced academic expert.
3. I compare what each letter selects, omits, emphasizes, and places first.
4. I study why the expert's choices may help an editor decide faster, without copying the wording.
5. I turn reusable lessons into general Skill rules.
6. I regenerate the letter with the same materials and compare again.
7. I repeat the generate–compare–extract–revise–test loop until the improvement is stable.

The expert letter is a **benchmark, not a gold standard**. Every fact and claim still has to be checked against the manuscript. Private manuscripts and real letters used in this process are never added to this repository.

## How the versions evolved

| Version | What the comparison revealed | What changed |
|---|---|---|
| v1.0 | A persuasive letter is still unsafe if its facts drift | Added fact checking, journal research, previous-letter permission, and final checks |
| v2.0 | Research and Review should not use the same writing logic | Research gained a scientific story; Review focused on what the synthesis helps the field understand |
| v2.1 | A Review should not merely say what it reviewed | Added field diagnosis, a clear new interpretation, measured promotion, and journal-conversation fit |
| v2.2 | Complex methods can hide the actual scientific finding in Research letters | Put the phenomenon and finding first, translated methods into capabilities, and removed details that do not change editorial judgment |

Read the short [development story](docs/evolution.md).

## Privacy and limits

- Real manuscripts, cover letters, journals, editors, and source conversations are not published here.
- Public examples are fully synthetic.
- The project does not guarantee acceptance.
- Journal policies can change and should be checked for every submission.
- Authors remain responsible for facts, declarations, ethics, conflicts, and the final submission.

See the [privacy policy](docs/privacy.md).

## Contributing

Published papers and their related cover letters can help improve the project. Share only material you have the right to make public, and remove personal, confidential, and unpublished submission information first. See [Contributing](.github/CONTRIBUTING.md).

## Repository guide

Ordinary users can ignore the technical folders and download a Release directly.

| Path | Purpose |
|---|---|
| `skills/` | Current v2.2 Skill source |
| `docs/` | Chinese homepage, development story, privacy, and changes |
| `development/` | Synthetic examples, tests, evaluation data, and release tools |
| `.codex-plugin/` | Codex Plugin manifest |
| `.github/` | Automated checks and contribution templates |

## Author, citation, and license

Created by **Jizhou Hu (China Medical University)**. Citation information is in [CITATION.cff](CITATION.cff). Released under the [MIT License](LICENSE).
