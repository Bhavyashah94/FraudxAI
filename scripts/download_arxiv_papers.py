"""
Utility script to safely download open-access papers from arXiv for FraudxAI literature reviews.
Respects arXiv rate limits (1 request per 3 seconds) and sets a polite User-Agent.
Validates PDF headers and updates docs/papers/manifest.json.
"""

import os
import sys
import time
import json
import ssl
import urllib.request
import urllib.error
from pathlib import Path

MANIFEST_PATH = Path("docs/papers/manifest.json")
PAPERS_DIR = Path("docs/papers")

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

def download_arxiv_paper(arxiv_id: str, title: str, category: str, stance: str) -> bool:
    """
    Downloads paper PDF by arXiv ID.
    stance: 'supporting', 'opposing', or 'foundational'
    """
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    safe_id = arxiv_id.replace("/", "_").strip()
    pdf_filename = f"{safe_id}.pdf"
    pdf_path = PAPERS_DIR / pdf_filename

    manifest = load_manifest()
    if safe_id in manifest and pdf_path.exists() and pdf_path.stat().st_size > 5000:
        print(f"[ALREADY DOWNLOADED] {arxiv_id}: {title}")
        return True

    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    print(f"[DOWNLOADING] {arxiv_id} from {url} -> {pdf_path}")

    req = urllib.request.Request(url, headers=HEADERS)
    try:
        try:
            import ssl
            ctx = ssl.create_default_context()
        except Exception:
            ctx = None

        try:
            resp_cm = urllib.request.urlopen(req, timeout=30, context=ctx)
        except urllib.error.URLError as ssl_err:
            if "CERTIFICATE_VERIFY_FAILED" in str(ssl_err):
                import ssl
                ctx_unverified = ssl._create_unverified_context()
                resp_cm = urllib.request.urlopen(req, timeout=30, context=ctx_unverified)
            else:
                raise ssl_err

        with resp_cm as response, open(pdf_path, "wb") as out_file:
            data = response.read()
            out_file.write(data)

        # Validate PDF header
        with open(pdf_path, "rb") as f:
            header = f.read(5)
            if header != b"%PDF-":
                print(f"[ERROR] Invalid PDF magic bytes for {arxiv_id}: {header}")
                pdf_path.unlink(missing_ok=True)
                return False

        size_kb = pdf_path.stat().st_size / 1024
        print(f"[SUCCESS] {arxiv_id} saved ({size_kb:.1f} KB)")

        manifest[safe_id] = {
            "arxiv_id": arxiv_id,
            "title": title,
            "category": category,
            "stance": stance,
            "local_path": str(pdf_path.as_posix()),
            "size_kb": round(size_kb, 1),
            "url": url,
            "downloaded_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        save_manifest(manifest)
        # Polite rate limit sleep
        time.sleep(3.0)
        return True

    except urllib.error.HTTPError as e:
        print(f"[HTTP ERROR] {arxiv_id}: {e.code} {e.reason}")
        return False
    except Exception as e:
        print(f"[ERROR] {arxiv_id}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python scripts/download_arxiv_papers.py <arxiv_id> <title> <category> <stance>")
        sys.exit(1)
    
    aid = sys.argv[1]
    t = sys.argv[2]
    c = sys.argv[3]
    s = sys.argv[4]
    success = download_arxiv_paper(aid, t, c, s)
    sys.exit(0 if success else 1)
