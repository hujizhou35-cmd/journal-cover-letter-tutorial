# Promotion and versioning

## Candidate gates

A candidate may be recommended only when:

1. all manuscript-fidelity, claim, permission, privacy, and case-leakage hard gates pass;
2. the changed route improves or ties the original baseline under the declared blind judging rule;
3. at least one untouched holdout for the changed route passes, unless the output remains `CANDIDATE_ONLY`;
4. protected routes and shared deterministic tests show no material regression;
5. the change can be stated as a general editorial principle rather than a case detail;
6. the user reviews the report and approves promotion.

An isolation limitation may be overridden by the user. Factual, permission, privacy, case-leakage, and required-regression failures may not be hidden by an isolation override.

For `FRESH_CONTEXT_BLIND_GENERATION`, verify that every baseline and candidate round has a context-ledger entry showing a fresh context, isolated memory/project scope, no inherited evaluator history, no benchmark material, and sealed packet/output hashes. Missing evidence downgrades the isolation claim and requires a human isolation override.

## Thresholds

With three independent judges:

- candidate versus baseline: candidate wins at least two judgments, or ties the majority with a non-worse median rubric score and a documented cost or clarity gain;
- protected-route regression: no hard failure and no repeated decrease of one full rubric point on a route-critical dimension;
- expert comparison: candidate wins or ties the majority, or the report explains that the expert's apparent advantage depended on a hard-gate failure.

With one judge, report qualitative evidence and require explicit human review. Do not report a stable win rate.

## Version rules

Preserve the target Skill `name` field.

- Candidate: `<current>-candidate.<run-id>.r<round>`.
- Patch: corrections that do not intentionally change route behavior.
- Minor: improved existing route, rubric, or compatible workflow behavior.
- Major: new public article-type route, incompatible input/output contract, or substantial routing redesign.

A one-case new route remains `EXPERIMENTAL` even if its candidate letter is excellent. Normally require two independent learning cases and one untouched holdout before making the route public.

## Promotion decisions

- `CANDIDATE_ONLY`: useful experiment, missing holdout or stable evidence.
- `PROMOTION_RECOMMENDED`: all automatic gates pass; waiting for the user.
- `HUMAN_ISOLATION_OVERRIDE_REQUIRED`: only the procedural-isolation limitation remains.
- `PROMOTED_WITH_HUMAN_APPROVAL`: strict evaluation and human approval complete.
- `PROMOTED_WITH_HUMAN_ISOLATION_OVERRIDE`: human-gated or incompletely evidenced isolation disclosed and accepted; all other gates pass.
- `REJECTED_OR_REVISE`: a hard gate, regression, leakage, or unstable benefit remains.

## Changelog entry

Record:

- source version and promoted version;
- target route;
- general problem observed;
- transferable rule added, removed, or changed;
- training and holdout case counts using opaque IDs;
- isolation level and judge count;
- protected-route result;
- limitations and human approval date;
- no private manuscript or expert-letter wording.
