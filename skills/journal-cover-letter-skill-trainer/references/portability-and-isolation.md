# Portability and isolation (v0.2)

## Isolation is an execution property

A prompt can request blindness, but only the host controls which inputs a model context receives. Report the strongest level actually achieved.

### STRICT_AGENT_ISOLATED

Use when separate worker contexts or API requests are available.

1. Snapshot the target Skill.
2. Create a generator input packet containing the Skill, manuscript-side files, explicit case confirmations, and permitted journal evidence.
3. Do not include the expert file, its path, title, metadata, summary, or existence.
4. Start the generator with no inherited conversation containing expert material.
5. Seal its output before starting comparison.
6. Give the comparison worker the manuscript, sealed output, and expert letter.
7. Repeat candidate generation in a fresh context with the expert omitted again.

Context isolation is sufficient for methodological blindness. Security-grade isolation additionally requires separate file mounts or API requests that make the expert file inaccessible, not merely unreferenced.

### FRESH_CONTEXT_BLIND_GENERATION

Use when a human can control model context but cannot deploy host-managed isolated workers.

1. Start baseline generation in a new temporary chat or otherwise fresh conversation.
2. Supply only the target Skill, manuscript-side files, confirmations, and permitted journal evidence.
3. Seal the baseline output before uploading the expert to the evaluator conversation.
4. Keep the evaluator conversation as the only place that receives the expert.
5. After each candidate Skill is sealed, start another fresh generator conversation.
6. Check that cross-chat memory is disabled or isolated, project files cannot surface the expert, custom instructions do not summarize it, and evaluator history is not inherited.
7. Record a context ledger entry and seal the generator packet and output hashes.

This is methodologically blind when every round satisfies the boundary. It is human-orchestrated, not host-enforced or security-grade. If any round reuses the evaluator context, downgrade the run to `HUMAN_GATED_REVEAL`; if expert content reaches a claimed-blind generator, mark that round `REFERENCE_CONTAMINATED`.

### HUMAN_GATED_REVEAL

Use in one ordinary file-enabled conversation when the user can delay the expert upload but cannot create a fresh generator for later rounds.

1. Inventory filenames without opening the expert file.
2. Read the target Skill and manuscript first.
3. generate and visibly seal the baseline;
4. record a timestamp or hash when tools permit;
5. only then open the expert letter;
6. disclose that only the first baseline was protected;
7. do not call later generations blind after the reveal.

The user may authorize publication despite this limitation, but the report must use `HUMAN_ISOLATION_OVERRIDE` and must not claim a strict blind experiment.

`PROCEDURAL_DELAYED_READ` is the v0.1 legacy name for this state. Normalize it to `HUMAN_GATED_REVEAL` in new reports.

### REFERENCE_CONTAMINATED

Use for any round in which its generator has already seen the expert's text or a substantive summary before generation. Continue only for qualitative comparison and rule discovery. Do not count that round's pairwise win as blind evidence.

## Shared filesystem caution

An agent with an independent conversational context may still share a filesystem with other agents. Stage generator inputs in a dedicated directory, do not reveal the sealed directory, and instruct the worker to read only the supplied input manifest. Label this `STRICT_AGENT_ISOLATED` for methodological evaluation, not security isolation.

## Portable publishing rule

Portable chat may return a complete candidate. Formal promotion requires:

- human acceptance of procedural isolation;
- all factual, permission, leakage, and regression gates to pass;
- an explicit limitation in the training report.

Human override changes the promotion decision, not the recorded isolation level.

## Human context ledger

For each baseline and candidate generation, retain evaluator-side evidence:

```text
expected round/case entries
round_id
case_id
generator_context_id
context_mode
memory_or_project_boundary
custom_instructions_checked
inherited_evaluator_history: false
benchmark_material_present: false
generator_packet_sha256
output_sha256
sealed_at
verified_by
```

Never put this ledger into the generator packet because its benchmark-related fields reveal that a reference exists. The evaluator owns it.
