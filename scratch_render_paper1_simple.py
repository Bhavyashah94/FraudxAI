import subprocess
from pathlib import Path

OUTPUT_DIR = Path(r"C:\Users\bhavy\.gemini\antigravity\brain\bb46deb3-54dc-4cb9-a946-6206c822c9a5\scratch\slides")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
HTML_PATH = OUTPUT_DIR / "paper1_slide_simple.html"
IMAGE_PATH = OUTPUT_DIR / "paper1_slide_simple.png"

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
    background: #EFEFEF;
    padding: 90px 80px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .tag {
    font-size: 16px;
    font-weight: 700;
    color: #475569;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 20px;
  }

  .title {
    font-family: "DM Serif Text", Georgia, "Times New Roman", serif;
    font-size: 48px;
    font-weight: 700;
    color: #0F172A;
    line-height: 1.2;
    margin-bottom: 12px;
  }
  .citation {
    font-size: 20px;
    color: #2563EB;
    font-weight: 600;
    margin-bottom: 36px;
  }

  .section-block {
    margin-bottom: 28px;
  }
  .section-title {
    font-size: 22px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 10px;
  }
  .section-text {
    font-size: 21px;
    line-height: 1.55;
    color: #334155;
  }

  .steps-box {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 24px 28px;
    border: 1px solid #CBD5E1;
  }
  .step-item {
    font-size: 20px;
    line-height: 1.5;
    color: #334155;
    margin-bottom: 12px;
    display: flex;
    gap: 12px;
  }
  .step-item:last-child {
    margin-bottom: 0;
  }
  .step-num {
    font-weight: 700;
    color: #2563EB;
  }

  .footer-left {
    font-size: 15px;
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
    font-size: 42px;
    font-weight: 700;
    color: #0A292E;
    margin-bottom: 36px;
  }

  .points-container {
    display: flex;
    flex-direction: column;
    gap: 28px;
  }

  .point-card {
    background: rgba(255, 255, 255, 0.45);
    border-radius: 14px;
    padding: 22px 26px;
  }
  .point-card-title {
    font-size: 22px;
    font-weight: 700;
    color: #0A292E;
    margin-bottom: 8px;
  }
  .point-card-text {
    font-size: 20px;
    line-height: 1.5;
    color: #13444B;
  }

  /* Big Problem Box */
  .problem-card {
    background: #0A292E;
    color: #FFFFFF;
    border-radius: 16px;
    padding: 26px 28px;
  }
  .problem-tag {
    font-size: 15px;
    font-weight: 700;
    color: #38BDF8;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }
  .problem-title {
    font-size: 23px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 10px;
  }
  .problem-text {
    font-size: 19px;
    line-height: 1.55;
    color: #E2E8F0;
  }
  .problem-text strong {
    color: #38BDF8;
  }

  .footer-right {
    font-size: 15px;
    color: rgba(10, 41, 46, 0.6);
    text-align: right;
  }
</style>
</head>
<body>

  <!-- Left Side: Simple Goal & Steps -->
  <div class="left-half">
    <div>
      <div class="tag">Literature Review &bull; Paper 01</div>
      <h1 class="title">Can We Explain Fraud Detection Using SHAP?</h1>
      <div class="citation">IEEE / Springer Research (2025)</div>

      <div class="section-block">
        <div class="section-title">The Basic Goal</div>
        <div class="section-text">
          Banks use complex AI models to catch fraud, but these models are complete black boxes. This research tested if <strong>SHAP</strong> (a popular explainability tool) can reliably show <em>why</em> a transaction was blocked.
        </div>
      </div>

      <div class="section-block">
        <div class="section-title">What They Did</div>
        <div class="steps-box">
          <div class="step-item">
            <span class="step-num">1.</span>
            <span>Trained machine learning models on real-world credit card transaction logs.</span>
          </div>
          <div class="step-item">
            <span class="step-num">2.</span>
            <span>Used SHAP to calculate which features (Amount, Time, Location) triggered each fraud alert.</span>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-left">
      Atharva College of Engineering &bull; Department of Information Technology
    </div>
  </div>

  <!-- Right Side: Plain Findings & The Problem -->
  <div class="right-half">
    <div>
      <h2 class="right-header">What Worked &amp; Where It Failed</h2>

      <div class="points-container">
        
        <div class="point-card">
          <div class="point-card-title">1. Good on Big Trends, Confused on Individuals</div>
          <div class="point-card-text">
            SHAP accurately identified that <em>"Transaction Amount"</em> is generally risky. But for individual cardholders, it gets confused when features are related (like high spending during overseas travel).
          </div>
        </div>

        <div class="problem-card">
          <div class="problem-tag">The Big Unsolved Problem</div>
          <div class="problem-title">We Cannot Prove If SHAP Is Actually Right</div>
          <div class="problem-text">
            Real bank datasets only record <strong>if</strong> fraud happened, never <strong>why</strong>.<br><br>
            Because there is no "true answer" recorded in real data, <strong>we cannot verify whether SHAP's explanation is accurate or just a lucky hallucination by the AI.</strong>
          </div>
        </div>

      </div>
    </div>

    <div class="footer-right">
      FraudxAI &bull; Slide 04
    </div>
  </div>

</body>
</html>
"""

HTML_PATH.write_text(html_content, encoding="utf-8")
print(f"Wrote simple HTML to {HTML_PATH}")

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
    print(f"Screenshot saved to {IMAGE_PATH}")
