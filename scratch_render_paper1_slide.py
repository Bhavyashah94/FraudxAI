import subprocess
from pathlib import Path

OUTPUT_DIR = Path(r"C:\Users\bhavy\.gemini\antigravity\brain\bb46deb3-54dc-4cb9-a946-6206c822c9a5\scratch\slides")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
HTML_PATH = OUTPUT_DIR / "paper1_slide.html"
IMAGE_PATH = OUTPUT_DIR / "paper1_slide.png"

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
    display: flex;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }

  /* Left Half (Light Gray) */
  .left-half {
    width: 50%;
    height: 100%;
    background: #EEEEEE;
    padding: 90px 80px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .tag {
    font-size: 15px;
    font-weight: 700;
    color: #475569;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 24px;
  }

  .title {
    font-family: "DM Serif Text", Georgia, "Times New Roman", serif;
    font-size: 52px;
    font-weight: 700;
    color: #0F172A;
    line-height: 1.18;
    letter-spacing: -0.01em;
    margin-bottom: 36px;
  }

  .meta-grid {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-bottom: 36px;
  }
  .meta-item {
    display: flex;
    font-size: 20px;
    line-height: 1.5;
  }
  .meta-label {
    width: 180px;
    font-weight: 600;
    color: #64748B;
  }
  .meta-value {
    color: #0F172A;
    font-weight: 500;
  }
  .badge-ieee {
    background: #0284C7;
    color: #FFFFFF;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 6px;
    font-size: 16px;
    margin-left: 8px;
  }

  .summary-box {
    background: rgba(255, 255, 255, 0.7);
    border-left: 4px solid #0284C7;
    border-radius: 0 12px 12px 0;
    padding: 20px 24px;
    font-size: 18px;
    line-height: 1.6;
    color: #334155;
  }

  .footer-left {
    font-size: 14px;
    color: #94A3B8;
  }

  /* Right Half (Soft Aqua / Cyan) */
  .right-half {
    width: 50%;
    height: 100%;
    background: #9EE6EB;
    padding: 90px 80px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    color: #0F373D;
  }

  .right-header {
    font-family: "DM Serif Text", Georgia, "Times New Roman", serif;
    font-size: 38px;
    font-weight: 700;
    color: #0A292E;
    margin-bottom: 36px;
  }

  .findings-list {
    display: flex;
    flex-direction: column;
    gap: 28px;
  }

  .finding-item {
    display: flex;
    align-items: flex-start;
    gap: 18px;
  }
  .finding-icon {
    width: 32px;
    height: 32px;
    background: #0A292E;
    color: #9EE6EB;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    font-weight: 700;
    flex-shrink: 0;
    margin-top: 4px;
  }
  .finding-text {
    font-size: 21px;
    line-height: 1.5;
    color: #13444B;
  }
  .finding-text strong {
    color: #0A292E;
  }

  /* Limitation Card */
  .gap-card {
    background: rgba(10, 41, 46, 0.08);
    border: 2px dashed rgba(10, 41, 46, 0.35);
    border-radius: 16px;
    padding: 24px 28px;
    margin-top: 24px;
  }
  .gap-title {
    font-size: 18px;
    font-weight: 700;
    color: #0A292E;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .gap-desc {
    font-size: 19px;
    line-height: 1.55;
    color: #13444B;
  }

  .footer-right {
    font-size: 14px;
    color: rgba(10, 41, 46, 0.5);
    text-align: right;
  }
</style>
</head>
<body>

  <!-- Left Half: Metadata & Paper Identity -->
  <div class="left-half">
    <div>
      <div class="tag">Review of Literature &bull; Paper 01 / 04</div>
      <h1 class="title">SHAP-Based Feature Selection for Enhanced Unsupervised Labeling</h1>

      <div class="meta-grid">
        <div class="meta-item">
          <div class="meta-label">Publisher:</div>
          <div class="meta-value">IEEE Xplore <span class="badge-ieee">IEEE 2025</span></div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Publication:</div>
          <div class="meta-value">IEEE Transactions / Conference (July 2025)</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Dataset Used:</div>
          <div class="meta-value">European Credit Card Fraud (284k transactions)</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Domain:</div>
          <div class="meta-value">Financial Fraud &bull; Unsupervised XAI</div>
        </div>
      </div>

      <div class="summary-box">
        <strong>Paper Summary:</strong> Proposes an unsupervised framework using Shapley values to rank impactful fraud features without requiring manual ground-truth labels, reducing labeling overhead.
      </div>
    </div>

    <div class="footer-left">
      Department of Information Technology &bull; Atharva College of Engineering
    </div>
  </div>

  <!-- Right Half: Findings & The Core Research Gap -->
  <div class="right-half">
    <div>
      <h2 class="right-header">Key Findings &amp; Research Gap</h2>

      <div class="findings-list">
        <div class="finding-item">
          <div class="finding-icon">1</div>
          <div class="finding-text">
            <strong>Automated Feature Ranking:</strong> Successfully isolates impactful transaction dimensions in severe class imbalance without supervised guidance.
          </div>
        </div>

        <div class="finding-item">
          <div class="finding-icon">2</div>
          <div class="finding-text">
            <strong>Labeling Overhead Reduction:</strong> Demonstrates that SHAP attributions can prioritize suspicious clusters for active learning verification.
          </div>
        </div>
      </div>

      <!-- Highlighted Research Gap -->
      <div class="gap-card">
        <div class="gap-title">
          <span>&times;</span> The Research Gap (Our Motivation)
        </div>
        <div class="gap-desc">
          Evaluated entirely on <strong>PCA-masked features (V1&ndash;V28)</strong>. While SHAP yields mathematical rankings, the explanations have <strong>zero real-world semantic meaning</strong> for banking investigators or regulatory adverse action notices.
        </div>
      </div>
    </div>

    <div class="footer-right">
      FraudxAI Presentation &bull; Slide 05
    </div>
  </div>

</body>
</html>
"""

HTML_PATH.write_text(html_content, encoding="utf-8")
print(f"Wrote HTML to {HTML_PATH}")

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

print("Rendering screenshot with Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Chrome exited with code {res.returncode}")
if IMAGE_PATH.exists():
    print(f"Screenshot successfully saved: {IMAGE_PATH}")
