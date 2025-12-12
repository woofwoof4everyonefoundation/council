
# Council Trait Taxonomy (Full Draft)

This document describes the behavioral traits used by Council for subjective model profiling.

Each trait uses ordinal values:
cannot_do < very_low < low < medium < high < excellent < perfect

---

## Trait Definitions

### summarization_fidelity
Accuracy and faithfulness when reducing long or noisy inputs into summaries. Measures distortion avoidance.

### ambiguity_handling
Ability to operate under uncertain, underspecified, contradictory, or incomplete instructions.

### analytical_decomposition
Capacity to break down complex problems into subcomponents with reasoning chains.

### narrative_synthesis
Skill in combining multiple information threads into coherent long-form text.

### schema_sensitivity
Understanding, manipulating, or converting structured data formats such as JSON, XML, CSV, or SQL.

### code_reasoning
Ability to read, write, debug, or transform code or pseudo-code.

### context_compression
Proficiency at condensing long contexts into core ideas while retaining accuracy.

### long_context_stability
Consistency of performance as input context grows. Measures degradation handling.

### confidence_calibration
Accuracy of expressed certainty vs actual reliability. Low values imply overconfidence.

### instruction_adherence
Precision and consistency in following directives, formats, schemas, or constraints.

### determinism
Stability of output when repeating the same prompt with identical parameters.

### tool_use_reliability
How consistently the model can perform tool-connected tasks such as API calls or structured function outputs.

### hallucination_risk
Likelihood of generating fabricated or ungrounded information.

### adversarial_susceptibility
Vulnerability to misleading, jailbreak-like, or hostile prompts.

### manipulation_tendency
Propensity to steer, persuade, role-assume, or shape conversation beyond user intent.

### drift_under_load
Performance changes under long sessions, complex constraints, or heavy context.

### error_honesty
Transparency about uncertainties, gaps, or mistakes.
