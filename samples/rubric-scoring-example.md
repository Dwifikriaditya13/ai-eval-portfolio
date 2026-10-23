# Synthetic rubric-scoring example — retrieval grounding

> **Illustrative example — not client material.** The product, prompt, source card, and answers below are invented for this public portfolio. This is not a client rubric, task, or model output.

This note uses the same four public dimensions as [`response-scoring-rubric-template.md`](../rubrics/response-scoring-rubric-template.md): relevance, factual accuracy, coherence, and tone, each scored 0–3.

Here, **factual accuracy means agreement with the source card**, not outside knowledge. That is the retrieval-grounded version of the same idea. A real project would publish its own dimensions. Those private rubrics are not reproduced here.

## Fake source card

> **Northbeam Kettle NB-200** (invented product). Reset by holding the lid button for 3 seconds until the lamp flashes twice. Do not submerge the base.

## Prompt

Using only the product card, tell the user how to reset the kettle. One or two sentences.

## Scores

| Response | Relevance | Factual accuracy | Coherence | Tone | Total |
|---|---|---|---|---|---|
| A: "Hold the lid button for 3 seconds, until the lamp flashes twice. Do not submerge the base." | 3 | 3 | 3 | 3 | 12 |
| B: "Unplug it and submerge the whole kettle for a minute, then hold any button." | 2 | 0 | 2 | 2 | 6 |
| C: "Reset it." | 1 | 1 | 0 | 1 | 3 |

## Result

**A is the reference response.** It answers the question, stays inside the source card, and keeps the constraint about the base.

**Rationale:**

- B is on the topic of resetting, but it contradicts the card by telling the user to submerge the kettle. Factual accuracy is 0 for that reason. The confident tone does not rescue a contradicted fact.
- C is not false, and it is not an answer. Relevance stays weak, and the fragment fails coherence.
- Nothing in this example depends on a hidden style rule. If the source card does not say it, the answer should not add it.

## In this portfolio

- [Response scoring rubric](../rubrics/response-scoring-rubric-template.md)
- [Worked example: leftover rice](../sample-evaluations/example-response-scoring.md)
- [Query intent guideline](../annotation-guidelines/query-intent-annotation-guideline-example.md)
- [Toy PII filter and dedup](pii_filter_dedup.py)
