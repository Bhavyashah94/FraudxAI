"""Interactive Simulation Visualizer & Cybercrime Threat Graph Engine for FraudxAI.

Compiles simulation batches into:
1. Cybercrime Threat Graph (Syndicates -> Botnets -> Cards -> Merchants -> Mule Rings).
2. 4-Hop Banking Switch Funnel (Gateway -> Visa VAAI -> 3DS ACS -> Issuer Host).
3. Temporal Hawkes Event Dynamics (Circadian normal curves vs. adversarial bursts).
4. Standalone self-contained HTML5 interactive dashboard with zero external Python GUI dependencies.
"""

from __future__ import annotations

import html
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np

from .engine import SimulationEngine
from .syndicates import SyndicateRegistry


def compile_simulation_data_bundle(
    records: List[Dict[str, Any]],
    region: str = "US",
    seed: int = 42,
    max_table_records: int = 250,
) -> Dict[str, Any]:
    """Compiles raw simulation transaction records into an analytics data bundle for visualization."""
    total_tx = len(records)
    if total_tx == 0:
        return {"error": "Empty transaction batch"}

    fraud_records = [r for r in records if r.get("is_fraud") == 1]
    legit_records = [r for r in records if r.get("is_fraud") == 0]
    hard_neg_records = [r for r in legit_records if "HARD_NEGATIVE" in r.get("scenario_tag", "")]

    # 1. Macro-Option Breakdown
    macro_counts = Counter(r.get("scenario_tag", "UNKNOWN") for r in fraud_records)
    macro_stats = []
    for sc, cnt in macro_counts.most_common():
        amts = [r["amount"] for r in fraud_records if r.get("scenario_tag") == sc]
        macro_stats.append({
            "scenario": sc,
            "count": cnt,
            "pct": round(cnt / max(1, len(fraud_records)) * 100, 1),
            "amount_min": round(float(min(amts)), 2) if amts else 0.0,
            "amount_median": round(float(np.median(amts)), 2) if amts else 0.0,
            "amount_max": round(float(max(amts)), 2) if amts else 0.0,
            "amount_sum": round(float(sum(amts)), 2),
        })

    # 2. 4-Hop Banking Switch Funnel
    hop_origins = Counter(r.get("hop_origin", "ISSUER_HOST") for r in records)
    fraud_hop_origins = Counter(r.get("hop_origin", "ISSUER_HOST") for r in fraud_records)

    iso_codes = Counter(r.get("response_code", "00") for r in records)
    fraud_iso_codes = Counter(r.get("response_code", "00") for r in fraud_records)

    approved_count = sum(1 for r in records if r.get("response_code") in ("00", "10"))
    declined_count = total_tx - approved_count

    gateway_drops = sum(1 for r in records if r.get("hop_origin") == "GATEWAY_FILTER" and r.get("response_code") not in ("00", "10"))
    vaai_drops = sum(1 for r in records if r.get("hop_origin") == "NETWORK_SWITCH_VAAI" and r.get("response_code") not in ("00", "10"))
    acs_drops = sum(1 for r in records if r.get("hop_origin") == "ACS_3DS" and r.get("response_code") not in ("00", "10"))
    issuer_drops = sum(1 for r in records if r.get("hop_origin") == "ISSUER_HOST" and r.get("response_code") not in ("00", "10"))

    funnel_data = {
        "total_ingress": total_tx,
        "approved": approved_count,
        "declined": declined_count,
        "approval_rate": round(approved_count / total_tx * 100, 1),
        "hops": [
            {
                "id": "hop_1",
                "name": "Hop 1: Gateway Edge Filter",
                "description": "Browser Canvas Invariance, IP Reputation (>=85), Kinematic Supersonic Velocity",
                "drop_count": gateway_drops,
                "drop_pct": round(gateway_drops / total_tx * 100, 2),
            },
            {
                "id": "hop_2",
                "name": "Hop 2: Network Switch In-Flight ML",
                "description": "Visa Account Attack Intelligence (VAAI Field 44.5 >= 75) Carding Intercept",
                "drop_count": vaai_drops,
                "drop_pct": round(vaai_drops / total_tx * 100, 2),
            },
            {
                "id": "hop_3",
                "name": "Hop 3: 3DS Access Control Server",
                "description": "PSD2 Low-Value (<$30) & TRA (<$100) Exemptions vs 2FA Step-Up Challenge Drops",
                "drop_count": acs_drops,
                "drop_pct": round(acs_drops / total_tx * 100, 2),
            },
            {
                "id": "hop_4",
                "name": "Hop 4: Issuer Core Banking Host",
                "description": "DDA Solvency (ISO 51), Balance Oracle (ISO 10), Hourly Velocity (ISO 65), STIP (ISO 91)",
                "drop_count": issuer_drops,
                "drop_pct": round(issuer_drops / total_tx * 100, 2),
            },
        ],
        "iso_distribution": [{"code": k, "count": v, "pct": round(v / total_tx * 100, 1)} for k, v in iso_codes.most_common()],
        "fraud_iso_distribution": [{"code": k, "count": v, "pct": round(v / max(1, len(fraud_records)) * 100, 1)} for k, v in fraud_iso_codes.most_common()],
    }

    # 3. Temporal Hawkes Pacing (Hourly aggregation 0-23h)
    hourly_data = defaultdict(lambda: {"legit": 0, "fraud": 0, "hard_neg": 0, "amount_sum": 0.0})
    for r in records:
        tx_time = float(r.get("tx_time_seconds", 0.0))
        hour = int((tx_time / 3600.0) % 24)
        amt = float(r.get("amount", 0.0))
        is_f = int(r.get("is_fraud", 0))
        is_hn = 1 if "HARD_NEGATIVE" in r.get("scenario_tag", "") else 0

        if is_f:
            hourly_data[hour]["fraud"] += 1
        elif is_hn:
            hourly_data[hour]["hard_neg"] += 1
        else:
            hourly_data[hour]["legit"] += 1
        hourly_data[hour]["amount_sum"] += amt

    temporal_series = [
        {
            "hour": h,
            "legit": hourly_data[h]["legit"],
            "fraud": hourly_data[h]["fraud"],
            "hard_neg": hourly_data[h]["hard_neg"],
            "total_amount": round(hourly_data[h]["amount_sum"], 2),
        }
        for h in range(24)
    ]

    # 4. Cybercrime Threat Graph Construction
    nodes_map: Dict[str, Dict[str, Any]] = {}
    links_list: List[Dict[str, Any]] = []
    link_counts: Dict[str, int] = Counter()
    link_amounts: Dict[str, float] = defaultdict(float)

    def add_node(node_id: str, label: str, node_type: str, details: Dict[str, Any]) -> None:
        if node_id not in nodes_map:
            nodes_map[node_id] = {
                "id": node_id,
                "label": label,
                "type": node_type,
                "radius": 14 if node_type == "syndicate" else (11 if node_type in ("botnet", "mule") else 8),
                "details": details,
            }

    for r in fraud_records:
        syn_id = str(r.get("syndicate_id", ""))
        bot_id = str(r.get("botnet_cluster_id", ""))
        card_id = str(r.get("card_id", ""))
        merch_id = str(r.get("merchant_id", ""))
        mule_id = str(r.get("beneficiary_account_id", ""))
        amt = float(r.get("amount", 0.0))
        resp = str(r.get("response_code", "00"))

        if syn_id:
            add_node(syn_id, syn_id, "syndicate", {
                "Syndicate ID": syn_id,
                "Role": "Adversarial Threat Group",
            })

        if bot_id:
            add_node(bot_id, bot_id, "botnet", {
                "Botnet Cluster": bot_id,
                "IP Subnet": r.get("ip_subnet_prefix", "N/A"),
                "Device Fingerprint": r.get("device_fingerprint_id", "N/A"),
            })
            if syn_id:
                pair_key = f"{syn_id}->{bot_id}:OPERATES"
                link_counts[pair_key] += 1

        if card_id:
            add_node(card_id, card_id, "card", {
                "Card ID": card_id,
                "Currency": r.get("currency", "USD"),
                "Scenario": r.get("scenario_tag", ""),
                "Latest Response": f"ISO {resp}",
                "VAAI Score": r.get("vaai_score", "N/A"),
            })
            source_id = bot_id if bot_id else syn_id
            if source_id:
                pair_key = f"{source_id}->{card_id}:ATTACKS"
                link_counts[pair_key] += 1
                link_amounts[pair_key] += amt

        if merch_id:
            add_node(merch_id, merch_id, "merchant", {
                "Merchant ID": merch_id,
                "MCC": r.get("mcc", "N/A"),
                "Channel": r.get("channel_type", "N/A"),
            })
            if card_id:
                pair_key = f"{card_id}->{merch_id}:TRANSACTS"
                link_counts[pair_key] += 1
                link_amounts[pair_key] += amt

        if mule_id:
            add_node(mule_id, mule_id, "mule", {
                "Beneficiary Mule": mule_id,
                "Lien Status": r.get("cfcfrms_1930_lien_status", "NO_LIEN"),
                "Liability Tier": r.get("rbi_liability_tier", "N/A"),
            })
            if card_id:
                pair_key = f"{card_id}->{mule_id}:CASH_OUT"
                link_counts[pair_key] += 1
                link_amounts[pair_key] += amt

    for key, cnt in link_counts.items():
        src_dst, rel_type = key.split(":")
        src, dst = src_dst.split("->")
        if src in nodes_map and dst in nodes_map:
            links_list.append({
                "source": src,
                "target": dst,
                "type": rel_type,
                "count": cnt,
                "amount": round(link_amounts[key], 2),
            })

    threat_graph = {
        "nodes": list(nodes_map.values()),
        "links": links_list,
        "summary": {
            "syndicates_count": sum(1 for n in nodes_map.values() if n["type"] == "syndicate"),
            "botnets_count": sum(1 for n in nodes_map.values() if n["type"] == "botnet"),
            "cards_count": sum(1 for n in nodes_map.values() if n["type"] == "card"),
            "merchants_count": sum(1 for n in nodes_map.values() if n["type"] == "merchant"),
            "mules_count": sum(1 for n in nodes_map.values() if n["type"] == "mule"),
            "total_links": len(links_list),
        },
    }

    sample_pool = fraud_records + hard_neg_records
    remaining_slots = max(10, max_table_records - len(sample_pool))
    sample_pool += legit_records[:remaining_slots]
    sample_pool.sort(key=lambda x: float(x.get("tx_time_seconds", 0.0)))

    table_records = []
    display_fields = [
        "transaction_id", "card_id", "amount", "currency", "channel_type",
        "mcc", "scenario_tag", "is_fraud", "response_code", "hop_origin",
        "trans_status_3ds", "vaai_score", "syndicate_id", "botnet_cluster_id", "beneficiary_account_id"
    ]
    for r in sample_pool[:max_table_records]:
        table_records.append({k: r.get(k, "") for k in display_fields})

    return {
        "metadata": {
            "region": region,
            "seed": seed,
            "total_transactions": total_tx,
            "fraud_count": len(fraud_records),
            "fraud_rate_pct": round(len(fraud_records) / total_tx * 100, 2),
            "legitimate_count": len(legit_records),
            "hard_negative_count": len(hard_neg_records),
        },
        "macro_options": macro_stats,
        "switch_funnel": funnel_data,
        "temporal_series": temporal_series,
        "threat_graph": threat_graph,
        "table_records": table_records,
    }


