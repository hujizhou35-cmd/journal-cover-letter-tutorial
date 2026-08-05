# How the project evolved

[简体中文](evolution.zh-CN.md)

The project improves through one private loop:

> current Skill → manuscript → blind AI letter → permitted expert letter → compare decisions → extract reusable reasoning → revise the Skill → retest in a fresh context → release

The goal is not to copy an expert's sentences. The comparison asks what each letter selected, omitted, ordered, and emphasized—and why those choices change an editor's reading. The manuscript remains the factual source of truth.

## v1.0: make the letter reliable

The first version addressed fact drift. It added a sourced fact sheet, author confirmation, current official journal checks, permission before using an older letter, and a final audit.

## v2.0: separate Research from Review

A public-database Research comparison showed that a safe workflow could still be too uniform. Research usually needs one discovery story. Review needs to explain what becomes newly understood after evidence is combined. v2.0 created separate routes and kept causal, mechanistic, subgroup, proxy, and clinical limits.

## v2.1: make Review consequential

A medical-education Review comparison showed that an expert letter did more than report the search. It diagnosed how the field was reading the evidence and explained what the synthesis changed. v2.1 added honest field diagnosis, a memorable interpretation, measured promotion, direct reader relevance, and flexible length.

## v2.2: put the Research finding first

Another Research comparison showed that AI could make complex methods the main character. v2.2 foregrounded the scientific phenomenon and finding, translated methods into credibility, merged supporting results, and removed details that did not change editorial judgment.

## v2.3: sharpen the Review contrast

Review drafts could still end in broad claims. v2.3 added a simple contrast: what the field commonly assumes, what the synthesis shows, and what decision should change. It also added a fast path when the evidence is already complete and stronger checks against empty promotion.

## v3.0: add Bibliometrics as a third route

This was the major architectural change. Bibliometrics maps publications, citations, terms, authors, institutions, and networks. Its contribution is the structure or evolution of a field—not an experimental finding and not a traditional synthesis of study outcomes.

v3.0 therefore added a separate Bibliometrics route and separated two questions:

- What official article label does the journal use?
- What reasoning route should the cover letter use?

A bibliometric manuscript may be labeled `Review` or `Original Research` by the journal while still needing the Bibliometrics argument.

## v3.1: keep the paper's empirical identity

A blind bibliometric comparison recovered the broad field-level message but compressed away the manuscript's distinctive taxonomy, frontier terms, and directional shift. v3.1 required a compact manuscript-specific signature and added a blind baseline protocol before expert reveal.

## v3.2: protect facts and join both bibliometric evidence families

A later comparison showed that expert letters can contain earlier titles or numbers. v3.2 learns the expert's selection logic but never inherits stale facts. It also requires `BOTH` studies to use one performance-analysis signal and one science-mapping signal for the same thesis, connects journal fit to a specific mapped contribution, and removes submission-system-only details from the letter.

## Trainer v0.1.0 and v0.2.0

Trainer v0.1.0 turned the manual loop into a reusable Skill. It added a blind baseline, expert comparison, transferable-rule hypotheses, candidate building, holdouts, protected-route regression checks, and human approval.

Trainer v0.2.0 corrected an important blind-testing mistake: delaying the expert until after the first draft protects only that draft. Every later candidate must be generated in a fresh context that has not received the expert material. The Trainer now records the actual isolation level and context evidence.

## Privacy

Private manuscripts, real expert letters, journal details, research variables, and identifying filenames are not published. Public examples are fictional. Public descriptions mention only the broad development settings of medical education and public-database research.
