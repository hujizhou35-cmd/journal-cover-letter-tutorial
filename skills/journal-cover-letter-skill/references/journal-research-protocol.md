# Journal research protocol v3.2

Research current information at the time of use. Prioritize:

1. official journal author instructions and aims/scope;
2. official publisher policy pages;
3. current journal editorial pages and recent journal articles;
4. reputable indexing or society pages only as secondary confirmation.

Capture page title, direct URL, access date, finding, and category:

- `REQUIREMENT`: explicitly required;
- `OBSERVED_PREFERENCE`: cautious inference from current editorial material or recent publications;
- `GENERAL_PRACTICE`: not journal-specific.

Verify:

- the exact article-type label available in the target journal and section;
- article-type-specific criteria and formatting;
- cover-letter requirements and submission constraints;
- required declarations;
- readership and scope;
- editor identity only when useful;
- relevant current journal conversation when it sharpens fit.

Record the exact journal label as `official_article_type`. Do not force it to match `intellectual_route`. For example, a bibliometric manuscript may legitimately have:

```yaml
official_article_type: Original Research
intellectual_route: BIBLIOMETRICS
```

Build fit evidence in descending priority: explicit criterion, concrete readership need, then recent journal conversation. Avoid generic praise. If official pages cannot be accessed or appear stale, use `NEEDS_JOURNAL_VERIFICATION`.

Complete a `journal_fit_bridge` by connecting one verified journal criterion or readership need to one specific manuscript contribution and the decision or understanding it offers readers. A scope match without that bridge is incomplete.
