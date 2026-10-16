# Downloaded Academic Research Corpus

This directory stores the complete, open-access full-text PDF documents retrieved for **FraudxAI** literature evaluations.

## Summary Statistics
* **Total PDF files on disk**: 94 (**85 unique documents**; 9 are byte-identical
  duplicates stored under two naming schemes — see "Known duplicates" below)
* **Total Markdown transcriptions**: 94 (one per PDF file, including the duplicates)
* **Total Corpus Size**: ~263 MB
* **Manifest Registry**: [`manifest.json`](manifest.json)
* **Status**: 100% verified magic bytes (`%PDF-`), validated, and indexed.

### Known duplicates (pending dedup)
Nine papers exist twice under two filenames (`md5`-identical `.pdf` and `.md`), so
any count that reads this directory as "number of papers" over-reports by 9. Both
copies of every pair appear in `INDEX.md`; the pairs differ only in whether the file
is also listed in the machine-readable `papers_registry.json`:

| In `papers_registry.json` | In `INDEX.md` only |
| :--- | :--- |
| `2026_yan_temporal_heterogeneous_graph_transf` | `2026_yan_temporal_heterogeneous_graph_transformer_fraud_detection` |
| `2024_networks_catgnn_enhancing_credit_card_fraud` | `2024_duan_cat_gnn_causal_temporal_graph_fraud_detection` |
| `2022_hedstrm_quantus_an_explainable_ai_toolkit_f` | `2023_hedstrom_quantus_responsible_evaluation_xai` |
| `2017_unknown_a_unified_approach_to_interpreting` | `2017_lundberg_unified_approach_interpreting_model_predictions_shap` |
| `2020_zhao_xfraud_explainable_fraud_transactio` | `2020_rao_xfraud_explainable_fraud_transaction_detection` |
| `2018_instead_stop_explaining_black_box_machine_l` | `2019_rudin_stop_explaining_black_box_high_stakes` |
| `2019_yoon_timeseries_generative_adversarial_n` | `2020_timegan_yoon2019` |
| `2020_measures_problems_with_shapleyvaluebased_exp` | `2020_kumar_problems_with_shapley_value_feature_importance` |
| `2022_evaluation_turning_the_tables_biased_imbalance` | `2022_jesus_turning_tables_biased_imbalanced_tabular` |

## Corpus Organization by Battleground

### 1. Explainable AI & Interpretability (Cluster 1)
* **Supporting / Foundational**: Quantus (`2202.06861.pdf`), OpenXAI (`2206.11104.pdf`), TreeSHAP, Integrated Gradients, GA2M/EBM, FastSHAP.
* **Opposing / Critical**: Cynthia Rudin - Stop Explaining Black Box Models (`1811.10154.pdf`), Kumar et al. - Problems with Shapley Values (`2002.11097.pdf`), Slack et al. - Fooling LIME and SHAP (`1911.02508.pdf`), Dimanov et al. - Concealing Biases (`2001.00000+`).

### 2. Synthetic Data Generation: DES vs. Deep Generative Models (Cluster 2)
* **Supporting / Foundational**: PaySim, ABIDES (`1904.12066.pdf`), Hawkes Point Process Models, Causal Representation Learning (`2102.11107.pdf`), New Money Financial Review (`2510.15096.pdf`, `2510.26076.pdf`).
* **Opposing / Critical (Deep Generative Models)**: TabDDPM (`2209.15421.pdf`), CTGAN / TVAE (`1907.00503.pdf`), TimeGAN (`1910.08260.pdf`, `1909.06711.pdf`), TabNet (`1908.07442.pdf`), CTAB-GAN (`2102.08369.pdf`), CTAB-GAN+ (`2204.00401.pdf`), STaSy (`2210.04018.pdf`), Quant GANs (`1907.13188.pdf`).

### 3. Adversarial Dynamics, Drift & Strategic Classification (Cluster 3)
* **Supporting / Foundational**: Dal Pozzolo et al. - Delayed Feedback (`1707.02640.pdf`), Bank Account Fraud Suite (`2211.13358.pdf`), Concept Drift Surveys (`1010.4781.pdf`).
* **Opposing / Critical (Strategic Classification & Performative Drift)**: Hardt et al. - Strategic Classification (`1506.06980.pdf`), Perdomo et al. - Performative Prediction (`2002.06673.pdf`), Miller et al. - Strategic Classification is Causal Modeling (`1910.10362.pdf`), Horowitz & Rosenfeld - Causal Strategic Classification (`2006.04683.pdf`), Cartella et al. - Adversarial Attacks on Tabular Fraud (`2101.08030.pdf`).

### 4. Graph ML, Network Topologies & Rail Constraints (Cluster 4)
* **Supporting / Foundational**: CARE-GNN (`2008.08692.pdf`), Heterogeneous Graph Transformer - HGT (`2003.01332.pdf`), Elliptic Bitcoin AML Benchmark (`1908.02591.pdf`), LaundroGraph (`2210.14360.pdf`), GraphConsis (`2005.00625.pdf`), CaT-GNN (`2402.14708.pdf`), LineMVGNN (`2603.23584.pdf`).
* **Opposing / Critical (Real-Time Sub-100ms Constraints & Silos)**: BRIGHT - Real-Time Graph Latency Bottlenecks (`2205.13084.pdf`), Spade - Streaming Graphs (`2211.06977.pdf`), FedGraph-VASP - Cross-Bank Silos (`2601.17935.pdf`), Adversarial Attacks on GNNs (`2104.08921.pdf`).

For detailed analytical breakdowns, review the reports in [`docs/research_reports/`](../research_reports/).
