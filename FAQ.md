
# FAQ — Council Framework

## Why not just use benchmarks?

Because benchmarks answer the question:

> “How well did the model perform on this static dataset?”

But real use cases ask:

- “What kind of work does this model excel at?”
- “How does it behave when things get messy?”
- “Can I trust it on this category of tasks?”

Benchmarks don’t measure:

- brittleness  
- drift  
- hallucination pressure  
- the model’s *style*  
- willingness to admit uncertainty  
- ambiguity tolerance  
- schema intuition  
- narrative coherence  

They measure point performance, not behavior over time.

---

## Is the trait system objective?

No — and that’s the point.

Council is explicitly subjective-aware.  
Your own experience is the source of truth.

---

## Does this create rankings?

No.  
The framework is incapable of producing global rankings.

It only answers:

> “For *this task*, based on *your* declared traits, this model fits best.”

---

## Will vendors hate this?

Unlikely.  
You are not publishing scores or naming losers.  
You are simply documenting your personal experiences.

---

## What about automated evaluation?

Feel free to add it.  
Council is intentionally open-ended.

---

## Can this be integrated with MCP agents?

Yes.  
Council chooses **which model** to use.  
MCP governs **how** that model uses tools.

The layers do not conflict.

---

## Is this a competitor to LangChain, AutoGen, or OpenAI evals?

No.  
Council is deliberately much smaller.

Think of it as a *notebook for your intuitions* that happens to be machine-readable.

---

# Self-Assessment in Council

## Why does Council include a model self-assessment feature?

Because **self-assessment is itself a behavior test**.

Asking a model to describe its own tendencies using a strict schema reveals:

- instruction-following discipline  
- ability to output strict JSON  
- hallucination tendencies  
- willingness to admit weaknesses  
- tendency to inflate abilities  

The *act* of self-assessment becomes part of the evaluation.

---

## What if a model cannot follow the self-assessment prompt?

That **is** the result.

Failure to:

- return valid JSON  
- respect allowed values  
- include all required traits  
- avoid extra text  

…indicates weaknesses in:

- instruction_adherence  
- schema_sensitivity  
- determinism  
- error_honesty  
- confidence_calibration  

Older SFT models often fail in predictable ways.  
That failure is a behavioral fingerprint.

---

## Why do some models overrate themselves?

Models trained to be helpful and confident often:

- overclaim reasoning ability  
- downplay hallucination risk  
- mark every trait as “excellent” or “perfect”  

This exposes gaps in:

- confidence_calibration  
- error_honesty  
- hallucination_risk  

Council does not correct bias — it *captures* it.

---

## What if a model rates itself differently from a human evaluator?

Expected — and useful.

Council treats:

- human assessments as *ground-level experience*
- model assessments as *behavior under introspection*

The difference is signal.  
It reveals drift, family tendencies, and stability patterns.

---

## Why require strict JSON? Isn’t that fragile?

Strict JSON is intentional.

It tests:

- global constraint tracking  
- ability to juggle structure + content  
- aversion to embellishment  
- deterministic formatting  

Many chatty or older models break under these constraints — and Council treats that breakage as valuable data.

JSON also enables automated diffing and routing.

---

## Does the self-assessment influence routing?

Only if the user opts in.

Council keeps:

- human-provided profiles  
- model-provided self-evals  

as separate layers.

You may merge, weight, or ignore them.

---

## Why not convert self-assessments into numeric scores?

Because Council avoids pseudo-precision.

Traits are **ordinal**, qualitative descriptors:

- "low"  
- "medium"  
- "high"  
- "excellent"  

Assigning numbers would create the illusion of objectivity and replicate benchmark distortions.

---

## Why doesn’t Council enforce a canonical trait set?

Because self-assessment should remain:

- contextual  
- forkable  
- personal  
- easy to modify  

Traits are a vocabulary, not a standard.

If your work requires new traits (e.g., “legal compliance stability”), you may extend the schema freely.

---

## Can models lie?

Yes — and that too is signal.

Models may:

- self-deceive  
- overclaim  
- mask weaknesses  
- misjudge hallucination frequency  

Council does not prevent lying; it *observes* the style of lying.

This often distinguishes model families more cleanly than benchmarks.

---

## Is self-assessment required?

No.

Council works perfectly well with human-only profiles.

Self-assessment is an optional behavioral probe — but when used, it becomes an unusually rich diagnostic tool.
