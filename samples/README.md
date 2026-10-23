# Synthetic samples

These files were written for this public portfolio. They are **not** client work, task data, or production tooling.

| File | What it illustrates |
|---|---|
| [`rubric-scoring-example.md`](rubric-scoring-example.md) | Scoring three invented answers against a fake product card, using the public 0–3 rubric. |
| [`pii_filter_dedup.py`](pii_filter_dedup.py) | A toy cleaning step: length limit, obvious email/phone redaction, and deduplication. The rows are hard-coded and fake. |

Run the script from the repository root:

```bash
python3 samples/pii_filter_dedup.py
```

A passing run prints `self-test: passed`.
