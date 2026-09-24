import os
import re
import pymupdf
import pymupdf4llm
import sys

sys.stdout.reconfigure(encoding='utf-8')

PAPERS_DIR = "docs/papers"

# Redundant files that already have slugged versions
redundant = [
    "walauskis_khoshgoftaar_ieee_access_2025.pdf",
    "fazel_2026_credit_card_fraud_explainable_ebm.pdf",
    "wu_2026_credit_card_fraud_temporal_shap_audit.pdf",
    "dal_pozzolo_2015_adaptive_machine_learning_credit_card_fraud.pdf",
    "raufi_et_al_springer_2024.pdf" # This was a 5kb cloudflare HTML page
]

for r in redundant:
    p = os.path.join(PAPERS_DIR, r)
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed redundant/temporary file: {r}")

# Files to convert
files_to_convert = [f for f in os.listdir(PAPERS_DIR) if f.endswith('.pdf') and not os.path.exists(os.path.join(PAPERS_DIR, f.replace('.pdf', '.md')))]

print(f"Converting remaining {len(files_to_convert)} files...")

for f in files_to_convert:
    pdf_path = os.path.join(PAPERS_DIR, f)
    try:
        doc = pymupdf.open(pdf_path)
        first_page = doc[0].get_text() if len(doc) > 0 else ""
        lines = [l.strip() for l in first_page.split('\n') if l.strip()]
        
        # Heuristic title
        title = (doc.metadata or {}).get("title", "")
        if not title or len(title) < 5 or title.lower().endswith(".pdf"):
            for l in lines[:6]:
                if len(l) > 10 and not any(s in l.lower() for s in ["arxiv:", "http", "vol.", "proceedings", "accepted"]):
                    title = l
                    break
        if not title:
            title = f.replace('.pdf', '').replace('_', ' ').title()
        
        # Year
        year_matches = re.findall(r'\b(20[12][0-9])\b', first_page[:2000])
        year = sorted(year_matches)[-1] if year_matches else "2020"
        
        # Clean slug
        clean_name = f.replace('.pdf', '')
        if not clean_name.startswith(('201', '202')):
            clean_name = f"{year}_{clean_name}"
        
        clean_pdf = os.path.join(PAPERS_DIR, clean_name + ".pdf")
        clean_md = os.path.join(PAPERS_DIR, clean_name + ".md")
        
        doc.close()
        if pdf_path != clean_pdf:
            os.rename(pdf_path, clean_pdf)
            
        md_text = pymupdf4llm.to_markdown(clean_pdf)
        frontmatter = f"""---
title: "{title}"
year: {year}
original_file: "{f}"
pdf_path: "{clean_pdf}"
---

# {title}

**Year:** {year}  
**Local PDF:** [`{clean_name}.pdf`](file:///{os.path.abspath(clean_pdf).replace(chr(92), '/')})

---

"""
        with open(clean_md, "w", encoding="utf-8") as out_f:
            out_f.write(frontmatter + md_text)
        print(f"  -> Converted {clean_name} ({len(md_text)} chars)")
    except Exception as e:
        print(f"  -> Error with {f}: {e}")

print("Final batch completed.")
