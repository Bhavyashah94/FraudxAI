import os
import subprocess
from pathlib import Path

OUTPUT_DIR = Path(r"C:\Users\bhavy\.gemini\antigravity\brain\bb46deb3-54dc-4cb9-a946-6206c822c9a5\scratch\slides")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
HTML_PATH = OUTPUT_DIR / "sample_slide_clean.html"
IMAGE_PATH = OUTPUT_DIR / "sample_slide_clean.png"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    width: 1920px;
    height: 1080px;
    background: #FFFFFF;
    color: #1E293B;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    overflow: hidden;
    padding: 120px 140px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* Header */
  .header {
    margin-bottom: 60px;
  }
  .category {
    font-size: 18px;
    font-weight: 600;
    color: #2563EB;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 16px;
  }
  .title {
    font-size: 54px;
    font-weight: 700;
    color: #0F172A;
    line-height: 1.15;
    letter-spacing: -0.02em;
  }

  /* Content */
  .content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 36px;
    max-width: 1500px;
  }

  .point {
    display: flex;
    align-items: flex-start;
    gap: 24px;
  }
  .bullet {
    width: 12px;
    height: 12px;
    background: #2563EB;
    border-radius: 50%;
    margin-top: 14px;
    flex-shrink: 0;
  }
  .text {
    font-size: 26px;
    line-height: 1.5;
    color: #334155;
  }
  .text strong {
    color: #0F172A;
    font-weight: 600;
  }

  /* Footer */
  .footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 30px;
    border-top: 1px solid #E2E8F0;
    font-size: 16px;
    color: #94A3B8;
  }
</style>
</head>
<body>

  <!-- Top Header -->
  <div class="header">
    <div class="category">Problem Statement</div>
    <h1 class="title">Why Explainable AI Fails on Existing Fraud Datasets</h1>
  </div>

  <!-- Bullet Points (Clean, Short, Readable) -->
  <div class="content">
    
    <div class="point">
      <div class="bullet"></div>
      <div class="text">
        <strong>Masked &amp; Anonymized Features:</strong> Real bank datasets hide transaction features behind PCA components (like V1&ndash;V28), making explanations completely uninterpretable to investigators.
      </div>
    </div>

    <div class="point">
      <div class="bullet"></div>
      <div class="text">
        <strong>No Explanation Ground Truth:</strong> Datasets only label <em>if</em> a transaction was fraudulent, never <em>why</em>. There is no benchmark to prove whether SHAP or LIME is accurate or hallucinating.
      </div>
    </div>

    <div class="point">
      <div class="bullet"></div>
      <div class="text">
        <strong>Outdated &amp; Unrealistic Simulators:</strong> Existing synthetic datasets (like PaySim) rely on 10-year-old flat tables with no card rails, no credit limits, and no modern cybercrime tactics.
      </div>
    </div>

    <div class="point">
      <div class="bullet"></div>
      <div class="text">
        <strong>Our Goal:</strong> Build a realistic payment environment where the exact cause of fraud is mathematically known, allowing us to objectively test and explain fraud detection models.
      </div>
    </div>

  </div>

  <!-- Footer -->
  <div class="footer">
    <div>FraudxAI &bull; Explainable AI for Payment Fraud</div>
    <div>03</div>
  </div>

</body>
</html>
"""

HTML_PATH.write_text(html_content, encoding="utf-8")
print(f"Wrote clean HTML to {HTML_PATH}")

# Render with Chrome Headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    f"--screenshot={IMAGE_PATH}",
    "--window-size=1920,1080",
    str(HTML_PATH.as_uri()),
]

print("Rendering clean screenshot with Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Chrome exited with code {res.returncode}")
if IMAGE_PATH.exists():
    print(f"Clean screenshot successfully saved: {IMAGE_PATH} ({IMAGE_PATH.stat().st_size} bytes)")
