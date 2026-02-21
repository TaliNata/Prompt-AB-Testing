## Model Configuration

- Model: GPT-4
- Interaction mode: Chat-based interaction
- Temperature: default
- Top-p: default
- Same input text for all runs

---

# Prompt A/B Testing Case Study

This repository demonstrates an A/B test of two LLM prompts
using the same input text about the platypus to evaluate
output quality, structure, and stability.

---

## Goal
Select the most stable and controllable prompt for summarizing
descriptive biological text.

---

## Method
- Same task
- Same model
- Same input text (platypus biology)
- 3 runs per prompt
- Qualitative evaluation

---

## Structure
- `prompts/` – tested prompts (baseline vs structured)
- `results/` – real model outputs
- `evaluation.md` – comparison and conclusion

---

## Key Result
Prompt B significantly improved output consistency and comparability
while preserving informational content. Structured prompting reduced
uncontrolled variability and produced automation-ready summaries.


