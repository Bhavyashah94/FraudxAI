import os
import re
import shutil
import pymupdf
import pymupdf4llm
import sys

sys.stdout.reconfigure(encoding='utf-8')

core_papers = [
    {
        "src": "walauskis_khoshgoftaar_ieee_access_2025.pdf",
        "slug": "2025_walauskis_shap_feature_selection_unsupervised_fraud_labeling",
        "title": "SHAP-Based Feature Selection for Enhanced Unsupervised Labeling",
        "authors": "Mary Anne Walauskis, Taghi M. Khoshgoftaar",
        "year": 2025,
        "venue": "IEEE Access (Vol. 13)",
        "domain": "XAI & Feature Selection in Credit Card Fraud"
    },
    {
        "src": "fazel_2026_credit_card_fraud_explainable_ebm.pdf",
        "slug": "2026_fazel_improving_credit_card_fraud_explainable_boosting_machine",
        "title": "Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine",
        "authors": "Reza E. Fazel, Arash Bakhtiary, Siavash A. Bigdeli",
        "year": 2026,
        "venue": "arXiv / EN Bank Credit and Collection Department",
        "domain": "Inherently Interpretable EBM / Glass-Box Credit Card Fraud"
    },
    {
        "src": "wu_2026_credit_card_fraud_temporal_shap_audit.pdf",
        "slug": "2026_wu_dollar_metric_credit_card_fraud_temporal_shap_audit",
        "title": "Class Weighting versus Amount Conditioning in Credit-Card Fraud Detection: A Dollar-Metric Study with a Temporal Explanation Audit",
        "authors": "Chenyu Wu",
        "year": 2026,
        "venue": "arXiv / Duke University",
        "domain": "Dollar-Metric Loss & Temporal SHAP Attribution Drift Audit"
    },
    {
        "src": "2402.14708.pdf",
        "slug": "2024_duan_cat_gnn_causal_temporal_graph_fraud_detection",
        "title": "CaT-GNN: Enhancing Credit Card Fraud Detection via Causal Temporal Graph Neural Networks",
        "authors": "Yifan Duan, Guibin Zhang, Shilong Wang, et al.",
        "year": 2024,
        "venue": "arXiv cs.LG / USTC & Peking University",
        "domain": "Causal Graph Neural Networks for Card Fraud"
    },
    {
        "src": "2609.07100.pdf",
        "slug": "2026_yan_temporal_heterogeneous_graph_transformer_fraud_detection",
        "title": "Temporal Heterogeneous Graph Transformer for Credit Card Fraud Detection (THGT-FD)",
        "authors": "Qinwen Yan",
        "year": 2026,
        "venue": "arXiv cs.LG / UCLA",
        "domain": "Relational Graph Transformers & Time2Vec Encodings"
    },
    {
        "src": "2011.12193.pdf",
        "slug": "2020_rao_xfraud_explainable_fraud_transaction_detection",
        "title": "xFraud: Explainable Fraud Transaction Detection on Bi-Relational Graph Neural Networks",
        "authors": "Susie Xi Rao, Shuai Zhang, Zhichao Han, Ce Zhang, et al.",
        "year": 2020,
        "venue": "ACM CIKM / ETH Zurich & eBay",
        "domain": "Industry Production Graph Explainer for Fraud Ops Analysts"
    },
    {
        "src": "dal_pozzolo_2015_adaptive_machine_learning_credit_card_fraud.pdf",
        "slug": "2015_dal_pozzolo_adaptive_machine_learning_credit_card_fraud",
        "title": "Adaptive Machine Learning for Credit Card Fraud Detection",
        "authors": "Andrea Dal Pozzolo",
        "year": 2015,
        "venue": "Université Libre de Bruxelles & Worldline (IEEE TNNLS)",
        "domain": "Foundational Credit Card Fraud Benchmark & Verification Latency"
    },
    {
        "src": "2002.11097.pdf",
        "slug": "2020_kumar_problems_with_shapley_value_feature_importance",
        "title": "Problems with Shapley-value-based explanations as feature importance measures",
        "authors": "I. Elizabeth Kumar, Suresh Venkatasubramanian, Carlos Scheidegger, Sorelle A. Friedler",
        "year": 2020,
        "venue": "ICML 2020",
        "domain": "Mathematical Proof of Correlation Leakage in SHAP"
    },
    {
        "src": "2202.06861.pdf",
        "slug": "2023_hedstrom_quantus_responsible_evaluation_xai",
        "title": "Quantus: An Explainable AI Toolkit for Responsible Evaluation of Neural Network Explanations",
        "authors": "Anna Hedström, Leander Weber, Dilyara Bareeva, et al.",
        "year": 2023,
        "venue": "Journal of Machine Learning Research (JMLR)",
        "domain": "Evaluation Benchmarks & Faithfulness Metrics for XAI"
    },
    {
        "src": "1811.10154.pdf",
        "slug": "2019_rudin_stop_explaining_black_box_high_stakes",
        "title": "Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead",
        "authors": "Cynthia Rudin",
        "year": 2019,
        "venue": "Nature Machine Intelligence",
        "domain": "Axiomatic Critique of Post-Hoc Explanations in High Stakes Domains"
    },
    {
        "src": "2211.13358.pdf",
        "slug": "2022_jesus_turning_tables_biased_imbalanced_tabular",
        "title": "Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation",
        "authors": "Sérgio Jesus, José Pombal, Duarte Alves, et al.",
        "year": 2022,
        "venue": "NeurIPS Datasets and Benchmarks Track / Feedzai",
        "domain": "Bank Account Fraud (BAF) Realism & Streaming Evaluation"
    },
    {
        "src": "1705.07874.pdf",
        "slug": "2017_lundberg_unified_approach_interpreting_model_predictions_shap",
        "title": "A Unified Approach to Interpreting Model Predictions (SHAP)",
        "authors": "Scott M. Lundberg, Su-In Lee",
        "year": 2017,
        "venue": "NeurIPS 2017",
        "domain": "Foundational Additive Feature Attribution (TreeSHAP)"
    }
]

