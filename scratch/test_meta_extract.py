import os
import re
import fitz
import pymupdf4llm
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

def extract_meta_from_text(first_page_text, meta):
    # Try to find title, authors, year
    lines = [l.strip() for l in first_page_text.split('\n') if l.strip()]
    
    # Heuristics for title:
    title = meta.get("title", "")
    if not title or len(title) < 5 or title.lower().endswith(".pdf") or "untitled" in title.lower():
        # Look for the first prominent line that isn't a conference header or arxiv badge
        for line in lines[:8]:
            if any(skip in line.lower() for skip in ["arxiv:", "http", "vol.", "issue", "proceedings of", "received", "accepted"]):
                continue
            if len(line) > 10 and not line.startswith("©"):
                title = line
                break
    
    # Year heuristic
    year = None
    # Check text for 201X or 202X
    year_matches = re.findall(r'\b(20[12][0-9])\b', first_page_text[:1500])
    if year_matches:
        # Pick the most frequent or latest plausible year
        year = sorted(year_matches)[-1]
    else:
        year = "2024"
        
    return title, year

# Test on 10 random papers
for fname in os.listdir("docs/papers")[:10]:
    if not fname.endswith(".pdf"): continue
    path = os.path.join("docs/papers", fname)
    doc = fitz.open(path)
    meta = doc.metadata or {}
    first_page = doc[0].get_text() if len(doc) > 0 else ""
    title, year = extract_meta_from_text(first_page, meta)
    print(f"Original: {fname}")
    print(f"  Year: {year} | Title: {title[:70]}")
