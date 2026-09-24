import os
import subprocess
from pathlib import Path

# Paths
OUTPUT_DIR = Path(r"C:\Users\bhavy\.gemini\antigravity\brain\bb46deb3-54dc-4cb9-a946-6206c822c9a5\scratch\slides")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
HTML_PATH = OUTPUT_DIR / "sample_slide.html"
IMAGE_PATH = OUTPUT_DIR / "sample_slide.png"

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
    background: #0B0F19;
    color: #F8FAFC;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Inter, Arial, sans-serif;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 80px 100px;
    position: relative;
  }
  
  /* Subtle background radial glow */
  body::before {
    content: '';
    position: absolute;
    top: -200px;
    right: -100px;
    width: 700px;
    height: 700px;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.08) 0%, rgba(11, 15, 25, 0) 70%);
    pointer-events: none;
  }
  body::after {
    content: '';
    position: absolute;
    bottom: -200px;
    left: -100px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(16, 185, 129, 0.05) 0%, rgba(11, 15, 25, 0) 70%);
    pointer-events: none;
  }

  /* Header Section */
  .header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  .tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.28);
    color: #38BDF8;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 16px;
  }
  .tag-dot {
    width: 6px;
    height: 6px;
    background: #38BDF8;
    border-radius: 50%;
  }
  .title {
    font-size: 46px;
    font-weight: 700;
    line-height: 1.15;
    color: #FFFFFF;
    letter-spacing: -0.02em;
    max-width: 1100px;
  }
  .subtitle {
    font-size: 20px;
    color: #94A3B8;
    margin-top: 12px;
    line-height: 1.5;
    max-width: 1000px;
  }
  .slide-num {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 16px;
    color: #64748B;
    font-weight: 500;
  }

  /* Content Grid */
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 36px;
    margin: 40px 0;
  }

  .card {
    background: #111827;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 36px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }
  .card.highlight {
    border-color: rgba(56, 189, 248, 0.35);
    background: linear-gradient(180deg, rgba(17, 24, 39, 0.95) 0%, rgba(15, 23, 42, 0.8) 100%);
  }
  .card.highlight::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #38BDF8, #818CF8);
  }

  .card-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
  }
  .card-icon {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    font-weight: 700;
  }
  .card-icon.red {
    background: rgba(244, 63, 94, 0.15);
    color: #F43F5E;
    border: 1px solid rgba(244, 63, 94, 0.3);
  }
  .card-icon.blue {
    background: rgba(56, 189, 248, 0.15);
    color: #38BDF8;
    border: 1px solid rgba(56, 189, 248, 0.3);
  }
  .card-title {
    font-size: 22px;
    font-weight: 600;
    color: #F1F5F9;
  }

  .bullet-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .bullet-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    font-size: 17px;
    line-height: 1.55;
    color: #CBD5E1;
  }
  .bullet-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    margin-top: 9px;
    flex-shrink: 0;
  }
  .bullet-dot.red { background: #F43F5E; }
  .bullet-dot.cyan { background: #38BDF8; }

  /* Formula / Callout Box */
  .formula-box {
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 16px 20px;
    margin-top: 24px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 15px;
    color: #E2E8F0;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .formula-highlight {
    color: #38BDF8;
    font-weight: 600;
  }

  /* Metric Row Bottom */
  .stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    padding-top: 10px;
  }
  .stat-card {
    background: rgba(17, 24, 39, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 14px;
    padding: 18px 22px;
  }
  .stat-value {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 28px;
    font-weight: 700;
    color: #38BDF8;
    letter-spacing: -0.02em;
  }
  .stat-label {
    font-size: 13px;
    color: #94A3B8;
    margin-top: 6px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  /* Footer */
  .footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 24px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-size: 14px;
    color: #64748B;
  }
  .footer-left {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .footer-badge {
    background: rgba(16, 185, 129, 0.1);
    color: #10B981;
    border: 1px solid rgba(16, 185, 129, 0.25);
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-family: ui-monospace, monospace;
    font-weight: 600;
  }
</style>
</head>
<body>

  <!-- Top Header -->
  <div class="header">
    <div>
      <div class="tag">
        <span class="tag-dot"></span>
        FraudxAI &bull; Research Methodology &amp; Motivation
      </div>
      <h1 class="title">The Ground-Truth Crisis in Fraud Explainability</h1>
      <p class="subtitle">Why post-hoc XAI (SHAP, LIME) cannot be validated on existing fraud datasets, and how causal intervention ground truth resolves the evaluation bottleneck.</p>
    </div>
    <div class="slide-num">03 / 12</div>
  </div>

  <!-- Main Content Comparison Grid -->
  <div class="grid">
    
    <!-- Left: Existing Dilemma -->
    <div class="card">
      <div>
        <div class="card-header">
          <div class="card-icon red">&times;</div>
          <h2 class="card-title">The Industry Dilemma (Existing Datasets)</h2>
        </div>
        <ul class="bullet-list">
          <li class="bullet-item">
            <span class="bullet-dot red"></span>
            <div><strong>Anonymized PCA Vectors:</strong> Public benchmarks (e.g., Kaggle ULB) mask features into eigenvectors (V1&ndash;V28), rendering explanations meaningless for banking compliance and fraud ops.</div>
          </li>
          <li class="bullet-item">
            <span class="bullet-dot red"></span>
            <div><strong>Zero Explanation Ground Truth:</strong> Real bank feeds record binary labels (<code>is_fraud</code>), but no mathematical record of the <em>exact root cause</em> behind the alert.</div>
          </li>
          <li class="bullet-item">
            <span class="bullet-dot red"></span>
            <div><strong>Subjective Confirmation Bias:</strong> Prior literature assesses SHAP by visual inspection ("Amount looks high, so SHAP works"), failing rigorous Quantus scientific standards.</div>
          </li>
        </ul>
      </div>
      
      <div class="formula-box">
        <span>Observed Reality:</span>
        <span style="color: #F43F5E;">Y &isin; {0, 1} &nbsp;|&nbsp; &nabla;x (Root Cause) = UNKNOWN</span>
      </div>
    </div>

    <!-- Right: Proposed Causal Solution -->
    <div class="card highlight">
      <div>
        <div class="card-header">
          <div class="card-icon blue">&check;</div>
          <h2 class="card-title">Our Causal Intervention Approach</h2>
        </div>
        <ul class="bullet-list">
          <li class="bullet-item">
            <span class="bullet-dot cyan"></span>
            <div><strong>Physical Attack Footprint (&Delta;x):</strong> Every simulated fraud attack injects explicit mathematical interventions against the cardholder's 30-day baseline profile.</div>
          </li>
          <li class="bullet-item">
            <span class="bullet-dot cyan"></span>
            <div><strong>Axiomatic Game-Theoretic Ground Truth:</strong> Generates exact Shapley attributions via Owen multilinear forms and 128-point Gauss-Legendre path integration.</div>
          </li>
          <li class="bullet-item">
            <span class="bullet-dot cyan"></span>
            <div><strong>Standardized Benchmark Metrics:</strong> Quantus &amp; OpenXAI evaluation using Precision@k, Recall@k, Kendall's &tau;<sub>b</sub>, and Relative Attribution Error (RAE).</div>
          </li>
        </ul>
      </div>
      
      <div class="formula-box">
        <span>Causal Delta:</span>
        <span class="formula-highlight">&Delta;x = x<sub>attack</sub> &minus; x<sub>baseline</sub> &nbsp;&bull;&nbsp; &Phi;<sup>*</sup> (True Logits)</span>
      </div>
    </div>

  </div>

  <!-- Bottom Metric Callouts -->
  <div class="stats-row">
    <div class="stat-card">
      <div class="stat-value">62.8%</div>
      <div class="stat-label">Intervention Precision (P@3)</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">0.4439</div>
      <div class="stat-label">Kendall's &tau;<sub>b</sub> Concordance</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">132 / 132</div>
      <div class="stat-label">Invariants 100% Green</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">&lt; 900 km/h</div>
      <div class="stat-label">Kinematic Transit Ceiling</div>
    </div>
  </div>

  <!-- Footer -->
  <div class="footer">
    <div class="footer-left">
      <span class="footer-badge">VERIFIED</span>
      <span>FraudxAI: Grounded Discrete-Event Simulation &amp; Causal XAI Benchmark</span>
    </div>
    <div>Department of Information Technology &bull; Academic Year 2025&ndash;2026</div>
  </div>

</body>
</html>
"""

HTML_PATH.write_text(html_content, encoding="utf-8")
print(f"Wrote HTML to {HTML_PATH}")

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

print("Rendering screenshot with Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Chrome exited with code {res.returncode}")
if IMAGE_PATH.exists():
    print(f"Screenshot successfully saved: {IMAGE_PATH} ({IMAGE_PATH.stat().st_size} bytes)")
else:
    print(f"Screenshot failed! Stderr: {res.stderr}")
