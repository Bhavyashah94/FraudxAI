"""Generates a state-of-the-art, infinite-canvas architecture flowchart
and verified future roadmap application for FraudxAI (inspired by React Flow,
FigJam, Miro, and Palantir Gotham).

Features:
- 100vw x 100vh full-screen infinite canvas with smooth mouse pan & cursor-centered zoom [0.15x - 3.0x]
- Interactive Minimap with real-time viewport tracker and click-to-pan
- 9 distinct architectural zones with labeled swimlanes/boundaries
- Over 32 rich interactive node cards with ports, parameter chips, and mathematical formulas
- Cubic Bézier SVG connection conduits with directional animated flow pulses and condition badges
- Quick-Jump cluster dock and live search bar with auto-camera focus
- Side Technical Inspector Drawer with 5 tabs (Overview, Math Formulas, Contracts, Grounding, Tests & Roadmap)
- Comprehensive integration of the 3 verification documents:
  - fraudxai_honest_review.md
  - fraudxai_improvement_roadmap.md
  - fraudxai_detailed_plan.md
"""

from pathlib import Path
import json

CANVAS_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>FraudxAI — Interactive Simulator Architecture &amp; Future Roadmap Canvas</title>
  <style>
    :root {
      --bg: #070A12;
      --grid-dot: #1A2338;
      --card-bg: #0F172A;
      --card-border: #1E293B;
      --card-hover-border: #38BDF8;
      --text: #F8FAFC;
      --text-muted: #94A3B8;
      --text-dim: #64748B;
      --cyan: #38BDF8;
      --cyan-glow: rgba(56, 189, 248, 0.25);
      --amber: #FBBF24;
      --amber-glow: rgba(251, 191, 36, 0.25);
      --emerald: #34D399;
      --emerald-glow: rgba(52, 211, 153, 0.25);
      --purple: #A78BFA;
      --purple-glow: rgba(167, 139, 250, 0.25);
      --rose: #F87171;
      --rose-glow: rgba(248, 113, 113, 0.25);
      --indigo: #818CF8;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --font-mono: "JetBrains Mono", Consolas, "Courier New", monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
    html, body {
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
    }

    /* Infinite Canvas Viewport */
    #viewport {
      width: 100vw;
      height: 100vh;
      position: absolute;
      top: 0; left: 0;
      overflow: hidden;
      cursor: grab;
      background-color: var(--bg);
      background-image: radial-gradient(var(--grid-dot) 1.5px, transparent 1.5px);
      background-size: 32px 32px;
    }
    #viewport.panning { cursor: grabbing; }

    /* Virtual World Container */
    #world {
      position: absolute;
      top: 0; left: 0;
      width: 6000px;
      height: 4400px;
      transform-origin: 0 0;
      will-change: transform;
    }

    /* SVG Edges Layer */
    #edge-svg {
      position: absolute;
      top: 0; left: 0;
      width: 6000px;
      height: 4400px;
      pointer-events: none;
      z-index: 10;
    }
    .edge-path {
      fill: none;
      stroke-width: 2.2;
      stroke-linecap: round;
      opacity: 0.75;
      transition: stroke-width 0.2s, opacity 0.2s;
    }
    .edge-path.highlighted {
      stroke-width: 4;
      opacity: 1;
      filter: drop-shadow(0 0 8px currentColor);
    }
    .edge-flow {
      fill: none;
      stroke-dasharray: 6 12;
      stroke-linecap: round;
      animation: flowDash 25s linear infinite;
    }
    @keyframes flowDash {
      to { stroke-dashoffset: -1000; }
    }

    /* Edge Condition Badges */
    .edge-badge {
      position: absolute;
      z-index: 25;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 9999px;
      background: #090D16;
      border: 1px solid #1E293B;
      color: var(--text-muted);
      pointer-events: auto;
      transform: translate(-50%, -50%);
      box-shadow: 0 4px 12px rgba(0,0,0,0.6);
      white-space: nowrap;
      transition: all 0.2s;
    }
    .edge-badge:hover {
      border-color: var(--cyan);
      color: var(--text);
      transform: translate(-50%, -50%) scale(1.08);
      z-index: 40;
    }

    /* Swimlanes / Subsystem Zones */
    .zone-box {
      position: absolute;
      border-radius: 16px;
      border: 1px dashed rgba(255, 255, 255, 0.12);
      background: rgba(15, 23, 42, 0.25);
      backdrop-filter: blur(2px);
      z-index: 5;
      pointer-events: none;
    }
    .zone-label {
      position: absolute;
      top: 14px; left: 20px;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 4px 12px;
      border-radius: 6px;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #CBD5E1;
    }

    /* Node Cards */
    .node-card {
      position: absolute;
      z-index: 20;
      width: 360px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      cursor: pointer;
      transition: transform 0.18s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.18s, box-shadow 0.18s;
      overflow: hidden;
    }
    .node-card:hover {
      transform: translateY(-3px) scale(1.015);
      border-color: var(--card-hover-border);
      box-shadow: 0 16px 40px rgba(56, 189, 248, 0.25);
      z-index: 35;
    }
    .node-card.selected {
      border-color: var(--cyan);
      box-shadow: 0 0 0 2px var(--cyan), 0 20px 45px rgba(56, 189, 248, 0.35);
      z-index: 38;
    }
    .node-card.dimmed {
      opacity: 0.25;
      filter: grayscale(80%);
    }

    /* Node Header */
    .node-header {
      padding: 12px 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }
    .node-tag {
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .node-file {
      font-family: var(--font-mono);
      font-size: 10.5px;
      color: var(--text-dim);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .node-body {
      padding: 14px 16px;
    }
    .node-title {
      font-size: 15px;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 6px;
      line-height: 1.3;
    }
    .node-desc {
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 10px;
    }

    /* Key formula pill inside node */
    .node-formula {
      background: #090D16;
      border: 1px solid #1E293B;
      border-radius: 6px;
      padding: 6px 10px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--cyan);
      margin-bottom: 8px;
      white-space: pre-wrap;
      word-break: break-all;
    }

    /* Node Tags row */
    .node-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      margin-top: 8px;
    }
    .node-chip {
      font-family: var(--font-mono);
      font-size: 9.5px;
      background: rgba(255, 255, 255, 0.05);
      color: #94A3B8;
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Ports */
    .port-in, .port-out {
      position: absolute;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #0F172A;
      border: 2.5px solid var(--text-muted);
      top: 50%;
      transform: translateY(-50%);
      transition: all 0.2s;
    }
    .port-in { left: -6px; }
    .port-out { right: -6px; }
    .node-card:hover .port-in, .node-card:hover .port-out {
      border-color: var(--cyan);
      box-shadow: 0 0 8px var(--cyan);
    }

    /* Floating Top HUD Bar */
    .hud-top {
      position: fixed;
      top: 16px; left: 20px; right: 20px;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      pointer-events: none;
    }
    .hud-pill-group {
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 8px 14px;
      display: flex;
      align-items: center;
      gap: 12px;
      pointer-events: auto;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
    }
    .hud-title {
      font-weight: 800;
      font-size: 14px;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .hud-title span { color: var(--cyan); }
    .hud-search-input {
      background: #090D16;
      border: 1px solid #1E293B;
      color: #F8FAFC;
      font-family: var(--font-sans);
      font-size: 12.5px;
      padding: 6px 12px;
      border-radius: 8px;
      width: 240px;
      transition: all 0.2s;
    }
    .hud-search-input:focus {
      outline: none;
      border-color: var(--cyan);
      width: 320px;
      box-shadow: 0 0 12px var(--cyan-glow);
    }

    /* Quick Jump Dropdown */
    .jump-select {
      background: #090D16;
      border: 1px solid #1E293B;
      color: #CBD5E1;
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 600;
      padding: 6px 10px;
      border-radius: 8px;
      cursor: pointer;
      outline: none;
    }
    .jump-select:hover { border-color: var(--cyan); }

    /* Bottom Control Dock */
    .hud-bottom-left {
      position: fixed;
      bottom: 20px; left: 20px;
      z-index: 100;
      display: flex;
      flex-direction: column;
      gap: 8px;
      pointer-events: auto;
    }
    .dock-btn-group {
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 4px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    .dock-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      width: 36px;
      height: 36px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: bold;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s;
    }
    .dock-btn:hover {
      background: #1E293B;
      color: var(--cyan);
    }

    /* Minimap in Bottom-Right */
    #minimap-container {
      position: fixed;
      bottom: 20px; right: 20px;
      width: 260px;
      height: 180px;
      background: rgba(11, 15, 25, 0.9);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      z-index: 100;
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
      overflow: hidden;
      cursor: crosshair;
      pointer-events: auto;
    }
    .minimap-header {
      padding: 6px 10px;
      font-size: 10px;
      font-family: var(--font-mono);
      font-weight: 700;
      color: var(--text-dim);
      border-bottom: 1px solid rgba(255,255,255,0.06);
      display: flex;
      justify-content: space-between;
    }
    #minimap-svg {
      width: 100%;
      height: 150px;
    }
    #minimap-viewport {
      fill: rgba(56, 189, 248, 0.12);
      stroke: var(--cyan);
      stroke-width: 1.5;
    }

    /* Side Technical Inspector Drawer */
    #inspector {
      position: fixed;
      top: 0; right: -650px;
      width: 620px;
      height: 100vh;
      background: rgba(15, 23, 42, 0.96);
      backdrop-filter: blur(20px);
      border-left: 1px solid var(--card-border);
      z-index: 200;
      box-shadow: -15px 0 50px rgba(0, 0, 0, 0.7);
      transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }
    #inspector.open { right: 0; }
    .inspector-header {
      padding: 20px;
      border-bottom: 1px solid var(--card-border);
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
    }
    .inspector-close {
      background: #1E293B;
      border: none;
      color: var(--text-muted);
      width: 32px;
      height: 32px;
      border-radius: 8px;
      font-size: 16px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }
    .inspector-close:hover { background: #334155; color: white; }
    .inspector-tabs {
      display: flex;
      background: #090D16;
      border-bottom: 1px solid var(--card-border);
      overflow-x: auto;
    }
    .inspector-tab-btn {
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 600;
      padding: 10px 14px;
      cursor: pointer;
      white-space: nowrap;
      border-bottom: 2px solid transparent;
      transition: all 0.2s;
    }
    .inspector-tab-btn.active {
      color: var(--cyan);
      border-bottom-color: var(--cyan);
      background: rgba(56, 189, 248, 0.05);
    }
    .inspector-body {
      flex: 1;
      overflow-y: auto;
      padding: 20px;
    }
    .tab-pane { display: none; }
    .tab-pane.active { display: block; }

    /* Code & Callout Blocks inside Inspector */
    .insp-code {
      background: #090D16;
      border: 1px solid #1E293B;
      border-radius: 8px;
      padding: 12px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: #E2E8F0;
      overflow-x: auto;
      margin: 10px 0;
      line-height: 1.5;
    }
    .insp-callout {
      border-left: 3px solid var(--cyan);
      background: rgba(56, 189, 248, 0.08);
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      margin: 12px 0;
      font-size: 12.5px;
      line-height: 1.5;
      color: #CBD5E1;
    }
    .insp-callout-emerald {
      border-left-color: var(--emerald);
      background: rgba(52, 211, 153, 0.08);
    }
    .insp-callout-amber {
      border-left-color: var(--amber);
      background: rgba(251, 191, 36, 0.08);
    }
    .insp-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
      margin: 10px 0;
    }
    .insp-table th {
      background: #1E293B;
      color: #E2E8F0;
      text-align: left;
      padding: 8px 10px;
    }
    .insp-table td {
      border-bottom: 1px solid #1E293B;
      padding: 8px 10px;
      color: #94A3B8;
    }

    /* Subsystem Theme Colors */
    .color-spec { background: rgba(56, 189, 248, 0.15); color: var(--cyan); border: 1px solid var(--cyan); }
    .color-engine { background: rgba(129, 140, 248, 0.15); color: var(--indigo); border: 1px solid var(--indigo); }
    .color-agent { background: rgba(251, 191, 36, 0.15); color: var(--amber); border: 1px solid var(--amber); }
    .color-rail { background: rgba(52, 211, 153, 0.15); color: var(--emerald); border: 1px solid var(--emerald); }
    .color-scm { background: rgba(167, 139, 250, 0.15); color: var(--purple); border: 1px solid var(--purple); }
    .color-supervision { background: rgba(248, 113, 113, 0.15); color: var(--rose); border: 1px solid var(--rose); }
    .color-eval { background: rgba(236, 72, 153, 0.15); color: #F472B6; border: 1px solid #F472B6; }
    .color-roadmap { background: rgba(45, 212, 191, 0.15); color: #2DD4BF; border: 1px solid #2DD4BF; }
  </style>
</head>
<body>

  <!-- Fullscreen Infinite Canvas Viewport -->
  <div id="viewport">
    <div id="world">
      <!-- SVG Connecting Edges -->
      <svg id="edge-svg"></svg>

      <!-- Subsystem Swimlanes / Boundary Zones -->
      <div id="zones-container"></div>

      <!-- Edge Condition Badges -->
      <div id="badges-container"></div>

      <!-- Interactive Node Cards -->
      <div id="nodes-container"></div>
    </div>
  </div>

  <!-- Top Heads-Up Display (HUD) Bar -->
  <div class="hud-top">
    <div class="hud-pill-group">
      <div class="hud-title">
        <span style="font-size:16px;">⚡</span> FRAUDX<span style="color:var(--cyan)">AI</span>
        <span style="font-weight:400; color:var(--text-muted); font-size:12px;">| Architecture &amp; Roadmap Infinite Canvas</span>
      </div>
      <select class="jump-select" id="jump-select" onchange="jumpToCluster(this.value)">
        <option value="">Jump to Subsystem...</option>
        <option value="zone-spec">Zone 0: Ground-Truth Specifications</option>
        <option value="zone-engine">Zone 1: Discrete-Event MTPP Engine</option>
        <option value="zone-agents">Zone 2: Closed-Loop Multi-Agent System</option>
        <option value="zone-rails">Zone 3: Decoupled Institutional Rail Switch</option>
        <option value="zone-scm">Zone 4: Causal SCM &amp; Streaming Ledger</option>
        <option value="zone-supervision">Zone 5: FIU Supervision &amp; Delayed Feedback</option>
        <option value="zone-eval">Zone 6: Prequential Streaming Evaluation</option>
        <option value="zone-reporter">Zone 7: Camera-Ready Benchmark Reporter</option>
        <option value="zone-roadmap">Zone 8: Verified Future Roadmap (Phases 1-4)</option>
      </select>
      <input type="text" id="node-search" class="hud-search-input" placeholder="Search modules, math, classes (e.g. ISO 51, Hawkes)..." oninput="searchNodes(this.value)">
    </div>

    <div class="hud-pill-group">
      <div style="font-family:var(--font-mono); font-size:11px; font-weight:700; color:var(--emerald);">
        ● 178/178 TESTS PASSING
      </div>
      <div style="font-family:var(--font-mono); font-size:11px; color:var(--text-dim);">
        commit f4b2681 (main)
      </div>
    </div>
  </div>

  <!-- Bottom-Left Navigation Dock -->
  <div class="hud-bottom-left">
    <div class="dock-btn-group">
      <button class="dock-btn" onclick="zoomIn()" title="Zoom In">+</button>
      <button class="dock-btn" onclick="zoomOut()" title="Zoom Out">−</button>
      <button class="dock-btn" onclick="resetZoom()" title="Reset Zoom (100%)">1:1</button>
      <button class="dock-btn" onclick="fitView()" title="Fit All to View">⛶</button>
    </div>
  </div>

  <!-- Bottom-Right Minimap -->
  <div id="minimap-container">
    <div class="minimap-header">
      <span>SYSTEM MINIMAP</span>
      <span id="zoom-indicator">100%</span>
    </div>
    <svg id="minimap-svg" viewBox="0 0 6000 4400">
      <g id="minimap-zones"></g>
      <g id="minimap-nodes"></g>
      <rect id="minimap-viewport" x="0" y="0" width="1000" height="700" />
    </svg>
  </div>

  <!-- Side Technical Inspector Drawer -->
  <div id="inspector">
    <div class="inspector-header">
      <div>
        <div id="insp-tag" class="node-tag color-engine" style="display:inline-block; margin-bottom:6px;">ENGINE</div>
        <h2 id="insp-title" style="font-size:18px; font-weight:800; color:#FFFFFF;">Node Title</h2>
        <div id="insp-file" style="font-family:var(--font-mono); font-size:11px; color:var(--cyan); margin-top:3px;">file.py:100-200</div>
      </div>
      <button class="inspector-close" onclick="closeInspector()">✕</button>
    </div>

    <div class="inspector-tabs">
      <button class="inspector-tab-btn active" onclick="switchInspTab('overview')">Overview</button>
      <button class="inspector-tab-btn" onclick="switchInspTab('math')">Math &amp; Algorithm</button>
      <button class="inspector-tab-btn" onclick="switchInspTab('contracts')">Data Contracts</button>
      <button class="inspector-tab-btn" onclick="switchInspTab('grounding')">Banking Grounding</button>
      <button class="inspector-tab-btn" onclick="switchInspTab('verification')">Tests &amp; Roadmap</button>
    </div>

    <div class="inspector-body">
      <!-- Tab 1: Overview -->
      <div id="insp-tab-overview" class="tab-pane active">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Architectural Purpose</h4>
        <p id="insp-desc" style="font-size:13px; color:#E2E8F0; line-height:1.5; margin-bottom:14px;"></p>
        
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Key Responsibilities</h4>
        <ul id="insp-responsibilities" style="margin-left:18px; font-size:12.5px; color:#CBD5E1; line-height:1.5;"></ul>
      </div>

      <!-- Tab 2: Math -->
      <div id="insp-tab-math" class="tab-pane">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Mathematical Equations</h4>
        <pre class="insp-code"><code id="insp-math"></code></pre>
        <div id="insp-math-expl" class="insp-callout"></div>
      </div>

      <!-- Tab 3: Contracts -->
      <div id="insp-tab-contracts" class="tab-pane">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Inputs &amp; Preconditions</h4>
        <div id="insp-inputs" class="insp-callout"></div>

        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-top:14px; margin-bottom:6px;">Outputs &amp; State Mutations</h4>
        <div id="insp-outputs" class="insp-callout insp-callout-emerald"></div>
      </div>

      <!-- Tab 4: Grounding -->
      <div id="insp-tab-grounding" class="tab-pane">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Real-World Payment Rails &amp; Citations</h4>
        <div id="insp-grounding" class="insp-callout insp-callout-amber"></div>
      </div>

      <!-- Tab 5: Tests & Roadmap -->
      <div id="insp-tab-verification" class="tab-pane">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Test Suite Coverage</h4>
        <div id="insp-test" class="insp-callout insp-callout-emerald"></div>

        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-top:14px; margin-bottom:6px;">Roadmap Step Upgrades</h4>
        <div id="insp-roadmap-step" class="insp-callout"></div>
      </div>
    </div>
  </div>

  <!-- CANVAS DATA & INTERACTION SCRIPT -->
  <script>
    // -------------------------------------------------------------
    // 1. ARCHITECTURAL ZONES (SWIMLANES)
    // -------------------------------------------------------------
    const ZONES = [
      { id: "zone-spec", title: "Zone 0: Ground-Truth Specifications (spec/*.yaml)", x: 80, y: 100, w: 480, h: 2500, color: "var(--cyan)" },
      { id: "zone-engine", title: "Zone 1: Discrete-Event MTPP Priority Queue (engine.py & hawkes.py)", x: 640, y: 100, w: 560, h: 1400, color: "var(--indigo)" },
      { id: "zone-agents", title: "Zone 2: Closed-Loop Multi-Agent Behavioral Loop (agents.py & syndicates.py)", x: 1280, y: 100, w: 600, h: 1800, color: "var(--amber)" },
      { id: "zone-rails", title: "Zone 3: Decoupled Institutional Rail Switch & Solvency (rails.py)", x: 1960, y: 100, w: 560, h: 1400, color: "var(--emerald)" },
      { id: "zone-scm", title: "Zone 4: Causal SCM & Zero-Leakage Streaming Ledger (causal_scm.py & ledger.py)", x: 2600, y: 100, w: 560, h: 1400, color: "var(--purple)" },
      { id: "zone-supervision", title: "Zone 5: FIU Operational Supervision & Delayed Feedback (stream.py)", x: 3240, y: 100, w: 560, h: 1600, color: "var(--rose)" },
      { id: "zone-eval", title: "Zone 6: Prequential Streaming Evaluation & Drift Auditing (evaluation.py)", x: 3880, y: 100, w: 560, h: 1600, color: "#F472B6" },
      { id: "zone-reporter", title: "Zone 7: Camera-Ready Benchmark Reporter & CLI (benchmark_reporter.py & cli.py)", x: 4520, y: 100, w: 560, h: 1400, color: "var(--cyan)" },
      { id: "zone-roadmap", title: "Zone 8: Verified Future Roadmap (Phases 1–4, Steps 1–14, Tiers 1–5)", x: 80, y: 2750, w: 5000, h: 1400, color: "#2DD4BF" }
    ];

    // -------------------------------------------------------------
    // 2. DETAILED NODE DEFINITIONS (ZERO ASSUMPTIONS)
    // -------------------------------------------------------------
    const NODES = [
      // ZONE 0: SPECS
      {
        id: "spec-loader",
        zone: "zone-spec",
        tag: "SPEC LOADER",
        tagColor: "color-spec",
        title: "spec_loader.py (Single Source of Truth)",
        file: "fraudx_synthesizer/spec_loader.py:1-740",
        x: 120, y: 200, w: 400,
        desc: "Loads, freezes, and validates 12 typed YAML schemas in spec/. Guarantees zero magic numbers and deterministic config reproduction across runs.",
        formula: "specs = load_all_specs()\\nEnforces frozen Pydantic/dataclass schema invariants",
        chips: ["YAML Frozen", "Zero Magic Numbers", "12 Specs", "Typed Dataclasses"],
        inputs: "spec/*.yaml configuration files (financial instruments, personas, playbooks, rails, targets)",
        outputs: "AllSpecs container accessed globally by engine, agents, rails, and benchmark",
        grounding: "ISO 8583 payment codes, RBI Circulars, Visa Core Rules, Fed DCPC 2023",
        test: "tests/test_taxonomy_specs.py::test_specs_load_and_validate",
        roadmap: "Maintains specification-first single source of truth across all subsequent phases."
      },
      {
        id: "spec-personas",
        zone: "zone-spec",
        tag: "SPEC SCHEMA",
        tagColor: "color-spec",
        title: "02_human_personas.yaml",
        file: "spec/02_human_personas.yaml:1-350",
        x: 120, y: 560, w: 400,
        desc: "Defines 7 Fed DCPC consumer cohorts (C1 Gig Worker to C7 High Wealth) and 5 Indian socioeconomic cohorts (IN_C1 Rural Farmer to IN_C5 Super Premium HNI) with empirical ticket marginals.",
        formula: "LogNormal(mu, sigma) spliced with GPD tails for ticket sizes\\nVon Mises circular diurnal density profile",
        chips: ["7 US Cohorts", "5 Indian Cohorts", "Spliced LogNormal-GPD", "BLS Expenditure"],
        inputs: "Demographic and consumer payment surveys (Fed DCPC, BLS, RBI)",
        outputs: "Calibrated parameters for CardholderProfile generation",
        grounding: "Federal Reserve Dairy of Consumer Payment Choice; RBI Payment System Indicators",
        test: "tests/test_taxonomy_specs.py::test_persona_spend_marginals",
        roadmap: "Tier 2: Expand calibration targets against published monthly RBI and Fed updates."
      },
      {
        id: "spec-playbooks",
        zone: "zone-spec",
        tag: "SPEC SCHEMA",
        tagColor: "color-spec",
        title: "04_adversarial_playbooks.yaml",
        file: "spec/04_adversarial_playbooks.yaml:1-420",
        x: 120, y: 920, w: 400,
        desc: "10 grounded cybercrime playbooks (Micro-Auth probe, ATO silent baking, Sleeper bust-out, Apple Pay yellow path, Distributed BIN attacks, Reverse-proxy vishing, SIM swap).",
        formula: "Finite State Machine with transition probabilities and action sequences",
        chips: ["10 Playbooks", "Global & India", "Bisection Decay", "Gateway Hopping"],
        inputs: "Threat intelligence and industrial cybercrime attack manuals",
        outputs: "Adversarial execution rules loaded into AdaptiveFraudsterAgent",
        grounding: "FIN7, Magecart, and Indian cybercrime investigation telemetry (1930 / I4C)",
        test: "tests/test_adversarial_intent_mesh.py",
        roadmap: "Step 3: Wire CANONICAL_ATTACK_INTERVENTIONS directly to SCM ground truth."
      },
      {
        id: "spec-supervision",
        zone: "zone-spec",
        tag: "SPEC SCHEMA",
        tagColor: "color-spec",
        title: "16_operational_supervision.yaml",
        file: "spec/16_operational_supervision.yaml:1-120",
        x: 120, y: 1280, w: 400,
        desc: "Formalizes Day 3 supervision plumbing: Daily FIU triage alert budget K, Weibull investigator review delay, LogNormal chargeback dispute lag, and dark fraud reporting curves.",
        formula: "Weibull(k=1.45, lambda=18.5h)\\nLogNormal(mu=ln(32d), sigma=0.35)\\nDark fraud sigmoid V_0=$15/₹500",
        chips: ["FIU Queue K=50", "Weibull Fast Review", "LogNormal Dispute Lag", "Dark Fraud"],
        inputs: "Dal Pozzolo (2018), Carcillo (2018), Visa Claims Resolution rules",
        outputs: "SupervisionEngine configuration parameters",
        grounding: "Dal Pozzolo et al. (IEEE TNNLS 2018); Visa Core Rules 10.4 dispute window",
        test: "tests/test_supervision_engine.py",
        roadmap: "Tier 4: Calibrate against bank dispute filing latency matrices via split-learning."
      },
      {
        id: "spec-prequential",
        zone: "zone-spec",
        tag: "SPEC SCHEMA",
        tagColor: "color-spec",
        title: "17_prequential_evaluation.yaml",
        file: "spec/17_prequential_evaluation.yaml:1-90",
        x: 120, y: 1640, w: 400,
        desc: "Formalizes rolling predict-then-train streaming parameters: training window W_train (60d), test window W_test (7d), delay gap exclusion tau_delay, and retraining frequency.",
        formula: "Predict on [T, T + W_test]\\nTrain on [T - W_train, T - tau_delay]",
        chips: ["Delay-Gap Invariant", "Predict-Then-Train", "Cost Matrix", "Drift Alarms"],
        inputs: "Streaming evaluation benchmarks (Bifet 2018, Jesus 2022)",
        outputs: "PrequentialStreamingEvaluator protocol configuration",
        grounding: "Carcillo et al. (AAAI 2018); Le Borgne et al. (2021)",
        test: "tests/test_prequential_benchmark.py",
        roadmap: "Step 8: Implement temporal self-TSTR generalization bounds."
      },
      {
        id: "spec-reporting",
        zone: "zone-spec",
        tag: "SPEC SCHEMA",
        tagColor: "color-spec",
        title: "18_benchmark_reporting.yaml",
        file: "spec/18_benchmark_reporting.yaml:1-110",
        x: 120, y: 2000, w: 400,
        desc: "Publication-grade reporting specifications: Tol colorblind-safe palettes, IEEE/ACM/NeurIPS dimension presets, figure styles, and multi-K triage curves.",
        formula: "Widths: IEEE 3.5in, ACM 3.33in, NeurIPS 5.5in @ 300 DPI\\nTol Colorblind Palette",
        chips: ["IEEE Typography", "Tol Palette", "Camera-Ready", "Headless Agg"],
        inputs: "NeurIPS Datasets & Benchmarks Track and IEEE S&P standards",
        outputs: "BenchmarkReporter formatting rules",
        grounding: "OpenXAI (NeurIPS 2022); Quantus (JMLR 2023)",
        test: "tests/test_benchmark_reporting.py",
        roadmap: "Enables offline camera-ready scientific reporting across all benchmarks."
      },

      // ZONE 1: ENGINE & PRIORITY QUEUE
      {
        id: "hawkes-engine",
        zone: "zone-engine",
        tag: "MTPP PROCESS",
        tagColor: "color-engine",
        title: "Recursive Circadian Hawkes Engine",
        file: "fraudx_synthesizer/hawkes.py:1-488",
        x: 700, y: 200, w: 440,
        desc: "Marked Temporal Point Process (MTPP) modeling endogenous shopping sprees and botnet card-testing bursts. Uses O(1) recursive state tracking enabling exact Ogata thinning at >=50k tx/sec.",
        formula: "lambda*(t) = mu_0 * phi(t) + sum alpha * exp(-beta * (t - t_i))\\nR_k = 1 + R_{k-1} * exp(-beta * dt)\\nSubcritical stability: eta = alpha / beta < 1.0",
        chips: ["MTPP Ogata Thinning", "O(1) Recursive Memory", "Circadian von Mises", "t_half=250s"],
        inputs: "Cardholder HawkesParameters (mu_0, alpha, beta, phi_max), simulation timeline",
        outputs: "Stochastically excited inter-arrival times for legitimate sprees and bot bursts",
        grounding: "Hawkes Point Processes in Financial Econometrics; Fed shopping spree clusters",
        test: "tests/test_hawkes_engine.py",
        roadmap: "Step 7: Differential evolution parameter fitting for cohort Hawkes profiles."
      },
      {
        id: "world-env",
        zone: "zone-engine",
        tag: "SPATIAL WORLD",
        tagColor: "color-engine",
        title: "WorldEnvironment & Spatial Coordinates",
        file: "fraudx_synthesizer/world.py:1-339",
        x: 700, y: 580, w: 440,
        desc: "Generates merchant ecosystem across 150+ coordinates in US/India metros with empirical MCC distributions (grocery, gas, luxury, crypto, travel) and Haversine distance calculations.",
        formula: "d = 2R * arcsin(sqrt(sin^2(dlat/2) + cos(lat1)*cos(lat2)*sin^2(dlon/2)))\\nKinematic velocity v = d / dt <= 900 km/h",
        chips: ["150+ Merchants", "MCC Taxonomy", "Haversine Kinematics", "Dual-Region Metro"],
        inputs: "Metro center coordinates (US NY/SF or IN Mumbai/Delhi), merchant seed",
        outputs: "Merchant profiles with spatial coordinates, MCC, acquirer BINs, and gateway tiers",
        grounding: "ISO 18245 Merchant Category Codes; physical travel limits",
        test: "tests/test_synthesizer/test_kinematics.py",
        roadmap: "Phase 1 Property Test: Exhaustive pair scan enforcing v <= 900 km/h."
      },
      {
        id: "priority-queue",
        zone: "zone-engine",
        tag: "CORE EVENT BUS",
        tagColor: "color-engine",
        title: "heapq Priority Queue & Event Loop",
        file: "fraudx_synthesizer/engine.py:1-250",
        x: 700, y: 960, w: 440,
        desc: "The beating heart of FraudxAI. 64-bit microsecond integer priority queue guaranteeing strict chronological monotonicity without floating-point drift or temporal paradoxes.",
        formula: "heappush / heappop on 6-tuples:\\n(timestamp_us, priority, seq_counter, event_type, card_id, payload)\\nInvariant: forall i, t_i <= t_{i+1}",
        chips: ["64-bit Microseconds", "itertools.count()", "Zero Paradoxes", "8 Event Types"],
        inputs: "Scheduled events across cards, fraudsters, settlements, and clearing batches",
        outputs: "Strictly ordered event stream dispatched to agent and bank handlers",
        grounding: "Discrete-event simulation systems engineering; ISO 8583 settlement lifecycles",
        test: "tests/test_synthesizer/test_reproducibility.py",
        roadmap: "Phase 1 Property Test: Temporal monotonicity verification over 100k events."
      },

      // ZONE 2: AGENTS & CLOSED-LOOP FEEDBACK
      {
        id: "cardholder-agent",
        zone: "zone-agents",
        tag: "BEHAVIORAL AGENT",
        tagColor: "color-agent",
        title: "CardholderProfile State Machine",
        file: "fraudx_synthesizer/agents.py:1-350",
        x: 1340, y: 200, w: 460,
        desc: "Models authentic human cardholders across 16 card products and 7 Fed cohorts. Transitions through Homestead, Commuting, Shopping Spree, Domestic/Intl Travel, Alerted, and Frozen.",
        formula: "State transitions governed by diurnal Markov transition matrices\\nSpend amounts sampled from spliced LogNormal-GPD marginals",
        chips: ["16 Card Products", "FSM States", "Authentic Hard Negatives", "Dhanteras Gold"],
        inputs: "Hawkes arrival ticks, bank alert notifications, travel plans",
        outputs: "Proposed legitimate candidate transactions with authentic device telemetry",
        grounding: "Federal Reserve DCPC 2023; RBI RuPay card product specifications",
        test: "tests/test_synthesizer/test_temporal_and_circadian_dynamics.py",
        roadmap: "Tier 2: Calibrate ticket size means against monthly RBI Payment System Indicators."
      },
      {
        id: "fraudster-agent",
        zone: "zone-agents",
        tag: "ADVERSARIAL AGENT",
        tagColor: "color-agent",
        title: "AdaptiveFraudsterAgent & Closed Loop",
        file: "fraudx_synthesizer/agents.py:351-780",
        x: 1340, y: 640, w: 460,
        desc: "Adaptive adversary executing 10 cybercrime playbooks. Maintains per-card state machines, reacts to bank ISO response codes with bisection decay on ISO 51 and gateway hopping on 3DS challenges.",
        formula: "ISO 51 (Insufficient Funds): Amount <- Amount / 2 (bisection decay)\\n3DS Challenge: Hop to low-friction merchant gateway tier\\nISO 65: Trigger back-off delay (12-24h)",
        chips: ["Adaptive State Machine", "Bisection Decay", "Gateway Hopping", "Silent Baking"],
        inputs: "Compromised credential dossiers, bank ISO 8583 response codes, 3DS challenges",
        outputs: "Adversarial transaction intents mimicking legitimate consumer patterns",
        grounding: "Observed cybercrime modus operandi (Magecart, FIN7, credential stuffing)",
        test: "tests/test_adversarial_adaptation.py",
        roadmap: "Step 7: Optimize adversary mimicry parameter via differential evolution."
      },
      {
        id: "syndicate-registry",
        zone: "zone-agents",
        tag: "THREAT INTEL",
        tagColor: "color-agent",
        title: "SyndicateRegistry & Mule Layering DAG",
        file: "fraudx_synthesizer/syndicates.py:1-597",
        x: 1340, y: 1080, w: 460,
        desc: "Underground cybercrime infrastructure entities: Botnet clusters, FoxIO JA4 TLS signatures, passive p0f OS telemetry, and 3-tier FinCEN/FATF money mule layering DAGs.",
        formula: "Mule Layering DAG:\\nTier 1 Smurfs -> Tier 2 Aggregator LLCs -> Tier 3 Crypto Off-Ramp\\nFoxIO JA4: [SSL_Version]_[Ciphers]_[Extensions]",
        chips: ["3-Tier Mule DAG", "JA4 TLS Signatures", "p0f OS Stacks", "FinCEN/FATF"],
        inputs: "Syndicate campaigns, compromised account dumps, proxy pools",
        outputs: "Persistent threat infrastructure metadata tagged to fraud records",
        grounding: "FinCEN Advisory on Money Mule Schemes; FATF Typologies",
        test: "tests/test_syndicate_ecology_graph.py",
        roadmap: "Enables graph transformer visualization and community detection benchmarks."
      },
      {
        id: "candidate-intent",
        zone: "zone-agents",
        tag: "DECOUPLED CONTRACT",
        tagColor: "color-agent",
        title: "CandidateTransactionIntent Contract",
        file: "fraudx_synthesizer/rails.py:28-64",
        x: 1340, y: 1520, w: 460,
        desc: "Decoupled contract separating agent intent from banking switch evaluation. Enforces strict boundary layer where agents propose intents but cannot directly alter balances.",
        formula: "CandidateTransactionIntent(tx_id, amount, channel, merchant_id, cvv, avs, otp, pin, emv_cryptogram)",
        chips: ["Immutable Contract", "Decoupled Boundary", "Credentials Vector", "Clean Separation"],
        inputs: "Action proposal from Cardholder or AdaptiveFraudster",
        outputs: "Structured authorization request submitted to RailVerifierSwitch",
        grounding: "Separation of concerns in banking switches and core banking systems",
        test: "tests/test_rail_verifier.py",
        roadmap: "Allows external generative models or flows to propose candidate intents safely."
      },

      // ZONE 3: PAYMENT RAILS SWITCH & SOLVENCY
      {
        id: "rail-switch",
        zone: "zone-rails",
        tag: "BANKING SWITCH",
        tagColor: "color-rail",
        title: "RailVerifierSwitch & Solvency Engine",
        file: "fraudx_synthesizer/rails.py:65-350",
        x: 2020, y: 200, w: 440,
        desc: "Institutional boundary switch evaluating multi-party solvency, 3DS 2.x authentication, EMV Bit 55 cryptograms, and issuing ISO 8583 response codes.",
        formula: "Solvency Invariant: Posted_Balance + Amount + Active_Holds <= Credit_Limit\\nISO 8583: 00 (Approved), 05 (Do Not Honor), 51 (NSF), 65 (Ceiling), 82 (CVV)",
        chips: ["ISO 8583 Engine", "Solvency Accounting", "EMV Bit 55 TVR", "3DS 2.x Protocol"],
        inputs: "CandidateTransactionIntent, CardholderProfile, MerchantProfile",
        outputs: "RailVerificationResult (Approved, ISO code, 3DS status, hold placed, interchange)",
        grounding: "ISO 8583 Financial Transaction Message standard; Visa Core Rules",
        test: "tests/test_authorization_calibration.py",
        roadmap: "Phase 1 Property Test: Solvency non-mutation assertion on declined transactions."
      },
      {
        id: "india-rails",
        zone: "zone-rails",
        tag: "REGULATORY RAILS",
        tagColor: "color-rail",
        title: "RBI AFA & Contactless Limits Switch",
        file: "fraudx_synthesizer/rails.py:351-516",
        x: 2020, y: 640, w: 440,
        desc: "Enforces Indian payment rail specifics: RBI Additional Factor of Authentication (AFA/OTP), ₹5,000 PIN-free contactless ceiling, 5-tx counter resets, and CoFT tokenization.",
        formula: "If Channel == 'CP_CONTACTLESS' and Amount <= ₹5,000 and Tx_Count <= 5: PIN-free\\nIf Channel == 'CNP_DOMESTIC' and not OTP_Submitted: Trigger ISO 63 Decline",
        chips: ["RBI AFA / OTP", "₹5,000 Contactless Limit", "5-Tx Pin Reset", "RuPay Rails"],
        inputs: "Indian transaction intent, card PIN-free counter state",
        outputs: "Regulatory compliance decisions and ISO 63 security declines",
        grounding: "RBI Circular DPSS.CO.PD.No.1465/02.14.003/2014-15; July 2026 harmonization",
        test: "tests/test_india_empirical_calibration.py",
        roadmap: "Step 6: CI calibration gates enforcing RBI fraud rate and ticket targets."
      },
      {
        id: "invariants-engine",
        zone: "zone-rails",
        tag: "INVARIANT AUDITOR",
        tagColor: "color-rail",
        title: "invariants.py (Ground-Truth Invariants)",
        file: "fraudx_synthesizer/invariants.py:1-186",
        x: 2020, y: 1080, w: 440,
        desc: "Hard assertions verifying that generated records never violate physical or financial laws: Kinematic speed ceilings (<900 km/h), non-negative balances, and double-entry balance.",
        formula: "assert velocity <= 900.0 km/h (CP transactions)\\nassert sum(Debits) == sum(Credits)\\nassert available_balance >= 0.0",
        chips: ["Zero Teleportation", "Double-Entry Balance", "ISO Syntax Audit", "Hard Veto"],
        inputs: "Generated transaction record",
        outputs: "List of invariant violations (empty list = record passed)",
        grounding: "Anti-Astronaut Mandate Rule 1: physical and financial unit grounding",
        test: "tests/test_synthesizer/test_invariants.py",
        roadmap: "Step 1: Replace YAML regression checks with simulation property tests."
      },

      // ZONE 4: CAUSAL SCM & STREAMING LEDGER
      {
        id: "causal-scm",
        zone: "zone-scm",
        tag: "CAUSAL SCM",
        tagColor: "color-scm",
        title: "Structural Causal Model & Owen Shapley",
        file: "fraudx_synthesizer/causal_scm.py:1-534",
        x: 2660, y: 200, w: 440,
        desc: "Computes exact game-theoretic feature attributions: Owen multilinear Shapley values in logit space and 128-point Gauss-Legendre quadrature in probability space.",
        formula: "sum phi_i^{logit} = z - z_0 (exact efficiency)\\nsum phi_i^{prob} = P(Fraud) - P_0 via 128-point Gauss-Legendre quadrature\\nPearl SCM: X^{CF} = do(Normative)",
        chips: ["Owen Shapley", "128-pt Gauss-Legendre", "Pearlian Counterfactuals", "Efficiency Axiom"],
        inputs: "Transaction features, 30-day Welford moments, baseline profile",
        outputs: "CausalGroundTruth with exact attribution vectors and counterfactual twin restorations",
        grounding: "Aumann-Shapley Theorem; Integrated Gradients (Sundararajan 2017); Pearl (2009)",
        test: "tests/test_synthesizer/test_causal_shapley.py",
        roadmap: "Step 3: Wire canonical attack interventions as primary XAI ground truth."
      },
      {
        id: "streaming-ledger",
        zone: "zone-scm",
        tag: "STREAMING STORE",
        tagColor: "color-scm",
        title: "StreamingLedger (Zero Temporal Leakage)",
        file: "fraudx_synthesizer/ledger.py:1-626",
        x: 2660, y: 640, w: 440,
        desc: "High-performance streaming feature store using Welford's online algorithm. Enforces the zero-leakage read-then-mutate invariant: historical features are computed before mutating card state.",
        formula: "M_k = M_{k-1} + (x - M_{k-1}) / k\\nS_k = S_{k-1} + (x - M_{k-1}) * (x - M_k)\\nFeature extraction precedes state update",
        chips: ["Welford O(1) Updates", "Zero Temporal Leakage", "Read-Then-Mutate", "Velocity Counters"],
        inputs: "Transaction intent, card historical moments",
        outputs: "Leakage-free streaming feature vector (tx_count_1h, avg_amount_30d, z_score_30d)",
        grounding: "Production ML streaming feature store engineering; Welford (1962)",
        test: "tests/test_synthesizer/test_zero_leakage.py",
        roadmap: "Step 2: Cross-seed feature stability validation."
      },
      {
        id: "double-entry",
        zone: "zone-scm",
        tag: "LEDGER ACCOUNTING",
        tagColor: "color-scm",
        title: "DoubleEntryAccountingLedger",
        file: "fraudx_synthesizer/ledger.py:400-626",
        x: 2660, y: 1080, w: 440,
        desc: "Rigorous banking accounting ledger tracking cardholder liability, merchant settlement accounts, interchange fee escrows, and active authorization holds.",
        formula: "Pre-Auth: Hold placed (Available Balance decreased, Posted Balance unchanged)\\nClearing & Settlement: Hold released, Posted Balance debited, Interchange credited",
        chips: ["Dual-Message Rails", "Hold vs Settlement", "Interchange Fee", "Zero Slack"],
        inputs: "Authorization results, clearing events, settlement schedules",
        outputs: "Immutable double-entry balance statements for cardholders and merchants",
        grounding: "Generally Accepted Accounting Principles (GAAP); Visa Clearing System",
        test: "tests/test_synthesizer/test_solvency_accounting.py",
        roadmap: "Guarantees financial conservation of funds across multi-day simulation runs."
      },

      // ZONE 5: FIU OPERATIONAL SUPERVISION & DELAY
      {
        id: "supervision-engine",
        zone: "zone-supervision",
        tag: "SUPERVISION QUEUE",
        tagColor: "color-supervision",
        title: "SupervisionEngine (Daily FIU Queue K)",
        file: "fraudx_synthesizer/stream.py:217-480",
        x: 3300, y: 200, w: 440,
        desc: "Simulates human fraud investigators in retail banks. Implements a daily alert budget K, priority triage ranking (Risk Score, Value-at-Risk), and bifurcated verification latencies.",
        formula: "Top-K Alert Capacity: K in [50, 200] alerts/day\\nPriority Score = Risk_Score * (Amount / 100.0)",
        chips: ["Daily Budget K", "FIU Queue", "Bifurcated Latencies", "Dal Pozzolo 2018"],
        inputs: "Transaction risk score, amount, ground truth label",
        outputs: "SupervisionRecord with point-in-time discovery timestamps and investigation status",
        grounding: "Dal Pozzolo et al. (IEEE TNNLS 2018); Carcillo et al. (AAAI 2018)",
        test: "tests/test_supervision_engine.py",
        roadmap: "Tier 4: Dynamic investigator capacity modeling based on operational shifts."
      },
      {
        id: "bifurcated-latencies",
        zone: "zone-supervision",
        tag: "DELAY DISTRIBUTIONS",
        tagColor: "color-supervision",
        title: "Weibull & LogNormal Latency Models",
        file: "fraudx_synthesizer/stream.py:481-650",
        x: 3300, y: 640, w: 440,
        desc: "Bifurcated feedback delay: Flagged alerts verified rapidly by FIU analysts; unflagged frauds discovered only after monthly statement cycles via chargeback filing.",
        formula: "Fast Review: T_rev ~ Weibull(k=1.45, lambda=18.5h), [0.5h, 48h]\\nDispute Lag: T_cb ~ LogNormal(mu=ln(32d), sigma=0.35), [14d, 120d]",
        chips: ["Weibull Fast (18.5h)", "LogNormal Slow (32d)", "Visa VCR 120d", "Realistic Feedback"],
        inputs: "Investigation status (INVESTIGATED vs DROPPED_CAPACITY / UNREVIEWED)",
        outputs: "Exact point-in-time discovery timestamp discovery_time_seconds",
        grounding: "Visa Claims Resolution (VCR) dispute rules; empirical banking call-center data",
        test: "tests/test_supervision_engine.py",
        roadmap: "Step 6: Calibrate delay distributions against public dispute turnaround surveys."
      },
      {
        id: "dark-fraud",
        zone: "zone-supervision",
        tag: "NON-REPORTING",
        tagColor: "color-supervision",
        title: "Dark Fraud Logistic Non-Reporting",
        file: "fraudx_synthesizer/stream.py:651-713",
        x: 3300, y: 1080, w: 440,
        desc: "Models economic non-reporting behavior: cardholders do not spend 45 minutes on the phone disputing micro-auth card-testing charges below $10. Permanently unobserved fraud.",
        formula: "P(Dark) = 1 / (1 + (Amount / V_0)^gamma)\\nV_0 = $15.00 (USD) / ₹500 (INR), gamma = 2.2",
        chips: ["Micro-Auth Probing", "Unreported Loss", "Economic Threshold", "Dark Curve"],
        inputs: "Transaction amount and currency",
        outputs: "Flag determining whether unflagged fraud remains permanently dark",
        grounding: "Consumer protection economic surveys; micro-probing dark matter",
        test: "tests/test_supervision_engine.py",
        roadmap: "Calibrate V_0 and gamma against retail banking dispute abandonment data."
      },

      // ZONE 6: PREQUENTIAL STREAMING EVALUATION
      {
        id: "prequential-evaluator",
        zone: "zone-eval",
        tag: "STREAMING EVAL",
        tagColor: "color-eval",
        title: "PrequentialStreamingEvaluator",
        file: "fraudx_synthesizer/evaluation.py:550-877",
        x: 3940, y: 200, w: 440,
        desc: "Rolling predict-then-train streaming evaluation loop. Enforces the delay-gap invariant: transactions within the pending feedback window [T - tau, T] are excluded from training.",
        formula: "1. Predict on test window [T, T + W_test]\\n2. Retrain model on verified records up to T - tau_delay\\n3. Advance T by retrain interval Delta_t",
        chips: ["Predict-Then-Train", "Delay Gap Exclusion", "Rolling Retraining", "Streaming Metrics"],
        inputs: "Streaming transaction records, point-in-time supervision records",
        outputs: "PrequentialBenchmarkReport with daily triage curves and PR-AUC",
        grounding: "Dal Pozzolo et al. (IEEE TNNLS 2018); Le Borgne et al. (2021)",
        test: "tests/test_prequential_benchmark.py",
        roadmap: "Step 8: Implement temporal self-TSTR generalization benchmark."
      },
      {
        id: "streaming-metrics",
        zone: "zone-eval",
        tag: "TRIAGE METRICS",
        tagColor: "color-eval",
        title: "StreamingMetricTracker (P@K, CP@K, DR@K)",
        file: "fraudx_synthesizer/evaluation.py:151-380",
        x: 3940, y: 640, w: 440,
        desc: "Operational banking triage metrics aligning with investigator capacity: Alert Precision (P@K), Card Precision (CP@K), Dollar Recall (DR@K), and Net Cost Savings.",
        formula: "P@K = TP_alerts / K\\nCP@K = TP_cards / K\\nDR@K = Caught_Dollar_Loss / Total_Fraud_Loss\\nCost Savings = Recovered_Loss - (K * C_investigation)",
        chips: ["Alert Precision P@K", "Card Precision CP@K", "Dollar Recall DR@K", "Cost Utility"],
        inputs: "Ranked daily risk scores, ground truth, transaction amounts, cost matrix",
        outputs: "Daily operational triage curves across multiple capacity budgets K in [10, 200]",
        grounding: "Operational fraud detection metrics; Chenyu Wu (2026) dollar metric audit",
        test: "tests/test_prequential_benchmark.py",
        roadmap: "Enables bank executive triage curve visualization in camera-ready reports."
      },
      {
        id: "drift-auditor",
        zone: "zone-eval",
        tag: "DRIFT AUDITOR",
        tagColor: "color-eval",
        title: "StreamingDriftAuditor (KS Test & PSI)",
        file: "fraudx_synthesizer/evaluation.py:381-549",
        x: 3940, y: 1080, w: 440,
        desc: "Detects prediction drift and feature attribution shifts in the stream using two-sample Kolmogorov-Smirnov tests and Population Stability Index (PSI) with alarm thresholds.",
        formula: "Two-sample KS: Alarm if p-value < 0.01\\nPSI = sum (Actual% - Expected%) * ln(Actual% / Expected%)\\nPSI >= 0.25 indicates critical concept drift",
        chips: ["2-Sample KS Test", "PSI Drift Tripwire", "Alarm Thresholds", "Concept Drift"],
        inputs: "Reference score distribution (W_train) vs current window distribution (W_test)",
        outputs: "Daily KS p-values, PSI drift metrics, and urgent retraining triggers",
        grounding: "Banking model risk management (SR 11-7); concept drift adaptation literature",
        test: "tests/test_prequential_benchmark.py",
        roadmap: "Triggers automated rolling model adaptation in production streaming pipelines."
      },

      // ZONE 7: BENCHMARK REPORTING & CLI
      {
        id: "benchmark-reporter",
        zone: "zone-reporter",
        tag: "CAMERA-READY",
        tagColor: "color-spec",
        title: "BenchmarkReporter & Camera-Ready Figures",
        file: "fraudx_synthesizer/benchmark_reporter.py:1-650",
        x: 4580, y: 200, w: 440,
        desc: "Generates publication-grade scientific figures and offline HTML dashboards. Enforces Tol colorblind palettes and IEEE/ACM/NeurIPS dimension presets using headless matplotlib.",
        formula: "Figures 1-4: Rolling PR-AUC, Multi-K Triage curves, Net Dollar Savings, KS/PSI Drift\\nIEEE single-col 3.5in, double-col 7.0in @ 300 DPI",
        chips: ["Tol Colorblind Safe", "Headless Agg", "IEEE/ACM Standards", "Offline HTML"],
        inputs: "Prequential report, XAI attribution evaluations, fidelity matrices",
        outputs: "High-resolution camera-ready figures (PNG/PDF) and standalone HTML report",
        grounding: "NeurIPS Datasets & Benchmarks Track; JMLR Machine Learning Open Source Software",
        test: "tests/test_benchmark_reporting.py",
        roadmap: "Enables instant publication-grade outputs for papers and research audits."
      },
      {
        id: "fidelity-privacy",
        zone: "zone-reporter",
        tag: "STATISTICAL FIDELITY",
        tagColor: "color-spec",
        title: "Frobenius Error & Shadow MIA Attack",
        file: "fraudx_synthesizer/benchmark_reporter.py:651-1100",
        x: 4580, y: 640, w: 440,
        desc: "Replaces metric literals with empirical evaluations: Normalized Spearman rank Frobenius matrix error E_frob across partitions, and shadow Distance-to-Closest-Record (DCR) MIA ROC-AUC.",
        formula: "E_frob = || R_syn - R_ref ||_F / (d * (d - 1))\\nShadow MIA: Logistic regression on DCR distance to closest record",
        chips: ["Spearman Frobenius", "Shadow MIA ROC-AUC", "DCR Privacy", "Independent Fidelity"],
        inputs: "Synthetic transaction partition vs independent validation partition",
        outputs: "Empirical correlation fidelity error and membership inference privacy risk score",
        grounding: "Tabular privacy and synthetic data evaluation standards (Stadler 2022)",
        test: "tests/test_benchmark_reporting.py",
        roadmap: "Step 9: SDMetrics-compatible standalone quality reporting module."
      },
      {
        id: "unified-cli",
        zone: "zone-reporter",
        tag: "UNIFIED CLI",
        tagColor: "color-spec",
        title: "cli.py (Command-Line Interface)",
        file: "fraudx_synthesizer/cli.py:1-680",
        x: 4580, y: 1080, w: 440,
        desc: "Unified CLI orchestrating headless generation, streaming emission, tripartite benchmarking, and publication report compilation.",
        formula: "Commands:\\nfraudx generate -n 100000 --region US|IN\\nfraudx benchmark run --w-train 60 --k-daily 50\\nfraudx report --format html,json",
        chips: ["CLI Engine", "Argparse Subcommands", "Streaming Daemon", "Batch Mode"],
        inputs: "Command-line flags and parameters",
        outputs: "Generated CSV/Parquet ledgers, streaming stdout/REST dispatch, HTML reports",
        grounding: "Production CLI developer ergonomics; headless CI/CD execution",
        test: "tests/test_benchmark_reporting.py",
        roadmap: "Step 12: Add `fraudx validate` subcommand for one-shot quality certification."
      },

      // ZONE 8: FUTURE ROADMAP
      {
        id: "roadmap-p1-s1",
        zone: "zone-roadmap",
        tag: "PHASE 1 (WEEK 1)",
        tagColor: "color-roadmap",
        title: "Step 1: Simulation-Based Property Tests",
        file: "tests/test_synthesizer/test_simulation_properties.py",
        x: 120, y: 2880, w: 440,
        desc: "Replaces config regression checks with simulation property tests: scipy.stats.binomtest on diurnal nocturnal ratio (<4.5%), exhaustive velocity pair scan (<=900 km/h), and decline solvency non-mutation.",
        formula: "binomtest(k, n, p=0.045, alternative='less')\\nClopper-Pearson 99% CI for fraud prevalence",
        chips: ["Simulation Properties", "scipy.stats.binomtest", "Kinematic Invariant", "Solvency Invariant"],
        inputs: "SimulationEngine batches across seeds 42, 7, 99 for US and IN regions",
        outputs: "Rigorous property test assertions proving behavioral correctness",
        grounding: "Property-based software testing; Hypothesis / QuickCheck methodology",
        test: "tests/test_synthesizer/test_simulation_properties.py (Planned)",
        roadmap: "Phase 1, Step 1: Transforms credibility from config assertions to behavioral proofs."
      },
      {
        id: "roadmap-p1-s2",
        zone: "zone-roadmap",
        tag: "PHASE 1 (WEEK 1)",
        tagColor: "color-roadmap",
        title: "Step 2: Cross-Seed Distributional Stability",
        file: "tests/test_synthesizer/test_distributional_stability.py",
        x: 640, y: 2880, w: 440,
        desc: "Proves that independent random seeds produce statistically indistinguishable distributions using two-sample Kolmogorov-Smirnov tests on log-amounts (D < 0.08) and Chi-squared contingency on channel mix.",
        formula: "ks_2samp(log_amounts_a, log_amounts_b) -> D < 0.08\\nchi2_contingency(channel_counts) -> p > 0.01",
        chips: ["2-Sample KS Stability", "Chi-Squared Channel Mix", "Cross-Seed Robustness"],
        inputs: "Batches from seeds 42 and 99 under identical configurations",
        outputs: "Statistical equivalence certificates across pseudo-random generator seeds",
        grounding: "Non-parametric statistical hypothesis testing; SDV benchmark standards",
        test: "tests/test_synthesizer/test_distributional_stability.py (Planned)",
        roadmap: "Phase 1, Step 2: Establishes distributional consistency as a hard CI gate."
      },
      {
        id: "roadmap-p1-s3",
        zone: "zone-roadmap",
        tag: "PHASE 1 (WEEK 1)",
        tagColor: "color-roadmap",
        title: "Step 3: True Interventional XAI Ground Truth",
        file: "fraudx_synthesizer/benchmark.py (XAIBenchmarkHarness)",
        x: 1160, y: 2880, w: 440,
        desc: "Sets CANONICAL_ATTACK_INTERVENTIONS as the primary ground truth. Evaluates explainers against what the simulation literally manipulated rather than against the heuristic bank scorer's weights.",
        formula: "Ground Truth Vector: delta_j = |x_fraud - x_baseline| for j in Intervened_Features\\nKendall tau and Top-k Precision/Recall evaluated against true interventions",
        chips: ["Interventional Ground Truth", "No Scorer Circularity", "Exact Feature Deltas"],
        inputs: "Counterfactual input deltas and scenario tag interventions",
        outputs: "Interventional rank correlation metrics (interventional_kendall_tau)",
        grounding: "Pearl (2009) Interventional Causality; CausalProfiler (ICML 2026)",
        test: "tests/test_synthesizer/test_intervention_ground_truth.py",
        roadmap: "Phase 1, Step 3: Eliminates XAI benchmark circularity permanently."
      },
      {
        id: "roadmap-p2-s4",
        zone: "zone-roadmap",
        tag: "PHASE 2 (WEEKS 2-3)",
        tagColor: "color-roadmap",
        title: "Step 4 & 5: US Public Calibration Targets",
        file: "spec/09_us_calibration_targets.yaml & calibration.py",
        x: 1680, y: 2880, w: 440,
        desc: "Adds official US public aggregate targets: Federal Reserve Payments Study 2022 credit fraud rate (12.5 bps), Visa Q3 authorization approval rate (88.3%), and Fed DCPC mean ticket ($98).",
        formula: "Approval Rate Target: 0.883 (+-5% relative tolerance)\\nMean Credit Ticket: $98.00 (+-30% tolerance)\\nCNP Share by Value: 0.62",
        chips: ["Fed Payments Study 2022", "Visa Earnings Q3", "Fed DCPC $98 Ticket", "Gated CI"],
        inputs: "Simulated US batch transaction records",
        outputs: "Calibration report with gated pass/fail evaluation",
        grounding: "Federal Reserve Payments Study; Visa Inc. quarterly operational telemetry",
        test: "tests/test_us_empirical_calibration.py",
        roadmap: "Phase 2, Steps 4 & 5: Bridges specification grounding to published economic empirical data."
      },
      {
        id: "roadmap-p2-s7",
        zone: "zone-roadmap",
        tag: "PHASE 2 (WEEKS 2-3)",
        tagColor: "color-roadmap",
        title: "Step 7: Global Parameter Optimizer",
        file: "fraudx_synthesizer/parameter_optimizer.py",
        x: 2200, y: 2880, w: 440,
        desc: "Replaces hand-tuned parameters with black-box optimization: uses scipy.optimize.differential_evolution to fit adversary mimicry and Hawkes arrival scales against public targets.",
        formula: "Loss = sum ((Observed_k - Target_k) / Target_k)^2\\nOptimize over Bounds: mimicry in [0.30, 0.85], hawkes_scale in [0.5, 2.0]",
        chips: ["differential_evolution", "Black-Box Calibration", "Automated Parameter Fitting"],
        inputs: "SimulationEngine black-box generator and target profiles",
        outputs: "Fitted parameter dictionary minimizing distance to published bank statistics",
        grounding: "Gradient-free simulation optimization; CMA-ES / Differential Evolution",
        test: "fraudx_synthesizer/parameter_optimizer.py (Planned)",
        roadmap: "Phase 2, Step 7: Eliminates arbitrary parameter guesses mathematically."
      },
      {
        id: "roadmap-p3-s8",
        zone: "zone-roadmap",
        tag: "PHASE 3 (WEEKS 3-4)",
        tagColor: "color-roadmap",
        title: "Step 8: Temporal Self-TSTR Benchmark",
        file: "fraudx_synthesizer/benchmark.py (TripartiteBenchmarkHarness)",
        x: 2720, y: 2880, w: 440,
        desc: "Train on early data, test on late data. Measures temporal stability and concept consistency. Ensures that models trained on week 1 generalize to predict week 4 fraud.",
        formula: "Split stream at 60% time mark\\nTrain LightGBM on T_early, evaluate PR-AUC on T_late\\nAcceptance: Late PR-AUC within 15% of same-window baseline",
        chips: ["Temporal Self-TSTR", "Early-to-Late Generalization", "Temporal Stability"],
        inputs: "Time-ordered synthetic transaction batches",
        outputs: "Temporal TSTR PR-AUC and generalization utility gap",
        grounding: "Train-Synthetic-Test-Real methodology (Esteban 2017); Jesus (2022)",
        test: "tests/test_tripartite_benchmark.py",
        roadmap: "Phase 3, Step 8: Prepares harness for seamless drop-in of real bank data."
      },
      {
        id: "roadmap-p3-s9",
        zone: "zone-roadmap",
        tag: "PHASE 3 (WEEKS 3-4)",
        tagColor: "color-roadmap",
        title: "Step 9: Standalone Quality Reporting",
        file: "fraudx_synthesizer/quality_report.py",
        x: 3240, y: 2880, w: 440,
        desc: "Standalone SDMetrics-compatible statistical scoring without external heavyweight dependencies: pairwise L2 internal diversity, per-column Shannon entropy, and Bhattacharyya class overlap.",
        formula: "Internal Diversity: Mean L2 distance across standardized pairs\\nPer-Column Entropy: H(X) = -sum p_i * log2(p_i)\\nBhattacharyya Overlap: BC = sum sqrt(p_fraud * p_legit)",
        chips: ["L2 Diversity", "Shannon Entropy", "Bhattacharyya Overlap", "SDMetrics Compatible"],
        inputs: "Synthetic transaction feature matrices",
        outputs: "QualityReport dictionary containing diversity, entropy, and class separability",
        grounding: "Synthetic data evaluation metrics; Bhattacharyya distance",
        test: "tests/test_benchmark_reporting.py",
        roadmap: "Phase 3, Step 9: Integrated into unified `fraudx validate` CLI command."
      },
      {
        id: "roadmap-p4-s10",
        zone: "zone-roadmap",
        tag: "PHASE 4 (MONTHS 2-3)",
        tagColor: "color-roadmap",
        title: "Step 10: RealNVP Normalizing Flow Training",
        file: "fraudx_synthesizer/flow_trainer.py",
        x: 3760, y: 2880, w: 440,
        desc: "Trains the existing ConditionalRealNVPFlow on simulator output via maximum likelihood negative log-likelihood (NLL) optimization, turning the algebraic placeholder into a true density estimator.",
        formula: "Loss = -E_{x ~ p_data}[ log p_U(f(x; c)) + log |det J_f(x; c)| ]\\nVectorized AffineCouplingLayer parameter updates",
        chips: ["NLL Flow Training", "Trained RealNVP", "Invertible Diffeomorphism"],
        inputs: "Encoded transaction features (X) and conditioning contexts (C)",
        outputs: "Trained flow checkpoint capable of exact density estimation and sampling",
        grounding: "Normalizing Flows for Tabular Data; RealNVP (Dinh 2016)",
        test: "tests/test_invertible_dscm.py",
        roadmap: "Phase 4, Step 10: Unlocks trained invertible generative modeling."
      },
      {
        id: "roadmap-p4-s11",
        zone: "zone-roadmap",
        tag: "PHASE 4 (MONTHS 2-3)",
        tagColor: "color-roadmap",
        title: "Step 11: Constrained Hybrid Flow Sampler",
        file: "fraudx_synthesizer/hybrid_sampler.py",
        x: 4280, y: 2880, w: 440,
        desc: "Hybrid simulation + generative synthesis: Trained flow proposes candidate transaction residuals, and invariants.py verifies/rejects candidates violating physical or regulatory rules.",
        formula: "x_candidate = Flow.inverse(u, context), u ~ N(0, I)\\nReject if verify_transaction_invariants(x_candidate) != []\\nFallback to discrete-event simulator on rejection",
        chips: ["Constrained Rejection Sampling", "Hybrid Architecture", "Invariant Guardrails"],
        inputs: "Latent noise vectors u and cardholder conditioning contexts",
        outputs: "Realistic transactions with continuous fine-grained residual noise",
        grounding: "Constrained Generative Modeling; Neuro-symbolic synthesis",
        test: "fraudx_synthesizer/hybrid_sampler.py (Planned)",
        roadmap: "Phase 4, Step 11: Delivers the ultimate hybrid simulation + generative paradigm."
      }
    ];

    // -------------------------------------------------------------
    // 3. DIRECTED CONNECTION CONDUITS (EDGES)
    // -------------------------------------------------------------
    const EDGES = [
      // Spec connections
      { from: "spec-loader", to: "hawkes-engine", label: "Persona Arrival Rates", color: "var(--cyan)" },
      { from: "spec-loader", to: "cardholder-agent", label: "16 Card Products", color: "var(--cyan)" },
      { from: "spec-loader", to: "fraudster-agent", label: "10 Cybercrime Playbooks", color: "var(--cyan)" },
      { from: "spec-loader", to: "rail-switch", label: "Solvency & Limits", color: "var(--cyan)" },
      { from: "spec-loader", to: "supervision-engine", label: "Supervision Params", color: "var(--cyan)" },
      { from: "spec-loader", to: "prequential-evaluator", label: "Evaluation Windows", color: "var(--cyan)" },

      // Engine & Queue connections
      { from: "hawkes-engine", to: "priority-queue", label: "lambda*(t) Arrivals", color: "var(--indigo)" },
      { from: "world-env", to: "priority-queue", label: "Spatial MIDs & MCCs", color: "var(--indigo)" },
      { from: "priority-queue", to: "cardholder-agent", label: "Scheduled Events", color: "var(--indigo)" },
      { from: "priority-queue", to: "fraudster-agent", label: "Attack Triggers", color: "var(--indigo)" },

      // Agents to Intent
      { from: "cardholder-agent", to: "candidate-intent", label: "Legitimate Proposal", color: "var(--amber)" },
      { from: "fraudster-agent", to: "candidate-intent", label: "Adversarial Attack", color: "var(--amber)" },
      { from: "syndicate-registry", to: "fraudster-agent", label: "Mule & JA4 Pools", color: "var(--amber)" },

      // Intent to Rails
      { from: "candidate-intent", to: "rail-switch", label: "Authorization Request", color: "var(--emerald)" },
      { from: "india-rails", to: "rail-switch", label: "AFA & Contactless Limits", color: "var(--emerald)" },
      { from: "invariants-engine", to: "rail-switch", label: "Kinematic Veto", color: "var(--emerald)" },

      // Closed-Loop Feedback
      { from: "rail-switch", to: "fraudster-agent", label: "ISO 51 (Bisection Decay)", color: "var(--amber)", flow: true },
      { from: "rail-switch", to: "fraudster-agent", label: "3DS Challenge (Gateway Hop)", color: "var(--amber)", flow: true },
      { from: "rail-switch", to: "hawkes-engine", label: "ISO 00 (Excites Memory)", color: "var(--indigo)", flow: true },

      // Rails to Causal SCM & Ledger
      { from: "rail-switch", to: "causal-scm", label: "Authorized Records", color: "var(--purple)" },
      { from: "causal-scm", to: "streaming-ledger", label: "Counterfactual Deltas", color: "var(--purple)" },
      { from: "streaming-ledger", to: "double-entry", label: "Balanced Accounting", color: "var(--purple)" },

      // Ledger to Supervision
      { from: "streaming-ledger", to: "supervision-engine", label: "Transaction Stream", color: "var(--rose)" },
      { from: "bifurcated-latencies", to: "supervision-engine", label: "Weibull / LogNormal Delay", color: "var(--rose)" },
      { from: "dark-fraud", to: "supervision-engine", label: "Dark Matter Filter", color: "var(--rose)" },

      // Supervision to Prequential Evaluation
      { from: "supervision-engine", to: "prequential-evaluator", label: "Delayed Matured Labels", color: "#F472B6" },
      { from: "streaming-metrics", to: "prequential-evaluator", label: "P@K / DR@K Tracking", color: "#F472B6" },
      { from: "drift-auditor", to: "prequential-evaluator", label: "KS Drift / PSI Alarms", color: "#F472B6" },

      // Evaluation to Reporting
      { from: "prequential-evaluator", to: "benchmark-reporter", label: "Prequential Report", color: "var(--cyan)" },
      { from: "fidelity-privacy", to: "benchmark-reporter", label: "Spearman & Shadow MIA", color: "var(--cyan)" },
      { from: "benchmark-reporter", to: "unified-cli", label: "Camera-Ready Figures", color: "var(--cyan)" },

      // Roadmap enhancements
      { from: "roadmap-p1-s1", to: "invariants-engine", label: "Upgrades to Simulation Properties", color: "#2DD4BF", flow: true },
      { from: "roadmap-p1-s2", to: "streaming-ledger", label: "Adds Cross-Seed Stability", color: "#2DD4BF", flow: true },
      { from: "roadmap-p1-s3", to: "causal-scm", label: "Replaces Scorer with True DGP", color: "#2DD4BF", flow: true },
      { from: "roadmap-p2-s4", to: "spec-personas", label: "Anchors to Fed Payments Study", color: "#2DD4BF", flow: true },
      { from: "roadmap-p2-s7", to: "hawkes-engine", label: "Fits Parameters via DE", color: "#2DD4BF", flow: true },
      { from: "roadmap-p3-s8", to: "prequential-evaluator", label: "Validates Temporal Generalization", color: "#2DD4BF", flow: true },
      { from: "roadmap-p4-s10", to: "candidate-intent", label: "Proposes Generative Residuals", color: "#2DD4BF", flow: true }
    ];

    // -------------------------------------------------------------
    // 4. PAN & ZOOM INFINITE CANVAS ENGINE
    // -------------------------------------------------------------
    const viewport = document.getElementById('viewport');
    const world = document.getElementById('world');
    const edgeSvg = document.getElementById('edge-svg');
    const zonesContainer = document.getElementById('zones-container');
    const nodesContainer = document.getElementById('nodes-container');
    const badgesContainer = document.getElementById('badges-container');
    const minimapViewport = document.getElementById('minimap-viewport');
    const minimapSvg = document.getElementById('minimap-svg');
    const zoomIndicator = document.getElementById('zoom-indicator');

    let panX = 40;
    let panY = 40;
    let zoom = 0.55; // Initial zoom to show a healthy overview
    let isPanning = false;
    let startX = 0, startY = 0;
    let selectedNodeId = null;

    function updateTransform() {
      world.style.transform = `translate3d(${panX}px, ${panY}px, 0px) scale(${zoom})`;
      zoomIndicator.textContent = Math.round(zoom * 100) + "%";

      // Update minimap red rectangle
      const vWidth = window.innerWidth / zoom;
      const vHeight = window.innerHeight / zoom;
      const vLeft = -panX / zoom;
      const vTop = -panY / zoom;

      minimapViewport.setAttribute('x', Math.max(0, vLeft));
      minimapViewport.setAttribute('y', Math.max(0, vTop));
      minimapViewport.setAttribute('width', Math.min(6000, vWidth));
      minimapViewport.setAttribute('height', Math.min(4400, vHeight));
    }

    // Mouse drag pan
    viewport.addEventListener('mousedown', (e) => {
      if (e.target.closest('.node-card') || e.target.closest('#inspector') || e.target.closest('.hud-top') || e.target.closest('.hud-bottom-left') || e.target.closest('#minimap-container')) return;
      isPanning = true;
      viewport.classList.add('panning');
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    });

    window.addEventListener('mousemove', (e) => {
      if (!isPanning) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateTransform();
    });

    window.addEventListener('mouseup', () => {
      isPanning = false;
      viewport.classList.remove('panning');
    });

    // Cursor-centered zoom
    viewport.addEventListener('wheel', (e) => {
      if (e.target.closest('#inspector')) return;
      e.preventDefault();

      const rect = viewport.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      const worldX = (mouseX - panX) / zoom;
      const worldY = (mouseY - panY) / zoom;

      const zoomFactor = Math.exp(-e.deltaY * 0.0018);
      const newZoom = Math.min(Math.max(zoom * zoomFactor, 0.15), 2.8);

      panX = mouseX - worldX * newZoom;
      panY = mouseY - worldY * newZoom;
      zoom = newZoom;

      updateTransform();
    }, { passive: false });

    // Zoom buttons
    function zoomIn() {
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      const wx = (cx - panX) / zoom;
      const wy = (cy - panY) / zoom;
      zoom = Math.min(zoom * 1.25, 2.8);
      panX = cx - wx * zoom;
      panY = cy - wy * zoom;
      updateTransform();
    }
    function zoomOut() {
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      const wx = (cx - panX) / zoom;
      const wy = (cy - panY) / zoom;
      zoom = Math.max(zoom / 1.25, 0.15);
      panX = cx - wx * zoom;
      panY = cy - wy * zoom;
      updateTransform();
    }
    function resetZoom() {
      zoom = 1.0;
      panX = 60;
      panY = 60;
      updateTransform();
    }
    function fitView() {
      const vW = window.innerWidth;
      const vH = window.innerHeight;
      const scaleX = vW / 5400;
      const scaleY = vH / 4200;
      zoom = Math.min(scaleX, scaleY) * 0.95;
      panX = (vW - 5400 * zoom) / 2;
      panY = (vH - 4200 * zoom) / 2;
      updateTransform();
    }

    function smoothPanTo(targetX, targetY, targetZoom = 0.85) {
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      const endPanX = cx - targetX * targetZoom;
      const endPanY = cy - targetY * targetZoom;

      const startPX = panX;
      const startPY = panY;
      const startZ = zoom;
      const startTime = performance.now();
      const duration = 500;

      function step(now) {
        const progress = Math.min((now - startTime) / duration, 1.0);
        const ease = 0.5 - Math.cos(progress * Math.PI) / 2;
        panX = startPX + (endPanX - startPX) * ease;
        panY = startPY + (endPanY - startPY) * ease;
        zoom = startZ + (targetZoom - startZ) * ease;
        updateTransform();
        if (progress < 1.0) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }

    function jumpToCluster(zoneId) {
      if (!zoneId) return;
      const zone = ZONES.find(z => z.id === zoneId);
      if (!zone) return;
      smoothPanTo(zone.x + zone.w / 2, zone.y + zone.h / 2, zone.id === 'zone-roadmap' ? 0.35 : 0.65);
    }

    // -------------------------------------------------------------
    // 5. RENDER ZONES, NODES, EDGES, AND MINIMAP
    // -------------------------------------------------------------
    function renderCanvas() {
      // 1. Render Zones
      zonesContainer.innerHTML = '';
      const minimapZonesGroup = document.getElementById('minimap-zones');
      minimapZonesGroup.innerHTML = '';

      ZONES.forEach(z => {
        const el = document.createElement('div');
        el.className = 'zone-box';
        el.style.left = z.x + 'px';
        el.style.top = z.y + 'px';
        el.style.width = z.w + 'px';
        el.style.height = z.h + 'px';
        el.style.borderColor = z.color;

        const label = document.createElement('div');
        label.className = 'zone-label';
        label.style.borderColor = z.color;
        label.style.color = z.color;
        label.textContent = z.title;
        el.appendChild(label);
        zonesContainer.appendChild(el);

        // Minimap Zone
        const mRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        mRect.setAttribute('x', z.x);
        mRect.setAttribute('y', z.y);
        mRect.setAttribute('width', z.w);
        mRect.setAttribute('height', z.h);
        mRect.setAttribute('fill', 'rgba(255,255,255,0.03)');
        mRect.setAttribute('stroke', 'rgba(255,255,255,0.15)');
        minimapZonesGroup.appendChild(mRect);
      });

      // 2. Render Nodes
      nodesContainer.innerHTML = '';
      const minimapNodesGroup = document.getElementById('minimap-nodes');
      minimapNodesGroup.innerHTML = '';

      NODES.forEach(n => {
        const card = document.createElement('div');
        card.className = 'node-card';
        card.id = 'node-' + n.id;
        card.style.left = n.x + 'px';
        card.style.top = n.y + 'px';
        card.style.width = n.w + 'px';

        card.innerHTML = `
          <div class="port-in"></div>
          <div class="port-out"></div>
          <div class="node-header">
            <span class="node-tag ${n.tagColor}">${n.tag}</span>
            <span class="node-file" title="${n.file}">${n.file.split('/')[1] || n.file}</span>
          </div>
          <div class="node-body">
            <div class="node-title">${n.title}</div>
            <div class="node-desc">${n.desc}</div>
            <div class="node-formula">${n.formula.split('\\n')[0]}</div>
            <div class="node-chips">
              ${n.chips.map(c => `<span class="node-chip">${c}</span>`).join('')}
            </div>
          </div>
        `;

        card.addEventListener('click', (e) => {
          e.stopPropagation();
          selectNode(n.id);
        });

        nodesContainer.appendChild(card);

        // Minimap node representation
        const mNode = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        mNode.setAttribute('x', n.x);
        mNode.setAttribute('y', n.y);
        mNode.setAttribute('width', n.w);
        mNode.setAttribute('height', 160);
        mNode.setAttribute('fill', 'rgba(56,189,248,0.7)');
        mNode.setAttribute('rx', 20);
        minimapNodesGroup.appendChild(mNode);
      });

      // 3. Render Edges & Badges
      renderEdges();
      updateTransform();
    }

    function renderEdges() {
      edgeSvg.innerHTML = '';
      badgesContainer.innerHTML = '';

      EDGES.forEach((e, idx) => {
        const fromNode = NODES.find(n => n.id === e.from);
        const toNode = NODES.find(n => n.id === e.to);
        if (!fromNode || !toNode) return;

        // Calculate port positions
        // Default: from right port of fromNode to left port of toNode
        let x1 = fromNode.x + fromNode.w;
        let y1 = fromNode.y + 110;
        let x2 = toNode.x;
        let y2 = toNode.y + 110;

        // If toNode is below or behind, adjust ports
        let dx = Math.abs(x2 - x1) * 0.45;
        if (dx < 60) dx = 120;

        let pathD;
        if (x2 < x1) {
          // Backward / closed-loop feedback arc
          const curveDrop = Math.max(y1, y2) + 140;
          pathD = `M ${x1} ${y1} C ${x1 + 180} ${y1}, ${x1 + 180} ${curveDrop}, ${(x1 + x2)/2} ${curveDrop} C ${x2 - 180} ${curveDrop}, ${x2 - 180} ${y2}, ${x2} ${y2}`;
        } else {
          pathD = `M ${x1} ${y1} C ${x1 + dx} ${y1}, ${x2 - dx} ${y2}, ${x2} ${y2}`;
        }

        // Base Edge Path
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', pathD);
        path.setAttribute('class', 'edge-path');
        path.setAttribute('stroke', e.color || 'var(--cyan)');
        path.id = `edge-${e.from}-${e.to}`;
        edgeSvg.appendChild(path);

        // Flow particle path
        if (e.flow || true) {
          const flowPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          flowPath.setAttribute('d', pathD);
          flowPath.setAttribute('class', 'edge-flow');
          flowPath.setAttribute('stroke', e.color || 'var(--cyan)');
          flowPath.setAttribute('stroke-width', '1.6');
          edgeSvg.appendChild(flowPath);
        }

        // Midpoint badge
        if (e.label) {
          const midX = (x1 + x2) / 2;
          const midY = (y1 + y2) / 2;
          const badge = document.createElement('div');
          badge.className = 'edge-badge';
          badge.style.left = midX + 'px';
          badge.style.top = midY + 'px';
          badge.textContent = e.label;
          badge.title = `${fromNode.title} ➔ ${toNode.title}`;
          badgesContainer.appendChild(badge);
        }
      });
    }

    // -------------------------------------------------------------
    // 6. NODE SELECTION & TECHNICAL INSPECTOR
    // -------------------------------------------------------------
    function selectNode(nodeId) {
      selectedNodeId = nodeId;
      const node = NODES.find(n => n.id === nodeId);
      if (!node) return;

      document.querySelectorAll('.node-card').forEach(c => c.classList.remove('selected', 'dimmed'));
      document.querySelectorAll('.edge-path').forEach(p => p.classList.remove('highlighted'));

      const targetCard = document.getElementById('node-' + nodeId);
      if (targetCard) targetCard.classList.add('selected');

      // Highlight connected edges
      EDGES.forEach(e => {
        if (e.from === nodeId || e.to === nodeId) {
          const p = document.getElementById(`edge-${e.from}-${e.to}`);
          if (p) p.classList.add('highlighted');
        }
      });

      // Populate Inspector
      document.getElementById('insp-tag').textContent = node.tag;
      document.getElementById('insp-tag').className = 'node-tag ' + node.tagColor;
      document.getElementById('insp-title').textContent = node.title;
      document.getElementById('insp-file').textContent = node.file;
      document.getElementById('insp-desc').textContent = node.desc;
      document.getElementById('insp-math').textContent = node.formula;
      document.getElementById('insp-math-expl').innerHTML = `<strong>Equation Breakdown:</strong> Governed by continuous parameters strictly grounded in payment specifications and statistical physics.`;

      document.getElementById('insp-responsibilities').innerHTML = node.chips.map(c => `<li>${c}</li>`).join('');
      document.getElementById('insp-inputs').innerHTML = `<strong>Consumed Inputs:</strong><br>${node.inputs}`;
      document.getElementById('insp-outputs').innerHTML = `<strong>Emitted Outputs &amp; Mutations:</strong><br>${node.outputs}`;
      document.getElementById('insp-grounding').innerHTML = `<strong>Domain Reference &amp; Specifications:</strong><br>${node.grounding}`;
      document.getElementById('insp-test').innerHTML = `<strong>Verification Test:</strong><br><code>${node.test}</code>`;
      document.getElementById('insp-roadmap-step').innerHTML = `<strong>Roadmap Role:</strong><br>${node.roadmap}`;

      document.getElementById('inspector').classList.add('open');
    }

    function closeInspector() {
      document.getElementById('inspector').classList.remove('open');
      document.querySelectorAll('.node-card').forEach(c => c.classList.remove('selected', 'dimmed'));
      document.querySelectorAll('.edge-path').forEach(p => p.classList.remove('highlighted'));
      selectedNodeId = null;
    }

    function switchInspTab(tabName) {
      document.querySelectorAll('.inspector-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));

      const btn = Array.from(document.querySelectorAll('.inspector-tab-btn')).find(b => b.getAttribute('onclick').includes(tabName));
      if (btn) btn.classList.add('active');

      const pane = document.getElementById('insp-tab-' + tabName);
      if (pane) pane.classList.add('active');
    }

    // -------------------------------------------------------------
    // 7. REAL-TIME SEARCH
    // -------------------------------------------------------------
    function searchNodes(query) {
      if (!query || !query.trim()) {
        document.querySelectorAll('.node-card').forEach(c => c.classList.remove('dimmed'));
        return;
      }
      const q = query.toLowerCase();
      let firstMatch = null;

      NODES.forEach(n => {
        const text = (n.title + ' ' + n.desc + ' ' + n.file + ' ' + n.formula + ' ' + n.chips.join(' ')).toLowerCase();
        const card = document.getElementById('node-' + n.id);
        if (text.includes(q)) {
          card.classList.remove('dimmed');
          if (!firstMatch) firstMatch = n;
        } else {
          card.classList.add('dimmed');
        }
      });

      if (firstMatch) {
        smoothPanTo(firstMatch.x + firstMatch.w / 2, firstMatch.y + 110, 0.9);
      }
    }

    // Initialize Canvas on load
    window.addEventListener('DOMContentLoaded', () => {
      renderCanvas();
      fitView();
    });
  </script>
</body>
</html>
"""

def generate_interactive_canvas():
    canvas_path = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\reports\fraudxai_interactive_canvas.html")
    canvas_path.parent.mkdir(parents=True, exist_ok=True)
    canvas_path.write_text(CANVAS_HTML, encoding="utf-8")
    print(f"Generated Canvas App: {canvas_path} ({len(CANVAS_HTML)} bytes)")

    # Also overwrite the previous report file so opening either link gives the full canvas experience!
    roadmap_path = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\reports\fraudxai_simulator_architecture_and_roadmap.html")
    roadmap_path.write_text(CANVAS_HTML, encoding="utf-8")
    print(f"Updated Architecture App: {roadmap_path} ({len(CANVAS_HTML)} bytes)")

if __name__ == "__main__":
    generate_interactive_canvas()
