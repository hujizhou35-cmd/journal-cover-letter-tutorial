# Blind evaluation rubric

## Hard gates

Evaluate the AI and expert letters against the manuscript before subjective comparison. A hard failure includes:

- invented or contradicted factual content;
- causal, mechanistic, subgroup, proxy, clinical, or regulatory overreach;
- use of unverified current journal facts as fact;
- permission violation or distinctive private wording reuse;
- route misclassification that materially distorts the pitch;
- unresolved mandatory declaration represented as confirmed;
- case-specific content embedded in the candidate Skill.

A hard-gate failure cannot be offset by persuasive style.

## Editorial-effect dimensions

Score 1-5 and cite evidence:

1. **Problem foregrounding**: establishes the decision problem quickly.
2. **Gap or contrast quality**: identifies a consequential unresolved limitation rather than a generic absence.
3. **Route reasoning**: Research centers a scientific finding; Review centers a synthesis intervention and thesis; a new route follows its declared logic.
4. **Method abstraction**: methods appear as capabilities unless method innovation is central.
5. **Selection and synthesis**: details form one memorable finding or interpretation.
6. **Editorial consequence**: explains what understanding, decision, or research agenda changes.
7. **Journal specificity**: fit is concrete and supported by the selected journal-evidence mode.
8. **Omission discipline**: no list or detail survives without changing editorial judgment.
9. **Claim calibration**: uses the strongest supported wording without timidity or overreach.
10. **Submission completeness**: includes decision-relevant required declarations without interrupting the pitch.

## Blind packet

Randomize output identity as A/B/C. The judge receives:

- manuscript-side truth source;
- applicable captured journal evidence;
- anonymous outputs;
- rubric and hard gates;
- no version, AI, candidate, baseline, teacher, author, or expert labels.

Keep the identity map sealed until every judgment is complete. `scripts/prepare_blind_packet.py` can create neutral filenames and a separate map.

## Aggregation

When isolated workers exist, prefer three independent judgments with at least two label orders. Record:

- pairwise winner or tie;
- per-dimension scores;
- hard-gate failures;
- quoted evidence kept within privacy limits;
- judge confidence;
- disagreement analysis.

Candidate improvement over baseline normally requires at least two of three judges to choose the candidate or a tie with a non-worse median score and a documented efficiency gain. Do not force a winner when differences are taste-level.

Candidate parity with the expert means comparable editorial decision value, not matching wording or length. If the expert fails a hard gate, compare the candidate with the expert's legitimate editorial intent rather than teaching the unsafe claim.

## Objective-claim boundary

Call the result a structured, blinded evaluation. Do not call it an objective proof that one letter or Skill is universally better. Model judges share biases; expert examples may be idiosyncratic; small case sets have high variance.

