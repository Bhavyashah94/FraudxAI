---
title: "Financial Fraud Detection Using Value-at-Risk with Machine Learning in Skewed Data"
year: 2022
original_file: "data_mining_for_credit_card_fraud_a.pdf"
pdf_path: "docs/papers\2022_data_mining_for_credit_card_fraud_a.pdf"
---

# Financial Fraud Detection Using Value-at-Risk with Machine Learning in Skewed Data

**Year:** 2022  
**Local PDF:** [`2022_data_mining_for_credit_card_fraud_a.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2022_data_mining_for_credit_card_fraud_a.pdf)

---

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



Date of publication xxxx 00, 0000, date of current version xxxx 00, 0000. 

_Digital Object Identifier 10.1109/ACCESS.2022.Doi Number_ 

# **Financial Fraud Detection Using Value-at-Risk with Machine Learning in Skewed Data** 

## **Abdullahi Ubale Usman**<sup>**1,3**</sup> **, Sunusi Bala Abdullahi**<sup>**2**</sup> **, Yu Liping**<sup>**1**</sup> ***,** **<mark>Bayan Alghofaily</mark>**<sup>**5**</sup> **, Ahmed S. Almasoud**<sup>**5**</sup> **, Amjad Rehman**<sup>**5**</sup> 

1School of Statistics and Mathematics, Zhejiang Gongshang University, Hangzhou, 310018, China. 

2Department of Electronics and Telecommunication Engineering, Faculty of Engineering, King Mongkut’s University of Technology Thonburi, Bang Mod, Thrung Khru, Bangkok 10140, Thailand. 

3Department of Statistics, Kano University of Science and Technology, Wudil 713281, Nigeria. 

4College of Computer & Information Sciences,  Prince Sultan University Riyadh Saudi Arabia 

*Corresponding Author: Y. Liping, yvliping@zjgsu.edu.cn 

**ABSTRACT** The significant losses that banks and other financial organizations suffered due to new bank account (NBA) fraud are alarming as the number of online banking service users increases. The inherent skewness and rarity of NBA fraud instances have been a major challenge to the machine learning (ML) models and happen when non-fraud instances outweigh the fraud instances, which leads the ML models to overlook and erroneously consider fraud as non-fraud instances. Such errors can erode the confidence and trust of customers. Existing studies consider fraud patterns instead of potential losses of NBA fraud risk features while addressing the skewness of fraud datasets. The detection of NBA fraud is proposed in this research within the context of value-at-risk as a risk measure that considers fraud instances as a worst-case scenario. Value-at-risk uses historical simulation to estimate potential losses of risk features and model them as a skewed tail distribution. The risk-return features obtained from value-at-risk were classified using ML on the bank account fraud (BAF) Dataset. The value-at-risk handles the fraud skewness using an adjustable threshold probability range to attach weight to the skewed NBA fraud instances. A novel detection rate (DT) metric that considers risk fraud features was used to measure the performance of the fraud detection model. An improved fraud detection model is achieved using a K-nearest neighbor with a true positive (TP) rate of 0.95 and a DT rate of 0.9406. Under an acceptable loss tolerance in the banking sector, value-at-risk presents an intelligent approach for establishing data-driven criteria for fraud risk management. 

**INDEX TERMS** Detection rate, Fraud detection, K-nearest neighbor, Skewed instances, Value-at-risk. 

### **_I._ INTRODUCTION** 

The Association of Certified Fraud Examiners (ACFE) 2022 released a financial fraud report stating that 2,110 fraud cases involving industries in financial sectors in 133 countries resulted in losses of around $3.6 billion[1]. Financial fraud can be termed as the deliberate employment of unlawful procedures or tactics to obtain financial gain[2]. The consequences of financial fraud can potentially disrupt economies, raise living expenses, and undermine consumer confidence[3]. Forms of financial fraud include insurance fraud, money laundering, new bank account fraud, credit and debit card fraud, mortgage fraud, and many more[4], [5]. The act of opening an account to commit fraud at banks or other financial organizations is known as "new bank account 

(NBA) fraud"[6]. Fraud not only results in immediate financial losses and erodes public confidence in institutions, but has broader consequences, affecting customers and financial systems through market instability and contributing to larger macroeconomic downturns[7]. Fraud datasets typically exhibit some properties including skewness, evolving patterns, highly dimensional, and restricted access to relevant information[3]. Specifically, fraud skewness which represents the majority fraud class over the non-fraud class has been a major concern to studies, as it affects the performance of fraud detection model. The Skewed fraud instances can have a bad influence on machine learning algorithms such as distance-based algorithms[8]. Previous efforts in tackling fraud involve developing rule-based expert 

VOLUME XX, 2017 

1 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



systems, statistical methods, machine learning, and riskbased methods[9], [10]. Due to the cost of maintenance and the inefficiency of rule-based methods[10], decision-makers decide to utilize statistical methods such as autoregressive models to handle financial fraud[11], [12], [13]. The complex patterns and high dimensional nature of frauds make the statistical methods less effective, as such machine learning models were deployed[10], [14]. However, some of the studies that utilize machine learning techniques were found to have a high False Positive (FP) rate[15], [16], [17]. Machine learning models can potentially handle highdimensional data and complex patterns of fraud instances. To evaluate the effectiveness of machine learning model, Jesus et. al[18] presented the first domain-specific and realworld bank account fraud (BAF) dataset. The datasets were generated using generative adversarial networks (GANs) and evaluated using light gradient boosting method (LGBM).The study[18], [19] utilizes 25 sets of hyperparameter configurations to optimize the LGBM model, utility aware reweighing was used to handle the class skewness of BAF dataset. The study[15] utilizes stacking in ensembled learning with majority voting to evaluate the BAF dataset and address the changing fraud patterns. The study[20] uses federated learning in addressing data privacy issues of BAF dataset and deep neural networks to classify fraud instances. These studies achieve good performance in addressing BAF challenges; However, the studies do not consider the potential losses of fraud risk features. To our knowledge, little research exists that employs machine learning techniques in NBA fraud detection. The detection of NBA fraud is proposed in this paper within the context of risk management that uses value-at-risk to considers skewed fraud instances as a worst-case scenario. To adequately estimate the losses of fraud risks, value-at-risk was augmented with expected loss and expected shortfall of frauds which further quantifies the mean and extreme loss effects respectively. These risk measures combination will allow the quantification of risks across mean, worst-case, and extreme scenarios. Value-at-risk employs historical simulation to estimate potential losses of risk features. The risk-return features obtained from value-at-risk are based on assessing their risk exposure to fraud risk. The risk-return features are sent as input to the NBA fraud detection model. Different machine learning models were trained; However, the K-nearest neighbor outperformed other models. The contributions of this paper are: 

• This paper used an extreme value theorem to model the tails (potential losses) instead of the fraud pattern. 

• This paper used value-at-risk to <mark>model the skewness of fraud instances more efficiently.</mark> 

• This paper utilized historical simulation to estimate value-at-risk as it makes no assumptions on any distribution. 

• This paper used novel detection rate performance metrics to capture the overall performance in detection of NBA fraud instances that incorporate risk fraud factors. 

The remainder of the paper is arranged as follows: The study's review of the literature is presented in Section 2. The problem definition is presented in Section 3. The materials and procedures are presented in Section 4. The experimental setup is presented in Section 5. The results are presented in Section 6. The study's conclusions and discussions are presented in Section 7. 

### **_II._ LITERATURE REVIEW** 

This section presents related studies in financial fraud detection. Different studies exist that utilize both statistical and artificial intelligence-based methods in the context of a risk and financial fraud perspective. 

### **_A. STATISTICAL METHODS OF FRAUD_** 

### **_DETECTION_** 

Many studies in the literature utilize statistical methods in evaluating financial fraud. Specifically, significant studies were found to utilize ordinary least squares (OLS) regression and autoregressive (AR) models for financial fraud evaluation. Using the Tehran Stock Exchange dataset, the study[21] uses a regression model to investigate the association between auditor characteristics and fraud detection in emerging economies. The authors provide useful information for improving the reliability of the findings. Using pooled OLS and panel regressions, the study[22] investigates the effect of political alignment on corporate fraud convictions, offering insights into the connection between politics and fraud. The authors use state-level data from 2003 to 2018 on US corporate fraud convictions and party affiliation. The study[23] utilizes OLS to investigate financial factors of financial fraud, which is attributed to the fraud triangle. The study[24] uses logistic regression to discover that external pressures and financial stability had a favorable impact on financial reporting fraud. On the other hand, collaboration, arrogance, changes in directors, incompetent oversight, and hubris have little bearing on false financial reporting. The study[25] provides evidence for the contribution of gender diversity to fraud commission and detection in Chinese listed businesses between 2007 and 2018 using bivariate probit model. The authors opined that female corporate executives are linked to a stronger ability to detect fraud, which lowers the likelihood that businesses to commit fraud. From the standpoint of external auditors, the study[26] sheds light on the causes of fraud and the function of forensic accounting using regression analysis to analyze Lebanese data. The study[4] discovered that while the overall number of employees engaged in fraud affects the performance of money banks in Nigeria, the number of fraud cases and the total amount lost to fraud had a favorable influence. The use of statistical methods by the author such as OLS regression, Pearson correlation, and descriptive analysis strengthens the findings by the authors. The sales growth index and the depreciation index factors make up the M-score are used in the study[27] to analyze the possibility of profit management using the Athens Stock Exchange 

VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



Market. It is pertinent to know that a large body of literature exists that utilizes the AR model. To handle[12] large-scale non-uniform transactions more quickly, the authors employ the AR model, which makes it appropriate for detecting money laundering operations. The study[11] uses factor analysis to generate the composite indicator, fractional integration (ARFIMA), and fractional cointegration VAR (FCVAR) approaches to evaluate the behavior of the composite suspicion tax fraud indicator about GDP and tax collection. The study[13] employs the AR model, which is appropriate for studying networks with such topologies and applying it to the detection of financial transaction fraud since it considers the block-wise structure of networks. The authors discovered that, in line with reality, there is a risk relationship between fraudulent groups and ordinary loan applicants. The study[28] outlined specific identification indicators that help with the detection of financial fraud using digital distribution laws, and the authors demonstrate that the probability of financial fraud increases significantly as the deviation of financial data distribution from Benford's law increases. 

In summary, a large body of literature uses statistical methods to analyze the causes and effects that influence financial fraud, but due to the complex nature and scalability of fraud, statistical methods are not enough to adequately examine financial fraud. 

### **_B. RISK-BASED METHODS OF FRAUD_** 

### **_DETECTION_** 

This section presents the financial fraud assessment from the perspective of risk mitigation. The existing studies utilize different risk measures such as value-at-risk (VaR), expected loss, and expected shortfall to assess the level of risk of fraud. The study[29] offers strategies for breaking down the risk of fraud, identifying potential fraudsters, and enabling more targeted anti-fraud measures by tying the motivation of the fraud triangle to human tendencies that lead to specific actions as well as the meta-model of fraud together. Regression analysis is utilized in the study[30] to look at how enterprises manage risk to determine how control environments, risk assessments, control activities, information and communication, and monitoring contributed to fraud prevention and detection efforts in Indonesian firms. The study[31] defined additional security attributes that might have an impact on the cloud system and carried out an anomaly detection based on risk assessment named parallel processing (PP) that covers cyber threats and exploitation likelihoods. The model checker is then employed to determine the risk exposure rates associated with the respective attacks. The study[32] proposes a framework in which doubly-truncated severity distributions are used to estimate the operational risk and offered a framework that includes database construction and risk modeling. By applying value-at-risk and expected shortfall to identify operational risk sources like external fraud risk and legal risk sections, the authors were able to produce better and 

consistent results. The study[33] uses the number of compromised records to determine the cost of a data breach; the findings indicate that the total number of affected records has a Fréchet distribution, random forest is used for estimating the number of such records. The study[34] uses the estimate of generalized extreme value parameters to evaluates competency, digital technology abilities, and personality qualities that may improve the ability of external auditors to identify fraud risk, the efficiency of fraud risk assessment was linked to digital technology abilities through the application of the partial least-squares structural equation model (PLS-SEM). The study[35] identified a positive correlation between fraud risk assessment and management and the efficient use of forensic accounting using chi-square, fisher test, and correlation, however, there is no relationship between fraud risk assessment and management in terms of techniques causing fraud. The study[9] examines fraud using ensemble learners for anomaly detection and also handles data skewness, a triage model that receives input from the ensemble model, and a risk model that estimates the financial losses. The authors successfully provide an effective fraud risk-based detection, from machine learning techniques to risk assessment, but do not to evaluate fraud detection by first considering the risk component before subjecting it to machine learning detection. 

In summary, risk measures are good in the assessment and management of the features associated with fraud for effective fraud prevention and control. However, due to the nonlinearity, high dimension, and complex nature of fraud, these risk measures need to be augmented with other techniques such as machine learning techniques that enable proper and efficient fraud prevention and detection. 

### **_C. MACHINE LEARNING METHODS IN FRAUD_** 

### **_DETECTION_** 

This section presents studies that utilize machine learning techniques for the classification of fraud applications. The majority of the presented studies consider the detection while addressing the skewed nature of fraud instances. Sampling methods, hybrid methods, and other novel methods are majorly used to overcome the skewed nature of fraud datasets. The study[36] addresses class skewness in credit card fraud using quantum machine learning (QML) and support vector machines (SVM). The results show that classic machine learning techniques are still useful for nontime series data, whereas QML applications can be used for time-series-based and highly skewed data. Quantum neural network (QNN) achieves good performance in fraud detection by the study[37]. The study[38] trained different machine learning models, all of which were using default implementations and parameters, XGBoost performed more accurately than any other models. The effectiveness of telecom fraud is assessed in the study[39] using a dynamic graph neural network (DGNN), the authors effectively present a suggested method for resolving the issue of telecom fraud detection in extensive phone social networks. To assess 

VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



credit card fraud while considering the skewness of fraud instances, the study[40] makes use of logistics regression (LR), K-nearest neighbor (KNN), decision tree (DT), random forest (RF), and autoencoder (AE) as they can handle skewed data better than other models, the AE model performs better. KNN, linear discriminant analysis (LDA), and linear regression are used in the study[41] to investigate credit card fraud, by addressing the skewed nature of the credit card fraud data and using cross-validation techniques, KNN showed higher performance. Using ARIMA model for fraud detection based on daily transaction counts, the study[14] carried out anomaly detection, the model is contrasted with four industry-standard anomaly detection algorithms: the box plot, isolation forest(IF), local outlier factor (LOF), and K- means models. An ensemble classifier (EC)[42] incorporating bagging and boosting has been used to address the issue of fraud class skewness, the approach are found to perform better when compared to the current methods. The study[43] addresses the issue of skewed datasets by using fuzzy C-means clustering and the selection of related instances. The authors address the issues with conventional under-sampling strategies to enhance the detection performance and accuracy. To identify fraudulent transactions, the study[44] suggested LSTM ensemble, SMOTE-ENN was used to address the problem of fraud skewness. The method outperformed other algorithms in terms of performance, but, SMOTE method may occasionally produce instances that are not typical instances of the minority class. A dynamic ensemble technique[45] for anomaly identification in the Internet of Things systems is proposed. To address the issue of fraud skewness, the borderline-synthetic minority over-sampling approach (Borderline-SMOTE), One-Sided Selection (OSS), and adaptive synthetic (ADASYN) were applied in the study[46], OSS were found to be optimal under-sampling technique and that adaptive synthetic (ADASYN) performs better when employing the gradient tree boosting (GTB) classifier. Random forest ensemble approach[47] performed exceptionally well on oversampling and under-sampling. Though under-sampling usually led to the loss of important information while on the other hand, oversampling brings information that may not be fully a representative of the training set. 

It is widely acknowledged that the skewed distribution of fraud instances presents a significant challenge for many machine learning models. The resampling techniques that have been used in effective fraud skewness mitigation may not be free from certain shortcomings. The resampled instances usually suffer from non-representative of the dataset, overfitting, and the loss of important data. Hence, there is a need to augment the effort of machine learning algorithms with novel approach in overcoming this challenge. 



|[14]|2021|**Study **<br>Anomaly and<br>fraud detection in<br>credit card<br>transactions using<br>the ARIMA<br>dl|**types **<br>Credit<br>card<br>fraud|Box plot,<br>LOF, IF,<br>and K-<br>means|**mance **<br>Recall<br>=<br>0.6667|
|---|---|---|---|---|---|
|[21]|2022|moe<br>The relationship<br>between auditor<br>characteristics<br>and fraud<br>detection|Financi<br>al<br>stateme<br>nt fraud|OLS for<br>regressio<br>n|P-value<br>= 0.45|
|[24]|2022|Hexagon fraud:<br>Detection of<br>fraudulent<br>financial<br>reporting in state-<br>owned enterprises<br>Indonesia|Financi<br>al<br>stateme<br>nt fraud|LR for<br>classifica<br>tion|P-value<br>< 0.01|
|[25]|2022|Gender diversity<br>and financial<br>statement fraud|Financi<br>al<br>stateme<br>nt fraud|Probit<br>model<br>for<br>classifica<br>i|P-value<br>< 0.01|
|[36]|2022|Integrating<br>machine learning<br>algorithms with<br>quantum<br>annealing solvers<br>for online fraud<br>|Credit<br>card<br>fraud|ton<br>SVM for<br>classifica<br>tion|AUC =<br>0.99|
|[27]|2022|detection<br>Detecting the<br>probability of<br>financial fraud<br>due to earnings<br>manipulation in<br>companies listed<br>in Athens Stock<br>ExchaneMarket|Financi<br>al<br>stateme<br>nt fraud|Beneish<br>model<br>for<br>estimatio<br>n|M-<br>score=<br>-2.22|
|[28]|2022|g <br>Detecting<br>financial fraud<br>using two types<br>of Benford<br>factors: evidence<br>fromChina|Corpor<br>ate<br>fraud|OLS for<br>regressio<br>n|Error<br>rate =<br>0.292|
|[11]|2022|<br>A proposal of a<br>suspicion of tax<br>fraud indicator<br>based on Google<br>trends to foresee<br>Spanish tax<br>revenues|Tax<br>fraud|Factor<br>analysis<br>for<br>regressio<br>n|Std<br>error =<br>0.0868|
|[40]|2022|Digital payment<br>fraud detection<br>methods in digital<br>ages and Industry<br>4.0|Credit<br>card<br>fraud|LR,<br>KNN<br>DT, RF<br>& AE for<br>classifica<br>ti|Specifi<br>city =<br>0.98|
|[13]|2022|A blockwise<br>network<br>autoregressive<br>model with the<br>application for<br>|Loan<br>fraud|on<br>AR<br>Model<br>for<br>regressio<br>n|P-value<br>< 0.01|
|[30]|2022|fraud detection<br>The effect of<br>enterprise risk<br>management on<br>prevention and<br>detection of fraud<br>in Indonesia’s<br>localgovernment|Financi<br>al<br>stateme<br>nt fraud|OLS for<br>regressio<br>n|P-value<br>< 0.01|



VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



|[31]|2022|Robust financial<br>fraud alerting<br>system based on<br>the<br>cloud<br>environment|Credit<br>card<br>fraud|PP for<br>classifica<br>tion|TP rate<br>=<br>0.9709|[26]|2023|using KNN,<br>LDA, and linear<br>regression<br>Fraud detection<br>and prevention|Financi<br>al<br>stateme|n<br>OLS for<br>regressio<br>n|P-value<br>< 0.05|
|---|---|---|---|---|---|---|---|---|---|---|---|
|[32]|2022|Operational risk<br>assessment of<br>third-party<br>payment<br>platforms: a case|E-<br>comme<br>rce<br>fraud|VaR, ES<br>for loss<br>estimatio<br>n|VaR =<br>724.46|[4]|2023|Effect of fraud on<br>commercial<br>banks’<br>performance in|ntfraud<br>Financi<br>al fraud|OLS for<br>regressio<br>n|P-value<br>< 0.05|
|||studyofChina||||||<br>Nieria||||
|[44]|2022|<br>A neural network<br>ensemble with<br>feature<br>engineering for<br>imroved credit|Credit<br>card<br>fraud|SVM,<br>MLP,<br>DT &<br>LSTM<br>for|Sensitiv<br>ity =<br>0.996|[43]|2023|g<br>Class balancing<br>framework for<br>credit card fraud<br>detection based<br>lti d|Credit<br>card<br>fraud|ANN,<br>LR,<br>KNN,<br>NB for<br>lifi|Accura<br>cy =<br>0.966|
|||p<br>card fraud<br>detection||<br>classifica<br>tion||||on cuserng an<br>similarity-based<br>selection(SBS)||cassca<br>tion||
|[45]|2022|A dynamic<br>ensemble<br>algorithm for<br>anomaly<br>detection in IoT|Cyber<br>fraud|EC for<br>classifica<br>tion|Accura<br>cy =<br>0.9406|[9]|2023|<br>Online payment<br>fraud: From<br>anomaly<br>detection to risk<br>management|Identity<br>theft<br>fraud|EC for<br>classifica<br>tion|FP rate<br>= 0.004|
|||<br>imbalanced data<br>streams||||[22]|2023|Political<br>alignment and|Corpor<br>ate|Pooled<br>OLS for|P-value<br>< 001|
|[46]|2022|Data sampling<br>strategies for<br>click fraud<br>detection usin|Mobile<br>advertis<br>ing|KNN,<br>DT, DA,<br>LR,<br>SVM|Precisio<br>n =<br>0.6432|||<br>corporate fraud:<br>evidence from the<br>United States of<br>America|<br>fraud|<br>regressio<br>n|.|
|||g<br>imbalanced user<br>click data of<br>online<br>advertising: An<br>emirical review||,<br>GTB &<br>RF for<br>classifica<br>tion||[23]|2024|Fraud detection<br>using fraud<br>triangle theory:<br>Evidence from<br>Chi|Corpor<br>ate<br>fraud|OLS for<br>regressio<br>n|P-value<br>< 0.05|
|[47]|2022|p <br>Credit card fraud<br>detection under<br>extreme|Credit<br>card<br>fraud|AdB,<br>RF,<br>XGB,|Recall<br>=1.00|[37]|2024|na<br>Financial fraud<br>detection using<br>quantum graph|Financi<br>al fraud|QNN for<br>classifica<br>tion|AUC =<br>0.85|
|||imbalanced data:<br>||KNN &<br>||||neural networks||||
|||A comparative<br>||SVM for<br>||||||||
|||study of data-||classifica||**_D._**|**_RES_**|**_ARCH PROBL_**|**_M_**|||
|[19]|2023|levelalgorithms<br>Fairness-aware<br>data valuation for<br>supervised<br>learning|NBA<br>fraud|tion<br>LGBM<br>for<br>classifica<br>tion.|TP rate<br>= 0.8|The pr<br>numbe<br>ML t<br>promis|oblem<br>r of onl<br>echniqu<br>ing perf|of NBA fraud k<br>ine banking serv<br>es applied in<br>ormance in over|eeps incr<br>ice users<br>many re<br>coming N|easing da<br>keeps inc<br>searches<br>BA fraud.|ily as the<br>reasing[3].<br>shows a<br>However,|
|[35]|2023|Application of<br>forensic<br>accounting<br>techniques in the<br>South African<br>banking industry<br>|Financi<br>al<br>stateme<br>nt fraud|Chi-<br>square,<br>Fisher<br>test &<br>Correlati<br>on for<br>|P-value<br>< 0.05|<br>most M<br>skewe<br>utilize<br>True<br>study[1|<br>L strug<br>d as in t<br>LGBM<br>Positive<br>5] util|<br>gles when the d<br>he case of BAF<br>to address skew<br>(TP) rate as a<br>izes stacking i|<br>istribution<br>dataset. T<br>ed fraud<br>perform<br>n ensem|<br>fraud ins<br>he studies<br>instances<br>ance mea<br>bled lear|<br>tances are<br>[18], [19]<br>using the<br>sure. The<br>ning with|
|||for the purpose of<br>fraud risk||testing<br>relations||<br>majori|<br>ty votin|<br>g to evaluate the|<br>BAF dat|<br>aset and a|<br>ddress the|
|||mitigation||hip||changi|ng frau|d patterns. Th|e study[|20] uses|federated|
|[38]|2023|Estimating<br>financial fraud<br>through<br>transaction-level|Credit<br>card<br>fraud|XGBoost<br>for<br>classifica<br>tion|Accura<br>cy =<br>0.998|learnin<br>networ<br>studies|g in ad<br>ks to cl<br>achie|dressing data pr<br>assify fraud wit<br>ve good perfor|ivacy issu<br>h TP rate<br>mance i|es and d<br>as a met<br>n address|eep neural<br>ric. These<br>ing BAF|
|||features and<br>||||<br>challen|<br>ges. H|<br>owever, the st|<br>udies did|<br>not con|<br>sider the|
|[39]|2023|machinelearning<br>Dynamic graph<br>neural network-<br>based fraud<br>detectors against<br>collaborative<br>fraudsters|Teleco<br>mmuni<br>cation<br>fraud|DGNN<br>for<br>classifica<br>tion|Precisio<br>n =<br>0.9292|<br>potenti<br>paper a<br>•<br>losses<br>rarely|<br>al losse<br>ddresse<br>Most<br>of frau<br>and caus|<br>s of fraud risk f<br>s include:<br>existing studie<br>d risk features,<br>e big losses whe|<br>eatures.<br>s do not<br>but frau<br>n they occ|<br>Major pro<br>consider<br>d instanc<br>ur.|<br>blems this<br>potential<br>es happen|
|[41]|2023|Credit card fraud<br>detection: an<br>improved strategy<br>for high recall|Credit<br>card<br>fraud|KNN,<br>LDA,<br>and<br>regressio|Recall<br>= 1.00|<br>•<br>non-fra|<br>Fraud<br>ud insta|<br>instances are in<br>nces, producing|<br>herently s<br>a highly s|<br>kewed co<br>kewed dis|mpared to<br>tribution.|



VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



• Fraud patterns tends to have more irregular and extreme values, while models like logistics regression or regression assume normality and predictions may produce an inaccurate result. 

### **_III._ PROBLEM DEFINITION** 

This paper considers 𝑋𝑖 = 𝑥1, 𝑥2, … , 𝑥𝑛 as a vector of observation in a respective raw feature. The 𝑋𝑖 is transformed to log return 𝑋𝑝 = 𝑥1, 𝑥2, … , 𝑥𝑚 which is a vector of log returns. The log return 𝑋𝑝 is computed using 𝑙𝑜𝑔(1 + 𝑥𝑥𝑖−1𝑖 ). The log returns are assessed using value-at-risk to determine the risk of fraud for each respective feature. The fraud instances are considered as the worst-case scenario and beyond. The value-at-risk model is the tail of a distribution i.e., extreme quantiles where fraud occurs. The historical simulation was conducted to estimate potential losses distribution ℓ̃𝑝 = ℓ(𝑋𝑝) = −(𝑓(𝑡+ 1, 𝑍𝑡 + 𝑥𝑝 ) −𝑓(𝑡, 𝑍𝑡)). The extreme value theorem is applied to estimate the tail distribution based on fraud instances skewness. The value-atrisk 𝒱 as a risk measure that assesses the risk of the features is the sum of expected loss ℓ and expected shortfall 𝒞, as can be seen in (3). The risk-return features were obtained as log return passes through the formulation comprising ℓ, 𝒱, and 𝒞 as given in (9-12) and the equations are derived based on tree event of fraud instances. The value-at-risk quantified risks across mean, worst-case, and extreme scenarios. This study aims to detect NBA fraud based on risk-return features using the KNN model. 

### **_IV._ MATERIALS AND METHODS** 

This section discusses the materials and methods adopted in this research. 



**_FIGURE 1._ Proposed method** 

### **_A. PROPOSED METHOD_** 

The proposed design of this research is illustrated in **_Error! Reference source not found._** which describes the steps and process involved in NBA fraud detection. Value-at-risk being an important part of this research is designed to model the 

severe and extreme fraud risk features, it also focuses on rare fraud instances that are detrimental and very costly when occurred. However, the rare cases that are mostly skewed can distort machine learning algorithms [51] especially distance based like KNN. The value-at-risk can handle the fraud skewness through the utilization of adjustable threshold probability ranges (confidence level) unlike the conventional methods that employ constant fraud probability weight that’s attached to the skewed fraud instances. The preprocessed, extracted and engineered features were sent as input to valueat-risk for simulation. Meanwhile, a distance based KNN is designed for adjustability to detect fraudulent features through identifying rare clusters with nearest neighbor distance 𝑘. The confidence level chosen considers the rare fraud cases as higher risk features that would result in fewer training sets, particularly for the KNN model with hyperparameter 𝑘. The fraud detection model requires the optimization of  𝑘 to a lower setting to sufficiently model the fraudulent features in the rare cluster. The distance weight of KNN is imperative in inhibiting fraud skewness by assigning a higher weight to near instances which in turn facilitates efficient detection of skewed instances. 

Additionally, this paper put forward a novel approach to NBA fraud detection through the utilization of value-at-risk that appropriately models the fraud skewness. The selection of a 99.5% confidence level highlighted the need to capture 0.5% of extreme fraud risk instances which fit to fall under the subset of 1% fraud rate (detection effectiveness) as shown in **Error! Reference source not found.** . The valueat-risk which is finance and risk management tools model the tails of a fraud event that are extreme. Consequently, a novel detection rate performance metrics that incorporate the risk of skewed fraud instances into the overall performance measure of detecting rare instances were put forward which will later be seen in (21). The metrics provides the model with capacity to identify and attach more weight to rare and extreme fraud instances by including the fraud rate and confidence level in detection process. Therefore, this research put forward a single metrics that capture overall rate of fraud detection based on risk exposure. Under an acceptable loss tolerance in the banking sector, value-at-risk presents an intelligent approach for establishing data-driven criteria for fraud risk management. 



**FIGURE 2. Value-at-risk return curve** 

VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



### **_B. DATA PREPROCESSING_** 

This paper carries out preprocessing tasks to improve the quality of features and ensure model accuracy. The redundant feature 𝑑𝑒𝑣𝑖𝑐𝑒_𝑓𝑟𝑎𝑢𝑑_𝑐𝑜𝑢𝑛𝑡 contains zero instances all of which were manually removed from the data making the model less complex. The categorical features 𝑑𝑒𝑣𝑖𝑐𝑒_𝑜𝑠, 𝑒𝑚𝑝𝑙𝑜𝑦𝑚𝑒𝑛𝑡_𝑠𝑡𝑎𝑡𝑢𝑠, 𝑝𝑎𝑦𝑚𝑒𝑛𝑡_𝑡𝑦𝑝𝑒, and ℎ𝑜𝑢𝑠𝑖𝑛𝑔_𝑠𝑡𝑎𝑡𝑢𝑠 were labeled to make them easier to learn because machine learning cannot process features that are non-numeric. The features 𝑧𝑖𝑝_𝑐𝑜𝑢𝑛𝑡, 𝑘𝑒𝑒𝑝_𝑎𝑙𝑖𝑣𝑒_𝑠𝑒𝑠𝑠𝑖𝑜𝑛 and 𝑏𝑎𝑛𝑘_𝑚𝑜𝑛𝑡ℎ𝑠_𝑐𝑜𝑢𝑛𝑡 were eliminated to avoid noise and collinearity issues. The features 𝑓𝑜𝑟𝑒𝑖𝑔𝑛_𝑟𝑒𝑞𝑢𝑒𝑠𝑡, ℎ𝑎𝑠_𝑜𝑡ℎ𝑒𝑟_𝑐𝑎𝑟𝑑, and 𝑒𝑚𝑎𝑖𝑙_𝑖𝑠_𝑓𝑟𝑒𝑒 were eliminated as they give too much undefined log returns. 

### **_C. FEATURE EXTRACTION AND ENGINEERING_** 

The development of a NBA fraud detection model was based on the selection of relevant features from demographic, behavioral, risk management and transactional perspective. Demographic features such as 𝑖𝑛𝑐𝑜𝑚𝑒, 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟_𝑎𝑔𝑒, and 𝑒𝑚𝑝𝑙𝑜𝑦𝑚𝑒𝑛𝑡_𝑠𝑡𝑎𝑡𝑢𝑠 were selected. Behavioral features such as 𝑏𝑎𝑛𝑘_𝑏𝑟𝑎𝑛𝑐ℎ_𝑐𝑜𝑢𝑛𝑡_8𝑤 and ℎ𝑜𝑢𝑠𝑖𝑛𝑔_𝑠𝑡𝑎𝑡𝑢𝑠were selected. Risk-based features that include 𝑐𝑟𝑒𝑑𝑖𝑡_𝑟𝑖𝑠𝑘_𝑠𝑐𝑜𝑟𝑒 and 𝑝𝑟𝑜𝑝𝑜𝑠𝑒𝑑_𝑐𝑟𝑒𝑑𝑖𝑡_𝑙𝑖𝑚𝑖𝑡 were selected. Transactional features such as 𝑑𝑎𝑦𝑠_𝑠𝑖𝑛𝑐𝑒_𝑟𝑒𝑞𝑢𝑒𝑠𝑡, 𝑡𝑜𝑡𝑎𝑙_𝑣𝑒𝑙𝑜𝑐𝑖𝑡𝑦, and 𝑝𝑎𝑦𝑚𝑒𝑛𝑡_𝑡𝑦𝑝𝑒 were also selected. Additionally, two or more existing features are combined to form a new feature as given in Table 2. The features engineered are based on location, velocity of transactions, default risk, and ability to repay loans to determine the likelihood of fraudulent behaviors. The selected features were used along with the other raw features for accurate model training. 

|||TABL<br>TABLE OF NE<br>|E2<br>W FEATURES<br>|
|---|---|---|---|
|**S/N**|**Description**|**New**<br>**feature**|**Formulation**|
|1|Total<br>duration in a<br>location|𝑡𝑜𝑡𝑎𝑙_𝑑𝑢𝑟|=<br>𝑝𝑟𝑒𝑣_𝑎𝑑𝑑𝑟𝑒𝑠𝑠_𝑚𝑜𝑛𝑡ℎ𝑠_𝑐𝑜𝑢𝑛𝑡 +<br>𝑐𝑢𝑟𝑟𝑒𝑛𝑡_𝑎𝑑𝑑𝑟𝑒𝑠𝑠_𝑚𝑜𝑛𝑡ℎ𝑠_𝑐𝑜𝑢𝑛𝑡|
|2|Total<br>velocity|𝑡𝑜𝑡𝑎𝑙_𝑣𝑒𝑙|= 𝑣𝑒𝑙𝑜𝑐𝑖𝑡𝑦_6ℎ + 𝑣𝑒𝑙𝑜𝑐𝑖𝑡𝑦_24ℎ<br>+ 𝑣𝑒𝑙𝑜𝑐𝑖𝑡𝑦_4𝑤|
|3|Phone<br>consistency|𝑝ℎ𝑜𝑛𝑒_𝑐𝑜𝑛|= 𝑝ℎ𝑜𝑛𝑒_ℎ𝑜𝑚𝑒_𝑣𝑎𝑙𝑖𝑑<br>+ 𝑝ℎ𝑜𝑛𝑒_𝑚𝑜𝑏𝑖𝑙𝑒_𝑣𝑎𝑙𝑖𝑑|
|4|Credit risk<br>score|𝑐𝑟𝑒𝑑𝑖𝑡_𝑟𝑎𝑡𝑖𝑜|=𝑖𝑛𝑡𝑒𝑛𝑑𝑒𝑑_𝑏𝑎𝑙𝑐𝑜𝑛_𝑎𝑚𝑜𝑢𝑛𝑡/<br>𝑝𝑟𝑜𝑝𝑜𝑠𝑒𝑑_𝑐𝑟𝑒𝑑𝑖𝑡_𝑙𝑖𝑚𝑖𝑡|
|5|Credit<br>capacity|𝑐𝑟𝑒𝑑𝑖𝑡_𝑐𝑎𝑝|= 𝑖𝑛𝑐𝑜𝑚𝑒<br>/ 𝑝𝑟𝑜𝑝𝑜𝑠𝑒𝑑_𝑐𝑟𝑒𝑑𝑖𝑡_𝑙𝑖𝑚𝑖𝑡|
|6|Credit<br>utilization|𝑐𝑟𝑒𝑑𝑖𝑡_𝑢𝑡|=𝑖𝑛𝑡𝑒𝑛𝑑𝑒𝑑_𝑏𝑎𝑙𝑐𝑜𝑛_𝑎𝑚𝑜𝑢𝑛𝑡/<br>𝑐𝑟𝑒𝑑𝑖𝑡_𝑟𝑖𝑠𝑘_𝑠𝑐𝑜𝑟𝑒|
|7|Transaction<br>intensity|𝑡𝑟𝑎𝑛𝑠_𝑖𝑛𝑡|=𝑡𝑜𝑡𝑎𝑙_𝑣𝑒𝑙 ×<br>𝑠𝑒𝑠𝑠𝑖𝑜𝑛_𝑙𝑒𝑛𝑔𝑡ℎ_𝑖𝑛_𝑚𝑖𝑛𝑢𝑡𝑒𝑠|



### **_D. VALUE-AT-RISK_** 𝓥 

Because of the value-at-risk emphasis on statistically extreme but significant fraud instances, it is ideally more suitable for the development of efficient fraud detection models. In the financial sector, value-at-risk is a quantile of loss distribution that gives a range of potential losses and is one of the most 

frequently used measures of risk. 𝒱 can also be termed as a statistical measure of the risk of loss over a specific time at a given confidence level. It also plays a significant part in the Basel regulatory framework. 𝒱 has a confidence level 𝛼∈ (0,1)[48]. This experiment adopted the Solvency II framework which uses a one-year horizon with the level of confidence, α equal to 0.995. It can be written as in (1): 



Where 𝜇 is the mean of a log loss returns and 𝜎 is the standard deviation of returns, 𝑍 represents the standard normal, and 𝑍<sup>−1</sup> (𝛼) represent the ∝ quantile of 𝑍.  The value-at-risk[49] can also be written as in (2): 

𝑉𝑎𝑙𝑢𝑒−𝑎𝑡−𝑟𝑖𝑠𝑘 = 𝐸𝑥𝑝𝑒𝑐𝑡𝑒𝑑 𝑙𝑜𝑠𝑠 + 𝑈𝑛𝑒𝑥𝑝𝑒𝑐𝑡𝑒𝑑 𝑙𝑜𝑠𝑠 _(2)_ 

In this paper, we consider the unexpected loss to be the expected shortfall. Therefore, the general relationship will be written as given in (3): 



Generally, expected loss alone does not sufficiently handle the tail risk of losses, applying 𝒱 additionally quantifies the aggregate potential losses of fraud risk features. The addition of 𝒞 will further quantify the extreme loss effects. This combination will allow quantification of risk across mean, worst-case, and extreme scenarios. The metrics will aggregate their strengths and overcome their weakness. 

1) EXPECTED LOSS ℓ 

Expected loss is an important risk measure for estimating the average or probable loss expected from a specific risk exposure. Intuitively, it indicates loss occurrence on average in a repeated situation. ℓ is measured usually based on 1 year, the higher value of ℓ indicates a high risk of exposure. ℓ does not sufficiently handle tail risks as it is considered more of an average risk measure, due to this limitation, there is a need for support by other risk measures like 𝒱 and 𝒞. The expected losses can be written mathematically in (4): 



The 𝑋𝑝 is a log return which was computed using the formula (5). The addition of 1 is to avoid having too much negative and undefined log returns. 



2) EXPECTED SHORTFALL 𝒞 

In other words, 𝒞 is a conditional value-at-risk given that the loss ℓ exceeds the 𝒱 threshold at the specified confidence level 𝛼. The 𝒞  as given in (6,7) represents the level for the worst 100(1 −𝛼)% losses in the distribution. It focuses on the severity of the rare worst-case losses ignored by 𝒱. 



VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 





However, the 𝒱 can be computationally expensive and difficult to apply to complex financial portfolios. It does not also give information on the severity of loss. To augment such weakness of 𝒱, expected shortfall 𝒞 were employed to estimate the severity of losses in the worst cases. Historical simulation is adopted to estimate the losses of fraud risk features. 

## 3) HISTORICAL SIMULATION 

This is a non-parametric technique that uses past information to model possible loss in the future[50]. This utilizes empirical distribution to estimate the loss distribution of previous changes in risk features. The advantage of historical simulation over covariance method of loss estimation is its ability to adapt over time and can model dynamic conditions. The loss distribution ℓ̃𝑝 measure the change in value between the returns 𝑓(𝑡, 𝑍𝑡)  at time 𝑡 and returns 𝑓(𝑡+ 1, 𝑍𝑡 + 𝑥𝑝) at time 𝑡+ 1 in a specific confidence level, the negative value is indicating the interest in quantification of loss given in (8), 𝑍𝑡 denotes condition of returns at time t. 



### 4) TREE EVENT OUTCOME 

Even tree is employed in risk assessment and analysis to pinpoint different event sequences for both fraud and nonfraud that may result in a particular outcome. An event tree also known as an incidence response tree (IRT)[49] contains four possible outcomes as given (9-12) that are based on prevention, detection, and response. The event tree significantly tracks fraudulent activities and estimates the return outcomes of monitoring decisions, hence improving prediction and risk models. The formulation of this paper is based on Dan Gorton[49]: Fraud without detection, fraud despite detection, fraud detected and stopped, and high-risk fraud stopped. The detection effectiveness 𝛾  is the fraud rate: 

1. Fraud without detection: 𝛾 is not regarded as fraud goes undetected as in (9). The worst-case scenario 𝒱 of losses when fraud stays undetected is understood by using the ℓ which is the mean of returns 𝜇.  𝒞 aids in evaluating the tail risk related to undetected fraud. 

𝑄𝑢𝑎𝑛𝑡𝑖𝑙𝑒(𝜇, 99.5%) = ℓ+ 𝐴𝑣𝑒𝑟𝑎𝑔𝑒(𝑋𝑝 | 𝑋𝑝 > 𝒱) _(9)_ 

Where ℓ = 𝜇, 𝒱 = 𝑄𝑢𝑎𝑛𝑡𝑖𝑙𝑒(𝜇, 99.5%), and 𝒞 = 𝐴𝑣𝑒𝑟𝑎𝑔𝑒(𝑋𝑝 | 𝑋𝑝 > 𝒱) 2. Fraud despite detection:  When fraud occurs with (1 - γ) detection, there is a reduction in ℓ and 𝒱 in proportion to 𝛾, while 𝒞  remains the same as given in (10). 



Where ℓ = 𝜇 × (1 – 𝛾), 𝒱 = 𝑄𝑢𝑎𝑛𝑡𝑖𝑙𝑒(𝜇, 99.5%) × (1 – 𝛾), and 𝒞 = 𝐴𝑣𝑒𝑟𝑎𝑔𝑒(𝑋𝑝 | 𝑋𝑝 > 𝒱) 

3. Fraud detected and stopped: This stops detection before major damage as shown in (11). Fraud is detected by γ and ℓ are restricted to the expenses related to prevention and detection, both 𝒱 and ℓ are proportional to γ, while 𝒞 remains the same. 



Where ℓ = 𝜇× 𝛾, 𝒱 = 𝑄𝑢𝑎𝑛𝑡𝑖𝑙𝑒(𝜇, 99.5%) × 𝛾, and 𝒞 = 𝐴𝑣𝑒𝑟𝑎𝑔𝑒(𝑋𝑝| 𝑋𝑝 > 𝒱) 

4. High-risk fraud stopped: This refers to fraud that is avoided because of potential risk exposure as given in (12). The ℓ is the associated cost of prevention and detection of high-risk fraud, it is assumed that the associated costs are relatively lower than the mean loss. 𝒱 is the 99.5 percentile of loss returns, 𝒞 quantifies average loss beyond 𝒱. 



Where ℓ = 𝜇(1 −𝛼), 𝒱 = 𝑄𝑢𝑎𝑛𝑡𝑖𝑙𝑒 (𝛾, 99.5%) , and 𝒞 = 𝐴𝑣𝑒𝑟𝑎𝑔𝑒(𝑋𝑝 | 𝑋𝑝 > 𝒱) 

In each of the four scenarios, these risk measures have distinct and significant roles played in managing the costs and risks related to fraud detection and prevention strategies. 

### **_E. NBA FRAUD DETECTION MODEL SELECTION_** 

Machine learning models can utilize high dimensional data to analyze complex fraud patterns that humans or rule-based systems would not. Supervised ML has unique significance in employing labeled data to find the patterns, anomalies, and fraudulent activity. Binary logistic regression (BLR) is suitable in handling categorical data and is good due its interpretability. Naïve bayes (NB) has efficiency and simplicity in terms of cost and time. K-nearest neighbor (KNN) has high effectiveness in fraud detection when managing transactional information, adaptability, and as well as its potential use in hybrid form. 

### 1) BINARY LOGISTIC REGRESSION 

BLR is a supervised ML [50] that is very effective in fraud detection capability due to its suitability in handling categorical data and its interpretability[51]. The solution for the fraud detection model is constructed by utilizing the binary fraud class 𝑦 and features 𝑋𝑖[52]. 𝑋𝑖 is a vector of features (𝑥1,𝑥2, … , 𝑥𝑛) capable of influencing the decision of fraud detection model to classify features as either fraud or non-fraud class 𝑦∈(0,1). BLR function uses the sigmoid function on  𝑦∈(0,1). The mathematical expression is given in (13,14): 





Based on the Bayes theorem, the Naive Bayes is a supervised machine learning algorithm[53]. The NB is very suitable in 

VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



fraud detection for its efficiency in terms of cost, time, and high accuracy[54]. When given the fraud class, the NB classifier assumes that all fraudulent features are independent of each other. Assume the target feature tobe 𝑌𝑗 ∈(0,1) and that 𝑋𝑖 is a vector of fraudulent features. The 𝑃(𝑌𝑗/𝑋𝑖) is the generic conditional probability 𝑋𝑖 given 𝑌𝑗. The Gaussian function of NB is given in (15), where 𝜎<sup>2</sup> and <u>𝑥 are the</u> variance and mean of probabilities. 



3) K-NEAREST NEIGHBOR 

KNN is a supervised machine learning algorithm that is useful for problem classification[55] and is good for its better detection and lower FP rate. KNN has high effectiveness in fraud detection when managing transactional information, adaptability, and as well as its potential use in hybrid form[56]. To determine whether there has been fraudulent behavior in fraudulent features 𝑋𝑖, studies employ KNN to classify 𝑋𝑖 into fraud class 𝑌𝑗 ∈(0,1). Two estimates are needed for the KNN fraud detection technique: The transaction correlation and the distance between the transaction’s occurrence of the fraud features. The indicator function is given in (16): 



### **V. EXPERIMENTAL SETUP** 

The simulation of value-at-risk was conducted in a Microsoft Excel environment, and the development of fraud detection models was conducted using Python. Experimental procedures that are carried out for developing a fraud detection model. 

### **_A. DATASET_** 

A real-world BAF dataset is accessible to the public[18]. It contains 32 features with 1 million instances. The dataset contains details about the demographic, behavioral, risk, and transactional features. The dataset is highly skewed with a fraud class of 11029 and a non-fraud class of 988971 as shown in **Error! Reference source not found.** . The primary obstacle to the detection of NBA fraud is the scarcity of datasets. The BAF dataset remain the only data in this domain. As such, the evaluation of this research paper is forced to rely on the BAF dataset. 



**FIGURE 3. Fraud class distribution** 

### **_B. PERFORMANCE METRICS_** 

The confusion matrix is used to evaluate the performance of a classification model and contains the values of true positive (TP), false positive (FP), true negative (TN), and false negative (FN)[52]. The majority of studies in the literature utilize the true positive (TP) rate, to give room for comparison, evaluation metrics such as accuracy, f-score, TP rate, and FP rate.  A novel detection rate was additionally proposed that integrate the overall detection performance with associated risk exposure. The Accuracy measures the overall performance of the model, F-score integrates precision (1-FP rate) and recall (TP rate) in a skewed dataset that struggles to balance between minimizing FN and FP. The TP rate measure the proportion of correct detection performance. The FP rate measure the proportion of incorrect detection.  The metrics are given mathematically in (17-20). 



The novel detection rate measures the overall rate of detection that incorporate the risk of detecting extreme instances. The 𝛾 denotes the fraud rate and 𝛼 denotes the <u>(1+𝛾 (1−𝛼))</u> confidence level as given in (21). The component (1+𝛾) is proportional to the proportion of extreme fraud instances exceeding 𝛼 _._ It has the advantage of integrating the capacity to detect rare but extremely significant fraud cases with the overall detection performance. The detection rate ranges from 0 to 1. 



### **_C. NBA FRAUD DETECTION MODEL DEVELOPMENT_** 

This section discusses the procedure for the development of NBA fraud detection model using raw features. Raw features 

VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



refer to the features in the initial stage that went through preprocessing, feature extraction, and engineering steps before transformation to either logarithmic or risk-return features. The datasets contain different format types and features in number type were converted to integers for simplicity and efficiency in processing the fraud detection model. Features that cause noise and collinearity were removed from the datasets to increase the performance of the model. Relevant features that facilitate accuracy were selected from demographic, behavioral, transactional, and risk perspectives. New features are engineered based on location, the velocity of transactions, default risk, and ability to repay loans to determine the risk of fraudulent behaviors. The processed features and newly engineered features were used to form the set of raw features and is highly skewed. The raw features were sent as input to the machine learning models to classify features as either fraud or non-fraud. BLR, KNN, and NB models are employed to build a fraud detection model. 

**_D. EXECUTIONN OF THE PROPOSED APPROACH_** The NBA fraud detection model presented in section C is achieved through the utilization of raw features. The raw features undergo preprocessing and feature selection. The engineered features along with other features were sent for training using different machine learning models. However, the results obtained are not very good for NBA fraud detection. Hence, the poor performance of raw features which is attributed to skewed data distribution highlighted the need for model improvement. The raw features were modeled by value-at-risk for improvement. Initially, raw features were transformed into a log return, the log returns were then passed through (3) of value-at-risk 𝒱. The riskreturn features were obtained from 𝒱, ℓ  and 𝒞 as seen in (912). The risk-return features were then subjected to classification by machine learning models. Machine learning models such as BLR, NB, and KNN were employed to develop the NBA fraud detection model. BLR is essentially a probability prediction model that needs to be turned into binary values. The maximum likelihood estimate is used to estimate the weights of BLR. A real-valued set of risk-return features is mapped into a binary class of fraud and non-fraud using the sigmoid function. A model that predicts a value very close to 1 is produced by using the best weights. Using the risk-return features in Naïve bayes, the conditional probability of fraud feature and the prior probability of fraud class are computed. To predict the fraud class based on new features, the posterior probability of the fraud class is obtained by combining the learning of probability distributions with Bayes' rule. The K-NN algorithm detects the K nearest neighbors, using a distance metric, to a given data point. The majority vote of the K neighbors is then used to establish the fraud class. Using this method enables the algorithm to classify outcomes based on the local structure of the data and adjust to various patterns. 

### **VI. RESULTS ANALYSIS & DISCUSSION** 

This section presents the general results obtained from experimental research with skewed fraud instances and riskreturn features with their validation. The 10-fold cross validation was used to evaluate NBA fraud detection models. 

### **_A. RESULT OF NBA FRAUD DETECTION MODEL WITH SKEWED FRAUD INSTANCES_** 

This section presents the result of the NBA fraud detection model with skewed instances using BLR, KNN, and NB. The results are presented in **Error! Reference source not found.** , the best metric results among the models were written in bold number. The accuracy result of BLR, KNN, and NB are 0.9869, 0.9884, and 0.9743 respectively. The TP rate results of BLR, KNN, and NB are 0.0016, 0.0061, and 0.1355 respectively. The FP rate results of BLR, KNN, and NB are 0.002, 0.0007, and 0.0163 respectively. The f-score results of BLR, KNN, and NB are 0.0028, 0.0115, and 0.1042 respectively. The illustrations of the metric results are demonstrated in **Error! Reference source not found.** . It can be observed that the results of accuracy and FP rate were good. However, the results of the TP rate and f-score were not very good. The TP rate is a very important metric especially in fraud detection, robust and accurate fraud detection must attain a good TP rate. The poor performance of the fraud detection model, particularly in TP rate and f- score, using fraud skewed instances highlighted the need for model improvement. We employ to improve the fraud detection model using value-at-risk augmented features which is presented in section B. 



**FIGURE 4. Performance evaluation of fraud detection model with skewed features** 

TABLE 3 

|RESULT O<br>**Metrics**|F FRAUD DETECT<br>**BLR**|ION MODEL WITH RAW FEATURES<br>**KNN**<br>**NB**|
|---|---|---|
|**Accuracy**|0.9869|**0.9884**<br>0.9743|
|**TP rate**|0.0016|0.0061<br>**0.1355**|
|**FP rate**|0.0020|**0.0007**<br>0.0163|
|**F-score**|0.0028|0.0115<br>**0.1042**|



VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



### **_B. RESULT OF AN IMPROVED NBA FRAUD DETECTION MODEL USING VALUE-AT-RISK_** 

This section presents the results of an improved NBA fraud detection model using BLR, KNN, and NB. The result indicated good performance by KNN and the results are written in bold number as shown in **Error! Reference source not found.** . The accuracy results of BLR, KNN, and NB are 0.8, 0.9167, and 0.8667 respectively. The TP rate results of BLR, KNN, and NB are 0.75, 0.95, and 0.875 respectively. The detection (DT) rate results of BLR, KNN, and NB are 0.7426, 0.9406, and 0.8580 respectively. The f- score results of BLR, KNN, and NB are 0.7333, 0.9333, and 0.8333 respectively. The illustrations of the metric results are demonstrated in **Error! Reference source not found.** . The results show that KNN has better performance in accuracy, TP rate, DT rate, and f-score. Overall, it can be concluded that the KNN model outperforms other models to emerge as the best NBA fraud detection model. 

TABLE 4 

|RESULT OF AN IMPROVED FR<br>**Metrics**<br>**BLR**|AUD DETECTION<br>**KNN**|MODEL<br>**NB**|
|---|---|---|
|**Accuracy**<br>0.8000|**0.9167**|0.8667|
|**TP rate**<br>0.7500|**0.9500**|0.8750|
|**DT rate**<br>0.7426|**0.9406**|0.8580|
|**F- score**<br>0.7333|**0.9333**|0.8333|





**FIGURE 5. Performance evaluation of risk-return features** 

The Receiver operating curve (ROC) in **Error! Reference source not found.** presents the classification capability, it indicates a high TP rate and low FP rate across different threshold values. The KNN model demonstrates high robustness in fraud detection as compared to BLR and NB. 

The risk-return features were reduced using principal component analysis to map the KNN decision boundary. The principal components (PC) were utilized to plot the KNN decision boundary. **Error! Reference source not found.** indicates that the KNN model identifies the fraud risk patterns based on its exhibited linear boundary which translates to a relatively simple relationship among fraud risk 

features. Also, the dominance of one class in a particular region may signal a distinct fraudulent feature through smaller 𝑘= 3 which successfully reduce the influence of skewed instances which is manifested by a high TP rate. 



**_FIGURE 6._ Receiver operating curve for the fraud models** 



**FIGURE 7. Decision boundary for KNN** 

### **_C. RELIABILITY ANALYSIS_** 

The reliability analysis of the value-at-risk-based fraud detection model is done using the Kupiec test. Kupiec proposed an additional failure rate-based test in 1995[57]. The test measures the frequency with which a value-at-risk is violated over a specified period. The test null hypothesis is when the expected violation rate by the value-at-risk model and the observed violation rate are equal and is given in (22) as ℎ. The test statistic follows chi-square with 1 degree of freedom is given in  (23) as the likelihood ratio (LR): 



The result for the test at a 5% significance level is given in **Error! Reference source not found.** . It can be seen that only 𝑛𝑎𝑚𝑒_𝑒𝑚𝑎𝑖𝑙_𝑠𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 and 𝑑𝑎𝑦𝑠_𝑠𝑖𝑛𝑐𝑒_𝑟𝑒𝑞𝑢𝑒𝑠𝑡 were found not to be consistent the observed violation rate. The rest of the features were found to be consistent and reliable. Hence, the incorporation of value-at-risk were adequate and reliable. 

VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 





**FIGURE 8. Reliability analysis** 

### **_D. COMPARISON WITH THE STATE-OF-THE-ART METHODS IN NBA FRAUD DETECTION_** 

The results of our experiment are compared with the state-ofthe-art methods for NBA fraud. The study[18] used 100 sets of hyperparameters for parameter configuration to optimize the LGBM model performance and obtained a TP rate result of about 0.6, under-sampling techniques for handling class skewness were used as part of hyperparameters. The study[19] utilizes 25 sets of hyperparameter configurations to optimize the LGBM model and obtained a TP rate result of almost 0.8, utility aware reweighing is used to handle the class skewness. Additionally, the study[15] uses ensemble learning techniques in which stacking was specifically applied to handle class skewness, the strengths of the weaker models trained were aggregated using majority voting to address evolving patterns and achieved a 0.9 TP rate result. Another study[20] combined federated learning to handle data privacy and SHAP value to ensure interpretability of feature importance by human experts, the deep neural network was used to recognize patterns of fraud, and a TP rate of about 0.75 was achieved, SMOTE  were employed to handle class skewness. Our paper uses KNN with k hyperparameter to detect fraud with a TP rate of 0.95. We overcome fraud skewness using value-at-risk that considers fraud instances as a worst-case scenario through the utilization of adjustable threshold probability ranges weight that’s attached to the skewed fraud instances. The results for comparison are given in Table _5_ . Also, while our paper reached an accuracy of 0.9167, another study[58] employed the BAF in evaluation with 0.677 of an accuracy. Our approach was particularly better than the methods that are currently in existence. 

TABLE 5 

|COMPARISON WITH THE STATE-OF-THE-ART METHODS<br> <br>|
|---|
|**Methods**<br>**TP rate**|
|LGBM[18]<br>0.6000|
|LGBM[19]<br>0.8000|
|Ensemble Learning[15]<br>0.9000|
|DNN[20]<br>0.7500|
|Our Proposedmethod<br>**0.9500**|



### **_E. ABLATION STUDY_** 

This paper conducted an ablation study to determine the contribution of components that influence the performance of the NBA fraud detection model. The choice of logarithmic return is among the components that impacted our result. Given log return 𝑋𝑝 = 𝑙𝑜𝑔(1 + 𝑥𝑥𝑖−1𝑖 ~~)~~ , 1 is removed from log return formulae to become 𝑋𝑝 = 𝑙𝑜𝑔(𝑥𝑥𝑖−1𝑖 ~~)~~ . The result which can be seen in 

Table 6 shows F-score of new bank account fraud detection models. The removal of 1 resulted in decreased performance for BLR, KNN, and NB. 

|ABL<br>**Log return**|TABLE6<br>ATION STUDY USI<br>BLR|NGF-SCORE<br>KNN|NB|
|---|---|---|---|
|𝒍𝒐𝒈(𝟏+ <sup>𝒙𝒊</sup><br>𝒙𝒊−𝟏<br>~~)~~|**0.7333**|**0.9333**|**0.7667**|
|𝒍𝒐𝒈( <sup>𝒙𝒊</sup><br>𝒙𝒊−𝟏<br>~~)~~|0.7273|0.7000|0.6667|



### **_F. PARAMETER ANALYSIS_** 

This paper examines hyperparameter space to determine the setup that led to optimum model efficiency and performance. The experiment utilizes different parameter ranges in BLR, KNN, and NB. For BLR, learning rate 𝑙𝑟 are examined, and the accuracy results of different parameter configurations are shown in Table _7_ . For KNN, the number of nearest neighbors 𝑘 are evaluated and the accuracy results of parameter settings are shown in Table _8_ . For NB, the different probability distributions were evaluated and the accuracy results as given in Table _9_ . 

|PARAM<br>|ETER ANAL<br>|TA<br>YSIS INVOL<br>|BLE7<br>VING LEAR<br>|NING RATE𝑙𝑟OFBLR<br><br>|
|---|---|---|---|---|
|**Learning**<br>**rate (**𝒍𝒓)|0.01|0.02|0.03|0.055<br>0.09|
|**Accuracy**<br>PARAMETER|0.8000<br>ANALYSIS|0.8000<br>TA<br>INVOLVING<br>OF|0.8000<br>BLE8<br>A NUMBER<br> KNN|0.8333<br>0.8333<br>OF NEAREST NEIGHBORS𝑘|
|**Nearest**<br>**neighbors**<br> (𝒌)|1|2|3|4<br>5<br>6|
|**Accuracy**|0.900<br>0|0.816<br>7|0.916<br>7|0.833<br>3<br>0.866<br>7<br>0.833<br>3|
|PARAMETER<br>|ANALYSIS<br> <br>|TA<br>INVOLVING<br>|BLE9<br>A DISTRIB<br>|UTION ASSUMPTION OFNB<br> <br>|
|**Distributio**|**n**<br>|Gaussian|Mult|inomial<br>Binary|
|**Accuracy**||0.8333|0.|8666<br>0.4500|



### **VII. DISCUSSIONS AND CONCLUSION** 

This section presents a discussion of the results and the conclusion of our findings. 

### **_A. DISCUSSIONS_** 

This paper explored improving the performance of NBA fraud detection model by employing value-at-risk. The performance of the fraud detection models was measured based on the removal of redundant features to lower the 

VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



complexity of the model, the selection of an important feature capable of influencing fraud detection to avoid noise and collinearity, and the engineering of features from the contextual perspective that increase the model performance. The raw features were sent to BLR, KNN, and NB models for classification. KNN model outperforms other models as shown in **Error! Reference source not found.** with an accuracy result of 0.9884, TP rate result of 0.0061, FP rate result of 0.0007, and f-score result of 0.0115. The performance of fraud detection is not very good and reliable as evidenced by the TP rate and f-score, hence, necessitating the need for the model improvement. Given that, value-atrisk was employed to improve the model. To improve NBA fraud detection model, raw features were simulated through value-at-risk. The risk-return features obtained from value-atrisk were sent to BLR, KNN, and NB models for classification. Among the models, the KNN model performs better as shown in **Error! Reference source not found.** with an f-score result of 0.9333, TP rate result of 0.95, accuracy result of 0.9167, and DT rate result of 0.9406. The NBA fraud detection model based on value-at-risk features appears to have good performance. The reliability test conducted using the Kupiec test proved to be reliable and consistent as shown in **Error! Reference source not found.** . This indicates that the value-at-risk engineered features led to the improvement of K-nearest neighbor fraud detection model. 

### **_B. CONCLUSION_** 

The value-at-risk-based fraud detection model presented in this paper enables the quantification and mitigation of fraud risk features and at the same time overcome the influence of skewed fraud instances which is very crucial in solving financial fraud challenges. The value-at-risk attach confidence probability weight to the rare fraud cases with nearest neighbor distance 𝑘. The distance weight of KNN is imperative in inhibiting class skewness by assigning a higher weight to near instances which in turn facilitates efficient detection of skewed instances. The deployment of expected shortfall and expected loss by value at risk allows quantification of risk across mean, worst-case, and extreme scenarios enabling aggregation of their strengths. Therefore, an accurate fraud detection system assists organizations in making effective choices and reducing the overall expense of fraud detection and prevention. This paper does not consider the time windows in the experiment. However, the major challenge is the lack of data availability in NBA fraud detection. 

### **CONFLICT OF INTEREST** 

There are no competing interests disclosed by the authors. 

### **ACKNOWLEDGMENT** 

The authors are also thankful to AIDA Lab CCIS Prince Sultan University, Riyadh Saudi Arabia for support of APC. 

The authors are grateful to the School of Statistics & Mathematics, Zhejiang Gongshang University, China. 

## **AVAILABILITY OF DATA AND MATERIALS** 

The data used in this research is publicly available at https://github.com/feedzai/bank-account-fraud 

### **REFERENCES** 

- [1] ACFE, “Association of Certified Fraud Examiners (ACFE) 2022 Report to the nations.” [Online]. Available: https://legacy.acfe.com/report-to-the-nations/2022/ 

- [2] Ashfaq, T., Khalid, R., Yahaya, A. S., Aslam, S., Azar, A. T., Alsafari, S., & Hameed, I. A. (2022). A machine learning and blockchain based efficient fraud detection mechanism. Sensors, 22(19), 7162. 

- [3] Alfaiz, N. S., & Fati, S. M. (2022). Enhanced credit card fraud detection model using machine learning. Electronics, 11(4), 662. 

- [4] Alfaadhel, A., Almomani, I., & Ahmed, M. (2023). Risk-Based Cybersecurity Compliance Assessment System (RC2AS). Applied Sciences, 13(10), 6145. 

- [5] D. Sarma, W. Alam, I. Saha, M. N. Alam, M. J. Alam, and S. Hossain, “Bank fraud detection using community detection algorithm,” in _2020 second international conference on inventive research in computing applications (ICIRCA)_ , IEEE, 2020, pp. 642– 646. 

- [6] A. Pagano, “Digital account opening fraud on demand deposit accounts: An assessment of available technology,” PhD Thesis, Utica College, 2020. 

- [7] Shuftipro, “New account fraud - A new breed of scams.” [Online]. Available: https://shuftipro.com/reports-whitepapers/new-accountfraud.pdf 

- [8] R. Sasirekha, B. Kanisha, and S. Kaliraj, “Study on class imbalance problem with modified KNN for classification,” _Intelligent data communication technologies and internet of things_ , vol. 101, pp. 207–217, 2022, doi: https://doi.org/10.1007/978-981-16-7610-9_15. 

- [9] P. Vanini, S. Rossi, E. Zvizdic, and T. Domenig, “Online payment fraud: from anomaly detection to risk management,” _Financ Innov_ , vol. 9, no. 1, p. 66, Mar. 2023, doi: 10.1186/s40854-023-00470-w. 

- [10] X. Zhu _et al._ , “Intelligent financial fraud detection practices in postpandemic era,” _Innovation (Camb)_ , vol. 2, no. 4, p. 100176, 2021, doi: 10.1016/j.xinn.2021.100176. 

- [11] [M. Monge, C. Poza, and S. Borgia, “A proposal of a suspicion of tax fraud indicator based on Google trends to foresee Spanish tax revenues,” _International Economics_ , vol. 169, pp. 1–12, May 2022, doi: 10.1016/j.inteco.2021.11.002. 

- [12] K. S. and S. K., “Autoregressive-based outlier algorithm to detect money laundering activities,” _JMLC_ , vol. 20, no. 2, pp. 190–202, May 2017, doi: 10.1108/JMLC-07-2016-0031. 

- [13] B. Xiao, B. Lei, W. Lan, and B. Guo, “A blockwise network autoregressive model with application for fraud detection,” _Ann Inst Stat Math_ , vol. 74, no. 6, pp. 1043–1065, Dec. 2022, doi: 10.1007/s10463-022-00822-w. 

- [14] G. Moschini, R. Houssou, J. Bovay, and S. Robert-Nicoud, “Anomaly and fraud detection in credit card transactions using the ARIMA model,” in _The 7th International conference on Time Series and Forecasting_ , MDPI, Jul. 2021, p. 56. doi: 10.3390/engproc2021005056. 

- [15] A. A. Alhashmi, A. M. Alashjaee, A. A. Darem, A. F. Alanazi, and R. Effghi, “An ensemble-based fraud detection model for financial transaction cyber threat classification and countermeasures,” _Eng. Technol. Appl. Sci. Res._ , vol. 13, no. 6, pp. 12433–12439, Dec. 2023, doi: 10.48084/etasr.6401. 

- [16] R. M. Aziz, R. Mahto, K. Goel, A. Das, P. Kumar, and A. Saxena,, “modified genetic algorithm with deep learning for fraud transactions of ethereum smart contract,” _Applied Sciences_ , vol. 13, no. 2, p. 697, Jan. 2023, doi: 10.3390/app13020697. 

VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



- [17] M. Hegazy, A. Madian, and M. Ragaie, “Enhanced fraud miner: Credit card fraud detection using clustering data mining techniques,” _Egyptian Computer Science Journal_ , vol. 40, no. 03, 2016. 

- [18] S. Jesus _et al._ , “Turning the tables: Biased, imbalanced, dynamic tabular datasets for ml evaluation,” _Advances in Neural Information Processing Systems_ , vol. 35, pp. 33563–33575, 2022. 

- [19] J. Pombal, P. Saleiro, M. A. T. Figueiredo, and P. Bizarro, “Fairnessaware data valuation for supervised learning.” [Online]. Available: http://arxiv.org/abs/2303.16963. 

- [20] T. Awosika, R. M. Shukla, and B. Pranggono, “Transparency and privacy: The role of explainable ai and federated learning in financial fraud detection.” [Online]. Available: http://arxiv.org/abs/2312.13334 

- [21] J. Khaksar, M. Salehi, and M. Lari DashtBayaz, “The relationship between auditor characteristics and fraud detection,” _Journal of Facilities Management_ , vol. 20, no. 1, pp. 79–101, 2022, doi: 10.1108/JFM-02-2021-0024. 

- [22] A. Cordis, “Political alignment and corporate fraud: Evidence from the United States of America,” _JAAR_ , Oct. 2023, doi: 10.1108/JAAR-06-2022-0159. 

- [23] M. J. Rahman and X. Jie, “Fraud detection using fraud triangle theory: Evidence from China,” _Journal of Financial Crime_ , vol. 31, no. 1, pp. 101–118, 2024, doi: 10.1108/JFC-09-2022-0219. 

- [24] T. Achmad, I. Ghozali, and I. D. Pamungkas, “Hexagon fraud: Detection of fraudulent financial reporting in state-owned enterprises Indonesia,” _Economies_ , vol. 10, no. 1, p. 13, 2022. 

- [25] Y. Wang, M. Yu, and S. Gao, “Gender diversity and financial statement fraud,” _Journal of Accounting and Public Policy_ , vol. 41, no. 2, p. 106903, 2022. 

- [26] J. Hendieh, M. Schneider, and T. Sakr, “Fraud detection and prevention,” _Middle-East Journal of Scientific Research_ , vol. 31, no. 1, pp. 44–52, 2023. 

- [27] A. Maniatis, “Detecting the probability of financial fraud due to earnings manipulation in companies listed in Athens Stock Exchange Market,” _Journal of Financial Crime_ , vol. 29, no. 2, pp. 603–619, 2022. 

- [28] Y. Gong, J. Li, Z. Xu, and G. Li, “Detecting financial fraud using two types of Benford factors: evidence from China,” _Procedia Computer Science_ , vol. 214, pp. 656–663, 2022, doi: 10.1016/j.procs.2022.11.225. 

- [29] P. Kagias, A. Cheliatsidou, A. Garefalakis, J. Azibi, and N. Sariannidis, “The fraud triangle – an alternative approach,” _JFC_ , vol. 

- 29, no. 3, pp. 908–924, May 2022, doi: 10.1108/JFC-07-2021-0159. 

- [30] T. Tarjo, H. V. Vidyantha, A. Anggono, R. Yuliana, and S. Musyarofah, “The effect of enterprise risk management on prevention and detection fraud in Indonesia’s local government,” _Cogent Economics & Finance_ , vol. 10, no. 1, p. 2101222, Dec. 2022, doi: 10.1080/23322039.2022.2101222. 

- [31] B. Stojanović and J. Božić, “Robust financial fraud alerting system based in the cloud environment,” _Sensors_ , vol. 22, no. 23, p. 9461, Dec. 2022, doi: 10.3390/s22239461. 

- [32] Y. Yao and J. Li, “Operational risk assessment of third-party payment platforms: A case study of China,” _Financ Innov_ , vol. 8, no. 1, p. 19, Dec. 2022, doi: 10.1186/s40854-022-00332-x. 

- [33] J. S. Kamdem and D. Selambi, “Cyber-risk forecasting using machine learning models and generalized extreme value distributions,” vol. 1, pp. 1–23, 2022. 

- [34] N. I. Mat Ridzuan, J. Said, F. M. Razali, D. I. Abdul Manan, and N. Sulaiman, “Examining the role of personality traits, digital technology skills and competency on the effectiveness of fraud risk assessment among external auditors,” _JRFM_ , vol. 15, no. 11, p. 536, Nov. 2022, doi: 10.3390/jrfm15110536. 

- [35] O. E. Akinbowale, H. E. Klingelhöfer, and M. F. Zerihun, “Application of forensic accounting techniques in the South African banking industry for the purpose of fraud risk mitigation,” _Cogent Economics & Finance_ , vol. 11, no. 1, p. 2153412, Dec. 2023, doi: 10.1080/23322039.2022.2153412. 

- [36] H. Wang, W. Wang, Y. Liu, and B. Alidaee, “Integrating machine learning algorithms with quantum annealing solvers for online fraud detection,” _IEEE Access_ , vol. 10, pp. 75908–75917, 2022. 

- [37] N. Innan _et al._ , “Financial fraud detection using quantum graph neural networks,” _Quantum Machine Intelligence_ , vol. 6, no. 1, pp. 1–18, 2024. 

- [38] A. Alwadain, R. F. Ali, and A. Muneer, “Estimating financial fraud through transaction-level features and machine learning,” _Mathematics_ , vol. 11, no. 5, p. 1184, 2023. 

- [39] L. Ren _et al._ , “Dynamic graph neural network-based fraud detectors against collaborative fraudsters,” _Knowledge-Based Systems_ , vol. 278, p. 110888, 2023. 

- [40] V. Chang, L. M. T. Doan, A. Di Stefano, Z. Sun, and G. Fortino, “Digital payment fraud detection methods in digital ages and Industry 4.0,” _Computers and Electrical Engineering_ , vol. 100, p. 107734, May 2022, doi: 10.1016/j.compeleceng.2022.107734. 

- [41] J. Chung and K. Lee, “Credit card fraud detection: An improved strategy for high recall using KNN, LDA, and linear regression,” _Sensors_ , vol. 23, no. 18, p. 7788, Sep. 2023, doi: 10.3390/s23187788. 

- [42] V. S. S. Karthik, A. Mishra, and U. S. Reddy, “Credit card fraud detection by modelling behavior pattern using hybrid ensemble model,” _Arab J Sci Eng_ , vol. 47, no. 2, pp. 1987–1997, Feb. 2022, doi: 10.1007/s13369-021-06147-9. 

- [43] H. Ahmad, B. Kasasbeh, B. Aldabaybah, and E. Rawashdeh, “Class balancing framework for credit card fraud detection based on clustering and similarity-based selection (SBS),” _Int. j. inf. tecnol._ , vol. 15, no. 1, pp. 325–333, Jan. 2023, doi: 10.1007/s41870-02200987-w. 

- [44] E. Esenogho, I. D. Mienye, T. G. Swart, K. Aruleba, and G. Obaido, “A neural network ensemble with feature engineering for improved credit card fraud detection,” _IEEE Access_ , vol. 10, pp. 16400–16407, 2022, doi: 10.1109/ACCESS.2022.3148298. 

- [45] J. Jiang _et al._ , “A dynamic ensemble algorithm for anomaly detection in IoT imbalanced data streams,” _Computer Communications_ , vol. 194, pp. 250–257, Oct. 2022, doi: 10.1016/j.comcom.2022.07.034. 

- [46] D. Sisodia and D. S. Sisodia, “Data sampling strategies for click fraud detection using imbalanced user click data of online advertising: An empirical review,” _IETE Technical Review_ , vol. 39, no. 4, pp. 789–798, Jul. 2022, doi: 10.1080/02564602.2021.1915892. 

- [47] A. Singh, R. K. Ranjan, and A. Tiwari, “Credit card fraud detection under extreme imbalanced data: A comparative study of data-level algorithms,” _Journal of Experimental & Theoretical Artificial Intelligence_ , vol. 34, no. 4, pp. 571–598, Jul. 2022, doi: 10.1080/0952813X.2021.1907795. 

- [48] A. J. McNeil, R. Frey, and P. Embrechts, _Quantitative risk management: concepts, techniques and tools_ , Revised edition. in Princeton series in finance. Princeton, NJ: Princeton University Press, 2015. 

- [49] D. Gorton, “Modeling fraud prevention of online services using incident response trees and value at risk,” in _2015 10th International Conference on Availability, Reliability and Security_ , Toulouse, France: IEEE, Aug. 2015, pp. 149–158. doi: 10.1109/ARES.2015.17. 

- [50] Y. Lyu, F. Qin, R. Ke, Y. Wei, and M. Kong, “Does mixed frequency variables help to forecast value at risk in the crude oil market?,” _Resources Policy_ , vol. 88, p. 104426, 2024, doi: https://doi.org/10.1016/j.resourpol.2023.104426. 

- [51] Abdullahi, SB. and Chamnongthai, K. “IDF-Sign: Addressing Inconsistent Depth Features for Dynamic Sign Word Recognition,” _IEEE Access_ , vol. 11, pp.88511–88526, 2023. 

- [52] A. Mahajan, V. S. Baghel, and R. Jayaraman, “Credit card fraud detection using logistic regression with imbalanced dataset,” in _2023 10th International Conference on Computing for Sustainable Global Development (INDIACom)_ , 2023, pp. 339–342. 

- [53] F. Aslam, A. I. Hunjra, Z. Ftiti, W. Louhichi, and T. Shams, “Insurance fraud detection: Evidence from artificial intelligence and machine learning,” _Research in International Business and Finance_ , vol. 62, p. 101744, Dec. 2022, doi: 10.1016/j.ribaf.2022.101744. 

- [54] E. Ileberi, Y. Sun, and Z. Wang, “A machine learning based credit card fraud detection using the GA algorithm for feature selection,” _J Big Data_ , vol. 9, no. 1, p. 24, Dec. 2022, doi: 10.1186/s40537-02200573-8. 

- [55] P. Atchaya and K. Somasundaram, “Novel logistic regression over naive bayes improves accuracy in credit card fraud detection,” _Journal of Survey in Fisheries Sciences_ , vol. 10, no. 1S, pp. 2172– 2181, 2023. 

VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



- [56] R. Bin Sulaiman, V. Schetinin, and P. Sant, “Review of machine learning approach on credit card fraud detection,” _hum-cent intell syst_ , vol. 2, no. 1–2, pp. 55–68, jun. 2022, doi: 10.1007/s44230-02200004-0. 

- [57] A. Kannagi, J. G. Mohammed, S. S. G. Murugan, and M. Varsha, “Intelligent mechanical systems and its applications on online fraud detection analysis using pattern recognition K-nearest neighbor algorithm for cloud security applications,” _Materials Today: Proceedings_ , vol. 81, pp. 745–749, 2023, doi: https://doi.org/10.1016/j.matpr.2021.04.228. 

- [58] P. H. Kupiec, _Techniques for verifying the accuracy of risk measurement models_ , vol. 95. Division of Research and Statistics, Division of Monetary Affairs, Federal Reserve Board, 1995. 

- [59] K. Kireev, M. Andriushchenko, C. Troncoso, and N. Flammarion, “Transferable adversarial robustness for categorical data via universal robust embeddings.” [Online]. Available: http://arxiv.org/abs/2306.04064 



**Abdullahi Ubale USMAN** received BSc in Statistics from Kano University of Science and Technology, Wudil, Nigeria in 2012, also received MSc in Statistics from Jodhpur National University, India in 2016. He is currently pursuing PhD degree with the School of Statistics and Mathematics, Zhejiang Gongshang University, Hangzhou, China. His current research interests are in financial fraud detection and machine learning. 



**Sunusi Bala ABDULLAHI** (Member, IEEE) received Ph.D. degree in King Mongkut’s University of Technology Thonburi, Thailand, also received the B.Sc. and M.Sc. degrees in electronics from Bayero University Kano (BUK), Nigeria. His current research interests include computer vision, artificial intelligence, nonlinear optimization and their applications in human motion analysis, data analysis, wireless systems, and social signal processing. 

University. He mainly involved in scientific and technological evaluation, technological innovation, and information management. He has six monographs. He is the first author for more than 170 articles. He has authored three articles in SCI and SSCI, 40 papers in first-class journals, and 140 papers in CSSCI. The academic achievements were collected by Xinhua digest and seven copies of the NPC. A paper was selected as Leader 5000-Top Academic Papers Platform for China’s Top Sci-Tech Journals (F5000). 



Amjad Rehman (Senior Member, IEEE) earned a PhD from the Faculty of Computing, Universiti Teknologi Malaysia (UTM), Malaysia, specializing in information security using image processing techniques in 2010. He received a Rector Award for the 2010 Best Student from UTM Malaysia. He is currently Associate Prof. at CCIS Prince Sultan University 

Riyadh, Saudi Arabia. He is also a PI in several projects and completed projects funded by MoHE Malaysia, Saudi Arabia. His research interests are bioinformatics, IoT, information security and pattern recognition. 

<mark>Bayan Alghofaily received the master’s and Ph.D. degrees in computer science from Toronto Metropolitan University, Toronto, Canada. During that period, she was a member of the Distributed Applications and Broadband Networks Laboratory (DABNEL). She focused on studying how the performance of machine learning models is affected by dataset features. She is currently an Assistant Professor with the Department of Information System, CCIS, Prince Sultan University (PSU). She is also a member of the Artificial Intelligence and Data Analytics (AIDA) Laboratory, CCIS, PSU. Her research interests include AI, NLP, ML, and neural networks. She continues to explore this further in her research.</mark> 

<mark>Ahmed S. Almasoud is currently an Assistant Professor in the College of Computer and Information Sciences at Prince Sultan University (PSU) in Riyadh, Saudi Arabia. Dr. Ahmed obtained his highest degree from University of Technology at Sydney and has worked in PSU from 2014 to present. He has published original articles in the finest journals in the area of his studies. His research interest includes (but not limited to) Artificial Intelligence,</mark> 

Machine Learning, Security Architecture, and Internet of Things <mark>.</mark> 

**Y. LIPING** received the Ph.D. degree. He is currently a Professor with Zhejiang Gongshang 

8 

VOLUME XX, 2017 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3393154 



VOLUME XX, 2017 

8 

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4 

