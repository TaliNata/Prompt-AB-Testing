# Structured JSON Output with Prompt A/B Testing (B2B SaaS Case)

## Overview

This repository demonstrates a production-oriented prompt engineering workflow
for Large Language Models with:
- strict structured JSON output;
- schema-first design;
- Pydantic validation;
- prompt A/B testing;
- business-driven evaluation metrics.

The case simulates a B2B SaaS lead analysis system, where unstructured inbound
messages are transformed into automation-ready business decisions.

---

## Business Problem

B2B SaaS companies receive large volumes of inbound messages from:
- website forms;
- emails;
- chat widgets;
- CRM integrations.

Manual qualification does not scale.

**Goal:**  
Use an LLM to reliably convert unstructured customer messages into structured,
validated business intelligence for sales routing and prioritization.

---

## Core Capabilities

The system produces:
- lead classification;
- intent and urgency detection;
- estimated deal value and LTV;
- risk assessment;
- recommended sales motion;
- confidence calibration.

All outputs strictly follow a predefined JSON schema.

---

## Prompt A/B Testing

Two prompt strategies are evaluated using the same schema:

| Variant | Strategy | Goal |
|------|--------|------|
| A | Business-First | Minimize false-positive high-priority leads |
| B | Revenue-Optimized | Maximize pipeline value and sales velocity |

This allows controlled experimentation while keeping downstream systems stable.

---

## Repository Structure
```
structured-json-output-ab-testing/
│
├─ README.md
├─ requirements.txt
│
├─ prompts/
│   ├─ system_prompt.txt
│   └─ user_prompt.txt
│
├─ schemas/
│   └─ lead_analysis.schema.json
│
├─ examples/
│   ├─ input_example.txt
│   └─ output_example.json
│
├─ validation/
│   └─ model.py
│
├─ pipeline/
│   └─ run.py
│
└─ ab_testing/
    ├─ prompts/
    │   ├─ prompt_A.txt
    │   └─ prompt_B.txt
    │
    ├─ metrics/
    │   └─ scoring.md
    │
    ├─ results/
    │   └─ comparison_example.json
    │
    └─ run_ab_test.py
```

---

## Typical Production Flow
```
Inbound message
↓
LLM (structured prompt)
↓
JSON validation
↓
CRM / Sales Routing / Analytics
```

---

## Why This Matters

This project demonstrates:
- disciplined prompt engineering;
- schema-driven LLM integration;
- prompt experimentation methodology;
- business-aware reasoning;
- production readiness.

---

## Possible Extensions

- automated evaluation with golden labels;
- prompt versioning and rollback;
- confidence-based routing;
- multi-model A/B testing;
- CRM or webhook integration.



