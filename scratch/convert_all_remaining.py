import os
import re
import json
import pymupdf
import pymupdf4llm
import sys

sys.stdout.reconfigure(encoding='utf-8')

PAPERS_DIR = "docs/papers"
MANIFEST_PATH = os.path.join(PAPERS_DIR, "manifest.json")

manifest = {}
if os.path.exists(MANIFEST_PATH):
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

def clean_slug_component(text, max_len=40):
    text = re.sub(r'[^a-zA-Z0-9\s_]', '', text)
    text = re.sub(r'\s+', '_', text.strip().lower())
    text = re.sub(r'_+', '_', text)
    return text[:max_len].rstrip('_')

numeric_pdfs = [f for f in os.listdir(PAPERS_DIR) if re.match(r'^\d{4}\.\d{4,5}\.pdf$', f)]
print(f"Found {len(numeric_pdfs)} numeric arXiv PDFs to process.")

processed_records = []

for idx, fname in enumerate(numeric_pdfs, 1):
    arxiv_id = fname.replace('.pdf', '')
    pdf_path = os.path.join(PAPERS_DIR, fname)
    
    # 1. Year from arXiv ID
    m = re.match(r'^(\d{2})(\d{2})\.', arxiv_id)
    if m:
        yy = int(m.group(1))
        year = 2000 + yy if yy <= 30 else 1900 + yy
    else:
        year = 2024

    # 2. Metadata from manifest or PDF
    m_info = manifest.get(arxiv_id, {})
    title = m_info.get("title", "")
    
    doc = None
    try:
        doc = pymupdf.open(pdf_path)
    except Exception as e:
        print(f"[{idx}/{len(numeric_pdfs)}] Error opening {fname}: {e}")
        continue

    first_page_text = doc[0].get_text() if len(doc) > 0 else ""
    lines = [l.strip() for l in first_page_text.split('\n') if l.strip()]

    if not title or len(title) < 5:
        # doc metadata title
        doc_title = (doc.metadata or {}).get("title", "")
        if doc_title and len(doc_title) > 6 and not doc_title.lower().endswith(".pdf") and "untitled" not in doc_title.lower():
            title = doc_title
        else:
            for l in lines[:6]:
                if any(s in l.lower() for s in ["arxiv:", "proceedings", "conference", "journal", "volume", "accepted", "received"]):
                    continue
                if len(l) > 10 and not l.startswith("©"):
                    title = l
                    break
    
    if not title:
        title = f"Paper {arxiv_id}"

    # 3. Extract Author
    author = "unknown"
    doc_author = (doc.metadata or {}).get("author", "")
    if doc_author and len(doc_author) > 2 and len(doc_author) < 40 and not any(c in doc_author for c in [":", "/", "\\", "@"]):
        first_a = doc_author.split(",")[0].split(";")[0].strip()
        tokens = first_a.split()
        if tokens:
            author = tokens[-1].lower()

    if author == "unknown":
        found_title = False
        for l in lines[:15]:
            if title[:15].lower() in l.lower():
                found_title = True
                continue
            if found_title and len(l) > 2 and len(l) < 50:
                if any(s in l.lower() for s in ["abstract", "university", "department", "school", "email", "@"]):
                    continue
                cleaned = re.sub(r'[*†‡§1-9]', '', l)
                first_name_token = cleaned.split(",")[0].split("and")[0].strip()
                toks = first_name_token.split()
                if toks:
                    author = toks[-1].lower()
                    break

    # Clean components
    author_slug = clean_slug_component(author, max_len=15)
    title_slug = clean_slug_component(title, max_len=35)
    clean_slug = f"{year}_{author_slug}_{title_slug}".strip('_')

    target_pdf = os.path.join(PAPERS_DIR, clean_slug + ".pdf")
    target_md = os.path.join(PAPERS_DIR, clean_slug + ".md")

    print(f"[{idx}/{len(numeric_pdfs)}] {fname} -> {clean_slug}")

    # Copy / rename PDF
    try:
        if not os.path.exists(target_pdf):
            doc.close()
            # Rename or copy
            os.rename(pdf_path, target_pdf)
        else:
            doc.close()
    except Exception as e:
        print(f"  Error renaming PDF {fname}: {e}")

    # Convert to Markdown
    try:
        md_text = pymupdf4llm.to_markdown(target_pdf)
        frontmatter = f"""---
title: "{title}"
authors: "{author}"
year: {year}
arxiv_id: "{arxiv_id}"
original_file: "{fname}"
pdf_path: "{target_pdf}"
---

# {title}

**Authors:** {author.title()} et al.  
**Year:** {year} | **arXiv:** [`{arxiv_id}`](https://arxiv.org/abs/{arxiv_id})  
**Local PDF:** [`{clean_slug}.pdf`](file:///{os.path.abspath(target_pdf).replace(chr(92), '/')})

---

"""
        with open(target_md, "w", encoding="utf-8") as out_f:
            out_f.write(frontmatter + md_text)
    except Exception as e:
        print(f"  Error converting markdown for {clean_slug}: {e}")

    processed_records.append({
        "arxiv_id": arxiv_id,
        "clean_slug": clean_slug,
        "title": title,
        "author": author,
        "year": year,
        "pdf_file": clean_slug + ".pdf",
        "md_file": clean_slug + ".md"
    })

# Save new mapping
with open(os.path.join(PAPERS_DIR, "papers_registry.json"), "w", encoding="utf-8") as reg_f:
    json.dump(processed_records, reg_f, indent=2)

print(f"\nAll {len(processed_records)} papers converted and registered successfully!")
