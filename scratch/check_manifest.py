import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('docs/papers/manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

print('Total papers:', len(manifest))
for k, v in list(manifest.items())[:20]:
    title = v.get('title')
    year = v.get('year')
    venue = v.get('venue')
    print(f"- {k}: {title} [{year}, {venue}]")
