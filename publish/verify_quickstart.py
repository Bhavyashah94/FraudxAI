#!/usr/bin/env python3
"""Verify the quickstart in a published dataset card actually runs and prints its claim.

Extracts the Python block under "## 4. Quickstart" from a card, executes it against a
CSV, and compares the ROC-AUC / PR-AUC it prints against the "Expected output" block in
the same file. Exits non-zero on any mismatch, so a stale number cannot be published.

Usage:
    python publish/verify_quickstart.py <card.md> <data.csv>
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path


def extract_code(card: Path) -> str:
    """Return the quickstart code block, with the card's own filename rebound to data."""
    text = card.read_text()
    match = re.search(
        r"^## 4\..*?^```python\n(.*?)^```",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise SystemExit(f"{card}: no '## 4.' python quickstart block found")
    code = match.group(1)
    # The card hardcodes the published filename; point it at whatever file we were given.
    code = re.sub(r"'[\w\-]+\.csv'", "DATA_PATH", code)
    return code.replace("DATA_PATH", "str(DATA)")


def extract_expected(card: Path) -> tuple[str, str]:
    """Return the ROC-AUC and PR-AUC the card claims the quickstart will print."""
    text = card.read_text()
    m = re.search(
        r"^ROC-AUC: ([\d.]+)\s*\nPR-AUC \(Average Precision\): ([\d.]+)",
        text,
        re.MULTILINE,
    )
    if not m:
        raise SystemExit(f"{card}: no 'Expected output' ROC/PR block found")
    return m.group(1), m.group(2)


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    card_arg, data_arg = sys.argv[1], sys.argv[2]
    card = Path(card_arg)
    data = Path(data_arg).resolve()
    if not data.exists():
        print(f"FAIL data file not found: {data}")
        return 2

    claim_roc, claim_pr = extract_expected(card)
    code = extract_code(card)
    print(f"card      : {card}")
    print(f"data      : {data}")
    print(f"claims    : ROC-AUC {claim_roc}  PR-AUC {claim_pr}")

    script = "import pandas as pd\nfrom pathlib import Path\nDATA = Path(r'%s')\n%s" % (
        data,
        code,
    )
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
        fh.write(script)
        tmp = fh.name
    proc = subprocess.run([sys.executable, tmp], capture_output=True, text=True)
    Path(tmp).unlink(missing_ok=True)

    out = proc.stdout
    if proc.returncode != 0:
        print("FAIL the card's quickstart did not run:")
        print(proc.stderr[-2000:])
        return 1

    m = re.search(r"ROC-AUC: ([\d.]+)", out)
    n = re.search(r"PR-AUC \(Average Precision\): ([\d.]+)", out)
    if not m or not n:
        print("FAIL quickstart printed no ROC/PR line")
        print(out[-2000:])
        return 1
    got_roc, got_pr = m.group(1), n.group(1)
    print(f"measured  : ROC-AUC {got_roc}  PR-AUC {got_pr}")

    ok = got_roc == claim_roc and got_pr == claim_pr
    print("RESULT    :", "MATCH" if ok else "MISMATCH")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())