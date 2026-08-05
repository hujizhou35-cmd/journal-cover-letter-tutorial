# Journal Cover Letter Skill｜投稿信撰写教程

[简体中文](docs/README.zh-CN.md)

Write a journal cover letter from manuscript files—or improve the Skill with manuscript and expert-letter examples.

## Start here

| I want to... | Use | What it does |
|---|---|---|
| Write a cover letter | **Journal Cover Letter Skill v3.2** | Reads the manuscript, checks the journal, writes the letter, and audits the result |
| Improve the Skill | **Cover Letter Skill Trainer v0.2.0** | Compares a blind AI draft with a permitted expert letter and turns useful lessons into a tested Skill update |

### Write a cover letter

- [Download the Codex Skill](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/v3.2/journal-cover-letter-skill-v3.2.skill)
- [Download the Codex Plugin](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/v3.2/journal-cover-letter-plugin-v3.2.zip)
- [Download SKILL.md for another AI](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/v3.2/SKILL.md)

### Improve the Skill

- [Download the Trainer Skill](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/trainer-v0.2.0/journal-cover-letter-skill-trainer-v0.2.0.skill)
- [Download the Trainer Plugin](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/trainer-v0.2.0/journal-cover-letter-skill-trainer-plugin-v0.2.0.zip)
- [Download the portable Trainer SKILL.md](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/trainer-v0.2.0/SKILL.md)

### Which file should I choose?

| File | Choose it when... |
|---|---|
| `.skill` | You want to install one Skill in Codex |
| Plugin `.zip` | You want the complete Codex package |
| `SKILL.md` | Your AI can read an instruction file but cannot install Codex packages |

## Write a letter in three steps

1. Upload the manuscript and any title page or supplement.
2. Tell the Skill the target journal. If an older cover letter exists, choose whether it may be used for facts, format, tone, or expert comparison.
3. Confirm any missing facts. The Skill checks current journal guidance, writes the letter, and returns a separate audit.

The default output is English. You can request another language.

## Three papers need three different letters

| Route | The letter should answer |
|---|---|
| **Research** | What scientific problem was studied, what was found, and why does the finding matter? |
| **Review** | What new understanding appears when the existing evidence is brought together? |
| **Bibliometrics** | What does the publication map reveal about the field's structure, growth, fragmentation, collaboration, or direction of travel? |

## Why Bibliometrics needs its own route

A bibliometric paper studies publications, citations, keywords, authors, institutions, and networks. Its main result is a map of a research field—not a treatment effect, mechanism, or ordinary summary of study findings.

A useful bibliometric cover letter asks:

1. What literature was mapped?
2. What previously unclear structure or change became visible?
3. Which topics, collaborations, or research directions are changing?
4. Why does that change matter to this journal's readers?
5. What cannot be concluded from publication counts, citations, or network position alone?

The journal may label the paper `Review` or `Original Research`. The Skill keeps that official label while still using the Bibliometrics writing route.

## Train the Skill with expert examples

The Trainer removes the need to repeat the improvement process by hand:

```text
Current Skill
→ manuscript materials
→ blind AI cover letter
→ permitted expert cover letter
→ compare the two decisions
→ extract reusable reasoning
→ revise the Skill
→ test again in a fresh context
→ release only after review
```

The Trainer learns how the expert selected facts, ordered the argument, and made the work relevant to an editor. It does not copy the expert's wording. The manuscript remains the source of truth, because an expert letter can still contain an older title, number, journal detail, or declaration.

A clean first draft is not enough for a blind improvement loop. After the expert letter is revealed, every candidate must be generated in a new context that has not received the expert material. See the [beginner Trainer guide](docs/trainer-guide.md).

## How I improve this project

1. Ask the current Skill to write from a manuscript.
2. Add a permitted expert-authored letter after the AI draft is sealed.
3. Compare what each letter selected, omitted, ordered, and emphasized.
4. Explain why the stronger choices help an editor; do not copy sentences.
5. Turn the reusable idea into a general Skill rule.
6. Generate again from the same manuscript in a fresh context.
7. Check the changed route and the routes that were not changed.
8. Publish when the improvement is useful beyond one example.

An expert letter is a benchmark, not a gold standard. Persuasion never overrides factual accuracy or evidence boundaries. Private manuscripts and real letters stay outside this repository.

## How the versions evolved

| Version | What the comparison revealed | What changed |
|---|---|---|
| v1.0 | A useful letter must first keep titles, numbers, authors, declarations, and journal rules accurate | Added a manuscript fact sheet, journal checks, permission for older letters, and a final audit |
| v2.0 | Research and Review should not use the same argument | Research tells one scientific discovery story; Review explains the new understanding created by synthesis |
| v2.1 | Review letters often report what was reviewed without saying what changed | Added field diagnosis, a memorable interpretation, measured promotion, and direct reader relevance |
| v2.2 | Research letters can let complex methods and result lists hide the discovery | Put the scientific finding first and describe methods by the credibility they add |
| v2.3 | Review conclusions could still be broad and the workflow could repeat questions already answered | Added a clear “old reading → synthesis finding → changed decision” contrast, a fast path for complete evidence, and stronger checks against empty promotion |
| **v3.0** | **Bibliometrics is neither ordinary Research nor a traditional Review** | **Added a third Bibliometrics route and separated the journal's official article label from the way the letter should argue** |
| v3.1 | A polished bibliometric letter can become so abstract that it loses the paper's own results | Required a manuscript-specific map, frontier signal, or directional shift and added blind benchmark testing |
| **v3.2** | Expert letters can contain stale facts, and bibliometric letters can overfocus on rankings or keywords | Keeps manuscript facts authoritative, joins performance analysis with science mapping, makes journal fit specific, and removes submission-system-only details |

Trainer development:

| Version | What changed |
|---|---|
| Trainer v0.1.0 | Added blind baseline generation, expert comparison, reusable rule extraction, candidate building, and regression checks |
| Trainer v0.2.0 | Requires a fresh expert-free context for every candidate round and records the real isolation level |

See [the full development story](docs/evolution.md) and [Trainer changes](docs/trainer-changelog.md).

## Privacy and limits

- Real manuscripts and expert letters are not published here.
- Public examples are fictional.
- Previous letters are used only with permission.
- The project does not guarantee acceptance.
- Authors remain responsible for the final facts, declarations, and submission rules.

See the [privacy policy](docs/privacy.md).

## Contributing

Published papers and their cover letters can help improve this project. Share only material you have the right to disclose, and remove personal, confidential, and unpublished submission information first. See [CONTRIBUTING](.github/CONTRIBUTING.md).

## Repository guide

Most users can ignore the folders below and download a Release directly.

| Path | Purpose |
|---|---|
| `skills/` | Current Writer and Trainer source |
| `docs/` | Chinese homepage, beginner guides, privacy, and version story |
| `development/` | Fictional examples, tests, and package builders |
| `.codex-plugin/` | Writer Plugin metadata |
| `.github/` | Automated checks and contribution forms |

## Author, citation, and license

Created by **Jizhou Hu, China Medical University**.

Licensed under the [MIT License](LICENSE). Citation metadata is available in [CITATION.cff](CITATION.cff).
