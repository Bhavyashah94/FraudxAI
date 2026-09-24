---
title: "Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine"
authors: "Reza E. Fazel, Arash Bakhtiary, Siavash A. Bigdeli"
year: 2026
venue: "arXiv / EN Bank Credit and Collection Department"
domain: "Inherently Interpretable EBM / Glass-Box Credit Card Fraud"
pdf_path: "docs/papers\2026_fazel_improving_credit_card_fraud_explainable_boosting_machine.pdf"
---

# Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine

**Authors:** Reza E. Fazel, Arash Bakhtiary, Siavash A. Bigdeli  
**Venue / Date:** arXiv / EN Bank Credit and Collection Department (2026)  
**Domain Focus:** Inherently Interpretable EBM / Glass-Box Credit Card Fraud  
**Original PDF:** [`2026_fazel_improving_credit_card_fraud_explainable_boosting_machine.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2026_fazel_improving_credit_card_fraud_explainable_boosting_machine.pdf)

---

# Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine 

Reza E. Fazel<sup>1*</sup> , Arash Bakhtiary<sup>2</sup> and Siavash A. Bigdeli<sup>3</sup> 

> 1*Credit and Collection Department, EN Bank, Tehran, Iran. 

> 2ReDi School, Copenhagen, Denmark. 

> 3Department of Applied Mathematics and Computer Science, DTU, Copenhagen, Denmark. 

*Corresponding author(s). E-mail(s): re.fazel22@gmail.com; Contributing authors: bakhtiary.arash@gmail.com; sarbi@dtu.dk; 

##### **Abstract** 

Addressing class imbalance is a central challenge in credit card fraud detection, as it directly impacts predictive reliability in real-world financial systems. To overcome this, the study proposes an enhanced workflow based on the Explainable Boosting Machine (EBM)—a transparent, state-of-the-art implementation of the GA²M algorithm—optimized through systematic hyperparameter tuning, feature selection, and preprocessing refinement. Rather than relying on conventional sampling techniques that may introduce bias or cause information loss, the optimized EBM achieves an effective balance between accuracy and interpretability, enabling precise detection of fraudulent transactions while providing actionable insights into feature importance and interaction effects. Furthermore, the Taguchi method is employed to optimize both the sequence of data scalers and model hyperparameters, ensuring robust, reproducible, and systematically validated performance improvements. Experimental evaluation on benchmark credit card data yields an ROC-AUC of 0.983, surpassing prior EBM baselines (0.975) and outperforming Logistic Regression, Random Forest, XGBoost, and Decision Tree models. These results highlight the potential of interpretable machine learning and data-driven optimization for advancing trustworthy fraud analytics in financial systems. 

**Keywords:** Explainable Boosting Machine, Imbalanced Data, Fraud Detection, Machine Learning, Taguchi Method 

1 

## **1 Introduction** 

In today’s digital economy, banks and credit card issuers face a critical responsibility: protecting customers from the growing threat of credit card fraud. As online transactions increase and fraud tactics become more sophisticated, the need to safeguard customers has become more urgent than ever. This protection is vital not only to uphold customer trust and financial security but also to ensure the integrity and stability of financial institutions. 

Over the past decade, the incidence of credit card fraud has increased considerably, placing immense pressure on financial institutions[1]. The Nilson Report revealed that global card fraud losses reached $33 billion in 2022, with the U.S. contributing roughly 40% of these losses. Projections indicate that card fraud will remain a significant concern, potentially escalating to nearly $400 billion globally by 2032[2]. 

Machine learning (ML) methods have become essential tools in addressing this issue, enabling issuers to detect fraud, adapt to new fraud techniques, and enhance customer trust. However, the success of ML-based fraud detection depends heavily on the quality of the training data[3, 4]. Unlike traditional techniques, ML approaches can instantly sift through large volumes of transaction data to spot anomalies, continuously improving by learning from each incident. This approach increases precision and reduces false positives. An ML-based fraud prevention strategy involves data collection, training algorithms on recent fraud patterns, and ongoing model optimization. These steps protect customers and strengthen trust, establishing a secure financial environment. Credit card fraud datasets tend to be imbalanced, with a much larger number of genuine transactions compared to fraudulent ones, making it essential to use specialized techniques and avoid skewed model performance. 

In financial contexts such as credit card fraud detection, having a model that is both high-performing and interpretable is critical. While many machine learning methods (e.g. boosted or bagged trees, SVMs, and deep neural networks) are effective for classification and regression tasks, their complexity makes the resulting models difficult for users to interpret[5]. 

To address these issues, we adopt a cutting-edge glass-box approach which manages data imbalance effectively without using resampling or anomaly detection methods. Using Explainable Boosting Machines (EBM) [6], we consistently achieve strong performance in the classification. A standout feature of the model is its ability to rank features by importance and impact on the target class, enabling selection of the most influential variables. This not only boosts model performance but also helps reduce complexity. 

Our proposed approach includes a data preprocessing and hyperparameter tuning pipeline using the Taguchi method to further improve the accuracy of the classifier model. In addition to identifying fraudulent transactions, our model can highlight the key factors that drive fraud detection, enabling card issuers to refine strategies and prune less significant features. 

This paper leverages EBM to strike a balance between interpretability and high performance. Unlike black-box models, EBM constructs an additive model that displays the effects of individual features and pairwise interactions on predictions, aiding 

2 

in feature selection. It often matches the performance of complex models like Random Forest and XGBoost, making it especially suitable for critical tasks such as fraud detection. In this work, we also compare EBM’s classification results with Logistic Regression, XGBoost, Random Forest, and Decision Tree models. 

## **2 Literature Review** 

In recent years, researchers have focused on AI-driven methods to improve credit card fraud detection, addressing the challenge of imbalanced datasets. These efforts aim to identify and compare the most effective models and techniques to enhance predictive accuracy. Fraud detection models examine examples of both fraudulent and legitimate transactions to determine whether a new transaction should be flagged as fraudulent [7]. Supervised classification, which requires pre-labeled data, has been particularly effective. However, the scarcity of illicit transaction records compared to the total transaction volume poses a significant challenge due to class imbalance [8]. Many researchers have used advanced sampling techniques like SMOTE, whereas others rely purely on state-of-the-art models without explicitly adopting sampling methods. 

### **2.1 Sampling Methods and Their Variants** 

Several studies have effectively applied Synthetic Minority Oversampling Technique (SMOTE) to address imbalanced datasets in credit card fraud detection, demonstrating its impact on improving model performance by generating synthetic samples for underrepresented classes [9–12], while some have found under-sampling more effective to address data imbalance when using a specific model [13]. 

Hybrid resampling techniques have been effectively applied in recent years, yielding significant improvements in model performance [7, 14–16]. Some recent research compares resampling methods. For instance [17] found that random oversampling and XGBoost yielded superior results, whereas [18] concluded that Random Forest performed best with under-sampled data. [19] emphasized the importance of adaptable models for evolving fraud tactics. [20] showed that ANN, combined with Benford’s law and SMOTE, improved Random Forest and Logistic Regression methods for money laundering detection. [21] compared threshold optimization with random under-sampling (RUS) and found threshold optimization more effective. 

### **2.2 Alternative Approaches** 

Generative Adversarial Networks (GANs) are another effective method for handling data imbalance and have been extensively used in recent fraud detection research [8, 22]. However, GANs require significant computational resources, and their performance can vary with architecture and training [23]. Some studies report that GANs outperform traditional methods such as Adaptive Synthetic Sampling (ADASYN) and SMOTE [23, 24]. Meanwhile, several researchers propose innovative techniques beyond existing resampling frameworks. [25] used anomaly detection to remove outliers before training a non-linear classifier and employed a Dynamic Weighted Entropy and a 

3 

Signal-to-Noise Ratio-based formula to handle class imbalance. [26] applied Stochastic Semi-Supervised Learning and Active Learning strategies to enhance training diversity. 

Autoencoders have also been integrated with various sampling strategies to address high-dimensional data challenges [27–29]. Combining autoencoders with deep learning or machine learning models can outperform traditional methods [30–32]. 

Leveraging deep learning models to tackle the challenge of imbalanced datasets has been a focus of several studies in recent years and has acquired strong results [33–36]. There are other research studies that forego explicit resampling, often relying on tree-based approaches that inherently handle imbalance by focusing on the most informative splits. 

A cost-sensitive decision tree, which focuses on high-value fraudulent transactions was developed by [37]. [38] assessed Decision Tree, Random Forest, and XGBoost for fraud detection, identifying XGBoost as the most effective. They addressed class imbalance via adjusted class weights and XGBoost’s scale ~~p~~ os ~~w~~ eight, highlighting the importance of metrics beyond accuracy for robust evaluation. [39] selected Random Forest for its ability to handle high-dimensional data and manage class imbalance via ensemble learning. In another study by [40] a hybrid approach was proposed where unsupervised methods like Isolation Forests, k-means, and Autoencoders to detect anomalies, and supervised methods like Random Forests, SVM, and Neural Networks were employed for classification using labeled data. [41] found that CatBoost outperformed other methods (Random Forest, XGBoost, Logistic Regression) for handling data imbalance. [42] examined various ML methods for credit card fraud detection, identifying Logistic Regression as the most effective for predicting fraud based on transaction features. [43] introduced the CCAD model, combining ensemble learning and meta-learning for anomaly detection. [44] proposed a cost-sensitive fraud detection model that combines dynamic Random Forest and KNN, effectively handling class imbalance and improving accuracy. 

Generalized additive models (GAMs) are considered the benchmark for interpretability when only univariate terms are included[45, 46]. Unfortunately, there is often a considerable gap in accuracy between the best standard GAMs and more complex models, such as tree ensembles[46]. [5] introduced a model class known as GA²M that incorporates pairwise interactions while retaining intelligibility. [6] later developed an open-source python package that implementing an efficient GA²M-based algorithm called the Explainable Boosting Machine (EBM), which achieves accuracy comparable to state-of-the-art methods such as Random Forest and Boosted Trees but remains highly interpretable. 

Although many recent studies apply Reinforcement Learning (RL) for HPO, we deliberately avoid RL for two key reasons. First, fraud detection datasets are typically highly imbalanced, as fraudulent events rarely occur, and offline RL often exhibits poor performance under such conditions [47]. Second, RL is extremely sensitive to its own hyperparameter settings [48–50], requiring additional hyperparameter tuning—a repetitive and time-consuming process that contradicts our efficiency goals. 

In this work, we employ the Taguchi approach—a form of Design of Experiments—to address two main objectives: determining the optimal sequence of data scalers prior to model training, and performing hyperparameter optimization (HPO) 

4 

for our model. The Taguchi method substantially reduces the number of experiments required, leading to significant savings in both computational cost and execution time. 

## **3 Dataset Description** 

European credit card fraud detection dataset from Kaggle is used in this research, comprising 284,807 transactions. The dataset consists of 30 features, and a 31st column (“Class”) indicates the response variable with two values: 0 for legitimate transactions and 1 for frauds. For privacy, features V1 through V28 have been transformed via Principal Component Analysis (PCA), but “Time” and “Amount” remain unmodified. 

The dataset is highly imbalanced, with 284,315 samples in class 0 and 492 in class 1, resulting in a class ratio of 1:577. We do not employ any resampling approach due to concerns about losing large portions of majority-class data (in under-sampling) or generating potentially non-informative synthetic samples (in over-sampling). Instead, we center our efforts on optimizing an advanced Explainable Boosting Machine model to achieve high accuracy. 

## **4 Exploratory Data Analysis** 

### **4.1 Correlation analysis** 

We examined various relationships—linear, monotonic, and complex— among the features using correlation matrices. The Pearson correlation matrix yielded values ranging from -0.53 to 0.4, indicating only weak to moderate relationships. To explore potential monotonic associations, we also examined Spearman’s and Kendall’s correlation coefficients. While Spearman and Kendall highlighted a moderate correlation between variables V21 and V22, this relationship was not captured by Pearson. According to [51], Spearman and Kendall sometimes outperform Pearson in detecting linear associations, while Pearson can be more sensitive to certain nonlinear relationship patterns. The above observations merit further exploration, detailed in our Experimental Results section. 

#### **4.1.1 Chatterjee’s Correlation Coefficient** 

Pearson, Spearman, and Kendall are all strong tools for detecting linear or monotonic relationships; however, they do not detect non-monotonic interactions, even when the data are noise-free [52]. [52] introduced a correlation coefficient _ξ_ **n** , and demonstrated that as the size of the data set (n) grows, this coefficient converges to a theoretical value _ξ_ ( _X, Y_ ) that equals one if Y is a measurable function of X, and zero if X and Y are independent [53]. In this case we used XICOR package for R [54], as researchers like [55] note that traditional correlation coefficients are limited to simpler relationships between two random variables. 

As clearly illustrated in Fig. 1 which is plotted using the ComplexHeatmap package in R [56], a moderate correlation between V21 and V22 is evident. Also there is a noteworthy correlation between V17 and Class which a discussion of these findings 

5 

1.00 0.06 0.02 0.19 0.04 0.06 0.02 0.03 0.03 0.10 0.03 0.06 0.14 0.09 0.10 0.09 0.02 0.05 0.03 0.01 0.02 0.04 0.04 0.03 0.01 0.07 0.03 0.02 0.05 0.03 0.06 Time 0.22 1.00 0.28 0.30 0.15 0.14 0.09 0.21 0.13 0.13 0.14 0.05 0.08 0.04 0.05 0.07 0.05 0.06 0.05 0.07 0.15 0.07 0.07 0.14 0.04 0.19 0.05 0.13 0.28 0.15 0.05 V1 0.03 0.28 1.00 0.09 0.10 0.18 0.06 0.25 0.06 0.10 0.12 0.04 0.05 0.03 0.06 0.04 0.05 0.06 0.05 0.04 0.10 0.06 0.04 0.08 0.04 0.08 0.04 0.09 0.09 0.22 0.10 V2 0.18 0.21 0.05 1.00 0.04 0.10 0.08 0.06 0.08 0.04 0.04 0.04 0.04 0.03 0.08 0.05 0.04 0.06 0.04 0.04 0.05 0.05 0.06 0.06 0.05 0.07 0.04 0.07 0.10 0.05 0.17 V3 0.07 0.13 0.09 0.07 1.00 0.06 0.08 0.06 0.05 0.12 0.13 0.05 0.08 0.04 0.05 0.07 0.08 0.07 0.05 0.09 0.06 0.05 0.06 0.06 0.05 0.07 0.13 0.07 0.06 0.05 0.18 V4 0.06 0.10 0.18 0.09 0.06 1.00 0.10 0.25 0.08 0.05 0.06 0.04 0.05 0.04 0.06 0.05 0.04 0.07 0.04 0.03 0.05 0.04 0.04 0.05 0.08 0.04 0.04 0.04 0.05 0.11 0.07 V5 0.03 0.08 0.05 0.12 0.07 0.13 1.00 0.10 0.22 0.04 0.04 0.06 0.05 0.04 0.05 0.05 0.05 0.06 0.06 0.05 0.04 0.05 0.06 0.04 0.17 0.04 0.04 0.05 0.04 0.07 0.06 V6 0.04 0.15 0.23 0.06 0.07 0.23 0.12 1.00 0.15 0.06 0.07 0.04 0.05 0.03 0.06 0.05 0.05 0.05 0.04 0.03 0.06 0.05 0.06 0.07 0.04 0.04 0.04 0.08 0.06 0.09 0.13 V7 0.04 0.19 0.08 0.11 0.04 0.08 0.26 0.19 1.00 0.04 0.05 0.05 0.05 0.06 0.06 0.04 0.06 0.06 0.04 0.03 0.05 0.07 0.06 0.06 0.06 0.04 0.03 0.09 0.07 0.05 0.07 V8 0.03 0.08 0.10 0.05 0.08 0.07 0.05 0.08 0.04 1.00 0.14 0.04 0.09 0.05 0.06 0.05 0.05 0.06 0.05 0.04 0.05 0.05 0.04 0.04 0.04 0.04 0.05 0.04 0.05 0.06 0.26 V9 0.04 0.16 0.12 0.06 0.12 0.08 0.05 0.09 0.06 0.16 1.00 0.05 0.08 0.04 0.09 0.06 0.05 0.09 0.06 0.05 0.08 0.06 0.05 0.05 0.04 0.05 0.05 0.05 0.07 0.06 0.42 V10 0.08 0.06 0.04 0.06 0.05 0.05 0.08 0.05 0.07 0.05 0.04 1.00 0.10 0.05 0.07 0.09 0.04 0.07 0.06 0.05 0.04 0.05 0.05 0.05 0.09 0.05 0.04 0.04 0.04 0.06 0.41 V11 0.04 0.05 0.05 0.05 0.06 0.06 0.05 0.06 0.05 0.12 0.08 0.11 1.00 0.16 0.11 0.06 0.05 0.09 0.04 0.03 0.04 0.04 0.04 0.04 0.04 0.04 0.04 0.03 0.03 0.05 0.51 V12 0.03 0.04 0.03 0.04 0.03 0.04 0.05 0.03 0.06 0.06 0.03 0.04 0.14 1.00 0.08 0.04 0.03 0.04 0.03 0.03 0.04 0.04 0.04 0.03 0.04 0.03 0.03 0.03 0.03 0.04 0.04 V13 0.05 0.05 0.07 0.09 0.05 0.07 0.06 0.07 0.05 0.07 0.06 0.07 0.09 0.09 1.00 0.06 0.05 0.14 0.05 0.03 0.04 0.05 0.05 0.04 0.04 0.04 0.04 0.04 0.04 0.05 0.47 V14 Xi Correlation1 0.06 0.05 0.03 0.06 0.05 0.05 0.07 0.04 0.05 0.04 0.03 0.05 0.04 0.03 0.05 1.00 0.04 0.04 0.04 0.04 0.04 0.04 0.04 0.03 0.04 0.04 0.04 0.03 0.04 0.05 0.04 V15 0.50 −0.5 0.03 0.05 0.06 0.04 0.06 0.05 0.06 0.06 0.05 0.06 0.06 0.04 0.06 0.03 0.05 0.04 1.00 0.10 0.09 0.05 0.06 0.06 0.06 0.04 0.04 0.04 0.06 0.03 0.03 0.07 0.37 V16 −1 0.03 0.06 0.05 0.06 0.05 0.07 0.07 0.05 0.05 0.05 0.06 0.05 0.07 0.04 0.09 0.04 0.11 1.00 0.08 0.05 0.03 0.04 0.04 0.04 0.06 0.03 0.04 0.03 0.04 0.05 0.56 V17 0.03 0.04 0.05 0.04 0.04 0.05 0.06 0.05 0.05 0.05 0.05 0.05 0.04 0.03 0.05 0.04 0.08 0.09 1.00 0.05 0.04 0.05 0.05 0.04 0.06 0.03 0.04 0.03 0.03 0.06 0.28 V18 0.03 0.07 0.03 0.05 0.05 0.04 0.09 0.03 0.05 0.05 0.05 0.04 0.04 0.03 0.04 0.05 0.06 0.05 0.04 1.00 0.08 0.04 0.05 0.04 0.05 0.04 0.04 0.03 0.04 0.05 0.05 V19 0.03 0.18 0.09 0.07 0.06 0.06 0.05 0.07 0.05 0.07 0.07 0.03 0.04 0.05 0.05 0.04 0.08 0.04 0.05 0.09 1.00 0.07 0.04 0.08 0.04 0.04 0.04 0.07 0.10 0.12 0.04 V20 0.05 0.09 0.07 0.05 0.05 0.05 0.06 0.06 0.11 0.05 0.05 0.04 0.04 0.03 0.05 0.04 0.06 0.04 0.04 0.03 0.10 1.00 0.50 0.09 0.04 0.05 0.05 0.04 0.05 0.08 0.05 V21 0.06 0.05 0.04 0.06 0.05 0.05 0.05 0.04 0.05 0.04 0.04 0.03 0.04 0.03 0.04 0.03 0.05 0.04 0.05 0.04 0.04 0.43 1.00 0.08 0.04 0.06 0.06 0.04 0.04 0.06 0.04 V22 0.05 0.16 0.08 0.07 0.04 0.06 0.05 0.07 0.05 0.04 0.04 0.04 0.04 0.03 0.04 0.04 0.03 0.04 0.05 0.04 0.08 0.10 0.09 1.00 0.05 0.18 0.04 0.06 0.06 0.08 0.04 V23 0.08 0.05 0.04 0.07 0.05 0.10 0.18 0.04 0.09 0.04 0.04 0.12 0.06 0.05 0.05 0.06 0.05 0.07 0.06 0.05 0.04 0.06 0.08 0.06 1.00 0.04 0.05 0.03 0.04 0.05 0.04 V24 0.08 0.09 0.05 0.05 0.04 0.06 0.04 0.05 0.05 0.04 0.04 0.04 0.03 0.03 0.04 0.04 0.04 0.04 0.03 0.03 0.04 0.04 0.05 0.16 0.04 1.00 0.05 0.05 0.05 0.05 0.04 V25 0.07 0.08 0.09 0.07 0.09 0.07 0.07 0.07 0.05 0.08 0.07 0.04 0.05 0.04 0.06 0.05 0.07 0.06 0.06 0.05 0.05 0.10 0.13 0.08 0.06 0.08 1.00 0.09 0.05 0.09 0.04 V26 0.03 0.31 0.15 0.10 0.05 0.07 0.07 0.13 0.10 0.06 0.08 0.04 0.04 0.04 0.07 0.05 0.04 0.04 0.04 0.04 0.08 0.06 0.06 0.06 0.04 0.08 0.11 1.00 0.23 0.07 0.05 V27 0.14 0.41 0.12 0.18 0.05 0.10 0.05 0.11 0.07 0.07 0.09 0.05 0.04 0.04 0.07 0.06 0.04 0.05 0.05 0.04 0.12 0.07 0.06 0.10 0.05 0.12 0.05 0.23 1.00 0.07 0.04 V28 0.04 0.06 0.25 0.06 0.12 0.11 0.07 0.10 0.04 0.10 0.10 0.02 0.05 0.03 0.06 0.05 0.07 0.05 0.05 0.04 0.12 0.13 0.14 0.07 0.01 0.05 0.14 0.07 0.04 1.00 0.03 Amount 0.00 0.00 0.00 0.00 0.00 −0.00 0.00 −0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 −0.00 0.00 −0.00 0.00 −0.00 0.00 0.00 0.00 0.00 −0.00 0.00 −0.00 1.00 Class 

**Fig. 1** Chatterjee’s Correlation Coefficient Heatmap 

will be provided in the Experimental Results section. A Chatterjee’s correlation coefficient of 0.51 between V12 and Class and also 0.56 for V17 and the Class suggests a moderate degree of association between them. The Chatterjee correlation is a rankbased measure, making it robust to nonlinear and non-monotonic relationships. These numbers indicate the features likely provides meaningful information about the target. 

### **4.2 Multicollinearity Analysis** 

If independent features are highly correlated, multicollinearity arises, and makes it difficult for the model to distinguish the effect of each feature on the dependent outcome. 

To find multicollinearity, we use Variance Inflation Factor (VIF). It assesses how much the variance of an estimated regression coefficient is inflated when predictors are correlated [57]. The formula for the VIF is as follows: 

6 

1 VIF _i_ = (1) 1 _− Ri_<sup>2</sup> 

Where _Ri_<sup>2is the coefficient of determination obtained by regressing the</sup><sup>_i_th predictor</sup> variable against all other predictor variables in the model. Table 1 shows the results of VIF analysis for all features in dataset. 

**Table 1** VIF Analysis for Detecting Multicollinearity 

|Feature|VIF|Standard<br>Error|CI<br>Lower|CI<br>Upper|
|---|---|---|---|---|
|Time|2.340|0.003|2.335|2.345|
|V1|1.638|0.001|1.636|1.641|
|V2|3.901|0.005|3.890|3.911|
|V3|1.321|0.001|1.320|1.322|
|V4|1.172|0.000|1.172|1.173|
|V5|2.764|0.003|2.758|2.771|
|V6|1.529|0.001|1.527|1.531|
|V7|2.604|0.003|2.598|2.609|
|V8|1.099|0.000|1.098|1.099|
|V9|1.038|0.000|1.038|1.038|
|V10|1.209|0.000|1.208|1.210|
|V11|1.080|0.000|1.080|1.081|
|V12|1.154|0.000|1.154|1.155|
|V13|1.003|0.000|1.003|1.003|
|V14|1.220|0.000|1.219|1.220|
|V15|1.014|0.000|1.014|1.014|
|V16|1.081|0.000|1.081|1.081|
|V17|1.227|0.000|1.226|1.228|
|V18|1.034|0.000|1.034|1.034|
|V19|1.041|0.000|1.041|1.041|
|V20|2.234|0.002|2.229|2.238|
|V21|1.103|0.000|1.103|1.103|
|V22|1.082|0.000|1.082|1.083|
|V23|1.149|0.000|1.149|1.150|
|V24|1.001|0.000|1.001|1.001|
|V25|1.014|0.000|1.013|1.014|
|V26|1.001|0.000|1.001|1.001|
|V27|1.010|0.000|1.009|1.010|
|V28|1.002|0.000|1.002|1.002|
|Amount|11.508|0.020|11.469|11.547|
|Class|2.094|0.002|2.090|2.098|



There are varying perspectives on how to interpret VIF results and whether a universal rule can be applied across all contexts. The debate arises from differences in research fields, dataset characteristics, and specific analytical goals, leading to differing opinions on the applicability of general thresholds. 

[57] stated that a VIF between 5 and 10 suggests a notable correlation that may create difficulties. When VIF surpasses 10, it typically signifies severe multicollinearity, leading to unreliable regression estimates and requiring corrective action. [58] cautioned against relying solely on standard VIF thresholds (e.g., above 4 or 10) as 

7 

the sole criterion for handling multicollinearity, such as by removing predictors. He focused on the importance of considering other factors, such as sample size, which can greatly influence the variability of regression coefficients and provide a more thorough understanding of the issue. 

[59] examine commonly used thresholds for VIF and Tolerance Index (TI), indicating that a VIF greater than 10 signifies serious multicollinearity, while values over 5 signals potential concerns requiring further analysis. They caution against strictly applying these thresholds, as their applicability depends on factors like sample size and study context. Additionally, they highlight that confidence intervals for VIF provide deeper insights, particularly when point estimates are close to the thresholds. 

The VIF output reveals that most variables, such as V1, V3, and V4, have VIF values well below 5, indicating low to moderate multicollinearity, and therefore do not pose important issues. However, the “Amount” variable has a VIF of 11.51, which is notably high, suggesting significant multicollinearity. Additionally, the wide confidence interval for “Amount” (ranging from 11.469 to 11.547) indicates a level of instability in the VIF estimate. This suggests that “Amount” may be highly correlated with other variables in the model. The standard errors for most variables are small, indicating precise estimates of VIF, but the larger standard error for “Amount” further points to its instability and the need for further actions. Overall, most predictors do not show concern for multicollinearity; however, we employ feature scaling and transformation for the whole dataset, which offer an effective way to mitigate the impact of multicollinearity, especially for “Amount” variable. In this study, techniques such as normalization, standardization, and other data scaling methods are applied to adjust the feature values. Additionally, tree-based models, known for their robustness to multicollinearity, are utilized. Specifically, the research employs the Explainable Boosting Machine, a type of tree-based model, to enhance interpretability and model performance. 

### **4.3 Causality Analysis** 

In this study, the DoWhy package in Python was used to perform causal inference. Results revealed minimal causal effects for all features except “Amount,” which showed a remarkable causal relationship with multiple features. Removing “Amount” from the dataset led to a decrease in model precision, underscoring its importance in improving predictive accuracy. 

## **5 Data Transformation** 

In this phase, we apply five data transformers —normalization, standardization, power transform, quantile transform, and robust scaler—and use the GridSearchCV to optimize their hyperparameters. These transformers are applied to five classification models: Logistic Regression, Decision Tree, Random Forest, XGBoost, and EBM. We then use GridSearchCV to optimize the hyperparameters for each transformation. 

8 

Table 2 illustrates the performance outcomes of various models after applying five distinct scalers optimized with their best hyperparameters. As observed, the EBM notably outperforms the other methods on all four performance metrics. The next step involves identifying the best sequence of scalers. Testing all permutations of scaler orders is computationally expensive, so we employ the Taguchi method to streamline this process. The sequence yielding the highest ROC-AUC score is adopted as the optimal configuration. 

**Table 2** Comparison of model performance after applying five distinct scalers, optimized with best hyperparameters. It is clearly visible that EBM consistently outperforms other models. 

|Scaler|Model|Best Parameters|Precision|Recall|ROC<br>~~A~~UC|F1 Score|
|---|---|---|---|---|---|---|
|minmax|LR|feature<br>~~r~~ange: (-1 , 1)|0.845|0.545|0.773|0.663|
|standard<br>|LR<br>|with<br>~~m~~ean:<br>False;<br>with<br>std:<br>False<br><br>|0.792<br>|0.691<br>|0.845<br>|0.738<br>|
|quantile|LR|n<br>~~q~~uantiles:<br>1000;<br>out-<br>put<br>~~d~~istribution: ’uniform’|0.794|0.736|0.868|0.764|
|robust|LR|quantile<br>~~r~~ange: (25.0 , 75.0)|0.825|0.600|0.800|0.695|
|power|LR|method’: ’yeo-johnson’|0.823|0.591|0.795|0.688|
|minmax|RF|feature<br>~~r~~ange: (0 , 0.5)|0.976|0.727|0.864|0.833|
|standard|RF|with<br>~~m~~ean:<br>False;<br>with<br>std:<br>False|0.975|0.718|0.859|0.827|
|quantile|RF|n<br>~~q~~uantiles:<br>1000;<br>out-<br>put<br>~~d~~istribution: ’normal’|0.975|0.718|0.859|0.827|
|robust|RF|quantile<br>~~r~~ange: (25.0 , 75.0)|0.975|0.718|0.859|0.827|
|power|RF|method: ’yeo-johnson’|0.952|0.718|0.859|0.819|
|minmax|DT|feature<br>~~r~~ange: (-1 , 1)|0.670|0.682|0.841|0.676|
|standard|DT|with<br>~~m~~ean:<br>True;<br>with<br>std:<br>True|0.639|0.691|0.845|0.664|
|quantile|DT|n<br>~~q~~uantiles:<br>1000;<br>out-<br>put<br>~~d~~istribution: ’normal’|0.672|0.709|0.854|0.690|
|robust|DT|quantile<br>~~r~~ange: (25.0 , 75.0)|0.670|0.682|0.841|0.676|
|power|DT|method: ’yeo-johnson’|0.667|0.673|0.836|0.670|
|minmax|XGB|feature<br>~~r~~ange: (0 , 1)|0.976|0.736|0.868|0.839|
|standard|XGB|with<br>~~m~~ean: True ; with<br>std:<br>True|0.976|0.736|0.868|0.839|
|quantile|XGB|n<br>~~q~~uantiles:<br>1500<br>;<br>out-<br>put<br>~~d~~istribution: ’normal’|0.976|0.736|0.868|0.839|
|robust|XGB|quantile<br>~~r~~ange: (25.0 , 75.0)|0.976|0.736|0.868|0.839|
|power|XGB|method: ’yeo-johnson’|0.976|0.736|0.868|0.839|
|minmax|EBM|feature<br>~~r~~ange’: (0 , 1)|0.988|0.755|0.877|0.856|
|standard|EBM|with<br>~~m~~ean: True ; with<br>std:<br>True|0.988|0.755|0.877|0.856|
|quantile|EBM|n<br>~~q~~uantiles:<br>1000<br>;<br>out-<br>put<br>~~d~~istribution: ’normal’|0.976|0.755|0.877|0.851|
|robust|EBM|quantile<br>~~r~~ange: (25.0 , 75.0)|0.988|0.755|0.877|0.856|
|power|EBM|method: ’yeo-johnson’|0.988|0.755|0.877|0.856|



Note: LR = Logistic Regression; RF = Random Forest; DT = Decision Tree; XGB = XGBoost 

9 

## **6 Optimization Techniques** 

### **6.1 Taguchi Method for Scalers’ Order** 

Developed by Genichi Taguchi, the Taguchi method systematically tests multiple factors with fewer experiments by using orthogonal arrays (OAs), which have a high degree of statistical confidence [60]. It is a systematic approach to designing experiments that helps optimize process or product performance while minimizing variability. It uses orthogonal arrays (OAs), which are specially arranged tables where each row represents an experimental run and each column represents a factor. These arrays allow balanced and independent testing of factor levels, reducing the total number of experiments compared to a full factorial design. 

In practice, factors and their levels are selected, an appropriate OA is chosen, and experiments are conducted according to the array. The results are analyzed using the Signal-to-Noise (S/N) ratio, which highlights both performance and robustness. This process identifies the optimal factor settings efficiently, saving time and resources while ensuring reliable outcomes. 

Rather than exhaustively testing all possible arrangements of the scalers, this approach chooses a reduced set of configurations that captures all influential factor levels. Since the goal of this research is to assess five different scalers and determine their optimal ordering for preprocessing data, we employ the standard L25 Taguchi OA. The L25 design tests 25 specific combinations of scalers instead of all 120 possible arrangements, significantly reducing computational time and complexity. We use the standard L25 OA for five scalers and five positions, modifying rows to skip redundant repeats by placing 0 for ’do nothing.’ Through StratifiedKFold cross-validation, each row’s AUC is computed, and the best sequence is selected. 

### **6.2 Hyperparameter Tuning for Models** 

Hyperparameters are crucial for controlling model complexity and preventing underfitting or overfitting. At this stage, we determine the optimal hyperparameters for each model by employing a Taguchi L9 orthogonal array (4 × 3). This Taguchi-based method allows us to identify the best combination of 4 different parameters, each with 3 different values, while minimizing computational costs. Using the L9 orthogonal array, we can efficiently test only 9 experiments to find the optimal settings, rather than testing all 81 possible combinations (since testing all status combinations would require evaluating 3<sup>4</sup> = 81 different setups). The orthogonal array approach strategically selects a subset of these combinations to ensure comprehensive coverage of the parameter space, significantly reducing the number of experiments needed while still identifying the best configuration for model performance. Table 3 presents the optimal hyperparameters, focusing on the four most influential ones, each evaluated across three distinct levels for all models. 

For class imbalance, we applied modelspecific techniques. For instance, in XGBoost, we used the scale ~~p~~ os ~~w~~ eight parameter to adjust for class distribution, and similar rebalancing strategies were adopted where available in other models. 

10 

**Table 3** Optimal Hyperparameters for All models using the Taguchi method 

|Model|Optimal Hyperparameters|ROC-AUC|
|---|---|---|
|Logistic Regression<br>Random Forest|C: 1, penalty: l2, class<br>weight: _{_0: 1, 1: 10_}_, solver: saga<br>max<br>~~d~~epth: 10, n<br>~~e~~stimators: 200, class<br>~~w~~eight: None,<br>max<br>~~f~~eatures: sqrt|0.981<br>0.974|
|Decision Tree|max<br>~~d~~epth: 5, min<br>~~s~~amples<br>~~s~~plit: 50, min<br>~~s~~amples<br>leaf: 20,<br>class<br>~~w~~eight: _{_0: 1, 1: 10_}_|0.926|
|XGBoost|learning<br>~~r~~ate: 0.1, max<br>~~d~~epth: 3, scale<br>pos<br>~~w~~eight: 10,<br>subsample: 1.0|0.980|
|EBM|interactions:<br>20,<br>max<br>bins:<br>256,<br>learning<br>rate:<br>0.05,<br>max<br>~~r~~ounds: 100|0.984|



To examine how sensitive the models are to the structure of the orthogonal array and the number of levels used, the analysis was extended using an L27 design with five hyperparameters at three levels each. Although this allowed for a broader exploration of the hyperparameter space, it led to only minimal changes in performance. 

## **7 Methodology** 

The Explainable Boosting Machine (EBM) is an advanced machine learning model combining high interpretability with accuracy comparable to models like Random Forest and XGBoost. EBM is inspired by the Generalized Additive Model (GAM): 



where _g_ represents the link function, which is applied to the expected value of response variable _y_ and _β_ 0 is the intercept. GAM is applicable to different settings such as regression or classification [6]. 

[5] observe that two-dimensional interactions can be visualized as heatmaps of _fij_ ( _xi, xj_ ) on the two-dimensional _xi, xj_ -plane. This approach, called Generalized Additive Models plus Interactions (GA2M), makes an interpretable model with oneand two-dimensional components, while also improves the overall performance. The model is formulated as: 



This additive part with the pair-wise elements ensures both robust accuracy and high interpretability [6]. 

We use the determined scaler sequences and hyperparameter configurations with best performance to train our initial EBM model. Our next goal is to identify the most significant features that contribute to the target variable (model prediction) in our binary classification task. We then retrain the model using only the top features, reducing complexity and computational efficiency by decreasing runtime. Finally, we 

11 



**Fig. 2** Feature Importance and Pairwise Interactions 

train other machine learning models on these selected features to compare their performance against EBM. As we show in the results, this approach provides a better balance between interpretability and predictive accuracy. 

Fig. 2 highlights the most significant individual features and pairwise interactions using EBM’s explain ~~g~~ lobal() function, ranking them by their importance to the target class. EBM can automatically identify and incorporate meaningful two-dimensional interactions. 

It learns each feature function _fj_ using methods like bagging and gradient boosting. Boosting is limited to focus on one feature at a time in a round-robin fashion with a very low learning rate, ensuring that the order of features doesn’t affect results. This approach helps reduce co-linearity issues and learns the best function for each feature, clarifying how each contributes to the model’s predictions. Additionally, EBM can automatically detect and incorporate pairwise interactions of the formula (2) form which improves accuracy while keeping the model intelligible [6]. 

Fig. 3 illustrates the ranked contributions of all individual features and pairwise interactions in class prediction. 

EBM also furnishes local-level interpretability through the explain ~~l~~ ocal() function, which shows how each feature contributes to an individual sample’s prediction. 

Fig. 4 is a “local feature explanation” chart that shows the contributions of individual features to a machine learning model’s prediction. Here’s what the picture communicates: 

The title indicates that the actual class is 0, the predicted class is 0, and the probability of Class 0 (Pr(y=0)) is 1. This means the model is almost 100% confident in predicting the class as 0. In the bar chart explanation, the list of features is shown on the y-axis, where these features contributed to the final prediction. The intercept is displayed at the top as a baseline value for the prediction which represents the starting prediction before considering the feature contributions. The “blue bars” represent negative contributions (pulling the prediction towards class 0), while the “orange bars” represent positive contributions (pushing the prediction towards the opposing class, 

12 



**Fig. 3** Feature Importance and pairwise interaction of All Features from EBM’s Global Explanation 



**Fig. 4** Feature Contributions to a Class 0 Prediction 

but not enough to change the outcome). The magnitude of the contributions is reflected by the length of the bars, with those extending further to the left or right indicating a greater impact on the prediction. 

In terms of interpretation, the most influential features that pushed the prediction towards class 0 include ‘feature ~~0~~ 003‘, ‘feature ~~0~~ 012‘, ‘feature ~~0~~ 014‘ (which represent V3, V12 and V14), and others with substantial blue bars. Some features, like ‘feature ~~0~~ 011‘ and ‘feature 0029‘, have smaller contributions shown as orange bars, which slightly counteract the dominant prediction but remain insufficient to shift the result. So the model predicts “Class 0” with extremely high confidence, and the key contributing features are those with significant negative (blue) contributions. 

13 

Fig. 5 demonstrates how individual features contributed to the model’s prediction for a specific sample with class 1. The prediction context shows that the actual class is 1, the predicted class is also 1, and the probability of class 1 is 0.927. This indicates that the model is highly confident, with a 92.7% probability, that this sample belongs to class 1. The majority of the features contribute positively, as indicated by the orange bars. For instance, ‘feature ~~0~~ 014‘ (wich represents V14) has the largest positive contribution, with a value of -3.46, making it a critical factor in driving the prediction toward class 1. Other features, such as ‘feature ~~0~~ 012‘ and ‘feature ~~0~~ 004‘, also have significant positive contributions. 



**Fig. 5** Feature Contributions to a Class 1 Prediction 

Despite the presence of some negative contributions, the cumulative positive contributions dominate the prediction. As a result, the model predicts class 1 with high confidence. This chart effectively highlights the most influential features that drove the prediction toward class 1. 

## **8 Experimental Results and Discussion** 

We trained the EBM for 3 to 30 top features using Stratified K-Fold cross-validation. To assess performance, we use Precision, Recall, F1 Score, and ROC-AUC, a key metric for imbalanced datasets [61]. Table 4 shows the results. 

The ROC-AUC score of 0.983 stands out as the highest achieved during testing of the proposed model and surpasses the 0.975 reported by [6], who introduced InterpretML as an open-source Python package and utilized EBM’s default parameters in their work, highlighting the effectiveness of our approach. 

Notably, this score reaches 0.983 for the first time when utilizing the top 18 features. Reducing the number of features is crucial for minimizing model complexity and runtime, especially when working with large datasets. Table 5 shows the result of comparing the performance of EBM with other models by using top 18 features selected by EBM in training phase, which helps identify the most effective classifier. 

14 

**Table 4** Performance of EBM with Varying Number of Top Features 

|Number of Top Features Contributing<br>to the Prediction|Precision|Recall|ROC-AUC|F1 Score|
|---|---|---|---|---|
|3|0.802|0.706|0.975|0.750|
|4|0.825|0.687|0.976|0.745|
|. . .<br>16|. . .<br>0.921|. . .<br>0.763|. . .<br>0.982|. . .<br>0.833|
|17|0.915|0.770|0.982|0.833|
|18|0.917|0.763|**0.983**|0.831|
|19|0.924|0.765|0.982|0.829|
|20|0.921|0.769|0.982|0.837|
|. . .<br>30|. . . . . .<br>0.922|. . .<br>0.755|. . .<br>0.981|0.835|



**Table 5** Comparison of EBM and Other Models Using Top 18 Selected Features 

|Model|Precision|Recall|ROC-AUC|F1 Score|
|---|---|---|---|---|
|Logistic Regression|0.765|0.806|0.979|0.780|
|Random Forest|0.942|0.761|0.976|0.837|
|Decition Tree|0.699|0.810|0.924|0.746|
|XGBoost|0.806|0.822|0.977|0.814|
|EBM|0.917|0.763|0.983|0.831|



As discussed in previous sections, V21 and V22 (feature ~~0~~ 021 and feature ~~0~~ 022) exhibit a moderate degree of correlation that warrants further investigation. In our case, only V21 appears in the top 18 features and thus remains in the final model. Systematic removal did not yield further performance gains. Additionally, we observe that V12 is among the top 18 features selected by the EBM model, indicating its relevance. In contrast, V17, ranked 22nd by the EBM and excluded from the top 18 training features, does not contribute to improving the model’s performance. 

## **9 Addressing Overfitting and Model Robustness** 

To assess overfitting, the cross ~~v~~ alidate function (with return ~~t~~ rain ~~s~~ core=True) was used. The model’s average training score was 0.99858, and the average test score was 0.98185—an acceptable train-test gap of 0.01673 (1.67%). Because this gap is much smaller than a set threshold of 0.1, we conclude that the model generalizes well. The negligible gap and high test performance confirm the absence of notable overfitting. 

## **10 Conclusion and Future Work** 

This study highlights the effectiveness of EBM-driven feature selection in optimizing credit card fraud detection. By leveraging the model’s interpretability, we identified the top 18 most influential features, achieving an ROC-AUC score of 0.983 eliminating the need for all features, which would otherwise increase computational cost and model complexity. This eliminated the need for all 30 features and thereby reduced 

15 

computational costs and complexity. An EBM trained on these selected features outperformed alternative models on the same feature set, reinforcing EBM’s accuracy advantage. 

Additionally, we implemented an optimized preprocessing and hyperparameter tuning strategy leveraging the Taguchi method, which demonstrated superior efficiency and effectiveness compared to exhaustive techniques such as GridSearchCV. By systematically optimizing the sequence of preprocessing steps—including scaler selection—alongside hyperparameter configurations and feature subset selection, the Explainable Boosting Machine (EBM) achieved notable gains in predictive performance. In fact, EBM consistently outperformed several well-established models, including Logistic Regression, Random Forest, XGBoost, and Decision Tree, across key evaluation metrics. 

Due to the combinatorial nature of hyperparameter tuning, it is impractical to exhaustively evaluate all possible orthogonal arrays or to test an extensive range of parameter levels within the scope of a single study. We encourage future research to explore alternative OA configurations, potentially involving more parameters or additional levels, to assess whether further performance improvements can be achieved. 

To ensure robustness, we evaluated overfitting with cross-validation, revealing a minimal train-test gap (1.67%), indicating strong generalization capabilities. Beyond its immediate contributions, this research opens new directions in feature selection and model optimization for fraud detection and other imbalanced classification problems. The interpretability of EBM can be further assessed in various datasets and domains, and the Taguchi method may find broader application in machine learning workflows. 

While EBMs do not support online learning, future work could explore adapting them for real-time fraud detection through periodic mini-batch retraining. This approach allows efficient integration of new data while maintaining historical patterns, supporting both stability and adaptability. Preliminary experiments with such incremental strategies may offer valuable insights for further optimization. In addition, state-of-the-art RL models can adapt to evolving fraud tactics as feature importance shifts, but their exploration risks and high computational costs limit practicality. 

Overall, our results establish a new benchmark in credit card fraud detection, introducing a highly effective approach to significantly enhance predictive accuracy. By reaching an ROC-AUC of 0.983, we exceed previous studies and illustrate the transformative potential of explainable AI (XAI) in financial fraud detection, offering a powerful and transparent solution for real-world applications. 

## **Acknowledgements** 

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. 

## **References** 

- [1] Dang TK, Tran TC, Tuan LM, Tiep MV. Machine Learning Based on Resampling Approaches and Deep Reinforcement Learning for Credit Card Fraud Detection Systems. Applied Sciences. 2021 Oct;11(21):10004. https://doi.org/10.3390/ 

16 

app112110004. 

- [2] Castillo M.: Why credit card fraud alerts are rising, and how worried you should be about them. Accessed 05 Sep 2025. Available from: https://www.cnbc.com/ 2024/09/12/why-credit-card-fraud-alerts-are-rising.html. 

- [3] Sanober S, Alam I, Pande S, Arslan F, Rane KP, Singh BK, et al. An Enhanced Secure Deep Learning Algorithm for Fraud Detection in Wireless Communication. Wireless Communications and Mobile Computing. 2021 Jan;2021(1):6079582. https://doi.org/10.1155/2021/6079582. 

- [4] Xue W, Zhang J. Dealing with Imbalanced Dataset: A Re-sampling Method Based on the Improved SMOTE Algorithm. Communications in Statistics - Simulation and Computation. 2016 Apr;45(4):1160–1172. https://doi.org/10.1080/03610918. 2012.728274. 

- [5] Lou Y, Caruana R, Gehrke J, Hooker G. Accurate intelligible models with pairwise interactions. In: Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining. KDD ’13. New York, NY, USA: Association for Computing Machinery; 2013. p. 623–631. Available from: https://doi.org/10.1145/2487575.2487579. 

- [6] Nori H, Jenkins S, Koch P, Caruana R.: InterpretML: A Unified Framework for Machine Learning Interpretability. arXiv. ArXiv:1909.09223 [cs]. Available from: http://arxiv.org/abs/1909.09223. 

- [7] Alamri M, Ykhlef M. Hybrid Undersampling and Oversampling for Handling Imbalanced Credit Card Data. IEEE Access. 2024;12:14050–14060. https://doi. org/10.1109/ACCESS.2024.3357091. 

- [8] Fiore U, De Santis A, Perla F, Zanetti P, Palmieri F. Using generative adversarial networks for improving classification effectiveness in credit card fraud detection. Information Sciences. 2019 Apr;479:448–455. https://doi.org/10.1016/j.ins.2017. 12.030. 

- [9] Dornadula VN, Geetha S. Credit Card Fraud Detection using Machine Learning Algorithms. Procedia Computer Science. 2019;165:631–641. https://doi.org/10. 1016/j.procs.2020.01.057. 

- [10] Pundkar SN, Zubei M. Credit Card Fraud Detection Methods: A Review. E3S Web of Conferences. 2023;453:01015. Publisher: EDP Sciences. https://doi.org/ 10.1051/e3sconf/202345301015. 

- [11] Rtayli N, Enneya N. Enhanced credit card fraud detection based on SVMrecursive feature elimination and hyper-parameters optimization. Journal of Information Security and Applications. 2020 Dec;55:102596. https://doi.org/10. 1016/j.jisa.2020.102596. 

17 

- [12] Zhu M, Zhang Y, Gong Y, Xu C, Xiang Y.: Enhancing Credit Card Fraud Detection A Neural Network and SMOTE Integrated Approach. arXiv. Version Number: 1. Available from: https://arxiv.org/abs/2405.00026. 

- [13] Afriyie JK, Tawiah K, Pels WA, Addai-Henne S, Dwamena HA, Owiredu EO, et al. A supervised machine learning algorithm for detecting and predicting fraud in credit card transactions. Decision Analytics Journal. 2023 Mar;6:100163. https://doi.org/10.1016/j.dajour.2023.100163. 

- [14] Abdul Salam M, Fouad KM, Elbably DL, Elsayed SM. Federated learning model for credit card fraud detection with data balancing techniques. Neural Computing and Applications. 2024 Apr;36(11):6231–6256. https://doi.org/10.1007/ s00521-023-09410-2. 

- [15] Esenogho E, Mienye ID, Swart TG, Aruleba K, Obaido G. A Neural Network Ensemble With Feature Engineering for Improved Credit Card Fraud Detection. IEEE Access. 2022;10:16400–16407. https://doi.org/10.1109/ACCESS. 2022.3148298. 

- [16] Sundarkumar GG, Ravi V. A novel hybrid undersampling method for mining unbalanced datasets in banking and insurance. Engineering Applications of Artificial Intelligence. 2015 Jan;37:368–377. https://doi.org/10.1016/j.engappai.2014. 09.019. 

- [17] Gupta P, Varshney A, Khan MR, Ahmed R, Shuaib M, Alam S. Unbalanced Credit Card Fraud Detection Data: A Machine Learning-Oriented Comparative Study of Balancing Techniques. Procedia Computer Science. 2023;218:2575–2584. https://doi.org/10.1016/j.procs.2023.01.231. 

- [18] Praveen Mahesh K, Ashar Afrouz S, Shaju Areeckal A. Detection of fraudulent credit card transactions: A comparative analysis of data sampling and classification techniques. Journal of Physics: Conference Series. 2022 Jan;2161(1):012072. https://doi.org/10.1088/1742-6596/2161/1/012072. 

- [19] Lucas Y, Jurgovsky J.: Credit card fraud detection using machine learning: A survey. arXiv. ArXiv:2010.06479 [cs]. Available from: http://arxiv.org/abs/2010. 06479. 

- [20] Lokanan ME. Predicting Money Laundering Using Machine Learning and Artificial Neural Networks Algorithms in Banks. Journal of Applied Security Research. 2024 Jan;19(1):20–44. Publisher: Routledge. https://doi.org/10.1080/19361610. 2022.2114744. 

- [21] Leevy JL, Johnson JM, Hancock J, Khoshgoftaar TM. Threshold optimization and random undersampling for imbalanced credit card data. Journal of Big Data. 2023 May;10(1):58. https://doi.org/10.1186/s40537-023-00738-z. 

18 

- [22] Strelcenia E, Prakoonwit S. Improving Classification Performance in Credit Card Fraud Detection by Using New Data Augmentation. AI. 2023 Jan;4(1):172–198. https://doi.org/10.3390/ai4010008. 

- [23] Tanaka FHKdS, Aranha C.: Data Augmentation Using GANs. arXiv. Version Number: 1. Available from: https://arxiv.org/abs/1904.09135. 

- [24] Ba H.: Improving Detection of Credit Card Fraudulent Transactions using Generative Adversarial Networks. arXiv. Version Number: 1. Available from: https://arxiv.org/abs/1907.03355. 

- [25] Li Z, Huang M, Liu G, Jiang C. A hybrid method with dynamic weighted entropy for handling the problem of class imbalance with overlap in credit card fraud detection. Expert Syst Appl. 2021 Aug;175(C). https://doi.org/10.1016/j.eswa. 2021.114750. 

- [26] Carcillo F, Le Borgne YA, Caelen O, Bontempi G. Streaming active learning strategies for real-life credit card fraud detection: assessment and visualization. International Journal of Data Science and Analytics. 2018 Jun;5(4):285–300. https://doi.org/10.1007/s41060-018-0116-z. 

- [27] Salekshahrezaee Z, Leevy JL, Khoshgoftaar TM. The effect of feature extraction and data sampling on credit card fraud detection. Journal of Big Data. 2023 Jan;10(1):6. https://doi.org/10.1186/s40537-023-00684-w. 

- [28] Abakarim Y, Lahby M, Attioui A. An Efficient Real Time Model For Credit Card Fraud Detection Based On Deep Learning. In: Proceedings of the 12th International Conference on Intelligent Systems: Theories and Applications. Rabat Morocco: ACM; 2018. p. 1–7. Available from: https://dl.acm.org/doi/10.1145/ 3289402.3289530. 

- [29] Zou J, Zhang J, Jiang P.: Credit Card Fraud Detection Using Autoencoder Neural Network. arXiv. Version Number: 1. Available from: https://arxiv.org/abs/1908. 11553. 

- [30] Pumsirirat A, Yan L. Credit Card Fraud Detection using Deep Learning based on Auto-Encoder and Restricted Boltzmann Machine. International Journal of Advanced Computer Science and Applications (ijacsa). 2018;9(1). Publisher: The Science and Information (SAI) Organization Limited. https://doi.org/10.14569/ IJACSA.2018.090103. 

- [31] Du H, Lv L, Guo A, Wang H. AutoEncoder and LightGBM for Credit Card Fraud Detection Problems. Symmetry. 2023 Apr;15(4):870. https://doi.org/10. 3390/sym15040870. 

- [32] Tingfei H, Guangquan C, Kuihua H. Using Variational Auto Encoding in Credit Card Fraud Detection. IEEE Access. 2020;8:149841–149853. https://doi.org/10. 

19 

1109/ACCESS.2020.3015600. 

- [33] Mienye ID, Sun Y. A Deep Learning Ensemble With Data Resampling for Credit Card Fraud Detection. IEEE Access. 2023;11:30628–30638. https://doi.org/10. 1109/ACCESS.2023.3262020. 

- [34] Najadat H, Altiti O, Aqouleh AA, Younes M. Credit Card Fraud Detection Based on Machine and Deep Learning. In: 2020 11th International Conference on Information and Communication Systems (ICICS); 2020. p. 204–208. ISSN: 2573-3346. Available from: https://ieeexplore.ieee.org/document/9078935. 

- [35] G´omez JA, Ar´evalo J, Paredes R, Nin J. End-to-end neural network architecture for fraud scoring in card payments. Pattern Recognition Letters. 2018 Apr;105:175–181. https://doi.org/10.1016/j.patrec.2017.08.024. 

- [36] Aziz LAR, Andriansyah Y. The role artificial intelligence in modern banking: an exploration of AI-driven approaches for enhanced fraud prevention, risk management, and regulatory compliance. Reviews of Contemporary Business Analytics. 2023;6(1):110–132. 

- [37] Sahin Y, Bulkan S, Duman E. A cost-sensitive decision tree approach for fraud detection. Expert Systems with Applications. 2013 Nov;40(15):5916–5923. https: //doi.org/10.1016/j.eswa.2013.05.021. 

- [38] Jain V, Agrawal M, Kumar A. Performance Analysis of Machine Learning Algorithms in Credit Cards Fraud Detection. In: 2020 8th International Conference on Reliability, Infocom Technologies and Optimization (Trends and Future Directions) (ICRITO). Noida, India: IEEE; 2020. p. 86–88. Available from: https://ieeexplore.ieee.org/document/9197762/. 

- [39] Chhabra Roy N, Prabhakaran S. Sustainable response system building against insider-led cyber frauds in banking sector: a machine learning approach. Journal of Financial Crime. 2023 Jan;30(1):48–85. https://doi.org/10.1108/ JFC-12-2021-0274. 

- [40] Carcillo F, Le Borgne YA, Caelen O, Kessaci Y, Obl´e F, Bontempi G. Combining unsupervised and supervised learning in credit card fraud detection. Information Sciences. 2021 May;557:317–331. https://doi.org/10.1016/j.ins.2019.05.042. 

- [41] Leevy JL, Hancock J, Khoshgoftaar TM. Comparative analysis of binary and one-class classification techniques for credit card fraud data. Journal of Big Data. 2023 Jul;10(1):118. https://doi.org/10.1186/s40537-023-00794-5. 

- [42] Venkata Suryanarayana S, N Balaji G, Venkateswara Rao G. Machine Learning Approaches for Credit Card Fraud Detection. International Journal of Engineering & Technology. 2018 Jun;7(2):917. https://doi.org/10.14419/ijet.v7i2. 9356. 

20 

- [43] Islam MA, Uddin MA, Aryal S, Stea G. An ensemble learning approach for anomaly detection in credit card data with imbalanced and overlapped classes. Journal of Information Security and Applications. 2023 Nov;78:103618. https: //doi.org/10.1016/j.jisa.2023.103618. 

- [44] Nami S, Shajari M. Cost-sensitive payment card fraud detection based on dynamic random forest and k -nearest neighbors. Expert Systems with Applications. 2018 Nov;110:381–392. https://doi.org/10.1016/j.eswa.2018.06.011. 

- [45] Hastie TJ, Tibshirani RJ. Generalized Additive Models. CRC Press; 1990. Google-Books-ID: qa29r1Ze1coC. 

- [46] Lou Y, Caruana R, Gehrke J. Intelligible models for classification and regression. In: Proceedings of the 18th ACM SIGKDD international conference on Knowledge discovery and data mining. KDD ’12. New York, NY, USA: Association for Computing Machinery; 2012. p. 150–158. Available from: https: //doi.org/10.1145/2339530.2339556. 

- [47] Jiang L, Cheng S, Qiu J, Xu H, Chan WK, Ding Z.: Offline Reinforcement Learning with Imbalanced Datasets. arXiv. Publisher: arXiv Version Number: 3. Available from: https://arxiv.org/abs/2307.02752. 

- [48] Khadka S, Majumdar S, Nassar T, Dwiel Z, Tumer E, Miret S, et al. Collaborative evolutionary reinforcement learning. In: International conference on machine learning. PMLR; 2019. p. 3341–3350. Available from: https://proceedings.mlr. press/v97/khadka19a.html. 

- [49] Eimer T, Lindauer M, Raileanu R.: Hyperparameters in Reinforcement Learning and How To Tune Them. arXiv. Version Number: 1. Available from: https: //arxiv.org/abs/2306.01324. 

- [50] Jomaa HS, Grabocka J, Schmidt-Thieme L.: Hyp-RL : Hyperparameter Optimization by Reinforcement Learning. arXiv. Version Number: 1. Available from: https://arxiv.org/abs/1906.11527. 

- [51] Van Den Heuvel E, Zhan Z. Myths About Linear and Monotonic Associations: Pearson’s _r_ , Spearman’s _ρ_ , and Kendall’s _τ_ . The American Statistician. 2022 Jan;76(1):44–52. https://doi.org/10.1080/00031305.2021.2004922. 

- [52] Chatterjee S. A New Coefficient of Correlation. Journal of the American Statistical Association. 2021 Oct;116(536):2009–2022. https://doi.org/10.1080/ 01621459.2020.1758115. 

- [53] Dalitz C, Arning J, Goebbels S. A Simple Bias Reduction for Chatterjee’s Correlation. Journal of Statistical Theory and Practice. 2024 Dec;18(4):51. https://doi.org/10.1007/s42519-024-00399-y. 

21 

- [54] Chatterjee S, Holmes S. XICOR: Robust and generalized correlation coefficients, 2023. URL https://CRAN R-project org/package= XICOR https://github com/spholmes/XICOR;. 

- [55] Hauke J, Kossowski T. Comparison of Values of Pearson’s and Spearman’s Correlation Coefficients on the Same Sets of Data. QUAGEO. 2011 Jun;30(2):87–93. https://doi.org/10.2478/v10117-011-0021-1. 

- [56] Gu Z. Complex heatmap visualization. iMeta. 2022 Sep;1(3):e43. https://doi. org/10.1002/imt2.43. 

- [57] Akinwande MO, Dikko HG, Samson A. Variance Inflation Factor: As a Condition for the Inclusion of Suppressor Variable(s) in Regression Analysis. Open Journal of Statistics. 2015;05(07):754–767. https://doi.org/10.4236/ojs.2015.57075. 

- [58] O’brien RM. A Caution Regarding Rules of Thumb for Variance Inflation Factors. Quality & Quantity. 2007 Sep;41(5):673–690. https://doi.org/10.1007/ s11135-006-9018-6. 

- [59] Marcoulides KM, Raykov T. Evaluation of Variance Inflation Factors in Regression Models Using Latent Variable Modeling Methods. Educational and Psychological Measurement. 2019 Oct;79(5):874–882. Publisher: SAGE Publications Inc. https://doi.org/10.1177/0013164418817803. 

- [60] Kaustav Sarkar.: Book Review #3: A Primer on the Taguchi Method. Publisher: Unpublished. Available from: http://rgdoi.net/10.13140/RG.2.2.21506.84163. 

- [61] Brownlee J. Imbalanced Classification with Python: Better Metrics, Balance Skewed Classes, Cost-Sensitive Learning. Machine Learning Mastery; 2020. Available from: https://books.google.com/books?id=jaXJDwAAQBAJ. 

22 

