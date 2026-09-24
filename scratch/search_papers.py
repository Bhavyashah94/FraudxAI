import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('docs/papers/manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

for k, v in manifest.items():
    title = str(v.get('title', ''))
    abstract = str(v.get('abstract', ''))
    if any(term in title.lower() for term in ['fraud', 'shap', 'credit', 'explain', 'gnn', 'tabular']):
        print(f"[{k}] {title}")
