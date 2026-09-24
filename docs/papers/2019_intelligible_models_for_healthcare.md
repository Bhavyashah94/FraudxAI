---
title: "Predictive Modeling of the Hospital Readmission Risk from Patients’ Claims Data Using Machine Learning: A Case Study on COPD"
year: 2019
original_file: "intelligible_models_for_healthcare.pdf"
pdf_path: "docs/papers\2019_intelligible_models_for_healthcare.pdf"
---

# Predictive Modeling of the Hospital Readmission Risk from Patients’ Claims Data Using Machine Learning: A Case Study on COPD

**Year:** 2019  
**Local PDF:** [`2019_intelligible_models_for_healthcare.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2019_intelligible_models_for_healthcare.pdf)

---

www.nature.com/scientificreports 









# **opeN** 

Received: 25 July 2018 Accepted: 15 January 2019 Published: xx xx xxxx 

**predictive Modeling of the Hospital Readmission Risk from patients’ Claims Data Using Machine Learning: A Case study on CopD** 

**Xu Min**<sup>**1,2**</sup> **, Bin Yu**<sup>**3**</sup> **& Fei Wang**<sup>**1**</sup> 

**Chronic Obstructive Pulmonary Disease (COPD) is a prevalent chronic pulmonary condition that affects hundreds of millions of people all over the world. Many CopD patients got readmitted to hospital within 30 days after discharge due to various reasons. Such readmission can usually be avoided if additional attention is paid to patients with high readmission risk and appropriate actions are taken. this makes early prediction of the hospital readmission risk an important problem. the goal of this paper is to conduct a systematic study on developing different types of machine learning models, including both deep and non-deep ones, for predicting the readmission risk of COPD patients. We evaluate those different approaches on a real world database containing the medical claims of 111,992 patients from the Geisinger Health System from January 2004 to September 2015. The patient features we build the machine learning models upon include both knowledge-driven ones, which are the features extracted according to clinical knowledge potentially related to COPD readmission, and data-driven features, which are extracted from the patient data themselves. Our analysis showed that the prediction performance in terms of Area Under the receiver operating characteristic (RoC) Curve (AUC) can be improved from around 0.60 using knowledge-driven features, to 0.653 by combining both knowledgedriven and data-driven features, based on the one-year claims history before discharge. Moreover, we also demonstrate that the complex deep learning models in this case cannot really improve the prediction performance, with the best AUC around 0.65.** 

Chronic Obstructive Pulmonary Disease (COPD) is one type of obstructive lung disease makes people difficult to breathe. The Global Burden of Disease Study reports a prevalence of 251 million cases of COPD globally in 2016, and it is estimated that 3.17 million global deaths were caused by the disease in 2015<sup>1</sup> . In US it was reported that 21% of the COPD patients got readmitted 30 days after discharge and the cost for these readmissions is 18% higher than those for initial hospital stays<sup>2</sup> . The Centers for Medicare and Medicaid Services (CMS) has set COPD as one of their important target diseases for designing policies to reduce readmissions because of this high prevalence and cost. According to Purdy _et al_ .<sup>3</sup> , COPD is an ambulatory care sensitive condition where hospital admission could be avoided by effective interventions in primary or preventative care. The risk factors for COPD readmission remain largely unknown. Retrospective<sup>4</sup> and prospective<sup>5</sup> studies have been conducted to investigate COPD readmissions. 

In recent years, because of the rapid development of computer software and hardware technologies and wide adoption of electronic medical data systems, more and more health related data such as Electronic Health Records (EHR) and medical claims are becoming readily available. Many computational models have been developed based on these data for predicting the risk of hospital readmission. The LACE index<sup>6</sup> uses four variables (L ength of stay (L), A cuity of the admission (A), C omorbidity of the patient (C) and E mergency department use in the duration of 6 months before admission (E)) to predict the risk of death or nonelective 30-day readmission after hospital discharge among both medical and surgical patients. Similarly, the HOSPITAL score<sup>7</sup> uses 7 clinical predictors (which are available in patient EHRs) to identify patients at high risk of potentially avoidable hospital 

1Department of Healthcare Policy and Research, Weill Cornell Medicine, New York, NY, USA. 2Department of Computer Science and Technology, Institute for Artificial Intelligence, Tsinghua-Fuzhou Institute for Data Technology, and Bioinformatics Division, BNRist, Tsinghua University, Beijing, China.<sup>3</sup> American Air Liquide, Newark, DE, USA. Correspondence and requests for materials should be addressed to F.W. (email: few2001@med.cornell.edu) 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

1 

www.nature.com/scientificreports 

www.nature.com/scientificreports/ 

readmission within 30 days. Researchers have also explored pure data-driven machine learning approaches for this problem. For example, Hosseinzadeh _et al_ .<sup>8</sup> investigated the predictability of hospital readmission using classical machine learning methods (e.g., naïve Bayes and decision trees) using the claims data from the provincial hospital system in Quebec, Canada. Cauruana _et al_ .<sup>9</sup> applied generalized additive model to predict the hospital readmission risk of a general cohort with around 400,000 patients, where each patient is represented as a vector of about 4,000 dimensions. Sushmita _et al_ .<sup>10</sup> studied the prediction of all-cause hospital readmission with machine learning methods (support vector machine, decision trees, random forests and generalized boosting machine) using the admission data of patients provided by a large hospital chain in the Northwestern United States. These studies have demonstrated the better potential of machine learning models for hospital readmission prediction comparing to LACE and HOSPITAL score. 

Recently, deep learning<sup>11</sup> , as a specific type of machine learning models, has attracted attentions of researchers in various fields (e.g., computer vision, speech analysis and natural language processing) because of their superior performance. Researchers have also explored the potential of deep learning approaches in hospital readmission prediction. For example, Wang _et al_ .<sup>12</sup> developed a cost-sensitive deep learning approach combining Convolutional Neural Network (CNN)<sup>13</sup> and Multi-Layer Perceptron (MLP)<sup>14</sup> for readmission prediction. Xiao _et al_ .<sup>15</sup> adapted the TopicRNN approach<sup>16</sup> , which combines probabilistic topic modeling<sup>17</sup> and Recurrent Neural Network (RNN)<sup>18</sup> to better capture long-term dependencies in sequences, to predict the readmission risk of heart failure patients. Rajkomar _et al_ .<sup>19</sup> also developed an approach that ensembles three deep learning models to predict the risk of 30-day unplanned readmission. 

Despite the initial success, so far there is no comprehensive and systematic investigation on the potential of machine learning models for hospital readmission risk prediction. The goal of this paper is to conduct such a study on COPD patients using their longitudinal claims records. The output of our model is the probability that each patient will be readmitted within 30 days at the time of discharge. We comprehensively examined the performance of traditional machine learning models including logistic regression and variants, random forest, Support Vector Machine (SVM) and Gradient Boosting Decision Tree, as well as deep learning models including MLP, CNN, RNN and variants, using both knowledge and data driven patient features. 

## **Methods and Materials** 

This paper aims at conducting a systematic comparative study on the performance of different machine learning models for predicting the hospital readmission risk of COPD patients. Here we characterize a machine learning model as either traditional (non-deep) or deep. A traditional model is typically composed of two major steps, feature engineering<sup>20</sup> and model building<sup>21</sup> . Feature engineering extracts “good” features from the data that are effective for the model building step. Different from traditional methods, a deep learning model<sup>11</sup> enjoys an end-to-end learning mechanism, where the feature engineering part is implicitly integrated into the learning pipeline. In the following we introduce these two types of approaches formally. 

**traditional Methods.** As we introduced above, there are two major steps in traditional methods: feature engineering and model building. 

_Feature Engineering._ Our goal is to predict the risk of hospital readmission, which is defined as a readmission to hospital within 30 days of a prior hospital discharge. Therefore, the prediction is made on the day of hospital discharge. Patient features can be constructed from the medical history prior to the discharge day. Here we categorize the patient features as either knowledge- or data-driven. More specifically, we investigate the following knowledge - driven features. 

- HOSPITAL Score<sup>7</sup> . The original HOSPITAL score is aggregated from 7 features from different subdomains, wherein 4 of them are available in our claims data, including the number of procedures performed during hospital stay (HOS_Proc), the number of hospital admissions during the previous year (HOS_NOAD), the number of hospital stays with >=5 days (HOS_LOS), and the index admission type (HOS_Index). We use them as separate dimensions in the patient representation. 

- LACE Index<sup>6</sup> . The LACE index is aggregated from 4 features, i.e. Length of stay (days) (L), Acute (emergent) admission (A), Charlson Comorbidity Index (C) and Number of ED visits within six months (E). We use them as separate dimensions in the patient representation. 

- • Handcrafted Features. In addition to HOSPITAL score and LACE index, we also picked 12 features that could be important to our task, including age, gender, length of stay (LOS), number of admissions in the previous year (NOA), total length of all stays in the previous year (LOAS), number of all kinds of admissions (NOAA, including outpatient admissions), number of different types of index admissions (Index, Index_trans, Index_ final, Readm, Readm_trans, Readm_final). 

One limitation of our data is that some important patient features, such as the Global Initiative for Obstructive Lung Disease (GOLD) severity grade<sup>22</sup> , are not available, therefore we cannot use them in the predictive modeling process. 

The other feature category is data-driven features, which includes the following four different types. 

- Diagnosis. The patient diagnosis in our data is encoded with the International Classification of Diseases (ICD-9) codes. Considering the large number of distinct ICD-9 codes, we further investigated three different grouping strategies: (1) First three digits of ICD-9; (2) Clinical Classifications Software (CCS) codes; (3) Hierarchical Condition Category (HCC) codes. 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

2 

www.nature.com/scientificreports 

www.nature.com/scientificreports/ 

|**Feature x**|**Dimension**<br>**(one-year history)**|**Dimension**<br>**(full history)**|
|---|---|---|
|HOS|4|—|
|Knowledge-driven<br>LACE|4|—|
|hand|12|12|
|DX|9743|10306|
|DX_3dig|1153|1169|
|DX_CCS|285|285|
|DX_HCC|197|197|
|Data-driven<br>PROC|11193|12009|
|PROC_group|399|402|
|PHAR|20289|22964|
|PHAR_GTC|42|42|
|LC|32|33|



**Table 1.** Dimensions of different kinds of features. 

- Procedures. The patient procedure information is encoded with three different coding sources, i.e., CCS codes, Berenson-Eggers Type of Service (BETOS) codes, and revenue codes. 

- • Pharmacy. The pharmacy/medication information is encoded with National Drug Code (NDC), which we further mapped to the Generic Therapeutic Class (GTC) codes for the sake of dimensionality reduction. 

- • Locations. We also consider the location where the medical service is provided. For all four types of data-driven features, we construct the following representations through the analogy with natural language processing<sup>23</sup> : 

- Bag-of-Words (BoW) representation, which counts the frequency of each feature in the feature construction time period. 

- boolean Bag-of-Words (bBoW), which just cares about whether or not a specific feature appears in the feature construction time period. 

- Term Frequency-Inverse Document Frequency (TFIDF) normalization of the BoW representation<sup>23</sup> , which suppresses the impact of highly prevalent features (which could be non-informative) by weighting the feature counts by the inverse of its popularity (counts) in all patients’ records. 

For both knowledge- and data-driven features, we use either one year or full period before the hospital discharge date as the feature construction period (also called observation window). The only exceptions are HOSPITAL score and LACE (which are defined over one year). Table 1 summarizes the dimensions of all features introduced above. In addition to the investigation of different groups of features respectively in the predictive modeling process, we also combine multiple groups of features for training the models to see how they can boost the performance 

_Model Building._ After the patient features are constructed, we will feed them into a machine learning model for readmission risk prediction. The following models are considered in this paper: (1) Logistic regression and its variants (with  1 or  2 norm regularizations); (2) Random F orest; (3) Support Vector Machine (SVM)<sup>24</sup> , where we only consider the linear case; (4) Gradient Boosting Decision Tree (GBDT)<sup>25</sup> ; (5) Multi-Layer Perceptron (MLP)<sup>14</sup> . We introduce more details of these models below. 

- Logistic Regression (LR). Logistic regression is a popular model in applied health service research. It can be used to explain the relationship between one dependent binary variable and one or more independent variables. Mathematically, we model the probability logit (which is the log-odds) of the probability of an event, as a linear combination of predictive variables, i.e., _logit_ ( _p_ ( _y_ = 1| **x** ; **w** )) = **w** _T_ **x** , where _logit_ ( _p_ ) = log( 1 − _<u>p</u> p_ ). The regression coefficients **w** are usually estimated through the maximum likelihood estimation (MLE) procedure, which is equivalent to minimize the negative total data log-likelihood as 

- **w** = arg min **w** −∑ _iN_ log _p_ ( _yi_ | **x** _i_ ; **w** ). 

- • Logistic Regression with  1 penalty (LR_l1). Sometimes the number of independent variables is large, in which case not every of them is useful. In order to promote model sparsity and pick out variables that really contribute to the prediction, we can add  1 regularization to the negative total data log-likelihood<sup>26</sup> , that is, **w** = arg min **w** −∑ _iN_ log _p_ ( _yi_ | **x** _i_ ; **w** ) + _β_ || **w** ||1<sup>.</sup><sup>_β_> 0 is the tradeoff parameter.</sup> 

- • Logistic Regression with  2 penalty (LR_l2). We can also add  2 regularization to the negative total data log-likelihood to improve numerical stability in the parameter estimation process, i.e., **w** = arg min **w** −∑ _iN_ log _p_ ( _yi_ | **x** _i_ ; **w** ) + _β_ || **w** ||2<sup>.</sup><sup>_β_> 0 is the tradeoff parameter.</sup> 

- • Random Forest (RF)<sup>27</sup> . Random forest is an ensemble learning method, which constructs multiple decision trees (each on a randomly sampled feature set) at the training stage. Their outputs will be aggregated in the prediction stage (usually through majority voting) as the final result. 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

3 

www.nature.com/scientificreports 

www.nature.com/scientificreports/ 

- Support Vector Machine (SVM)<sup>24</sup> . SVM is a discriminative classifier which constructs a hyperplane to separate the two classes with the maximum margin. In particular, solves the following optimization problem **w** = arg min **w** ∑1 _N_ max (0,1 − _yi_ ( **w** _T_ **x** _i_ − _b_ )) + _λ_ || **w** ||2<sup>, where</sup><sup>**w**is the separation hyperplane.</sup> 

- • Gradient Boosting Decision Tree (GBDT)<sup>25</sup> . Gradient boosting is an ensemble model comprising of a set of weak learners obtained in a stage-wise fashion through the minimization of some differentiable prediction loss using functional gradient descent. For GDBT those weak learners are set to be decision trees. 

- Multi-layer Perceptron (MLP)<sup>28</sup> . Multi-layer perceptron is a class of feed-forward artificial neural network. It consists of multiple hidden layers with nonlinear processing units, and is trained with the back-propagation technique. 

**Deep Learning Methods.** One limitation of all traditional machine learning models we introduced above is that they need to aggregate patient features in the observation window to form patient vectors. This ignores the temporality in patient records, which is usually important in healthcare settings as it indicates the disease progression process. To explore such temporality, we construct a set of deep learning models, specifically Convolutional Neural Networks (CNN)<sup>13</sup> , Recurrent Neural Networks (RNN)<sup>18</sup> and their variants (e.g., Long-Short Term Memory (LSTM)<sup>29</sup> and Gated Recurrent Unit (GRU)<sup>30</sup> ). In addition, we further incorporate contextual event embedding, time-sensitive modeling and attention mechanism into the model building process to enhance the model performance. The details are explained as follows. 

_Contextual Event Embedding._ If we concatenate the claim records for each patient according to their associated timestamps, we can obtain a medical event sequence for each patient. Contextual embedding<sup>31</sup> is a class of techniques that learn a vector based representation for each event in the sequence, such that each vector encodes the contextual information around its corresponding event. Word2Vec<sup>32</sup> is one representative contextual embedding technique that learns an embedded vector for each word in a document corpus (each document can be viewed as a word sequence). 

Claims data can be analogous to the text data as they contain sequences of medical events, which play a similar role as words in texts. The difference is that each medical event is associated with a concrete timestamp in claims data, which could be critical. For example, two medical events with one day and one year gap can have completely different meanings in healthcare setting. Therefore we investigated the following variants of contextual embedding techniques. 

1. Using a time window instead of a context window to generate event contexts. 

2. Weighting the event pairs according to the temporal gap between them. Higher weights will be given to temporally closer event pairs 

3. Med2Vec<sup>33</sup> , which is a contextual embedding technique that is able to learn both event -level and visit-level representations for longitudinal patient records, where the temporal gap information is appended as an additional dimension in the event/visit vectors. 

More details of these methods are provided in Supplementary Materials. In addition to these methods, we also implemented the one-hot embedding model as the baseline. Specifically, let _V_ be the number of unique medical events, then the one-hot representation of an event is a _V_ -dimensional binary vector with value 1 on the dimension corresponding to the event and all other entries being 0. 

_Time Fusion in Deep Models._ In order to conveniently explore the event temporalities in patient claims, we investigated three types of patient representations. 

1. _Sequence Representation_ . We represent the records for each patient as two sequences, an event sequence and a timestamp sequence, and then treat the prediction problem as a sequence classification problem. Specifically, let _V_ be the number of distinct medical events. For any specific patient, we have the event sequence 〈 _c_ 1, _c_ 2,  , _cL_ 〉, and the the corresponding timestamp sequence 〈 _t_ 1, _t_ 2,  , _tL_ 〉, where _ci_ ∈ [1, 2,  , _V_ ], and _t_ 1 ≤ _t_ 2 ≤  ≤ _tL_ . We can apply the contextual event embedding techniques introduced above to embed each event _ci_ as a vector **w** _i_ , then the event sequence becomes the vector sequence **w** 1, **w** 2,  , **w** _L_ . Then we can incorporate time information using a time weighting layer. Given the timestamp sequence, we can get a temporal weight _di_ ∝ _softmax_ ( _λ_ ⋅Δ _ti_ )<sup>, where Δ</sup><sup>_ti_is the temporal gap</sup> between _ti_ and the hospital discharge date when the prediction is made on, _λ_ is a time scaling parameter to be learned in the training phase. 

2. _Matrix Representation with Regular Time Intervals (MR-RTI)_ . In this case, we represent the claims records of each patient as a longitudinal matrix similar to what Wang _et al_ .<sup>34</sup> did. The columns correspond to different medical events, so there are **_V_** columns in total. The rows correspond to regular time intervals. For example, each row could represent a day, a week or a month, depending on the time resolution. The ( _i_ , _j_ )-th entry of this matrix is 1, if the _j_ -th event is observed at the _i_ -th timestamp in the patient’s claims, and 0 otherwise. 

3. _Matrix Representation with Irregular Time Intervals (MR-ITI)_ . The MR-RTI representation could be very sparse – if the patient did not pay visit to the clinic on a specific day then he/she will have an all-zero row in the matrix. The MR-ITI representation deletes these all-zero rows in MR-RTI, which greatly reduced the matrix sparsity. However, because the time intervals are no longer regular, we also need to record the exact timestamp for each row in the matrix. This is similar to the sequence representation. 

We summarize the three different patient representations in Fig. 1. 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

4 

www.nature.com/scientificreports 

www.nature.com/scientificreports/ 



**Figure 1.** Three types of patient representations for incorporating the temporal information. ( **a** ) Sequence Representation; ( **b** ) Matrix Representation with Regular Time Intervals (MR-RTI); ( **c** ) Matrix Representation with Irregular Time Intervals (MR-ITI). 



**Figure 2.** AUC performance achieved by predictive models with different types of features and machine learning models. In ( **a** ), ‘hos’, ‘lace’, ‘hand’, ‘knowledge’ represent HOSPITAL score, LACE index, handcrafted feature, and the combination of all these three kinds of features. For the legend, ‘lr’, ‘lrl1’, ‘lrl1’, ‘rf’, ‘svm’, ‘gbdt’, ‘mlp’ represent logistic regression, logistic regression with L1 penalty, logistic regression with L2 penalty, random forest, support vector machine, gradient boosting decision tree, and multi-layer perceptron. The same naming convention is also applied in the legends of the follow-up figures. In ( **b** ), COPD readmission prediction performance with combined data -driven features. For the x-axis, ‘data_bow’, ‘data_tfidf’ and ‘data_bbow’ represent BoW, TFIDF and BBoW features. 

_Attention Mechanism._ In addition to the time weighting layer to incorporate timestamp information, we can also apply attention mechanism on the event embeddings to emphasize more on the important medical events. _T_ The attention weight for event _ci_ is computed using a softmax function _ai_ ∝ _softmax_ ( _β_ **w** _i_ )<sup>, where</sup><sup>_β_is a reference</sup> vector to be learned from the model training process, and **w** _i_ is the embedded vector of _ci_ . This attention weight _ai_ tells us how much attention we should pay on event _ci_ . We can multiply it with the time weight to get a composite weight for each event in the modeling process. 

The overall architecture of the deep learning models we investigated is provided in Fig. 3 in the supplemental material. 

## **Results** 

The detailed experimental results are presented in this section. First we introduce the process of data preprocessing. 

**Data preprocessing.** Our raw data contain 111,992 patients in Geisinger Health System who had at least one COPD related diagnosis (ICD-9 diagnosis codes: 490.**, 491.**, 492.**, 493.2*, 494.**, 496.**) between January 2004 and September 2015. The information contained in patient claims include patient demographics, medication, service location (utilization), diagnosis and procedure. Table 1 in the supplemental material summarizes the details of each type of information. 

We built a three-step pipeline for data preprocessing: data filtering, data labeling and data splitting, which are detailed below. 

_Data Filtering._ We filter the raw patient claims with the following criteria: (1) Keep Main Hospital (MH) claims with status ‘Approved’; (2) Keep patients who have ever been diagnosed with at least one of 491.*, 492.*, and 496.* in MH DX claims; (3) Keep patients who are at least 40 years old; (4) Keep patients with decided gender; (5) Keep patients with at least one Inpatient MH claim in the entire history; (6) Keep patients with observation history 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

5 

www.nature.com/scientificreports 

www.nature.com/scientificreports/ 

|**Variables**|**Mean**|**Std**|**Min**|**Max**|**Variables**|**Mean**|**Std**|**Min**|**Max**|
|---|---|---|---|---|---|---|---|---|---|
|Age|72.10|11.83|29|99|Readm_trans|0.01|0.11|0|6|
|Gender|0.50|0.50|0|1|Readm_final|0.01|0.09|0|2|
|LOS|5.00|6.21|0|389|LACE_L|3.43|1.49|0|7|
|LOAS|9.74|12.28|0|404|LACE_A|2.04|1.40|0|3|
|NOA|1.89|1.36|1|16|LACE_C|2.73|1.15|0|4|
|NOAA|55.17|38.07|1|493|LACE_E|1.85|1.40|0|4|
|Index|1.53|0.90|0|7|HOS_Proc|0|0|0|0|
|Index_trans|0.10|0.36|0|7|HOS_LOS|0.78|0.97|0|2|
|Index_final|0.09|0.30|0|3|HOS_NOAD|1.00|1.19|0|5|
|Readm|0.16|0.56|0|13|HOS_Index|0.68|0.47|0|1|



**Table 2.** Summary statistics of the 67,771 patients. 



**Figure 3.** Comparisons of the predictive performance of different types of data-driven features on COPD readmission. In ( **a** ), ‘dx_bow’, ‘dx_tfidf’, ‘dx_bbow’ represent BoW, TFIDF and BBoW feature for diagnosis records. ‘dx_ccs_bow’, ‘dx_ccs_tfidf’, ‘dx_ccs_bbow’ represent Bow, TFIDF and BBoW feature for grouped diagnosis codes using CCS hierarchy. The same naming convention also applies to ( **b** – **d** ). 

of at least 60 days; (7) Keep patients with at least one pharmacy claim in the entire history. The detailed patient information before and after each filtering criterion can be found in the Supplementary Material. 

_Data Labeling._ In order to build the predictive model, we further label each patient hospital admission as either index admission or readmission. Specifically, a hospital readmission is when a patient who had been discharged from a hospital is admitted again to the same or a different hospital within 30 days. The original hospital admission is referred to as index admission, and the subsequent admission is referred to as readmission. We further have the following inclusion criteria for index admissions in our study. 

> 1. The patient has enrollment information for at least 30 days after the discharge. This is necessary to gaurantee that readmissions within 30 days can be tracked. 

6 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

www.nature.com/scientificreports 

www.nature.com/scientificreports/ 

||**Age**|**Gender**|**LOS**|**LOAS**|**NOA**|**NOAA**|**Index**|
|---|---|---|---|---|---|---|---|
|LR|0.0032|0.0996|0.0174|−0.0089|0.0861|0.0056|0.0002|
|LR_l1|0.0026|0.0987|0.0172|−0.0087|0.0847|0.0056|0.0|
||**Index_trans**|**Index_final**|**Readm**|**Readm_trans**|**Readm_final**|**LACE_L**|**LACE_A**|
|LR|−0.1364|0.1081|0.0893|0.2166|−0.1918|0.0737|0.0213|
|LR_l1|−0.1238|0.0914|0.0885|0.1177|−0.0677|0.0732|0.0235|
||**LACE_C**|**LACE_E**|**HOS_Proc**|**HOS_LOS**|**HOS_NOAD**|**HOS_Index**|**Intercept**|
|LR|0.0444|0.0761|0.0|0.0536|0.0747|0.0071|−1.5246|
|LR_l1|0.0493|0.0761|0.0|0.0537|0.0753|0.0|−1.4950|



**Table 3.** Coefficients of knowledge-driven features in LR model and LR model with  1 penalty. 

2. The patient was enrolled for 12 months prior to the index admission. This is necessary to gather adequate clinical information for accurate risk adjustment. 

One issue we need to deal with is hospital transfer. A hospital transfer is the case in which a patient is discharged from a hospital and admitted to another hospital at the same day. Therefore, we have 6 classes of hospital admissions in total: index admission, index transfer (the patient is transferred at the same day of the index admission), index final (this is the last stop of the transfer), readmission, readmission transfer, and readmission final. The numbers of all 6 kinds of admissions are provided in the supplemental material. Finally, we get 67,771 index admissions (i.e, index and index_final), among which 10,265 (15.15%) samples are followed by a 30-day readmission. There are 27,138 patients involved in these hospital stays. We summarize the statistical characteristics of the overall samples in Table 2. 

_Data Splitting._ We apply five-fold cross validation on all 27,138 patients to evaluate the performance of the investigated approaches. Note that we cannot apply five-fold cross validation on discharges, because if one patient has multiple discharges, it is possible that some of these discharges are in training set while some are in validation set. This may produce overly optimistic performance due to label leaking. 

**traditional Methods.** We implemented seven different traditional machine learning models with different of feature sets as introduced in the Methods Section. The results are summarized below. 

_Knowledge-driven features._ The prediction performance in terms of Area Under the r eceiver o perating c haracteristic (ROC) Curve (AUC) with knowledge-driven features are shown in Fig. 2(a). These features are extracted from the one-year history prior to the discharge of the index admission. We can observe that: 

1. The two baseline methods, HOSPITAL score and LACE index, have similar performance with AUC around 0.60, and HOSPITAL score is slightly better. 

2. Our handcrafted features can produce better performance than the two baseline methods. 

3. The combined knowledge-driven features lead to the best performance, with the mean AUC of 0.643 using the GBDT classifier. 

To better understand knowledge-driven features, we further investigate the trained logistic regression model. We record the coefficients of all predictors in Table 3. We can find that older age, male gender, longer length of stay, and more admissions in previous year will increase the risk of readmission. It is interesting to notice that a larger number of index_trans in the previous year will decrease the risk. The reason could be that more hospital transfers lead to better patient care. The LACE index features and HOSPITAL score features have positive relationship with readmission risk, except HOS_Proc, HOS_index. 

_Data-driven features._ For data-driven features, we combine the grouped diagnosis, grouped procedure, grouped pharmacy and location codes together to obtain the combined data-driven features, whose performances are summarized in Fig. 2(b). From the figure we can observe that the best mean AUC value is around 0.646, which can be obtained from the BoW representation using GBDT classifier. 

We further explore how different types of data -driven features influence the prediction performance. These features are extracted from the one-year history prior to the discharge date of the index admission. The results are shown in Fig. 3, from which we can observe that: 

1. The grouped codes (e.g., diagnosis codes grouped by CCS) can produce better performances than the original raw codes. This is potentially due to the high dimensionality of the raw codes, which results in highly sparse feature representations. Grouping the codes can greatly reduce the dimensionality and thus increase the density of the feature vector. 

2. Comparing with other features, diagnosis and procedure are more useful to the readmission prediction task, while the pharmacy feature is not very informative. 

3. The GBDT classifier generally achieves the best performance among the seven traditional classifiers for most of the features. 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

7 

www.nature.com/scientificreports 

www.nature.com/scientificreports/ 

||**LR**|**LR_l1**|**LR_l2**|**RF**|**SVM**|**GBDT**|**MLP**|
|---|---|---|---|---|---|---|---|
|One year|0.617|0.616|0.617|0.636|0.612|0.653|0.571|
|Full history|0.635|0.644|0.645|0.624|0.643|0.654|0.627|



**Table 4.** Prediction performance for comprehensive features extracted from one-year history and from full history. 



**Figure 4.** Performance comparison among different time fusion and different embedding strategies. In ( **a** ), ‘basic’ indicates the most basic model where we use the sequence input without any time weighting or attention mechanisms. ‘basic_day’, ‘basic_week’ and ‘basic_month’ indicate the model using matrix input with regular time interval, whose time granularity is day, week and month. ‘time_day’, ‘att_day’, ‘time_att_day’ indicate the model using matrix input of irregular time interval, plus the time weighting layer, attention weighting layer, and both layers. For all models, we adopt Word2Vec embedding, and let the embedding layer be trainable when training the deep models. In ( **b** ),’skipgrams’,’skipgrams_w’ and’med2vec’ indicate the models using embedding matrix learned by Skip-grams model, the time weighted Skip-grams model, and the Med2vec model. The suffix’_fixed’ means that we keep the parameters in the embedding layer fixed during training.’one-hot’ indicates the model simply uses the one-hot embedding layer. 

_The Effect of Observation Window Lengths._ We also explored how the observation window length will affect the readmission prediction performance. We compared the performance of one-year observation window against the full-history. All knowledge- and data-driven features are concatenated. The results are summarized in Table 4, from which we can observe that: 

1. For the one-year observation window, we can obtain the best AUC of 0.653 using GBDT, which is better than knowledge-or data-driven features alone. 

2. Increasing the observation window from one year to full history barely improves the performance of GBDT, while most of other models get obvious improvements. 

**Deep Learning Methods.** For deep learning experiments, we focus on the impact of different time fusion and embedding strategies. 

_Time Fusion Strategies._ We compare the performance of different time fusion methods in Fig. 4a, from which we can observe that: 

1. The basic sequence classification without considering time information generates the worst performance. 

   - This means that considering the exact event timestamps can indeed improve the prediction performance. 

2. Matrix representation with regular time intervals performs better than sequence representation. 

3. Matrix representation with irregular time interval combined with event attentions does not necessarily improve the prediction performance. 

4. If we use a coarse time granularity, for example by week or month instead of by day in matrix representations, the prediction AUC can be improved. The best performance of AUC 0.650 is achieved by GRU model based on matrix representation by month. 

_Embedding Strategies._ We also explored the impact of different embedding strategies. We used the matrix representation with regular time intervals aggregated by month. The performance of using different embedding strategies is summarized in Fig. 4(b), from which we do not observe significant differences across the performances of different embedding strategies. 

8 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

www.nature.com/scientificreports 

www.nature.com/scientificreports/ 

## **Discussions** 

From our investigations above on the task of readmission risk prediction for COPD patients based on patient claims data, we have the following observations. 

1. _Knowledge is powerful_ . Similar to what has been observed in Rajkomar _et al_ .<sup>19</sup> , simple models based on clinical knowledge, such as LACE and Hospital Score, work pretty well in reality. We also expanded the knowledge-driven features used in these two models to a broader set (see the handcrafted features in Table 1), which can further improve the prediction performance in terms of AUC (from 0.61 to 0.64). Comparing with data-driven features, those knowledge-driven features are highly interpretable and generalizable. 

2. _Data-driven features are helpful_ . With the data-driven features, we can improve the prediction performance (from 0.64 to 0.65). Combining the knowledge- and data-driven features leads to the best prediction performance (around 0.653). 

3. _GDBT is powerful_ . Comparing with other traditional machine learning models, GBDT can achieve better performance almost across all different experimental settings, and it obtained the best performance with the combination of both knowledge- and data-driven features. 

4. _Longer history barely helps_ . We do not observe much differences on the prediction performance on patient records with one-year observation window or full-history. This observation also explains implicitly why only one year history was used in both LACE and HOSPITAL Score models. 

5. _Deep learning barely helps_ . We have systematically investigated the performance of various deep learning models, including the variants of CNN and RNN with different representation, embedding and time-sensitive strategies. However, the best performance achieved among them is on par with the best performance of GDBT (around 0.65). The same phenomenon is also observed in Rajkomar _et al_ .<sup>19</sup> . 

With these observations, we can conclude that predicting the risk of hospital readmission is difficult based on only claims data. Machine learning models can benefit when combining patient data with clinical knowledge. This is potentially be explained from the following aspects. 

1. Medicine has been a research discipline with long history. The medical knowledge people accumulated from clinical practice are invaluable and powerful. 

2. Unlike other application domains such as computer vision and natural language processing, where deep learning models have been shown to be very powerful, medical problems are much more complicated and with less available training samples. This means that it is difficult to have a ‘sufficiently large’ patient dataset to train a very good machine learning model. In this case, incorporating domain knowledge into the model building process is of vital importance, and complex models do not necessarily lead to better performance as they need even more training samples. 

3. The information contained in patient claims records may not be sufficient for building good hospital readmission risk prediction models. Some important and relevant clinical features, such as GOLD severity grade, are not available. More comprehensive and finer granular patient data, such as electronic health records, could be potentially more helpful. 

4. Our claims data lacks mortality information of patients. In fact, hospital readmission risk and death risk are competing clinical risks, since patients that die after discharge cannot be readmitted, which makes the risk of readmission and death after discharge are often negatively linked. However, there could be some common causes for both risks (e.g., condition exacerbation), which could confuse the predictive models. 

## **Conclusion** 

We conducted a comprehensive study on predictive modeling of the 30 day readmission risk of COPD patients based on their claims records with various machine learning models. We constructed both knowledge- and data-driven features from the patients’ claim records to train the predictive models. Both traditional and modern machine learning models are investigated. The results showed that the combination of both knowledge and data driven features can lead to the best prediction performance, and complicated models such as deep learning can barely improvement the performance. Our studies verify the importance of medical knowledge in the predictive modeling process, as well as the demands for better patient data. 

## **References** 

1. Chronic obstructive pulmonary disease (copd). http://www.who.int/news-room/fact-sheets/detail/chronic-obstructive-pulmonarydisease-(copd) (2016). 

2. Elixhauser, A. _et al_ . Readmissions for chronic obstructive pulmonary disease. _Rockville, MD: Agency for Heal. Care Res. Qual_ . (2011). 

3. Purdy, S., Griffin, T., Salisbury, C. & Sharp, D. Prioritizing ambulatory care sensitive hospital admissions in england for research and intervention: a delphi exercise. _Prim. Heal. Care Res. & Dev._ **11** , 41–50 (2010). 

4. Harries, T. H. _et al_ . Hospital readmissions for copd: a retrospective longitudinal study. _NPJ primary care respiratory medicine_ **27** , 31 (2017). 

5. Garcia-Aymerich, J. _et al_ . Risk factors of readmission to hospital for a copd exacerbation: a prospective study. _Thorax_ **58** , 100–105 (2003). 

6. vanWalraven, C. _et al_ . Derivation and validation of an index to predict early death or unplanned readmission after discharge from hospital to the community. _Can. Med. Assoc. J._ **182** , 551–557 (2010). 

7. Donzé, J., Aujesky, D., Williams, D. & Schnipper, J. L. Potentially avoidable 30-day hospital readmissions in medical patients: derivation and validation of a prediction model. _JAMA internal medicine_ **173** , 632–638 (2013). 

8. Hosseinzadeh, A., Izadi, M. T., Verma, A., Precup, D. & Buckeridge, D. L. Assessing the predictability of hospital readmission using machine learning. In _The Twenty-Fifth Innovative Applications of Artificial Intelligence Conference_ (2013). 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

9 

www.nature.com/scientificreports 

www.nature.com/scientificreports/ 

9. Caruana, R. _et al_ . Intelligible models for healthcare: Predicting pneumonia risk and hospital 30-day readmission. In _Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , 1721–1730 (ACM, 2015). 

10. Sushmita, S. _et al_ . Predicting 30-day risk and cost of “all-cause” hospital readmissions. In _AAAI Workshop: Expanding the Boundaries of Health Informatics Using AI_ (2016). 

11. LeCun, Y., Bengio, Y. & Hinton, G. Deep learning. _nature_ **521** , 436 (2015). 

12. Wang, H. _et al_ . Predicting hospital readmission via cost-sensitive deep learning. _IEEE/ACM Transactions on Comput. Biol. Bioinforma_ . (2018). 

13. Krizhevsky, A., Sutskever, I. & Hinton, G. E. Imagenet classification with deep convolutional neural networks. In _Advances in neural information processing systems_ , 1097–1105 (2012). 

14. Rosenblatt, F. Principles of neurodynamics. perceptrons and the theory of brain mechanisms. _Tech. Rep., CORNELL AERONAUTICAL LAB INC BUFFALO NY_ (1961). 

15. Xiao, C., Ma, T., Dieng, A. B., Blei, D. M. & Wang, F. Readmission prediction via deep contextual embedding of clinical concepts. _PloS one_ **13** , e0195024 (2018). 

16. Dieng, A. B., Wang, C., Gao, J. & Paisley, J. TopicRNN: A recurrent neural network with long-range semantic dependency. _arXiv preprint arXiv:1611.01702_ (2016). 

17. Blei, D. M. Probabilistic topic models. _Commun. ACM_ **55** , 77–84 (2012). 

18. Mikolov, T., Karafiát, M., Burget, L., Černockỳ, J. & Khudanpur, S. Recurrent neural network based language model. In _Eleventh Annual Conference of the International Speech Communication Association_ (2010). 

19. Rajkomar, A. _et al_ . Scalable and accurate deep learning with electronic health records. NPJ Digit. _Medicine_ **1** , 18 (2018). 

20. Liu, H. & Motoda, H. _Feature extraction, construction and selection: A data mining perspective_ , vol. 453 (Springer Science & Business Media, 1998). 

21. Michalski, R. S., Carbonell, J. G. & Mitchell, T. M. _Machine learning: An artificial intelligence approach_ . (Springer Science & Business Media, 2013). 

22. Vestbo, J. _et al_ . Global strategy for the diagnosis, management, and prevention of chronic obstructive pulmonary disease: Gold executive summary. _Am. journal respiratory critical care medicine_ **187** , 347–365 (2013). 

23. Manning, C. D., Manning, C. D. & Schütze, H. _Foundations of statistical natural language processing_ . (MIT press, 1999). 

24. Cortes, C. & Vapnik, V. Support-vector networks. _Mach. learning_ **20** , 273–297 (1995). 

25. Friedman, J. H. Greedy function approximation: a gradient boosting machine. _Annals statistics_ 1189–1232 (2001). 

26. Lee, S.-I., Lee, H., Abbeel, P. & Ng, A. Y. Efficient l˜ 1 regularized logistic regression. _In AAAI_ **6** , 401–408 (2006). 

27. Breiman, L. Random forests. _Mach. learning_ **45** , 5–32 (2001). 

28. Rumelhart, D. E., Hinton, G. E. & Williams, R. J. Learning representations by back-propagating errors. _nature_ **323** , 533 (1986). 

29. Hochreiter, S. & Schmidhuber, J. Long short-term memory. _Neural computation_ **9** , 1735–1780 (1997). 

30. Cho, K. _et al_ . Learning phrase representations using rnn encoder-decoder for statistical machine translation. _arXiv preprint arXiv:1406.1078_ (2014). 

31. Farhan, W. _et al_ . A predictive model for medical events based on contextual embedding of temporal sequences. _JMIR medical informatics_ 4 (2016). 

32. Mikolov, T., Chen, K., Corrado, G. & Dean, J. Efficient estimation of word representations in vector space. _arXiv preprint arXiv:1301.3781_ (2013). 

33. Choi, E. _et al_ . Multi-layer representation learning for medical concepts. In _Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , 1495–1504 (ACM, 2016). 

34. Wang, F. _et al_ . A framework for mining signatures from event sequences and its applications in healthcare data. _IEEE transactions on pattern analysis machine intelligence_ **35** , 272–285 (2013). 

## **Acknowledgements** 

The work of F. W. is partially supported by NSF IIS-1716432 and NSF IIS-1750326. The authors would like to acknowledge Geisinger Health System for providing the data, and Dr. Yang Jiang for the insightful feedbacks about the research. X. M. is also grateful for the valuable comments from Prof. Ting Chen, and the financial support from China Scholarship Council (CSC). 

## **Author Contributions** 

X.M. and F.W. designed the approach. B.Y. prepared the data. X.M. conducted all the experiments and summarized the results. X.M. and F.W. wrote the paper. All authors polished the manuscript. 

## **Additional Information** 

**Supplementary information** accompanies this paper at https://doi.org/10.1038/s41598-019-39071-y. 

**Competing Interests:** The authors declare no competing interests. 

**Publisher’s note:** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/. 

© The Author(s) 2019 

Scientific **RepoRts** | _(2019) 9:2362_ | https://doi.org/10.1038/s41598-019-39071-y 

10 