def render_standalone_html(data_bundle: Dict[str, Any], title: str = "FraudxAI Simulation & Threat Graph Visualizer") -> str:
    """Renders a self-contained, interactive HTML5 application visualizing the simulation data bundle."""
    data_json = json.dumps(data_bundle, indent=None)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      --bg-primary: #0a0e17;
      --bg-secondary: #121826;
      --bg-card: #182234;
      --border-color: #24334c;
      --text-primary: #f0f4f8;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --accent-blue: #38bdf8;
      --accent-red: #f43f5e;
      --accent-orange: #fb923c;
      --accent-green: #10b981;
      --accent-purple: #a855f7;
      --accent-yellow: #facc15;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.5;
      overflow-x: hidden;
    }}
    header {{
      background: var(--bg-secondary);
      border-bottom: 1px solid var(--border-color);
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .brand-logo {{
      width: 28px;
      height: 28px;
      background: linear-gradient(135deg, var(--accent-red), var(--accent-orange));
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      color: white;
    }}
    .brand-title {{
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.025em;
    }}
    .badge {{
      font-size: 0.75rem;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      font-weight: 600;
    }}
    .badge-us {{ background: rgba(56, 189, 248, 0.15); color: var(--accent-blue); border: 1px solid var(--accent-blue); }}
    .badge-in {{ background: rgba(251, 146, 60, 0.15); color: var(--accent-orange); border: 1px solid var(--accent-orange); }}
    nav.tabs {{
      display: flex;
      gap: 0.5rem;
      background: var(--bg-primary);
      padding: 0.25rem;
      border-radius: 8px;
      border: 1px solid var(--border-color);
    }}
    nav.tabs button {{
      background: transparent;
      border: none;
      color: var(--text-secondary);
      padding: 0.5rem 1rem;
      font-size: 0.875rem;
      font-weight: 600;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }}
    nav.tabs button.active {{
      background: var(--bg-card);
      color: var(--accent-blue);
      box-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }}
    main {{
      padding: 1.5rem 2rem;
      max-width: 1600px;
      margin: 0 auto;
    }}
    .metrics-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 1.5rem;
    }}
    .metric-card {{
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 1rem 1.25rem;
    }}
    .metric-title {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 0.25rem;
    }}
    .metric-val {{
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--text-primary);
    }}
    .metric-sub {{
      font-size: 0.75rem;
      color: var(--text-secondary);
      margin-top: 0.25rem;
    }}
    .tab-content {{
      display: none;
    }}
    .tab-content.active {{
      display: block;
    }}
    /* Graph View */
    .graph-container {{
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      height: 750px;
      position: relative;
      overflow: hidden;
    }}
    #threat-svg {{
      width: 100%;
      height: 100%;
      cursor: grab;
    }}
    #threat-svg:active {{
      cursor: grabbing;
    }}
    .graph-legend {{
      position: absolute;
      top: 1rem;
      left: 1rem;
      background: rgba(18, 24, 38, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-size: 0.8rem;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }}
    .legend-item {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .legend-dot {{
      width: 12px;
      height: 12px;
      border-radius: 50%;
    }}
    .inspector-panel {{
      position: absolute;
      top: 1rem;
      right: 1rem;
      width: 320px;
      background: rgba(18, 24, 38, 0.95);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 1.25rem;
      font-size: 0.85rem;
      display: none;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }}
    .inspector-panel h4 {{
      font-size: 1rem;
      margin-bottom: 0.75rem;
      color: var(--accent-blue);
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 0.5rem;
    }}
    .inspector-row {{
      display: flex;
      justify-content: space-between;
      padding: 0.35rem 0;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }}
    .inspector-key {{ color: var(--text-muted); }}
    .inspector-val {{ font-weight: 600; color: var(--text-primary); text-align: right; }}
    /* Funnel View */
    .funnel-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 1.5rem;
    }}
    .hop-flow {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}
    .hop-card {{
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 1.25rem;
      position: relative;
    }}
    .hop-header {{
      display: flex;
      justify-content: space-between;
      margin-bottom: 0.5rem;
    }}
    .hop-name {{ font-weight: 700; font-size: 1rem; }}
    .hop-drop {{ color: var(--accent-red); font-weight: 700; }}
    .hop-desc {{ font-size: 0.8rem; color: var(--text-secondary); }}
    .bar-track {{
      background: rgba(255,255,255,0.05);
      height: 8px;
      border-radius: 4px;
      margin-top: 0.75rem;
      overflow: hidden;
    }}
    .bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
      border-radius: 4px;
    }}
    /* Table View */
    .table-container {{
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      overflow-x: auto;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.8rem;
      text-align: left;
    }}
    th {{
      background: var(--bg-card);
      color: var(--text-secondary);
      font-weight: 600;
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--border-color);
    }}
    td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }}
    tr:hover {{
      background: rgba(255,255,255,0.02);
    }}
    .tag-probe {{ background: rgba(56, 189, 248, 0.15); color: var(--accent-blue); padding: 0.15rem 0.4rem; border-radius: 4px; }}
    .tag-harvest {{ background: rgba(244, 63, 94, 0.15); color: var(--accent-red); padding: 0.15rem 0.4rem; border-radius: 4px; }}
    .tag-drain {{ background: rgba(251, 146, 60, 0.15); color: var(--accent-orange); padding: 0.15rem 0.4rem; border-radius: 4px; }}
    .tag-hardneg {{ background: rgba(250, 204, 21, 0.15); color: var(--accent-yellow); padding: 0.15rem 0.4rem; border-radius: 4px; }}
    .tag-legit {{ color: var(--text-muted); }}
    .resp-00 {{ color: var(--accent-green); font-weight: 700; }}
    .resp-decl {{ color: var(--accent-red); font-weight: 700; }}
  </style>
  <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>

  <header>
    <div class="brand">
      <div class="brand-logo">FX</div>
      <div class="brand-title">FraudxAI Visualizer</div>
      <span class="badge badge-{data_bundle['metadata']['region'].lower()}">{data_bundle['metadata']['region']} PAYMENT RAILS</span>
    </div>
    <nav class="tabs">
      <button class="active" onclick="switchTab('tab-threat')">Cybercrime Threat Graph</button>
      <button onclick="switchTab('tab-switch')">4-Hop Switch Funnel</button>
      <button onclick="switchTab('tab-temporal')">Hawkes Event Timeline</button>
      <button onclick="switchTab('tab-table')">Live Transaction Stream</button>
    </nav>
  </header>

  <main>
    <div class="metrics-bar">
      <div class="metric-card">
        <div class="metric-title">Total Batch Volume</div>
        <div class="metric-val">{data_bundle['metadata']['total_transactions']:,}</div>
        <div class="metric-sub">{data_bundle['metadata']['legitimate_count']:,} Organic, {data_bundle['metadata']['hard_negative_count']:,} Hard Negatives</div>
      </div>
      <div class="metric-card">
        <div class="metric-title">Adversarial Fraud Attack Rate</div>
        <div class="metric-val" style="color: var(--accent-red);">{data_bundle['metadata']['fraud_rate_pct']}%</div>
        <div class="metric-sub">{data_bundle['metadata']['fraud_count']:,} Fraud ({data_bundle['metadata']['total_transactions'] - data_bundle['metadata']['fraud_count']:,} Legit Cardholder)</div>
      </div>
      <div class="metric-card">
        <div class="metric-title">Core Banking Approvals</div>
        <div class="metric-val" style="color: var(--accent-green);">{data_bundle['switch_funnel']['approval_rate']}%</div>
        <div class="metric-sub">{data_bundle['switch_funnel']['approved']:,} Approved | {data_bundle['switch_funnel']['declined']:,} Declined ({round(data_bundle['switch_funnel']['declined'] / max(1, data_bundle['switch_funnel']['total_ingress']) * 100, 1)}%)</div>
      </div>
      <div class="metric-card">
        <div class="metric-title">Threat Graph Enclave</div>
        <div class="metric-val" style="color: var(--accent-purple);">{data_bundle['threat_graph']['summary']['syndicates_count']} Syndicates</div>
        <div class="metric-sub">{data_bundle['threat_graph']['summary']['botnets_count']} Botnets, {data_bundle['threat_graph']['summary']['cards_count']} Cards, {data_bundle['threat_graph']['summary']['mules_count']} Mules</div>
      </div>
    </div>

    <!-- TAB 1: THREAT GRAPH -->
    <div id="tab-threat" class="tab-content active">
      <div class="graph-container">
        <div class="graph-legend">
          <div class="legend-item"><div class="legend-dot" style="background: #f43f5e;"></div> Syndicate Group</div>
          <div class="legend-item"><div class="legend-dot" style="background: #fb923c;"></div> Botnet / Proxy Cluster</div>
          <div class="legend-item"><div class="legend-dot" style="background: #a855f7;"></div> Compromised Card Target</div>
          <div class="legend-item"><div class="legend-dot" style="background: #38bdf8;"></div> Merchant / MCC Terminal</div>
          <div class="legend-item"><div class="legend-dot" style="background: #10b981;"></div> Cash-Out Mule Account</div>
        </div>

        <div id="inspector" class="inspector-panel">
          <h4 id="inspect-title">Entity Inspector</h4>
          <div id="inspect-body"></div>
        </div>

        <svg id="threat-svg"></svg>
      </div>
    </div>

    <!-- TAB 2: 4-HOP SWITCH FUNNEL -->
    <div id="tab-switch" class="tab-content">
      <div class="funnel-grid">
        <div class="hop-flow">
          <h3>4-Hop Banking Switch Pipeline</h3>
          <div id="hop-cards-container"></div>
        </div>
        <div class="metric-card">
          <h3>ISO 8583 Response Code Distribution</h3>
          <div id="iso-breakdown" style="margin-top: 1rem; display: flex; flex-direction: column; gap: 0.5rem;"></div>
        </div>
      </div>
    </div>

    <!-- TAB 3: TEMPORAL HAWKES TIMELINE -->
    <div id="tab-temporal" class="tab-content">
      <div class="metric-card" style="height: 500px; display: flex; flex-direction: column;">
        <h3>Circadian 24-Hour Spending & Attack Kinetics</h3>
        <p style="font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 1rem;">
          Shows Hawkes process inter-arrival dynamics: legitimate daytime spend curve (blue) vs. nocturnal adversary bursts & carding sweeps (red).
        </p>
        <svg id="timeline-svg" style="width: 100%; flex: 1;"></svg>
      </div>
    </div>

    <!-- TAB 4: TRANSACTION TABLE -->
    <div id="tab-table" class="tab-content">
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>TX ID</th>
              <th>Card ID</th>
              <th>Amount</th>
              <th>Channel</th>
              <th>MCC</th>
              <th>Scenario / Intent</th>
              <th>Response</th>
              <th>Hop Origin</th>
              <th>VAAI</th>
              <th>Syndicate</th>
            </tr>
          </thead>
          <tbody id="table-body"></tbody>
        </table>
      </div>
    </div>
  </main>

  <script>
    const DATA = {data_json};

    function switchTab(tabId) {{
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('nav.tabs button').forEach(el => el.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
      event.target.classList.add('active');

      if (tabId === 'tab-threat') initThreatGraph();
      if (tabId === 'tab-switch') initSwitchFunnel();
      if (tabId === 'tab-temporal') initTimeline();
      if (tabId === 'tab-table') initTable();
    }}

    // 1. Force-Directed Threat Graph
    let graphInitialized = false;
    function initThreatGraph() {{
      if (graphInitialized) return;
      graphInitialized = true;

      const svg = d3.select("#threat-svg");
      const width = document.querySelector(".graph-container").clientWidth;
      const height = document.querySelector(".graph-container").clientHeight;

      const g = svg.append("g");
      const zoom = d3.zoom().scaleExtent([0.1, 4]).on("zoom", (event) => {{
        g.attr("transform", event.transform);
      }});
      svg.call(zoom);

      const colorMap = {{
        syndicate: "#f43f5e",
        botnet: "#fb923c",
        card: "#a855f7",
        merchant: "#38bdf8",
        mule: "#10b981"
      }};

      const nodes = DATA.threat_graph.nodes.map(d => Object.create(d));
      const links = DATA.threat_graph.links.map(d => Object.create(d));

      const simulation = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(links).id(d => d.id).distance(60))
        .force("charge", d3.forceManyBody().strength(-120))
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("collision", d3.forceCollide().radius(d => d.radius + 8));

      const link = g.append("g")
        .selectAll("line")
        .data(links)
        .join("line")
        .attr("stroke", "rgba(255,255,255,0.15)")
        .attr("stroke-width", d => Math.min(4, Math.max(1, d.count)));

      const node = g.append("g")
        .selectAll("circle")
        .data(nodes)
        .join("circle")
        .attr("r", d => d.radius)
        .attr("fill", d => colorMap[d.type] || "#ffffff")
        .attr("stroke", "#0a0e17")
        .attr("stroke-width", 2)
        .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

      node.on("click", (event, d) => {{
        showInspector(d);
      }});

      node.append("title").text(d => `${{d.type.toUpperCase()}}: ${{d.label}}`);

      simulation.on("tick", () => {{
        link
          .attr("x1", d => d.source.x)
          .attr("y1", d => d.source.y)
          .attr("x2", d => d.target.x)
          .attr("y2", d => d.target.y);

        node
          .attr("cx", d => d.x)
          .attr("cy", d => d.y);
      }});

      function dragstarted(event, d) {{
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      }}
      function dragged(event, d) {{
        d.fx = event.x;
        d.fy = event.y;
      }}
      function dragended(event, d) {{
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      }}
    }}

    function showInspector(d) {{
      const panel = document.getElementById("inspector");
      const title = document.getElementById("inspect-title");
      const body = document.getElementById("inspect-body");

      title.innerText = `${{d.type.toUpperCase()}}: ${{d.label}}`;
      let htmlContent = "";
      for (const [k, v] of Object.entries(d.details || {{}})) {{
        htmlContent += `<div class="inspector-row"><span class="inspector-key">${{k}}</span><span class="inspector-val">${{v}}</span></div>`;
      }}
      body.innerHTML = htmlContent;
      panel.style.display = "block";
    }}

    // 2. 4-Hop Banking Switch Pipeline
    function initSwitchFunnel() {{
      const container = document.getElementById("hop-cards-container");
      container.innerHTML = "";
      DATA.switch_funnel.hops.forEach(hop => {{
        const card = document.createElement("div");
        card.className = "hop-card";
        card.innerHTML = `
          <div class="hop-header">
            <span class="hop-name">${{hop.name}}</span>
            <span class="hop-drop">${{hop.drop_count}} Drops (${{hop.drop_pct}}%)</span>
          </div>
          <div class="hop-desc">${{hop.description}}</div>
          <div class="bar-track">
            <div class="bar-fill" style="width: ${{Math.min(100, Math.max(4, hop.drop_pct * 4))}}%"></div>
          </div>
        `;
        container.appendChild(card);
      }});

      const isoBox = document.getElementById("iso-breakdown");
      isoBox.innerHTML = "";
      DATA.switch_funnel.iso_distribution.forEach(iso => {{
        isoBox.innerHTML += `
          <div style="display: flex; justify-content: space-between; font-size: 0.85rem; padding: 0.25rem 0;">
            <span>ISO ${{iso.code}}</span>
            <span style="font-weight: 700;">${{iso.count}} tx (${{iso.pct}}%)</span>
          </div>
        `;
      }});
    }}

    // 3. Temporal Hawkes Timeline (SVG)
    function initTimeline() {{
      const svg = d3.select("#timeline-svg");
      svg.selectAll("*").remove();

      const width = document.querySelector("#timeline-svg").clientWidth;
      const height = 400;
      const margin = {{ top: 20, right: 30, bottom: 40, left: 50 }};

      const x = d3.scaleLinear().domain([0, 23]).range([margin.left, width - margin.right]);
      const maxVol = d3.max(DATA.temporal_series, d => d.legit + d.fraud + d.hard_neg) || 10;
      const y = d3.scaleLinear().domain([0, maxVol * 1.1]).range([height - margin.bottom, margin.top]);

      svg.append("g")
        .attr("transform", `translate(0,${{height - margin.bottom}})`)
        .call(d3.axisBottom(x).ticks(24).tickFormat(d => `${{d}}:00`))
        .attr("color", "#64748b");

      svg.append("g")
        .attr("transform", `translate(${{margin.left}},0)`)
        .call(d3.axisLeft(y).ticks(6))
        .attr("color", "#64748b");

      // Legit line (blue)
      const legitLine = d3.line().x(d => x(d.hour)).y(d => y(d.legit));
      svg.append("path")
        .datum(DATA.temporal_series)
        .attr("fill", "none")
        .attr("stroke", "#38bdf8")
        .attr("stroke-width", 2)
        .attr("d", legitLine);

      // Fraud line (red)
      const fraudLine = d3.line().x(d => x(d.hour)).y(d => y(d.fraud));
      svg.append("path")
        .datum(DATA.temporal_series)
        .attr("fill", "none")
        .attr("stroke", "#f43f5e")
        .attr("stroke-width", 3)
        .attr("d", fraudLine);
    }}

    // 4. Live Transaction Stream Table
    function initTable() {{
      const tbody = document.getElementById("table-body");
      tbody.innerHTML = "";
      DATA.table_records.forEach(r => {{
        let tagClass = "tag-legit";
        if (r.scenario_tag.includes("PROBE")) tagClass = "tag-probe";
        else if (r.scenario_tag.includes("HARVEST")) tagClass = "tag-harvest";
        else if (r.scenario_tag.includes("DRAIN")) tagClass = "tag-drain";
        else if (r.scenario_tag.includes("HARD_NEGATIVE")) tagClass = "tag-hardneg";

        const respClass = (r.response_code === "00" || r.response_code === "10") ? "resp-00" : "resp-decl";

        tbody.innerHTML += `
          <tr>
            <td><code>${{r.transaction_id}}</code></td>
            <td><code>${{r.card_id}}</code></td>
            <td style="font-weight: 600;">$${{parseFloat(r.amount).toFixed(2)}}</td>
            <td>${{r.channel_type}}</td>
            <td>${{r.mcc}}</td>
            <td><span class="${{tagClass}}">${{r.scenario_tag}}</span></td>
            <td class="${{respClass}}">ISO ${{r.response_code}}</td>
            <td>${{r.hop_origin}}</td>
            <td>${{r.vaai_score || "—"}}</td>
            <td>${{r.syndicate_id || "—"}}</td>
          </tr>
        `;
      }});
    }}

    // Auto-init on load
    window.addEventListener("DOMContentLoaded", () => {{
      initThreatGraph();
    }});
  </script>
