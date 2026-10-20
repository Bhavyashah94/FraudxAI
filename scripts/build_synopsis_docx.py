#!/usr/bin/env python
"""Build the corrected B.E. Major Project I synopsis .docx for FraudxAI.

The single source of truth is `docs/SYNOPSIS_MASTER_CONTENT.md` (chapters, tables,
references) plus the figure files produced by `scripts/generate_synopsis_figures.py`;
the abstract and keywords are the `ABSTRACT` constant in this script.
This script exists so the submitted document cannot drift from the repository again:
the last hand-edited .docx advertised "64,850 events/s", "217 tests", "10 playbooks"
and a fabricated benchmark table, each contradicted by a file in this tree.

Everything is regenerated from source on every run; nothing is hand-edited in Word.

Usage:
    /tmp/opencode/docxenv/bin/python scripts/build_synopsis_docx.py \
        --out /home/bshah/Downloads/FraudxAI_Major_Project_1_Synopsis_REBUILT.docx \
        --figures /tmp/opencode/synopsisdocs/figures_build \
        [--pages /tmp/opencode/synopsisdocs/page_map.json]
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Mm, Pt

REPO = Path(__file__).resolve().parents[1]
MASTER = REPO / "docs" / "SYNOPSIS_MASTER_CONTENT.md"

TITLE = "FraudxAI: Grounded Multi-Agent Payment Fraud Simulation & Causal XAI Benchmark"
STUDENTS = [("Aariz Warsi", "58"), ("Anshul Tipnis", "49"), ("Bhavya Shah", "36"), ("Sagar Uradi", "54")]
GUIDES = ["Prof. Preeti Tiwari", "Prof. Pradnya Kamble"]

CHAPTER_TITLES = {
    1: "Introduction",
    2: "Review of Literature",
    3: "Report on the Present Investigation",
    4: "Aim and Objectives",
    5: "Problem Statement",
    6: "Proposed System",
    7: "Requirement Analysis",
    8: "Feasibility Study",
    9: "Design Details",
    10: "Implementation Plan & Preliminary Results",
    11: "Gantt Chart",
    12: "Conclusion and Future Scope",
}

FIGURE_FILES = {
    "6.1": "fig_6_1_architecture.png",
    "9.1": "fig_9_1_context.png",
    "9.2": "fig_9_2_dfd_l1.png",
    "9.3": "fig_9_3_sequence.png",
    "9.4": "fig_9_4_er.png",
    "9.5": "fig_9_5_control_flow.png",
    "10.1": "fig_10_1_dashboard.png",
    "10.2": "fig_10_2_concordance.png",
    "11.1": "fig_11_1_gantt.png",
}

FIG_LIST = [
    ("6.1", "FraudxAI System Architecture and Processing Pipeline"),
    ("9.1", "Context Level Diagram (Level 0 DFD)"),
    ("9.2", "Data Flow Diagram (Level 1 DFD)"),
    ("9.3", "UML Sequence Diagram for Transaction Authorization & Audit"),
    ("9.4", "Entity-Relationship (E-R) Diagram"),
    ("9.5", "Control Flow Diagram of Multi-Agent Simulation Engine"),
    ("10.1", "FraudxAI Interactive Telemetry and XAI Dashboard"),
    ("10.2", "Benchmarking Post-Hoc Explainers Against Ground-Truth SCM"),
    ("11.1", "Project Implementation Gantt Chart"),
]

TAB_LIST = [
    ("2.1", "Comparative Summary of Literature Survey"),
    ("7.1", "Hardware and Software Specifications"),
    ("8.1", "Feasibility Study Matrix"),
    ("10.1", "Baseline Model Performance and Explanation Fidelity Metrics"),
]

# One continuous paragraph by design (synopsis style): the body is a single string
# element, and the last element is the keywords line.
ABSTRACT = [
    "Digital payment economies process billions of daily transactions through card switches, "
    "point-of-sale terminals and instant mobile rails such as the Unified Payments Interface "
    "(UPI). The same expansion has grown coordinated fraud syndicates whose global card-fraud "
    "losses are estimated to exceed USD 35 billion annually [13], while over-aggressive "
    "blocking costs US merchants an estimated USD 118 billion per year in false declines, "
    "more than thirteen times the cost of actual card fraud [14]. Banking switches answer "
    "authorizations in under 50 milliseconds, and regulatory regimes (RBI master directions, "
    "the US Equal Credit Opportunity Act Regulation B, the Fair Credit Reporting Act and "
    "Federal Reserve SR 11-7) demand human-readable reasons for declined transactions. "
    "Explaining fraud decisions is nevertheless blocked by a ground-truth gap: production "
    "databases record only binary dispute labels, never the causal drivers of the fraud, and "
    "proprietary logs, 30-to-90-day chargeback latency and PCI-DSS restrictions keep "
    "researchers from reconstructing them. "
    "This project develops FraudxAI, an open-source multi-agent payment fraud simulation and "
    "causal XAI benchmarking platform. A 64-bit microsecond monotonic discrete-event engine "
    "driven by non-stationary Hawkes point processes schedules cardholder spend and merchant "
    "burstiness; dual-region rails reproduce US authorization and delayed clearing "
    "(ISO 8583 MTI 0100/0200, AVS) and Indian regulatory invariants (RBI two-factor "
    "authentication, RuPay on UPI); and 13 grounded adversarial playbooks (8 US + 5 India) "
    "adapt in closed loop to bank declines. Each fraudulent transaction is coupled to a "
    "Structural Causal Model that computes its exact Pearlian counterfactual twin and "
    "closed-form Shapley attributions, turning explanation correctness into a measurable "
    "quantity rather than a matter of opinion. "
    "Preliminary results are reported with their provenance. The engine is measured at "
    "2,015-2,626 events/second (1.5 GB peak memory) on commodity multi-core hardware; "
    "37 formal invariants are certified and the 410-test suite passes fully; and auditing "
    "post-hoc TreeSHAP against the causal ground truth shows modest rank concordance "
    "(Kendall τ_b 0.3106, Spearman ρ 0.3726, RAE 1.6927; LightGBM, n = 2,000, seed 42), the "
    "kind of evidence the platform exists to produce. A specification-driven four-pillar "
    "certification benchmark (data fidelity, adversarial privacy, streaming operations, "
    "causal XAI) grades the platform against declared thresholds: the current pinned "
    "evaluation passes all nineteen gates, the verdict's seed-to-seed spread across five "
    "evaluation pins is quantified, and the full scorecard, including the earlier audits "
    "that named breaches, is published in the project repository.",
    "Keywords: Payment Fraud Simulation, Multi-Agent Systems, Hawkes Processes, Causal "
    "Explainable AI, Shapley Attributions, Counterfactual Twins, Streaming Delayed Feedback.",
]


@dataclass
class Block:
    kind: str  # chapter | section | para | figure | table
    text: str = ""
    number: str = ""
    caption: str = ""
    rows: list = field(default_factory=list)


def parse_master(path: Path) -> tuple[list[Block], list[str], list[str]]:
    """Parse chapters, acknowledgement paragraphs and references from the master file."""
    lines = path.read_text(encoding="utf-8").splitlines()

    chapters: list[Block] = []
    ack: list[str] = []
    refs: list[str] = []

    # The master file's fence markers are malformed in places (a closing fence
    # written as ```text), so fence state is unreliable. Every rule below is
    # content-driven instead: a genuine Markdown table carries a `| :--- |`
    # separator row; ASCII diagrams never do.
    mode = None  # None | "chapter" | "back"
    subsection = None  # "ack" | "refs" once the back matter is reached
    pending_table = None
    table_buf: list[str] = []
    chapter_num = 0
    chapter_title = ""

    def _sep(cell: str) -> bool:
        return bool(re.fullmatch(r":?-{3,}:?", cell))

    def flush_table(blocks: list[Block]):
        nonlocal pending_table, table_buf
        rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in table_buf]
        if len(rows) >= 2 and any(all(_sep(c) for c in cs) for cs in rows):
            rows = [cs for cs in rows if not all(_sep(c) for c in cs)]
            blocks.append(Block("table", caption=pending_table or "", rows=rows))
        pending_table = None
        table_buf = []

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if line.startswith("## BACK MATTER"):
            flush_table(chapters)
            mode = "back"
            continue
        m = re.match(r"^## CHAPTER (\d+): (.+)$", line)
        if m:
            flush_table(chapters)
            chapter_num = int(m.group(1))
            chapter_title = m.group(2).strip()
            chapters.append(Block("chapter", number=str(chapter_num)))
            mode = "chapter"
            continue
        if line.startswith("## "):
            flush_table(chapters)
            mode = None
            continue

        if stripped.startswith("|"):
            if mode in ("chapter", "back"):
                table_buf.append(stripped)
            continue
        if table_buf:
            flush_table(chapters if mode == "chapter" else [])

        if (not stripped or stripped.startswith("```") or stripped.startswith("###")
                or stripped == "---"):
            continue

        if mode == "back":
            if stripped in {"Acknowledgement", "References"}:
                subsection = "ack" if stripped == "Acknowledgement" else "refs"
                continue
            if subsection == "refs":
                refs.append(stripped)
            else:
                ack.append(stripped)
            continue

        if mode != "chapter":
            continue

        if stripped.startswith("*(") or stripped.startswith("["):
            continue  # paste hints, [INSERT FIGURE ...], diagram frames
        if re.match(r"^\(.*\)$", stripped) and len(stripped) < 60:
            continue  # parenthesised labels from the ASCII diagrams, e.g. "(3.0 SCM Causal Engine)"
        if (re.match(r"^Chapter \d+$", stripped, re.I)
                or stripped.casefold() == chapter_title.casefold()):
            continue  # the fence repeats the chapter heading; the real one is emitted above
        if re.match(r"^\*\*Table \d+\.\d+:", stripped) or re.match(r"^Table \d+\.\d+:", stripped):
            pending_table = re.sub(r"\*\*", "", stripped).strip()
            continue
        m = re.match(r"^Figure (\d+\.\d+): (.+)$", stripped)
        if m:
            chapters.append(Block("figure", number=m.group(1), caption=f"Figure {m.group(1)}: {m.group(2)}"))
            continue
        m = re.match(r"^(\d{1,2})\.(\d{1,2}(?:\.\d)?)\s+(.+)$", stripped)
        if m and int(m.group(1)) == chapter_num:
            chapters.append(Block("section", number=f"{m.group(1)}.{m.group(2)}", text=m.group(3).strip()))
            continue
        if strip_diagram(stripped):
            continue
        chapters.append(Block("para", text=stripped))

    flush_table(chapters)
    return chapters, ack, refs


def strip_diagram(s: str) -> bool:
    """True when a line is part of an ASCII diagram rather than prose."""
    if set(s) <= set("|+-^v<>= "):
        return True
    if s.startswith("+") or s.startswith("|"):
        return True
    if "---" in s or "-->" in s or "<--" in s:
        return True
    if re.match(r"^[A-Za-z0-9_ ]+\s{2,}[A-Za-z0-9_ ]+(\s{2,}[A-Za-z0-9_ ]+)+$", s) and "  " in s:
        return True  # spaced column layouts of ASCII diagrams
    return False


def add_runs(paragraph, text: str) -> None:
    """Render **bold** spans and strip markdown/latex noise."""
    text = re.sub(r"\\text\{([^}]*)\}", r"\1", text)
    text = text.replace("`", "")
    text = text.replace("$", "")
    text = text.replace("^2", "\u00b2").replace("^b", "\u1d47")
    for i, part in enumerate(re.split(r"\*\*", text)):
        if not part:
            continue
        run = paragraph.add_run(part)
        run.bold = i % 2 == 1


def set_cell_text(cell, text: str, *, bold=False, size=9.0):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.line_spacing = 1.0
    add_runs(p, text)
    for run in p.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(size)
        if bold:
            run.font.bold = True


def add_page_number_footer(section, fmt: str | None, start: int | None):
    if fmt:
        sectPr = section._sectPr
        pg = OxmlElement("w:pgNumType")
        pg.set(qn("w:fmt"), fmt)
        if start is not None:
            pg.set(qn("w:start"), str(start))
        sectPr.append(pg)
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if fmt is None:
        return
    run = p.add_run()
    fld1 = OxmlElement("w:fldChar")
    fld1.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.text = "PAGE"
    fld2 = OxmlElement("w:fldChar")
    fld2.set(qn("w:fldCharType"), "end")
    run._r.append(fld1)
    run._r.append(instr)
    run._r.append(fld2)
    for r in p.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)


def add_header(section):
    section.header.is_linked_to_previous = False
    p = section.header.paragraphs[0]
    p.paragraph_format.tab_stops.add_tab_stop(Inches(6.3), WD_TAB_ALIGNMENT.RIGHT)
    run = p.add_run("FraudxAI\t2026-2027")
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)


def paragraph(doc, text: str, *, size=12, bold=False, italic=False, align="justify",
              space_after=6, space_before=0, line_spacing=1.5, first_line_indent=None):
    p = doc.add_paragraph()
    p.alignment = {
        "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
        "center": WD_ALIGN_PARAGRAPH.CENTER,
        "left": WD_ALIGN_PARAGRAPH.LEFT,
        "right": WD_ALIGN_PARAGRAPH.RIGHT,
    }[align]
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if first_line_indent:
        p.paragraph_format.first_line_indent = Inches(first_line_indent)
    add_runs(p, text)
    if bold or italic:
        for run in p.runs:
            run.bold = bold or run.bold
            run.italic = italic or run.italic
    for run in p.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(size)
    return p


def add_figure(doc, figures: Path, number: str):
    fname = FIGURE_FILES.get(number)
    if fname and (figures / fname).exists():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run()
        run.add_picture(str(figures / fname), width=Inches(6.1))
    else:
        paragraph(doc, f"[missing figure {number}]", align="center")


def add_table(doc, block: Block, pages: dict):
    if block.caption:
        paragraph(doc, block.caption, size=11, bold=True, align="center", space_after=4, line_spacing=1.0)
    rows = block.rows
    if not rows:
        return
    width = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=width)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, row in enumerate(rows):
        for ci in range(width):
            text = row[ci] if ci < len(row) else ""
            set_cell_text(table.cell(ri, ci), text, bold=(ri == 0), size=9.0)
    paragraph(doc, "", space_after=2, line_spacing=1.0)


def simple_table(doc, rows, widths=None, header=True, size=10.5):
    table = doc.add_table(rows=len(rows), cols=len(rows[0]))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, row in enumerate(rows):
        for ci, text in enumerate(row):
            set_cell_text(table.cell(ri, ci), str(text), bold=(header and ri == 0), size=size)
    if widths:
        for ci, w in enumerate(widths):
            for ri in range(len(rows)):
                table.cell(ri, ci).width = Inches(w)
    paragraph(doc, "", space_after=2, line_spacing=1.0)
    return table


def build(out_path: Path, figures: Path, pages: dict):
    doc = Document()

    # base style
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    normal.paragraph_format.line_spacing = 1.5
    normal.paragraph_format.space_after = Pt(6)

    sec = doc.sections[0]
    sec.page_width = Mm(210)
    sec.page_height = Mm(297)
    sec.top_margin = sec.bottom_margin = sec.left_margin = sec.right_margin = Inches(1)
    add_header(sec)  # the college template carries the running header on every page

    def heading(text, size=16, space_before=6, space_after=12, break_before=False):
        # `page_break_before` avoids the empty-paragraph blank pages that
        # doc.add_page_break() produces when the previous content ends at a
        # page boundary.
        p = paragraph(doc, text, size=size, bold=True, align="center",
                      space_after=space_after, line_spacing=1.2)
        if break_before:
            p.paragraph_format.page_break_before = True
        return p

    # ---------------- COVER ----------------
    paragraph(doc, "Synopsis of Project work on,", size=12, align="center", space_after=2, line_spacing=1.2)
    paragraph(doc, TITLE, size=16, bold=True, align="center", space_after=18, line_spacing=1.3)
    paragraph(doc, "Submitted in partial fulfillment of the requirements of the degree", size=12,
              align="center", space_after=2, line_spacing=1.2)
    paragraph(doc, "of", size=12, align="center", space_after=2, line_spacing=1.2)
    paragraph(doc, "Bachelor of Engineering in Information Technology", size=13, bold=True,
              align="center", space_after=16, line_spacing=1.2)
    paragraph(doc, "By:", size=12, bold=True, align="center", space_after=4, line_spacing=1.2)
    for name, roll in STUDENTS:
        paragraph(doc, f"{name} {roll}", size=12, align="center", space_after=2, line_spacing=1.2)
    paragraph(doc, "Supervisor(s):", size=12, bold=True, align="center", space_after=4, line_spacing=1.2)
    for g in GUIDES:
        paragraph(doc, g, size=12, align="center", space_after=1, line_spacing=1.2)
        paragraph(doc, "Assistant Professor", size=11, align="center", space_after=4, line_spacing=1.2)
    logo = figures / "college_logo.png"
    if logo.exists():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(6)
        p.add_run().add_picture(str(logo), width=Inches(2.4))
    paragraph(doc, "Department of Information Technology", size=13, bold=True,
              align="center", space_after=4, line_spacing=1.2)
    paragraph(doc, "AET\u2019s", size=12, align="center", space_after=0, line_spacing=1.2)
    paragraph(doc, "Atharva College of Engineering", size=14, bold=True,
              align="center", space_after=0, line_spacing=1.2)
    paragraph(doc, "Malad West, Mumbai \u2014 400095", size=12, align="center", space_after=0, line_spacing=1.2)
    paragraph(doc, "University of Mumbai", size=12, align="center", space_after=0, line_spacing=1.2)
    paragraph(doc, "2026-2027", size=12, bold=True, align="center", space_after=0, line_spacing=1.2)

    # ---------------- CERTIFICATE ----------------
    cert_logo = figures / "college_logo.png"
    if cert_logo.exists():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.page_break_before = True
        p.add_run().add_picture(str(cert_logo), width=Inches(1.6))
    heading("AET\u2019S ATHARVA COLLEGE OF ENGINEERING", size=13,
            break_before=not cert_logo.exists())
    heading("CERTIFICATE", size=16)
    paragraph(doc, "This is to certify that", align="center", space_after=10)
    for name, roll in STUDENTS:
        paragraph(doc, f"{name} \u2014 {roll}", size=12, bold=True, align="center", space_after=2, line_spacing=1.2)
    paragraph(doc, "have satisfactorily completed the requirements of the Synopsis", align="center",
              space_after=6, space_before=8)
    paragraph(doc, "on", align="center", space_after=6, line_spacing=1.2)
    paragraph(doc, TITLE, size=12, bold=True, align="center", space_after=6, line_spacing=1.3)
    paragraph(doc, "as prescribed by the University of Mumbai for the academic year 2026\u201327",
              align="center", space_after=10, line_spacing=1.2)
    paragraph(doc, "under the guidance of", align="center", space_after=4, line_spacing=1.2)
    paragraph(doc, " & ".join(GUIDES), size=12, bold=True, align="center", space_after=2, line_spacing=1.2)
    paragraph(doc, "Guide(s)", size=11, italic=True, align="center", space_after=22, line_spacing=1.2)
    simple_table(doc, [
        ["Dr. Nileema Pathak", "Dr. Bhavna Arora", "Dr. Ramesh Kulkarni"],
        ["Project Coordinator", "Head (Information Technology)", "Principal"],
        ["", "", ""],
        ["Internal Examiner", "College Seal", "External Examiner"],
    ], widths=None, header=False)

    # ---------------- APPROVAL ----------------
    heading("MAJOR PROJECT I SYNOPSIS APPROVAL FOR B.E.", size=15, break_before=True)
    paragraph(doc,
              f"This Major Project I synopsis entitled \u201c{TITLE}\u201d by "
              + ", ".join(f"{n} ({r})" for n, r in STUDENTS)
              + " is approved for the award of the degree of Bachelor of Engineering in "
                "Information Technology, as prescribed by the University of Mumbai for the "
                "academic year 2026\u201327.",
              space_after=16)
    paragraph(doc, "Examiners:", bold=True, align="left", space_after=10)
    paragraph(doc, "1. \u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", align="left", space_after=10)
    paragraph(doc, "2. \u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", align="left", space_after=30)
    paragraph(doc, "Date: \u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", align="left", space_after=6)
    paragraph(doc, "Place: Atharva College of Engineering, Mumbai.", align="left", space_after=6)

    # ---------------- DECLARATION ----------------
    heading("DECLARATION", break_before=True)
    paragraph(doc,
              "We declare that this written submission represents our ideas in our own words and "
              "where others\u2019 ideas or words have been included, we have adequately cited and "
              "referenced the original sources. We also declare that we have adhered to all "
              "principles of academic honesty and integrity and have not misrepresented or "
              "fabricated or falsified any idea/data/fact/source in our submission. We understand "
              "that any violation of the above will cause disciplinary action by the Institute and "
              "can also evoke penal action from the sources which have thus not been properly cited "
              "or from whom proper permission has not been taken when needed.")
    paragraph(doc, "Signature(s):", bold=True, align="left", space_after=10)
    for name, roll in STUDENTS:
        paragraph(doc, f"{name} ({roll})", bold=True, align="left", space_after=4, line_spacing=1.2)
    paragraph(doc, "Date: \u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", align="left",
              space_after=4, space_before=18, line_spacing=1.2)
    paragraph(doc, "Place: Atharva College of Engineering, Mumbai.", align="left",
              space_after=4, line_spacing=1.2)

    # ---------------- SECTION 2: ABSTRACT, INDEX, LISTS (roman) ----------------
    sec2 = doc.add_section(WD_SECTION.NEW_PAGE)
    sec2.page_width, sec2.page_height = Mm(210), Mm(297)
    sec2.top_margin = sec2.bottom_margin = sec2.left_margin = sec2.right_margin = Inches(1)
    sec2.different_first_page_header_footer = False
    add_header(sec2)
    add_page_number_footer(sec2, "upperRoman", 1)

    heading("ABSTRACT")
    for para in ABSTRACT[:-1]:
        paragraph(doc, para, size=11.5, line_spacing=1.3, space_after=5)
    paragraph(doc, ABSTRACT[-1], size=11.5, line_spacing=1.3, space_after=6)

    heading("INDEX", break_before=True)
    chap_pages = pages.get("chapters", {})
    index_rows = [["Sr. No.", "Content", "Page No."],
                  ["1", "Certificate", "\u2014"],
                  ["2", "Declaration", "\u2014"],
                  ["3", "Abstract", "I"],
                  ["4", "Index", "II"],
                  ["5", "List of Figures", "III"],
                  ["6", "List of Tables", "IV"],
                  ["7", "List of Abbreviations", "V"]]
    fig_pages = pages.get("figures", {})
    for i in range(1, 13):
        index_rows.append([str(7 + i), f"Chapter {i}: {CHAPTER_TITLES[i]}", str(chap_pages.get(str(i), ""))])
        if i == 9:  # the college template nests the Chapter-9 diagrams under the chapter row
            for num, cap in FIG_LIST:
                if num.startswith("9."):
                    index_rows.append([num, f"    {cap}", str(fig_pages.get(num, ""))])
    index_rows.append(["20", "Acknowledgement", str(pages.get("ack", ""))])
    index_rows.append(["21", "References", str(pages.get("refs", ""))])
    simple_table(doc, index_rows, widths=[0.8, 4.4, 1.0], size=11)

    heading("LIST OF FIGURES", break_before=True)
    fig_rows = [["Figure No.", "Name of Figure", "Page No."]]
    for num, cap in FIG_LIST:
        fig_rows.append([num, cap, str(fig_pages.get(num, ""))])
    simple_table(doc, fig_rows, widths=[1.0, 4.2, 1.0], size=11)

    heading("LIST OF TABLES", break_before=True)
    tab_rows = [["Table No.", "Name of Table", "Page No."]]
    for num, cap in TAB_LIST:
        tab_rows.append([num, cap, str(pages.get("tables", {}).get(num, ""))])
    simple_table(doc, tab_rows, widths=[1.0, 4.2, 1.0], size=11)

    heading("LIST OF ABBREVIATIONS", break_before=True)
    abbr = [
        ["Abbreviation", "Expansion", "Pages"],
        ["B.E.", "Bachelor of Engineering", "I, II"],
        ["IT", "Information Technology", "I, II"],
        ["AET\u2019s", "Atharva Educational Trust\u2019s", "I"],
        ["XAI", "Explainable Artificial Intelligence", "I, 1, 4, 5"],
        ["SCM", "Structural Causal Model", "2, 8, 10, 11"],
        ["SHAP", "SHapley Additive exPlanations", "4, 8, 12, 21"],
        ["EBM", "Explainable Boosting Machine", "4"],
        ["ISO", "International Organization for Standardization", "2, 6, 8, 9"],
        ["UPI", "Unified Payments Interface", "I, 1, 8"],
        ["RBI", "Reserve Bank of India", "I, 1, 2, 8, 9"],
        ["AFA", "Additional Factor of Authentication", "2, 11, 19"],
        ["EMV", "Europay Mastercard and Visa", "6"],
        ["3DS", "3-D Secure Protocol", "6, 18"],
        ["POS", "Point of Sale", "1, 17"],
        ["AVS", "Address Verification System", "I, 2, 6, 8"],
        ["STIP", "Stand-In Processing", "1, 13"],
        ["DFD", "Data Flow Diagram", "16, 17"],
        ["ERD", "Entity Relationship Diagram", "18, 19"],
        ["PR-AUC", "Precision-Recall Area Under Curve", "21, 22"],
        ["RAE", "Relative Attribution Error", "I, 21, 22"],
    ]
    simple_table(doc, abbr, widths=[1.2, 3.8, 1.2], size=10.5)

    # ---------------- SECTION 3: CHAPTERS (arabic) ----------------
    sec3 = doc.add_section(WD_SECTION.NEW_PAGE)
    sec3.page_width, sec3.page_height = Mm(210), Mm(297)
    sec3.top_margin = sec3.bottom_margin = sec3.left_margin = sec3.right_margin = Inches(1)
    add_header(sec3)
    add_page_number_footer(sec3, "decimal", 1)

    chapters, ack, refs = parse_master(MASTER)

    first_chapter = True
    for block in chapters:
        if block.kind == "chapter":
            num = int(block.number)
            heading(f"Chapter {num}", size=16, space_after=2, break_before=not first_chapter)
            heading(CHAPTER_TITLES.get(num, ""), size=16, space_after=14)
            first_chapter = False
        elif block.kind == "section":
            paragraph(doc, f"{block.number} {block.text}", size=14, bold=True, align="left",
                      space_before=8, space_after=6, line_spacing=1.3)
        elif block.kind == "figure":
            add_figure(doc, figures, block.number)
            paragraph(doc, block.caption, size=11, bold=True, align="center",
                      space_after=10, line_spacing=1.15)
        elif block.kind == "table":
            add_table(doc, block, pages)
        else:
            paragraph(doc, block.text)

    # ---------------- ACKNOWLEDGEMENT + REFERENCES ----------------
    heading("Acknowledgement", size=16, break_before=True)
    for para in ack:
        paragraph(doc, para)
    heading("References", size=16, break_before=True)
    for ref in refs:
        p = paragraph(doc, ref, align="justify", space_after=6, line_spacing=1.15)
        p.paragraph_format.left_indent = Inches(0.35)
        p.paragraph_format.first_line_indent = Inches(-0.35)

    doc.save(str(out_path))
    print(f"wrote {out_path}")
    print(f"chapters: {sum(1 for b in chapters if b.kind=='chapter')}, "
          f"figures: {sum(1 for b in chapters if b.kind=='figure')}, "
          f"tables: {sum(1 for b in chapters if b.kind=='table')}, "
          f"references: {len(refs)}, acknowledgement paragraphs: {len(ack)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--figures", type=Path, default=Path("/tmp/opencode/synopsisdocs/figures_build"))
    ap.add_argument("--pages", type=Path, default=None,
                    help="JSON with {'index': [[...]], 'figures': {...}, 'tables': {...}} page numbers")
    args = ap.parse_args()
    pages = json.loads(args.pages.read_text()) if args.pages and args.pages.exists() else {}
    build(args.out, args.figures, pages)


if __name__ == "__main__":
    main()
