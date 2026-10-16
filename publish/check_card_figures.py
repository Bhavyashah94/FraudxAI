"""Self-check every published enrichment figure in the three dataset cards.

Extracts the "Real world (spec)" / "This dataset" / "Ratio" rows from each card's
enrichment table and verifies that the reader can reproduce the ratio from the two numbers
printed beside it. A disclosure whose own arithmetic does not close is worse than none.

Run:  python publish/check_card_figures.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = {
    "US 100k": ROOT / "publish" / "README.md",
    "India 100k": ROOT / "publish" / "india_100k" / "README.md",
    "US 500k": ROOT / "publish" / "us_500k" / "README.md",
}

# Row label -> how to turn the printed reference/measured cells into a comparable number.
UNITS = {
    "Fraud as a share of transactions": ("pct", 1.0),
    "Fraud as a share of purchase value": ("bps", 1.0),
    "Fraud as a share of transaction value": ("bps", 1.0),
    "Average amount on a fraud transaction": ("money", 1.0),
}


def parse_number(text: str, kind: str) -> float:
    cleaned = text.replace(",", "").replace("**", "").strip()
    cleaned = cleaned.rstrip("x").strip()
    if cleaned.endswith("%"):
        return float(cleaned[:-1])
    if cleaned.endswith("bps"):
        return float(cleaned[:-3])
    for symbol in ("Rs", "$"):
        if cleaned.startswith(symbol):
            return float(cleaned[len(symbol):])
    return float(cleaned)


def main() -> int:
    failures = []
    for label, card in CARDS.items():
        text = card.read_text()
        if "Deliberately Enriched" not in text:
            failures.append(f"{label}: no enrichment disclosure section")
            continue
        rows = re.findall(
            r"^\|\s*((?:Fraud as a share of|Average amount on a fraud transaction)[^|]*?)"
            r"\s*\|\s*([^|]+?)\s*\|\s*\**([^|*]+?)\**\s*\|\s*\**([^*|]+?)\**\s*\|",
            text,
            re.MULTILINE,
        )
        if len(rows) < 3:
            failures.append(f"{label}: parsed {len(rows)} table rows, expected 3")
            continue
        print(f"\n{label}  ({card.relative_to(ROOT)})")
        for row_label, ref_cell, meas_cell, ratio_cell in rows:
            ref = parse_number(ref_cell, "")
            meas = parse_number(meas_cell, "")
            stated = parse_number(ratio_cell, "")
            computed = meas / ref
            ok = abs(computed - stated) <= max(0.02 * stated, 0.05)
            print(
                f"  {row_label:44s} {ref:>12g} -> {meas:>12g} "
                f"= {computed:9,.1f}x  stated {stated:g}x  {'OK' if ok else 'MISMATCH'}"
            )
            if not ok:
                failures.append(
                    f"{label}: '{row_label}' ratio {stated}x but {ref}->{meas} is {computed:.1f}x"
                )
    print()
    if failures:
        print("FAILURES:")
        for f in failures:
            print("  -", f)
        return 1
    print("all published ratios are reproducible from the printed operands")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())