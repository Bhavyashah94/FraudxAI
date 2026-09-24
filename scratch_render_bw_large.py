import subprocess
from pathlib import Path

SVG_PATH = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\docs\fraudxai_architecture_bw_large.svg")
PNG_PATH = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\docs\fraudxai_architecture_bw_large.png")

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 850" width="1600" height="850" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Sharp Black Arrow Marker -->
    <marker id="arrow-large" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0F172A"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="1600" height="850" fill="#FFFFFF"/>

  <!-- ==================== COLUMN 1 ==================== -->
  <g transform="translate(50, 40)">
    <rect width="335" height="770" rx="14" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
    <!-- Top Header Bar -->
    <rect width="335" height="85" rx="14" fill="#0F172A"/>
    <rect y="60" width="335" height="25" fill="#0F172A"/>
    <circle cx="48" cy="42" r="20" fill="#FFFFFF"/>
    <text x="48" y="49" text-anchor="middle" font-size="18" font-weight="800" fill="#0F172A">01</text>
    <text x="82" y="49" font-size="20" font-weight="700" fill="#FFFFFF">Multi-Agent Simulation</text>

    <!-- Point to Point Content (No nested cards) -->
    <g transform="translate(24, 125)">
      <!-- Point 1 -->
      <circle cx="8" cy="10" r="5" fill="#0F172A"/>
      <text x="24" y="16" font-size="18" font-weight="700" fill="#0F172A">Normal Cardholders</text>
      <text x="24" y="44" font-size="16" fill="#334155" width="280">
        <tspan x="24" dy="0">Real shopping habits calibrated</tspan>
        <tspan x="24" dy="26">to official US &amp; Indian data</tspan>
        <tspan x="24" dy="26">(commutes, meals, bills).</tspan>
      </text>

      <!-- Point 2 -->
      <circle cx="8" cy="145" r="5" fill="#0F172A"/>
      <text x="24" y="151" font-size="18" font-weight="700" fill="#0F172A">Adaptive Attackers</text>
      <text x="24" y="179" font-size="16" fill="#334155">
        <tspan x="24" dy="0">10 realistic cybercrime tactics</tspan>
        <tspan x="24" dy="26">(card testing, stolen mobile</tspan>
        <tspan x="24" dy="26">wallets, account takeovers).</tspan>
      </text>

      <!-- Point 3 -->
      <circle cx="8" cy="280" r="5" fill="#0F172A"/>
      <text x="24" y="286" font-size="18" font-weight="700" fill="#0F172A">Merchant Network</text>
      <text x="24" y="314" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Real store categories (MCC)</tspan>
        <tspan x="24" dy="26">across physical card swipes</tspan>
        <tspan x="24" dy="26">and online 3DS gateways.</tspan>
      </text>

      <!-- Point 4 -->
      <circle cx="8" cy="415" r="5" fill="#0F172A"/>
      <text x="24" y="421" font-size="18" font-weight="700" fill="#0F172A">High-Speed Engine</text>
      <text x="24" y="449" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Generates 64,000+ events</tspan>
        <tspan x="24" dy="26">per second on standard</tspan>
        <tspan x="24" dy="26">consumer laptops.</tspan>
      </text>

      <!-- Bottom Status Pill -->
      <rect x="0" y="555" width="287" height="48" rx="8" fill="#F1F5F9" stroke="#0F172A" stroke-width="1.2"/>
      <text x="143" y="585" text-anchor="middle" font-size="15" font-weight="700" fill="#0F172A">Authentic User Routines</text>
    </g>
  </g>

  <!-- Arrow 1 -> 2 -->
  <line x1="395" y1="425" x2="435" y2="425" stroke="#0F172A" stroke-width="2.5" marker-end="url(#arrow-large)"/>

  <!-- ==================== COLUMN 2 ==================== -->
  <g transform="translate(445, 40)">
    <rect width="335" height="770" rx="14" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
    <rect width="335" height="85" rx="14" fill="#0F172A"/>
    <rect y="60" width="335" height="25" fill="#0F172A"/>
    <circle cx="48" cy="42" r="20" fill="#FFFFFF"/>
    <text x="48" y="49" text-anchor="middle" font-size="18" font-weight="800" fill="#0F172A">02</text>
    <text x="82" y="49" font-size="20" font-weight="700" fill="#FFFFFF">Banking Rules &amp; Switch</text>

    <g transform="translate(24, 125)">
      <!-- Point 1 -->
      <circle cx="8" cy="10" r="5" fill="#0F172A"/>
      <text x="24" y="16" font-size="18" font-weight="700" fill="#0F172A">Payment Switch (&lt;50ms)</text>
      <text x="24" y="44" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Standard ISO 8583 banking</tspan>
        <tspan x="24" dy="26">rails with real approval and</tspan>
        <tspan x="24" dy="26">decline response codes.</tspan>
      </text>

      <!-- Point 2 -->
      <circle cx="8" cy="145" r="5" fill="#0F172A"/>
      <text x="24" y="151" font-size="18" font-weight="700" fill="#0F172A">Regulatory Guardrails</text>
      <text x="24" y="179" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Mandatory 2-Factor OTP</tspan>
        <tspan x="24" dy="26">(RBI) and legal Adverse Action</tspan>
        <tspan x="24" dy="26">notices (US Reg B).</tspan>
      </text>

      <!-- Point 3 -->
      <circle cx="8" cy="280" r="5" fill="#0F172A"/>
      <text x="24" y="286" font-size="18" font-weight="700" fill="#0F172A">Physical Invariants</text>
      <text x="24" y="314" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Blocks impossible travel</tspan>
        <tspan x="24" dy="26">(&gt;900 km/h) and enforces</tspan>
        <tspan x="24" dy="26">daily card spending limits.</tspan>
      </text>

      <!-- Point 4 -->
      <circle cx="8" cy="415" r="5" fill="#0F172A"/>
      <text x="24" y="421" font-size="18" font-weight="700" fill="#0F172A">Ledger Balance</text>
      <text x="24" y="449" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Strict double-entry accounting</tspan>
        <tspan x="24" dy="26">guarantees zero missing</tspan>
        <tspan x="24" dy="26">or invented money.</tspan>
      </text>

      <!-- Bottom Status Pill -->
      <rect x="0" y="555" width="287" height="48" rx="8" fill="#F1F5F9" stroke="#0F172A" stroke-width="1.2"/>
      <text x="143" y="585" text-anchor="middle" font-size="15" font-weight="700" fill="#0F172A">152 / 152 Unit Tests Passed</text>
    </g>
  </g>

  <!-- Arrow 2 -> 3 -->
  <line x1="790" y1="425" x2="830" y2="425" stroke="#0F172A" stroke-width="2.5" marker-end="url(#arrow-large)"/>

  <!-- ==================== COLUMN 3 ==================== -->
  <g transform="translate(840, 40)">
    <rect width="335" height="770" rx="14" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
    <rect width="335" height="85" rx="14" fill="#0F172A"/>
    <rect y="60" width="335" height="25" fill="#0F172A"/>
    <circle cx="48" cy="42" r="20" fill="#FFFFFF"/>
    <text x="48" y="49" text-anchor="middle" font-size="18" font-weight="800" fill="#0F172A">03</text>
    <text x="82" y="49" font-size="20" font-weight="700" fill="#FFFFFF">Operations &amp; Queues</text>

    <g transform="translate(24, 125)">
      <!-- Point 1 -->
      <circle cx="8" cy="10" r="5" fill="#0F172A"/>
      <text x="24" y="16" font-size="18" font-weight="700" fill="#0F172A">Human Investigator Desk</text>
      <text x="24" y="44" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Models daily alert review</tspan>
        <tspan x="24" dy="26">limits, prioritizing the most</tspan>
        <tspan x="24" dy="26">suspicious card alerts first.</tspan>
      </text>

      <!-- Point 2 -->
      <circle cx="8" cy="145" r="5" fill="#0F172A"/>
      <text x="24" y="151" font-size="18" font-weight="700" fill="#0F172A">Dispute &amp; Chargeback Lag</text>
      <text x="24" y="179" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Simulates real 30 to 90 day</tspan>
        <tspan x="24" dy="26">customer reporting delays</tspan>
        <tspan x="24" dy="26">and statement lag.</tspan>
      </text>

      <!-- Point 3 -->
      <circle cx="8" cy="280" r="5" fill="#0F172A"/>
      <text x="24" y="286" font-size="18" font-weight="700" fill="#0F172A">Zero-Leakage Feeds</text>
      <text x="24" y="314" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Strictly separates live swipe</tspan>
        <tspan x="24" dy="26">data from future settlement</tspan>
        <tspan x="24" dy="26">to stop models from cheating.</tspan>
      </text>

      <!-- Point 4 -->
      <circle cx="8" cy="415" r="5" fill="#0F172A"/>
      <text x="24" y="421" font-size="18" font-weight="700" fill="#0F172A">Unreported Dark Fraud</text>
      <text x="24" y="449" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Accounts for small micro-charges</tspan>
        <tspan x="24" dy="26">that cardholders fail to notice</tspan>
        <tspan x="24" dy="26">or dispute.</tspan>
      </text>

      <!-- Bottom Status Pill -->
      <rect x="0" y="555" width="287" height="48" rx="8" fill="#F1F5F9" stroke="#0F172A" stroke-width="1.2"/>
      <text x="143" y="585" text-anchor="middle" font-size="15" font-weight="700" fill="#0F172A">Real-World Bank Workflows</text>
    </g>
  </g>

  <!-- Arrow 3 -> 4 -->
  <line x1="1185" y1="425" x2="1225" y2="425" stroke="#0F172A" stroke-width="2.5" marker-end="url(#arrow-large)"/>

  <!-- ==================== COLUMN 4 ==================== -->
  <g transform="translate(1235, 40)">
    <rect width="335" height="770" rx="14" fill="#FFFFFF" stroke="#0F172A" stroke-width="2"/>
    <rect width="335" height="85" rx="14" fill="#0F172A"/>
    <rect y="60" width="335" height="25" fill="#0F172A"/>
    <circle cx="48" cy="42" r="20" fill="#FFFFFF"/>
    <text x="48" y="49" text-anchor="middle" font-size="18" font-weight="800" fill="#0F172A">04</text>
    <text x="82" y="49" font-size="20" font-weight="700" fill="#FFFFFF">Ground-Truth XAI Audits</text>

    <g transform="translate(24, 125)">
      <!-- Point 1 -->
      <circle cx="8" cy="10" r="5" fill="#0F172A"/>
      <text x="24" y="16" font-size="18" font-weight="700" fill="#0F172A">Known Fraud Cause (Δx)</text>
      <text x="24" y="44" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Explicit mathematical record</tspan>
        <tspan x="24" dy="26">of exactly what the fraudster</tspan>
        <tspan x="24" dy="26">changed during the attack.</tspan>
      </text>

      <!-- Point 2 -->
      <circle cx="8" cy="145" r="5" fill="#0F172A"/>
      <text x="24" y="151" font-size="18" font-weight="700" fill="#0F172A">Model Benchmarking</text>
      <text x="24" y="179" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Compares fast models (LightGBM)</tspan>
        <tspan x="24" dy="26">with transparent glass-box</tspan>
        <tspan x="24" dy="26">models (EBM) over time.</tspan>
      </text>

      <!-- Point 3 -->
      <circle cx="8" cy="280" r="5" fill="#0F172A"/>
      <text x="24" y="286" font-size="18" font-weight="700" fill="#0F172A">Auditing Explanations</text>
      <text x="24" y="314" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Uses Quantus benchmarks to</tspan>
        <tspan x="24" dy="26">score whether tools (SHAP)</tspan>
        <tspan x="24" dy="26">tell the truth or hallucinate.</tspan>
      </text>

      <!-- Point 4 -->
      <circle cx="8" cy="415" r="5" fill="#0F172A"/>
      <text x="24" y="421" font-size="18" font-weight="700" fill="#0F172A">Regulatory Compliance</text>
      <text x="24" y="449" font-size="16" fill="#334155">
        <tspan x="24" dy="0">Produces verifiable, auditable</tspan>
        <tspan x="24" dy="26">reports that meet Federal</tspan>
        <tspan x="24" dy="26">Reserve &amp; RBI rules.</tspan>
      </text>

      <!-- Bottom Status Pill -->
      <rect x="0" y="555" width="287" height="48" rx="8" fill="#F1F5F9" stroke="#0F172A" stroke-width="1.2"/>
      <text x="143" y="585" text-anchor="middle" font-size="15" font-weight="700" fill="#0F172A">Verifiable Trust for Regulators</text>
    </g>
  </g>
</svg>
"""

SVG_PATH.write_text(svg_content, encoding="utf-8")
print(f"Wrote SVG to {SVG_PATH}")

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    f"--screenshot={PNG_PATH}",
    "--window-size=1600,850",
    str(SVG_PATH.as_uri()),
]

res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Chrome exited with code {res.returncode}")
if PNG_PATH.exists():
    print(f"PNG saved successfully: {PNG_PATH} ({PNG_PATH.stat().st_size} bytes)")
