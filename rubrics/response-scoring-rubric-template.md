# Response Scoring Rubric — Template Example

A generic rubric template for scoring AI-generated responses on a 0–3 scale across four core dimensions. This is a self-built example illustrating a general rubric-based evaluation approach used in AI/LLM data annotation work — not an actual client rubric.

## Scoring dimensions

| Dimension | 0 (Poor) | 1 (Weak) | 2 (Good) | 3 (Excellent) |
|---|---|---|---|---|
| **Relevance** | Ignores the user's actual request | Partially addresses the request | Addresses the request with minor gaps | Fully and precisely addresses the request |
| **Factual Accuracy** | Contains clear factual errors | Mostly accurate, one notable error | Accurate with minor imprecision | Fully accurate, verifiable claims |
| **Coherence** | Disorganized, hard to follow | Some structure, unclear in places | Clear structure, minor awkwardness | Clear, logically ordered, easy to follow |
| **Tone & Persona Consistency** | Inconsistent or inappropriate tone | Tone mostly fits but slips occasionally | Tone fits with minor lapses | Tone is consistent and appropriate throughout |

## How this gets used

1. A prompt is given to a model, which generates multiple candidate responses.
2. Each response is scored against every dimension above using the 0–3 scale.
3. The highest-scoring response is selected as the reference ("golden") response, or used as the basis to write one.
4. Scores and rationale are logged to support downstream fine-tuning or model comparison.

## Notes

- Rubric dimensions should be tailored per task type (e.g. open-ended vs. close-ended queries may weight dimensions differently).
- A short written rationale (1–2 sentences) per dimension improves consistency across annotators working on the same dataset.
