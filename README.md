# Journal Cover Letter Skill

[简体中文](README.zh-CN.md) · [Evolution](docs/evolution.md) · [Architecture](docs/architecture.md) · [Privacy](PRIVACY.md)

An open-source Codex Skill and Plugin that turns manuscript evidence into an editor-facing academic journal cover letter. It is designed for general scholarly publishing, with biomedical and life-science submissions as the first-class use case.

> **Current recommendation:** v2.1 (`2.1.0`). v1.0 and v2.0 remain available as Legacy releases for comparison and reproducibility.

## Why this is different from a template generator

A template can arrange paragraphs. It cannot decide which manuscript facts are reliable, whether a result supports causal or mechanistic language, what story an editor should remember, or how the work enters a journal's current scholarly conversation.

This project therefore treats a cover letter as an **editorial decision brief**:

1. identify manuscript, title-page, supplementary, and prior-letter files;
2. build a traceable fact sheet with `verified`, `conflict`, and `missing` states;
3. confirm article type, submission branch, target journal, declarations, and permissions;
4. research current official journal requirements and recent relevant conversation;
5. select a Research story or Review editorial thesis;
6. write with controlled persuasion and evidence boundaries;
7. run bounded audit and adaptive-length loops;
8. deliver text, optional DOCX, an audit, unresolved items, and a readiness status.

The default output language is English. Users can request another language.

## Two editorial routes

### Original Research

> Important problem → knowledge gap → design advantage → central finding → defensible meaning → journal conversation

The route tells one scientific discovery story. Methods support credibility rather than becoming a list. It explicitly checks causal, mechanistic, subgroup, proxy-measure, and clinical-translation boundaries.

### Review and Synthesis

> Field misreading or unresolved tension → synthesis intervention → editorial thesis → changed decision or research agenda → journal conversation → calibrated boundary

The route asks what the review changes in the field's interpretation of existing evidence. It does not force controversy onto descriptive or scoping reviews.

## Version evolution

| Public release | Manifest | Status | Main design change |
|---|---:|---|---|
| v1.0 | `1.0.0` | Legacy | Fact Sheet, journal research, previous-letter permissions, unified `1-5-1-1` iteration and audits |
| v2.0 | `2.0.0` | Legacy | Research/Review routing, scientific story selection, persuasion calibration, bounded state loops |
| v2.1 | `2.1.0` | Recommended stable | Review field diagnosis, `editorial_thesis`, controlled uplift, journal conversation, adaptive length |

The project learned from human-authored cover letters without treating them as unquestionable models. An expert letter is a **benchmark, not a gold standard**: its selection, rhythm, and promotional judgment may be useful, while every fact and claim still has to survive manuscript-level verification. See [the full evolution narrative](docs/evolution.md).

## Install

Each Release contains two independently usable packages:

- `journal-cover-letter-skill-vX.Y.skill` — standalone Skill archive;
- `journal-cover-letter-plugin-vX.Y.zip` — complete Plugin archive;
- `SHA256SUMS.txt` — integrity hashes.

For a standalone repository installation, place the extracted skill directory at:

```text
.agents/skills/journal-cover-letter-skill/
```

for a project, or in your user-level Agent Skills directory. For Plugin use, extract the Plugin archive and install/import the folder in a Codex surface that supports local plugins. The package layouts follow the current [OpenAI Skill](https://developers.openai.com/codex/build-skills) and [Plugin](https://developers.openai.com/plugins/build/plugins) documentation.

Use the Release matching the behavior you want. Do not combine a v1.0 Skill with a v2.1 Plugin manifest.

## Invoke

Attach the manuscript-related files and ask, for example:

> Analyze these files and help me prepare a cover letter for an original research submission. Stop after the fact sheet and story candidates so I can confirm them before you research the journal.

or:

> This is a scoping review. Build a truthful editorial thesis only if the evidence supports one; otherwise frame the descriptive map and research agenda without manufacturing controversy.

Expected outputs:

- final cover-letter text;
- optional DOCX;
- fact, journal, permission, story/thesis, and claim-strength audit;
- items still requiring author confirmation;
- one state: `SUBMISSION_READY`, `NEEDS_AUTHOR_CONFIRMATION`, `NEEDS_JOURNAL_VERIFICATION`, or `BEST_SAFE_DRAFT_WITH_UNRESOLVED_ITEMS`.

## Repository layout

```text
.codex-plugin/plugin.json            Plugin manifest
skills/journal-cover-letter-skill/   Installable Skill
docs/specs/                           Sanitized version specifications
examples/synthetic/                  Fictional cases only
evals/                               Behavioral evaluation set and review artifacts
tests/                               Deterministic regression tests
scripts/                             Structure, privacy, and release utilities
```

## Synthetic examples and evaluation

The public test matrix covers original research with proxy/mediation/subgroup risks, a thesis-capable systematic review, a descriptive scoping review, prior-letter permission boundaries, conflicting facts or missing declarations, unavailable journal information, and DOCX generation. See [examples/synthetic](examples/synthetic/README.md), [evals/evals.json](evals/evals.json), and the [static human-review page](evals/review.html).

No real manuscript, real cover letter, active target journal, editor identity, or unpublished submission detail is included.

## Limitations

- The project does not guarantee acceptance.
- Journal pages and policies change; current official verification is required for readiness.
- Scientific interpretation remains a model-assisted judgment and must be reviewed by the authors.
- The author is responsible for facts, declarations, ethics, conflicts, and final submission compliance.
- DOCX inheritance can reproduce layout, but it must not carry hidden text, tracked changes, metadata, or stale journal details.

## Roadmap

- Add discipline-specific branches without weakening the shared evidence gates.
- Expand multilingual output evaluation.
- Add more public, rights-cleared benchmark pairs.
- Improve reproducible human review of version comparisons.
- Consider wider plugin-directory submission only after stable public use; this repository is not currently submitted to a universal plugin directory.

## Contributing

Published articles and their related cover letters can help improve this project. Submit only materials you have the right to share publicly, and remove personal, confidential, and unpublished submission information before contributing. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Author, citation, and license

Created by **Jizhou Hu (China Medical University)**. Cite the project using [CITATION.cff](CITATION.cff). Released under the [MIT License](LICENSE).
