---
title: "Financial Tabular Data Synthesis with Large Language Models"
authors: "unknown"
year: 2024
arxiv_id: "2402.12876"
original_file: "2402.12876.pdf"
pdf_path: "docs/papers\2024_unknown_financial_tabular_data_synthesis_wi.pdf"
---

# Financial Tabular Data Synthesis with Large Language Models

**Authors:** Unknown et al.  
**Year:** 2024 | **arXiv:** [`2402.12876`](https://arxiv.org/abs/2402.12876)  
**Local PDF:** [`2024_unknown_financial_tabular_data_synthesis_wi.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2024_unknown_financial_tabular_data_synthesis_wi.pdf)

---

# **Federated Multi-Task Learning on Non-IID Data Silos: An Experimental Study** 

Suizhi Huang huangsuizhi@sjtu.edu.cn Shanghai Jiao Tong University Shanghai, China 

Yuwen Yang youngfish@sjtu.edu.cn Shanghai Jiao Tong University Shanghai, China 

Yuxiang Lu luyuxiang_2018@sjtu.edu.cn Shanghai Jiao Tong University Shanghai, China 

Shalayiding Sirejiding salaydin@sjtu.edu.cn Shanghai Jiao Tong University Shanghai, China 

Hongtao Lu htlu@sjtu.edu.cn Shanghai Jiao Tong University Shanghai, China 

## Yue Ding 

dingyue@sjtu.edu.cn Shanghai Jiao Tong University Shanghai, China 



<!-- Start of picture text -->
Data Level Client  Task<br>Client  Task<br>Domain<br>Task  Task<br>Task<br>Client<br>Task<br>Domain  Domain<br>Task  Task<br>Model Level<br>Decoder Decoder Decoder Decoder Decoder Decoder Decoder<br>A B C A B C ANY<br>TC<br>Multiple single task learning model Single-Encoder Multi-Decoder (MD) Single-Decoder (TC)<br>Optimization Algorithm Level<br>Server<br>Personalized<br>Shared<br>Client  Client  Client  Input<br>Federated Learning Algorithm Optimization FL based on parameter decoupling<br>Encoder A Encoder B Encoder C Encoder  Encoder<br><!-- End of picture text -->

### **ABSTRACT** 

The innovative Federated Multi-Task Learning (FMTL) approach consolidates the benefits of Federated Learning (FL) and MultiTask Learning (MTL), enabling collaborative model training on multi-task learning datasets. However, a comprehensive evaluation method, integrating the unique features of both FL and MTL, is currently absent in the field. This paper fills this void by introducing a novel framework, FMTL-Bench, for systematic evaluation of the FMTL paradigm. This benchmark covers various aspects at the data, model, and optimization algorithm levels, and comprises seven sets of comparative experiments, encapsulating a wide array of non-independent and identically distributed (Non-IID) data partitioning scenarios. We propose a systematic process for comparing baselines of diverse indicators and conduct a case study on communication expenditure, time, and energy consumption. Through our exhaustive experiments, we aim to provide valuable insights into the strengths and limitations of existing baseline methods, contributing to the ongoing discourse on optimal FMTL application in practical scenarios. The source code can be found on https://github.com/youngfish42/FMTL-Benchmark. 

### **CCS CONCEPTS** 

- **Security and privacy** ; • **Computing methodologies** → **Super-** 

- **vised learning** ; **Multi-task learning** ; 

### **KEYWORDS** 

Federated Learning, Multi-Task Learning, Dense Prediction 

### **1 INTRODUCTION** 

Federated Multi-Task Learning (FMTL) [36, 65], a burgeoning machine learning paradigm, facilitates collaborative model training on multi-task learning datasets of diverse sample sizes, domains, and task types while ensuring data locality. It marries the advantages of Federated Learning (FL) [28, 39] and Multi-Task Learning (MTL) [5], both extensively employed in sectors like medical imaging [2, 3, 13–15, 21, 23, 24, 27, 45], healthcare [11, 57, 60, 64], and personalized recommendations [25, 58, 59]. FMTL enables a single model to learn multiple tasks in a privacy-preserving, distributed machine learning environment, thereby inheriting and amplifying the challenges of both FL [22, 61] and MTL [10, 48, 55]. 

**Figure 1: Design of Comparative Experimental Scenarios in FMTL-Bench. Refer to (Sec. 3.2) for detailed information. Data Level** : We design seven sets of experiments to cover main data partitioning scenarios in FMTL. These scenarios consider the different numbers and types of MTL tasks from various domains that a client may train. For more details, refer to Fig. 2. **Model Level** : We examine numerous single-task learning models and MTL models, the latter based on either multi-decoder (MD) or single-decoder architectures contingent on task conditions (TC). Experiments are conducted using network backbones of different sizes. The shaded sections in the figure represent task-agnostic parameters. **Optimization Algorithm Level** : We discuss nine baseline algorithms encompassing local training, FL, MTL, and FMTL algorithms. These algorithms leverage optimization based on either model parameters or accumulated gradients. Some baselines employ a parameter decoupling strategy and use model encoder as feature extractor during the FL process. 

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY 

Yuwen Yang et al. 

Early research [16, 32, 38, 40, 52] predominantly adopted MTL’s optimization strategy for personalized federated learning (PFL) [54] contexts. In non-independent and identically distributed (Non-IID or NIID) scenarios, each client’s personalized optimization objective function was treated as an individual task, with MTL optimization methods managing task heterogeneity arising from diverse client data. Classic machine learning tasks like image classification were commonly employed. A handful of studies [4, 8, 42] have started probing more complex scenarios, aiming to allow clients to concurrently train different task types via FL. In some industrial contexts, such as autonomous driving [20], a single model must learn multiple distinct dense prediction tasks [7, 47, 56] (e.g., semantic segmentation, depth estimation, and surface normal estimation) simultaneously. The final scenario [36, 65] involves learning an MTL model within a single client, which is the focus of this article. 

However, the current research landscape of the FMTL paradigm is still in its infancy and has not fully integrated the characteristics of both FL and MTL to establish suitable scenarios and evaluation methods. The currently employed FL and MTL optimization algorithms and models are relatively simple, and there is a scarcity of experimental research to systematically comprehend FMTL task scenarios and baselines. Given growing interest in this technology, we introduce the FMTL-Bench to systematically evaluate the FMTL paradigm. Drawing from previous work on FL and MTL evaluation benchmarks [18, 27, 29, 44, 46, 55, 65], we integrated the strengths of these works to establish a comprehensive benchmark in the FMTL field, addressing data, model, and optimization algorithm levels for the first time. **Contributions** of our paper include: 

- We meticulously consider the data, model, and optimization algorithm to design seven sets of comparative experiments. 

- We amalgamate the characteristics of the two fields of multitask learning and federated learning, conduct a case study, and extensively utilize a variety of evaluation methods to assess the performance of each baseline. 

- We glean insights from comparative experiments and case analyses, and provide application suggestions for FMTL scenarios. 

**Multi-Task Learning (MTL) model level architecture design.** To reduce the number of model parameters in MTL, a “singleencoder multi-decoder” (MD) architecture [55] is often employed. 



Here, x _𝑛_ denotes the _𝑛_ -th input data, y _𝑛_ is the corresponding output, _𝜃𝑘_<sup>_𝐸_denotes the encoder parameters of the</sup><sup>_𝑘_-th client model,</sup> and _𝜃𝑘,𝑡_<sup>_𝐷_represents the decoder parameters for task</sup><sup>_𝑡_.</sup> To further reduce the number of parameters, a “single-decoder based on task conditions” (TC) architecture [37, 53] is utilized. 



In this equation, _𝜃𝑘_<sup>_𝐸_and</sup><sup>_𝜃_</sup> _𝑘_<sup>_𝐷_are encoder and decoder parameters</sup> shared among all tasks T _𝑘_ , and _𝜃𝑘,𝑡_<sup>_𝑇_are the task-specific parameters</sup> for task _𝑡_ used in the conditioning strategy. In addition to architecture design, MTL also requires a lot of optimization work from the perspective of parameters and gradients [55]. 

**Federated learning (FL) algorithm optimization level.** Parameter decoupling strategies are also frequently used in FL and FMTL scenarios to reduce communication expenses, manage with model task heterogeneity, and improve optimization performance. These strategies divide the model parameters into shared parameters _𝑢_ and personalized parameters _𝑣𝑘_ for client _𝑘_ . 



In FL scenarios, sharing feature extractors between clients [9] is common, while in FMTL scenarios, the encoder serves as a default feature extractor [4, 8]. In addition to parameter decoupling strategy, we also verified the effects of various FL, PFL, MTL, and FMTL algorithms in subsequent experiments (see Sec. 3.2.3). We have introduced the core methodology, and due to space limitations, we will not discuss in detail the nine algorithms used in this article. 

### **3 EXPERIMENT EVALUATION** 

### **2 METHODOLOGY OVERVIEW** 

Suppose we have _𝐾_ clients in total, Federated Learning (FL) [39] is an optimization process that aims to minimize a global objective function. This function is defined by model parameters _𝜃𝑘_ , local objective function L _𝑘_ , and client weights _𝑝𝑘_ . In the Federated MultiTask Learning (FMTL) scenario, each client manages a set of tasks T _𝑘_ associated with a local dataset. The global function seeks to optimize personalized models for each client as expressed in Equation 1: 



In this equation, L _𝑘_ is the local objective function. Weight _𝑝𝑘_ of client _𝐶𝑘_ in aggregation defaults to _𝐾_<sup><u>1</u>, where</sup><sup>_𝐾_is the total number</sup> of clients. Each task loss function _ℓ𝑘,𝑡_ ( _𝜃𝑘_ ) is computed over the local dataset D _𝑘_ of client _𝐶𝑘_ for task _𝑡_ in T _𝑘_ . The weights _𝑞𝑘,𝑡_ for each task _𝑡_ default to | T1 _𝑘_ |<sup>, where |T</sup><sup>_𝑘_| is the number of local tasks.</sup> 

This research aims to establish a comprehensive benchmark, referred to as FMTL-Bench, in the field of federated multi-task learning. We have designed a robust experimental setup with three key components: comparative experiment, case study, and suggestion. 

### **3.1 Experimental Setup** 

Our experiments are conducted using the PyTorch framework [43]. The hardware setup comprises a server equipped with eight NVIDIA RTX2080Ti GPUs, while memory-intensive experiments are executed on two NVIDIA RTX4080 GPUs. The design of our experimental configurations is guided by previous studies [4, 8, 26, 37, 62, 65]. **Optimization.** Model optimization is achieved using the AdamW optimizer [35], with an initial learning rate and weight decay rate of 1e-4. The batch size is set to 8. A cosine decay learning rate scheduler [34] is employed with a warm-up phase of 5 rounds. Loss functions are chosen based on the task; cross-entropy loss for semantic segmentation and human parts segmentation, and L1 loss for surface normal estimation and depth estimation. Weighted binary cross-entropy loss for edge detection and the weights for 

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY 

Federated Multi-Task Learning on Non-IID Data Silos: An Experimental Study 



<!-- Start of picture text -->
IID-1 SDMT NIID-2 SDST NIID-4 UBSDMT NIID-5 UBSDST<br>NIID-6 UBCDMT 176 176 176 176 176 0 0 0 64 136 208 280 64 0 0 0<br>(see Table 7)<br>176 176 176 176 0 176 0 0 64 136 208 280 0 136 0 0<br>IID-1 SDMT NIID-4 UBSDMT 176 176 176 176 0 0 176 0 64 136 208 280 0 0 176 0<br>(see Table 2) unbalanced (see Table 6) 176 176 176 176 0 0 0 176 64 136 208 280 0 0 0 176<br>0 1 2 3 0 1 2 3 0 1 2 3 0 1 2 3<br>NIID-3 SDHT Client Client Client Client<br>Task Depth Edge Normals Semseg Parts (P) Normals (P)<br>(see Table 2)<br>NIID-3 SDHT NIID-6 UBCDMT NIID-7 UBCDST<br>0 0 0 0 4496 0 0 0 0 0 4496<br>NIID-2 SDST unbalanced NIID-5 UBSDST 176 0 0 0 176 176 176 176 0 0 0 0 4496 0 0 0 0 4496 0<br>(see Table 3) (see Table 4) 0 176 0 0 176 176 176 176 176 176 176 176 0 176 0 0 0 0 0<br>0 0 176 0 176 176 176 176 176 176 176 176 0 0 176 0 0 0 0<br>NIID-7 UBCDST 176 176 176 176 0 0 0 176 0 0 0<br>(see Table 5) 0 0 0 176 176 176 176 176 176 176 176 176 0 0 0 0 176 0 0<br>0 1 2 3 4 5 6 7 0 1 2 3 4 0 1 2 3 4 5<br>Client Client Client<br>cross domain<br>cross domain<br>merge<br>merge<br>single task<br><!-- End of picture text -->

**Figure 2: Data Level: Relationship diagram and Data Distribution of Comparative Experiments in Federated Multi-Task Learning.** This figure presents two levels of detail regarding our comparative experiments in federated multi-task learning. ‘MT’ represents Multi-Task, ‘ST’ stands for Single-Task, and ‘HT’ denotes Hybrid-Task. ‘SD’ signifies a single domain, while ‘CD’ refers to cross-domain. ‘UB’ is an abbreviation for unbalanced quantity. **Left-hand side** : an overview of the relationships between seven groups of comparative experiments is provided. This relationship diagram encapsulates the main scenarios of independent and identically distributed (IID) and non-independent and identically distributed (NIID) federated multi-task learning. **Right-hand side** : a visualization of the training data distribution for these seven sets of comparative experiments is displayed. Each subfigure corresponds to a different comparative experiment. The horizontal axis denotes the client ID, while the vertical axis, differentiated by color, represents various types of tasks. Task types include depth estimation (‘Depth’), edge detection (‘Edge’), surface normal estimation (‘Normals’), semantic segmentation (‘SemSeg’), and human parts segmentation (‘Parts’). Dataset comes from NYUD-v2 by default, and (P) represents using the PASCAL-Context. The relative size of the scatter points signifies the number of task samples, and the center of each point corresponds to the specific number of samples. For a detailed view, please zoom in. 

positive and negative pixels are set to 0.8 and 0.2 for the NYUD-v2 dataset, and 0.95 and 0.05 for the PASCAL-Context dataset. 

We adhere to the default settings for FL, PFL, MTL, and FMTL baselines (see Sec. 3.2.3) as recommended in the original papers or source codes. The number of local training epochs is set to 4 for the NYUD-v2 dataset and 1 for the PASCAL-Context dataset, based on dataset size. Maximum number of communication rounds is capped at 100. Source code will be made available to reproduce the results. **Datasets.** Our experiments utilize the PASCAL-Context [41] and NYUD-v2 [51] datasets, both of which are widely recognized in FMTL research [4, 8]. For single-domain experiments, we employ the NYUD-v2 dataset, which includes 795 training and 654 testing images of indoor scenes. The dataset provides labels for depth estimation (‘Depth’), edge detection (‘Edge’), surface normal estimation (‘Normals’), and semantic segmentation (‘SemSeg’) tasks. In crossdomain experiments, we introduce the PASCAL-Context dataset, from which we obtain the same type of normal task (‘Normals’) as NYUD-v2 and a different type of human parts segmentation (‘Parts’). The PASCAL-Context dataset contains 4998 training images and 5105 testing images for edge detection, semantic segmentation, human parts segmentation, surface normal estimation, and saliency detection tasks. The original training set is randomly divided into each client according to the specified method. The local dataset obtained by the client is re-divided into a local training set and a test set at a ratio of 9:1. Global evaluation G-FL and local evaluation P-FL [6, 50] are conducted on the original test set and each client’s dataset, respectively. Following [26, 37, 62], we employ diverse data augmentation techniques such as random scaling, cropping, horizontal flipping, and color jittering to augment training dataset. Both training and evaluation stages incorporate image normalization. 

### **3.2 Comparative Experiments** 

Our comparative experiments comprehensively consider data, model, and optimization algorithms levels, among others. 

_3.2.1 Data Level._ We begin with the IID-1 SDMT (Single-Domain Multi-Task) experiment, an independent and identically distributed (IID) setup involving four clients, each possessing a non-overlapping dataset from the same domain for identical tasks. Motivated by the pathological partition scenario in federated learning [39], we devised the NIID-2 SDST (Single-Domain Single-Task) scenario. In this setup, each client is responsible for a distinct task, representing an extreme case of federated multi-task learning. To examine the influence of the number of tasks within a client on the outcomes, we amalgamated the clients from the IID-1 and NIID-2 scenarios, leading to the NIID-3 SDHT (Single-Domain Hybrid-Task) scenario. 

To investigate the impact of imbalanced data volume, we established the NIID-4 UBSDMT (Unbalanced Single-Domain Multi-Task) and NIID-5 UBSDST (Unbalanced Single-Domain Single-Task) scenarios, derived from the IID-1 and NIID-2 scenarios, respectively. For a comprehensive understanding of federated multi-task learning in cross-domain situations, we introduced the NIID-6 UBCDMT (Unbalanced Cross-Domain Multi-Task) and NIID-7 UBCDST (Unbalanced Cross-Domain Single-Task) scenarios. These scenarios involve clients from diverse fields, utilizing cross-domain data with unbalanced sample sizes, and exhibiting heterogeneous tasks and models. Refer to Fig. 2 for relationship diagram and visualization of training data distribution across comparative experiment groups. 

_3.2.2 Model Level._ In alignment with the conventional practice of implementing an “encoder-decoder” model architecture in multitask learning, our experimental design subscribes to this paradigm. We bifurcate the client model into the encoder and decoder. 

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY 

Yuwen Yang et al. 

**Table 1: Enumeration of multi-task learning model parameters and computational complexity (FLOPs) for clients in IID1 Single-Domain Multi-Task (SDMT) scenario from Tab. 2.** 

|Ar|BN|Encoder|<br> Decoder|Parameters<br> TC module|(M)<br>  Total|Encoder/Total|FLOPs<br>Per task|(G)<br> Total|
|---|---|---|---|---|---|---|---|---|
|MD|resnet|11.18|26.21|/|37.39|29.89%|-|272.14|
|TC|resnet|11.18|7.09|0.12|18.39|60.79%|75.47|301.88|
|MD|swin-t|27.52|52.28|/|79.80|34.49%|-|211.13|
|TC|swin-t|27.52|13.76|0.12|41.40|66.48%|71.01|284.04|



In multi-task learning, the network typically shares a single encoder across multiple tasks. For this shared encoder, we employ a lightweight structure grounded on the pre-trained ResNet-18 [17]. Additionally, we include pre-trained Swin-T [33] in our experiments for comparative analysis. This backbone network is paired with a Fully Convolutional Network and the task-specific header. 

The decoder component, on the other hand, can vary based on the architecture [55]. While the conventional “multi-decoder” (MD) architecture as Eq. (2) assigns a separate decoder to each task, we introduce an innovative “single-decoder based on task conditions” (TC) architecture [37, 53] as Eq. (3). This novel approach, applied in the context of FMTL, employs a single decoder that adjusts according to the specific conditions of each task. 

_3.2.3 Optimization Algorithm Level._ Our experimental setup deploys a suite of nine optimization algorithms, covering gradientand parameter-based strategies for MTL optimization, along with personalization and parameter decoupling strategies for FL. The baseline algorithms are categorized as follows: Firstly, the **Local** method, which solely operates on local dataset training, refraining from involvement in the federated learning process. Secondly, the **Federated Learning Method** , exemplified by FedAvg [39]. Thirdly, the category of **Personalized Federated Learning Algorithms** , encompassing FedProx [30], FedAMP [19], and FedRep [9]. Fourthly, **Multi-Task Learning Algorithms** , which includes PCGrad [63] and CAGrad [31], both underpinned by gradient optimization techniques. Finally, the **Federated Multi-Task Learning Algorithms** , comprising the FMTL methods MaT-FL [4] and FedMTL [52]. 

It is noteworthy that PCAGrad [63] and CAGrad [31] are adapted for multi-task optimization using accumulated gradients transmitted by clients during FL communication rounds. Besides, FedRep [9] and MaT-FL [4] employ a parameter decoupling strategy as Eq. (4) for optimization. By default, the model’s encoder serves as a feature extractor, and only this portion of the parameters is transmitted during the FL process. Furthermore, in the NIID-6 UBCDMT scenario from Tab. 7, due to the diversity in the number and types of tasks among different clients, the model based on the MD architecture exhibits heterogeneity. Consequently, for this scenario, FedProx, FedAMP, PCGrad, CAGrad, and the FedMTL algorithms are modified using parameter decoupling strategy. This implies that algorithms with the “-E” flag only transmit and utilize the parameters or accumulated gradient of model encoder for FL optimization. 

_3.2.4 Evaluation Criteria._ In our comparative studies, we devise evaluative indicators that comprehensively reflect the unique attributes of individual tasks, the holistic performance of multi-task learning, and the diversity of test set origins. 



<!-- Start of picture text -->
20 Global Performance with MD 20 Global Performance with TC<br>0 0<br>20 20<br>40 40<br>60 Local FedAMP CAGrad 60 Local FedAMP CAGrad<br>FedAvg Mat-FL FedRep FedAvg Mat-FL FedRep<br>FedProx PCGrad FedMTL FedProx PCGrad FedMTL<br>80 80<br>0 20 40 60 80 100 0 20 40 60 80 100<br>20 Personalized Performance with MD 20 Personalized Performance with TC<br>0 0<br>20 20<br>40 40<br>60 Local FedAMP CAGrad 60 Local FedAMP CAGrad<br>FedAvg Mat-FL FedRep FedAvg Mat-FL FedRep<br>FedProx PCGrad FedMTL FedProx PCGrad FedMTL<br>80 80<br>0 20 40 60 80 100 0 20 40 60 80 100<br>Round Round<br>Average Performance Improvement<br>Average Performance Improvement<br><!-- End of picture text -->

**Figure 3: Case Study: Average task performance improvement (** Δ% ↑ **) versus communication rounds for baselines in IID-1 SDMT scenario from Tab. 2. Please zoom in for details.** 

**Task-Specific Metrics** : Each task type is evaluated using its appropriate metric. For example, depth estimation is assessed using the Root Mean Square Error (RMSE), while the test Loss is used for edge detection. The mean error (mErr) is utilized for surface normal estimation, and the mean Intersection over Union (mIoU) is applied for both semantic segmentation and human parts segmentation. **Comprehensive Multi-Task Performance** : To provide a holistic evaluation of various algorithms, we compute weighted average per-task performance improvement [37], relative to the target local training baseline without any aggregation. The calculation is now adjusted to incorporate individual task weights: 



In this formula, _𝑁_ signifies the task count, and _𝑀_ Fed _,𝑖_ and _𝑀_ Target _,𝑖_ denote the performance of task _𝑖_ under federated learning techniques and the target local baseline, respectively. The variable _𝑙𝑖_ equals 1 when a lower metric value is desirable for task _𝑖_ , and 0 otherwise. The weight assigned to task _𝑖_ , represented by _𝑤𝑖_ , denotes the importance or priority of each task within the FMTL framework. By default, all tasks are assigned equal weight, i.e., _𝑤𝑖_ = 1/ _𝑁,_ ∀ _𝑖_ . 

### **3.3 Case Study** 

Taking advantage of the unique characteristics of both multi-task learning and federated learning, we perform a case study using a variety of evaluation methods to assess baseline performances. These evaluation methods serve as a robust means for comparing the effectiveness of various algorithms and techniques. The case study complements the comparative experiments as an essential supplement (see Sec. 3.2.4). 

_3.3.1 Additional Evaluation Criteria in the Case Study._ We have selected the IID-1 SDMT scenario in Tab. 2 as the primary focus of our case study. To meet the practical requirements of FMTL, we have structured our case study as follows: 

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY 

Federated Multi-Task Learning on Non-IID Data Silos: An Experimental Study 

**Table 2: Comparative Experiments: Single-Domain Multi-Task (SDMT) and Single-Domain Hybrid-Task (SDHT) Scenarios.** 

**Above** : SDMT (IID-1) with four Multi-Task (MT) clients using NYUD-v2. **Below** : SDHT (NIID-3) with four MT and four single-task clients using NYUD-v2. **Notations** : ‘BN’ denotes Backbone Network, ‘Algo’ represents Optimization Algorithm, ‘Ar’ signifies Architecture, and ‘OOM’ is Out of Memory. G-FL and P-FL refer to evaluations using global and local test sets, respectively. ‘↑’ indicates higher is better, ‘↓’ implies lower is better. An asterisk (*) means actual results to be multiplied by 1 _𝐸_ − 2. Values before and after ‘±’ represent the average and standard deviation of performance indicators from multiple clients. Light blue shading indicates a baseline for comparison. ‘Δ%’ denotes average per-task performance improvement relative to the target baseline. **Unless otherwise noted, subsequent tables share these notations.** Please refer to Fig. 2 for relationship diagrams and training data distribution visualizations across comparative experiments. 

|||||||G-FL<br>|||||P-FL<br>|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Scenario|BN|Algo|Ar|Depth<br>RSME*↓|Edge<br>Loss*↓|Normals<br>mErr↓|Semseg<br>mIoU↑|ΔG%↑|Depth<br>RSME*↓|Edge<br>Loss*↓|Normals<br>mErr↓|Semseg<br>mIoU↑|ΔP%↑|
||||MD|81.41±1.95|4.76±0.01|26.44±0.23|23.36±0.54|0.00|91.28±12.93|4.79±0.07|26.35±1.39|24.74±0.91|0.00|
|||Local|TC|81.34±1.47|4.80±0.01|26.72±0.34|22.14±0.27|-1.76|89.90±10.42|4.84±0.07|26.35±1.10|22.06±0.99|-2.59|
|||FdA|MD|71.10±0.13|4.77±0.00|22.96±0.01|30.01±0.08|13.52|75.76±16.96|4.80±0.07|22.69±1.23|31.67±0.92|14.67|
|||evg|TC|70.23±0.35|4.83±0.01|22.19±0.05|30.90±0.30|15.15|73.80±13.00|4.86±0.07|22.02±0.96|31.13±2.60|14.99|
|||FdP|MD|70.92±1.27|4.77±0.00|22.95±0.12|29.98±0.38|13.55|75.66±13.53|4.80±0.07|22.80±1.32|31.71±1.94|14.64|
|||erox|TC|72.04±0.21|4.80±0.00|22.55±0.04|32.99±0.19|16.65|77.82±11.43|4.83±0.08|22.31±1.00|31.80±1.46|14.44|
|||FedAMP|MD|81.30±2.58|4.75±0.00|26.47±0.24|23.49±0.45|0.20|92.24±13.78|4.79±0.07|26.41±1.25|23.55±1.39|-1.52|
||||TC|79.88±2.04|4.78±0.00|26.20±0.31|22.78±0.45|-0.03|85.18±11.53|4.82±0.07|25.86±1.43|23.12±2.08|0.34|
|||MTFL|MD|79.22±0.99|4.75±0.00|25.89±0.15|23.73±0.50|1.64|88.55±13.90|4.79±0.07|25.55±1.30|24.37±1.74|1.13|
||resnet|a-|TC|75.85±4.83|4.78±0.00|24.85±0.55|25.06±1.45|4.93|85.78±11.97|4.82±0.07|24.89±1.54|26.14±2.82|4.15|
||||MD|83.64±0.85|4.77±0.00|28.87±0.20|20.02±0.27|-6.61|90.49±12.06|4.81±0.07|28.10±1.93|20.58±1.15|-5.75|
|||PCGrad|TC|120.74±5.01|4.99±0.03|31.31±0.64|17.83±0.84|-23.81|122.00±9.23|5.02±0.09|31.05±0.85|17.50±0.85|-21.39|
||||MD|77.48±1.50|4.75±0.00|25.24±0.09|24.16±0.37|3.25|85.35±15.28|4.78±0.07|25.06±1.26|25.18±1.87|3.34|
|||CAGrad|TC|77.13±0.80|4.84±0.01|24.16±0.17|24.60±0.36|4.38|82.00±12.09|4.88±0.08|24.11±0.94|24.69±1.71|4.15|
|||FdR|MD|78.01±1.52|4.75±0.00|25.39±0.13|24.21±0.38|3.00|86.96±14.58|4.79±0.07|25.37±1.25|25.00±1.97|2.38|
|||eep|TC|74.03±1.03|4.78±0.01|24.18±0.17|26.09±0.19|7.22|79.22±15.16|4.81±0.07|24.11±1.20|26.63±2.35|7.23|
|||FedMTL|MD|81.19±1.80|4.76±0.00|26.43±0.11|23.35±0.38|0.07|91.60±13.28|4.79±0.07|26.06±1.02|24.18±1.99|-0.38|
|IID-1<br>|||TC|80.99±0.85|4.78±0.01|26.35±0.27|22.72±0.61|-0.58|81.99±2.39|4.78±0.01|26.50±0.21|22.63±0.58|0.32|
|SDMT||Local|MD|72.56±0.75|4.73±0.00|24.51±0.13|33.89±0.53|15.97|79.29±13.61|4.76±0.07|24.58±1.03|33.33±3.24|13.80|
||||TC|77.54±2.18|4.75±0.00|25.19±0.26|29.55±0.52|9.05|84.64±11.69|4.78±0.07|25.19±0.92|30.03±2.00|8.32|
|||FdA|MD|61.96±0.00|4.73±0.00|21.24±0.00|44.61±0.00|33.79|66.41±14.28|4.76±0.07|21.35±1.13|44.64±3.37|31.82|
|||evg|TC|65.82±0.15|4.76±0.00|21.14±0.01|41.94±0.05|29.68|69.09±12.07|4.78±0.07|21.17±1.06|43.33±3.25|29.83|
|||FdP|MD|62.42±0.00|4.73±0.00|21.22±0.00|44.51±0.00|33.56|65.94±13.85|4.76±0.07|21.29±1.03|43.65±2.31|31.01|
|||erox|TC|65.63±0.32|4.75±0.00|21.14±0.01|41.95±0.04|29.80|67.97±10.79|4.79±0.07|21.23±1.09|42.76±3.62|29.45|
|||FedAMP|MD|72.25±0.95|4.73±0.00|24.49±0.14|33.92±0.34|16.12|80.04±11.34|4.76±0.07|24.39±1.17|33.37±4.09|13.82|
||||TC|77.40±1.41|4.74±0.00|25.24±0.27|29.98±0.72|9.56|83.54±10.86|4.77±0.07|25.38±1.22|30.60±2.08|9.07|
||i-t|MT-FL|MD|70.29±0.51|4.73±0.01|23.99±0.09|34.74±0.28|18.07|77.41±12.33|4.76±0.07|23.82±1.01|34.01±4.06|15.72|
||swn|a|TC|74.43±3.58|4.74±0.00|24.22±0.47|32.37±1.81|13.99|81.65±12.53|4.78±0.07|24.13±0.78|31.31±2.95|11.43|
|||PCGrad|MD|109.92±2.54|4.84±0.00|26.09±0.21|28.67±0.87|-3.16|109.76±14.45|4.88±0.07|26.14±0.84|29.40±2.71|-0.62|
||||TC|93.46±7.97|4.88±0.02|26.03±0.16|31.78±0.67|5.07|100.31±17.26|4.92±0.07|26.00±0.70|30.17±2.31|2.67|
|||CAGd|MD|67.89±0.89|4.75±0.00|22.54±0.09|37.18±0.52|22.68|74.53±14.31|4.78±0.07|22.61±1.18|36.11±3.10|19.68|
|||ra|TC|74.67±4.00|4.78±0.00|22.23±0.05|35.07±0.58|18.48|79.42±13.01|4.81±0.07|22.32±0.88|35.46±2.94|17.80|
|||FdR|MD|69.79±0.59|4.73±0.01|23.80±0.07|35.24±0.19|18.94|76.98±12.73|4.76±0.07|23.97±0.99|34.92±3.25|16.62|
|||eep|TC|72.12±1.66|4.74±0.00|23.73±0.11|33.80±0.37|16.69|77.11±11.24|4.77±0.07|23.74±1.03|33.23±3.88|15.04|
|||FdMTL|MD|OOM|OOM|OOM|OOM|OOM|OOM|OOM|OOM|OOM|OOM|
|||e|TC|77.34±1.51|4.75±0.00|25.17±0.18|30.03±0.41|9.64|81.42±11.29|4.78±0.07|25.17±0.96|30.11±1.40|9.30|
|||Local||81.50±0.81|4.75±0.00|26.47±0.17|23.58±1.06|0.21|82.44±10.02|4.80±0.07|26.20±1.30|23.77±3.37|1.54|
|||FedRep|MD|78.90±0.76|4.75±0.00|25.93±0.10|24.31±0.64|2.31|76.35±6.60|4.79±0.07|25.29±0.99|25.42±3.70|5.77|
|||Mat-FL||80.55±0.99|4.75±0.00|25.84±0.08|24.49±0.74|2.10|79.42±8.16|4.79±0.07|25.25±1.03|25.62±3.96|5.20|
||resnet|Local<br>||81.07±0.90<br>|4.77±0.01<br>|26.43±0.20<br>|23.05±1.07<br>|-0.29<br>|83.18±5.64<br>|4.82±0.08<br>|26.01±1.17<br>|23.83±3.96<br>|1.49<br>|
|||FedAvg||73.16±0.68|4.81±0.01|22.94±0.04|31.61±0.14|14.39|65.94±9.43|4.84±0.08|21.25±1.28|38.14±4.66|25.08|
|||FedRep|TC|75.92±1.68|4.78±0.02|25.28±0.14|24.99±0.90|4.43|73.18±5.55|4.82±0.08|24.7±0.82|25.72±3.59|7.36|
|NIID-3||Mat-FL||77.69±2.42|4.78±0.02|24.96±0.11|25.57±0.86|4.79|76.12±6.39|4.82±0.09|24.32±0.71|26.36±3.81|7.56|
|SDHT||Local||73.45±1.12|4.73±0.00|24.31±0.20|34.05±1.92|16.07|73.41±9.63|4.77±0.07|24.45±0.73|32.37±5.64|14.53|
|||FedRep|MD|70.22±0.70|4.72±0.00|24.25±0.18|35.55±1.17|18.76|66.65±7.28|4.76±0.07|23.85±0.73|35.17±5.96|19.81|
|||Mat-FL||71.13±1.26|4.72±0.00|23.60±0.15|34.82±1.13|18.30|71.21±6.22|4.76±0.07|23.21±0.76|33.23±5.25|17.20|
||swin-t|Local||75.95±2.93|4.74±0.01|25.07±0.35|31.01±2.52|11.27|75.05±7.54|4.78±0.07|24.97±0.82|29.48±4.69|10.61|
|||FedAvg|TC|64.33±0.18|4.77±0.01|21.43±0.04|42.84±0.05|30.80|56.58±8.48|4.77±0.08|18.95±1.77|53.32±7.32|45.52|
|||FedRep||71.52±1.68|4.74±0.01|24.31±0.10|34.34±1.16|16.93|68.54±6.89|4.77±0.08|24.04±0.65|34.70±4.31|18.59|
|||Mat-FL||72.86±1.56|4.74±0.01|23.98±0.12|34.79±1.01|17.30|71.40±4.96|4.78±0.07|23.51±0.72|35.03±4.54|18.61|



Conference acronym ’XX, June 03–05, 2018, Woodstock, NY 

Yuwen Yang et al. 

**Table 3: Comparative Experiment: NIID-2 Single-Domain Single-Task (SDST) scenario. In this scenario, each client holds data pertaining to distinct task types. Refer to Table 2 for notation definitions and comparison baseline.** 

||||||G-FL|||||P-FL|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|BN|Algo|Ar<br>|Depth<br>RSME*↓|Edge  <br>Loss*↓|Normals<br>mErr↓|Semseg<br>mIoU↑|ΔG%↑|Depth<br>RSME*↓|Edge <br>Loss*↓|Normal<br>mErr↓|s Semseg<br>mIoU↑|<br>ΔP%↑|
||Ll|SD|81.13|4.75|26.61|24.68|1.39|68.93|4.71|27.64|23.85|4.42|
||oca|TC|80.02|4.75|26.55|24.03|1.09|67.82|4.71|27.31|23.61|4.79|
||FdA|SD|114.71|4.80|31.84|13.89|-25.68|107.56|4.77|33.77|12.14|-24.13|
||evg|TC|79.34|4.77|26.85|23.27|0.10|72.17|4.73|27.97|23.50|2.76|
||FdP|SD|114.95|4.81|31.65|13.97|-25.54|106.66|4.78|33.69|11.62|-24.38|
||erox|TC|79.29|4.78|26.86|23.02|-0.22|75.87|4.74|28.01|21.92|0.06|
||FdAMP|SD|79.90|4.74|26.64|24.85|1.97|69.39|4.70|27.47|23.46|4.11|
||e|TC|79.52|4.75|26.77|24.10|1.11|69.86|4.71|27.82|23.35|3.48|
||MTFL<br>|SD|81.10|4.74|27.02|24.46|0.83|69.81|4.71|28.40|22.67|2.26|
|resne|a-<br>|TC|78.71|4.74|27.57|24.03|0.58|69.20|4.71|28.86|23.26|2.59|
||PCGd|SD|109.75|4.83|32.89|11.52|-27.84|102.94|4.80|34.06|10.51|-24.94|
||ra|TC|138.12|4.77|32.34|15.45|-31.51|130.30|4.73|33.93|14.64|-27.77|
|||SD|114.64|4.80|32.02|13.55|-26.19|108.57|4.77|33.99|12.50|-24.25|
||CAGrad|TC|80.55|4.79|27.28|22.80|-1.29|75.44|4.75|28.14|19.97|-1.97|
|||SD|80.47|4.74|27.06|23.91|0.40|72.79|4.71|28.64|21.54|0.08|
||FedRep|TC|79.09|4.74|27.40|23.87|0.46|73.76|4.71|28.91|23.64|1.68|
|||SD|79.89|4.75|26.49|25.16|2.40|67.72|4.71|27.54|22.75|3.73|
||FedMTL|TC|78.70|4.75|26.67|24.07|1.43|72.92|4.71|27.98|22.26|1.39|
||Ll|SD|73.00|4.72|24.18|36.46|18.95|64.29|4.68|25.15|32.03|16.47|
||oca|TC|71.81|4.73|24.52|35.73|18.16|64.27|4.69|25.72|31.72|15.57|
||FdA|SD|106.96|4.76|28.80|24.25|-9.13|96.45|4.73|29.64|22.72|-6.27|
||evg|TC|71.61|4.74|24.93|34.49|16.45|67.61|4.70|25.90|31.26|13.97|
||FdP|SD|108.05|4.76|28.47|25.46|-7.85|99.37|4.72|29.65|23.95|-5.78|
||erox|TC|71.77|4.74|24.95|34.76|16.67|67.50|4.70|25.86|31.41|14.19|
||FdAP|SD|72.65|4.72|24.20|36.89|19.50|64.99|4.68|25.72|31.71|15.42|
||eM|TC|73.23|4.73|24.44|35.21|17.24|65.01|4.69|25.66|32.36|16.07|
|||SD|74.92|4.72|24.83|38.70|20.14|64.17|4.68|26.12|31.85|15.40|
|swin-|MaT-FL<br>|TC|75.07|4.73|25.08|36.23|17.16|70.06|4.68|26.44|31.88|13.52|
|||SD|113.43|4.78|29.32|26.79|-8.99|106.03|4.75|30.36|23.37|-9.02|
||PCGrad|TC|146.54|4.77|28.47|31.94|-12.79|139.00|4.74|29.97|27.00|-13.96|
|||SD|105.23|4.77|28.00|24.60|-7.52|95.27|4.73|28.39|25.36|-2.09|
||CAGrad|TC|72.12|4.75|24.73|34.94|16.92|70.28|4.71|26.24|29.94|11.53|
|||SD|71.90|4.72|25.09|35.93|17.86|63.53|4.68|26.34|30.53|14.03|
||FedRep|TC|70.30|4.72|25.62|34.22|16.02|65.59|4.68|26.77|28.85|11.36|
|||SD|73.40|4.72|24.25|36.62|18.93|63.58|4.68|25.45|30.99|15.33|
||FedMTL|TC|72.10|4.73|24.40|35.90|18.37|61.46|4.69|25.83|32.43|16.95|



**Table 4: Comparative Experiment: NIID-5 Unbalanced SingleDomain Single-Task (UBSDST) with ResNet backbone. Each client holds distinct task types and variable sample numbers. Notations and the target baseline are as defined in Tab. 2.** 

|||||G-FL|||||P-FL|||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Algo|Ar|Depth<br>RSME*↓|Edge <br>Loss*↓|Normals<br>mErr↓|Semseg<br>mIoU↑|ΔG%↑|Depth<br>RSME*↓|Edge <br>Loss*↓|Normals<br>mErr↓|Semseg<br>mIoU↑|ΔP%↑|
|Ll|SD|75.48|4.75|27.06|16.89|-5.64|66.87|4.68|27.93|13.14|-5.96|
|oca|TC|74.83|4.75|27.08|16.45|-5.93|64.11|4.68|27.78|13.83|-4.37|
|FedAv|SD|104.07|4.81|31.53|7.26|-29.26|96.73|4.75|32.40|7.82|-24.12|
|g|TC|75.98|4.78|27.61|15.41|-8.05|67.79|4.71|27.75|12.23|-7.12|
|FdP|SD|105.09|4.81|31.70|7.20|-29.80|97.95|4.75|32.46|7.62|-24.71|
|erox|TC|76.94|4.78|27.49|14.72|-8.97|67.46|4.71|27.95|11.60|-7.85|
|FdAMP|SD|75.34|4.74|27.03|16.89|-5.51|65.61|4.67|27.43|13.90|-4.32|
|e|TC|75.21|4.75|27.11|16.86|-5.63|67.18|4.68|28.07|14.16|-5.15|
|MTFL|SD|76.17|4.75|27.76|16.64|-6.78|64.14|4.68|28.78|12.54|-6.63|
|a-|TC|74.75|4.75|27.96|16.34|-6.85|63.11|4.67|28.99|14.60|-4.41|
|PCGd|SD|112.07|4.83|33.19|6.95|-33.73|110.01|4.77|33.81|7.10|-29.93|
|ra|TC|122.28|4.90|31.72|12.07|-30.36|124.20|4.84|32.98|9.60|-30.87|
|CAGd|SD|107.69|4.82|31.76|7.38|-30.52|101.75|4.75|32.54|7.98|-25.47|
|ra|TC|76.05|4.80|28.12|15.68|-8.37|68.97|4.72|28.73|12.77|-7.88|
||SD|75.23|4.75|27.41|16.74|-6.05|68.96|4.68|27.92|14.36|-5.29|
|FedRep|TC|73.53|4.75|27.82|16.45|-6.23|70.33|4.69|28.99|13.54|-7.56|
|FdMTL|SD|75.36|4.75|27.05|16.81|-5.68|64.54|4.68|27.58|12.89|-5.24|
|e|TC|74.35|4.75|27.16|16.65|-5.64|65.58|4.68|27.96|14.14|-4.63|



**Performance Improvement Over Time** : Initially, we generate a curve that represents the evolution of the average per-task performance improvement, as defined by Eq. (5), as the number of federated learning communication rounds varies. This curve serves as a foundation for discussing the necessary number of rounds to achieve a specific target (see Fig. 3). 

**Table 5: Comparative Experiment: NIID-7 Unbalanced CrossDomain Single-Task (UBCDST) with ResNet backbone.** 

Symbols (P) represent PASCAL-Context dataset. The configuration for first four clients mirrors that of NIID-2 scenario detailed in Tab. 3. In addition, Clients 4 and 5 incorporate larger datasets from a different domain. Client 4 introduces a new task, human parts segmentation, while Client 5 undertakes surface normal estimation as Client 1. Light blue shading indicates baseline for comparison. Refer to Tab. 2 for other notations. 

|Eval|Algo|Ar|Depth<br>RSME*↓|Edge<br>Loss*↓|Normals<br>mErr↓|Semseg<br>mIoU↑|Parts(P)<br>mIoU↑|Normals(P)<br>mErr↓|Δ%↑|
|---|---|---|---|---|---|---|---|---|---|
||Ll|SD|80.38|4.75|26.55|24.64|55.01|14.57|0.00|
||oca|TC|79.27|4.75|26.62|24.62|54.80|14.59|0.09|
||FedAv|SD|111.71|4.85|30.18|10.63|39.25|17.92|-27.21|
||g|TC|81.30|4.81|25.96|22.57|50.38|15.65|-4.07|
||FedProx|SD|111.66|4.85|29.98|10.99|40.03|17.69|-26.33|
|||TC|80.04|4.81|25.95|22.55|50.45|15.63|-3.77|
||FdAMP|SD|80.42|4.75|26.55|24.77|55.07|14.58|0.09|
||e|TC|79.60|4.75|26.61|24.19|54.78|14.60|-0.28|
|||SD|80.79|4.75|26.59|23.49|52.47|15.00|-2.15|
|G-FL|MaT-FL|TC|80.97|4.75|26.56|23.27|52.94|14.91|-2.07|
||PCGrad|SD|113.39|4.86|31.13|8.49|34.67|19.07|-32.34|
|||TC|117.70|4.85|30.69|15.57|39.24|18.34|-25.91|
||CAGrad|SD|111.52|4.84|29.85|10.82|39.71|17.99|-26.74|
|||TC|80.72|4.82|26.63|22.16|49.37|16.03|-5.42|
||FedRe|SD|80.44|4.75|26.62|23.60|52.36|15.02|-2.08|
||p|TC|78.17|4.75|26.77|23.54|52.52|14.99|-1.66|
||d|SD|80.54|4.74|26.56|24.74|54.97|14.59|0.03|
||FeMTL|TC|80.03|4.75|26.61|23.89|54.68|14.60|-0.61|
||Ll|SD|69.08|4.71|27.14|22.44|54.28|14.24|0.00|
||oca|TC|75.83|4.71|27.21|22.90|55.62|14.17|-0.84|
||FedAv|SD|103.69|4.82|31.81|9.43|38.11|17.45|-29.99|
||g|TC|74.99|4.77|27.12|20.67|51.12|15.33|-5.19|
|||SD|102.58|4.83|31.71|10.07|38.50|17.30|-28.93|
||FedProx|TC|73.09|4.77|27.17|19.61|49.88|15.33|-5.93|
||FdAMP|SD|71.89|4.71|27.82|24.44|55.65|14.14|0.93|
||e|TC|69.65|4.70|27.28|22.40|55.16|14.15|0.16|
|PFL|MTFL|SD|71.26|4.71|27.79|20.16|53.21|14.62|-3.39|
|-|a-|TC|77.87|4.70|28.17|20.75|52.95|14.50|-4.69|
||PCGd|SD|107.86|4.83|32.36|8.84|34.36|18.91|-34.67|
||ra|TC|105.01|4.80|32.40|14.79|37.20|18.03|-27.58|
|||SD|102.67|4.81|32.04|10.01|37.76|17.51|-29.60|
||CAGrad|TC|69.89|4.78|28.03|19.23|48.88|15.67|-6.71|
|||SD|71.55|4.71|28.01|21.04|52.51|14.65|-3.19|
||FedRep|TC|74.10|4.71|28.34|22.58|53.08|14.54|-2.56|
|||SD|67.38|4.71|27.29|22.35|54.50|14.18|0.39|
||FedMTL|TC|69.90|4.72|27.54|22.71|54.55|14.12|-0.05|



**Metrics Recording and Analysis** : We record key metrics such as communication overhead, energy consumption, and carbon emissions for each algorithm baseline. We then analyze these metrics in relation to the convergence speed of the algorithms (see Tab. 8). **Baseline Comparisons** : Acknowledging the unique attributes of different MTL indicators, we first conduct a comparison of baselines using the average per-task performance improvement, a normalized singular metric. We also employ statistical methods, such as the Critical Difference (CD) Diagram [12] with the Nemenyi post-hoc test [49] (see Fig. 5) for comparing baselines across multiple metrics. **Influence of Pre-Training Strategy and Scalability** : We include experiments where the model is trained from scratch. We also conduct experiments with varying numbers of clients, ranging from 2 to 8 (see Tab. 9). 

### **3.4 Results and Suggestions** 

Our experimental findings provide valuable insights and recommendations for future studies and applications in the FMTL. 

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY 

Federated Multi-Task Learning on Non-IID Data Silos: An Experimental Study 

**Table 6: Comparative Experiment: NIID-4 Unbalanced Single-Domain Multi-Task (UBSDMT) scenario. This scenario mirrors the IID-1 as detailed in Tab. 2, with the sole distinction being an unbalanced distribution of total samples across different clients.** 

|||||G-FL|||||P-FL|||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Algo|Ar|Depth<br>RSME*↓|Edge<br>Loss*↓|Normals<br>mErr↓|Semseg<br>mIoU↑|ΔG%↑|Depth<br>RSME*↓|Edge<br>Loss*↓|Normals<br>mErr↓|Semseg<br>mIoU↑|ΔP%↑|
|Local|MD|84.82±9.99|4.77±0.03|26.82±1.68|22.16±4.48|-2.74|91.08±20.63|4.81±0.11|26.70±2.52|22.32±6.16|-2.83|
||TC|82.36±7.60|4.78±0.00|26.72±1.68|22.04±4.66|-2.07|87.42±18.66|4.82±0.10|26.67±2.54|22.48±6.57|-1.69|
|FdA|MD|71.55±0.07|4.77±0.00|22.96±0.01|29.98±0.10|13.35|68.15±4.99|4.80±0.10|22.69±0.56|29.15±4.67|14.21|
|evg|TC|74.57±1.25|4.82±0.02|22.57±0.02|30.48±0.45|13.06|69.68±4.83|4.85±0.10|22.16±0.47|26.76±4.00|11.62|
|FdP|MD|71.55±0.12|4.77±0.00|22.95±0.02|29.79±0.09|13.16|67.39±4.93|4.80±0.10|22.50±0.46|28.45±3.87|13.89|
|erox|TC|72.68±1.18|4.82±0.02|22.56±0.02|30.23±0.45|13.39|70.78±7.83|4.85±0.10|22.34±0.48|26.94±3.07|11.33|
|FdAMP|MD|84.86±10.09|4.77±0.03|26.85±1.68|22.00±4.41|-2.96|91.62±22.57|4.81±0.11|26.38±2.62|22.62±6.60|-2.37|
|e|TC|83.11±7.45|4.78±0.01|26.83±1.76|21.92±4.24|-2.54|85.32±14.26|4.81±0.10|26.78±2.70|21.78±5.42|-1.87|
|MTFL|MD|82.68±8.21|4.77±0.02|26.02±1.02|22.61±3.58|-0.85|86.93±18.93|4.80±0.11|25.70±1.66|23.31±5.86|0.31|
|a-|TC|78.31±4.16|4.78±0.01|25.62±0.89|23.94±3.62|2.24|82.91±13.85|4.82±0.11|25.28±1.42|23.25±5.28|1.65|
|PCGrad|MD|141.20±11.51|4.86±0.01|29.04±0.88|14.55±1.27|-30.77|146.40±18.90|4.89±0.10|28.25±1.09|14.81±2.01|-27.46|
||TC|105.72±15.51|4.95±0.04|32.33±0.59|17.24±2.54|-20.58|107.12±17.75|4.99±0.09|32.43±1.37|16.53±3.74|-19.45|
|CAGd|MD|84.53±6.03|4.81±0.01|25.33±0.87|19.66±2.36|-4.13|86.12±15.21|4.85±0.10|25.14±1.24|20.51±3.80|-2.03|
|ra|TC|79.71±3.73|4.86±0.01|24.48±0.82|23.59±3.29|2.10|78.93±6.44|4.89±0.10|24.20±1.20|23.18±5.55|3.32|
|FdR|MD|81.55±8.21|4.77±0.02|25.62±1.08|23.03±3.63|0.33|84.27±17.17|4.80±0.11|25.50±1.81|23.11±5.93|1.03|
|eep|TC|77.41±5.02|4.78±0.01|24.93±0.95|24.67±4.05|3.95|75.64±10.29|4.82±0.10|24.54±1.63|24.00±5.49|5.10|
|FdMTL|MD|85.10±9.98|4.77±0.02|26.85±1.66|21.92±4.32|-3.11|90.05±19.50|4.80±0.11|26.46±2.49|23.29±5.93|-1.28|
|e|TC|83.21±7.25|4.78±0.01|26.76±1.82|22.22±4.40|-2.18|86.52±16.15|4.82±0.10|26.22±2.22|21.77±6.11|-1.73|



#### **Table 7: Comparative Experiment: NIID-6 Unbalanced CrossDomain Multi-Task (UBCDMT) with global evaluation G-FL.** 

The setup for the first four clients mirrors that of the IID-1 scenario as detailed in Table 2. Client 4 incorporates a larger dataset from a different domain, introducing a new task of human parts segmentation while also performing the same surface normal estimation task as Client 1. ‘NULL’ indicates the absence of such a baseline. The ‘-E’ flag is used when only the parameters of the model encoder or the accumulated gradient are transmitted and utilized for federated learning optimization. For additional notation definitions, please refer to Table 2 and Table 5. 

|BN|Algo|Ar|Depth<br>RSME*↓|Edge<br>Loss*↓|Normals<br>mErr↓|Semseg<br>mIoU↑|Parts(P) <br>mIoU↑|Normals(P)<br>mErr↓|ΔG%↑|
|---|---|---|---|---|---|---|---|---|---|
||Local|MD|81.82±2.09|4.76±0.00|26.49±0.13|23.37±0.64|54.12|13.86|0.00|
||Local<br>|TC|80.44±1.86|4.78±0.01|26.43±0.17|22.72±0.40|52.54|13.78|-0.61|
||FedAvg<br>|MD|NULL|NULL|NULL|NULL|NULL|NULL|NULL|
||FedAvg|TC|75.27±0.20|4.82±0.00|22.15±0.04|30.50±0.19|50.59|14.89|6.61|
||FedProx-E<br>|MD|78.55±1.17|4.76±0.00|25.14±0.20|23.61±0.55|54.08|14.11|1.37|
||FedProx|TC|73.76±0.20|4.82±0.00|22.23±0.04|30.06±0.19|50.22|14.88|6.46|
||FedAMP-E|MD|81.33±1.74|4.76±0.00|26.50±0.13|23.16±0.37|54.2|13.87|-0.04|
||FedAMP|TC|80.49±1.58|4.78±0.01|26.47±0.16|22.48±0.54|53.05|13.84|-0.73|
|t|MaT-FL|MD|79.33±0.92|4.76±0.00|25.48±0.48|23.24±0.51|54.21|14.06|0.84|
|resne|MaT-FL|TC|78.44±3.28|4.79±0.01|25.24±0.77|23.78±0.72|53.19|14.01|1.20|
||PCGrad-E|MD|88.96±1.27|4.79±0.00|30.43±0.28|16.32±0.40|46.73|18.67|-17.13|
||PCGrad|TC|96.21±1.95|4.94±0.02|32.90±0.43|16.86±0.47|43.75|24.84|-28.63|
||CAGrad-E<br>|MD|78.22±1.21|4.75±0.00|25.02±0.16|24.07±0.68|53.78|14.16|1.73|
||CAGrad|TC|78.71±1.80|4.86±0.01|23.81±0.04|23.95±0.39|49.77|14.99|-0.32|
||FedRep|MD|78.86±1.43|4.76±0.00|25.16±0.13|23.66±0.53|54.17|14.08|1.40|
||FedRep|TC|75.41±1.38|4.78±0.01|24.52±0.09|24.94±0.48|52.87|14.05|2.98|
||FedMTL-E|MD|82.02±1.96|4.76±0.00|26.50±0.12|23.14±0.30|53.84|13.86|-0.30|
||FedMTL|TC|80.61±1.38|4.78±0.01|26.43±0.18|22.88±0.61|52.69|13.81|-0.52|
||Local|MD|72.34±1.14|4.73±0.01|24.4±0.13|33.83±0.38|54.42|13.67|11.13|
||Local|TC|77.50±2.22|4.75±0.00|25.19±0.20|29.98±0.59|52.35|13.65|6.15|
||FedAvg|MD|NULL|NULL|NULL|NULL|NULL|NULL|NULL|
||FedAvg|TC|70.15±0.17|4.78±0.00|20.96±0.02|40.65±0.03|52.32|14.61|16.65|
||FedProx-E|MD|70.89±1.19|4.73±0.00|23.92±0.05|33.91±0.37|55.22|14.13|11.48|
||FedProx<br>|TC|70.12±0.18|4.78±0.00|20.99±0.02|40.51±0.03|52.32|14.62|16.53|
||FedAMP-E|MD|OOM|OOM|OOM|OOM|OOM|OOM|OOM|
||FedAMP|TC|77.77±1.53|4.75±0.00|25.25±0.15|29.95±0.99|52.33|13.7|5.97|
|swin-t|MaT-FL|MD|71.48±0.59|4.73±0.00|23.96±0.19|33.41±0.85|55.42|14.05|11.14|
||MaT-FL|TC|72.08±1.33|4.74±0.00|23.80±0.07|33.69±0.23|52.09|13.62|10.77|
||PCGrad-E|MD|79.38±2.37|4.73±0.00|26.16±0.05|33.25±0.34|52.93|15.38|5.66|
||PCGrad|TC|85.99±14.50|4.90±0.02|28.31±0.22|34.98±0.49|50.84|19.68|-2.21|
||CAGrad-E|MD|69.90±0.82|4.73±0.01|23.67±0.06|34.57±0.33|55|14.21|12.14|
||CAGrad|TC|75.34±8.49|4.81±0.01|21.97±0.02|34.15±0.86|51.1|14.69|9.75|
||FedRep|MD|70.78±1.18|4.73±0.00|23.89±0.04|33.90±0.43|55.32|14.13|11.54|
||FedRep|TC|72.93±1.22|4.75±0.00|23.91±0.07|31.54±0.58|53.01|14.2|8.55|
||FedMTL-E|MD|OOM|OOM|OOM|OOM|OOM|OOM|OOM|
||FedMTL|TC|77.30±2.03|4.75±0.00|25.23±0.17|29.70±0.54|52.32|13.64|5.97|





<!-- Start of picture text -->
Heatmap of p-values after Bonferroni correction<br>MD-Local 153.0 0.114 0.0 0.0 0.0 0.0 3.411 43.696 0.001 0.0 0.0 0.0 0.0 0.003 0.0 0.0 34.494 17.618<br>TC-Local 0.114 153.0 0.0 0.0 0.0 0.0 0.059 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.008 0.0 140<br>MD-FedAvg 0.0 0.0 153.0 0.318 92.71 17.618 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>TC-FedAvg 0.0 0.0 0.318 153.0 0.318 87.312 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 120<br>MD-FedProx 0.0 0.0 92.71 0.318 153.0 17.618 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>TC-FedProx 0.0 0.0 17.618 87.312 17.618 153.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>100<br>MD-FedAMP 3.411 0.059 0.0 0.0 0.0 0.0 153.0 10.22 0.001 0.0 0.0 0.0 0.0 0.0 0.001 0.0 0.325 87.312<br>TC-FedAMP 43.696 0.0 0.0 0.0 0.0 0.0 10.22 153.0 0.008 0.002 0.0 0.0 0.0 0.0 0.0 0.0 43.696 9.34<br>MD-Mat-FL 0.001 0.0 0.0 0.0 0.0 0.0 0.001 0.008 153.0 0.0 0.0 0.0 0.0 0.001 0.001 0.0 0.0 0.172 80<br>TC-Mat-FL 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.002 0.0 153.0 0.0 0.0 0.011 125.76 0.0 0.0 0.0 0.003<br>MD-PCGrad 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 153.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>60<br>TC-PCGrad 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 153.0 0.0 0.0 0.0 0.0 0.0 0.0<br>MD-CAGrad 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.011 0.0 0.0 153.0 1.188 0.001 0.0 0.0 0.001<br>TC-CAGrad 0.003 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.001 125.76 0.0 0.0 1.188 153.0 0.783 0.0 0.0 0.003 40<br>MD-FedRep 0.0 0.0 0.0 0.0 0.0 0.0 0.001 0.0 0.001 0.0 0.0 0.0 0.001 0.783 153.0 0.0 0.0 0.018<br>TC-FedRep 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 153.0 0.0 0.0<br>20<br>MD-FedMTL 34.494 0.008 0.0 0.0 0.0 0.0 0.325 43.696 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 153.0 35.281<br>TC-FedMTL 17.618 0.0 0.0 0.0 0.0 0.0 87.312 9.34 0.172 0.003 0.0 0.0 0.001 0.003 0.018 0.0 35.281 153.0<br>MD-Local TC-Local MD-FedAvgTC-FedAvgMD-FedProxTC-FedProxMD-FedAMPTC-FedAMPMD-Mat-FL TC-Mat-FLMD-PCGradTC-PCGradMD-CAGradTC-CAGradMD-FedRepTC-FedRepMD-FedMTLTC-FedMTL 0<br><!-- End of picture text -->

**Figure 4: Case Study: Adjusted** _𝑝_ **-value heatmap for pairwise comparisons of baselines in IID-1 SDMT scenario from Tab. 2.** Heatmap displays adjusted _𝑝_ -values from pairwise comparisons, utilizing Wilcoxon signed-rank test with Bonferroni correction for multiple comparisons. Each cell corresponds to _𝑝_ -value from comparing the row and column baselines. _𝑝_ -values below 0.05, marked in white, signify a statistically significant performance difference between the pair of baselines. Please zoom in for details. 

_3.4.1 General Evaluation._ In accordance with the “No Free Lunch” principle, our results from seven comparative experiments demonstrate that no single “algorithm-model” baseline consistently outperforms others across all experiments. In fact, the PCGard algorithm, 

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY 

Yuwen Yang et al. 



<!-- Start of picture text -->
CD<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18<br>MD-FedProx TC-PCGrad<br>MD-FedAvg TC-Local<br>TC-FedProx MD-PCGrad<br>TC-FedAvg MD-FedAMP<br>TC-FedRep TC-FedAMP<br>MD-CAGrad MD-FedMTL<br>MD-FedRep TC-FedMTL<br>TC-MaT-FL MD-Local<br>MD-MaT-FL TC-CAGrad<br><!-- End of picture text -->

**Figure 5: Case Study: the Critical Difference (CD) Diagram for baselines in IID-1 SDMT scenario from Table 2.** 

The CD Diagram [12] illustrates the performance-based ranking of various baselines. Sorted from left (best) to right, baselines that are not significantly different according to Nemenyi post-hoc test [49] are connected by horizontal lines. Please zoom in for details. 

**Table 8: Case Study: Comparison of communication costs (GB), energy consumption (kWh), training duration (min), and carbon dioxide emissions (g) for each baseline in the IID1 Single-Domain Multi-Task (SDMT) scenario from Table 2.** _𝑃_ is equipment running average power (W). _𝐶𝑟_ and _𝑇𝑟_ are communication overhead and running time (s) for each round respectively. _𝑅_ 30, _𝐸_ 30, _𝐶_ 30, and _𝑇_ 30 are respectively the number of communication rounds, energy consumption, communication costs, and time when the average task improvement reaches -30%, while _𝑅_ 10, _𝐸_ 10, _𝐶_ 10, and _𝑇_ 10 are for -10% improvement. CO2 _𝑒_ refers to carbon dioxide emissions during training at -10% improvement. We refer to previous works [46, 65], and use the tool [1] to record power, time, and carbon dioxide emissions on a server equipped with two NVIDIA RTX2080Ti GPUs and two Intel E5-2680V4 CPUs 

|Algo|Ar|_𝑃_(w)|_𝐶𝑟_|_𝑇𝑟_(s)|_𝑅_30|_𝐸_30|_𝐶_30|_𝑇_30|_𝑅_10 _𝐸_10|_𝐶_10|_𝑇_10|CO2_𝑒_|ΔG% ↑|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Local|MD|738.36|0.00|186.5|11|0.42|0.00|34|23 0.88|0.00|71|476.25|0.00|
||TC|699.72|0.00|209.3|11|0.45|0.00|38|19<br>0.77|0.00|66|418.31|-1.76|
|FdA|MD|745.99|1.17|189.0|11|0.43|12.85|35|23 0.90|26.87|72|487.62|13.52|
|evg|TC|705.58|0.57|210.3|15|0.62|8.62|53|23<br>0.95|13.22|81|513.06|15.15|
|FedProx|MD|720.21|1.17|196.0|11|0.43|12.85|36|23 0.90|26.87|75|488.21|13.55|
||TC|683.44|0.57|232.8|11|0.49|6.32|43|19<br>0.84|10.92|74|454.47|16.65|
|FdAMP|MD|713.05|1.17|189.9|11|0.41|12.85|35|27 1.02|31.55|85|549.73|0.20|
|e|TC|710.36|0.57|215.3|7|0.30|4.02|25|27<br>1.15|15.52|97|620.80|-0.03|
|MT-FL|MD|736.19|0.35|190.0|11|0.43|3.84|35|27 1.05|9.43|86|567.89|1.64|
|a|TC|699.51|0.35|212.0|7|0.29|2.45|25|15<br>0.62|5.24|53|334.49|4.93|
|PCGrad|MD|736.81|1.17|194.8|11|0.44|12.85|36|27 1.08|31.55|88|582.58|-6.61|
||TC|694.33|0.57|211.5|27|1.10|15.52|95|55<br>2.24|31.61|194|1214.51|-23.81|
|CAGd|MD|736.23|1.17|191.8|11|0.43|12.85|35|23 0.90|26.87|74|488.25|3.25|
|ra|TC|703.17|0.57|212.0|11|0.46|6.32|39|23<br>0.95|13.22|81|515.57|4.38|
|FdR|MD|738.90|0.35|188.0|11|0.42|3.84|34|23 0.89|8.04|72|480.43|3.00|
|eep|TC|706.55|0.35|208.8|7|0.29|2.45|24|19<br>0.78|6.64|66|421.39|7.22|
|FdMTL|MD|692.65|4.67|202.6|11|0.43|51.41|37|23 0.90|107.50|78|485.35|0.07|
|e|TC|694.80|2.30|225.5|11|0.48|25.29|41|23<br>1.00|52.87|86|541.87|-0.58|



designed to resolve gradient conflict issues, generally underperforms. We advise selecting a baseline method based on the specific requirements of the scenario. 

Different types of tasks have distinct indicators, and the relative ratios of their standard deviations also vary considerably. This suggests that the difficulty of learning varies across tasks. Although we treated each task equally in our work, as per Eq. (5), we posit that in real-world FMTL scenarios, the value of labels for different tasks can vary. Consequently, data holders should select high-value labels based on their actual requirements. 

_3.4.2 Data Level Analysis._ In the IID-1 scenario (Tab. 2, Fig. 3, Fig. 5), FedAvg and FedProx significantly outperform others. 

#### **Table 9: Case Study: Influence of client size and scratch training strategy on model performance.** 

SN denotes the scenario, while 2C-8C represent training sets evenly distributed among 2 to 8 clients. ATI refers to Average Task Performance Improvement (Δ% ↑). The blue shading indicates the target baseline from IID-1 SDMT scenario in Tab. 2. Different bar colors and lengths in the upper table denote relative improvements of baselines across scenarios. In the lower table, ‘*’ indicates the use of scratch training strategy, with color brightness representing relative improvement. Refer to Tab. 2 for details. 

|SN|ATI|Local|FedAvg|FedProx|FedAMP|Mat-FL|PCGrad|CAGrad|FedRep|FedMTL|
|---|---|---|---|---|---|---|---|---|---|---|
|2C|G|11.27|19.90|19.22|10.92|11.13|-24.43|13.45|13.39|11.27|
|MD|P|12.75|21.17|21.14|13.15|12.62|-20.99|14.03|14.44|12.15|
|2C|G|10.58|19.07|19.23|10.14|10.80|-24.16|13.01|14.87|10.52|
|TC|P|11.31|19.83|19.70|9.91|11.67|-22.12|13.65|15.45|10.49|
|4C|G|0.00|13.52|13.55|0.20|1.64|-6.61|3.25|3.00|0.07|
|MD|P|0.00|14.67|14.64|-1.52|1.13|-5.75|3.34|2.38|-0.38|
|4C|G|-1.76|15.15|16.65|-0.03|4.93|-23.81|4.38|7.22|-0.58|
|TC|P|-2.59|14.99|14.44|0.34|4.15|-21.39|4.15|7.23|0.32|
|6C|G|-7.78|3.55|3.63|-7.75|-5.95|-25.12|-10.88|-5.17|-7.90|
|MD|P|-9.33|2.37|2.39|-9.93|-7.62|-24.39|-11.24|-6.95|-9.70|
|6C|G|-7.94|12.14|11.50|-7.80|-2.95|-46.99|-2.68|-1.45|-8.02|
|TC|P|-9.13|7.74|6.80|-10.23|-3.69|-45.72|-3.93|-3.42|-9.16|
|8C|G|-12.48|-3.90|-3.67|-12.65|-11.13|-32.12|-16.70|-10.68|OOM|
|MD|P|-9.45|1.37|1.27|-9.47|-8.32|-25.58|-11.78|-8.08|OOM|
|8C|G|-11.41|9.37|10.60|-11.52|-7.87|-28.51|-7.70|-6.11|-11.94|
|TC|P|-10.09|9.12|8.85|-8.88|-5.01|-25.10|-5.70|-4.61|-11.14|
|4C|G|-20.99|-7.62|-7.43|-21.21|-16.90|-46.03|-32.98|-13.97|-20.93|
|MD*|P|-17.73|-6.75|-7.03|-18.53|-14.65|-44.30|-30.92|-12.55|-17.62|
|4C|G|-15.35|-1.34|-1.45|-15.30|-12.96|-44.49|-24.69|-10.42|-15.52|
|TC*|P|-14.81|-3.34|-3.77|-14.91|-12.37|-42.02|-23.59|-10.23|-15.27|



Comparing the Local baseline of IID-1 in Tab. 2 and NIID-2 in Tab. 3, we observe that in a scenario where the number of labels for each task is balanced: multiple single-task learning models (each model only learns one task) can achieve better performance than a multi-task learning model. Furthermore, in three sets of pathological partition scenarios (NIID-2, NIID-5 in Tab. 4, NIID-7 in Tab. 5) where each client has only one task, the combination of FedAvg, FedProx and CAGrad with the SD (single-task MD) has extremely poor performance. FedAMP and FedMTL can achieve a slight G-FL improvement compared to the Local algorithm. The TC architecture suffers less performance loss than the SD architecture. 

In the NIID-3 from Tab. 2 mixed task number scenario, the combination of FedAvg algorithms with the TC architecture significantly improves the P-FL. 

Compared with IID-1 in Tab. 2, the average task improvement indicator of NIID-4 in Tab. 6 for algorithms other than FedAvg and FedProx all decreased by 1 to 2 percentage points, suggesting that these two algorithms are relatively robust. 

Two sets of cross-domain tasks (NIID-6 Tab. 7 and NIID-7 Tab. 5) are jointly trained with the larger PASCAL dataset. Compared with the original IID-1 scenario in Tab. 2, all baselines perform significantly worse in most tasks when evaluated using each task’s metrics. This indicates cross-domain tasks pose a challenge for FMTL, thereby necessitating design of additional optimization strategies. 

_3.4.3 Model Level Analysis._ **Model Architecture.** As per Tab. 1, compared to the widely studied MD architecture [55, 65], the TC architecture [37, 53] trades time and computation for space. The MD architecture learns all task labels simultaneously during training, while the TC learns different task labels sequentially. Hence, the TC architecture utilizes fewer model parameters but significantly increases the computational load and training time (see Tab. 8). It also does not require a balanced number of task labels, making it 

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY 

Federated Multi-Task Learning on Non-IID Data Silos: An Experimental Study 

more flexible. For FMTL scenarios, the computing and communication capabilities of the participants and the characteristics of their datasets are crucial considerations, and the two architectures offer different selection biases. **Backbone Network.** It’s noteworthy that using a larger backbone significantly improves model performance across all comparative experiments. Provided that device computing capability and inter-client communication bandwidth are sufficient, we recommend using a larger backbone network in FMTL scenarios to handle complex tasks. 

_3.4.4 Optimization Algorithm Level Analysis._ As can be seen from NIID-6 Tab. 7, the **parameter decoupling strategy** can aid the MD architecture in performing FL in heterogeneous model scenarios. Simultaneously, it can resist optimization direction conflicts from the MTL process and reduce model performance losses. Also, as observed from the Tab. 8 experiment, it can significantly reduce communication expenses when the same accuracy is achieved. 

its original domain. To facilitate this, we have developed a benchmark, FMTL-Bench, which covers a wide range of settings at data, model, and optimization algorithm levels. We carried out seven sets of comparative experiments to encompass a broad spectrum of data partitioning scenarios. To cater to the practical implementation needs of federated learning (FL) scenarios and the multi-task evaluation requirements of MTL, we utilized a diverse array of evaluation methodologies in our case studies. Through comprehensive experimentation, we have outlined the strengths and weaknesses of existing baseline methods, providing valuable insights for future method selection. 

### **ACKNOWLEDGMENTS** 

This paper is supported by NSFC (No. 62176155), Shanghai Municipal Science and Technology Major Project (2021SHZDZX0102). 

_3.4.5 Case Study._ As illustrated in Tab. 9, **Pre-training Strategy.** Initiating training with a pre-trained model, rather than starting from scratch, can markedly improve the model’s training efficacy. This strategy can significantly decrease communication overhead, training time, and energy consumption. **Scale Impact.** When client data diminishes and number of clients escalates, the performance of all algorithms, excluding FedAvg and FedProx, declines significantly. These two algorithms exhibit notable performance improvements compared to Local baseline (especially when combined with TC). This suggests that in IID scenarios, FedAvg and FedProx are highly effective, and TC can also be a primary consideration. 

FMTL encompasses numerous model performance evaluation metrics, with each task having separate indicators. In addition to the average task improvement as in Eq. (5), we introduce a statistical method in Fig. 5 to evaluate the ranking of different baselines across multiple indicators, thereby gaining a clear understanding of the strengths, weaknesses, and statistical differences among baselines. 

FMTL also needs to consider real-world deployment issues. The average task improvement as a function of communication rounds was obtained in Fig. 3 and used in Tab. 8. In the latter, we comprehensively assess the energy consumption, carbon emissions, communication volume, and time consumption of all baselines. Different baselines utilize the federated learning system differently, and the resources used to achieve specified goals also vary. In the IID-1 scenario from Tab. 2, when reaching a -10% average task improvement, except for the outlier “PCGrad-TC”, the time, energy consumption, and carbon emissions of all other baselines are relatively close. The parameter decoupling strategy significantly reduces the communication cost. Future research could incorporate communication expenditure, energy consumption, and time as optimization objectives in real-life FMTL deployment. Due to paper length constraints, we have not listed all conclusions from other experiments. These will be discussed in detail in subsequent work. 

### **4 CONCLUSION** 

The emerging paradigm of federated multi-task learning (FMTL) enables data owners to collaboratively train cross-domain multi-task learning (MTL) models without the need for transferring data from 

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY 

Yuwen Yang et al. 

### **REFERENCES** 

- [1] Lasse F. Wolff Anthony et al. 2020. Carbontracker: Tracking and Predicting the Carbon Footprint of Training Deep Learning Models. ICML Workshop on Challenges in Deploying and monitoring Machine Learning Systems. 

- [2] Xiang Bai et al. 2021. Advancing COVID-19 Diagnosis with Privacy-Preserving Collaboration in Artificial Intelligence. _Nature Machine Intelligence_ 3, 12 (2021), 1081–1089. 

- [3] Cosmin I. Bercea et al. 2022. Federated Disentangled Representation Learning for Unsupervised Brain Anomaly Detection. _Nature Machine Intelligence_ 4, 8 (2022), 685–695. 

- [4] Ruisi Cai, Xiaohan Chen, Shiwei Liu, Jayanth Srinivasa, Myungjin Lee, Ramana Kompella, and Zhangyang Wang. 2023. Many-Task Federated Learning: A New Problem Setting and A Simple Baseline. In _CVPR_ . 5037–5045. 

- [5] Rich Caruana. 1997. Multitask learning. _Machine learning_ 28, 1 (1997), 41–75. 

- [6] Hong-You Chen and Wei-Lun Chao. 2022. On Bridging Generic and Personalized Federated Learning for Image Classification. In _ICLR_ . 

- [7] Liang-Chieh Chen et al. 2018. Encoder-decoder with atrous separable convolution for semantic image segmentation. In _ECCV_ . 801–818. 

- [8] Yiqiang Chen, Teng Zhang, Xinlong Jiang, Qian Chen, Chenlong Gao, and Wuliang Huang. 2023. FedBone: Towards Large-Scale Federated Multi-Task Learning. _CoRR_ abs/2306.17465 (2023). 

- [9] Liam Collins, Hamed Hassani, et al. 2021. Exploiting shared representations for personalized federated learning. In _ICML_ . 2089–2099. 

- [10] Michael Crawshaw. 2020. Multi-task learning with deep neural networks: A survey. _CoRR_ abs/2009.09796 (2020). 

- [11] Ittai Dayan et al. 2021. Federated Learning for Predicting Clinical Outcomes in Patients with COVID-19. _Nature Medicine_ 27, 10 (2021), 1735–1743. 

- [12] Janez Demsar. 2006. Statistical Comparisons of Classifiers over Multiple Data Sets. _J. Mach. Learn. Res._ 7 (2006), 1–30. 

- [13] Sabri Eyuboglu et al. 2021. Multi-task weak supervision enables anatomicallyresolved abnormality detection in whole-body FDG-PET/CT. _Nat Commun_ 12 (2021), 1880. 

- [14] Bao Feng, Jiangfeng Shi, et al. 2024. Robustly federated learning model for identifying high-risk patients with postoperative gastric cancer recurrence. _Nat Commun_ 15 (2024), 742. 

- [15] Tianyu Han et al. 2020. Breaking Medical Data Sharing Boundaries by Using Synthesized Radiographs. _Science Advances_ 6, 49 (2020), eabb7973. 

- [16] Chaoyang He, Emir Ceyani, Keshav Balasubramanian, Murali Annavaram, and Salman Avestimehr. 2022. Spreadgnn: Decentralized multi-task federated learning for graph neural networks on molecular data. In _AAAI_ , Vol. 36. 6865–6873. 

- [17] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual learning for image recognition. In _CVPR_ . 770–778. 

- [18] Sixu Hu, Yuan Li, Xu Liu, Qinbin Li, Zhaomin Wu, and Bingsheng He. 2022. The oarf benchmark suite: Characterization and implications for federated learning systems. _ACM Transactions on Intelligent Systems and Technology_ 13 (2022), 1–32. 

- [19] Yutao Huang, Lingyang Chu, et al. 2021. Personalized cross-silo federated learning on non-iid data. In _AAAI_ , Vol. 35. 7865–7873. 

- [20] Joel Janai et al. 2020. Computer vision for autonomous vehicles: Problems, datasets and state of the art. _Foundations and Trends® in Computer Graphics and Vision_ 12, 1–3 (2020), 1–308. 

- [21] Cheng Jin et al. 2021. Predicting treatment response from longitudinal images using multi-task deep learning. _Nat Commun_ 12 (2021), 1851. 

- [22] Peter Kairouz, H. Brendan McMahan, et al. 2021. Advances and Open Problems in Federated Learning. _Found. Trends Mach. Learn._ 14, 1-2 (2021), 1–210. 

- [23] Georgios Kaissis et al. 2021. End-to-End Privacy Preserving Deep Learning on Multi-Institutional Medical Imaging. _Nature Machine Intelligence_ 3, 6 (2021), 473–484. 

- [24] Georgios A. Kaissis et al. 2020. Secure, Privacy-Preserving and Federated Machine Learning in Medical Imaging. _Nature Machine Intelligence_ 2, 6 (2020), 305–311. 

- [25] Shivam Kalra et al. 2023. Decentralized federated learning through proxy model sharing. _Nat Commun_ 14 (2023), 2899. 

- [26] Menelaos Kanakis, David Bruggemann, Suman Saha, Stamatios Georgoulis, Anton Obukhov, and Luc Van Gool. 2020. Reparameterizing convolutions for incremental multi-task learning without task interference. In _ECCV_ . 689–707. 

- [27] Alexandros Karargyris and otherss. 2023. Federated benchmarking of medical artificial intelligence with MedPerf. _Nat Mach Intell_ 5, 7 (2023), 799–810. 

- [28] Jakub Konečný et al. 2015. Federated Optimization: Distributed Optimization Beyond the Datacenter. _CoRR_ abs/1511.03575 (2015). 

- [29] Qinbin Li, Yiqun Diao, Quan Chen, and Bingsheng He. 2022. Federated learning on non-iid data silos: An experimental study. In _2022 IEEE 38th International Conference on Data Engineering (ICDE)_ . IEEE, 965–978. 

- [30] Tian Li, Anit Kumar Sahu, Manzil Zaheer, Maziar Sanjabi, et al. 2020. Federated Optimization in Heterogeneous Networks. In _MLSys_ . 

- [31] Bo Liu, Xingchao Liu, Xiaojie Jin, Peter Stone, and Qiang Liu. 2021. ConflictAverse Gradient Descent for Multi-task learning. In _NeurIPS_ . 18878–18890. 

- [32] Ken Liu, Shengyuan Hu, Steven Z Wu, and Virginia Smith. 2022. On privacy and personalization in cross-silo federated learning. _NeurIPS_ 35 (2022), 5925–5940. 

- [33] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, and Baining Guo. 2021. Swin transformer: Hierarchical vision transformer using shifted windows. In _ICCV_ . 10012–10022. 

- [34] Ilya Loshchilov and Frank Hutter. 2017. Sgdr: Stochastic gradient descent with warm restarts. In _ICLR_ . 

- [35] Ilya Loshchilov and Frank Hutter. 2019. Decoupled Weight Decay Regularization. In _ICLR_ . 

- [36] Yuxiang Lu, Suizhi Huang, Yuwen Yang, Shalayiding Sirejiding, Yue Ding, and Hongtao Lu. 2023. Towards Hetero-Client Federated Multi-Task Learning. _CoRR_ abs/2311.13250 (2023). 

- [37] Kevis-Kokitsi Maninis, Ilija Radosavovic, and Iasonas Kokkinos. 2019. Attentive single-tasking of multiple tasks. In _CVPR_ . 1851–1860. 

- [38] Othmane Marfoq, Giovanni Neglia, Aurélien Bellet, Laetitia Kameni, and Richard Vidal. 2021. Federated Multi-Task Learning under a Mixture of Distributions. In _NeurIPS_ . 15434–15447. 

- [39] Brendan McMahan et al. 2017. Communication-Efficient Learning of Deep Networks from Decentralized Data. In _AISTATS_ , Vol. 54. 1273–1282. 

- [40] Jed Mills et al. 2021. Multi-task federated learning for personalised deep neural networks in edge computing. _TPDS_ 33, 3 (2021), 630–641. 

- [41] Roozbeh Mottaghi et al. 2014. The role of context for object detection and semantic segmentation in the wild. In _CVPR_ . 891–898. 

- [42] Sangjoon Park et al. 2021. Federated Split Task-Agnostic Vision Transformer for COVID-19 CXR Diagnosis. In _NeurIPS_ . 

- [43] Adam Paszke et al. 2019. Pytorch: An imperative style, high-performance deep learning library. _NeurIPS_ 32 (2019). 

- [44] Sara Pieri, Jose Restom, Samuel Horvath, and Hisham Cholakkal. 2024. Handling Data Heterogeneity via Architectural Design for Federated Visual Recognition. _NeurIPS_ 36 (2024). 

- [45] Tao Qi et al. 2023. Differentially private knowledge transfer for federated learning. _Nat Commun_ 14 (2023), 3785. 

- [46] Xinchi Qiu, Titouan Parcollet, Javier Fernández-Marqués, Pedro P. B. de Gusmao, Yan Gao, Daniel J. Beutel, Taner Topal, Akhil Mathur, and Nicholas D. Lane. 2023. A First Look into the Carbon Footprint of Federated Learning. _J. Mach. Learn. Res._ 24 (2023), 129:1–129:23. 

- [47] René Ranftl, Alexey Bochkovskiy, and Vladlen Koltun. 2021. Vision transformers for dense prediction. In _ICCV_ . 12179–12188. 

- [48] Sebastian Ruder. 2017. An overview of multi-task learning in deep neural networks. _CoRR_ abs/1706.05098 (2017). 

- [49] Lothar Sachs. 2013. _Angewandte Statistik: Statistische Methoden und ihre Anwendungen_ . Springer-Verlag. 

- [50] Mingjia Shi et al. 2023. PRIOR: Personalized Prior for Reactivating the Information Overlooked in Federated Learning.. In _NeurIPS_ . 

- [51] Nathan Silberman et al. 2012. Indoor segmentation and support inference from rgbd images. In _ECCV_ . 746–760. 

- [52] Virginia Smith, Chao-Kai Chiang, Maziar Sanjabi, and Ameet Talwalkar. 2017. Federated Multi-Task Learning. In _NeurIPS_ . 4424–4434. 

- [53] Guolei Sun, Thomas Probst, Danda Pani Paudel, Nikola Popović, Menelaos Kanakis, Jagruti Patel, Dengxin Dai, and Luc Van Gool. 2021. Task switching network for multi-task learning. In _ICCV_ . 8291–8300. 

- [54] Alysa Ziying Tan, Han Yu, Lizhen Cui, and Qiang Yang. 2022. Towards Personalized Federated Learning. _IEEE Transactions on Neural Networks and Learning Systems_ (2022), 1–17. 

- [55] Simon Vandenhende et al. 2021. Multi-task learning for dense prediction tasks: A survey. _IEEE TPAMI_ 44, 7 (2021), 3614–3633. 

- [56] Wenhai Wang et al. 2021. Pyramid vision transformer: A versatile backbone for dense prediction without convolutions. In _ICCV_ . 568–578. 

- [57] Stefanie Warnat-Herresthal et al. 2021. Swarm Learning for Decentralized and Confidential Clinical Machine Learning. _Nature_ 594, 7862 (2021), 265–270. 

- [58] Chuhan Wu et al. 2022. Communication-Efficient Federated Learning via Knowledge Distillation. _Nature Communications_ 13, 1 (2022), 2032. 

- [59] Chuhan Wu et al. 2022. A Federated Graph Neural Network Framework for Privacy-Preserving Personalization. _Nature Communications_ 13 (2022), 3091. 

- [60] Xiaosong Wu et al. 2023. Wearable in-sensor reservoir computing using optoelectronic polymers with through-space charge-transport characteristics for multi-task learning. _Nat Commun_ 14 (2023), 468. 

- [61] Qiang Yang, Yang Liu, Tianjian Chen, and Yongxin Tong. 2019. Federated Machine Learning: Concept and Applications. _ACM Trans. Intell. Syst. Technol._ 10, 2 (2019), 12:1–12:19. 

- [62] Hanrong Ye and Dan Xu. 2022. Inverted pyramid multi-task transformer for dense scene understanding. In _ECCV_ . 514–530. 

- [63] Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn. 2020. Gradient Surgery for Multi-Task Learning. In _NeurIPS_ . 

- [64] Angela Zhang et al. 2022. Shifting Machine Learning for Healthcare from Development to Deployment and from Models to Data. _Nature Biomedical Engineering_ (2022), 1–16. 

- [65] Weiming Zhuang, Yonggang Wen, Lingjuan Lyu, and Shuai Zhang. 2023. MAS: Towards Resource-Efficient Federated Multiple-Task Learning. In _ICCV_ . 23414– 23424. 

