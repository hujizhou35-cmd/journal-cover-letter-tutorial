# Blind benchmark loop v3.1

## Purpose

Test whether the skill can independently recover the valuable editorial decisions in a human-authored cover letter without copying or reading that letter during baseline generation.

## Isolation levels

- `STRICT_COGNITIVE_BLIND`: a separate model session or external agent has no access to the benchmark.
- `FILE_LEVEL_BLIND_ONLY`: the generation process uses an explicit input allowlist and does not open the benchmark, but the same conversational model may have seen it previously. This must be disclosed.

Never claim strict cognitive isolation when only file-level isolation was achieved.

## Procedure

1. **Allowlist**: manuscript, title page, supplements needed for facts, the candidate skill, and verified official journal sources.
2. **Denylist**: human cover letter, prior comparison notes, extracted benchmark phrases, and any prompt containing benchmark wording.
3. **Baseline**: draft from the allowlisted sources. Freeze the exact output and record a hash.
4. **Reveal**: open the benchmark only after freezing.
5. **Extract effects**: identify empirical selection intelligence, selection granularity, editorial interpretation, and administrative choices.
6. **Exclude defects**: do not converge toward factual errors, unsupported declarations, stale journal details, grammar defects, or overclaims.
7. **Compare**: score 0-5 on empirical-anchor fidelity, selection granularity, editorial meaning, route logic, consequence, journal fit, claim calibration, administrative completeness, naturalness, and authorial fingerprint.
8. **Refine the rule**: describe the smallest transferable skill change responsible for each material gap. Do not patch only the example letter.
9. **Regenerate blind**: use the manuscript and revised skill only. The benchmark text remains excluded from the generation prompt.
10. **Stop**: no core dimension below 4/5 and overall effect at least 85%, or after three revision rounds with an explicit unresolved report.

## Anti-copying rule

Convergence is semantic and editorial, not lexical. Similarity in exact phrasing is neither required nor rewarded. Preserve the human's valid selection logic while independently expressing it.
