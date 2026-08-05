# Bibliometrics playbook: field-map route v3.1

## Editorial purpose

A bibliometric cover letter should sell a field-level interpretation, not the existence of a large dataset or a set of visualizations. Its task is to show what becomes visible about a research field's structure, evolution, concentration, connectivity, or emerging attention, and why that visibility changes the next research decision.

## Methodological foundation

Bibliometric analysis can combine two broad families:

- `PERFORMANCE_ANALYSIS`: publication activity, citation activity, sources, authors, institutions, countries, or other productivity and impact indicators;
- `SCIENCE_MAPPING`: conceptual, intellectual, or social structure using co-word, co-citation, bibliographic coupling, co-authorship, collaboration, clustering, or related network methods.

This distinction follows established bibliometric guidance, including Donthu et al. (2021), Zupic and Čater (2015), and Aria and Cuccurullo (2017). Responsible interpretation should also follow the spirit of the Leiden Manifesto and DORA: metrics support expert interpretation and should not be treated as direct substitutes for quality.

## Route discriminator

Use `BIBLIOMETRICS` when:

- the primary analytical objects are publications and their metadata or relations;
- the main results are field maps, temporal shifts, clusters, networks, concentration patterns, or emerging themes;
- the main contribution is orientation or coordination of a research field.

Use `REVIEW_SYNTHESIS` instead when bibliometric outputs are secondary and the main contribution synthesizes the substantive findings of included studies.

The official submission label is separate. Record the exact journal label even when it is `Original Research`, `Review`, or `Systematic Review`.

## Required internal state

```yaml
bibliometric_mode: PERFORMANCE_ANALYSIS | SCIENCE_MAPPING | BOTH
field_orientation_problem: string
corpus_boundary: string
mapping_capability: string
empirical_anchor: string
mapping_intervention: string
mapping_thesis: string
editorial_meaning: string
research_coordination_consequence: string
metric_boundary: string
bibliometric_signature_packet: string
authorial_specificity_floor: string
bibliometric_decision_spine: string
```

## Decision spine

> Field-scale uncertainty -> bounded corpus -> mapping capability -> empirical anchor -> mapping thesis -> coordination or research consequence -> journal fit -> metric boundary

### 1. Field-scale uncertainty

State the orientation problem, not merely that publications have increased. Examples:

- a rapidly expanding literature lacks a coherent map of its conceptual structure;
- clinical and technical research streams are developing in parallel with weak integration;
- apparent growth obscures whether validation, implementation, or collaboration has kept pace;
- topic labels are proliferating without clarity about which themes are mature, emerging, or disconnected.

### 2. Corpus boundary

Use database, date range, document types, query, and cleaning as credibility boundaries. Mention only what is necessary to establish reproducibility and scope. A large corpus is not itself the contribution.

### 3. Mapping capability

Translate methods into what they reveal:

- performance analysis quantifies concentration or distribution;
- co-authorship maps collaboration structure;
- co-citation identifies the intellectual base;
- bibliographic coupling identifies current research fronts;
- co-word analysis maps conceptual structure;
- temporal or burst analysis identifies intensifying attention within the indexed period.

Do not list software unless software is itself the innovation.

### 4. Empirical anchor

Select one concrete map-level pattern, such as:

- a transition from isolated algorithm development to multimodal and real-world validation;
- strong publication growth but persistent fragmentation between clinical and engineering communities;
- concentration of output in a small group of countries while cross-regional collaboration remains sparse;
- an emerging topic that is weakly connected to established clinical evidence.

The anchor must be directly supported by the manuscript's analyses.

### 5. Mapping intervention and thesis

`mapping_intervention` states what the analysis makes visible. `mapping_thesis` states the field-level interpretation.

Example:

> The analysis does not merely identify popular keywords; it shows that the field is shifting from isolated diagnostic models toward multimodal and implementation-oriented research, while external validation remains underconnected.

Use one thesis and at most two supporting patterns.

### 6. Editorial consequence

Translate the map into a decision, for example:

- prioritize external and cross-population validation;
- connect technically mature clusters to clinical implementation questions;
- direct collaboration toward underrepresented regions or methods;
- distinguish mature themes from newly intensifying but weakly validated topics;
- refine future review or funding priorities.

Do not claim that a map directly establishes clinical effectiveness.

### 7. Metric boundary

Retain the boundary that matters most:

- database coverage and language/indexing bias;
- citation and publication time lag;
- field and document-type differences;
- author or institution name disambiguation;
- sensitivity to thresholds, normalization, clustering, or parameter choices;
- citation volume is not quality;
- co-occurrence and network position do not establish causality or conceptual validity.

Place the boundary after the contribution is clear. It should calibrate the claim, not erase it.


## Bibliometric signature packet

A field-level thesis must remain visibly attached to the manuscript's own empirical identity. Construct a compact signature packet from up to three components:

1. `structural_map`: a central taxonomy, cluster structure, or collaboration pattern;
2. `frontier_signal`: two or three exact recently intensifying terms or themes;
3. `directional_transition`: a supported movement from one research orientation to another.

Retain at least two components when the manuscript supports them. Do not substitute generic phrases such as “multiple themes” or “emerging topics” when the named categories or terms are the paper's principal result.

A taxonomy may be listed when all of the following are true:

- it contains three to six domains;
- the domains are clinically or conceptually interpretable;
- the taxonomy is a principal result rather than a software artifact;
- compressed parallel syntax keeps the paragraph readable.

This is an empirical-specificity rule, not permission to reproduce every cluster, country, institution, or keyword.

`authorial_specificity_floor` requires at least one named or quantified manuscript-native result beyond corpus size. The editor should be able to distinguish the submission from another bibliometric paper on the same topic after one reading.

## Bibliometric claim ladder

1. `describes` publication activity;
2. `maps` a relational structure;
3. `identifies` concentration, fragmentation, or thematic transition;
4. `supports` a field-level interpretation or coordination priority;
5. `predicts` future development only with an explicit forecasting design beyond descriptive trend extrapolation.

Most bibliometric studies should stop at rung 3 or 4.

## High-risk substitutions

Replace unsupported formulations:

- “the leading country” -> “the country with the highest indexed output in this corpus”;
- “the most influential institution” -> “the institution with the highest citation or network indicator under the stated metric”;
- “future research direction” -> “a recently intensifying or emerging area within the indexed period”;
- “the field is dominated by” -> “output is concentrated in”;
- “proves collaboration drives impact” -> “shows an association between collaboration structure and the selected metric”;
- “complete landscape” -> “a database-bounded map of the field.”

## Omission discipline

Remove any country, institution, journal, keyword, cluster, centrality value, or software detail that does not change the mapping thesis, the consequence, the credibility boundary, or the authorial empirical fingerprint. Omission is not a virtue when it erases the principal taxonomy, frontier terms, or directional transition that makes the paper distinctive.

## Self-audit

- Is the official article type recorded separately from the bibliometric route?
- Is there one field-orientation problem rather than a generic growth statement?
- Does the letter contain one concrete map-level anchor?
- Does it retain a bibliometric signature packet and meet the authorial-specificity floor?
- Does it explain what the map changes, rather than list outputs?
- Are performance analysis and science mapping used accurately?
- Are ranking, quality, leadership, and forecasting claims calibrated?
- Is the database and metric boundary explicit enough to prevent misinterpretation?
- Does journal fit connect the map to a readership decision?
