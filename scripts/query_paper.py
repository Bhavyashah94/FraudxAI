import sys
import fitz

sys.stdout.reconfigure(encoding='utf-8')

def inspect_paper(pdf_path, queries):
    doc = fitz.open(pdf_path)
    print(f"\n==========================================")
    print(f"*** {pdf_path} (Pages: {len(doc)}) ***")
    print(f"==========================================")
    for q in queries:
        found_count = 0
        for p_idx, page in enumerate(doc):
            text = page.get_text()
            if q.lower() in text.lower():
                found_count += 1
                if found_count <= 2:
                    print(f"\n--- Query '{q}' found on Page {p_idx+1} ---")
                    idx = text.lower().find(q.lower())
                    start = max(0, idx - 80)
                    end = min(len(text), idx + 1200)
                    print(text[start:end])
                    print("." * 40)

if __name__ == "__main__":
    paper = sys.argv[1]
    queries = sys.argv[2:]
    inspect_paper(paper, queries)
