import subprocess
import os

svg_path = r"C:\Users\bhavy\Downloads\FraudxAI Multi-Agent Payment Benchmark Architecture.svg"
png_path = r"C:\Users\bhavy\.gemini\antigravity\brain\bb46deb3-54dc-4cb9-a946-6206c822c9a5\diagram_original.png"

browser = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(browser):
    browser = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

print("Using browser:", browser)
cmd = [
    browser,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    f"--screenshot={png_path}",
    "--window-size=1600,1300",
    "file:///" + svg_path.replace("\\", "/")
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Returncode:", res.returncode)
print("Output file exists:", os.path.exists(png_path))
if os.path.exists(png_path):
    print("Size:", os.path.getsize(png_path))
