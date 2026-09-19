"""
Comprehensive downloader to acquire all 116 research papers from the FraudxAI literature corpus.
- Resolves valid arXiv IDs and downloads via arXiv PDF API with SSL unverified context.
- Resolves non-arXiv papers via OpenAlex API for open-access PDF links.
- Validates %PDF- magic bytes.
- Records all acquired papers into docs/papers/manifest.json.
"""

import sys
import re
import time
import json
import ssl
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding="utf-8")

MANIFEST_PATH = Path("docs/papers/manifest.json")
PAPERS_DIR = Path("docs/papers")
REPORTS_DIR = Path("docs/research_reports")

HEADERS = {
    "User-Agent": "FraudxAI-Research-Agent/1.0 (https://github.com/Bhavyashah94/FraudxAI; mailto:research@fraudx.ai)"
}

ctx = ssl._create_unverified_context()

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
        json.dump(manifest, f, indent=2, ensure_ascii=False)

def extract_all_papers():
    arxiv_re = re.compile(r"\b(0[7-9]|1[0-9]|2[0-6])(0[1-9]|1[0-2])\.\d{4,5}(?:v\d+)?\b")
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
                    m_explicit = re.search(r"arXiv:?\s*(\d{4}\.\d{4,5}(?:v\d+)?)", full_text, re.IGNORECASE)
                    if m_explicit:
                        aid = m_explicit.group(1)
                    else:
                        m = arxiv_re.search(full_text)
                        aid = m.group(0) if m else None
                    
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
                        "stance": stance
                    })
    return papers

def download_file(url: str, dest_path: Path) -> bool:
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp, open(dest_path, "wb") as f:
            f.write(resp.read())
        
        with open(dest_path, "rb") as f:
            header = f.read(5)
            if header != b"%PDF-":
                print(f"    [WARN] Header is not PDF: {header[:15]}")
                dest_path.unlink(missing_ok=True)
                return False
        return True
    except Exception as e:
        print(f"    [ERROR] Download failed from {url}: {e}")
        dest_path.unlink(missing_ok=True)
        return False

def query_openalex_oa(title: str):
    clean_title = re.sub(r"[^\w\s]", " ", title).strip()
    query = urllib.parse.quote(clean_title[:80])
    url = f"https://api.openalex.org/works?search={query}&per-page=1&mailto=research@fraudx.ai"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("results"):
                w = data["results"][0]
                best_oa = w.get("best_oa_location") or {}
                return {
                    "work_id": w.get("id"),
                    "title": w.get("title"),
                    "pdf_url": best_oa.get("pdf_url"),
                    "landing_url": best_oa.get("landing_page_url") or w.get("doi")
                }
    except Exception as e:
        print(f"    [OPENALEX ERROR] {e}")
    return None

def main():
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    papers = extract_all_papers()
    
    print(f"=== Total Papers in Corpus: {len(papers)} ===")
    print(f"=== Already in Manifest: {len(manifest)} ===")
    
    new_downloads = 0
    
    for i, p in enumerate(papers, 1):
        title = p["title"]
        aid = p["arxiv_id"]
        stance = p["stance"]
        report = p["report"]
        
        # 1. If it has an arXiv ID
        if aid:
            safe_id = aid.replace("/", "_").strip()
            pdf_path = PAPERS_DIR / f"{safe_id}.pdf"
            
            if safe_id in manifest and pdf_path.exists() and pdf_path.stat().st_size > 5000:
                continue
                
            print(f"[{i}/{len(papers)}] [arXiv] {aid}: {title[:50]}...")
            url = f"https://arxiv.org/pdf/{aid}.pdf"
            ok = download_file(url, pdf_path)
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
                new_downloads += 1
                print(f"  -> SUCCESS ({size_kb:.1f} KB)")
            time.sleep(1.8)
            
        # 2. If it is a non-arXiv paper
        else:
            # Generate a slug id
            slug = re.sub(r"[^\w]+", "_", title.lower())[:35].strip("_")
            pdf_path = PAPERS_DIR / f"{slug}.pdf"
            
            if slug in manifest and pdf_path.exists() and pdf_path.stat().st_size > 5000:
                continue
                
            print(f"[{i}/{len(papers)}] [OpenAlex Search] {title[:50]}...")
            oa_info = query_openalex_oa(title)
            if oa_info and oa_info.get("pdf_url"):
                pdf_url = oa_info["pdf_url"]
                print(f"  -> Found Open Access PDF: {pdf_url[:70]}...")
                ok = download_file(pdf_url, pdf_path)
                if ok:
                    size_kb = pdf_path.stat().st_size / 1024
                    manifest[slug] = {
                        "openalex_id": oa_info.get("work_id"),
                        "title": title,
                        "category": report.replace(".md", ""),
                        "stance": stance,
                        "local_path": str(pdf_path.as_posix()),
                        "size_kb": round(size_kb, 1),
                        "url": pdf_url,
                        "downloaded_at": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    save_manifest(manifest)
                    new_downloads += 1
                    print(f"  -> SUCCESS ({size_kb:.1f} KB)")
            elif oa_info and oa_info.get("landing_url"):
                # Register open access landing page if direct PDF is behind landing page
                manifest[slug] = {
                    "openalex_id": oa_info.get("work_id"),
                    "title": title,
                    "category": report.replace(".md", ""),
                    "stance": stance,
                    "local_path": None,
                    "open_access_landing_url": oa_info.get("landing_url"),
                    "downloaded_at": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                save_manifest(manifest)
                print(f"  -> Registered Open Access Landing URL: {oa_info.get('landing_url')}")
            time.sleep(1.5)

    print("\n==========================================")
    print("Download Complete!")
    print(f"Total entries in manifest: {len(manifest)}")
    print(f"New downloads in this run: {new_downloads}")
    print("==========================================")

if __name__ == "__main__":
    main()
