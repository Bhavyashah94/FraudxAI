"""Generates the verified, exact 1-page Project One Page Report for FraudxAI (Group 18)
preserving 100% of the Atharva College of Engineering template format.
"""

from pathlib import Path
import shutil
import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import fitz
import win32com.client


def generate_report():
    template_path = Path(r"C:\Users\bhavy\Downloads\Project One Page Report Format.docx")
    out_docx_dl = Path(r"C:\Users\bhavy\Downloads\Project_One_Page_Report_Atharva_Group_18.docx")
    out_pdf_dl = Path(r"C:\Users\bhavy\Downloads\Project_One_Page_Report_Atharva_Group_18.pdf")
    
    out_docx_repo = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\reports\Project_One_Page_Report_Atharva_Group_18.docx")
    out_pdf_repo = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\reports\Project_One_Page_Report_Atharva_Group_18.pdf")
    out_docx_repo.parent.mkdir(parents=True, exist_ok=True)

    # Work on a clean copy of the official template
    shutil.copyfile(template_path, out_docx_dl)
    doc = docx.Document(out_docx_dl)

    def set_run(r, text, font_name="Times New Roman", size_pt=12, bold=False):
        r.text = text
        r.font.name = font_name
        r.font.size = Pt(size_pt)
        r.bold = bold

    # P1: Project Group ID:
    doc.paragraphs[1].runs[0].text = "Project Group ID: "
    r = doc.paragraphs[1].add_run("18")
    set_run(r, "18", size_pt=12, bold=False)

    # P2: Project Category
    doc.paragraphs[2].runs[0].text = "Project Category (Software / Hardware) Subcategory if any: "
    r = doc.paragraphs[2].add_run("Software")
    set_run(r, "Software", size_pt=12, bold=False)

    # P3: Title of the Project:
    doc.paragraphs[3].runs[0].text = "Title of the Project: "
    r = doc.paragraphs[3].add_run("FraudxAI: Explainable AI for Payment Fraud Detection")
    set_run(r, "FraudxAI: Explainable AI for Payment Fraud Detection", size_pt=12, bold=False)

    # Remove P4 (empty line between Title and Guide)
    doc.paragraphs[4]._element.getparent().remove(doc.paragraphs[4]._element)

    # Name of the Guide:
    guide_idx = [i for i, p in enumerate(doc.paragraphs) if "Name of the Guide" in p.text][0]
    p_guide = doc.paragraphs[guide_idx]
    p_guide.text = ""
    r_label = p_guide.add_run("Name of the Guide: ")
    set_run(r_label, "Name of the Guide: ", size_pt=12, bold=True)
    r_val = p_guide.add_run("Prof. Preeti Tiwari / Prof. Pradnya Kamble")
    set_run(r_val, "Prof. Preeti Tiwari / Prof. Pradnya Kamble", size_pt=12, bold=False)

    # Mobile Number of Guide:
    p_mob = doc.paragraphs[guide_idx + 1]
    p_mob.text = ""
    r_label = p_mob.add_run("Mobile Number of Guide: ")
    set_run(r_label, "Mobile Number of Guide: ", size_pt=12, bold=True)
    r_val = p_mob.add_run("[To be provided]")
    set_run(r_val, "[To be provided]", size_pt=12, bold=False)

    # Email ID of the Guide:
    p_email = doc.paragraphs[guide_idx + 2]
    p_email.text = ""
    r_label = p_email.add_run("Email ID of the Guide: ")
    set_run(r_label, "Email ID of the Guide: ", size_pt=12, bold=True)
    r_val = p_email.add_run("[To be provided]")
    set_run(r_val, "[To be provided]", size_pt=12, bold=False)

    # Table 0: Populate student rows
    t = doc.tables[0]
    students = [
        ("Aariz Warsi", "BE IT", "IT", "8208117344", "blazar11111@gmail.com"),
        ("Anshul Tipnis", "BE IT", "IT", "—", "—"),
        ("Bhavya Shah", "BE IT", "IT", "—", "bhavyashah04122005@gmail.com"),
        ("Sagar Uradi", "BE IT", "IT", "—", "—"),
    ]

    for row_i, stud in enumerate(students, start=1):
        row = t.rows[row_i]
        for col_i, val in enumerate(stud, start=1):
            cell = row.cells[col_i]
            cell.text = ""
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_i in (2, 3) else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            set_run(r, val, size_pt=10, bold=False)

    # Remove empty paragraph between Table and Abstract
    abs_idx = [i for i, p in enumerate(doc.paragraphs) if "Abstract" in p.text][0]
    p_before_abs = doc.paragraphs[abs_idx - 1]
    if p_before_abs.text.strip() == "":
        p_before_abs._element.getparent().remove(p_before_abs._element)

    # Abstract text
    abs_idx = [i for i, p in enumerate(doc.paragraphs) if "Abstract" in p.text][0]
    p_abs = doc.paragraphs[abs_idx + 1]
    p_abs.text = ""
    p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    abs_text = (
        "Payment fraud poses a severe multi-billion-dollar threat to global digital financial infrastructure. While modern "
        "machine learning architectures achieve high detection accuracy, they operate as opaque black boxes, violating "
        "regulatory mandates that require explainable adverse actions. Furthermore, evaluating explainability in fraud detection "
        "is constrained by the absence of verified ground-truth explanations in banking data. FraudxAI resolves this by integrating "
        "a generative discrete-event simulation engine calibrated to empirical payment rails (Federal Reserve and RBI/NPCI), "
        "closed-loop adversarial attack agents, and a Structural Causal Model enabling exact, closed-form Shapley and counterfactual ground truths."
    )
    r_abs = p_abs.add_run(abs_text)
    set_run(r_abs, abs_text, size_pt=10.5, bold=False)

    # Remove empty placeholder paragraphs between Abstract and Working of the Project
    work_idx = [i for i, p in enumerate(doc.paragraphs) if "Working of the Project" in p.text][0]
    for idx in range(work_idx - 1, abs_idx + 1, -1):
        p_del = doc.paragraphs[idx]
        p_del._element.getparent().remove(p_del._element)

    # Working of the Project text
    work_idx = [i for i, p in enumerate(doc.paragraphs) if "Working of the Project" in p.text][0]
    p_work = doc.paragraphs[work_idx + 1]
    p_work.text = ""
    p_work.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    w_text = (
        "The system simulates realistic payment kinematics across dual-rail topologies (US and Indian rails) using non-stationary "
        "Circadian Hawkes point processes. Concurrently, closed-loop adversarial agents execute fraud tactics (micro-auth probes, "
        "botnets, and mule rings) that dynamically adapt to bank authorization declines. Transactions are evaluated by an industrial "
        "ensemble inference engine (LightGBM, XGBoost, Autoencoder) under sub-50ms latency constraints, triggering local feature attributions "
        "alongside exact Pearlian counterfactual estimators when fraud is flagged. In the operational layer, transactions enter an empirical "
        "Fraud Investigation Unit queue subject to daily analyst review budgets and bifurcated feedback latencies (rapid analyst audits vs. delayed chargebacks). "
        "A zero-leakage partitioner isolates inference features from supervision metadata to ensure unbiased retraining, while a real-time React dashboard "
        "provides live feeds, risk telemetry, and interactive SHAP waterfall visual explanations."
    )
    r_w = p_work.add_run(w_text)
    set_run(r_w, w_text, size_pt=10.0, bold=False)

    # Remove empty placeholder paragraphs between Working and Applications
    app_idx = [i for i, p in enumerate(doc.paragraphs) if "Applications of the Project" in p.text][0]
    for idx in range(app_idx - 1, work_idx + 1, -1):
        p_del = doc.paragraphs[idx]
        p_del._element.getparent().remove(p_del._element)

    # Applications of the Project
    app_idx = [i for i, p in enumerate(doc.paragraphs) if "Applications of the Project" in p.text][0]
    p_app1 = doc.paragraphs[app_idx + 1]
    p_app1.text = ""
    p_app1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_app1 = p_app1.add_run("1. Real-Time Banking Fraud Switches: Sub-50ms explainable transaction scoring with auditable adverse-action reasons for card issuers and gateways.")
    set_run(r_app1, r_app1.text, size_pt=10.0, bold=False)

    if app_idx + 2 < len(doc.paragraphs):
        p_app2 = doc.paragraphs[app_idx + 2]
        p_app2.text = ""
    else:
        p_app2 = doc.add_paragraph()
    p_app2.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_app2 = p_app2.add_run("2. Regulatory Compliance & Forensic Auditing: Quantitative benchmarking of post-hoc XAI explainers against exact causal ground truths.")
    set_run(r_app2, r_app2.text, size_pt=10.0, bold=False)

    # Remove any extra trailing paragraphs
    while len(doc.paragraphs) > app_idx + 3:
        p_extra = doc.paragraphs[-1]
        p_extra._element.getparent().remove(p_extra._element)

    # Save docx to Downloads and Repo
    doc.save(out_docx_dl)
    doc.save(out_docx_repo)
    print(f"Saved DOCX:\n  {out_docx_dl}\n  {out_docx_repo}")

    # Export PDF via Word
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        w_doc = word.Documents.Open(str(out_docx_dl.resolve()), ReadOnly=True)
        w_doc.SaveAs(str(out_pdf_dl.resolve()), FileFormat=17)
        w_doc.Close(False)
    finally:
        word.Quit()

    shutil.copyfile(out_pdf_dl, out_pdf_repo)
    print(f"Saved PDF:\n  {out_pdf_dl}\n  {out_pdf_repo}")

    # Verify Page Count
    doc_pdf = fitz.open(out_pdf_dl)
    print(f"VERIFIED PDF PAGE COUNT: {len(doc_pdf)} PAGE(S)")
    assert len(doc_pdf) == 1, f"Expected exactly 1 page, got {len(doc_pdf)}"


if __name__ == "__main__":
    generate_report()
