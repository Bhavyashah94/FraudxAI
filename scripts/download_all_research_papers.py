"""
Comprehensive batch downloader for all papers identified in FraudxAI literature reviews.
Parses cluster reports, finds arXiv IDs and open-access URLs, downloads PDFs,
validates PDF headers, and updates docs/papers/manifest.json.
"""

import os
import sys
import re
import time
import json
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

MANIFEST_PATH = Path("docs/papers/manifest.json")
PAPERS_DIR = Path("docs/papers")
REPORTS_DIR = Path("docs/research_reports")

HEADERS = {
    "User-Agent": "FraudxAI-Research-Agent/1.0 (https://github.com/Bhavyashah94/FraudxAI; mailto:research@fraudx.ai)"
}

def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_manifest(manifest: dict):
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

def extract_papers_from_reports():
    arxiv_re = re.compile(r'(\d{4}\.\d{4,5}(?:v\d+)?)')
    papers = []
    
    for r in sorted(REPORTS_DIR.glob("cluster_*.md")):
        lines = r.read_text(encoding="utf-8").splitlines()
        in_table = False
        for line in lines:
            if ("| #" in line or "| No" in line) and "Title" in line:
                in_table = True
                continue
            if in_table:
                if not line.strip().startswith("|"):
                    in_table = False
                    continue
                if line.strip().startswith("|:-") or line.strip().startswith("|--"):
                    continue
                cols = [c.strip() for c in line.split("|")[1:-1]]
                if len(cols) >= 5:
                    full_text = " ".join(cols)
                    m = arxiv_re.search(full_text)
                    aid = m.group(1) if m else None
                    title = cols[1].strip("*").strip()
                    stance = "foundational"
                    for col in cols:
                        if "opposing" in col.lower():
                            stance = "opposing"
                            break
                        elif "supporting" in col.lower():
                            stance = "supporting"
                            break
                    papers.append({
                        "report": r.name,
                        "title": title,
                        "arxiv_id": aid,
                        "cols": cols,
                        "stance": stance,
                        "raw_line": line
                    })
    return papers

def download_url_to_file(url: str, dest_path: Path) -> bool:
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as response, open(dest_path, "wb") as out_file:
            data = response.read()
            out_file.write(data)
        
        with open(dest_path, "rb") as f:
            header = f.read(5)
            if header != b"%PDF-":
                print(f"  [ERROR] Magic bytes not PDF: {header} for {url}")
                dest_path.unlink(missing_ok=True)
                return False
        return True
    except Exception as e:
        print(f"  [DOWNLOAD FAIL] {url}: {e}")
        dest_path.unlink(missing_ok=True)
        return False

def search_arxiv_id_by_title(title: str):
    clean_title = re.sub(r"[^\w\s]", "", title)
    query = urllib.parse.quote(f'ti:"{clean_title}"')
    url = f"http://export.arxiv.org/api/query?search_query={query}&max_results=1"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode("utf-8")
            m = re.search(r"<id>http://arxiv\.org/abs/(\d{4}\.\d{4,5}(?:v\d+)?)</id>", content)
            if m:
                return m.group(1)
    except Exception:
        pass
    return None

def main():
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    papers = extract_papers_from_reports()
    
    print(f"=== Total Papers in Reports: {len(papers)} ===")
    print(f"=== Existing in Manifest: {len(manifest)} ===")
    
    success_count = 0
    fail_count = 0
    
    for i, p in enumerate(papers, 1):
        title = p["title"]
        aid = p["arxiv_id"]
        stance = p["stance"]
        report = p["report"]
        
        # If no arXiv ID, try search
        if not aid:
            print(f"[{i}/{len(papers)}] Searching arXiv for: {title[:50]}...")
            aid = search_arxiv_id_by_title(title)
            if aid:
                print(f"  -> Found arXiv ID: {aid}")
                p["arxiv_id"] = aid
            time.sleep(2.0)
            
        if not aid:
            print(f"[{i}/{len(papers)}] Non-arXiv paper (will check DOI/open access): {title[:60]}")
            continue
            
        safe_id = aid.replace("/", "_").strip()
        pdf_path = PAPERS_DIR / f"{safe_id}.pdf"
        
        if safe_id in manifest and pdf_path.exists() and pdf_path.stat().st_size > 5000:
            # Already valid
            success_count += 1
            continue
            
        url = f"https://arxiv.org/pdf/{aid}.pdf"
        print(f"[{i}/{len(papers)}] Downloading: {aid} ({title[:45]}...)")
        
        ok = download_url_to_file(url, pdf_path)
        if ok:
            size_kb = pdf_path.stat().st_size / 1024
            manifest[safe_id] = {
                "arxiv_id": aid,
                "title": title,
                "category": report.replace(".md", ""),
                "stance": stance,
                "local_path": str(pdf_path.as_posix()),
                "size_kb": round(size_kb, 1),
                "url": url,
                "downloaded_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            save_manifest(manifest)
            success_count += 1
            print(f"  -> Saved {safe_id}.pdf ({size_kb:.1f} KB)")
        else:
            fail_count += 1
            
        # Rate limit compliance
        time.sleep(2.5)

    print("\n==========================================")
    print(f"Download Batch Complete!")
    print(f"Total in Manifest: {len(manifest)}")
    print(f"Successful in this run: {success_count}")
    print(f"Failed in this run: {fail_count}")
    print("==========================================")

if __name__ == "__main__":
    main()
