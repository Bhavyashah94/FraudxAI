import glob
import os
import fitz
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

pdf_files = glob.glob('docs/papers/*.pdf')
print(f"Total PDFs found: {len(pdf_files)}")

results = []
for p in pdf_files:
    fname = os.path.basename(p)
    try:
        doc = fitz.open(p)
        meta = doc.metadata or {}
        first_page = doc[0].get_text() if len(doc) > 0 else ""
        lines = [line.strip() for line in first_page.split('\n') if line.strip()]
        snippet = " // ".join(lines[:6])
        results.append({
            "filename": fname,
            "path": p,
            "pages": len(doc),
            "meta_title": meta.get("title", ""),
            "snippet": snippet
        })
    except Exception as e:
        results.append({
            "filename": fname,
            "path": p,
            "error": str(e)
        })

print(f"Processed {len(results)} PDFs.")
for r in results[:25]:
    print(f"- {r['filename']} ({r.get('pages', 0)} pp): {r.get('snippet', '')[:120]}")

with open("scratch/pdf_survey.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
print("Saved full survey to scratch/pdf_survey.json")
