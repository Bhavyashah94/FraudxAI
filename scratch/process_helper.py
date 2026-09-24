import os
import re
import json
import shutil
import pymupdf
import pymupdf4llm
import sys

sys.stdout.reconfigure(encoding='utf-8')

PAPERS_DIR = "docs/papers"
MANIFEST_PATH = os.path.join(PAPERS_DIR, "manifest.json")

# Load existing manifest if present
manifest = {}
if os.path.exists(MANIFEST_PATH):
    try:
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        print("Error reading manifest:", e)

def sanitize_slug(text, max_len=45):
    text = re.sub(r'[^a-zA-Z0-9\s_]', '', text)
    text = re.sub(r'\s+', '_', text.strip().lower())
    text = re.sub(r'_+', '_', text)
    return text[:max_len].rstrip('_')

def get_year_from_arxiv(fname):
    m = re.match(r'^(\d{2})(\d{2})\.', fname)
    if m:
        yy = int(m.group(1))
        # arXiv IDs before 07 started with subject-class, after 2007 they start with YYMM
        if 7 <= yy <= 26:
            return 2000 + yy
    return None

def extract_author_and_title(doc, fname):
    first_page = doc[0].get_text() if len(doc) > 0 else ""
    lines = [l.strip() for l in first_page.split('\n') if l.strip()]
    
    # Check if in manifest
    base_no_ext = fname.replace('.pdf', '')
    meta_title = ""
    if base_no_ext in manifest and 'title' in manifest[base_no_ext]:
        meta_title = manifest[base_no_ext]['title']
    
    # Fallback to doc metadata
    if not meta_title:
        doc_title = (doc.metadata or {}).get("title", "")
        if doc_title and len(doc_title) > 6 and not doc_title.lower().endswith(".pdf") and "untitled" not in doc_title.lower():
            meta_title = doc_title

    # Fallback to text parsing
    if not meta_title:
        for line in lines[:8]:
            if any(skip in line.lower() for skip in ["arxiv:", "http", "vol.", "issue", "proceedings of", "received", "accepted", "issn", "doi"]):
                continue
            if len(line) > 10 and not line.startswith("©"):
                meta_title = line
                break
    
    if not meta_title:
        meta_title = base_no_ext

    # Extract author heuristic
    author = "unknown"
    doc_author = (doc.metadata or {}).get("author", "")
    if doc_author and len(doc_author) > 2 and len(doc_author) < 40 and not any(c in doc_author for c in [":", "/", "\\", "@"]):
        # pick last name of first author
        first_a = doc_author.split(",")[0].split(";")[0].strip()
        parts = first_a.split()
        if parts:
            author = parts[-1].lower()
    
    if author == "unknown":
        # Search lines after title for author names
        found_title = False
        for line in lines[:15]:
            if meta_title and meta_title[:20].lower() in line.lower():
                found_title = True
                continue
            if found_title and len(line) > 2 and len(line) < 60:
                if any(skip in line.lower() for skip in ["abstract", "university", "department", "school", "institute", "email", "@", "college"]):
                    continue
                # Potential author line
                cleaned_line = re.sub(r'[*†‡§1-9]', '', line)
                first_name_match = cleaned_line.split(",")[0].split("and")[0].strip()
                tokens = first_name_match.split()
                if tokens:
                    author = tokens[-1].lower()
                    break

    # Year
    year = get_year_from_arxiv(fname)
    if not year:
        year_matches = re.findall(r'\b(20[12][0-9])\b', first_page[:2000])
        if year_matches:
            year = int(sorted(year_matches)[-1])
        else:
            year = 2024

    return meta_title, author, year

print("Script template ready.")
