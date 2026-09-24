---
title: "SHAP-Based Feature Selection for Enhanced Unsupervised Labeling"
authors: "Mary Anne Walauskis, Taghi M. Khoshgoftaar"
year: 2025
venue: "IEEE Access (Vol. 13)"
domain: "XAI & Feature Selection in Credit Card Fraud"
pdf_path: "docs/papers\2025_walauskis_shap_feature_selection_unsupervised_fraud_labeling.pdf"
---

# SHAP-Based Feature Selection for Enhanced Unsupervised Labeling

**Authors:** Mary Anne Walauskis, Taghi M. Khoshgoftaar  
**Venue / Date:** IEEE Access (Vol. 13) (2025)  
**Domain Focus:** XAI & Feature Selection in Credit Card Fraud  
**Original PDF:** [`2025_walauskis_shap_feature_selection_unsupervised_fraud_labeling.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2025_walauskis_shap_feature_selection_unsupervised_fraud_labeling.pdf)

---



Received 21 June 2025, accepted 18 July 2025, date of publication 22 July 2025, date of current version 28 July 2025. _Digital Object Identifier 10.1109/ACCESS.2025.3591554_ 

# SHAP-Based Feature Selection for Enhanced Unsupervised Labeling 

MARY ANNE WALAUSKIS , (Graduate Student Member, IEEE), AND TAGHI M. KHOSHGOFTAAR, (Life Member, IEEE) 

College of Engineering and Computer Science, Florida Atlantic University, Boca Raton, FL 33431, USA 

Corresponding author: Mary Anne Walauskis (mwalauskis2022@fau.edu) 

- **ABSTRACT** Manual dataset labeling is expensive, time-consuming, and susceptible to noise and inaccuracies, often necessitating significant financial investments with risks of inconsistencies from human annotations. These challenges are further extended in domains such as fraud detection because of privacy concerns due to manual annotations and severe class imbalance, which negatively impact machine learning models. Our unsupervised approach integrates SHapley Additive exPlanations (SHAP) for feature selection with our novel unsupervised labeling method which uses an ensemble unsupervised method in conjunction with a percentile-based threshold technique on the widely used Kaggle Credit Card Fraud Detection dataset. We create subsets with three and five features using unsupervised SHAP-based feature selection to determine the most impactful features, as well as use the full-featured dataset. To evaluate, we compare the newly generated binary class labels to the actual labels, which were only used for evaluation, and calculate Matthews Correlation Coefficient (MCC), Jaccard Index (JI), and Precision. Furthermore, we compare our method to an unsupervised baseline and show significant improvements. Our empirical results demonstrate that unsupervised SHAP-based feature selection consistently improves the quality of our labels, when compared to the baseline unsupervised method. Lastly, unsupervised SHAP-based feature selection improves label quality when comparing feature subsets to the full-feature dataset while reducing computational complexity. Our work provides an unsupervised framework capable of addressing the challenges of labeling highly imbalanced and unlabeled data while preserving data privacy concerns given the unsupervised nature of our methodology and application of unsupervised SHAP-based feature selection. 

**INDEX TERMS** Credit card fraud detection, feature selection, label generation, SHAP, unsupervised learning. 

## **I. INTRODUCTION** 

Acquiring quality labels is a common challenge in machine learning. Labeling data is often resource-intensive, costly, prone to errors, and full of inconsistencies [1]. Quality of labels is an important factor as noise and inaccurate labels undermine reliability of models [2]. Moreover, a large proportion of new data remains unlabeled, partially due to factors such as cost and the necessity of domain knowledge. In general, machine learning models often perform better with more data [2]; however, in domains such as medical 

The associate editor coordinating the review of this manuscript and approving it for publication was Wei Wei . 

diagnostics and fraud, the absence of class labels limits the applicability of commonly used supervised models which are dependent on labeled data. A concern over privacy only exacerbates this issue, as labeling often requires human expert involvement, and limits the public availability of these types of datasets [3]. Furthermore, in domains such as fraud, machine learning practitioners face the challenge of class imbalance, as the majority of transactions are legitimate with only a small portion representing fraud, which further complicates the challenge of generating labels. Our novel unsupervised labeling method aims to provide a robust solution to mitigate these challenges, as evidenced by our empirical results, demonstrating a significant improvement 

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. 

For more information, see https://creativecommons.org/licenses/by/4.0/ 

130098 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



over a widely used unsupervised learner which served as our baseline comparison. 

Unsupervised approaches to data labeling offer a promising alternative as they eliminate the need for human annotation by leveraging the dataset’s features to generate labels. However, the difficulty with unsupervised approaches is that they typically do not perform as well as supervised approaches [4], especially when there is significant class imbalance. In domains such as fraud, accurately identifying fraudulent transactions is imperative, as misclassification of a legitimate transaction as fraudulent results in unnecessary investigations, incurring additional cost and wasting valuable resources. 

Yet another challenge facing machine learning in label generation is the size of the dataset [5]. Supervised and unsupervised methods are computationally expensive when applied to large and big data. However, feature selection has emerged as a powerful data reduction technique to manage computational expense when dealing with large and big data [6]. Feature selection also plays a beneficial role when the data has significant class imbalance by identifying and retaining only the most relevant features making it more human readable and interpretable [6]. Our work integrates feature selection with our unsupervised labeling technique to address these challenges, and empirical results demonstrate the effectiveness of feature selection to further improve our unsupervised labeling methods results. 

Specifically, we employ SHapley Additive exPlanations (SHAP) [7] for our feature selection. Typically, the feature selection process is supervised; however, our work is entirely unsupervised, so we needed to apply a feature selection method that is able to be used in an unsupervised manner. SHAP is a robust method which provides a ranking of each feature’s importance and can be applied regardless of whether the data is labeled or unlabeled. First, an unsupervised learner, Isolation Forest (IF), was trained on the dataset, the SHAP explainer was configured using this model and dataset without class labels, and SHAP values were calculated to quantify the contribution each feature makes in that model’s predictions. The higher the SHAP value, the more impactful the feature. To determine whether SHAP feature selection improves the quality of our newly generated labels, we apply it to a widely used and publicly available Credit Card Fraud Detection dataset [8], which are real credit card transactions from September 2013. To the best of our knowledge, this is the only publicly available credit card fraud dataset, specifically focused on credit card fraud data, and it represents a large dataset with over 280,000 real transactions. 

Using unsupervised SHAP to perform feature selection, we create two datasets, which contain only a subset of the original features. For our study, we selected the top three and five features for our datasets after evaluating multiple feature selection levels (3, 5, 7, 9, 10, 13, and 15), where three and five features consistently had the highest evaluation metrics. Additionally, we used the original 

dataset, which has 29 features, for a total of three datasets. We then apply our unsupervised labeling methodology to each of the datasets. To assess the label quality produced by our unsupervised labeling method, we want to evaluate our labels compared to an unsupervised baseline; however, to the best of our knowledge, there is not an entirely unsupervised labeling method. Because of this, we chose Isolation Forest [9] as our unsupervised baseline comparison, as it is widely used and appropriate for large and big data. IF has been shown to outperform other unsupervised learning methods (e.g., Gaussian Mixture Model, k-Nearest Neighbors [10]). IF offers low computational complexity and high accuracy making well-suited for large data [11]. Additionally, IF avoids some of the unpredictability that can be associated with clustering algorithms [12]. Therefore, we also apply IF to each of the three datasets to serve as our unsupervised baseline labeling method. The unsupervised anomaly detection method serves only as a baseline to measure the quality of our generated labels. We then compare each SHAP feature selection dataset to the full dataset to evaluate the impact of SHAP with our unsupervised labeling method as well as compare each dataset to the unsupervised baseline, IF. We provide empirical results which demonstrate SHAP improves label quality over the baseline approach as well as using all features. Thus, we successfully demonstrate that unsupervised SHAP-based feature selection is able to reduce computational complexity while improving label quality. 

Fraud detection also illustrates the broader challenge of anomaly detection in which rare patterns, like fraudulent transactions, need to be identified within a majority of legitimate or normal data. The term fraud encompasses many activities such as credit card fraud, healthcare fraud, identity theft all of which leave the victims with emotional distress and financial loss [13], [14]. In the United States alone, credit card fraud affects nearly sixty percent of card holders with annual losses exceeding a staggering five billion dollars [15]. This highlights the importance of advancements in machine learning, particularly unsupervised methods, which can address challenges such as class imbalance, the absence of labels, and the need to process large volumes of data to classify instances as either normal (legitimate, in the case of fraud) or anomalous (fraudulent, in the case of fraud). Our work aims to provide a solution which is able to generate new binary labels in an unsupervised manner while minimizing computational cost by effectively employing unsupervised SHAP-based feature selection to reduce the number of features. 

The major contributions of our work include an improved version of our original unsupervised labeling method [16], which no longer labels only a subset of instances and relies on a Random Forest classifier to label the remaining instances. Instead, our revised approach [17] now labels every instance without a Random Forest step, thus reducing computational complexity and simplifying the overall algorithm. Our 

130099 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



novel unsupervised framework generates binary class labels for highly imbalanced datasets by combining clustering with a percentile-based thresholding mechanism, thereby eliminating manual threshold tuning and expert-defined rules. Furthermore, our manuscript introduces the addition of unsupervised SHAP-based feature selection prior to labeling, which further reduces computational costs and improves evaluation metrics. We also introduce direct evaluation of label quality (rather than training a supervised learner) to save time and resources, and to avoid the bias-variance trade-off introduced by dataset-model interactions. Finally, we provide empirical validation on the highly imbalanced Credit Card Fraud Detection dataset, demonstrating that our method consistently and significantly outperforms the stateof-the-art unsupervised baseline (Isolation Forest) across metrics such as Matthews Correlation Coefficient (MCC), Jaccard Index, and Precision, using both the full feature set and reduced subsets derived from SHAP rankings. Lastly, we conduct an analysis of how varying the number of positive (fraudulent) instances impacts label quality, which highlights the robustness and adaptability of our approach. Collectively, these contributions advance automated labeling techniques and highlight the potential of our approach to improve machine learning applications in domains burdened by challenges of unlabeled data and class imbalance. 

The remainder of this paper is organized as follows. Section II presents current literature relating to unsupervised labeling and SHAP applications while highlighting the novelty of our work within these domains. In Section III, we present a in-depth explanation of our unsupervised labeling methodology with unsupervised SHAP-based feature selection. Section IV provides details relating to our experiment and label evaluation as well as the baseline used for comparison. We present our empirical results in Section V. Lastly, in Section VI, we conclude our paper with discussions of future work and applications of our methodology. 

## **II. RELATED WORKS** 

The presented works concentrate on the application of SHapley Additive exPlanations (SHAP) in the contexts of feature selection, class label generation and evaluation, as well as methodologies specifically designed for fraud detection tasks, particularly within imbalanced and large datasets, and the incorporation of SHAP into varying methods. For instance, Hancock et al. [18] demonstrate its utility in both supervised and unsupervised environments. Furthermore, SHAP is integrated into broader strategies for anomaly detection and classification. Although SHAP has proven effective in data reduction and improving model performance, its role within completely unsupervised frameworks is still an emerging field of interest. The methodologies examined display a variety of dependency on labeled data, with some employing techniques such as pseudo-labeling, supervised models, or ensemble methods. This section emphasizes relevant studies that utilize SHAP 

alongside other techniques for feature selection, labeling, and fraud detection, and demonstrates our approach as an unsupervised method that utilizes SHAP for feature selection to produce high-quality binary labels without the necessity of ground truth labels. 

Ghaheri et al. [19] propose a machine learning-based approach for early diagnosis of Parkinson’s disease (PD) using voice recordings as the primary data source. Their method employs Pearson Correlation Coefficients (PCCs) to select features most correlated with PD outcomes, which are then ranked using SHAP to assess importance. These selected features are used as input for four classifiers: XGBoost, LightGBM, Gradient Boosting, and Bagging. A Hard Voting Ensemble technique, weighted by classifier importance, determines the final prediction through majority voting. However, their method relies on labeled data and supervised models, which may not generalize well to entirely unlabeled or imbalanced datasets. In contrast, our method offers a fully unsupervised binary labeling approach that applies SHAP-based feature selection prior to any labeling. By ranking and retaining only the most important features without relying on class labels, our method reduces computational complexity and enhances scalability for large, imbalanced datasets. Unlike Ghaheri et al.’s reliance on supervised models, our method generates labels independently of prior training, providing a more robust solution when labeled data is scarce. 

Park and Lee [20] utilize SHAP-driven pseudo-labeling in their proposed advanced mixing-based text data augmentation approach, which incorporates explainable artificial intelligence (XAI) to enhance the pseudo-labeling process. Their method calculates the importance of words using explainability scores derived from SHAP. Due to the inherent uncertainty in pseudo-labels, they combine pseudo-labels with original ground-truth labels during training. Similarly, our method leverages SHAP to improve labeling; however, unlike their approach, ours employs an entirely unsupervised SHAP process. While their method relies on a pre-trained model for SHAP and considers pseudo-labels alongside original labels during training, our approach is fully unsupervised and does not require original labels to determine the final label for each instance. 

Liu et al. [21] employed SHAP for feature selection on the UCI Parkinson’s disease dataset, integrating SHAP values with four classifiers: Deep Forest, Extreme Gradient Boosting, Light Gradient Boosting Machine, and Random Forest. SHAP values were calculated for individual features using these classifiers, and the effectiveness of SHAP-based feature selection was compared against traditional filterbased methods, including F-score, ANOVA-F, and Mutual Information. Unlike their approach, which relies on supervised models to compute SHAP values and applies feature selection only to the training dataset, our method applies SHAP in an entirely unsupervised manner across the full dataset before labeling. By employing SHAP to rank feature importance without any reliance on class labels or predefined 

130100 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



training and testing splits, our approach ensures the labeling process is entirely independent of prior supervised learning steps. 

Jiang et al. [22] propose an anomaly detection framework for credit card fraud detection using an unsupervised attentional anomaly detection network (UAAD-FDNet). Their method trains the model exclusively on non-fraudulent transactions, treating fraud detection as an anomaly detection problem. The network incorporates a generator and discriminator, where the generator uses an autoencoder with channel-wise feature attention to reconstruct input features while learning latent representations. Similarly to our work, they use the Kaggle Credit Card Fraud Detection dataset; however, while the training process is unsupervised, the data preparation requires labels to isolate non-fraudulent transactions, making the approach partially supervised unlike our method which is entirely unsupervised. Additionally, they use feature attention whereas we use feature selection which maintains all instances but reduces complexity by only keeping the most important features. 

Babu and Pratap [23] use the Kaggle Credit Card Fraud dataset to train a convolutional neural network (CNN) capable of labeling unseen transactions. While their method demonstrates better performance, it depends on the availability of ground truth labels during training of the CNN given that CNNs are supervised learners. In contrast, our fully unsupervised approach successfully labels the Kaggle credit card dataset without relying on original labels. Additionally, Babu and Pratap [23] primarily evaluate their labeling method using accuracy, a metric that is less suitable for imbalanced datasets like the Credit Card Fraud dataset, as it can be misleading [24]. We have similar objection to Naby et al. [25] given they used a supervised approach and accuracy to evaluate their results. On the other hand, our method evaluates the quality of newly generated labels using a direct method by calculating Precision, Matthews Correlation Coefficient, and Jaccard Index, which are well-established for assessing imbalanced datasets [26], [27]. 

The related works presented differ significantly from our approach in multiple ways. First, while many employ SHAP for feature selection or labeling, as seen in [20] and [21], these methods rely on supervised components, such as pretrained models or original labels, which requires labeled data. In contrast, our method applies SHAP in a completely unsupervised manner and labels without the need for pre-labeled data. Second, some approaches, such as [22], require partially supervised data preparation, such as isolating non-fraudulent transactions, which is not required in our process, rather we are able to take both the fraudulent and non-fraudulent transactions and determine whether they are fraudulent or not. Third, methods like [23] and [25] depend on accuracy as their evaluation metric, which is less reliable for imbalanced datasets [24]. Our method mitigates these limitations by using metrics such as Precision, Matthews Correlation Coefficient, and Jaccard Index to 

directly evaluate the quality of labels. These methods have been validated for their reliability on imbalanced data [27]. Lastly, the method introduced by [22] incorporates feature attention with their unsupervised approach to assign greater weight to more important features. In contrast, we utilize SHAP feature selection with our unsupervised labeling method, identifying and retaining only the most significant features. Our approach not only considers feature importance but also reduces computational complexity, unlike feature attention, making it more scalable and efficient for large, imbalanced datasets. 

## **III. METHODOLOGY** 

This paper presents a novel method for generating binary class labels for large data with significant class imbalance. Unlike traditional methods, our method leverages unsupervised learning components as part of the labeling process, reducing the need for domain expertise by automatically identifying structure in the data. This unsupervised framework allows our approach to be easily applied to a wide range of real-world datasets, such as the Kaggle Credit Card Fraud dataset, where labeled data is scarce and domain knowledge can be limited or costly. We integrate two labeling strategies: an ensemble of three unsupervised methods implemented using the scikit-learn library [28] and a percentile-gradient based approach. The data points in the intersection of the two labeling strategies form a subset, which we use to create confidence intervals. Through experimentation, we found the instances in the subset are consistently well-labeled. The confidence intervals are then used to select which positively labeled instances in the whole dataset should be labeled as positive in the final labeling. 

## _A. PREPROCESSING THE DATASET_ 

Feature vectors are normalized using scikit-learn’s normalize function [29], which scales each feature such that its Euclidean norm (L2 norm) equals 1. This standardization maintains the relative proportions of the data while ensuring that all features contribute equally, preventing features with larger scales from disproportionately influencing the results and enhancing classification performance [30]. 

Following normalization, the dataset is randomized by shuffling the rows using pandas’ sample method [31] with _frac_ = 1, which includes all rows in a reshuffled order. A random state (42) is applied to ensure the randomized order is consistent across trial runs. Additionally, to manage computational resources, the normalized and shuffled dataset is divided into smaller chunks of up to 25,000 rows. The total number of chunks is determined by dividing the dataset size by the chunk size and rounding up to ensure all rows are included. Chunking is particularly beneficial for handling large datasets, as it enables sequential processing of smaller portions, reducing memory consumption, and improving computational efficiency. The chunking approach is important in the context of our unsupervised method, 

130101 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



as the methodology employs three unsupervised algorithms. By processing manageable data portions, the methodology ensures scalability and efficient resource utilization, allowing large scale datasets to be processed more efficiently, reducing memory usage and improving computational performance [32]. 

## _B. ENSEMBLE UNSUPERVISED LABEL GENERATION METHOD (EUM)_ 

To gain insight about the unlabeled dataset, an initial set of labels are generated during this section of our labeling method. Using the normalized and chunked datasets from the preprocessing phase, three unsupervised algorithms: KMeans, Spectral Clustering (SC), and Gaussian Mixture Model (GMM) are employed. 

KMeans is a widely used clustering algorithm due to its simplicity and computational efficiency. It partitions a dataset into k-clusters by iteratively minimizing the sum of squared distances between points and their cluster centroids. However, KMeans assumption of spherical clusters can limit effectiveness on complex or non-linearly separable data causing the algorithm to misinterpret true cluster configuration [33]. 

Spectral Clustering (SC) with Nystroem Approximation is effective for large-scale datasets [34]. SC clusters data by partitioning a similarity graph based on the Laplacian eigenvectors, but constructing and decomposing the similarity matrix (or adjacency matrix) can be computationally expensive for large datasets. The Nystroem approximation addresses this by approximating the graph eigenvectors using a subset of the data, reducing computational cost while maintaining clustering outcomes [34]. 

Gaussian Mixture Models (GMM) offer a probabilistic clustering approach by modeling data as a mixture of Gaussian distributions. Each cluster is represented by a Gaussian component with its own mean and covariance matrix. Using the Expectation-Maximization (EM) algorithm, GMM iteratively refines the parameters and assigns probabilities to each point for belonging to a cluster. This soft clustering approach enables GMM to identify complex patterns and overlapping clusters effectively [35]. 

Adopting an ensemble approach allows us to overcome limitations presented by individual unsupervised algorithms. Combining the ensemble unsupervised approach with the preprocessing steps, described in Section III-A, we are able to explore patterns and cluster structures in large data. We force the clusters to two to align with the requirements of binary classification. This setup a simple assignment of labels to each instance, thereby supporting our binary labeling objective. Even though these unsupervised algorithms are not designed for direct labeling, our ensemble approach adapts the capabilities to effectively achieve this goal. For each algorithm (KMeans, SC, and GMM), we set n_clusters to two and random_state to zero. For KMeans, n_init is set to ‘‘auto’’, and for SC, affinity is set to ‘‘Nearest 



**FIGURE 1.** Label matrix example with predicted labels. 

Neighbor’’. Spectral clustering often struggles with large datasets due to high computational and memory demands. To overcome this, the Nystroem method, a sampling-based technique, approximates large positive semi-definite matrices by selecting a representative subset of data points [36]. scikit-learn’s implementation controls the approximation’s dimensionality via the default value for n_components [37]. 

In a post-processing step, the outputs of the algorithms are combined to create a label matrix, as shown in Figure 1, which records the label given by KMeans, SC and, and GMM for each instance. Lastly, a majority vote is applied to determine a single label for each instance. Given that our goal is binary class labeling, we assign a positive label (1) to the minority cluster and negative label (0) to the majority cluster. As an example, in Figure 1, the first row would be labeled as positive (1) while the last two rows would be labeled at negative (0). 

## _C. PERCENTILE GRADIENT LABEL GENERATION METHOD (PGM)_ 

Using the output of the EUM labeling portion, a calculation is taken to quantify the difference in the median between the positive and negative classes, for each feature. The determination is whether the positive class, generally, has larger or smaller values than the negative class. This calculation is detailed in Section III-D. From this determination, PGM generates a labeled dataset based on statistical thresholds and majority voting. 

A label matrix is created with the goal of identifying feature-based patterns in the normalized version of the dataset. Binary labels, for each column, are given based on statistical thresholds. Specifically, if the feature values for the positive class are expected to be larger, the 97th percentile is used as a threshold, and data points with values exceeding this threshold are labeled as 1. Conversely, if smaller values are expected for the positive class, the 3rd percentile is used, and data points below this threshold are labeled as 1. All other data points are labeled as 0. This process generates a matrix where each column represents a feature and each row contains varying combinations of binary labels, as described in Algorithm 1. 

A majority-voting technique is applied to each instance within the matrix so that each instance has a single binary label. A threshold, determined as a fixed fraction (0.009) of the total number of features, is used to classify rows. This threshold is adjustable, but through experimentation with a variety of datasets, the fixed value of 0.009 has performed effectively. Instances whose count of 1s exceeds the threshold 

130102 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



**Algorithm 1** Percentile Gradient Label Matrix Creation for <u>Imbalanced Data</u> 

- 1: **Input:** DataFrame _df_ 

- 2: **Output:** DataFrame _label_  matrix_ 

- 3: _label_  matrix_ ← empty dataframe with the same index as _df_ 

- 4: _temp_  labels_ ← empty list 

- 5: **for** each column _col_ in _df_ **do** 

- 6: **if** Positive class has higher medians **then** 

- 7: _threshold_ ← 97th percentile of _df_ [ _col_ ] 8: _temp_  labels.append_ (( _df_ [ _col_ ] _> threshold_ ) _.astype_ ( _int_ )) 

- 9: **else** 

10: _threshold_ ← 3rd percentile of _df_ [ _col_ ] 11: _temp_  labels.append_ (( _df_ [ _col_ ] _< threshold_ ) _.astype_ ( _int_ )) 

- 12: **end if** 

- 13: **end for** 

14: _label_  matrix_ ← concatenate _temp_  labels_ along columns 

- 15: **Return** _label_  matrix_ 

are assigned a final label of 1, while all others are assigned 0. In other words, the threshold determines the minimum number of positive labels (1s) required for a row in the label matrix to be assigned a positive label. 

The majority vote first calculates the threshold by multiplying the total number of feature columns by 0.009. For each row in the label matrix, the number of ones is counted. If this count exceeds the threshold, the row is labeled as 1; otherwise, it is labeled as 0. This process results in a fully labeled dataset. 

## _D. INSTANCE MINIMIZATION FOR EUM AND PGM_ 

Our focus for this portion is minimizing the number of positive instances overall while capturing the highest number of true positive (actual fraud) instances. The minimization technique described is applied to both the labeled datasets produced by EUM and PGM. 

Using the initial labels generated by the EUM technique, Section III-B, we compare the median values of features for the positive and negative classes by calculating the differences in feature distributions between the two classes. The positive class is the class of interest, as in our dataset it represents fraudulent transactions. Note, this is the same class calculation mentioned in Section III-C. First, the dataset is separated by class, and the median is calculated for each feature within the two classes, excluding the class label column. Then, the medians are compared to identify the number of features where one class has a higher median value than the other. By counting the number of features for which the positive class has a higher median value, we can determine which class demonstrates higher values, in terms of median values. Additionally, a Boolean indicator ( _class_ _1 is_  larger_ referred to in Algorithm 1) is assigned to specify whether the positive class has a greater number of features with 



**FIGURE 2.** Venn diagram of dataset subsets. 

higher medians than negative class. This is an important determination as it becomes a key piece of information when minimizing the instances, specifically the positive instances. 

The minimization technique, defined in Algorithm 2, is applied to both datasets labeled by the EUM and PGM methods. The aim of this technique is to reduce the number of instances labeled as positive under the assumption of class imbalance, where fraudulent instances are expected to be rare. The technique is intended to balance the instances labeled as positive while preserving as many potential true positive instances as possible. It is important to note, there are no ground-truth labels used during this process. The goal of this technique is to minimize false positives, given the real-world implications of misclassifying a legitimate transaction as fraud wastes time and resources. The determination of true or false to _class_ _1 is_  larger_ defines the relabeling process, as described in Step 6 of Algorithm 2. If _class_ _1 is_  larger_ is false, the top 95% of rows labeled 0 remain unchanged, and the bottom 5% are relabeled as 1, with the remaining rows staying labeled as 0. For rows labeled 1, the top 1% remain 1, and the rest are relabeled as 0. If _class_ _1 is_  larger_ is true, the process is reversed: the bottom 95% of rows labeled 0 remain unchanged, and the top 5% are relabeled as 1. Among rows labeled 1, the bottom 1% stay labeled 1, while the others are relabeled as 0. This reduces false positives in the original labeling from EUM and PGM. 

## _E. CONFIDENT LABEL CREATION_ 

Confident Labels (CL), which are a subset of the full dataset, are formed from the minimized datasets produced by EUM and PGM, from Section III-D. Instances that are present at the intersection between the two and share the same predicted label are selected as the instances for the CL dataset. Illustrated in Figure 2, this subset captures instances to help to determine the final positives instances to be kept, as outlined in Section III-F. 

## _F. CONTROLLING POSITIVE INSTANCES_ 

Declaration of the desired number of positives, _p_ , is the final step in the labeling process. Given that negative instances are easier to predict, as they are the majority class, the focus of the final labeling adjustment is centered around the 

130103 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



**Algorithm 2** Data Transformation and Relabeling Process 

- 1: **Input** : Dataframe with newly generated class label. 

- 2: **Output** : Transformed dataset with updated labels. 3: **Step 1** : **Sort Rows by Class** 

- 4: Sort the dataframe by the newly generated class label to group rows by labels (0 or 1). 

- 5: **Step 2** : **Split Data by Class** 6: Create two subsets: 7: Class 0: Rows where newly generated label = 0. 

- 8: Class 1: Rows where newly generated label = 1. 9: **Step 3** : **Compute Row Sums** 

- 10: For each subset, calculate the row-wise sum of feature values. 

- 11: **Step 4** : **Sort Rows by Row Sum** 

- 12: Sort Class 0 in descending order of the row-wise sum. 13: Sort Class 1 in ascending order of the row-wise sum. 14: **Step 5** : **Define Thresholds for Relabeling** 15: Compute: 

- 16: Class 0 dataframe: Top 95% of rows. 17: Class 0 dataframe: Bottom 5% of rows excluding the top 95%. 

- 18: Class 1 dataframe: Bottom 1% of rows. 19: **Step 6** : **Relabel Rows** 

- 20: If _class_ _1 is_  larger_ was determined to be false 21: Keep highest-ranked 95% of rows in Class 0 dataframe unchanged. 

- 22: Relabel lowest-ranked 5% of rows in Class 0 dataframe as 1. 

- 23: Select the rest of the rows in Class 0 dataframe and keep label as 0. 

- 24: Keep highest-ranked 1% of rows in Class 1 dataframe unchanged. 

- 25: Relabel remaining rows in Class 1 dataframe as 0. 

- 26: If _class_ _1 is_  larger_ was determined to be true 

- 27: Keep lowest-ranked 95% of rows in Class 0 dataframe unchanged. 

- 28: Relabels highest-ranked 5% of rows in Class 0 dataframe as 1. 

- 29: Select the rest of the rows in Class 0 dataframe and keep label as 0. 

- 30: Keep lowest-ranked 1% of rows in Class 1 dataframe unchanged. 

- 31: Relabel remaining rows in Class 1 dataframe as 0. 32: **Step 7** : **Combine Transformed Data** 

- 33: Concatenate all transformed subsets into a single dataframe. 

count of the positive instances. Once _p_ has been declared, if there are enough positive instances from the minimized PGM method (mPGM), only those instances are considered for final labeling as positive with any additional unused being relabeled as negative. In the case where mPGM does not have enough positive instances to fill _p_ , a selection of the negative instances are kept and relabeled as positive. 

The CLs from Section III-E are used to create confidence intervals, which are created for each feature from the positive labeled instances. If _p_ is less than or equal to the positives in the mPGM dataset, only the labeled positive instances are considered. If _p_ is greater than the positives in the mPGM dataset, additional instances labeled as negative are also considered, which is described below. The fully labeled mPGM separates instances by class (0 and 1). For each positive instance (1), the method checks if feature values fall within their corresponding confidence intervals. Values within the confidence intervals are labeled as 1; otherwise, they are labeled as 0. Once this has been done for all features and instances, the count of features within the confidence intervals is calculated. This results in a total for each instance, with the instances then sorted by the count of ones in each row. Using the predetermined total for the positive count per row, rows are added until the desired number of positives, _p_ , is reached. Any remaining unused rows are then relabeled as zero. At this step, all instances are labeled, and the final labeling of the dataset is complete. 

When _p_ exceeds the available positives in the labeled mPGM dataset, all positive instances are retained, and additional instances labeled as 0 are used to meet the required value of _p_ . Negative instances are sorted using the previously described technique, and the top instances are relabeled as 1 until the desired count of positives is reached. Any remaining unused rows retain their original label of 0. This process completes the final labeling of the dataset. 

## **IV. EXPERIMENTAL DESIGN AND DATASETS** 

Our experiments are designed to evaluate both the quality of our method’s newly generated labels, as well as the quality of labels generated after applying unsupervised feature selection on imbalanced fraud data. We start by using SHAP to select the top three and five features for our dataset. As noted in Section I, our selection of three and five features was determined after experimentation with varying feature selection levels, with three and five consistently yielding the highest evaluation metrics. With the inclusion of the original dataset with full features, we have three datasets, each using only the features available for each respective dataset to generate positive (fraudulent) or negative (legitimate) class labels. After generating the new class labels, we compare the newly generated labels to the ground truth labels. It is important to note that the ground truth labels were only used for evaluation not labeling. Lastly, we compare our results with that of an unsupervised baseline trained using the same three datasets, which allows us to effectively evaluate the efficacy of our labels with and without feature selection. 

## _A. FRAUD DATASET_ 

This dataset [8], widely used for fraud detection, provides binary class labels to distinguish fraudulent transactions from legitimate ones. To the best of our knowledge, this is the only publicly available dataset of its kind, concentrating exclusively on credit card fraud data, and has a substantial number 

130104 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



**TABLE 1.** Credit card fraud detection dataset class characteristics. 

of instances. It was created through a collaboration between Worldline, a leading payment processing company, and the Université Libre de Bruxelles. The dataset comprises over 280,000 European credit card transactions recorded between September 1st and September 30th, 2013. Each transaction is characterized by 30 features: anonymized variables ‘‘V1’’ through ‘‘V28’’, along with ‘‘Time’’ and ‘‘Amount’’. The ‘‘V’’ features were anonymized and transformed using PCA by the original researchers. Furthermore, the ‘‘Time’’ feature has been omitted, as prior studies have shown it lacks meaningful predictive value [38]. 

As typical in fraud detection data, this dataset exhibits significant class imbalance, with negative instances (legitimate transactions) significantly outnumbering positive instances (fraudulent transactions). Table 1 provides further details about the dataset. While the dataset includes class labels, these are solely used as ground truth for evaluating the efficacy of our unsupervised labeling methodology. During the label generation process, the original labels are not used. 

During the unsupervised SHAP feature selection process, the features are ranked from most important to least important. Thus, indicators for fraudulent transactions are more evident in the features listed first. Based on our SHAP analysis, the ranked features are as follows in descending order of importance: ‘‘Amount’’, ‘‘V13’’, ‘‘V12’’, ‘‘V15’’, ‘‘V19’’, ‘‘V24’’, ‘‘V6’’, ‘‘V11’’, ‘‘V9’’, ‘‘V3’’, ‘‘V26’’, ‘‘V18’’, ‘‘V25’’, ‘‘V17’’, ‘‘V16’’, ‘‘V4’’, ‘‘V1’’, ‘‘V20’’, ‘‘V5’’, ‘‘V14’’, ‘‘V28’’, ‘‘V8’’, ‘‘V22’’, ‘‘V27’’, ‘‘V7’’, ‘‘V10’’, ‘‘V23’’, ‘‘V21’’, ‘‘V2’’. The top 3 features for the CC - SHAP 3 dataset are ‘‘Amount’’, ‘‘V13’’, and ‘‘V12’’. The top 5 features for the CC - SHAP 5 dataset are ‘‘Amount’’, ‘‘V13’’, ‘‘V12’’, ‘‘V15’’, and ‘‘V19’’, see Table 1. 

## _B. MEASURING LABEL QUALITY_ 

Our labeling method is applied after SHAP feature selection and does not omit any instances. As can be seen in Table 1, the number of features changes, but the number of instances and level of class imbalance remains the same. Direct evaluation of the newly generated binary class labels avoids the biases stemming from dataset-classifier interactions, ensuring a more consistent and reliable assessment of label quality. The quality of the labels generated by our method are compared against the quality of those produced by the unsupervised baseline Isolation Forest (IF). It is important to note, ground truth labels were used solely for evaluation. Our empirical results demonstrate that the proposed approach significantly outperforms the baseline across all feature subsets, producing higher quality labels. 

Binary labeling methods often evaluate the quality of labels indirectly by training a supervised model and assessing its performance; however, this approach has limitations, as the choice of technique introduces a bias-variance trade-off and can lead to inconsistent results [39]. We overcome this challenge by directly assessing the quality of the labels generated by our method. By directly evaluating the newly generated labels, we can easily interpret the validity of our labeling method. By calculating true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN), and using metrics such as Precision, Jaccard Index (JI), and Matthews Correlation Coefficient (MCC), our approach directly evaluates the efficacy of the labels themselves since the goal is producing accurate and reliable labels. This enables effective evaluation and validation of the labels both with and without SHAP feature selection. 

## _C. LABEL EVALUATION METRICS_ 

Precision, Matthews Correlation Coefficient (MCC), and Jaccard Index (JI) are used to assess the quality of labels generated by unsupervised methods such as the one presented in this paper. Based on confusion matrix results of true positive (TP), false positive (FP), true negative (TN), and false negative (FN), the newly generated labels are compared to the ground truth labels to calculate these metrics. The combination of these metrics provides a comprehensive evaluation by quantifying how well the generated labels align with ground truth labels for severely imbalanced datasets [40], [41], [42], [43]. 

Precision, defined in Equation 1, measures the proportion of correctly identified positive labels among all predicted positives, making it particularly valuable when false positives carry high costs, as in fraud detection, as a small number of false positive instances can result in diminished trust in the system as well well considerable resource expenditure [40]. Similarly, Matthews Correlation Coefficient (MCC), defined in Equation 2, evaluates all confusion matrix categories, offering a balanced and reliable metric for binary classification tasks, particularly in imbalanced datasets [40], [43], [44]. The Jaccard Index (JI), defined in Equation 3, quantifies the overlap between generated and ground-truth labels, focusing on positive class predictions and accounting for false positives and false negatives. This makes JI well-suited for imbalanced datasets and a robust measure of prediction alignment [27], [42]. In using multiple evaluation metrics, we ensure a comprehensive and fair assessment of label quality by capturing different aspects of labeled outcomes. 









130105 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



## _D. BASELINE COMPARISON_ 

To assess the impact of SHAP feature selection on generating binary labels with our labeling method, we compared the labels to an unsupervised baseline. However, to the best of our knowledge, no fully automated and entirely unsupervised labeling method currently exists. Therefore, we selected Isolation Forest (IF) [9], a widely recognized unsupervised anomaly detection method, as our unsupervised baseline because of its suitability for large datasets. Among state-of-the-art unsupervised methods, IF has demonstrated performance comparable to alternatives such as One-Class SVM (OCSVM) and Local Outlier Factor (LOF) [45]. However, unlike these methods, which may suffer from scalability issues due to their computational complexity, IF maintains high accuracy while offering significantly lower computational complexity, making it a suitable selection for large and big data [11], [46]. IF has demonstrated superior performance compared to other unsupervised learners [10], higher accuracy with low computational complexity [11], and has been shown to avoid the unpredictability of clustering algorithms [12]. We compared the labels generated by our approach with those produced by the Isolation Forest (IF) algorithm for each SHAP dataset with 3 and 5 features, as well the original dataset, which has 29 features. Using Isolation Forest from the scikit-learn library [28], we set the contamination rate to ‘‘auto’’, which is the default value. We compare the labels produced by our method to those from IF and find that our approach consistently yields higherquality labels. 

## _E. EXPERIMENTAL SETUP_ 

We begin by applying the SHAP feature selection technique to the credit card fraud detection dataset to determine feature importance in an unsupervised manner. Using SHAP, we generate two datasets: one with the top five features, and one with the top three features as well as use the original dataset with all 29 features, resulting in three total datasets. Subsequently, our unsupervised labeling technique is applied to each dataset to evaluate the impact of feature selection on the generated class labels for fraud detection. For each feature subset, the method is configured to produce labeled datasets with positive class counts of 500, 600, 700, 800, 900, and 1000. The initial value of 500 was chosen to reflect an estimated class ratio of approximately 0.002, guided by domain expertise and experimentation. This process results in 18 datasets, which are evaluated using the label evaluation methodology described in Section IV-B. 

Additionally, labels are generated using Isolation Forest (IF), which serves as our unsupervised baseline method, is applied to each original unlabeled dataset. The results from the datasets with and without SHAP feature selection are compared against the corresponding IF results, assessing the combined impact of feature selection and the proposed labeling method. The labels generated by IF are evaluated using the same methodology employed for assessing the 

**TABLE 2.** Metrics across feature subsets and positive class counts. 



**TABLE 3.** Baseline Isolation Forest (IF) metrics. 



newly generated binary class labels from our method. While both SHAP feature selection and our labeling technique rely exclusively on dataset features to generate feature importance and class labels, the original class labels are preserved for each instance and used solely to calculate MCC, JI, and Precision for evaluation. 

## **V. RESULTS AND ANALYSIS** 

The two key determinations to be considered are: (1) SHAP feature selection to significantly improve the labeling when compared to an unsupervised baseline learner, and (2) evidence that SHAP feature selection, in conjunction with our unsupervised labeling method, significantly improves label quality when comparing the reduced number of features to the full-featured dataset as well as reducing computational complexity when dealing with large and big data given the reduction of features. We present the Matthews Correlation Coefficient (MCC), Jaccard Index (JI), and Precision results for six levels of positives and three levels of feature selection, one of which is the full features for our labeling method, as shown in Table 2. Table 3 shows the corresponding results from our baseline unsupervised method, IF, across varying number of features. 

Without feature selection (using all 29 features) as shown in Table 2, our labeling method results in MCC values diminishing slightly from 500 to 700 and increasing from 700 to 1000. Our MCC values range from 0.2489 to 

130106 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



0.3077 while the baseline, IF, results in an MCC value of 0.1751. Additionally, JI values decreased from 500 to 700 and increased from 700 to 1000. With a minimum value of 0.1407 and maximum value of 0.1702, for our method, whereas IF resulted in a JI value of 0.0385. Lastly, we compare Precision, which shows similar results. Our labeling method resulted in a minimum value of 0.2100 and maximum value of 0.2800 while IF has a Precision value of only 0.0388. Our method clearly outperforms the baseline across all evaluation metrics. 

Using only the top three features, as shown in Table 2, we can see MCC is fairly consistent from 500 to 1000 though slightly increasing from 500 to 800 and slightly decreasing from 800 to 1000, and the MCC value at 1000 is greater than the value at 500. This is fairly consistent around 0.3347 since, with each addition of an additional 100 positive instances, the number of true positives is steadily increasing. For Jaccard Index, a similar pattern emerges though the increase is from 500 to 700 with a slight diminishment in values from 700 to 1000. Lastly, Precision has its peak at 500 with diminishing values up to 1000. However, each significantly outperforms the baseline, IF, across all metrics. The mean MCC for our labeling method with three features is 0.3347 while IF is 0.0435. For both Jaccard Index and Precision, IF has values of 0.0068, while our method is 0.1959 and 0.2777, respectively. Thus, this demonstrates a clear improvement over the baseline. Additionally, when comparing the evaluation metrics for three features compared to twenty-nine features, again there is a clear improvement, which demonstrates the application of SHAP improves our labeling method while reducing complexity. The mean values across all levels of positives for three features are 0.3347, 0.1959, and 0.2777 for MCC, JI, and Precision, respectively. On the other hand, the mean values across all levels of positives for the full-featured dataset are 0.2780, 0.1576, and 0.2301 for MCC, JI, and Precision, respectively. This further highlights the improvement in label quality achieved through unsupervised SHAP-based feature selection. 

Using only the top five features, as shown in Table 2, we observed MCC has a peak value of 0.3780 at 500, which gradually diminished as the positive count neared 1000. As positives were incrementally added, the initial number of true positives (fraudulent transactions) identified was significantly higher than the trials with three and twentynine features. For example, the peak value for three features is 0.3397, at 800 total positive count, and twenty-nine features is 0.3077, at 1000 total positive count, whereas the peak value for five features is 0.3780 at 500 total positive instances. However, despite the larger initial number of true positives, the incremental growth in true positives did not keep pace with the overall increase in total positives added. Similarly to the results from the top three features selected, all metrics for five features, MCC, JI, and Precision, were significantly higher than the baseline, IF. Using SHAP feature selection in conjunction with our labeling method, resulted in mean values for MCC, JI, and Precision of 0.3675, 

0.2193, and 0.3057, respectively. Meanwhile, IF resulted in values for MCC, Jaccard Index, and Precision of 0.1009, 0.0147, and 0.0147, respectively, demonstrating a significant improvement of our method with SHAP feature selection compared to the baseline. Additionally, we compare metrics for five features and the full-featured dataset. The five feature dataset has mean values of 0.3675, 0.2193, and 0.3057 for MCC, JI, and Precision, respectively compared to 0.2780, 0.1576, and 0.2301 for MCC, JI, and Precision, respectively for twenty-nine features. Again, it is evident that SHAP-based feature selection improves our label quality. 

As evidenced, our labeling method outperformed the baseline across all metrics with and without SHAP feature selection. An important consideration is how SHAP feature selection affects our method’s ability to achieve significantly improved label metric results with fewer features. With SHAP feature selection for both the top three and five features, across all metrics, unsupervised SHAP-based feature selection significantly improved the labeling results; however, five features have the best results overall. Lastly, a key point is that unsupervised feature selection did not degrade the quality of the labels generated by our unsupervised labeling method but rather improved the quality, as evidenced by the metrics in Table 2; however, IF was negatively impacted by feature selection. 

## **VI. CONCLUSION** 

The abundance of unlabeled data, coupled with the expense of manual annotation, point to the need for reliable unsupervised labeling methods. Our work addresses this challenge by leveraging an ensemble-based unsupervised approach and a percentile thresholding technique to assign binary labels without the need for ground-truth labels. Moreover, our unsupervised labeling method is able to effectively handle common challenges present in real-world applications, such as severe class imbalance and large data. 

This study thoroughly evaluates the improvements achieved by employing an unsupervised feature selection technique, SHAP, in the context of a highly imbalanced Credit Card Fraud Detection datasets. The SHAP feature selection method, which ranks feature importance without requiring class labels, is used to create two datasets with varying numbers of the top features. Additionally, we use the full featured version of the dataset. These datasets are then processed by our unsupervised labeling technique to generate class labels. The proposed approach effectively addresses the challenges of large, unlabeled datasets with significant class imbalance while reducing the number of required features, which in turn minimizes computational complexity, all within a fully unsupervised framework. 

To the best of our knowledge, this is the first work to combine unsupervised SHAP-based feature selection with an automated clustering and thresholding labeling method for unlabeled data. We calculate MCC, JI, and Precision to measure the quality of the newly generated labels and compare the results to both an unsupervised baseline and 

130107 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



the full-feature dataset. We demonstrate its state-of-the-art performance by quantifying substantial gains in MCC, JI, and Precision over a widely used unsupervised baseline. Our empirical results demonstrate that combining our unsupervised labeling method with SHAP-based feature selection significantly enhances label quality. The top 5 features selected by SHAP consistently produce the highest quality labels, outperforming those generated using all features and the baseline. A limitation of our current approach is that it is not yet a fully automated framework, as we set the number of positive instances. Future work will focus on developing data-driven techniques to select the optimal number of positive instances and threshold parameters without any domain expertise. Additionally, we will validate scalability and performance on additional large and big datasets across a variety of domains to demonstrate the generalizability of our method. 

## **REFERENCES** 

- [1] C. Gao, M. Goswami, J. Chen, and A. Dubrawski, ‘‘Classifying unstructured clinical notes via automatic weak supervision,’’ in _Proc. 7th Mach. Learn. Healthcare Conf._ , Aug. 2022, pp. 673–690. [Online]. Available: https://proceedings.mlr.press/v182/gao22a.html 

- [2] J. Shen, Z. Li, Y. Lu, M. Pan, and X. Li, ‘‘Mitigating the impact of mislabeled data on deep predictive models: An empirical study of learning with noise approaches in software engineering tasks,’’ _Automated Softw. Eng._ , vol. 31, no. 1, p. 33, Apr. 2024, doi: 10.1007/s10515-024-00435-y. 

- [3] T. Fredriksson, D. I. Mattos, J. Bosch, and H. Olsson, ‘‘Data labeling: An empirical investigation into industrial challenges and mitigation strategies,’’ in _Product-Focused Software Process Improvement_ . Cham, Switzerland: Springer, 2020, pp. 202–216. 

- [4] J. Xie, R. Girshick, and A. Farhadi, ‘‘Unsupervised deep embedding for clustering analysis,’’ in _Proc. Int. Conf. Mach. Learn._ , 2015, pp. 478–487. 

- [5] J. Fan, F. Han, and H. Liu, ‘‘Challenges of big data analysis,’’ _Nat. Sci. Rev._ , vol. 1, no. 2, pp. 293–314, Jun. 2014, doi: 10.1093/nsr/nwt032. 

- [6] J. Li, K. Cheng, S. Wang, F. Morstatter, R. P. Trevino, J. Tang, and H. Liu, ‘‘Feature selection: A data perspective,’’ _ACM Comput. Surv._ , vol. 50, no. 6, pp. 1–45, Dec. 2017, doi: 10.1145/3136625. 

- [7] S. M. Lundberg and S. Lee, ‘‘A unified approach to interpreting model predictions,’’ in _Proc. Adv. Neural Inf. Process. Syst._ , 2017, pp. 4765–4774. 

- [8] Kaggle. (2018). _Credit Card Fraud Detection_ . [Online]. Available: https://www.kaggle.com/mlg-ulb/creditcardfraud 

- [9] F. T. Liu, K. M. Ting, and Z. Zhou, ‘‘Isolation forest,’’ in _Proc. 8th IEEE Int. Conf. Data Mining_ , May 2008, pp. 413–422. 

- [10] K. T. Vasudev, M. M. M. Pai, and R. M. Pai, ‘‘Comparative analysis of generic outlier detection techniques,’’ in _Data Analytics and Learning_ , D. S. Guru, N. V. Kumar, and M. Javed, Eds., Singapore: Springer, 2024, pp. 117–126. 

- [11] C. Shao, X. Du, J. Yu, and J. Chen, ‘‘Cluster-based improved isolation forest,’’ _Entropy_ , vol. 24, no. 5, p. 611, Apr. 2022. [Online]. Available: https://www.mdpi.com/1099-4300/24/5/611 

- [12] R. Gelbard, O. Goldman, and I. Spiegler, ‘‘Investigating diversity of clustering methods: An empirical comparison,’’ _Data Knowl. Eng._ , vol. 63, no. 1, pp. 155–166, Oct. 2007. [Online]. Available: https://www. sciencedirect.com/science/article/pii/S0169023X07000031 

- [13] U.S. Department of Justice. _Criminal Resource Manual: 976. Health Care Fraud Generally_ . Accessed: Jan. 16, 2025. [Online]. Available: https://www.justice.gov/archives/jm/criminal-resource-manual-976health-care-fraud-generally 

- [14] Bureau of Justice Statistics. (2021). _Victims of Identity Theft, 2021_ . [Online]. Available: https://bjs.ojp.gov/press-release/victims-identitytheft-2021 

- [15] (2024). _Credit Card Fraud Report_ . [Online]. Available: https://www. security.org/digital-safety/credit-card-fraud-report/ 

- [16] M. A. Walauskis and T. M. Khoshgoftaar, ‘‘Confident labels: A novel approach to new class labeling and evaluation on highly imbalanced data,’’ in _Proc. IEEE 36th Int. Conf. Tools Artif. Intell. (ICTAI)_ , Oct. 2024, pp. 232–239. 

- [17] M. A. Walauskis and T. M. Khoshgoftaar, ‘‘Unsupervised label generation for severely imbalanced fraud data,’’ _J. Big Data_ , vol. 12, no. 1, p. 63, Mar. 2025, doi: 10.1186/s40537-025-01120-x. 

- [18] J. Hancock, T. M. Khoshgoftaar, and Q. Liang, ‘‘A problem-agnostic approach to feature selection and analysis using SHAP,’’ _J. Big Data_ , vol. 12, no. 1, p. 12, Jan. 2025. 

- [19] P. Ghaheri, H. Nasiri, A. Shateri, and A. Homafar, ‘‘Diagnosis of Parkinson’s disease based on voice signals using SHAP and hard voting ensemble method,’’ _Comput. Methods Biomech. Biomed. Eng._ , vol. 27, no. 13, pp. 1858–1874, Oct. 2024, doi: 10.1080/10255842.2023.226 3125. 

- [20] J. Park and Y. Lee, ‘‘Advanced pseudo-labeling approach in mixing-based text data augmentation method,’’ _Pattern Anal. Appl._ , vol. 27, no. 4, p. 129, Sep. 2024, doi: 10.1007/s10044-024-01340-6. 

- [21] Y. Liu, Z. Liu, X. Luo, and H. Zhao, ‘‘Diagnosis of Parkinson’s disease based on SHAP value feature selection,’’ _Biocybern. Biomed. Eng._ , vol. 42, no. 3, pp. 856–869, Jul. 2022. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S0208521622000638 

- [22] S. Jiang, R. Dong, J. Wang, and M. Xia, ‘‘Credit card fraud detection based on unsupervised attentional anomaly detection network,’’ _Systems_ , vol. 11, no. 6, p. 305, Jun. 2023. [Online]. Available: https://www.mdpi.com/20798954/11/6/305 

- [23] A. M. Babu and A. Pratap, ‘‘Credit card fraud detection using deep learning,’’ in _Proc. IEEE Recent Adv. Intell. Comput. Syst. (RAICS)_ , Dec. 2020, pp. 32–36. 

- [24] J. Li, R. J. Stones, G. Wang, Z. Li, X. Liu, and K. Xiao, ‘‘Being accurate is not enough: New metrics for disk failure prediction,’’ in _Proc. IEEE 35th Symp. Reliable Distrib. Syst. (SRDS)_ , Sep. 2016, pp. 71–80. 

- [25] A. A. El Naby, E. El-Din Hemdan, and A. El-Sayed, ‘‘Deep learning approach for credit card fraud detection,’’ in _Proc. Int. Conf. Electron. Eng. (ICEEM)_ , Jul. 2021, pp. 1–5. 

- [26] J.-G. Gaudreault and P. Branco, ‘‘Empirical analysis of performance assessment for imbalanced classification,’’ _Mach. Learn._ , vol. 113, no. 8, pp. 5533–5575, Aug. 2024. [Online]. Available: https://link.springer. com/article/10.1007/s10994-023-06497-5 

- [27] Y. Zhou, H. Yan, J. Wang, Z. Chen, and A. Ma, ‘‘Knowledge transferbased network from medium and high-resolution SAR imagery for built-up extraction with class-imbalanced data,’’ in _Proc. SAR Big Data Era (BIGSARDATA)_ , Sep. 2023, pp. 1–4. 

- [28] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay, ‘‘Scikit-learn: Machine learning in Python,’’ _J. Mach. Learn. Res._ , vol. 12, pp. 2825–2830, Oct. 2011. 

- [29] Scikit-Learn Developers. (2024). _Sklearn.Preprocessing.Normalize_ . Accessed: Dec. 2, 2024. [Online]. Available: https://scikit-learn. org/1.5/modules/generated/sklearn.preprocessing.normalize.html 

- [30] L. de Amorim, G. Cavalcanti, and R. Cruz, ‘‘The choice of scaling technique matters for classification performance,’’ _Appl. Soft Comput._ , vol. 133, Jan. 2023, Art. no. 109924, doi: 10.1016/j.asoc.2022.109924. 

- [31] (2024). _Pandas.Dataframe.Samples—Pandas Documentation_ . Accessed: Dec. 2, 2024. [Online]. Available: http://pandas.pydata.org/ docs/reference/api/pandas.DataFrame.sample.html 

- [32] Y. Zhu, W. Jiang, and G. Alonso, ‘‘Efficient tabular data preprocessing of ML pipelines,’’ 2024, _arXiv:2409.14912_ . 

- [33] G. Venkata Nikhil Sai, R. Aulia Tubagus, V. Rohith, and H. Donavalli, ‘‘Comparative analysis of kmeans technique on non convex cluster,’’ _Int. J. Innov. Sci. Res. Technol._ , vol. 9, no. 10, pp. 2546–2552, Oct. 2024, doi: 10.38124/ijisrt/ijisrt24oct1507. 

- [34] Q. Zhan and Y. Mao, ‘‘Improved spectral clustering based on Nyström method,’’ _Multimedia Tools Appl._ , vol. 76, no. 19, pp. 20149–20165, Oct. 2017, doi: 10.1007/s11042-017-4566-4. 

- [35] E. Patel and D. S. Kushwaha, ‘‘Clustering cloud workloads: K- means vs Gaussian mixture model,’’ _Proc. Comput. Sci._ , vol. 171, pp. 158–167, Jan. 2020. [Online]. Available: https://www.sciencedirect. com/science/article/pii/S1877050920309820 

- [36] F. Pourkamali-Anaraki, ‘‘Scalable spectral clustering with Nyström approximation: Practical and theoretical aspects,’’ _IEEE Open J. Signal Process._ , vol. 1, pp. 242–256, 2020, doi: 10.1109/OJSP.2020.3039330. 

- [37] Scikit Learn Developers. (2024). _Nystroem_ . Accessed: Dec. 2, 2024. [Online]. Available: https://scikit-learn.org/stable/modules/generated/ sklearn.kernel_approximation.Nystro-em.html 

130108 

VOLUME 13, 2025 

M. A. Walauskis, T. M. Khoshgoftaar: SHAP-Based Feature Selection 



- [38] J. L. Leevy, T. M. Khoshgoftaar, and J. Hancock, ‘‘Evaluating performance metrics for credit card fraud classification,’’ in _Proc. IEEE 34th Int. Conf. Tools with Artif. Intell. (ICTAI)_ , Oct. 2022, pp. 1336–1341. 

- [39] M. Hort, Z. Chen, J. M. Zhang, M. Harman, and F. Sarro, ‘‘Bias mitigation for machine learning classifiers: A comprehensive survey,’’ _ACM J. Responsible Comput._ , vol. 1, no. 2, pp. 1–52, Jun. 2024, doi: 10.1145/3631326. 

- [40] J. Gaudreault, P. Branco, and J. Gama, ‘‘An analysis of performance metrics for imbalanced classification,’’ in _Discovery Science_ . Cham, Switzerland: Springer, 2021, pp. 67–77. 

- [41] M. A. Walauskis and T. M. Khoshgoftaar, ‘‘Choosing the right metrics: A study of performance measurement for binary classification in imbalanced and big data,’’ _Int. FLAIRS Conf. Proc._ , vol. 38, no. 1, pp. 4–6, May 2025. [Online]. Available: https://journals.flvc.org/FLAIRS/article/view/139140 

MARY ANNE WALAUSKIS (Graduate Student Member, IEEE) received the Bachelor of Science degree from Valencia College, in 2021, and the Master of Science degree from the University of West Florida, in 2022. She is currently pursuing the Ph.D. degree with Florida Atlantic University. She is a Researcher with the Department of Electrical Engineering and Computer Science, Florida Atlantic University. She has published multiple articles and made significant contributions to the field of machine learning. Her current research interest includes unsupervised labeling. 

- [42] D. Müller, I. Soto-Rey, and F. Kramer, ‘‘Towards a guideline for evaluation metrics in medical image segmentation,’’ 2022, _arXiv:2202.05273_ . 

- [43] D. Chicco and G. Jurman, ‘‘The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation,’’ _BMC Genomics_ , vol. 21, no. 1, pp. 1–13, Dec. 2020. 

- [44] B. Krawczyk, ‘‘Learning from imbalanced data: Open challenges and future directions,’’ _Prog. Artif. Intell._ , vol. 5, no. 4, pp. 221–232, Nov. 2016. [Online]. Available: https://link.springer.com/article/10.1007/s13748-0160094-0 

- [45] E. F. Agyemang, ‘‘Anomaly detection using unsupervised machine learning algorithms: A simulation study,’’ _Sci. Afr._ , vol. 26, Dec. 2024, Art. no. e02386. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/S2468227624003284 

- [46] S. M. Erfani, S. Rajasegarar, S. Karunasekera, and C. Leckie, ‘‘Highdimensional and large-scale anomaly detection using a linear one-class SVM with deep learning,’’ _Pattern Recognit._ , vol. 58, pp. 121–134, Oct. 2016. [Online]. Available: https://www.sciencedirect.com/science/ article/pii/S0031320316300267 

TAGHI M. KHOSHGOFTAAR (Life Member, IEEE) is currently a Motorola Endowed Chair Professor with the Department of Computer and Electrical Engineering and Computer Science, Florida Atlantic University, and the Director of the NSF Big Data Training and Research Laboratory. He has published more than 900 refereed journals and conference papers. His research interests include big data analytics, data mining, machine learning, security analytics, health informatics, bioinformatics, social network mining, fraud detection, and software engineering. He has served on organizing and technical program committees for various international conferences, symposia, and workshops. He is the Co-Editor-in Chief of the _Journal of Big Data_ . 

130109 

VOLUME 13, 2025 

