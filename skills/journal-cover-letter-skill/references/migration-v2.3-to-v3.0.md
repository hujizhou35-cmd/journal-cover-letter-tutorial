# Migration from v2.3 to v3.0

## Breaking conceptual change

v2.3 used one `article_type` field for both journal submission label and reasoning route. v3.0 separates:

```yaml
official_article_type: exact journal label
intellectual_route: ORIGINAL_RESEARCH | REVIEW_SYNTHESIS | BIBLIOMETRICS | OTHER_OR_UNRESOLVED
```

This prevents a bibliometric or scoping manuscript submitted as `Original Research` from being mislabeled as `Review` in the cover letter.

## New universal fields

- `empirical_anchor`
- `editorial_meaning`

## New Bibliometrics fields

- `bibliometric_mode`
- `mapping_intervention`
- `mapping_thesis`
- `bibliometric_decision_spine`
- `metric_boundary`

## Benchmark change

Benchmark analysis now separates `benchmark_empirical_signal` from `benchmark_editorial_logic`. Superficial features such as sentence length are secondary.

## Script change

Payload validation now requires the exact official label, intellectual route, and route-specific fields. Bibliometric ranking, quality, completeness, and forecasting language is flagged for semantic review.
