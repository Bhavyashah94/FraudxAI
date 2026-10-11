#!/usr/bin/env python3
"""Render dataset-cover-image.png: a static, iconic FraudxAI brand emblem.

The canvas is exactly 560x280 pixels, matching Kaggle's upload API specifications:
1. Cover image rectangle: (left=0, top=0, width=560, height=280)
2. Thumbnail rectangle: (left=140, top=0, width=280, height=280)

All primary visual elements (the hexagonal causal neural emblem, the FraudxAI
lettermark, and the subtitle) are centered at (x=280, y=140) inside the central
280px window (x in [140, 420]). This ensures the graphic displays cleanly and
without text clipping in both the full banner and the square thumbnail.

Usage:
    python publish/make_cover_image.py
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "dataset-cover-image.png"
W, H = 560, 280

BG_DARK = (10, 15, 30)
CYAN = (0, 229, 255)
BLUE = (37, 99, 235)
WHITE = (255, 255, 255)
PURPLE = (168, 85, 247)
MUTED = (148, 163, 184)

FONT_DIR = "/usr/share/fonts/noto"


def _font(name: str, size: int) -> ImageFont.FreeTypeFont:
    path = os.path.join(FONT_DIR, name)
    if not os.path.exists(path):
        raise SystemExit(f"font not found: {path}")
    return ImageFont.truetype(path, size)


def render_logo() -> Image.Image:
    img = Image.new("RGB", (W, H), BG_DARK)
    d = ImageDraw.Draw(img)

    cx, cy = W // 2, H // 2

    # Radial gradient / soft atmospheric glow behind the emblem
    for r in range(180, 0, -2):
        alpha = int(45 * (1.0 - r / 180.0))
        c = (10 + alpha // 2, 15 + alpha, 30 + alpha * 2)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)

    # Geometric Causal Neural Emblem (Shield / Hexagonal Causal Core)
    ecx, ecy = cx, cy - 36
    radius = 48

    # Outer Hexagon
    hex_pts = []
    for i in range(6):
        angle = math.radians(60 * i - 30)
        hx = ecx + radius * math.cos(angle)
        hy = ecy + radius * math.sin(angle)
        hex_pts.append((hx, hy))

    d.polygon(hex_pts, fill=(15, 23, 42), outline=CYAN, width=3)

    # Inner directed causal graph edges
    d.line([(ecx, ecy - 30), (ecx, ecy)], fill=CYAN, width=2)
    d.line([(ecx - 24, ecy + 12), (ecx, ecy)], fill=BLUE, width=2)
    d.line([(ecx + 24, ecy + 12), (ecx, ecy)], fill=PURPLE, width=2)
    d.line([(ecx - 24, ecy + 12), (ecx + 24, ecy + 12)], fill=(40, 60, 100), width=1)

    # Central glowing junction node
    d.ellipse([ecx - 6, ecy - 6, ecx + 6, ecy + 6], fill=CYAN)
    d.ellipse([ecx - 3, ecy - 3, ecx + 3, ecy + 3], fill=WHITE)

    # Hexagon vertex anchor nodes
    for hx, hy in hex_pts:
        d.ellipse([hx - 3, hy - 3, hx + 3, hy + 3], fill=CYAN)

    # Secondary causal nodes
    d.ellipse([ecx - 4, ecy - 34, ecx + 4, ecy - 26], fill=WHITE)
    d.ellipse([ecx - 28, ecy + 8, ecx - 20, ecy + 16], fill=BLUE)
    d.ellipse([ecx + 20, ecy + 8, ecx + 28, ecy + 16], fill=PURPLE)

    # Typography
    font_title = _font("NotoSans-Bold.ttf", 38)
    font_sub = _font("NotoSans-Regular.ttf", 12)

    w_fraud = d.textlength("Fraud", font=font_title)
    w_xai = d.textlength("xAI", font=font_title)
    total_w = w_fraud + w_xai

    ty = cy + 32
    start_x = cx - total_w / 2

    d.text((start_x, ty), "Fraud", font=font_title, fill=WHITE)
    d.text((start_x + w_fraud, ty), "xAI", font=font_title, fill=CYAN)

    # Minimal clean subtitle
    tag = "CAUSAL PAYMENT INTELLIGENCE"
    w_tag = d.textlength(tag, font=font_sub)
    d.text((cx - w_tag / 2, ty + 50), tag, font=font_sub, fill=MUTED)

    return img


def main() -> None:
    img = render_logo()
    img.save(OUT)
    print(f"wrote static logo cover to {OUT} ({W}x{H})")


if __name__ == "__main__":
    sys.exit(main())
