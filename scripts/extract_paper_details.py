import sys
import fitz

sys.stdout.reconfigure(encoding='utf-8')

def extract_section(pdf_path, title_snippets, max_chars=2000):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening {pdf_path}: {e}")
        return
    print(f"\n==========================================")
    print(f"*** {pdf_path} (Total Pages: {len(doc)}) ***")
    print(f"==========================================")
    for page_idx, page in enumerate(doc):
        text = page.get_text()
        for snippet in title_snippets:
            if snippet.lower() in text.lower():
                print(f"\n--- Found '{snippet}' on Page {page_idx+1} ---")
                idx = text.lower().find(snippet.lower())
                start = max(0, idx - 100)
                end = min(len(text), idx + max_chars)
                print(text[start:end])
                print("-" * 40)
                break

if __name__ == "__main__":
    extract_section('docs/papers/1707.02640.pdf', ['verification latency', 'prequential', 'feedback', 'chargeback'], 2000)
    extract_section('docs/papers/2211.13358.pdf', ['Base', 'Variant I', 'delayed feedback', 'drift'], 2000)
    extract_section('docs/papers/2002.06673.pdf', ['Definition 2.1', 'Definition 2.2', 'repeated risk minimization', 'performatively stable'], 2000)
    extract_section('docs/papers/1506.06980.pdf', ['Stackelberg', 'Definition 1', 'cost function', 'empirical risk'], 2000)
    extract_section('docs/papers/2101.08030.pdf', ['non-editable', 'imperceptible', 'problem formulation'], 2000)
    extract_section('docs/papers/1910.10362.pdf', ['causal model', 'Definition 3', 'gaming', 'Theorem 4.1'], 2000)
