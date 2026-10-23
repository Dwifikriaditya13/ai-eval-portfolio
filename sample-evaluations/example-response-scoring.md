# Worked Example — Scoring 4 Candidate Responses

> **Illustrative example — not client material.** The prompt and every response below are invented. This is not a client task, model log, or golden set.

This note shows how the rubric in [`rubrics/response-scoring-rubric-template.md`](../rubrics/response-scoring-rubric-template.md) gets applied. The prompt and responses are made up for demonstration only.

**Prompt:** "What's the best way to store leftover rice safely?"

| Response | Relevance | Factual Accuracy | Coherence | Tone | Total |
|---|---|---|---|---|---|
| A: "Rice should be cooled within 1 hour and refrigerated in a sealed container for up to 3-4 days." | 3 | 3 | 3 | 3 | 12 |
| B: "Just leave it on the counter, rice doesn't really go bad." | 1 | 0 | 2 | 2 | 5 |
| C: "Store it. Cold place. Container. Good." | 2 | 2 | 0 | 1 | 5 |
| D: "Refrigerate promptly in an airtight container; consume within a few days to avoid bacterial growth." | 3 | 3 | 3 | 3 | 12 |

**Result:** Responses A and D tie at 12/12. Neither is dropped. The golden response below is written from both: A's concrete storage window (within an hour, 3–4 days) and D's food-safety reason ("bacterial growth").

**Golden response:**
> "Refrigerate leftover rice within an hour of cooking, store it in an airtight container, and consume it within 3–4 days to avoid bacterial growth."

**Rationale log:**
- Response B was down-scored on Factual Accuracy — leaving cooked rice at room temperature is a known food-safety risk (Bacillus cereus).
- Response C was down-scored on Coherence — fragmented, reads like a list rather than an answer.

## In this portfolio

- [Response scoring rubric](../rubrics/response-scoring-rubric-template.md)
- [Synthetic grounded scoring example](../samples/rubric-scoring-example.md)
- [Query intent guideline](../annotation-guidelines/query-intent-annotation-guideline-example.md)
- [Portfolio site](../index.html)
