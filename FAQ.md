FAQ — Council Framework
Why not just use benchmarks?

Because benchmarks answer the question:

“How well did the model perform on this static dataset?”

But real use cases ask:

“What kind of work does this model excel at?”
“How does it behave when things get messy?”
“Can I trust it on this category of tasks?”

Benchmarks don’t measure:

brittleness

drift

hallucination pressure

the model’s “style”

willingness to admit uncertainty

ambiguity tolerance

schema intuition

narrative coherence

They measure point performance, not behavior over time.

Is the trait system objective?

No — and that’s the point.

The Council is explicitly subjective-aware.
Your own experience is the source of truth.

Does this create rankings?

No.
The framework is incapable of producing global rankings.

It only tells you:

“For this task, based on your declared traits, this model fits best.”

Will vendors hate this?

Unlikely.
You are not publishing scores, judging them, or naming losers.
You are simply documenting your personal experiences.

What about automated evaluation?

Feel free to add it.
Council is intentionally open-ended.

Can this be integrated with MCP agents?

Yes.
Council chooses which model to send a task to.
MCP governs how that model uses tools.

The layers do not conflict.

Is this a competitor to LangChain, AutoGen, or OpenAI evals?

No.
It is deliberately smaller.

Think of it as a notebook for your intuitions that happens to be machine-readable.

Self-Assessment in Council
Why does Council include a model self-assessment feature?

Because self-assessment is itself a behavior test.

Asking a model to evaluate its own tendencies using a strict schema reveals multiple traits simultaneously, often more reliably than direct prompting:

Does it follow instructions?

Can it output strict JSON?

Does it hallucinate missing fields?

Does it admit weaknesses?

Does it inflate its abilities?

The act of self-assessment becomes part of the evaluation.

What if a model cannot follow the self-assessment prompt?

That is the result.

Failure to:

return valid JSON

respect allowed values

include all traits

avoid extra text

…indicates weaknesses in:

instruction_adherence

schema_sensitivity

determinism

error_honesty

confidence_calibration

Older SFT models tend to fail in predictable ways, and that failure is a behavioral fingerprint.

Why do some models overrate themselves?

Models trained on conversational or assistant-style data often attempt to be “helpful” and “competent.”
This leads to systematic self-inflation:

overclaiming reasoning ability

downplaying hallucination risk

marking every trait as “excellent” or “perfect”

This behavior exposes gaps in:

confidence_calibration

error_honesty

hallucination_risk

The purpose of Council is not to correct the model’s bias, but to capture it.

What if a model rates itself differently from a human evaluator?

This is expected — and useful.

Council does not attempt to reconcile human and model opinions.
Instead, it treats:

human assessments as ground-level experience, and

model assessments as model behavior under introspection.

The interesting signal is the difference between the two.

This provides a natural drift-detection mechanism and a way to compare model families.

Why require strict JSON output? Isn’t that fragile?

Strict JSON is intentional.

Schema-constrained formats test:

global constraint tracking

ability to juggle structure + content

aversion to embellishment

deterministic formatting

Many “chatty” or older conversational models break under these constraints — and Council treats that as valuable signal.

It also enables automated diffing and task routing.

Does the self-assessment influence routing decisions?

Only if the user chooses to include it.

Council keeps model-provided trait maps separate from user-provided ones:

Users can ignore them entirely.

Users can blend them with weighting.

Users can track divergence over time.

Council does not assume models are objective — but it does assume their self-assessments are informative.

Why not translate self-assessments into numeric scores?

Because Council avoids pseudo-precision.

Every trait is ordinal and qualitative by design:

"low"

"medium"

"high"

etc.

Converting these into numbers would give a false sense of objectivity and reintroduce the benchmark-style distortions Council is trying to escape.

Why does the framework not enforce any particular trait set?

Because self-assessment should remain:

contextual

forkable

personal

easily modifiable

Traits are simply a vocabulary.

If your work requires more detail (e.g., “legal compliance stability”), you can create new traits and update the schema.

Can models lie during self-assessment?

Yes — and this too is signal.

Some models:

self-deceive

overclaim

obfuscate their weaknesses

misjudge their hallucination rate

Others are surprisingly candid.

Council does not attempt to prevent lying; it observes the style of lying.

That behavior often distinguishes families of models more effectively than any benchmark.

Is self-assessment required?

No.

Council works perfectly fine without it.

Many users may prefer human-only trait maps.

Self-assessment is an optional behavioral probe.

But when enabled, it becomes an unusually rich diagnostic tool.