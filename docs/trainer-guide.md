# Beginner guide: improve the Skill with the Trainer

Use the Trainer when you have a current Cover Letter Skill, a manuscript, and an expert-authored cover letter that you are allowed to analyze.

## What to prepare

1. The current `.skill` or Skill folder.
2. The manuscript and any files needed to understand it.
3. The target writing route: Research, Review, Bibliometrics, or a proposed new route.
4. The expert cover letter—but do not give it to the baseline generator yet.
5. Permission to use that letter as an anonymous expert benchmark.

## The simple workflow

1. Open a clean conversation and provide only the Trainer, current Skill, and manuscript materials.
2. Ask for the baseline cover letter. Do not mention or upload the expert letter.
3. Save or seal the baseline output.
4. Give the expert letter to the evaluator conversation and allow anonymous benchmark analysis.
5. Review the comparison and proposed reusable Skill changes.
6. Open another clean conversation. Give it only the revised Skill and manuscript-side materials.
7. Return the new output to the evaluator for comparison.
8. Repeat until the improvement is stable or the Trainer reports a stop condition.

## When is it really blind?

- **Strongest:** separate agent or API contexts enforce the input boundary.
- **Practical:** a new temporary conversation is used for every generation round, with memory and shared project files unable to expose the expert.
- **First draft only:** the expert is delayed in one conversation, but later drafts use that revealed conversation.
- **Contaminated:** the generator has already seen the expert letter or a substantive summary.

The Trainer must report which condition was actually achieved.

## What not to upload publicly

Do not commit manuscripts, real cover letters, author contacts, submission identifiers, private journal correspondence, chat-share links, or identifying filenames. Keep raw cases in an ignored private folder.

One case can reveal a useful problem. It cannot prove that a new version is better for every manuscript.
