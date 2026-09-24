import re

svg_path = r"C:\Users\bhavy\Downloads\FraudxAI Multi-Agent Payment Benchmark Architecture.svg"
with open(svg_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

print("Length:", len(content))
print("Text tags:", len(re.findall(r"<text\b", content)))
print("Path tags:", len(re.findall(r"<path\b", content)))
print("Rect tags:", len(re.findall(r"<rect\b", content)))
vb = re.search(r'viewBox="([^"]*)"', content)
print("ViewBox:", vb.group(1) if vb else "None")

# Find texts with positions and styles
texts = re.findall(r'<text[^>]*>([^<]*)</text>', content)
print(f"Total extracted text nodes: {len(texts)}")
for t in texts[:30]:
    if t.strip():
        print("  -", t.strip()[:60])
