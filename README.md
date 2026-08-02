# Journal Cover Letter Skill

[简体中文](README.zh-CN.md)

An open-source Codex Skill and Plugin for turning manuscript evidence into an editor-facing academic journal cover letter. It prioritizes biomedical and life-science workflows while remaining useful across academic fields.

Unlike a template generator, the project first builds a traceable fact sheet, confirms what may be learned from any previous letter, checks current official journal requirements, selects the contribution story, and audits claims before producing text or DOCX output.

## Workflow

1. Identify manuscript, title-page, supplementary, and previous-letter files.
2. Build a `verified/conflict/missing` fact sheet.
3. Confirm article type, submission branch, target journal, declarations, and prior-letter permission.
4. Research current official journal requirements and readership after author confirmation.
5. Convert the manuscript into one central editorial problem and layered contributions.
6. Run bounded draft, audit, and compression loops.
7. Deliver the letter, optional DOCX, audit report, unresolved items, and readiness status.

## Version 1.0

This release establishes the fact-grounded `1-5-1-1` workflow: one central problem, up to five layered contributions, one bounded implication, and one journal-specific reader-value claim.

## Install

Install either the standalone Skill package or the Plugin package from the matching GitHub Release. The repository root is also a valid plugin source, with the skill stored under `skills/journal-cover-letter-skill/`.

Invoke it with a request such as:

> Analyze these manuscript files and help me prepare a cover letter for an academic journal submission.

The default output language is English. Ask for another language when needed.

## Privacy

Do not commit confidential manuscripts, unpublished submission material, identifiable correspondence, or real journal-research captures. The included examples are synthetic. See [PRIVACY.md](PRIVACY.md).

## Limitations

This project does not guarantee acceptance and does not replace author review of facts, declarations, ethics, conflicts, journal policy, or submission compliance.

## Contributing

Published articles and their related cover letters can help improve this project. Submit only materials you have the right to share publicly, and remove personal, confidential, and unpublished submission information before contributing. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Author and license

Created by **Jizhou Hu (China Medical University)**. Released under the [MIT License](LICENSE). Citation metadata is provided in [CITATION.cff](CITATION.cff).
