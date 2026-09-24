import subprocess
from pathlib import Path

SVG_PATH = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\docs\fraudxai_architecture_v2.svg")
PNG_PATH = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\docs\fraudxai_architecture_v2.png")

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900" style="background:#FFFFFF; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#EA580C"/>
    </marker>
  </defs>

  <rect width="1600" height="900" fill="#FFFFFF"/>
  <rect x="30" y="30" width="1540" height="840" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>

  <text x="70" y="85" font-family="'DM Serif Text', Georgia, serif" font-size="28" font-weight="700" fill="#0F172A">System Architecture: End-to-End Simulation &amp; XAI Auditing</text>
  <text x="70" y="115" font-size="15" fill="#64748B">From generative multi-agent transactions to ground-truth explainability benchmarks</text>

  <!-- STAGE 1: Multi-Agent Simulation -->
  <g transform="translate(70, 160)" filter="url(#card-shadow)">
    <rect width="320" height="640" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="320" height="70" rx="14" fill="#EFF6FF"/>
    <rect y="56" width="320" height="14" fill="#EFF6FF"/>
    <circle cx="45" cy="35" r="18" fill="#2563EB"/>
    <text x="45" y="41" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">01</text>
    <text x="75" y="41" font-size="17" font-weight="700" fill="#1E3A8A">Multi-Agent Simulation</text>
    
    <g transform="translate(25, 105)">
      <rect x="0" y="0" width="270" height="120" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="24" r="5" fill="#2563EB"/>
      <text x="35" y="28" font-size="15" font-weight="700" fill="#0F172A">Normal Cardholders</text>
      <text x="35" y="52" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• Calibrated US &amp; India habits</tspan>
        <tspan x="35" dy="20">• Commutes, meals &amp; online shopping</tspan>
        <tspan x="35" dy="20">• Diurnal 24h spending rhythms</tspan>
      </text>

      <rect x="0" y="140" width="270" height="125" rx="10" fill="#FEF2F2" stroke="#FECACA"/>
      <circle cx="20" cy="164" r="5" fill="#DC2626"/>
      <text x="35" y="168" font-size="15" font-weight="700" fill="#991B1B">Adaptive Attackers</text>
      <text x="35" y="192" font-size="13" fill="#7F1D1D">
        <tspan x="35" dy="0">• 10 cybercrime attack playbooks</tspan>
        <tspan x="35" dy="20">• Card testing, stolen wallets &amp; ATO</tspan>
        <tspan x="35" dy="20">• Backs off or decays on decline</tspan>
      </text>

      <rect x="0" y="285" width="270" height="120" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="309" r="5" fill="#2563EB"/>
      <text x="35" y="313" font-size="15" font-weight="700" fill="#0F172A">Merchant Network</text>
      <text x="35" y="337" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• 4-digit MCC merchant taxonomy</tspan>
        <tspan x="35" dy="20">• Physical in-store POS vs e-Commerce</tspan>
        <tspan x="35" dy="20">• Dual-currency (USD cents / INR paisa)</tspan>
      </text>

      <rect x="0" y="440" width="270" height="50" rx="8" fill="#F1F5F9"/>
      <text x="135" y="470" text-anchor="middle" font-size="12.5" font-weight="600" fill="#475569">Generates 64,000+ events / sec</text>
    </g>
  </g>

  <line x1="405" y1="460" x2="435" y2="460" stroke="#EA580C" stroke-width="2.5" marker-end="url(#arrow)"/>

  <!-- STAGE 2: Real-World Banking Rules -->
  <g transform="translate(450, 160)" filter="url(#card-shadow)">
    <rect width="320" height="640" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="320" height="70" rx="14" fill="#FFF7ED"/>
    <rect y="56" width="320" height="14" fill="#FFF7ED"/>
    <circle cx="45" cy="35" r="18" fill="#EA580C"/>
    <text x="45" y="41" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">02</text>
    <text x="75" y="41" font-size="17" font-weight="700" fill="#9A3412">Banking Rules &amp; Switch</text>

    <g transform="translate(25, 105)">
      <rect x="0" y="0" width="270" height="120" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="24" r="5" fill="#EA580C"/>
      <text x="35" y="28" font-size="15" font-weight="700" fill="#0F172A">Payment Switch (&lt;50ms)</text>
      <text x="35" y="52" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• ISO 8583 financial message rails</tspan>
        <tspan x="35" dy="20">• Instant approve / decline codes</tspan>
        <tspan x="35" dy="20">• Pre-authorization hold lifecycle</tspan>
      </text>

      <rect x="0" y="140" width="270" height="125" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="164" r="5" fill="#EA580C"/>
      <text x="35" y="168" font-size="15" font-weight="700" fill="#0F172A">Regulatory Guardrails</text>
      <text x="35" y="192" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• RBI mandatory 2-Factor OTP</tspan>
        <tspan x="35" dy="20">• Rule 114B ₹50,000 cash/PAN limits</tspan>
        <tspan x="35" dy="20">• US Reg B Adverse Action notices</tspan>
      </text>

      <rect x="0" y="285" width="270" height="120" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="309" r="5" fill="#EA580C"/>
      <text x="35" y="313" font-size="15" font-weight="700" fill="#0F172A">Physical Invariants</text>
      <text x="35" y="337" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• Great-circle travel speed limits</tspan>
        <tspan x="35" dy="20">• Blocks &gt;900 km/h impossible travel</tspan>
        <tspan x="35" dy="20">• Strict double-entry balance check</tspan>
      </text>

      <rect x="0" y="440" width="270" height="50" rx="8" fill="#FFF7ED"/>
      <text x="135" y="470" text-anchor="middle" font-size="12.5" font-weight="600" fill="#9A3412">152 / 152 Unit Tests Passed</text>
    </g>
  </g>

  <line x1="785" y1="460" x2="815" y2="460" stroke="#EA580C" stroke-width="2.5" marker-end="url(#arrow)"/>

  <!-- STAGE 3: Operations & Review Queue -->
  <g transform="translate(830, 160)" filter="url(#card-shadow)">
    <rect width="320" height="640" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="320" height="70" rx="14" fill="#F0FDF4"/>
    <rect y="56" width="320" height="14" fill="#F0FDF4"/>
    <circle cx="45" cy="35" r="18" fill="#16A34A"/>
    <text x="45" y="41" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">03</text>
    <text x="75" y="41" font-size="17" font-weight="700" fill="#14532D">Operations &amp; Supervision</text>

    <g transform="translate(25, 105)">
      <rect x="0" y="0" width="270" height="120" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="24" r="5" fill="#16A34A"/>
      <text x="35" y="28" font-size="15" font-weight="700" fill="#0F172A">Human Investigator Desk</text>
      <text x="35" y="52" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• Daily alert review capacity limits</tspan>
        <tspan x="35" dy="20">• Prioritizes high-risk card alerts</tspan>
        <tspan x="35" dy="20">• Rapid verification (24 to 72 hours)</tspan>
      </text>

      <rect x="0" y="140" width="270" height="125" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="164" r="5" fill="#16A34A"/>
      <text x="35" y="168" font-size="15" font-weight="700" fill="#0F172A">Dispute &amp; Chargeback Lag</text>
      <text x="35" y="192" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• 30 to 90 day customer dispute delay</tspan>
        <tspan x="35" dy="20">• Simulates statement arrival lag</tspan>
        <tspan x="35" dy="20">• Accounts for unreported dark fraud</tspan>
      </text>

      <rect x="0" y="285" width="270" height="120" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="309" r="5" fill="#16A34A"/>
      <text x="35" y="313" font-size="15" font-weight="700" fill="#0F172A">Zero-Leakage Partitioning</text>
      <text x="35" y="337" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• Real-time inference feed (Day 0)</tspan>
        <tspan x="35" dy="20">• Settlement feed (Day 1-3)</tspan>
        <tspan x="35" dy="20">• Prevents models peeking into future</tspan>
      </text>

      <rect x="0" y="440" width="270" height="50" rx="8" fill="#F0FDF4"/>
      <text x="135" y="470" text-anchor="middle" font-size="12.5" font-weight="600" fill="#15803D">Authentic Banking Operations</text>
    </g>
  </g>

  <line x1="1165" y1="460" x2="1195" y2="460" stroke="#EA580C" stroke-width="2.5" marker-end="url(#arrow)"/>

  <!-- STAGE 4: Ground-Truth XAI Benchmark -->
  <g transform="translate(1210, 160)" filter="url(#card-shadow)">
    <rect width="320" height="640" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect width="320" height="70" rx="14" fill="#FAF5FF"/>
    <rect y="56" width="320" height="14" fill="#FAF5FF"/>
    <circle cx="45" cy="35" r="18" fill="#9333EA"/>
    <text x="45" y="41" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">04</text>
    <text x="75" y="41" font-size="17" font-weight="700" fill="#581C87">Ground-Truth XAI Audits</text>

    <g transform="translate(25, 105)">
      <rect x="0" y="0" width="270" height="120" rx="10" fill="#FAF5FF" stroke="#E9D5FF"/>
      <circle cx="20" cy="24" r="5" fill="#9333EA"/>
      <text x="35" y="28" font-size="15" font-weight="700" fill="#6B21A8">Known Attack Cause (Δx)</text>
      <text x="35" y="52" font-size="13" fill="#581C87">
        <tspan x="35" dy="0">• Records exact cardholder baseline</tspan>
        <tspan x="35" dy="20">• Knows exact amount/speed jump</tspan>
        <tspan x="35" dy="20">• True mathematical "answer key"</tspan>
      </text>

      <rect x="0" y="140" width="270" height="125" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="164" r="5" fill="#9333EA"/>
      <text x="35" y="168" font-size="15" font-weight="700" fill="#0F172A">Model Benchmarking</text>
      <text x="35" y="192" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• Evaluates XGBoost &amp; LightGBM</tspan>
        <tspan x="35" dy="20">• Benchmarks transparent EBM</tspan>
        <tspan x="35" dy="20">• Rolling prequential time testing</tspan>
      </text>

      <rect x="0" y="285" width="270" height="120" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="20" cy="309" r="5" fill="#9333EA"/>
      <text x="35" y="313" font-size="15" font-weight="700" fill="#0F172A">Auditing Explanations</text>
      <text x="35" y="337" font-size="13" fill="#475569">
        <tspan x="35" dy="0">• Audits SHAP, LIME, and EBM</tspan>
        <tspan x="35" dy="20">• Quantus mathematical metrics</tspan>
        <tspan x="35" dy="20">• Proves if AI tells truth or lies</tspan>
      </text>

      <rect x="0" y="440" width="270" height="50" rx="8" fill="#FAF5FF"/>
      <text x="135" y="470" text-anchor="middle" font-size="12.5" font-weight="600" fill="#6B21A8">Verifiable Trust for Regulators</text>
    </g>
  </g>
</svg>
"""

SVG_PATH.write_text(svg_content, encoding="utf-8")
print(f"Wrote SVG to {SVG_PATH}")

# Render with Chrome Headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    f"--screenshot={PNG_PATH}",
    "--window-size=1600,900",
    str(SVG_PATH.as_uri()),
]

res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Chrome exited with code {res.returncode}")
if PNG_PATH.exists():
    print(f"PNG saved successfully: {PNG_PATH} ({PNG_PATH.stat().st_size} bytes)")
