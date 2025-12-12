![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Local-First](https://img.shields.io/badge/Local-First-blue)
![Subjective-Aware](https://img.shields.io/badge/Subjective-Aware-purple)



# Council Framework v0.4

Council is a small, local-first framework for understanding **model behavior** using subjective, human-interpretable **traits** instead of benchmark scores.

It is intentionally minimal:

- no leaderboards  
- no numeric scoring  
- no central authority  
- fully forkable  
- designed for personal calibration, drift detection, and practical model routing  

Council does **not** attempt to define universal standards.  
It provides a *vocabulary* for describing how models behave — and why some feel better for certain tasks than others.

## 🎛 Core Concepts

### Behavioral Trait Profiles
Each model receives a trait map describing tendencies such as:

- summarization fidelity  
- hallucination risk  
- schema sensitivity  
- long-context stability  
- ambiguity handling  
- error honesty  
- instruction adherence  

See **docs/TRAITS.md** for full definitions.

### Task → Model Routing
Tasks declare the traits they require.  
Models declare the traits they exhibit.

Council chooses the best fit and explains *why*:

```
council route summarize_document
```

### Model Self-Assessment (Optional)
Models may introspectively rate their own tendencies using a strict JSON schema:

```
council self-assess --model mistral --save mistral.json
```

### CLI Tools

```
council tasks
council profiles
council route <task>
council compare A B
council self-assess
council drift <model>
```

## 📚 Philosophy

Council is **descriptive, not prescriptive**.

# ❓ FAQ

## Why not just use benchmarks?
Benchmarks measure correctness.  
Council measures *behavior*.

## Is the trait system objective?
No — deliberately so.

## Does this create rankings?
No.

## Will vendors dislike this?
Unlikely.

## Does this conflict with MCP agents?
No.

# 🧩 Self-Assessment FAQ

## Why include a self-assessment feature?
Because self-assessment is a **behavior test**.

## What if a model can't follow the instructions?
Failure becomes signal.

## Why strict JSON?
To test formatting reliability and constraint tracking.

## Is self-assessment required?
No.

# 🤝 Contributing

Council is intentionally minimal and fork-friendly.

# 📂 See Also

- docs/TRAITS.md  
- examples/  
- CLI tools  