papers_dir = "docs/papers"
print(f"Converting {len(core_papers)} core papers to clean Markdown...")

for item in core_papers:
    src_file = os.path.join(papers_dir, item["src"])
    if not os.path.exists(src_file):
        print(f"Warning: {src_file} does not exist, skipping.")
        continue
    
    target_pdf = os.path.join(papers_dir, item["slug"] + ".pdf")
    target_md = os.path.join(papers_dir, item["slug"] + ".md")
    
    # 1. Rename/copy PDF to clean slug
    if src_file != target_pdf:
        shutil.copy2(src_file, target_pdf)
        print(f"Copied PDF: {item['src']} -> {item['slug']}.pdf")
    
    # 2. Extract full text to Markdown
    print(f"Converting {item['slug']} to markdown...")
    try:
        md_content = pymupdf4llm.to_markdown(target_pdf)
        
        # 3. Add frontmatter
        frontmatter = f"""---
title: "{item['title']}"
authors: "{item['authors']}"
year: {item['year']}
venue: "{item['venue']}"
domain: "{item['domain']}"
pdf_path: "{target_pdf}"
---

# {item['title']}

**Authors:** {item['authors']}  
**Venue / Date:** {item['venue']} ({item['year']})  
**Domain Focus:** {item['domain']}  
**Original PDF:** [`{item['slug']}.pdf`](file:///{os.path.abspath(target_pdf).replace(chr(92), '/')})

---

"""
        full_md = frontmatter + md_content
        with open(target_md, "w", encoding="utf-8") as f:
            f.write(full_md)
        print(f"  -> Generated {target_md} ({len(full_md)} chars)")
    except Exception as e:
        print(f"  -> Error converting {item['slug']}: {e}")

print("Core papers processing completed successfully.")