</body>
</html>
"""


def generate_visualization_file(
    output_path: str = "reports/fraudx_visualizer.html",
    n_transactions: int = 1500,
    region: str = "US",
    fraud_rate: float = 0.04,
    adversary_mode: str = "intent",
    seed: int = 42,
    open_browser: bool = False,
) -> Path:
    """Generates a synthetic simulation batch and compiles it into an interactive HTML visualizer file."""
    engine = SimulationEngine(
        n_cards=80,
        n_merchants=120,
        region=region,
        adversary_mode=adversary_mode,
        seed=seed,
    )
    records = engine.generate_batch(
        n_transactions=n_transactions,
        fraud_prevalence=fraud_rate,
        time_span_days=14,
    )

    bundle = compile_simulation_data_bundle(records, region=region, seed=seed)
    html_content = render_standalone_html(bundle, title=f"FraudxAI {region} Threat Graph Visualizer")

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(html_content, encoding="utf-8")

    if open_browser:
        import webbrowser
        webbrowser.open(out_file.resolve().as_uri())

    return out_file


def compile_bundle_from_metadata(
    meta: Dict[str, Any],
    threat_graph_sample: Optional[Dict[str, Any]] = None,
    sample_records: Optional[List[Dict[str, Any]]] = None,
    max_nodes: int = 5000,
) -> Dict[str, Any]:
    """Compiles a visualization bundle from high-scale simulation metadata and threat samples."""
    total_tx = int(meta.get("total_transactions", 0))
    fraud_count = int(meta.get("total_fraud_count", 0))
    legit_count = total_tx - fraud_count
    approved_count = int(meta.get("approved_count", 0))
    declined_count = int(meta.get("declined_count", 0))

    region = str(meta.get("region", "US"))
    total_vol = float(meta.get("total_volume", 0.0))
    fraud_vol = float(meta.get("total_fraud_volume", 0.0))

    # Macro-options breakdown
    macro_stats = []
    for sc, cnt in meta.get("macro_options", {}).items():
        macro_stats.append({
            "scenario": sc,
            "count": cnt,
            "pct": round(cnt / max(1, fraud_count) * 100, 1),
            "amount_min": 0.0,
            "amount_median": 0.0,
            "amount_max": 0.0,
            "amount_sum": 0.0,
        })

    # 4-Hop Funnel Drops
    hop_drops = meta.get("hop_drops", {})
    gateway_drops = hop_drops.get("GATEWAY_FILTER", 0)
    vaai_drops = hop_drops.get("NETWORK_SWITCH_VAAI", 0)
    acs_drops = hop_drops.get("ACS_3DS", 0)
    # The transactions that drop at Hop 4 are the remaining declines that reached the issuer host
    issuer_drops = max(0, declined_count - (gateway_drops + vaai_drops + acs_drops))

    funnel_data = {
        "total_ingress": total_tx,
        "approved": approved_count,
        "declined": declined_count,
        "approval_rate": round(approved_count / max(1, total_tx) * 100, 1),
        "decline_rate": round(declined_count / max(1, total_tx) * 100, 1),
        "hops": [
            {
                "id": "hop_1",
                "name": "Hop 1: Gateway Edge Filter",
                "description": "Browser Canvas Invariance, IP Reputation (>=85), Kinematic Supersonic Velocity",
                "drop_count": gateway_drops,
                "drop_pct": round(gateway_drops / max(1, total_tx) * 100, 2),
            },
            {
                "id": "hop_2",
                "name": "Hop 2: Network Switch In-Flight ML",
                "description": "Visa Account Attack Intelligence (VAAI Field 44.5 >= 75) Carding Intercept",
                "drop_count": vaai_drops,
                "drop_pct": round(vaai_drops / max(1, total_tx) * 100, 2),
            },
            {
                "id": "hop_3",
                "name": "Hop 3: 3DS Access Control Server",
                "description": "PSD2 Low-Value (<$30) & TRA (<$100) Exemptions vs 2FA Step-Up Challenge Drops",
                "drop_count": acs_drops,
                "drop_pct": round(acs_drops / max(1, total_tx) * 100, 2),
            },
            {
                "id": "hop_4",
                "name": "Hop 4: Issuer Core Banking Host",
                "description": "DDA Solvency (ISO 51), Balance Oracle (ISO 10), Hourly Velocity (ISO 65), STIP (ISO 91)",
                "drop_count": issuer_drops,
                "drop_pct": round(issuer_drops / max(1, total_tx) * 100, 2),
            },
        ],
    }

    # Temporal series
    h_legit = meta.get("hourly_legitimate", [0] * 24)
    h_fraud = meta.get("hourly_fraud", [0] * 24)
    temporal_series = [
        {
            "hour": h,
            "legit": h_legit[h] if h < len(h_legit) else 0,
            "fraud": h_fraud[h] if h < len(h_fraud) else 0,
            "hard_neg": 0,
            "total_amount": 0.0,
        }
        for h in range(24)
    ]

    # Threat Graph Construction from Sample
    raw_nodes = []
    raw_links = []
    if threat_graph_sample:
        raw_nodes = threat_graph_sample.get("nodes", [])
        raw_links = threat_graph_sample.get("links", [])

    # Filter to top max_nodes
    if len(raw_nodes) > max_nodes:
        raw_nodes = sorted(raw_nodes, key=lambda n: n.get("volume", 0), reverse=True)[:max_nodes]
    retained_ids = {n["id"] for n in raw_nodes}

    filtered_links = []
    for l in raw_links:
        if l["source"] in retained_ids and l["target"] in retained_ids:
            filtered_links.append(l)

    formatted_nodes = []
    for n in raw_nodes:
        n_type = str(n.get("type", "card")).lower()
        formatted_nodes.append({
            "id": n["id"],
            "label": n.get("label", n["id"]),
            "type": n_type,
            "radius": 14 if n_type == "syndicate" else (11 if n_type in ("botnet", "mule_ring", "mule") else 8),
            "details": {
                "Entity ID": n["id"],
                "Entity Type": n_type.upper(),
                "Associated Volume": n.get("volume", 1),
            },
        })

    threat_graph = {
        "nodes": formatted_nodes,
        "links": filtered_links,
        "summary": {
            "syndicates_count": sum(1 for n in formatted_nodes if n["type"] == "syndicate"),
            "botnets_count": sum(1 for n in formatted_nodes if n["type"] == "botnet"),
            "cards_count": sum(1 for n in formatted_nodes if n["type"] == "card"),
            "merchants_count": sum(1 for n in formatted_nodes if n["type"] == "merchant"),
            "mules_count": sum(1 for n in formatted_nodes if "mule" in n["type"]),
            "total_links": len(filtered_links),
        },
    }

    # Compute hard negative count from macro options
    hard_neg_count = sum(cnt for sc, cnt in meta.get("macro_options", {}).items() if "HARD_NEGATIVE" in sc)
    organic_legit_count = max(0, legit_count - hard_neg_count)

    return {
        "metadata": {
            "region": region,
            "seed": 42,
            "total_transactions": total_tx,
            "fraud_count": fraud_count,
            "fraud_rate_pct": round(fraud_count / max(1, total_tx) * 100, 2),
            "legitimate_count": organic_legit_count,
            "hard_negative_count": hard_neg_count,
            "total_volume_usd": total_vol,
            "fraud_volume_usd": fraud_vol,
        },
        "macro_options": macro_stats,
        "switch_funnel": funnel_data,
        "temporal_series": temporal_series,
        "threat_graph": threat_graph,
        "table_records": sample_records or [],
    }


def generate_visualization_from_dir(
    input_dir: str | Path,
    output_path: str = "reports/fraudx_visualizer_scale.html",
    max_nodes: int = 5000,
    open_browser: bool = False,
) -> Path:
    """Renders visualizer dashboard from high-scale simulation output directory."""
    in_path = Path(input_dir)
    meta_path = in_path / "master_simulation_metadata.json"
    if not meta_path.exists():
        meta_path = in_path / "simulation_metadata.json"
    if not meta_path.exists():
        raise FileNotFoundError(f"Simulation metadata not found in {input_dir}")

    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    # Load threat graph sample if present
    graph_path = in_path / "threat_graph_sample.json"
    threat_sample = None
    if graph_path.exists():
        threat_sample = json.loads(graph_path.read_text(encoding="utf-8"))
    else:
        # Check sub-worker directories
        for w_dir in in_path.glob("worker_*"):
            w_graph = w_dir / "threat_graph_sample.json"
            if w_graph.exists():
                threat_sample = json.loads(w_graph.read_text(encoding="utf-8"))
                break

    # Sample a few records from parquet if available
    sample_records = []
    try:
        import polars as pl
        pq_files = list(in_path.glob("**/*.parquet"))
        if pq_files:
            auth_pqs = [f for f in pq_files if "auth_stream" in str(f)]
            target_pq = auth_pqs[0] if auth_pqs else pq_files[0]
            df = pl.read_parquet(target_pq).head(150)
            sample_records = df.to_dicts()
    except Exception:
        pass

    bundle = compile_bundle_from_metadata(
        meta=meta,
        threat_graph_sample=threat_sample,
        sample_records=sample_records,
        max_nodes=max_nodes,
    )

    region = str(meta.get("region", "US"))
    total_tx = int(meta.get("total_transactions", 0))
    html_content = render_standalone_html(
        bundle,
        title=f"FraudxAI Scale Visualizer - {total_tx:,} Transactions ({region})",
    )

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(html_content, encoding="utf-8")

    if open_browser:
        import webbrowser
        webbrowser.open(out_file.resolve().as_uri())

    return out_file

