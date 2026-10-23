#!/usr/bin/env python3
"""Synthetic demo: length limit, obvious-PII redaction, and deduplication.

SYNTHETIC / ILLUSTRATIVE ONLY.
This is a toy version of a dataset-cleaning step for a public portfolio.
It is not client code, not a production filter, and every row below is invented.
It does not try to find people, recover redacted text, or bypass a real filter.

Order of operations:
1. Drop a row when the raw instruction is over MAX_CHARS.
2. Replace obvious email addresses and phone-like numbers.
3. Deduplicate on normalized text and keep the earliest id.

Run from the repository root:
    python3 samples/pii_filter_dedup.py
"""

from __future__ import annotations

import re
import unicodedata

MAX_CHARS = 180

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
# Requires separators, so ordinary phrases like "3 to 4" are left alone.
PHONE_RE = re.compile(
    r"(?<!\w)(?:\+\d{1,3}[\s.-])?(?:\(\d{2,4}\)[\s.-]?|\d{2,4}[\s.-])\d{3,4}[\s.-]\d{3,4}(?!\w)"
)

RAW_ROWS = [
    {
        "id": "ex-001",
        "instruction": "Explain how to brew tea in two sentences.",
    },
    {
        "id": "ex-002",
        "instruction": "Explain how to brew tea in two sentences.",
    },
    {
        "id": "ex-003",
        "instruction": "Explain   how to brew tea   in two sentences.",
    },
    {
        "id": "ex-004",
        "instruction": "Reply to Ada Lovelace at ada.demo@example.com about the kettle warranty.",
    },
    {
        "id": "ex-005",
        "instruction": "Call the fictional help desk at +1 555 010 0199 and summarize the hours.",
    },
    {
        "id": "ex-006",
        "instruction": "A" * 220,
    },
    {
        "id": "ex-007",
        "instruction": "List three ways to label a speaker turn without changing the words.",
    },
    {
        "id": "ex-008",
        "instruction": "Store rice for 3 to 4 days in a sealed box.",
    },
]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return re.sub(r"\s+", " ", text).strip()


def redact(text: str) -> tuple[str, bool]:
    updated, email_count = EMAIL_RE.subn("[REDACTED_EMAIL]", text)
    updated, phone_count = PHONE_RE.subn("[REDACTED_PHONE]", updated)
    return updated, (email_count + phone_count) > 0


def clean(rows: list[dict[str, str]]) -> dict[str, object]:
    dropped_length: list[str] = []
    dropped_duplicate: list[str] = []
    redacted_ids: list[str] = []
    kept: list[dict[str, str]] = []
    seen: dict[str, str] = {}

    for row in rows:
        instruction = row["instruction"]
        if len(instruction) > MAX_CHARS:
            dropped_length.append(row["id"])
            continue
        cleaned, did_redact = redact(instruction)
        if did_redact:
            redacted_ids.append(row["id"])
        key = normalize(cleaned)
        if key in seen:
            dropped_duplicate.append(row["id"])
            continue
        seen[key] = row["id"]
        kept.append({"id": row["id"], "instruction": cleaned})

    return {
        "input": len(rows),
        "dropped_length": dropped_length,
        "dropped_duplicate": dropped_duplicate,
        "redacted": redacted_ids,
        "kept": kept,
    }


def main() -> None:
    report = clean(RAW_ROWS)
    kept = report["kept"]
    assert isinstance(kept, list)

    print("Synthetic PII filter + dedup demo")
    print("Not client data. Every row is invented.")
    print(f"input rows: {report['input']}")
    print(f"dropped (length): {', '.join(report['dropped_length']) or '—'}")
    print(f"dropped (duplicate): {', '.join(report['dropped_duplicate']) or '—'}")
    print(f"redacted: {', '.join(report['redacted']) or '—'}")
    print(f"kept: {len(kept)}")
    print()
    for row in kept:
        print(f"{row['id']} | {row['instruction']}")

    kept_ids = [row["id"] for row in kept]
    by_id = {row["id"]: row["instruction"] for row in kept}
    assert report["dropped_length"] == ["ex-006"]
    assert report["dropped_duplicate"] == ["ex-002", "ex-003"]
    assert report["redacted"] == ["ex-004", "ex-005"]
    assert kept_ids == ["ex-001", "ex-004", "ex-005", "ex-007", "ex-008"]
    assert by_id["ex-004"] == (
        "Reply to Ada Lovelace at [REDACTED_EMAIL] about the kettle warranty."
    )
    assert by_id["ex-005"] == (
        "Call the fictional help desk at [REDACTED_PHONE] and summarize the hours."
    )
    assert "3 to 4" in by_id["ex-008"]
    assert "[REDACTED" not in by_id["ex-008"]
    print()
    print("self-test: passed")


if __name__ == "__main__":
    main()
