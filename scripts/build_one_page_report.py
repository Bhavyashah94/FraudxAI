"""Builds the Project One Page Report for FraudxAI (Group 18)
by cleanly modifying the official Atharva College of Engineering docx template.
"""

from pathlib import Path
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn


def set_cell_margins(cell, top=35, bottom=35, left=55, right=55):
    """Sets cell margins in dxa (1 pt = 20 dxa)."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders(table):
    """Sets clean borders on the table."""
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            r'<w:tblBorders %s>'
            r'  <w:top w:val="single" w:sz="6" w:space="0" w:color="555555"/>'
            r'  <w:left w:val="single" w:sz="6" w:space="0" w:color="555555"/>'
            r'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="555555"/>'
            r'  <w:right w:val="single" w:sz="6" w:space="0" w:color="555555"/>'
            r'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            r'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            r'</w:tblBorders>' % nsdecls('w')
        )
        tblPr[0].append(borders)


def format_field(p, label, value, before_pt=0, after_pt=1.5, size_pt=10.0, line_spacing=1.05):
    """Formats a key-value field paragraph."""
    p.text = ""
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.space_before = Pt(before_pt)
    pf.space_after = Pt(after_pt)
    pf.line_spacing = line_spacing

    if label:
        r1 = p.add_run(label)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(size_pt)
        r1.bold = True
        r1.font.color.rgb = RGBColor(0, 0, 0)
    if value:
        r2 = p.add_run(value)
        r2.font.name = "Times New Roman"
        r2.font.size = Pt(size_pt)
        r2.bold = False
        r2.font.color.rgb = RGBColor(0, 0, 0)


def format_section_header(p, title, before_pt=3.5, after_pt=1.5, size_pt=10.5):
    """Formats a bold section heading."""
    p.text = ""
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.space_before = Pt(before_pt)
    pf.space_after = Pt(after_pt)
    pf.line_spacing = 1.05

    r = p.add_run(title)
    r.font.name = "Times New Roman"
    r.font.size = Pt(size_pt)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 0, 0)


def format_body_text(p, text, before_pt=0, after_pt=2.5, size_pt=9.5, line_spacing=1.05):
    """Formats a justified body paragraph."""
    p.text = ""
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.space_before = Pt(before_pt)
    pf.space_after = Pt(after_pt)
    pf.line_spacing = line_spacing

    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(size_pt)
    r.bold = False
    r.font.color.rgb = RGBColor(0, 0, 0)


def format_application_item(p, num_str, title_str, text_str, before_pt=0, after_pt=1.5, size_pt=9.5):
    """Formats a numbered application entry."""
    p.text = ""
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.space_before = Pt(before_pt)
    pf.space_after = Pt(after_pt)
    pf.line_spacing = 1.05

    r1 = p.add_run(f"{num_str}. {title_str}: ")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(size_pt)
    r1.bold = True
    r1.font.color.rgb = RGBColor(0, 0, 0)

    r2 = p.add_run(text_str)
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(size_pt)
    r2.bold = False
    r2.font.color.rgb = RGBColor(0, 0, 0)


def main():
    template_path = Path(r"C:\Users\bhavy\Downloads\Project One Page Report Format.docx")
    out_dl = Path(r"C:\Users\bhavy\Downloads\Project_One_Page_Report_Group_18_FraudxAI.docx")
    out_repo = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\reports\Project_One_Page_Report_Group_18_FraudxAI.docx")
    out_repo.parent.mkdir(parents=True, exist_ok=True)

    doc = docx.Document(template_path)

    # 1. Page Margins & Header Setup for Precise 1-Page Rendering
    section = doc.sections[0]
    section.top_margin = Inches(0.35)
    section.bottom_margin = Inches(0.35)
    section.left_margin = Inches(0.60)
    section.right_margin = Inches(0.60)
    section.header_distance = Inches(0.18)

    paragraphs = list(doc.paragraphs)

    # P0: empty header spacing -> remove
    p0 = paragraphs[0]
    p0._element.getparent().remove(p0._element)

    # P1: Project Group ID
    format_field(paragraphs[1], "Project Group ID: ", "18", before_pt=0, after_pt=1.2)

    # P2: Project Category
    format_field(paragraphs[2], "Project Category (Software / Hardware) Subcategory if any: ", "Software (FinTech / Applied Machine Learning / Explainable AI)", before_pt=0, after_pt=1.2)

    # P3: Title of the Project
    format_field(paragraphs[3], "Title of the Project: ", "FraudxAI: Grounded Financial Transaction Simulation & Explainable AI for Payment Fraud Detection", before_pt=0, after_pt=1.2)

    # P4: empty line -> remove
    paragraphs[4]._element.getparent().remove(paragraphs[4]._element)

    # P5: Name of the Guide
    format_field(paragraphs[5], "Name of the Guide: ", "Prof. Preeti Tiwari / Prof. Pradnya Kamble", before_pt=0, after_pt=1.2)

    # P6: Mobile Number of Guide
    format_field(paragraphs[6], "Mobile Number of Guide: ", "[To be provided]", before_pt=0, after_pt=1.2)

    # P7: Email ID of the Guide
    format_field(paragraphs[7], "Email ID of the Guide: ", "[To be provided]", before_pt=0, after_pt=1.5)

    # P8: Team Members header
    format_section_header(paragraphs[8], "Team Members:", before_pt=1.5, after_pt=1.5, size_pt=10.5)

    # Table 0: Format and populate
    table = doc.tables[0]
    set_table_borders(table)

    team_data = [
        ("Sr No", "Name of the Student", "Class", "Branch", "Mobile No.", "Email ID"),
        ("1", "Aariz Warsi", "BE IT", "Information Technology", "+91 82081 17344", "blazar11111@gmail.com"),
        ("2", "Anshul Tipnis", "BE IT", "Information Technology", "—", "—"),
        ("3", "Bhavya Shah", "BE IT", "Information Technology", "—", "bhavyashah04122005@gmail.com"),
        ("4", "Sagar Uradi", "BE IT", "Information Technology", "—", "—"),
    ]

    col_widths = [Inches(0.55), Inches(1.55), Inches(0.65), Inches(1.55), Inches(1.10), Inches(1.90)]

    for r_idx, row_values in enumerate(team_data):
        row = table.rows[r_idx]
        for c_idx, val in enumerate(row_values):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=30, bottom=30, left=50, right=50)

            cell.text = ""
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in (0, 2) else WD_ALIGN_PARAGRAPH.LEFT
            pf = p.paragraph_format
            pf.space_before = Pt(0)
            pf.space_after = Pt(0)
            pf.line_spacing = 1.0

            run = p.add_run(val)
            run.font.name = "Times New Roman"
            is_header = (r_idx == 0)
            run.font.size = Pt(9.0 if is_header else 8.5)
            run.bold = is_header
            run.font.color.rgb = RGBColor(0, 0, 0)

            if is_header:
                shd = parse_xml(r'<w:shd %s w:fill="F2F2F2"/>' % nsdecls('w'))
                cell._element.get_or_add_tcPr().append(shd)

    # P9: empty line after table -> remove
    paragraphs[9]._element.getparent().remove(paragraphs[9]._element)

    # P10: Abstract header
    format_section_header(paragraphs[10], "Abstract:", before_pt=3.0, after_pt=1.0, size_pt=10.5)

    # P11: Abstract content
    abstract_text = (
        "Payment fraud represents an existential multi-billion-dollar threat to global digital financial infrastructure. "
        "While modern gradient-boosted and deep neural architectures achieve high detection accuracy, they operate as opaque "
        "black boxes, creating severe regulatory vulnerabilities under international banking mandates that require transparent "
        "adverse-action notices and fair credit practices. Furthermore, evaluating explainability in fraud detection suffers from "
        "the 'Ground-Truth Explainability Crisis,' as real-world banking datasets lack verified counterfactual explanations. "
        "FraudxAI addresses this challenge by providing an end-to-end framework integrating: (1) a generative discrete-event banking "
        "simulation engine calibrated against empirical payment clearing rails (Federal Reserve DCPC and RBI/NPCI guidelines) with "
        "non-stationary Hawkes arrival pacing; (2) closed-loop adversarial attack agents modeling 10 empirical fraud playbooks; and "
        "(3) a mathematically rigorous Structural Causal Model (SCM) enabling exact, closed-form Shapley feature attributions and "
        "Pearlian counterfactual ground truths. Benchmarking post-hoc explainers against exact causal ground truths under realistic "
        "dual-timescale label latency establishes an auditable, high-throughput explainability platform for real-time payment switches."
    )
    format_body_text(paragraphs[11], abstract_text, before_pt=0, after_pt=2.0, size_pt=9.0, line_spacing=1.05)

    # P12 to P15: empty lines after Abstract -> remove
    for idx in range(12, 16):
        paragraphs[idx]._element.getparent().remove(paragraphs[idx]._element)

    # P16: Working of the Project header
    format_section_header(paragraphs[16], "Working of the Project: (Write 1 or 2 Paragraphs)", before_pt=2.5, after_pt=1.0, size_pt=10.5)

    # P17: Working Paragraph 1
    working_p1 = (
        "The FraudxAI architecture begins with the Generative Transaction Engine, which simulates realistic payment kinematics "
        "across dual-rail topologies (US Card-Present/CNP rails and Indian NPCI/RBI regulations). Transactions are paced using non-stationary "
        "Circadian Hawkes processes and routed through multi-party ISO 8583 banking switches. Simultaneously, closed-loop adversarial agents "
        "execute sophisticated fraud tactics (such as micro-auth card testing, distributed ATO botnets, and mule rings) that dynamically adapt "
        "upon encountering bank declines. Transactions are evaluated by an industrial ensemble inference engine (LightGBM, XGBoost, and Autoencoders) "
        "operating under strict sub-50ms latency constraints. When an anomaly is flagged, the system invokes local feature attribution algorithms "
        "alongside exact Pearlian counterfactual estimators to identify the precise invariant violations triggering the decline."
    )
    format_body_text(paragraphs[17], working_p1, before_pt=0, after_pt=1.8, size_pt=9.0, line_spacing=1.05)

    # P18: Working Paragraph 2
    working_p2 = (
        "In the supervision and operational triage layer, transactions enter an empirical Fraud Investigation Unit (FIU) queue subject to daily "
        "investigator review capacities (K_daily) and bifurcated discovery latencies (rapid 0.5 to 72 hours analyst review vs. slow 3 to 120 days customer chargeback "
        "maturity). To prevent data leakage during model retraining, a zero-leakage data partitioner decouples inference features from delayed "
        "supervision labels and threat intelligence enclaves. The interactive React analytics frontend and FastAPI microservices stream live transactions, "
        "visualize real-time risk scores with dynamic SHAP waterfall decompositions, and provide interactive force plots for compliance auditors and fraud operations analysts."
    )
    format_body_text(paragraphs[18], working_p2, before_pt=0, after_pt=2.0, size_pt=9.0, line_spacing=1.05)

    # P19 to P22: empty lines after Working -> remove
    for idx in range(19, 23):
        paragraphs[idx]._element.getparent().remove(paragraphs[idx]._element)

    # P23: Applications of the Project header
    format_section_header(paragraphs[23], "Applications of the Project:  ( Explain  in  2 Lines)", before_pt=2.5, after_pt=1.0, size_pt=10.5)

    # P24: Application 1
    format_application_item(
        paragraphs[24],
        "1",
        "Production FinTech & Banking Fraud Switches",
        "Enables real-time, sub-50ms payment fraud detection with regulatory-compliant, auditable explainability (adverse action reasons) for card issuers, payment gateways, and acquiring networks.",
        before_pt=0,
        after_pt=1.2,
        size_pt=9.0,
    )

    # Add Application 2 right after P24
    p_app2 = doc.add_paragraph()
    format_application_item(
        p_app2,
        "2",
        "Regulatory Compliance & Forensic Audit",
        "Provides quantitative benchmarking of post-hoc XAI fidelity against exact causal ground truths while training fraud analysts on realistic, multi-scenario adversarial attack topologies.",
        before_pt=0,
        after_pt=0,
        size_pt=9.0,
    )

    # Save to both target locations
    doc.save(out_dl)
    doc.save(out_repo)
    print(f"Successfully generated populated report:\n- {out_dl}\n- {out_repo}")


if __name__ == "__main__":
    main()
