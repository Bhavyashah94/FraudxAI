"""Builds the complete, world-class interactive infinite canvas web application
for FraudxAI using the 51 audited nodes, 70 edges, and 14 clusters from
fraudx_architecture_graph.json.

Outputs:
- reports/fraudxai_interactive_canvas.html
- reports/fraudxai_simulator_architecture_and_roadmap.html
"""

import json
from pathlib import Path

def build_canvas():
    json_path = Path(r"C:\Users\bhavy\.gemini\antigravity\brain\8f9a2210-f49c-46a8-9d2a-89e0154e42c1\fraudx_architecture_graph.json")
    if not json_path.exists():
        raise FileNotFoundError(f"Missing {json_path}")

    graph_data = json.loads(json_path.read_text(encoding="utf-8"))
    nodes = graph_data["nodes"]
    edges = graph_data["edges"]
    clusters = graph_data["clusters"]

    # Cluster Column and Y organization
    cluster_layout = {
        "CLUSTER_SPEC": {"col": 0, "start_y": 120, "color": "var(--cyan)"},
        "CLUSTER_WORLD": {"col": 1, "start_y": 120, "color": "var(--emerald)"},
        "CLUSTER_HAWKES": {"col": 1, "start_y": 1100, "color": "var(--amber)"},
        "CLUSTER_AGENTS": {"col": 2, "start_y": 120, "color": "var(--purple)"},
        "CLUSTER_INTENT": {"col": 2, "start_y": 1200, "color": "var(--rose)"},
        "CLUSTER_ENGINE": {"col": 3, "start_y": 120, "color": "var(--indigo)"},
        "CLUSTER_CLI": {"col": 3, "start_y": 1100, "color": "#94A3B8"},
        "CLUSTER_RAILS_LEDGER": {"col": 4, "start_y": 120, "color": "var(--emerald)"},
        "CLUSTER_CAUSAL": {"col": 5, "start_y": 120, "color": "var(--purple)"},
        "CLUSTER_SUPERVISION": {"col": 6, "start_y": 120, "color": "var(--rose)"},
        "CLUSTER_CALIBRATION": {"col": 6, "start_y": 1100, "color": "var(--emerald)"},
        "CLUSTER_EVALUATION": {"col": 7, "start_y": 120, "color": "#F472B6"},
        "CLUSTER_REPORTING": {"col": 7, "start_y": 1600, "color": "var(--cyan)"},
        "CLUSTER_ROADMAP": {"col": 8, "start_y": 3200, "color": "#2DD4BF"} # Special horizontal zone
    }

    col_x = {
        0: 100,
        1: 750,
        2: 1400,
        3: 2050,
        4: 2700,
        5: 3350,
        6: 4000,
        7: 4650
    }

    # Position each node
    node_positions = {}
    cluster_current_y = {c["cluster_id"]: cluster_layout[c["cluster_id"]]["start_y"] for c in clusters}
    roadmap_x = 100

    for node in nodes:
        cid = node["subsystem_group"]
        cfg = cluster_layout.get(cid, {"col": 0, "start_y": 100, "color": "#94A3B8"})
        
        if cid == "CLUSTER_ROADMAP":
            x = roadmap_x
            y = 3300
            w = 580
            roadmap_x += 640
        else:
            x = col_x[cfg["col"]]
            y = cluster_current_y[cid]
            w = 520
            cluster_current_y[cid] += 260 # vertical step

        node_positions[node["node_id"]] = {"x": x, "y": y, "w": w, "h": 220}

    # Calculate cluster bounding boxes
    zone_boxes = []
    for c in clusters:
        cid = c["cluster_id"]
        c_nodes = [n for n in nodes if n["subsystem_group"] == cid]
        if not c_nodes:
            continue
        xs = [node_positions[n["node_id"]]["x"] for n in c_nodes]
        ys = [node_positions[n["node_id"]]["y"] for n in c_nodes]
        min_x = min(xs) - 30
        min_y = min(ys) - 60
        max_x = max([node_positions[n["node_id"]]["x"] + node_positions[n["node_id"]]["w"] for n in c_nodes]) + 30
        max_y = max([node_positions[n["node_id"]]["y"] + 220 for n in c_nodes]) + 30
        zone_boxes.append({
            "id": cid,
            "name": c["name"],
            "desc": c["description"],
            "color": cluster_layout[cid]["color"],
            "x": min_x,
            "y": min_y,
            "w": max_x - min_x,
            "h": max_y - min_y
        })

    # Prepare injected JSON payloads
    payload_nodes = []
    for n in nodes:
        pos = node_positions[n["node_id"]]
        payload_nodes.append({
            "id": n["node_id"],
            "name": n["human_name"],
            "cluster": n["subsystem_group"],
            "file": n["source_file"],
            "lines": n["line_range"],
            "inputs": n["inputs"],
            "outputs": n["outputs"],
            "formulas": n.get("mathematical_formulas", []),
            "state_vars": n.get("state_variables", []),
            "citations": n.get("regulatory_or_research_citations", []),
            "x": pos["x"],
            "y": pos["y"],
            "w": pos["w"],
            "h": pos["h"]
        })

    payload_edges = []
    for idx, e in enumerate(edges):
        payload_edges.append({
            "id": f"edge-{idx}",
            "from": e["source"],
            "to": e["target"],
            "label": e.get("label", ""),
            "condition": e.get("condition_trigger", e.get("condition", ""))
        })

    nodes_json = json.dumps(payload_nodes)
    edges_json = json.dumps(payload_edges)
    zones_json = json.dumps(zone_boxes)
    clusters_json = json.dumps(clusters)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>FraudxAI — Complete System Architecture &amp; Future Roadmap Infinite Canvas</title>
  <style>
    :root {{
      --bg: #070A13;
      --grid-dot: #1A2338;
      --card-bg: rgba(15, 23, 42, 0.95);
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
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; user-select: none; }}
    html, body {{
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
    }}

    /* Infinite Canvas Viewport */
    #viewport {{
      width: 100vw;
      height: 100vh;
      position: absolute;
      top: 0; left: 0;
      overflow: hidden;
      cursor: grab;
      background-color: var(--bg);
      background-image: radial-gradient(var(--grid-dot) 1.5px, transparent 1.5px);
      background-size: 32px 32px;
    }}
    #viewport.panning {{ cursor: grabbing; }}

    /* Virtual World Container */
    #world {{
      position: absolute;
      top: 0; left: 0;
      width: 6000px;
      height: 4800px;
      transform-origin: 0 0;
      will-change: transform;
    }}

    /* SVG Edges Layer */
    #edge-svg {{
      position: absolute;
      top: 0; left: 0;
      width: 6000px;
      height: 4800px;
      pointer-events: none;
      z-index: 10;
    }}
    .edge-path {{
      fill: none;
      stroke-width: 2.2;
      stroke-linecap: round;
      opacity: 0.7;
      transition: stroke-width 0.2s, opacity 0.2s;
    }}
    .edge-path.highlighted {{
      stroke-width: 4.5;
      opacity: 1;
      filter: drop-shadow(0 0 10px currentColor);
    }}
    .edge-flow {{
      fill: none;
      stroke-dasharray: 6 14;
      stroke-linecap: round;
      animation: flowDash 28s linear infinite;
    }}
    @keyframes flowDash {{
      to {{ stroke-dashoffset: -1000; }}
    }}

    /* Edge Condition Badges */
    .edge-badge {{
      position: absolute;
      z-index: 25;
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 9999px;
      background: #090D16;
      border: 1px solid #1E293B;
      color: var(--text-muted);
      pointer-events: auto;
      transform: translate(-50%, -50%);
      box-shadow: 0 4px 14px rgba(0,0,0,0.7);
      white-space: nowrap;
      transition: all 0.2s;
      cursor: pointer;
    }}
    .edge-badge:hover {{
      border-color: var(--cyan);
      color: #FFFFFF;
      transform: translate(-50%, -50%) scale(1.1);
      z-index: 45;
      box-shadow: 0 0 12px var(--cyan-glow);
    }}

    /* Swimlanes / Subsystem Zones */
    .zone-box {{
      position: absolute;
      border-radius: 18px;
      border: 1.5px dashed rgba(255, 255, 255, 0.15);
      background: rgba(15, 23, 42, 0.35);
      backdrop-filter: blur(2px);
      z-index: 5;
      pointer-events: none;
    }}
    .zone-label {{
      position: absolute;
      top: 14px; left: 20px;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 5px 14px;
      border-radius: 8px;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: #CBD5E1;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* Node Cards */
    .node-card {{
      position: absolute;
      z-index: 20;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55);
      cursor: pointer;
      transition: transform 0.18s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.18s, box-shadow 0.18s;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}
    .node-card:hover {{
      transform: translateY(-4px) scale(1.015);
      border-color: var(--card-hover-border);
      box-shadow: 0 16px 40px rgba(56, 189, 248, 0.25);
      z-index: 35;
    }}
    .node-card.selected {{
      border-color: var(--cyan);
      box-shadow: 0 0 0 2px var(--cyan), 0 20px 45px rgba(56, 189, 248, 0.35);
      z-index: 40;
    }}
    .node-card.dimmed {{
      opacity: 0.2;
      filter: grayscale(80%);
    }}

    /* Node Header */
    .node-header {{
      padding: 10px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      background: rgba(255, 255, 255, 0.02);
    }}
    .node-tag {{
      font-family: var(--font-mono);
      font-size: 9.5px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }}
    .node-file {{
      font-family: var(--font-mono);
      font-size: 10px;
      color: var(--text-dim);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .node-body {{
      padding: 12px 14px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .node-title {{
      font-size: 14.5px;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 6px;
      line-height: 1.3;
    }}
    .node-desc {{
      font-size: 11.5px;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 8px;
    }}

    /* Formula Pill inside node */
    .node-formula {{
      background: #090D16;
      border: 1px solid #1E293B;
      border-radius: 6px;
      padding: 5px 9px;
      font-family: var(--font-mono);
      font-size: 10.5px;
      color: var(--cyan);
      margin-top: 4px;
      white-space: pre-wrap;
      word-break: break-all;
      line-height: 1.4;
    }}

    /* Ports */
    .port-in, .port-out {{
      position: absolute;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #0F172A;
      border: 2.5px solid var(--text-muted);
      top: 50%;
      transform: translateY(-50%);
      transition: all 0.2s;
    }}
    .port-in {{ left: -6px; }}
    .port-out {{ right: -6px; }}
    .node-card:hover .port-in, .node-card:hover .port-out {{
      border-color: var(--cyan);
      box-shadow: 0 0 8px var(--cyan);
    }}

    /* Floating Top HUD Bar */
    .hud-top {{
      position: fixed;
      top: 16px; left: 20px; right: 20px;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      pointer-events: none;
    }}
    .hud-pill-group {{
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 8px 14px;
      display: flex;
      align-items: center;
      gap: 12px;
      pointer-events: auto;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.55);
    }}
    .hud-title {{
      font-weight: 800;
      font-size: 14px;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .hud-title span {{ color: var(--cyan); }}
    .hud-search-input {{
      background: #090D16;
      border: 1px solid #1E293B;
      color: #F8FAFC;
      font-family: var(--font-sans);
      font-size: 12.5px;
      padding: 6px 12px;
      border-radius: 8px;
      width: 250px;
      transition: all 0.2s;
    }}
    .hud-search-input:focus {{
      outline: none;
      border-color: var(--cyan);
      width: 330px;
      box-shadow: 0 0 12px var(--cyan-glow);
    }}

    /* Quick Jump Dropdown */
    .jump-select {{
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
    }}
    .jump-select:hover {{ border-color: var(--cyan); }}

    /* Bottom Control Dock */
    .hud-bottom-left {{
      position: fixed;
      bottom: 20px; left: 20px;
      z-index: 100;
      display: flex;
      flex-direction: column;
      gap: 8px;
      pointer-events: auto;
    }}
    .dock-btn-group {{
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 4px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }}
    .dock-btn {{
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
    }}
    .dock-btn:hover {{
      background: #1E293B;
      color: var(--cyan);
    }}

    /* Minimap in Bottom-Right */
    #minimap-container {{
      position: fixed;
      bottom: 20px; right: 20px;
      width: 270px;
      height: 190px;
      background: rgba(11, 15, 25, 0.92);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      z-index: 100;
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.65);
      overflow: hidden;
      cursor: crosshair;
      pointer-events: auto;
    }}
    .minimap-header {{
      padding: 6px 10px;
      font-size: 10px;
      font-family: var(--font-mono);
      font-weight: 700;
      color: var(--text-dim);
      border-bottom: 1px solid rgba(255,255,255,0.06);
      display: flex;
      justify-content: space-between;
    }}
    #minimap-svg {{
      width: 100%;
      height: 155px;
    }}
    #minimap-viewport {{
      fill: rgba(56, 189, 248, 0.15);
      stroke: var(--cyan);
      stroke-width: 1.5;
    }}

    /* Side Technical Inspector Drawer */
    #inspector {{
      position: fixed;
      top: 0; right: -660px;
      width: 630px;
      height: 100vh;
      background: rgba(15, 23, 42, 0.98);
      backdrop-filter: blur(20px);
      border-left: 1px solid var(--card-border);
      z-index: 200;
      box-shadow: -15px 0 50px rgba(0, 0, 0, 0.75);
      transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }}
    #inspector.open {{ right: 0; }}
    .inspector-header {{
      padding: 20px;
      border-bottom: 1px solid var(--card-border);
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
    }}
    .inspector-close {{
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
    }}
    .inspector-close:hover {{ background: #334155; color: white; }}
    .inspector-tabs {{
      display: flex;
      background: #090D16;
      border-bottom: 1px solid var(--card-border);
      overflow-x: auto;
    }}
    .inspector-tab-btn {{
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
    }}
    .inspector-tab-btn.active {{
      color: var(--cyan);
      border-bottom-color: var(--cyan);
      background: rgba(56, 189, 248, 0.05);
    }}
    .inspector-body {{
      flex: 1;
      overflow-y: auto;
      padding: 20px;
    }}
    .tab-pane {{ display: none; }}
    .tab-pane.active {{ display: block; }}

    /* Code & Callout Blocks inside Inspector */
    .insp-code {{
      background: #090D16;
      border: 1px solid #1E293B;
      border-radius: 8px;
      padding: 12px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: #E2E8F0;
      overflow-x: auto;
      margin: 10px 0;
      line-height: 1.5;
    }}
    .insp-callout {{
      border-left: 3px solid var(--cyan);
      background: rgba(56, 189, 248, 0.08);
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      margin: 12px 0;
      font-size: 12.5px;
      line-height: 1.5;
      color: #CBD5E1;
    }}
    .insp-callout-emerald {{
      border-left-color: var(--emerald);
      background: rgba(52, 211, 153, 0.08);
    }}
    .insp-callout-amber {{
      border-left-color: var(--amber);
      background: rgba(251, 191, 36, 0.08);
    }}
    .edge-chip-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin: 10px 0;
    }}
    .edge-chip-item {{
      background: #090D16;
      border: 1px solid #1E293B;
      border-radius: 6px;
      padding: 8px 12px;
      font-size: 12px;
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}
    .edge-chip-target {{
      font-family: var(--font-mono);
      font-weight: 700;
      color: var(--cyan);
    }}
    .edge-chip-label {{
      color: var(--text);
    }}
    .edge-chip-cond {{
      font-size: 11px;
      color: var(--text-dim);
    }}
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
        <span style="font-weight:400; color:var(--text-muted); font-size:12px;">| Full System Architecture &amp; Roadmap Infinite Canvas</span>
      </div>
      <select class="jump-select" id="jump-select" onchange="jumpToCluster(this.value)">
        <option value="">Jump to Subsystem...</option>
        <option value="CLUSTER_SPEC">Zone 0: Ground-Truth Specifications (12 YAMLs)</option>
        <option value="CLUSTER_WORLD">Zone 1A: World Environment &amp; Kinematics</option>
        <option value="CLUSTER_HAWKES">Zone 1B: Generative Arrival Pacing (Hawkes MTPP)</option>
        <option value="CLUSTER_AGENTS">Zone 2A: Behavioral Agent FSM Subsystem</option>
        <option value="CLUSTER_INTENT">Zone 2B: Adversarial Intent &amp; Threat Mesh</option>
        <option value="CLUSTER_ENGINE">Zone 3A: Discrete-Event Engine Core (heapq μs)</option>
        <option value="CLUSTER_CLI">Zone 3B: CLI Orchestrator &amp; Entrypoints</option>
        <option value="CLUSTER_RAILS_LEDGER">Zone 4: Payment Rails &amp; Double-Entry Ledger</option>
        <option value="CLUSTER_CAUSAL">Zone 5: Causal Ground-Truth &amp; Invertible Flows</option>
        <option value="CLUSTER_SUPERVISION">Zone 6A: Operational Supervision &amp; Delayed Feedback</option>
        <option value="CLUSTER_CALIBRATION">Zone 6B: Central Bank Calibration Subsystem</option>
        <option value="CLUSTER_EVALUATION">Zone 7A: Prequential Evaluation &amp; Drift Auditing</option>
        <option value="CLUSTER_REPORTING">Zone 7B: Publication Scorecards &amp; Forensic Graph</option>
        <option value="CLUSTER_ROADMAP">Zone 8: Verified Future Roadmap (Phases 1-4 &amp; 6-9)</option>
      </select>
      <input type="text" id="node-search" class="hud-search-input" placeholder="Search 51 nodes, math, classes (e.g. ISO 51, Hawkes, Welford)..." oninput="searchNodes(this.value)">
    </div>

    <div class="hud-pill-group">
      <div style="font-family:var(--font-mono); font-size:11px; font-weight:700; color:var(--emerald);">
        ● 178/178 TESTS PASSING
      </div>
      <div style="font-family:var(--font-mono); font-size:11px; color:var(--text-dim);">
        51 Nodes | 70 Edges | 14 Clusters
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
    <svg id="minimap-svg" viewBox="0 0 6000 4800">
      <g id="minimap-zones"></g>
      <g id="minimap-nodes"></g>
      <rect id="minimap-viewport" x="0" y="0" width="1000" height="700" />
    </svg>
  </div>

  <!-- Side Technical Inspector Drawer -->
  <div id="inspector">
    <div class="inspector-header">
      <div>
        <div id="insp-tag" class="node-tag" style="display:inline-block; margin-bottom:6px; background:rgba(56,189,248,0.15); color:var(--cyan); border:1px solid var(--cyan);">NODE</div>
        <h2 id="insp-title" style="font-size:17px; font-weight:800; color:#FFFFFF;">Node Title</h2>
        <div id="insp-file" style="font-family:var(--font-mono); font-size:11px; color:var(--cyan); margin-top:3px;">file.py:100-200</div>
      </div>
      <button class="inspector-close" onclick="closeInspector()">✕</button>
    </div>

    <div class="inspector-tabs">
      <button class="inspector-tab-btn active" onclick="switchInspTab('overview')">Overview</button>
      <button class="inspector-tab-btn" onclick="switchInspTab('math')">Math &amp; Algorithm</button>
      <button class="inspector-tab-btn" onclick="switchInspTab('contracts')">Data Contracts</button>
      <button class="inspector-tab-btn" onclick="switchInspTab('grounding')">Banking Grounding</button>
      <button class="inspector-tab-btn" onclick="switchInspTab('edges')">Connections (70)</button>
    </div>

    <div class="inspector-body">
      <!-- Tab 1: Overview -->
      <div id="insp-tab-overview" class="tab-pane active">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Node Identification</h4>
        <div id="insp-node-id" style="font-family:var(--font-mono); font-size:12px; color:#FBBF24; margin-bottom:12px;"></div>

        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Subsystem Cluster</h4>
        <p id="insp-cluster" style="font-size:13px; color:#E2E8F0; line-height:1.5; margin-bottom:14px;"></p>
        
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">State Variables</h4>
        <div id="insp-state-vars" class="insp-callout"></div>
      </div>

      <!-- Tab 2: Math -->
      <div id="insp-tab-math" class="tab-pane">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Mathematical Equations &amp; Algorithms</h4>
        <div id="insp-math-container"></div>
      </div>

      <!-- Tab 3: Contracts -->
      <div id="insp-tab-contracts" class="tab-pane">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Consumed Inputs</h4>
        <div id="insp-inputs" class="insp-callout"></div>

        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-top:14px; margin-bottom:6px;">Emitted Outputs &amp; State Mutations</h4>
        <div id="insp-outputs" class="insp-callout insp-callout-emerald"></div>
      </div>

      <!-- Tab 4: Grounding -->
      <div id="insp-tab-grounding" class="tab-pane">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Payment Rail Specs &amp; Academic Citations</h4>
        <div id="insp-grounding" class="insp-callout insp-callout-amber"></div>
      </div>

      <!-- Tab 5: Edges -->
      <div id="insp-tab-edges" class="tab-pane">
        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-bottom:6px;">Outgoing Connections</h4>
        <div id="insp-out-edges" class="edge-chip-list"></div>

        <h4 style="font-size:12px; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.05em; margin-top:14px; margin-bottom:6px;">Incoming Connections</h4>
        <div id="insp-in-edges" class="edge-chip-list"></div>
      </div>
    </div>
  </div>

  <script>
    const NODES = {nodes_json};
    const EDGES = {edges_json};
    const ZONES = {zones_json};
    const CLUSTERS = {clusters_json};

    const viewport = document.getElementById('viewport');
    const world = document.getElementById('world');
    const edgeSvg = document.getElementById('edge-svg');
    const zonesContainer = document.getElementById('zones-container');
    const nodesContainer = document.getElementById('nodes-container');
    const badgesContainer = document.getElementById('badges-container');
    const minimapViewport = document.getElementById('minimap-viewport');
    const zoomIndicator = document.getElementById('zoom-indicator');

    let panX = 40;
    let panY = 40;
    let zoom = 0.40; // Initial zoom to show healthy wide overview
    let isPanning = false;
    let startX = 0, startY = 0;
    let selectedNodeId = null;

    function updateTransform() {{
      world.style.transform = `translate3d(${{panX}}px, ${{panY}}px, 0px) scale(${{zoom}})`;
      zoomIndicator.textContent = Math.round(zoom * 100) + "%";

      const vWidth = window.innerWidth / zoom;
      const vHeight = window.innerHeight / zoom;
      const vLeft = -panX / zoom;
      const vTop = -panY / zoom;

      minimapViewport.setAttribute('x', Math.max(0, vLeft));
      minimapViewport.setAttribute('y', Math.max(0, vTop));
      minimapViewport.setAttribute('width', Math.min(6000, vWidth));
      minimapViewport.setAttribute('height', Math.min(4800, vHeight));
    }}

    // Mouse drag pan
    viewport.addEventListener('mousedown', (e) => {{
      if (e.target.closest('.node-card') || e.target.closest('#inspector') || e.target.closest('.hud-top') || e.target.closest('.hud-bottom-left') || e.target.closest('#minimap-container')) return;
      isPanning = true;
      viewport.classList.add('panning');
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isPanning) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isPanning = false;
      viewport.classList.remove('panning');
    }});

    // Cursor-centered zoom
    viewport.addEventListener('wheel', (e) => {{
      if (e.target.closest('#inspector')) return;
      e.preventDefault();

      const rect = viewport.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      const worldX = (mouseX - panX) / zoom;
      const worldY = (mouseY - panY) / zoom;

      const zoomFactor = Math.exp(-e.deltaY * 0.0018);
      const newZoom = Math.min(Math.max(zoom * zoomFactor, 0.12), 2.8);

      panX = mouseX - worldX * newZoom;
      panY = mouseY - worldY * newZoom;
      zoom = newZoom;

      updateTransform();
    }}, {{ passive: false }});

    function zoomIn() {{
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      const wx = (cx - panX) / zoom;
      const wy = (cy - panY) / zoom;
      zoom = Math.min(zoom * 1.25, 2.8);
      panX = cx - wx * zoom;
      panY = cy - wy * zoom;
      updateTransform();
    }}
    function zoomOut() {{
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      const wx = (cx - panX) / zoom;
      const wy = (cy - panY) / zoom;
      zoom = Math.max(zoom / 1.25, 0.12);
      panX = cx - wx * zoom;
      panY = cy - wy * zoom;
      updateTransform();
    }}
    function resetZoom() {{
      zoom = 1.0;
      panX = 60;
      panY = 60;
      updateTransform();
    }}
    function fitView() {{
      const vW = window.innerWidth;
      const vH = window.innerHeight;
      const scaleX = vW / 5600;
      const scaleY = vH / 4600;
      zoom = Math.min(scaleX, scaleY) * 0.95;
      panX = (vW - 5600 * zoom) / 2;
      panY = (vH - 4600 * zoom) / 2;
      updateTransform();
    }}

    function smoothPanTo(targetX, targetY, targetZoom = 0.75) {{
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      const endPanX = cx - targetX * targetZoom;
      const endPanY = cy - targetY * targetZoom;

      const startPX = panX;
      const startPY = panY;
      const startZ = zoom;
      const startTime = performance.now();
      const duration = 500;

      function step(now) {{
        const progress = Math.min((now - startTime) / duration, 1.0);
        const ease = 0.5 - Math.cos(progress * Math.PI) / 2;
        panX = startPX + (endPanX - startPX) * ease;
        panY = startPY + (endPanY - startPY) * ease;
        zoom = startZ + (targetZoom - startZ) * ease;
        updateTransform();
        if (progress < 1.0) requestAnimationFrame(step);
      }}
      requestAnimationFrame(step);
    }}

    function jumpToCluster(zoneId) {{
      if (!zoneId) return;
      const zone = ZONES.find(z => z.id === zoneId);
      if (!zone) return;
      smoothPanTo(zone.x + zone.w / 2, zone.y + zone.h / 2, zone.id === 'CLUSTER_ROADMAP' ? 0.35 : 0.65);
    }}

    // Render nodes, zones, edges
    function renderCanvas() {{
      // 1. Zones
      zonesContainer.innerHTML = '';
      const minimapZonesGroup = document.getElementById('minimap-zones');
      minimapZonesGroup.innerHTML = '';

      ZONES.forEach(z => {{
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
        label.textContent = z.name;
        el.appendChild(label);
        zonesContainer.appendChild(el);

        const mRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        mRect.setAttribute('x', z.x);
        mRect.setAttribute('y', z.y);
        mRect.setAttribute('width', z.w);
        mRect.setAttribute('height', z.h);
        mRect.setAttribute('fill', 'rgba(255,255,255,0.03)');
        mRect.setAttribute('stroke', 'rgba(255,255,255,0.12)');
        minimapZonesGroup.appendChild(mRect);
      }});

      // 2. Nodes
      nodesContainer.innerHTML = '';
      const minimapNodesGroup = document.getElementById('minimap-nodes');
      minimapNodesGroup.innerHTML = '';

      NODES.forEach(n => {{
        const card = document.createElement('div');
        card.className = 'node-card';
        card.id = 'node-' + n.id;
        card.style.left = n.x + 'px';
        card.style.top = n.y + 'px';
        card.style.width = n.w + 'px';
        card.style.minHeight = n.h + 'px';

        const firstFormula = n.formulas.length > 0 ? n.formulas[0] : (n.outputs.length > 0 ? n.outputs[0] : '');
        card.innerHTML = `
          <div class="port-in"></div>
          <div class="port-out"></div>
          <div class="node-header">
            <span class="node-tag" style="background:rgba(56,189,248,0.15); color:var(--cyan); border:1px solid var(--cyan);">${{n.cluster.replace('CLUSTER_', '')}}</span>
            <span class="node-file" title="${{n.file}}:${{n.lines}}">${{n.file.split('/')[1] || n.file}}:${{n.lines}}</span>
          </div>
          <div class="node-body">
            <div>
              <div class="node-title">${{n.name}}</div>
              <div class="node-desc">${{n.inputs.slice(0, 2).join(', ')}}</div>
            </div>
            ${{firstFormula ? `<div class="node-formula">${{firstFormula}}</div>` : ''}}
          </div>
        `;

        card.addEventListener('click', (e) => {{
          e.stopPropagation();
          selectNode(n.id);
        }});

        nodesContainer.appendChild(card);

        // Minimap
        const mNode = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        mNode.setAttribute('x', n.x);
        mNode.setAttribute('y', n.y);
        mNode.setAttribute('width', n.w);
        mNode.setAttribute('height', n.h);
        mNode.setAttribute('fill', 'rgba(56,189,248,0.75)');
        mNode.setAttribute('rx', 16);
        minimapNodesGroup.appendChild(mNode);
      }});

      renderEdges();
      updateTransform();
    }}

    function renderEdges() {{
      edgeSvg.innerHTML = '';
      badgesContainer.innerHTML = '';

      EDGES.forEach((e, idx) => {{
        const fromNode = NODES.find(n => n.id === e.from);
        const toNode = NODES.find(n => n.id === e.to);
        if (!fromNode || !toNode) return;

        let x1 = fromNode.x + fromNode.w;
        let y1 = fromNode.y + 110;
        let x2 = toNode.x;
        let y2 = toNode.y + 110;

        let dx = Math.abs(x2 - x1) * 0.45;
        if (dx < 60) dx = 140;

        let pathD;
        if (x2 < x1) {{
          // Backward / feedback loop
          const curveDrop = Math.max(y1, y2) + 160;
          pathD = `M ${{x1}} ${{y1}} C ${{x1 + 180}} ${{y1}}, ${{x1 + 180}} ${{curveDrop}}, ${{(x1 + x2)/2}} ${{curveDrop}} C ${{x2 - 180}} ${{curveDrop}}, ${{x2 - 180}} ${{y2}}, ${{x2}} ${{y2}}`;
        }} else {{
          pathD = `M ${{x1}} ${{y1}} C ${{x1 + dx}} ${{y1}}, ${{x2 - dx}} ${{y2}}, ${{x2}} ${{y2}}`;
        }}

        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', pathD);
        path.setAttribute('class', 'edge-path');
        path.setAttribute('stroke', (e.label.includes('ISO') || e.label.includes('Feedback')) ? 'var(--amber)' : (e.label.includes('Approved') ? 'var(--emerald)' : 'var(--cyan)'));
        path.id = `edge-${{e.from}}-${{e.to}}`;
        edgeSvg.appendChild(path);

        // Animated flow dash
        const flowPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        flowPath.setAttribute('d', pathD);
        flowPath.setAttribute('class', 'edge-flow');
        flowPath.setAttribute('stroke', path.getAttribute('stroke'));
        flowPath.setAttribute('stroke-width', '1.6');
        edgeSvg.appendChild(flowPath);

        // Badge
        if (e.label && idx % 2 === 0) {{
          const midX = (x1 + x2) / 2;
          const midY = (y1 + y2) / 2;
          const badge = document.createElement('div');
          badge.className = 'edge-badge';
          badge.style.left = midX + 'px';
          badge.style.top = midY + 'px';
          badge.textContent = e.label;
          badge.title = `${{fromNode.name}} ➔ ${{toNode.name}} [${{e.condition}}]`;
          badge.onclick = () => selectNode(fromNode.id);
          badgesContainer.appendChild(badge);
        }}
      }});
    }}

    function selectNode(nodeId) {{
      selectedNodeId = nodeId;
      const node = NODES.find(n => n.id === nodeId);
      if (!node) return;

      document.querySelectorAll('.node-card').forEach(c => c.classList.remove('selected', 'dimmed'));
      document.querySelectorAll('.edge-path').forEach(p => p.classList.remove('highlighted'));

      const targetCard = document.getElementById('node-' + nodeId);
      if (targetCard) targetCard.classList.add('selected');

      // Highlight edges
      EDGES.forEach(e => {{
        if (e.from === nodeId || e.to === nodeId) {{
          const p = document.getElementById(`edge-${{e.from}}-${{e.to}}`);
          if (p) p.classList.add('highlighted');
        }}
      }});

      // Populate Inspector
      document.getElementById('insp-tag').textContent = node.cluster.replace('CLUSTER_', '');
      document.getElementById('insp-title').textContent = node.name;
      document.getElementById('insp-file').textContent = `${{node.file}} (${{node.lines}})`;
      document.getElementById('insp-node-id').textContent = `ID: ${{node.id}}`;

      const clusterObj = CLUSTERS.find(c => c.cluster_id === node.cluster);
      document.getElementById('insp-cluster').textContent = clusterObj ? clusterObj.description : node.cluster;

      document.getElementById('insp-state-vars').innerHTML = node.state_vars.length > 0 
        ? node.state_vars.map(s => `<div>• <code>${{s}}</code></div>`).join('') 
        : '<em>Stateless functional evaluator</em>';

      document.getElementById('insp-math-container').innerHTML = node.formulas.length > 0
        ? node.formulas.map(f => `<pre class="insp-code"><code>${{f}}</code></pre>`).join('')
        : '<div class="insp-callout">Evaluates business logic and protocol state machines.</div>';

      document.getElementById('insp-inputs').innerHTML = node.inputs.map(i => `<div>• ${{i}}</div>`).join('');
      document.getElementById('insp-outputs').innerHTML = node.outputs.map(o => `<div>• ${{o}}</div>`).join('');

      document.getElementById('insp-grounding').innerHTML = node.citations.length > 0
        ? node.citations.map(c => `<div>• ${{c}}</div>`).join('')
        : 'ISO 8583 Banking Standard; Visa Core Rules; RBI Master Directions.';

      // Connected Edges
      const outEdges = EDGES.filter(e => e.from === nodeId);
      const inEdges = EDGES.filter(e => e.to === nodeId);

      document.getElementById('insp-out-edges').innerHTML = outEdges.length > 0 
        ? outEdges.map(e => `
            <div class="edge-chip-item">
              <div class="edge-chip-target">➔ ${{NODES.find(n=>n.id===e.to)?.name || e.to}}</div>
              <div class="edge-chip-label">${{e.label}}</div>
              <div class="edge-chip-cond">Trigger: ${{e.condition}}</div>
            </div>
          `).join('')
        : '<em>Terminal leaf node</em>';

      document.getElementById('insp-in-edges').innerHTML = inEdges.length > 0
        ? inEdges.map(e => `
            <div class="edge-chip-item">
              <div class="edge-chip-target">⬅ ${{NODES.find(n=>n.id===e.from)?.name || e.from}}</div>
              <div class="edge-chip-label">${{e.label}}</div>
              <div class="edge-chip-cond">Condition: ${{e.condition}}</div>
            </div>
          `).join('')
        : '<em>Root source node</em>';

      document.getElementById('inspector').classList.add('open');
    }}

    function closeInspector() {{
      document.getElementById('inspector').classList.remove('open');
      document.querySelectorAll('.node-card').forEach(c => c.classList.remove('selected', 'dimmed'));
      document.querySelectorAll('.edge-path').forEach(p => p.classList.remove('highlighted'));
      selectedNodeId = null;
    }}

    function switchInspTab(tabName) {{
      document.querySelectorAll('.inspector-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));

      const btn = Array.from(document.querySelectorAll('.inspector-tab-btn')).find(b => b.getAttribute('onclick').includes(tabName));
      if (btn) btn.classList.add('active');

      const pane = document.getElementById('insp-tab-' + tabName);
      if (pane) pane.classList.add('active');
    }}

    function searchNodes(query) {{
      if (!query || !query.trim()) {{
        document.querySelectorAll('.node-card').forEach(c => c.classList.remove('dimmed'));
        return;
      }}
      const q = query.toLowerCase();
      let firstMatch = null;

      NODES.forEach(n => {{
        const text = (n.name + ' ' + n.id + ' ' + n.file + ' ' + n.formulas.join(' ') + ' ' + n.inputs.join(' ') + ' ' + n.outputs.join(' ')).toLowerCase();
        const card = document.getElementById('node-' + n.id);
        if (text.includes(q)) {{
          card.classList.remove('dimmed');
          if (!firstMatch) firstMatch = n;
        }} else {{
          card.classList.add('dimmed');
        }}
      }});

      if (firstMatch) {{
        smoothPanTo(firstMatch.x + firstMatch.w / 2, firstMatch.y + 110, 0.85);
      }}
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      renderCanvas();
      fitView();
    }});
  </script>
</body>
</html>
"""

    out1 = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\reports\fraudxai_interactive_canvas.html")
    out2 = Path(r"c:\Users\bhavy\Documents\Projects\FraudxAI\reports\fraudxai_simulator_architecture_and_roadmap.html")
    out1.write_text(html_template, encoding="utf-8")
    out2.write_text(html_template, encoding="utf-8")
    print(f"Generated 51-node canvas at {out1} ({len(html_template)} bytes)")
    print(f"Updated {out2}")

if __name__ == "__main__":
    build_canvas()
