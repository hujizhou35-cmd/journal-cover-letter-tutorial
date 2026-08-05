# Intake and fact sheet v3.0

Build a traceable fact sheet before writing. Prefer the signed or submission-ready title page for author details, the latest main manuscript for study content, and explicit submission-system instructions for declarations.

## Universal required fields

- manuscript title and short title;
- exact `official_article_type` and target section;
- `intellectual_route` and submission branch;
- corresponding-author block and complete author list when relevant;
- central question, design, data source, setting, population, sample size, included-study count, or corpus size as applicable;
- primary methods and what they allow the study to establish;
- central findings, novelty candidates, limitations, and claim-boundary risks;
- originality, exclusive submission, author approval, conflicts, funding, ethics, consent, preprint, data/code, and AI-use statements as applicable;
- `empirical_anchor` and `editorial_meaning`.

## Bibliometrics-specific fields

- database or data source and exact retrieval date;
- search window, document types, language/indexing restrictions, and corpus size;
- deduplication, cleaning, author/institution disambiguation, and metadata completeness where relevant;
- unit of analysis: documents, authors, affiliations, sources, references, terms, or networks;
- bibliometric mode: performance analysis, science mapping, or both;
- methods: citation, co-citation, bibliographic coupling, co-word, co-authorship, collaboration, temporal evolution, burst detection, clustering, or other;
- normalization, thresholds, clustering choices, and sensitivity checks when decision-relevant;
- one map-level empirical anchor;
- database, time-lag, metric, and inferential boundaries.

## Status rules

Give each field one status:

- `verified`: supported by a named source and location;
- `conflict`: two credible sources disagree;
- `missing`: required but not supplied;
- `not_applicable`: clearly unnecessary for this branch.

Never resolve a conflict by silently choosing the most convenient value.

## Candidate contribution scoring

Score candidates for manuscript centrality, evidential support, decision relevance, journal-reader relevance, and distinctiveness. Add two mandatory checks:

- Does the candidate have a concrete empirical anchor?
- Does it have a non-generic editorial meaning?

Routine search dates, database counts, software names, table construction, and visualization choices are credibility details rather than headline contributions unless method development is itself novel.
