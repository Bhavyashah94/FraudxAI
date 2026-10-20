"""Regression guards for the generated B.E. synopsis.

The synopsis .docx is rebuilt from `docs/SYNOPSIS_MASTER_CONTENT.md` and the figure
files, so the document cannot drift from the repository by hand-editing Word. These
tests pin the two properties that make that claim true: the master content parses
into every declared chapter/figure/table, and the builder writes a readable .docx
even when the generated figure assets are not present.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

pytest.importorskip(
    "docx",
    reason="synopsis build needs the docs extra: pip install '.[docs]'",
)

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

import build_synopsis_docx as synopsis  # noqa: E402
import generate_synopsis_figures as figures  # noqa: E402


def test_master_content_parses_into_every_declared_block():
    chapters, acknowledgement, references = synopsis.parse_master(synopsis.MASTER)

    chapter_numbers = [int(block.number) for block in chapters if block.kind == "chapter"]
    assert chapter_numbers == list(range(1, 13))

    parsed_figures = {block.number for block in chapters if block.kind == "figure"}
    assert parsed_figures == set(synopsis.FIGURE_FILES)

    parsed_tables = [block.caption for block in chapters if block.kind == "table"]
    assert len(parsed_tables) == len(synopsis.TAB_LIST)
    for number, _caption in synopsis.TAB_LIST:
        assert any(caption.startswith(f"Table {number}:") for caption in parsed_tables)

    assert acknowledgement, "the acknowledgement section must not disappear"
    assert references, "the reference list must not disappear"


def test_builder_writes_a_docx_without_generated_figures(tmp_path: Path):
    out_path = tmp_path / "synopsis.docx"
    synopsis.build(out_path, tmp_path / "missing_figures", {})

    assert out_path.exists()
    assert out_path.stat().st_size > 10_000

    from docx import Document

    text = "\n".join(paragraph.text for paragraph in Document(out_path).paragraphs)
    for number, title in synopsis.CHAPTER_TITLES.items():
        assert f"Chapter {number}" in text
        assert title in text
    assert "References" in text


def test_figure_builder_writes_a_png(tmp_path: Path):
    out_path = figures.figure_gantt(tmp_path)

    assert out_path.exists()
    assert out_path.suffix == ".png"
    assert out_path.stat().st_size > 1_000
