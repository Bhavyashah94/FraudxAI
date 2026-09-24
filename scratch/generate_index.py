import os
import re
import yaml
import sys

sys.stdout.reconfigure(encoding='utf-8')

PAPERS_DIR = "docs/papers"

files = [f for f in os.listdir(PAPERS_DIR) if f.endswith('.md') and f not in ['README.md', 'INDEX.md']]

records = []
for f in files:
    md_path = os.path.join(PAPERS_DIR, f)
    pdf_name = f.replace('.md', '.pdf')
    pdf_path = os.path.join(PAPERS_DIR, pdf_name)
    has_pdf = os.path.exists(pdf_path)
    
    with open(md_path, 'r', encoding='utf-8', errors='ignore') as m:
        content = m.read(4000)
    
    # parse frontmatter
    title = f.replace('.md', '').replace('_', ' ')
    year = "2024"
    authors = "Unknown"
    domain = "General ML"
    
    fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        for line in fm_text.split('\n'):
            if line.startswith('title:'):
                title = line.replace('title:', '').strip(' "')
            elif line.startswith('year:'):
                year = line.replace('year:', '').strip(' "')
            elif line.startswith('authors:'):
                authors = line.replace('authors:', '').strip(' "')
            elif line.startswith('domain:'):
                domain = line.replace('domain:', '').strip(' "')
                
    records.append({
        "slug": f.replace('.md', ''),
        "md_file": f,
        "pdf_file": pdf_name if has_pdf else None,
        "title": title,
        "year": str(year),
        "authors": authors,
        "domain": domain
    })

# Sort by year descending, then slug
records.sort(key=lambda r: (r['year'], r['slug']), reverse=True)

# Write INDEX.md
index_path = os.path.join(PAPERS_DIR, "INDEX.md")
with open(index_path, "w", encoding="utf-8") as out:
    out.write("# 📚 FraudxAI: Complete Research Paper Catalog (Markdown & PDF)\n\n")
    out.write("This directory contains **100+ fully transcribed research papers converted into GitHub-flavored Markdown (`.md`)** alongside their original PDFs.\n\n")
    out.write("Every paper can now be directly inspected, searched, and cited using plain Markdown text.\n\n")
    out.write("---\n\n")
    out.write("## 🌟 Core Credit Card Fraud & Explainable AI (XAI) Papers\n\n")
    out.write("| Year | Paper Title | Authors / Institution | Markdown Text | PDF Source |\n")
    out.write("| :--- | :--- | :--- | :---: | :---: |\n")
    
    # Priority fraud papers
    core_slugs = [
        "2025_walauskis_shap_feature_selection_unsupervised_fraud_labeling",
        "2026_fazel_improving_credit_card_fraud_explainable_boosting_machine",
        "2026_wu_dollar_metric_credit_card_fraud_temporal_shap_audit",
        "2024_duan_cat_gnn_causal_temporal_graph_fraud_detection",
        "2026_yan_temporal_heterogeneous_graph_transformer_fraud_detection",
        "2020_rao_xfraud_explainable_fraud_transaction_detection",
        "2015_dal_pozzolo_adaptive_machine_learning_credit_card_fraud",
        "2020_kumar_problems_with_shapley_value_feature_importance",
        "2023_hedstrom_quantus_responsible_evaluation_xai",
        "2019_rudin_stop_explaining_black_box_high_stakes",
        "2022_jesus_turning_tables_biased_imbalanced_tabular",
        "2017_lundberg_unified_approach_interpreting_model_predictions_shap"
    ]
    
    for slug in core_slugs:
        rec = next((r for r in records if r['slug'] == slug), None)
        if rec:
            pdf_link = f"[`{rec['slug']}.pdf`](file:///c:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/{rec['pdf_file']})" if rec['pdf_file'] else "N/A"
            md_link = f"[`{rec['slug']}.md`](file:///c:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/{rec['md_file']})"
            out.write(f"| **{rec['year']}** | **{rec['title']}** | {rec['authors']} | [📖 Read .md]({rec['md_file']}) | [📄 Open .pdf]({rec['pdf_file']}) |\n")

    out.write("\n---\n\n")
    out.write("## 🗂️ Complete Alphabetical & Chronological Archive\n\n")
    out.write("| Year | Slug / Filename | Paper Title | Links |\n")
    out.write("| :---: | :--- | :--- | :--- |\n")
    
    for rec in records:
        out.write(f"| {rec['year']} | `{rec['slug']}` | {rec['title']} | [📖 .md]({rec['md_file']}) &bull; [📄 .pdf]({rec['pdf_file']}) |\n")

print(f"Generated {index_path} with {len(records)} entries.")
