import xml.etree.ElementTree as ET
import re

svg_path = r"C:\Users\bhavy\Downloads\FraudxAI Multi-Agent Payment Benchmark Architecture.svg"
tree = ET.parse(svg_path)
root = tree.getroot()

min_x, min_y, max_x, max_y = 1e9, 1e9, -1e9, -1e9

for elem in root.iter():
    # check x, y, width, height
    x = elem.attrib.get('x')
    y = elem.attrib.get('y')
    w = elem.attrib.get('width')
    h = elem.attrib.get('height')
    if x is not None and y is not None:
        try:
            fx, fy = float(x), float(y)
            fw = float(w) if w is not None else 0
            fh = float(h) if h is not None else 0
            # skip the eraser logo at the bottom
            if fy > 850:
                continue
            min_x = min(min_x, fx)
            min_y = min(min_y, fy)
            max_x = max(max_x, fx + fw)
            max_y = max(max_y, fy + fh)
        except ValueError:
            pass

print(f"Content Bounding Box (approx): x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
