#!/usr/bin/env python3
"""Render dataset-cover-image.png from the published export's own measurements.

The cover quotes four numbers. Three of them are read straight out of the staged
*.csv.gz at runtime rather than typed in, so the image cannot drift away from the
data it describes:

    transactions  row count of the main export
    fraud rate    is_fraud == 1 over that row count
    span          max - min timestamp_utc, in days
    views         number of staged *.csv.gz files

The canvas is square on purpose. Kaggle renders a dataset cover as a square and
center-crops anything wider, which cut this banner in half; a 1:1 layout survives
that crop intact and Hugging Face renders it at its natural ratio.

Usage:

    FRAUDX_DATA_DIR=/path/to/staged python publish/make_cover_image.py

Writes publish/dataset-cover-image.png. Requires Pillow.
"""

from __future__ import annotations

import csv
import gzip
import os
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "dataset-cover-image.png"
W, H = 1000, 1000

BG_TOP = (10, 18, 32)
BG_BOTTOM = (13, 25, 45)
ACCENT = (86, 199, 255)
ACCENT_DIM = (46, 96, 130)
TEXT = (232, 240, 248)
MUTED = (150, 168, 186)
CARD_BG = (17, 31, 52)
CARD_EDGE = (35, 58, 88)

FONT_DIR = "/usr/share/fonts/noto"


def _font(name: str, size: int) -> ImageFont.FreeTypeFont:
    path = os.path.join(FONT_DIR, name)
    if not os.path.exists(path):
        raise SystemExit(f"font not found: {path}")
    return ImageFont.truetype(path, size)


def measure(data_dir: Path) -> dict:
    """Read the four cover figures straight from the staged export."""
    files = sorted(data_dir.glob("*.csv.gz"))
    if not files:
        raise SystemExit(f"no *.csv.gz in {data_dir}")

    main = data_dir / "fraudxai_us_100k_seed42.csv.gz"
    if not main.exists():
        main = files[0]

    rows = fraud = 0
    first = last = None
    with gzip.open(main, "rt", newline="") as fh:
        for row in csv.DictReader(fh):
            rows += 1
            fraud += int(row["is_fraud"])
            ts = datetime.fromisoformat(row["timestamp_utc"])
            first = ts if first is None or ts < first else first
            last = ts if last is None or ts > last else last

    if not rows or first is None:
        raise SystemExit("export is empty; cannot measure a cover")

    return {
        "rows": rows,
        "rate": 100.0 * fraud / rows,
        "span": (last - first).total_seconds() / 86400.0,
        "views": len(files),
    }


def gradient() -> Image.Image:
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        d.line(
            [(0, y), (W, y)],
            fill=tuple(int(a + (b - a) * t) for a, b in zip(BG_TOP, BG_BOTTOM)),
        )
    return img


def mesh(img: Image.Image, seed: int = 42) -> None:
    """A sparse node/edge motif, deterministic so re-renders are byte-stable."""
    d = ImageDraw.Draw(img)
    s = seed
    pts = []
    for _ in range(24):
        s = (1103515245 * s + 12345) % (2**31)
        x = s % W
        s = (1103515245 * s + 12345) % (2**31)
        y = s % H
        pts.append((x, y))
    for i, (x1, y1) in enumerate(pts):
        for x2, y2 in pts[i + 1:]:
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if dist < 300:
                fade = max(0.0, 1.0 - dist / 300)
                c = tuple(int(v * fade * 0.28) for v in ACCENT_DIM)
                d.line([(x1, y1), (x2, y2)], fill=c, width=1)
    for x, y in pts:
        d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=ACCENT_DIM)


def stat_card(d: ImageDraw.ImageDraw, box: tuple, value: str, label: str,
              vf, lf) -> None:
    x1, y1, x2, _y2 = box
    d.rounded_rectangle(box, radius=12, fill=CARD_BG, outline=CARD_EDGE, width=1)
    vw = d.textlength(value, font=vf)
    d.text(((x1 + x2 - vw) / 2, y1 + 32), value, font=vf, fill=ACCENT)
    lw = d.textlength(label, font=lf)
    d.text(((x1 + x2 - lw) / 2, y1 + 92), label, font=lf, fill=MUTED)


def render(m: dict) -> Image.Image:
    img = gradient()
    mesh(img)
    d = ImageDraw.Draw(img)

    title = _font("NotoSans-Bold.ttf", 86)
    sub = _font("NotoSans-Regular.ttf", 33)
    tag = _font("NotoSans-Regular.ttf", 20)
    vf = _font("NotoSans-Bold.ttf", 40)
    lf = _font("NotoSans-Regular.ttf", 18)

    def center(y: int, text: str, font, fill) -> None:
        w = d.textlength(text, font=font)
        d.text(((W - w) / 2, y), text, font=font, fill=fill)

    center(150, "FraudxAI", title, ACCENT)
    center(262, "100,000 US Card Transactions Benchmark", sub, TEXT)
    center(
        320,
        "Discrete-Event Payment Simulator  \u2022  ISO 8583 Rails  \u2022  Pearlian Causal Twins",
        tag,
        MUTED,
    )

    cards = [
        (f"{m['rows']:,}", "Transactions"),
        (f"{m['rate']:.3f}%", "Fraud Prevalence"),
        (f"{m['span']:.2f} Days", "Simulated Span"),
        (str(m['views']), "Institutional Views"),
    ]

    margin, gap, ch = 90, 30, 150
    cw = (W - 2 * margin - gap) / 2
    for i, (value, label) in enumerate(cards):
        row, col = divmod(i, 2)
        x1 = margin + col * (cw + gap)
        y1 = 430 + row * (ch + gap)
        stat_card(d, (x1, y1, x1 + cw, y1 + ch), value, label, vf, lf)

    center(
        840,
        "Synthetic data. No real cardholder, card number or merchant appears in it.",
        _font("NotoSans-Regular.ttf", 19),
        MUTED,
    )
    return img


def main() -> None:
    data_dir = os.environ.get("FRAUDX_DATA_DIR")
    if not data_dir:
        raise SystemExit("set FRAUDX_DATA_DIR to the directory of staged *.csv.gz")
    m = measure(Path(data_dir))
    render(m).save(OUT)
    print(
        f"wrote {OUT} ({W}x{H})\n"
        f"  rows={m['rows']:,}  rate={m['rate']:.3f}%  "
        f"span={m['span']:.2f}d  views={m['views']}"
    )


if __name__ == "__main__":
    sys.exit(main())
