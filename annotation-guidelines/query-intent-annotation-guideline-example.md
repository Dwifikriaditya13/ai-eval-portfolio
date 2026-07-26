# Query Intent Annotation Guideline — Example

A self-built example guideline for classifying user query intent, illustrating the kind of annotation framework used in search/RAG evaluation work. This is a generic template, not an actual client guideline.

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
