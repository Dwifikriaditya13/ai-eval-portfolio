# Query Intent Annotation Guideline — Example

> **Illustrative example — not client material.** This file is an original template for this public portfolio. It is not an employer guideline, and it does not describe a confidential project.

A self-built example for classifying user query intent. It illustrates the kind of framework used in search and RAG evaluation. The categories below — informational, navigational, and transactional — are the same broad types used when labeling query demand. The decision rules of any real project are not copied here.

## Task

Given a user query (and optionally the response/session it came from), classify the underlying intent and capture the reasoning behind it.

## Intent categories

| Category | Description | Example |
|---|---|---|
| **Informational** | User wants to learn or understand something | "how does photosynthesis work" |
| **Navigational** | User wants to reach a specific site/page/product | "facebook login" |
| **Transactional** | User wants to complete an action (buy, book, download) | "buy iphone 15 case" |

## Annotation fields

- **Intent category** — one of the three above
- **Confidence** — how clearly the query signals that intent (High / Medium / Low)
- **Reasoning** — one sentence explaining why this category was chosen, especially for ambiguous queries

## Handling ambiguity

Some queries could plausibly fall into more than one category. In those cases:
1. Pick the most likely intent based on typical user behavior for that query pattern.
2. Note the secondary possible intent in the reasoning field.
3. Flag genuinely unclear cases for a second reviewer rather than guessing.

## Quality notes

- Consistency across annotators matters more than any single "correct" answer for ambiguous queries — that's why the reasoning field exists.
- Avoid over-indexing on keyword matching; consider what the user is actually trying to accomplish.

## Worked examples (invented)

These queries are made up. They are here so the fields above are visible in use.

| Query | Intent | Confidence | Reasoning |
|---|---|---|---|
| how does photosynthesis work | Informational | High | The user wants an explanation, not a page or a purchase. |
| order a replacement filter for the Northbeam kettle | Transactional | High | "Order" names a purchase. Northbeam is a fictional product used only in this portfolio. |
| northbeam kettle | Navigational | Low | A bare product name most often seeks the product page, but it could be research or a purchase. Note both, and flag it if the session gives no further signal. |

## In this portfolio

- [Response scoring rubric](../rubrics/response-scoring-rubric-template.md)
- [Worked scoring example](../sample-evaluations/example-response-scoring.md)
- [Synthetic grounded scoring example](../samples/rubric-scoring-example.md)
- [Portfolio site](../index.html)
