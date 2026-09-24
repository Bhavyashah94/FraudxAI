---
title: "Class Weighting versus Amount Conditioning in Credit-Card Fraud Detection: A Dollar-Metric Study with a Temporal Explanation Audit"
authors: "Chenyu Wu"
year: 2026
venue: "arXiv / Duke University"
domain: "Dollar-Metric Loss & Temporal SHAP Attribution Drift Audit"
pdf_path: "docs/papers\2026_wu_dollar_metric_credit_card_fraud_temporal_shap_audit.pdf"
---

# Class Weighting versus Amount Conditioning in Credit-Card Fraud Detection: A Dollar-Metric Study with a Temporal Explanation Audit

**Authors:** Chenyu Wu  
**Venue / Date:** arXiv / Duke University (2026)  
**Domain Focus:** Dollar-Metric Loss & Temporal SHAP Attribution Drift Audit  
**Original PDF:** [`2026_wu_dollar_metric_credit_card_fraud_temporal_shap_audit.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2026_wu_dollar_metric_credit_card_fraud_temporal_shap_audit.pdf)

---

# Class Weighting versus Amount Conditioning in Credit-Card Fraud Detection: A Dollar-Metric Study with a Temporal Explanation Audit 

Chenyu Wu 

_Duke University_ 

2080 Duke University Road, Durham, NC 27708, USA wuchenyu999@outlook.com 

**_Abstract_ —Credit-card fraud losses are monetary, but papers often judge models with transaction-level scores. We ask whether transaction amount should shape training weights or be used later to order alerts. To separate this question from ordinary class imbalance handling, we keep total fraud-case weight fixed and vary only its allocation across fraud cases. The experiments test two chronological card-fraud datasets with XGBoost under unweighted training, standard class weighting, matched logamount weighting, stronger amount-weighted variants, and score times amount reranking. Metrics are average precision, dollar recall, and dollar precision at fixed alert budgets over five seeds, with 95 percent day-block bootstrap intervals for the main contrasts. Results are narrower than expected. Amount-derived ratio and velocity features carry much of the signal, while raw amount fields add little once those features are in the model. In the matched setting, amount-conditioned training gives only small gains over class weighting and does not consistently beat the plain unweighted model. Stronger amount weights recover more fraudulent dollars, but at lower ranking quality and dollar precision. Reranking alerts by score times amount after training gives the largest dollar-recall shift. A small SHAP audit finds larger month-to-month attribution movement for fraud cases than for aggregate traffic. In these tests, amount is useful as a feature and as an alert-ordering variable, not by itself as a better sample-weighting rule.** 

**_Index Terms_ —credit card fraud detection, cost-sensitive learning, class imbalance, gradient boosting, SHAP, concept drift** 

## I. Introduction 

Payment fraud is a costly failure mode in retail banking, and supervised learning is standard practice for detecting it [1], [2]. Common model metrics rarely match the way fraud causes loss. Precision, recall, and the area under the receiver operating characteristic curve treat a missed five-dollar purchase and a missed five-thousand-dollar purchase as the same event, so a model can look strong while the dollars leaving the bank tell a different story. 

One natural response is to weight fraudulent training cases by amount, so high-value fraud has more influence during fitting. That idea is consistent with example-dependent costsensitive learning [3], [4], but it creates a confound. An amount-based weight usually increases the total weight placed on the fraud class, which is also what ordinary class weighting does. A gain credited to amount conditioning may come 

from a larger positive-class weight, not from the within-fraud distribution of that weight. 

This paper runs the controlled comparison. We hold the total fraud-class weight fixed and change only its allocation across fraud cases: uniform for standard class weighting, or proportional to log amount for amount conditioning. It is a diagnostic comparison, not a new detector, so the contribution is the design rather than a model: a matched-total-weight setup that separates allocation from mass, a dollar-budget evaluation, and an explanation audit run on the alert population. Analogous concerns arise elsewhere: separating a confounded aggregate into its components is a recurring inference problem [5], and a relevant signal need not warrant the conclusion drawn from it [6]. Experiments report dollar recall and dollar precision at five alert budgets, average results over random seeds, and dayblock bootstrap intervals for the main contrasts. Two reference points bound the role of amount itself: a model with amountderived features removed and a ranker that uses amount alone. A temporal SHAP audit then asks whether the explanation profile shifts over time, especially within fraud cases and highscore alerts. 

Our results are deliberately qualified. Amount should remain in the modeling pipeline: ratio and velocity features derived from amount carry signal, and dollar metrics expose behavior that average precision can hide. Once ordinary fraud upweighting is controlled, matched amount conditioning adds little and does not reliably improve on a plain model. When the objective is to recover more fraudulent dollars under a fixed review budget, the more direct intervention is often at inference: rank by fraud score for general detection, then use a rule such as score times amount when dollar recall is the priority. That rule lowers precision, so it is an explicit queue policy. This SHAP audit adds a monitoring caution: fraudcase explanations can move while the aggregate explanation plot looks stable, so audits should include the alert population that analysts actually review. 

## II. Related Work 

Credit-card fraud detection has a long data-mining literature [1], and much of it is cost-sensitive. Example-dependent formulations [4] minimize expected financial loss instead of 

event-count error, cost-aware features improve fraud savings on card data [3], and recent work has paired interpretable gradient boosting with SHAP for insurance-fraud triage [7]. Transaction amount is a recurring input in these designs, appearing as a loss term, a sample weight, or a cost feature. This design choice is reasonable, but it is easy to misread. If amount weighting also raises the total positive-class weight, the reported benefit may reflect class imbalance handling more than amount conditioning. Prior comparisons rarely hold that total fixed, which is the gap addressed here. 

Imbalance is the other long-standing difficulty [8], and it shapes how the amount can be used. Resampling methods such as SMOTE [9] and inverse-frequency weighting are common remedies, aggregating a cardholder’s recent history sharpens the fraud signal [3], [10], and sequence and hybrid models have pushed detection accuracy further [11], [12]. Deep models are now competitive: graph neural networks resist camouflage by fraudsters [13] or propagate risk through a gated temporal attention graph [14]. We do not claim to beat these, since they need entity graphs or sequence context beyond our tabular setting, and boosting remains the stronger family on typical tabular data [15]. Plain and class-weighted gradient boosting [16]–[18] therefore remain strong and widely used baselines, and they serve here as the reference points an amount-conditioned scheme has to beat. 

Because fraud is rare, the evaluation metric matters as much as the model. Precision-recall views are more informative than receiver operating characteristic views under heavy imbalance [19], and the two curves are formally related [20]. Ranking summaries say little, though, about how much money a fixed review budget recovers, which has motivated cost- and amount-aware evaluation [3], [4], construct-aligned grading of financial models [21], and economic-validity audits of tabular predictions used in discrete choice [22], [23]. Dollar recall and dollar precision follow this line. 

Explanation stability over time is a separate concern. SHAP [24], [25] and LIME [26] are common attribution tools; counterfactual explanations provide a complementary actionoriented view [27], and recent fraud studies compare several methods on anonymized data [28]. Concept drift is well studied in general [29], [30] and in fraud [2]. Less often checked is whether the attribution profile itself changes across chronological periods, and whether that change is larger in fraud cases than in ordinary traffic. 

## III. Methodology 

## _A. Datasets_ 

Sparkov [31] is a synthetic credit-card dataset with interpretable fields: amount, merchant category, cardholder and merchant coordinates, time of day, and demographics. Using the public chronological partition, we split its training portion again by time, giving 972,506 training transactions (5,523 fraud, 0.57 percent), 324,169 validation (1,983 fraud, 0.61 percent), and 555,719 test (2,145 fraud, 0.39 percent); the test set holds 1.13 million dollars of fraud out of 38.6 million. The pooled rate is about 0.52 percent, and dates run from January 

2019 to December 2020. IEEE-CIS [32] is a real e-commerce, card-not-present fraud dataset from Vesta spanning about six months; most features are anonymized. A chronological 60/20/20 split gives 354,324 training (11,988 fraud), 118,108 validation (4,611 fraud), and 118,108 test (4,064 fraud), a 3.5 percent fraud rate. IEEE-CIS is used only to test transfer of the weighting comparison, since its anonymized features make SHAP attributions hard to read. 

## _B. Preprocessing and leakage controls_ 

Splits are chronological and never shuffled; the test set is evaluated once. Categorical fields are one-hot encoded, not target encoded. Per-cardholder rolling statistics use a onestep lag, so the current transaction cannot enter its own rolling window. For IEEE-CIS, the row identifier and raw time offset are dropped after ordering because both can leak position under a chronological split. High-cardinality fields are frequency encoded from the training split only. A runtime check confirms that no identifier, raw time field, or nonnumeric column reaches the model. Weighting choices and thresholds are selected on validation data. 

## _C. Weighting schemes_ 

Let _𝑎𝑖_ be the transaction amount and let s = _𝑛_ negative/ _𝑛_ positive, computed on the training split. Legitimate cases have weight 1 in every run. We compare four ways of weighting fraud cases. Plain also gives fraud cases weight 1. ClassWt uses _𝑤𝑖_ = s. AmtLogN uses _𝑤𝑖_ = s log(1 + _𝑎𝑖_ ) / meantrain _,_ fraud [log(1 + _𝑎_ )]. Because its mean fraud weight is s, ClassWt and AmtLogN assign the same total fraud weight; only the allocation among fraud cases changes. That is the comparison we care about most. AmtLog uses _𝑤𝑖_ = 10 log(1 + _𝑎𝑖_ ), so its total fraud weight is not matched to ClassWt. AmtLin uses _𝑤𝑖_ = _𝑎𝑖_ only as a stress test. We test the log shape: amounts are heavy-tailed, so a linear weight lets a few large frauds dominate the gradient while the log compresses that tail. To check that the compression rather than the specific function does the work, we add matched AmtSqrtN and AmtRankN variants replacing log(1 + _𝑎_ ) by<sup>√</sup> _<u>𝑎</u>_ and by the within-fraud rank of _𝑎_ . 

Two reference runs help keep the interpretation honest. NoAmt removes amount-derived features. AmtOnly ranks by amount alone. On IEEE-CIS, NoAmt removes only TransactionAmt because anonymized variables may still encode amountrelated information. Logistic regression and random forest baselines with balanced class weights [18] reached Sparkov average precision 0.22 and 0.89, below the boosting models. Sample weights can also change effective regularization, so the matched setup and the depth sweep check, roughly, that we are not calling a regularization effect an amount effect. At inference we also rerank Plain by multiplying its score by raw dollar amount. Because XGBoost scores are not calibrated probabilities, we use the product only as a ranking signal. 

## _D. Evaluation protocol_ 

Average precision is computed with scikit-learn’s average precision score summary of the precision-recall curve 

[19], [20]. For queue metrics, the alert budget is the top k percent of highest-scoring transactions. We evaluate k = 0.1, 0.5, 1, 2, and 5 percent, and report representative budgets in the tables. Dollar recall is the share of fraudulent dollars captured. Dollar precision is the share of flagged dollars that are fraudulent. Recorded outputs also include the false-positive count and the mean legitimate amount flagged. Each model is trained under five random seeds, and tables report the mean and standard deviation. For the key contrasts, a block bootstrap resamples whole calendar days because same-day transactions are correlated; we draw 1,000 resamples conditional on the seed42 models and report 95 percent intervals. Because several are inspected at once, interval widths give normal-approximation standard errors and two-sided p-values, corrected with Holm– Bonferroni across the twelve contrasts. Contrast estimates and intervals use the seed-42 models while tables report five-seed means, so the treatment remains descriptive. 

## _E. Temporal SHAP drift protocol_ 

Our audit uses the log-amount model (AmtLog). SHAP values are computed with the tree-path-dependent estimator [25], which uses the tree structure and needs no background dataset. For each calendar month, importance is the mean absolute SHAP value over up to 2,000 sampled transactions, or all available cases when a subset is smaller. That exception matters for fraud months, where counts are often low. Importance vectors are normalized to sum to one before comparison. A fixed-model design trains once on the first three months and explains each later month, measuring data-driven change; three months is a pragmatic minimum, leaving most of the timeline for auditing. An expanding-window design retrains each month before explaining, adding model-update change. Across the 21 audited months we measure Jensen-Shannon distance between consecutive months and Kendall rank correlation against the first month, for all transactions, true fraud cases, and the highestscoring one percent. 

## IV. Experiments And Results 

## _A. Setup_ 

All gradient boosting models use 500 trees, depth seven, learning rate 0.05, and 0.8 column and row subsampling, trained with the histogram method [16]. Experiments run on a laptop with 16 GB of memory and no graphics accelerator. On validation, we set the AmtLog multiplier to ten. A depth sweep over 5, 7, and 9 on the Sparkov validation set keeps the schemes within 0.006 average precision of one another at every depth, so the depth-seven choice does not favor one weighting scheme. Seeds are fixed, library versions are pinned (XGBoost 2.1.4, SHAP 0.49.1), splits are deterministic and chronological, and exact split sizes are reported. Cost is set by the data and the tree budget, not by the weighting: median fit time is 69 s on Sparkov and 50 s on IEEE-CIS, and scoring runs at 3.3 and 4.5 microseconds per transaction. Reranking adds no measurable cost; the SHAP audit is the expensive part and runs as a scheduled monthly job, and tighter budgets may draw on analogous work in compression and split execution 

TABLE I 

Sparkov test results, mean over five seeds (std in parentheses for AP and DR@1%). AP: average precision; DR: dollar recall; DP@1%: dollar precision at 1%. 

|**Model**|**AP**<br>|**DR@0.5%**|**DR@1%**|**DR@2% **|**DP@1%**|
|---|---|---|---|---|---|
|Plain|0.930 (.001)|0.970|0.990 (.001)|0.997|0.47|
|ClassWt|0.931 (.001)|0.973|0.992 (.000)|0.997|0.58|
|AmtLogN (matched)|0.932 (.000)|0.973|0.992 (.001)|0.997|0.58|
|AmtLog|0.934 (.000)|0.974|0.993 (.001)|0.997|0.57|
|AmtLin|0.927 (.001)|0.978|0.991 (.002)|0.997|0.58|
|Plain + score*amt rerank|0.820|0.980|0.995|0.998|0.25|



NoAmt and AmtOnly have DR@1% of 0.63 and 0.83; at the 0.1% budget, precision is one. 

[33] or resource-aware scheduling [34]. Deployments also carry review-capacity and privacy constraints we omit; analogous online dispatch work models capacity and privacy jointly [35]. Code and configuration are available from the authors and will be released in a public repository on acceptance. 

## _B. Amount as a feature_ 

Removing all amount-derived features collapses ranking on Sparkov, from 0.930 average precision to 0.336, but the raw amount column alone is not the cause: removing it leaves 0.907, and removing only the velocity features, the seven-day rolling mean and the amount-to-average ratio, leaves 0.874. Ranking collapses only when both go. Explicit amount columns are largely redundant with the derived ones, since the ratio already contains the current amount. On IEEE-CIS, removing the amount field changes average precision only from 0.548 to 0.538, although anonymized features may still carry amountrelated signal. Ranking by amount alone is weak on both datasets (0.14 on Sparkov, 0.04 on IEEE-CIS), so trained models are not simply sorting by size. Amount is useful as a feature; that is separate from whether it should set sample weights. 

## _C. Controlled weighting comparison_ 

Tables I and II give the five-seed means, with standard deviations for AP and DR@1%. On Sparkov, the boosting schemes are close in both average precision and dollar recall. AmtLogN is 0.002 above ClassWt in average precision (dayblock interval 0.0002 to 0.004). That difference is nominally detectable but does not survive the Holm correction over the twelve contrasts (adjusted p = 0.20), and it is too small to matter in an alert queue. For DR@1%, the interval includes zero. Against Plain, neither interval excludes zero. Sparkov is highly separable at small alert budgets, so there is little room for any weighting scheme to improve detection. A more visible movement is DP@1%, which rises from 0.47 for Plain to 0.58 for ClassWt, with AmtLogN also at 0.58: the reduction in falsepositive dollars comes from fraud-class weighting, not from conditioning that weight on amount. At the 1% budget this is about 3,500 false positives and a mean legitimate amount flagged of 235 dollars for ClassWt and AmtLogN, against 368 dollars for Plain. 

IEEE-CIS gives a different picture. Plain is the strongest baseline among the tested models, with average precision 0.548 and DR@1% of 0.188. None of the amount-conditioned 

TABLE II 

IEEE-CIS test results, mean over five seeds (std in parentheses for AP and DR@1%). Columns as in Table I. 

|**Model**|**AP**<br>|**DR@0.5%**|**DR@1%**|**DR@2% **|**DP@1%**|
|---|---|---|---|---|---|
|Plain|0.548 (.002)|0.092|0.188 (.004)|0.344|0.89|
|ClassWt|0.513 (.002)|0.076|0.155 (.005)|0.310|0.89|
|AmtLogN (matched)|0.514 (.003)|0.082|0.180 (.004)|0.345|0.89|
|AmtLog|0.503 (.004)|0.080|0.175 (.003)|0.340|0.89|
|AmtLin|0.444 (.004)|0.131|0.242 (.009)|0.379|0.68|
|Plain + score*amt rerank|0.307|0.274|0.384|0.516|0.33|



Rerank multiplies Plain scores by amount without retraining. 

schemes beats that dollar recall with an interval excluding zero. ClassWt is harmful here: average precision falls to 0.513 and DR@1% to 0.155. AmtLogN recovers part of that loss. Its DR@1% gain over ClassWt is 0.020 (day-block interval 0.007 to 0.034), while the average-precision interval includes zero (interval -0.005 to 0.007). Against Plain, though, AmtLogN is still lower on average precision (interval -0.042 to -0.025), and its DR@1% interval includes zero. That DR@1% gain is the one matched result surviving Holm correction (adjusted p = 0.032); six of seven nominally significant contrasts survive. Because model specification can reorder rankings, as crossmarket volatility forecasting illustrates [36], we repeated the comparison in a second boosting implementation, LightGBM, which shows the same pattern: average precision 0.555 for Plain against 0.515 for ClassWt and 0.514 for AmtLogN, the latter two differing by 0.001, and AmtLogN again above ClassWt on dollar recall (0.175 against 0.158). 

Among trained schemes, only AmtLin has a dollar-recall increase over Plain whose interval excludes zero. It raises dollar recall by 0.054 (interval 0.033 to 0.076), but average precision drops by 0.108 (interval -0.124 to -0.091) and DP@1% falls from 0.89 to 0.68. A simpler reranking check is more revealing. Multiplying the Plain score by amount raises DR@1% to 0.384, above every trained scheme, while average precision falls to 0.31 and DP@1% to 0.33. We read this as a different alert ordering. Tempering the exponent traces that trade-off: with score times amount<sup>_𝛾_</sup> at _𝛾_ = 0.25, 0.5, and 0.75, average precision is 0.520, 0.457, and 0.380 at DR@1% of 0.279, 0.335, and 0.366, so _𝛾_ = 0.5 keeps most of the dollar-recall gain at far better ranking, exceeding every trained scheme on DR@1% though at lower average precision than all but AmtLin. A flat per-review cost sets the budget, not the order: thresholding the product at a constant leaves the ordering unchanged. Calling it cost-optimal would require calibrated probabilities, which we do not claim. Reranking as a post-hoc stage is familiar elsewhere [37], and the expected-value view resembles portfolio rules trading return against downside risk [38]. Fig. 1 reports dollar recall relative to Plain. 

## _D. Sensitivity to weighting strength_ 

To map the weighting-strength trade-off, we swept the fixed multiplier of the log-amount weight on the IEEE-CIS validation set. That sweep is the AmtLog family. Average precision falls steadily as the multiplier grows, from 0.609 with no weighting to 0.525 at the largest setting. DR@1% peaks at multiplier one, 



Fig. 1. Dollar recall at the 1% budget for each scheme minus the unweighted model, mean over five seeds with std bars. 



Fig. 2. IEEE-CIS validation performance as the fixed log-amount multiplier varies (the AmtLog family, distinct from the matched-weight AmtLogN). 

so the knob is not monotone in the metric it is meant to improve; non-monotone returns from a single scaling parameter are also reported in LLM tuning [39], [40]. The limited checks suggest shape matters less than compression: matched square-root and rank variants both reach 0.930 average precision on Sparkov against 0.932 for AmtLogN, and on IEEE-CIS the schemes trace one axis ordered by tail compression (ClassWt 0.513 at DR@1% 0.155, AmtLogN 0.514 at 0.180, AmtSqrtN 0.504 at 0.214, AmtLin 0.444 at 0.242), none reaching Plain’s 0.548. AmtLogN is used for the controlled comparison: AmtLog changes both the within-fraud allocation and the total fraud weight, while AmtLogN holds the total fixed. Fig. 2 shows the validation trend. 

## _E. Temporal explanation drift_ 

Table III reports the Sparkov drift audit for AmtLog, one representative amount-aware classifier. We did not repeat the audit for every scheme; this part of the paper is exploratory. Score times amount only reorders Plain scores, so it has no separate trained model to explain. Fraud-subset explanations move much more than all-traffic explanations, with mean Jensen-Shannon distance 0.057 compared with 0.012 in the fixed-model design; an aggregate curve can stay flat while local behavior moves underneath it, as also reported for model editing 

TABLE III 

Temporal SHAP drift on Sparkov (log-amount model). Higher JS distance and lower Kendall tau mean more drift. 



<!-- Start of picture text -->
Design Subset Mean JS Min Kendall tau<br>A (data only) all 0.012 0.97<br>A (data only) fraud 0.057 0.82<br>A (data only) top 1% 0.043 0.89<br>B (retraining) all 0.037 0.71<br>B (retraining) fraud 0.074 0.68<br>B (retraining) top 1% 0.061 0.72<br>A uses a fixed model trained on months 1–3; B uses monthly expanding-<br>window retraining.<br><!-- End of picture text -->



Fig. 3. Normalized monthly SHAP importance of the leading fraud-subset features (expanding-window design, Sparkov, log-amount model). 

[41]. The 2,000-transaction cap does not drive this: monthly fraud counts run from 258 to 592, so it never binds on the fraud subset, and recomputing the all-traffic curve at caps of 1,000, 2,000, and 5,000 gives 0.017, 0.012, and 0.009, leaving fraud drift over three times the aggregate at every cap. In this run, expanding-window retraining increases measured drift on every subset. Fraud-subset monitoring is retrospective because labels arrive with delay; the top-one-percent alert subset is easier to compute immediately, although it changes when the model changes and so mixes explanation drift with selection drift. The audit matters because dollar-oriented operation makes fraudcase monitoring relevant, and fraud-case explanations moved most. Fig. 3 plots normalized monthly importance. 

## V. Discussion 

Our matched-weight results do not support amount weighting as the default move. Amount is not irrelevant: ratio and velocity variables carry much of the useful signal, and dollar metrics expose behavior average precision misses. On Sparkov the small-budget task is nearly solved, so the schemes have little room to separate. On IEEE-CIS, Plain is the best baseline; ClassWt hurts it and AmtLogN repairs some of that damage without moving ahead. AmtLin buys more dollar recall, yet a post-training reranking rule moves farther along the same tradeoff without retraining. For deployment the first decision is queue design: train a strong baseline, then choose an alert ordering matching the review goal. Amount-conditioned training is still worth testing where class weighting or an explicit cost model is already in use. 

The SHAP audit gives a smaller warning. Dollar-aware rules change the alert population; in the audit, fraud-case explanations moved fastest, and a single global SHAP plot would have missed it. Timing remains a problem: confirmed labels arrive late, so the fraud subset is retrospective, while top-one-percent subsets are immediate but shift when the model updates. 

## VI. Limitations 

Scope here is limited. Sparkov is synthetic; its named variables suit controlled checks, but the near-perfect smallbudget precision should not be read as live alert quality. IEEECIS is a useful transfer check, although its anonymized fields make feature-level interpretation weak, and the relative ordering of schemes is more informative than absolute scores. We study only gradient-boosted trees, in two libraries; a genuinely different model family, sequence or graph models, or richer entity features may change the comparison. These weighting rules are also simpler than deployed cost models, omitting review cost, recovery, customer friction, and intervention effects. Sample weights affect regularization, which the matched design and depth checks address only partly. Our statistical treatment is descriptive: corrected p-values are normal approximations from percentile intervals conditional on one seed, and SHAP drift uses monthly point estimates without confidence bands. Delayed labels, alert-selection effects, and rules for refreshing explanation baselines are left unresolved. 

## VII. Ethical And Data Considerations 

Both datasets are public and contain no personally identifying information we access: Sparkov is synthetic and IEEE-CIS anonymized. Deployed fraud models can produce unequal error rates across customer groups and can inconvenience legitimate customers through false alarms; our dollar-precision metric speaks to the second concern but not the first, and any deployment should include fairness review and human adjudication. For graph-based deployments, unlearning requests can also degrade group fairness [42]. 

## VIII. Conclusion 

We asked a deliberately small question: after total fraud-case weight is fixed, does distributing that weight by transaction amount help? In the matched setting tested here, usually not. Amount still matters, but more through features and queue ordering than through matched sample weights: on Sparkov, ratio and velocity features carried much of the signal, and score times amount reranking changed dollar recall more directly than retraining did, while matched amount-weighted training gave only small gains over class weighting. The caution matters, since that reranking is not a free improvement: it raised dollar recall on IEEE-CIS but lowered average precision and dollar precision, so it is a queue-management rule rather than a better classifier. 

For papers in this area, dollar-level queue metrics belong beside transaction-level ranking metrics, because the two views can rank methods differently, and formal claims over a family of contrasts should carry a multiplicity correction: the Sparkov AmtLogN-ClassWt gap in average precision does not survive 

one. Amount-conditioned training may still help where class weighting or explicit cost models are already in use, but comparisons should include Plain and inference-time reranking. Richer entity features and explicit investigation costs would make the cost setting more realistic, and for the explanation audit delayed labels and confidence bands are the next missing pieces. 

## References 

- [1] S. Bhattacharyya, S. Jha, K. Tharakunnel, and J. C. Westland, ”Data mining for credit card fraud: A comparative study,” Decis. Support Syst., vol. 50, no. 3, pp. 602-613, 2011, doi: 10.1016/j.dss.2010.08.008. 

- [2] A. Dal Pozzolo, G. Boracchi, O. Caelen, C. Alippi, and G. Bontempi, ”Credit card fraud detection: A realistic modeling and a novel learning strategy,” IEEE Trans. Neural Netw. Learn. Syst., vol. 29, no. 8, pp. 3784-3797, 2018, doi: 10.1109/TNNLS.2017.2736643. 

- [3] A. C. Bahnsen, D. Aouada, A. Stojanovic, and B. Ottersten, ”Feature engineering strategies for credit card fraud detection,” Expert Syst. Appl., vol. 51, pp. 134-142, 2016, doi: 10.1016/j.eswa.2015.12.030. 

- [4] S. Hoppner, B. Baesens, W. Verbeke, and T. Verdonck, ”Instancedependent cost-sensitive learning for detecting transfer fraud,” Eur. J. Oper. Res., vol. 297, no. 1, pp. 291-300, 2022, doi: 10.1016/j.ejor.2021.05.028. 

- [5] X. Han and Y. Xiao, ”Decomposing firm-level crisis responses from incomplete market signals: Evidence from China’s IT sector during COVID-19,” arXiv:2606.10297, 2026. 

- [6] P. Qian et al., ”Relevant is not warranted: Evidence-force calibration for cited RAG,” arXiv:2605.28044, 2026. 

- [7] D. Banulescu-Radu and S. Yankol-Schalck, ”Practical guideline to efficiently detect insurance fraud in the era of machine learning: A household insurance case,” J. Risk Insur., vol. 91, no. 4, pp. 867-913, 2024, doi: 10.1111/jori.12452. 

- [8] H. He and E. A. Garcia, ”Learning from imbalanced data,” IEEE Trans. Knowl. Data Eng., vol. 21, no. 9, pp. 1263-1284, 2009, doi: 10.1109/TKDE.2008.239. 

- [9] N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, ”SMOTE: Synthetic minority over-sampling technique,” J. Artif. Intell. Res., vol. 16, pp. 321-357, 2002, doi: 10.1613/jair.953. 

- [10] C. Whitrow, D. J. Hand, P. Juszczak, D. Weston, and N. M. Adams, ”Transaction aggregation as a strategy for credit card fraud detection,” Data Min. Knowl. Discov., vol. 18, no. 1, pp. 30-55, 2009, doi: 10.1007/s10618-008-0116-z. 

- [11] J. Jurgovsky et al., ”Sequence classification for credit-card fraud detection,” Expert Syst. Appl., vol. 100, pp. 234-245, 2018, doi: 10.1016/j.eswa.2018.01.037. 

- [12] F. Carcillo, Y.-A. Le Borgne, O. Caelen, Y. Kessaci, F. Oble, and G. Bontempi, ”Combining unsupervised and supervised learning in credit card fraud detection,” Inf. Sci., vol. 557, pp. 317-331, 2021, doi: 10.1016/j.ins.2019.05.042. 

- [13] Y. Dou, Z. Liu, L. Sun, Y. Deng, H. Peng, and P. S. Yu, ”Enhancing graph neural network-based fraud detectors against camouflaged fraudsters,” in Proc. 29th ACM Int. Conf. Inf. Knowl. Manage. (CIKM), 2020, pp. 315-324, doi: 10.1145/3340531.3411903. 

- [14] S. Xiang et al., ”Semi-supervised credit card fraud detection via attribute-driven graph representation,” in Proc. AAAI Conf. Artif. Intell., vol. 37, no. 12, 2023, pp. 14557-14565, doi: 10.1609/aaai.v37i12.26702. 

- [15] L. Grinsztajn, E. Oyallon, and G. Varoquaux, ”Why do tree-based models still outperform deep learning on typical tabular data?” in Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 35, 2022, pp. 507-520. 

- [16] T. Chen and C. Guestrin, ”XGBoost: A scalable tree boosting system,” in Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Min. (KDD), 2016, pp. 785-794, doi: 10.1145/2939672.2939785. 

- [17] J. H. Friedman, ”Greedy function approximation: A gradient boosting machine,” Ann. Stat., vol. 29, no. 5, pp. 1189-1232, 2001, doi: 10.1214/aos/1013203451. 

- [18] L. Breiman, ”Random forests,” Mach. Learn., vol. 45, no. 1, pp. 5-32, 2001, doi: 10.1023/A:1010933404324. 

- [19] T. Saito and M. Rehmsmeier, ”The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets,” PLoS ONE, vol. 10, no. 3, p. e0118432, 2015, doi: 10.1371/journal.pone.0118432. 

- [20] J. Davis and M. Goadrich, ”The relationship between precision-recall and ROC curves,” in Proc. 23rd Int. Conf. Mach. Learn. (ICML), 2006, pp. 233-240, doi: 10.1145/1143844.1143874. 

- [21] J. Lu et al., ”GAUGE: Grading agent-built financial models without a golden answer,” arXiv:2607.24889, 2026. 

- [22] Y. Wang, X. Sun, Y. Li, Z. Fan, and Z. Zhuang, ”Auditing and fixing economic validity in tabular foundation models for discrete choice,” presented at the FMSD Workshop, Int. Conf. Mach. Learn. (ICML), 2026, arXiv:2605.26559. 

- [23] Y. Wang, X. Sun, Y. Li, Z. Fan, and Z. Zhuang, ”Embedding foundation model predictions in discrete-choice models with structural guarantees,” arXiv:2606.26432, 2026. 

- [24] S. M. Lundberg and S.-I. Lee, ”A unified approach to interpreting model predictions,” in Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 30, 2017, pp. 4765-4774. 

- [25] S. M. Lundberg et al., ”From local explanations to global understanding with explainable AI for trees,” Nat. Mach. Intell., vol. 2, pp. 56-67, 2020, doi: 10.1038/s42256-019-0138-9. 

- [26] M. T. Ribeiro, S. Singh, and C. Guestrin, ”Why should I trust you?: Explaining the predictions of any classifier,” in Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Min. (KDD), 2016, pp. 11351144, doi: 10.1145/2939672.2939778. 

- [27] Z. Chen, F. Silvestri, J. Wang, H. Zhu, H. Ahn, and G. Tolomei, ”ReLAX: Reinforcement learning agent explainer for arbitrary predictive models,” in Proc. 31st ACM Int. Conf. Inf. Knowl. Manage. (CIKM), 2022, pp. 252-261, doi: 10.1145/3511808.3557429. 

- [28] B. Raufi, C. Finnegan, and L. Longo, ”A comparative analysis of SHAP, LIME, ANCHORS, and DICE for interpreting a dense neural network in credit card fraud detection,” in Explainable Artificial Intelligence (xAI 2024), Commun. Comput. Inf. Sci., vol. 2156, Springer, 2024, pp. 365383, doi: 10.1007/978-3-031-63803-9 20. 

- [29] J. Lu, A. Liu, F. Dong, F. Gu, J. Gama, and G. Zhang, ”Learning under concept drift: A review,” IEEE Trans. Knowl. Data Eng., vol. 31, no. 12, pp. 2346-2363, 2019, doi: 10.1109/TKDE.2018.2876857. 

- [30] J. Gama, I. Zliobaite, A. Bifet, M. Pechenizkiy, and A. Bouchachia, ”A survey on concept drift adaptation,” ACM Comput. Surv., vol. 46, no. 4, art. 44, 2014, doi: 10.1145/2523813. 

- [31] K. Shenoy and B. Harris, ”Credit card transactions fraud detection dataset (Sparkov generator),” Kaggle, 2020. [Online]. Available: https: //www.kaggle.com/datasets/kartik2112/fraud-detection 

- [32] Vesta Corp. and IEEE Computational Intelligence Society, ”IEEE-CIS fraud detection,” Kaggle, 2019. [Online]. Available: https://www.kaggle. com/competitions/ieee-fraud-detection 

- [33] J. Guo et al., ”Quantized-TinyLLaVA: A new multimodal foundation model enables efficient split learning,” arXiv:2511.23402, 2025. 

- [34] Y. Liu, I. A. Akinlade, X. Jiang, W. Yang, and S. Yang, ”An AI-driven framework for energy-efficient environmental monitoring in smart cities using edge intelligence,” arXiv:2605.22824, 2026. 

- [35] Y. Liu et al., ”Privacy-preserving context-based electric vehicle dispatching for energy scheduling in microgrids: An online learning approach,” IEEE Trans. Emerg. Topics Comput. Intell., vol. 6, no. 3, pp. 462-478, 2022, doi: 10.1109/TETCI.2021.3085964. 

- [36] K. Cheng, X. Qi, Z. Cheng, and L. Lai, ”Volatility persistence and model choice in cross-market volatility forecasting,” SSRN Working Paper 6610278, 2026. 

- [37] Z. Cheng, L. Lai, Y. Liu, K. Cheng, and X. Qi, ”Enhancing financial report question-answering: A retrieval-augmented generation system with reranking analysis,” presented at ICECET 2026, arXiv:2603.16877. 

- [38] Z. Song et al., ”From deterministic to stochastic: An interpretable stochastic model-free reinforcement learning framework for portfolio optimization,” Appl. Intell., vol. 53, no. 12, pp. 15188-15203, 2023, doi: 10.1007/s10489-022-04217-5. 

- [39] A. Ainiwaer, Q. Liu, and M. Lily, ”Study of examples effect on the LLM performance,” preprint, 2026, doi: 10.13140/RG.2.2.20382.40007. 

- [40] Q. Liu, A. Ainiwaer, and M. Lily, ”How well does the numbers of steps work in LLM performance? A comprehensive analysis,” preprint, 2026, doi: 10.13140/RG.2.2.18516.56969. 

- [41] Z. Gu et al., ”Diagnosing hidden instabilities in model editing via uncertainty quantification,” in Proc. 64th Annu. Meeting Assoc. Comput. Linguistics (ACL), 2026, pp. 32544-32566. 

- [42] Z. Chen et al., ”FROG: Fair removal on graph,” in Proc. 34th ACM Int. Conf. Inf. Knowl. Manage. (CIKM), 2025, pp. 415-424, doi: 10.1145/3746252.3761341. 

