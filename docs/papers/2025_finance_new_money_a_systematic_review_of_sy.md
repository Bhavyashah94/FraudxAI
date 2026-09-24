---
title: "New Money: A Systematic Review of Synthetic Data Generation for Finance"
authors: "finance"
year: 2025
arxiv_id: "2510.26076"
original_file: "2510.26076.pdf"
pdf_path: "docs/papers\2025_finance_new_money_a_systematic_review_of_sy.pdf"
---

# New Money: A Systematic Review of Synthetic Data Generation for Finance

**Authors:** Finance et al.  
**Year:** 2025 | **arXiv:** [`2510.26076`](https://arxiv.org/abs/2510.26076)  
**Local PDF:** [`2025_finance_new_money_a_systematic_review_of_sy.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2025_finance_new_money_a_systematic_review_of_sy.pdf)

---

# New Money: A Systematic Review of Synthetic Data Generation for Finance 

James Meldrum<sup>1</sup> , Basem Suleiman<sup>2*</sup> , Fethi Rabhi<sup>2</sup> , Muhammad Johan Alibasa<sup>3</sup> 

- 1School of Computer Science, University of Sydney, Sydney, NSW, Australia. 

> 2Computer Science and Engineering, University of New South Wales, Sydney, NSW, Australia. 

> 3Faculty of Information Technology, Monash University Indonesia, Tangerang, Banten, Indonesia. 

- *Corresponding author(s). E-mail(s): b.suleiman@unsw.edu.au; Contributing authors: jmel2994@uni.sydney.edu.au; 

   - f.rabhi@unsw.edu.au; johan.alibasa@monash.edu; 

##### **Abstract** 

Synthetic data generation has emerged as a promising approach to address the challenges of using sensitive financial data in machine learning applications. By leveraging generative models, such as Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs), it is possible to create artificial datasets that preserve the statistical properties of real financial records while mitigating privacy risks and regulatory constraints. Despite the rapid growth of this field, a comprehensive synthesis of the current research landscape has been lacking. This systematic review consolidates and analyses 72 studies published since 2018 that focus on synthetic financial data generation. We categorise the types of financial information synthesised, the generative methods employed, and the evaluation strategies used to assess data utility and privacy. The findings indicate that GAN-based approaches dominate the literature, particularly for generating time-series market data and tabular credit data. While several innovative techniques demonstrate potential for improved realism and privacy preservation, there remains a notable lack of rigorous evaluation of privacy safeguards across studies. By providing an integrated overview of generative techniques, applications, and evaluation methods, this review highlights critical research gaps and offers guidance for future work aimed at developing robust, privacy-preserving synthetic data solutions for the financial domain. 

1 

**Keywords:** financial data, synthetic data generation, generative adversarial networks, systematic review 

## **1 Introduction** 

Financial technology (Fintech) and the application of machine learning (ML) in the financial sector have expanded substantially over the past two decades (Yeo et al., 2025). Financial institutions increasingly rely on data-driven models for credit evaluation, fraud detection, algorithmic trading, and customer management. In 2020, 83% of financial organisations reported using machine learning within their operations (horacio, 2019), and spending on AI in the sector exceeded USD $11 billion, with projections rising to USD $31 billion by 2025 (Bouzarouata, 2023). 

The effective use of financial data enables more informed decisions and improved services (Soon, 2021). However, much of this data is highly sensitive, including personal identifiers, transaction records, and credit histories. Regulatory frameworks such as the GDPR in Europe and regulations enforced by ASIC in Australia impose strict controls on how this information can be used and shared (Strelcenia & Prakoonwit, 2023). 

Synthetic data generation, which leverages generative models to produce artificial datasets, offers a promising approach to address these challenges (Martineau & Feris, 2021). Synthetic datasets can replicate the statistical properties of real data while reducing privacy risks and enabling broader sharing and experimentation. In practice, generative models can create nearly unlimited quantities of realistic data that are unlinked to any specific individuals. Despite these advantages, research into synthetic data has historically focused on text and image generation, particularly in healthcare. Comprehensive analyses of synthetic data generation techniques applied to financial datasets remain limited. 

This observation motivates the present study. Specifically, we aim to address the following research questions: 

1. What types of financial data have been synthesised in the current literature? 

2. Which generative models have been employed for synthetic financial data generation? 

3. What evaluation methods have been used to assess the quality and privacy of synthetic datasets? 

The contributions of this review are threefold. First, we provide an exhaustive synthesis of research on synthetic financial data generation published since 2018. Second, we critically analyse the generative techniques applied to a range of data types and financial tasks. Third, we review evaluation practices to inform standardisation efforts and highlight areas for further research. 

2 

## **2 Related Work** 

### **2.1 Background and Key Concepts** 

Synthetic data generation refers to the use of generative models to create artificial datasets that replicate important statistical properties of original data while reducing privacy risks (Martineau & Feris, 2021). In the financial sector, such datasets can support model development, address class imbalance, and enable compliant data sharing. 

Two main classes of generative models are commonly applied in this domain. Generative Adversarial Networks (GANs) consist of a generator and a discriminator trained adversarially to produce realistic samples (Goodfellow et al., 2020). Variational Autoencoders (VAEs) encode data into latent probabilistic representations and reconstruct synthetic samples from this space (Kingma & Welling, 2013). Other techniques, including style transfer and privacy-preserving frameworks such as Private Aggregation of Teacher Ensembles (PATE), have been investigated in specific contexts but remain less widely adopted in finance. 

Synthetic datasets in finance are typically tabular or time-series. Evaluation criteria commonly include statistical similarity to real data distributions, machine learning efficacy (e.g., predictive performance), and privacy preservation (e.g., preventing re-identification). This subsection provides essential context for understanding the generative methods and evaluation strategies assessed in the remainder of this review. 

### **2.2 Synthetic Data Generation for Finance** 

A growing body of research has examined the use of synthetic data generation to address privacy, regulatory, and technical challenges in financial machine learning. Several studies have highlighted that financial data are among the most sensitive forms of information, subject to strict legal requirements such as the GDPR and requiring robust privacy safeguards during analysis and model development (Assefa et al., 2020; Strelcenia & Prakoonwit, 2023). 

Early work in this area often focused on describing motivations and outlining potential benefits, including improved data sharing, mitigation of class imbalance, and enhanced machine learning performance (Assefa et al., 2020). More recent studies have explored specific generative techniques, with Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs) emerging as the most widely adopted methods for synthesising tabular and time-series financial data (Eckerli & Osterrieder, 2021; Singh & Ogunfunmi, 2022; Strelcenia & Prakoonwit, 2023). 

Although GAN-based approaches have demonstrated promising results, including realistic synthetic samples for training predictive models and simulating trading activity, their applications often lack rigorous evaluation of privacy preservation and data utility (Eckerli & Osterrieder, 2021; Jordon et al., 2022). Additionally, VAEs, while theoretically well-suited for generating structured data, appear to be infrequently used in financial contexts, with only a few studies applying them to stock option data or credit risk modelling (Singh & Ogunfunmi, 2022). 

3 

Beyond the technical aspects, several publications have discussed practical and regulatory considerations when adopting synthetic data in financial organisations. For example, authors have emphasised the importance of clear policies on data retention and sharing, as well as mechanisms to ensure stakeholder trust and regulatory compliance (James, Harbron, Branson, & Sundler, 2021). However, these contributions typically stop short of offering detailed frameworks or comparative evaluations of generative models in financial settings. 

### **2.3 Reviews of Synthetic Data Generation** 

More general surveys of synthetic data generation have been published across domains, especially in healthcare and image analysis. Some reviews have outlined a broad taxonomy of methods, including GANs, VAEs, and hybrid approaches, but tend to focus primarily on computer vision tasks (Figueira & Vaz, 2022). Others have discussed the potential of synthetic data to mitigate data scarcity and enhance machine learning workflows, while acknowledging that domain-specific challenges remain underexplored (Abufadda & Mansour, 2021; Lu et al., 2023). 

For instance, Hernandez, Epelde, Alberdi, Cilla, and Rankin (2022) conducted a systematic review of synthetic data generation for tabular health records and found that GANs generally outperform other techniques in terms of statistical similarity and model training efficacy. However, their analysis also revealed a lack of standardised metrics for assessing privacy and data resemblance, a limitation echoed in several other studies (Reiter, 2023). 

In financial applications, existing reviews have primarily provided high-level overviews without a comprehensive, structured comparison of methods and evaluation strategies (Jordon et al., 2022; Kharkiv, 2023). This gap highlights the need for a focused synthesis of synthetic data generation techniques and practices specific to finance, which is the aim of this work. 

## **3 Methodology** 

This review critically analyses the current state of research on synthetic data generation for financial applications. Following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines (Moher et al., 2009), the review was conducted in four stages, illustrated in Figure 1. First, a two-stage search strategy was developed across five research databases. Second, the search was executed to identify and screen studies relevant to the research questions. Third, data were extracted from the included studies. Finally, the extracted information was synthesised and analysed. 

### **3.1 Search Strategy** 

To identify all potentially relevant studies, the search was conducted in two phases: a database search and a snowball search. 

#### **3.1.1 Database Search** 

Five databases were queried: 

4 



**Fig. 1** Overview of the systematic review process. 

1. ACM Digital Library 

2. IEEE Xplore 

3. Scopus 

4. SpringerLink 

5. Web of Science 

Search strings combined keywords related to synthetic data generation and finance. A study was considered for inclusion if at least one keyword from each category appeared in the title, abstract, or keyword list: 

1. Synthetic Data Generation: 

   - “data generat*” 

   - “synthetic data*” 

   - “generated data*” 

   - “artificial data*” 

2. Finance: 

   - “financ*” 

   - “econom*” 

   - “bank*” 

   - “stock*” 

Where possible, filters were applied to limit results by publication date and language. 

#### **3.1.2 Snowball Search** 

After the database search, forward and backward snowballing was performed (Wohlin, 2014). References cited by included studies (backward snowballing) and studies citing them (forward snowballing) were reviewed iteratively until no new relevant publications were identified. All studies identified through snowballing were screened with the same criteria as the database search. 

5 

### **3.2 Screening Strategy** 

Screening was conducted in two stages to assess relevance and quality. Prior to screening, two exclusion criteria were enforced using database filters: 

- Studies published before 2018 were excluded to ensure coverage of recent advancements. 

- Studies not published in English were excluded due to language limitations. 

#### **3.2.1 Title and Abstract Screening** 

In the first phase, titles and abstracts were reviewed to exclude clearly irrelevant studies. The criteria applied were: 

- Studies explicitly focused on fields unrelated to finance or computer science were excluded. 

- Studies that did not mention synthetic data generation or related terms were excluded. 

- Studies that did not mention a research focus relevant to finance or computer science were excluded. 

- Studies that explicitly described the generation of exclusively non-financial data were excluded. 

#### **3.2.2 Full-Text Screening** 

Remaining studies were assessed in full text against the following criteria: 

- Studies must describe the generation of financial (or closely related) data. 

- Studies must protect sensitive or personally identifiable information. 

- Studies must state the data generation method used. 

- Studies generating data not based on existing datasets were excluded. 

- Studies focused exclusively on minority oversampling, forecasting, or unrelated machine learning tasks were excluded. 

### **3.3 Data Extraction** 

For each included study, data were extracted to address the research questions. Table 1 summarises the data points collected. 

### **3.4 Data Synthesis** 

Data synthesis involved categorising and analysing the extracted data by attributes including generative techniques, applications, evaluation methods, and publication year. Results were organised into tables and visualisations to support interpretation and discussion. Data processing and analysis were conducted using Microsoft Excel and Python, with libraries including Pandas, Matplotlib, and Plotly. 

6 

|**Research**<br>**Question**|**Data Points Extracted**|
|---|---|
|RQ1|Data types synthesised (e.g., time series, tabular); financial applications tar-<br>geted (e.g., stock exchange, transactions).|
|RQ2|Type of generative techniques used; specific implementations.|
|RQ3|Evaluation focus (statistical similarity, machine learning efficacy, privacy<br>preservation); metrics and methods employed (e.g., visual inspection, F1<br>score, comparisons to baselines).|



**Table 1** Summary of data points extracted from included studies. 

## **4 Results** 

### **4.1 Study Selection and Collection** 

In total, we collected 72 studies focused on the generation of synthetic financial data across a diverse range of applications within the industry. Figure 2 illustrates the process of study identification, screening, and inclusion, as described in Section 3. From the initial retrieval of studies, the majority were excluded as irrelevant to the review’s focus, with 3,246 records removed prior to full-text screening. 

Notably, most of the included studies were identified during the snowball search phase rather than through the initial database queries. This likely reflects a gap between the terminology used in search strategies, where finance-specific keywords were essential, and the way many authors report their research. In many cases, financial applications of synthetic data were only mentioned within the methodology sections rather than in titles, abstracts, or keywords. 

The number of relevant publications has grown steadily over recent years, as shown in Figure 3. One exception is 2020, when only nine studies were published, potentially due to the disruption caused by the COVID-19 pandemic. The relatively lower count in 2023 is attributable to the data collection occurring during the first half of that year. Overall, these results indicate a consistent and increasing research interest in the use of synthetic data generation for financial applications. 

### **4.2 What financial information has been synthesised throughout the relevant literature?** 

#### **4.2.1 Market Data** 

We find the generation of univariate or multivariate stock market data to be the most common application of synthetic data generation within our collected studies. Most studies synthesising stock market data generated a combination of (or all of) daily opening, closing, high and low stock prices, adjusted closing prices, volume, and turnover rate for one or multiple stocks and indexes. We note that for studies generating univariate stock prices, we recorded this as daily closing prices unless stated otherwise. Many of these studies used the synthetic market data to train machine learning models such as trading agents or market price forecasting systems. 

7 



**Fig. 2** PRISMA flow diagram. 

Market order information involves the synthesis of data representing stock order streams (buy/sell signals, price, volume, and similar features). Coletta et al. (2021) and Coletta et al. (2022) used a single generative model to produce order streams for the entire market that react to the activity of experimental agents, as an alternative to simulating many trading agents independently. This approach enables the creation of realistic market scenarios for testing trading strategies. J. Li et al. (2020) similarly generated market order streams with historical dependencies, aiming to improve the ability to analyse sensitive stock market information. 

8 



**Fig. 3** Number of studies collected by published year. 

A related time-series application is the synthesis of exchange information. A number of the collected studies synthesised correlated exchange rates between currencies of two or more countries. For example, Da Silva and Shi (2019) generated realistic exchange rates between AUD and USD. Boursin et al. (2022) similarly produced correlated prices of coal, gas, electricity, and oil to perform hedging on futures contracts using deep learning. Carvajal Patino and Ramos Pollan (2022) synthesised both currency and commodity data in the form of correlated exchange rates between the price of gold, USD, and EUR. 

#### **4.2.2 Credit and Loan Data** 

A large portion of the literature also focuses on synthesising credit and loan data. As opposed to market data, which is mostly time series, credit data is primarily mixedtype tabular data. A common use case is the detection of fraudulent behaviours. We found that nine studies generated synthetic credit and loan data for this purpose. The other most frequent application was assessing customer credit risk. This is consistent with the fact that personal credit information is highly sensitive, and the ability to use 

9 

|**ID**|**Citation**|**Title**|**Task**|
|---|---|---|---|
|14|Kegel, Hahmann,<br>and Lehner<br>(2018)|Feature-Based Comparison and Generation of<br>Time Series|Not Specified|
|30|Park et al. (2018)|Data Synthesis Based on Generative Adversarial<br>Networks|Retail Prices|
|34|Xiao et al. (2018)|Learning Conditional Generative Models for<br>Temporal Point Processes|Stock Market|
|39|Simonetto (2018)|Generating Spiking Time Series with Generative<br>Adversarial Networks: An Application on Banking<br>Transactions|Transaction|



**Table 2** Studies collected from 2018. 

synthetic versions without risking privacy breaches is valuable. A similar motivation applies to the four studies that synthesised personal loan data. 

#### **4.2.3 Other Applications** 

Among the remaining applications, the generation of synthetic transaction data was the most common, appearing in seven studies. Four studies generated marketing and customer churn data for banking institutions. Flaig and Junike (2022) created synthetic economic scenarios for insurance risk calculations. Interestingly, only one study generated synthetic tax data, which represents a potentially important area for future work given the sensitivity of such records. 

Overall, we find that the main applications of synthetic financial data in the literature are in stock and market data generation, credit risk, and credit fraud detection. Opportunities for future work include further generation of transaction, retail, and tax data to broaden the applicability of synthetic data across financial institutions. 

### **4.3 What generative models have been used for the generation of financial data?** 

To answer this research question, we isolated the studies that contained experiments assessing generative techniques for synthetic data generation. We summarised the methods discussed across these studies in five groups, based on the taxonomy illustrated in Figure 4: Conditional GANs, Vanilla and Wasserstein GANs, Other GANs, Autoencoders, and Other Techniques. 

#### **4.3.1 What are the different types of techniques researched?** 

The taxonomy in Figure 4 illustrates that Generative Adversarial Networks (GANs) are by far the most heavily researched family of methods for financial synthetic data generation. Within GANs, Conditional GANs, Vanilla GANs, and Wasserstein GANs are the most prevalent variants. Autoencoders are the next most common, particularly 

10 

|**ID**|**Citation**|**Title**|**Task**|
|---|---|---|---|
|12|Raimbault (2019)|Second-Order Control of Complex Systems with<br>Correlated Synthetic Data|Currency<br>Exchange|
|13|K. Zhang, Zhong,<br>Dong, Wang, and<br>Wang (2019)|Stock Market Prediction Based on Generative<br>Adversarial Network|Stock Market|
|17|Jordon, Yoon,<br>and Van<br>Der Schaar<br>(2018)|Pate-GAN: Generating Synthetic Data with<br>Differential Privacy Guarantees|Credit|
|18|Koshiyama,<br>Firoozye, and<br>Treleaven (2021)|Generative Adversarial Networks for Financial<br>Trading Strategies Fine-Tuning and Combination|Currency<br>Exchange,<br>Stock Market|
|20|Wiese, Knobloch,<br>Korn, and<br>Kretschmer<br>(2020)|Quant GANs: Deep Generation of Financial Time<br>Series|Stock Market|
|21|Yoon, Jarrett,<br>and Van der<br>Schaar (2019)|Time-Series Generative Adversarial Networks|Stock Market|
|24|Da Silva and Shi<br>(2019)|Style Transfer with Time Series: Generating<br>Synthetic Financial Data|Currency<br>Exchange|
|27|Fu, Chen, Zeng,<br>Zhuang, and<br>Sudjianto (2019)|Time Series Simulation by Conditional Generative<br>Adversarial Net|Stock Market|
|28|Abay, Zhou,<br>Kantarcioglu,<br>Thuraisingham,<br>and Sweeney<br>(2019)|Privacy Preserving Synthetic Data Release Using<br>Deep Learning|Credit|
|32|Xu, Skoularidou,<br>Cuesta-Infante,<br>and<br>Veeramachaneni<br>(2019)|Modeling Tabular Data Using Conditional GAN|Credit|
|36|de Meer Pardo<br>(2019)|Enriching Financial Datasets with Generative<br>Adversarial Networks|Stock Market|
|38|Brenninkmeijer<br>and Amro (2019)|On the Generation and Evaluation of Tabular<br>Data Using GANs|Credit,<br>Transaction|
|66|Miok, Nguyen-<br>Doan, Zaharie,<br>and Robnik-<br>ˇSikonja (2019)|Generating Data Using Monte Carlo Dropout|Credit|
|67|Takahashi, Chen,<br>and Tanaka-Ishii<br>(2019)|Modeling Financial Time Series with Generative<br>Adversarial Networks|Stock Market|



**Table 3** Studies collected from 2019. 

11 

|**ID**|**Citation**|**Title**|**Task**|
|---|---|---|---|
|11|Z. Zhang et al.<br>(2020)|A Generative Adversarial Network Based Method<br>for Generating Negative Financial Samples|Transaction|
|19|J. Li, Wang, Lin,<br>Sinha, and<br>Wellman (2020)|Generating Realistic Stock Market Order Streams|Market Orders|
|22|Efimov, Xu,<br>Kong, Nefedov,<br>and<br>Anandakrishnan<br>(2020)|Using Generative Adversarial Networks to<br>Synthesize Artificial Financial Datasets|Not Specified|
|25|van Bree (2020)|Unlocking the Potential of Synthetic Tabular Data<br>Generation with Variational Autoencoders|Credit|
|31|Padhi et al.<br>(2021)|Tabular Transformers for Modeling Multivariate<br>Time Series|Transaction|
|33|Kondratyev and<br>Schwarz (2020)|The Market Generator|Currency<br>Exchange|
|37|Karlsson (2020)|Synthesis of Tabular Financial Data Using<br>Generative Adversarial Networks|Marketing|
|42|Vega-M´arquez,<br>Rubio-Escudero,<br>Riquelme, and<br>Nepomuceno-|Creation of Synthetic Data with Conditional<br>Generative Adversarial Networks|Credit|
||Chamorro (2020)|||
|65|Goos et al.(2020)|Privacy-Preserving Anomaly Detection Using<br>Synthetic Data|Transaction|



**Table 4** Studies collected from 2020. 

Variational Autoencoders, while a variety of other techniques, including Generative Moment Matching Networks and transformers, have also been explored. 

**Conditional GANs** : Conditional GANs (CGANs) generate data conditioned on auxiliary information, making them well suited for datasets with categorical or structured attributes. Across our collection, five main variants of Conditional GANs were assessed (Table 12). 

STOCKGAN (J. Li et al., 2020) is designed specifically for generating realistic stock market orders by capturing historical dependencies. Compared to Variational Autoencoders and Deep Convolutional GANs, STOCKGAN showed a significant performance advantage in Kolmogorov–Smirnov distance but was not evaluated for privacy preservation or downstream ML performance. 

SIGCWGAN (Liao et al., 2020) and RCGAN (Esteban, Hyland, & R¨atsch, 2017) were assessed together by Gatta et al. (2022), who found SIGCWGAN particularly promising for privacy preservation (with a perfect innovation score) but less competitive in predictive performance. 

CTGAN and CTab-GAN were primarily applied to tabular credit and transaction data. CTGAN (Xu et al., 2019) demonstrated strong improvements over benchmarks such as TGAN in modelling mixed-type data. CTab-GAN (Zhao et al., 2021) further 

12 

|**ID**|**Citation**|**Title**|**Task**|
|---|---|---|---|
|2|Coletta et al.<br>(2021)|Towards Realistic Market Simulations: A<br>Generative Adversarial Networks Approach|Market Orders|
|9<br>10|Liao et al. (2020)<br>Park, Gu, and<br>Yoo (2021)|Sig-Wasserstein GANs for Time Series Generation<br>Synthesizing Individual Consumers’ Credit<br>Historical Data Using Generative Adversarial<br>Networks|Stock Market<br>Loan, Credit|
|23|Desai, Freeman,<br>Wang, and<br>Beaver (2021)|TimeVAE: A Variational Auto-Encoder for<br>Multivariate Time Series Generation|Stock Market|
|26|Dogariu, S¸tefan,<br>Boteanu, Lamba,<br>and Ionescu<br>(2021)|Towards Realistic Financial Time Series<br>Generation via Generative Adversarial Learning|Stock Market|
|29|Ljung (2021)|Synthetic Data Generation for the Financial<br>Industry Using Generative Adversarial Networks|Marketing|
|35|Zhao, Kunar,<br>Birke, and Chen<br>(2021)|CTAB-GAN: Effective Table Data Synthesizing|Loan, Credit|
|43|Kim, Jeon, Lee,<br>Hyeong, and<br>Park (2021)|OCT-GAN: Neural ODE-Based Conditional<br>Tabular GANs|Credit|
|44|Long et al.(2021)|G-PATE: Scalable Differentially Private Data<br>Generator via Private Aggregation of Teacher<br>Discriminators|Credit|
|45|B. Li, Luo, Qin,<br>and Pan (2021)|Improving GAN with Inverse Cumulative<br>Distribution Function for Tabular Data Synthesis|Credit|
|46|Van Breugel,<br>Kyono,<br>Berrevoets, and<br>Van der Schaar<br>(2021)|DECAF: Generating Fair Synthetic Data Using<br>Causally-Aware Generative Networks|Credit|
|52|Remlinger,<br>Mikael, and Elie<br>(2022)|Conditional Loss and Deep Euler Scheme for Time<br>Series Generation|Stock Market,<br>Other|
|56|J. Li, Liu, Yang,<br>and Han (2021)|A Credit Risk Model with Small Sample Data<br>Based on G-XGBoost|Credit|
|59|Pei, Yang, Liu,<br>and Li (2021)|Towards Generating Real-World Time Series Data|Stock Market|
|60|Yin et al. (2021)|Multi-Attention Generative Adversarial Network<br>for Multivariate Time Series Prediction|Stock Market|
|68|Alaa, Chan, and<br>van der Schaar<br>(2021)|Generative Time-Series Modeling with Fourier<br>Flows|Stock Market|
|73|Platzer and<br>Reutterer (2021)|Holdout-Based Empirical Assessment of<br>Mixed-Type Synthetic Data|Credit, Other|
|74|Ge, Mohapatra,<br>He, and Ilyas<br>(2020)|Kamino: Constraint-Aware Differentially Private<br>Data Synthesis|Tax|



**Table 5** Studies collected from 2021. 

13 

|**ID**|**Citation**|**Title**|**Task**|
|---|---|---|---|
|0|Liu, Ventre, and<br>Polukarov (2022)|Synthetic Data Augmentation for Deep Reinforcement<br>Learning in Financial Trading|Stock Market|
|1|El-Laham and<br>Vyetrenko (2022)|StyleTime: Style Transfer for Synthetic Time Series<br>Generation|Stock Market|
|5|Dogariu et al. (2022)|Generation of Realistic Synthetic Financial Time-Series|Stock Market|
|6|Coletta, Moulin,<br>Vyetrenko, and Balch<br>(2022)|Learning to Simulate Realistic Limit Order Book Markets<br>from Data as a World Agent|Market Orders|
|7|Azamuke,<br>Katarahweire, and<br>Bainomugisha (2022)|Scenario-Based Synthetic Dataset Generation for Mobile<br>Money Transactions|Transaction|
|8|Rizzato, Morizet,<br>Mar´echal, and Geissler<br>(2022)|Stress Testing Electrical Grids: Generative Adversarial<br>Networks for Load Scenario Generation|Commodities|
|16|Vega-M´arquez,<br>Rubio-Escudero, and<br>Nepomuceno-<br>Chamorro (2022)|Generation of Synthetic Data with Conditional Generative<br>Adversarial Networks|Credit|
|41|Tan, Zhang, Zhao, and<br>Wang (2022)|DeepPricing: Pricing Convertible Bonds Based on Financial<br>Time-Series Generative Adversarial Networks|Stock Market|
|47|Lee, Hyeong, Jeon,<br>Park, and Cho (2021)|Invertible Tabular GANs: Killing Two Birds with One Stone<br>for Tabular Data Synthesis|Credit|
|48|Duan et al. (2022)|HT-Fed-GAN: Federated Generative Model for<br>Decentralized Tabular Data Synthesis|Credit|
|50|Nickerson et al. (2022)|Banksformer: A Deep Generative Model for Synthetic<br>Transaction Sequences|Transaction|
|53|Flaig and Junike<br>(2022)|Scenario Generation for Market Risk Models Using<br>Generative Neural Networks|Economic Scenario|
|54|Allouche, Girard, and<br>Gobet (2022)|EV-GAN: Simulation of Extreme Events with ReLU Neural<br>Networks|Stock Market|
|55|Hayashi (2022)|Fractional SDE-Net: Generation of Time Series Data with<br>Long-Term Memory|Stock Market|
|61|Rizzato, Wallart,<br>Geissler, Morizet, and<br>Boumlaik (2023)|Generative Adversarial Networks Applied to Synthetic<br>Financial Scenarios Generation|Currency Exchange,<br>Commodities, Credit,<br>Stock Market|
|62|Gatta et al. (2022)|Neural Networks Generative Models for Time Series|Stock Market|
|63|Jeon, Kim, Song, Cho,<br>and Park (2022)|GT-GAN: General Purpose Time Series Synthesis with<br>Generative Adversarial Networks|Stock Market|
|64|Juneja, Bajaj, and<br>Sethi (2023)|Synthetic Time Series Data Generation Using TimeGAN<br>with Synthetic and Real-Time Data Analysis|Stock Market|
|69|Cramer et al. (2022)|Validation Methods for Energy Time Series Scenarios from<br>Deep Generative Models|Commodities|
|71|Carvajal Patino and<br>Ramos Pollan (2022)|Synthetic Data Generation with Deep Generative Models to<br>Enhance Predictive Tasks in Trading Strategies|Commodities,<br>Currency Exchange|
|72|Boursin, Remlinger,<br>and Mikael (2022)|Deep Generators on Commodity Markets: Application to<br>Deep Hedging|Commodities|



**Table 6** Studies collected from 2022. 

14 

|**ID**|**Citation**|**Title**|**Task**|
|---|---|---|---|
|15|Y. Zhang, Zaidi,<br>Zhou, and Li<br>(2023)|Interpretable Tabular Data Generation|Loan, Credit|
|40|Yadav, Gaur,<br>Fatima, and<br>Sarwar (2023)|Qualitative and Quantitative Evaluation of<br>Multivariate Time-Series Synthetic Data<br>Generated Using MTS-TGAN: A Novel Approach|Stock Market|
|51|J.L. Wu, Tang,<br>and Hsu (2023)|A Prediction Model of Stock Market Trading<br>Actions Using Generative Adversarial Network<br>and Piecewise Linear Representation Approaches|Stock Market|
|57|Tang, Zhang, and<br>Zhang (2023)|A Recurrent Neural Network Based Generative<br>Adversarial Network for Long Multivariate Time<br>Series Forecasting|Currency<br>Exchange|
|58|Ahmed and<br>Schmidt-Thieme<br>(2023)|Sparse Self-Attention Guided Generative<br>Adversarial Networks for Time-Series Generation|Stock Market|
|70|J. Wu,<br>Plataniotis, Liu,<br>Amjadian, and<br>Lawryshyn<br>(2023)|Interpretation for Variational Autoencoder Used to<br>Generate Financial Synthetic Tabular Data|Other, Loan|



**Table 7** Studies collected from 2023. 

|**Category**|**Task**|**Count**|**Studies ID**|
|---|---|---|---|
||Open|13|[0] [13] [21] [23] [26] [40] [51] [52] [58] [59] [62]<br>[63] [64]|
||Close|25|[0] [1] [5] [9] [13] [18] [20] [21] [23] [26] [27]<br>[36] [40] [51] [52] [54] [55] [58] [59] [60] [61]<br>|
|Stock Market|High|13|[62] [63] [64] [67]<br>[0] [13] [21] [23] [26] [40] [51] [52] [58] [59] [62]<br>[63] [64]|
||Low|13|[0] [13] [21] [23] [26] [40] [51] [52] [58] [59] [62]<br>[63] [64]|
||Adjusted Close|10|[0] [21] [23] [40] [51] [52] [58] [59] [63] [64]|
||Volume|12|[0] [13] [21] [23] [40] [51] [52] [58] [59] [62] [63]<br>[64]|
||Turnover Rate|1|[13]|
||5-Day Average|1|[13]|
||Transactions|1|[34]|
||Details Not<br>Specified|2|[41] [68]|
|Market Orders|Market Orders|3|[2] [6] [19]|
|Currency|Currency|7|[12] [18] [24] [33] [57] [61] [71]|
|Exchange|Exchange|||
|Commodities|Commodities|5|[8] [61] [69] [71] [72]|



**Table 8** Studies synthesising market data. 

15 

|**Category**|**Task**|**Count**|**Stu**|**dies **|**ID**|
|---|---|---|---|---|---|
||Credit Card|1|[10]|||
||Credit Risk|9|[10]|[16]|[28] [46] [47] [56] [61] [66] [73]|
|Credit|Credit (Not|2|[15]|[45]||
||Specified)|||||
||Credit Fraud|9|[17]|[25]|[32] [35] [38] [42] [43] [44] [48]|
||Personal Loan|4|[10]|[15]|[35] [70]|



**Table 9** Studies synthesising credit and loan data. 

|**Category**|**Task**|**Count**|**Stu**|**dies ID**|
|---|---|---|---|---|
||Transactions<br>Not Specified|7<br>2|[7] [<br>[14]|11] [31] [38] [39] [50] [65]<br> [22]|
||Marketing|4|[29]|[37] [70] [73]|
|Other|Churn|2|[29]|[70]|
||Retail Prices|2|[30]|[52]|
||Economic|1|[53]||
||Scenario||||
||Tax|1|[74]||



**Table 10** Studies applying synthetic data in other financial domains. 

|Method Type|Usages in Collected Literature|Percentage of All Method Usages|
|---|---|---|
|**GANs**|**76**|**73.8%**|
|CGANs|16|15.5%|
|V/WGANs|18|17.5%|
|Other GANs|42|40.8%|
|**Autoencoders**|**9**|**8.7%**|
|**Other**|**18**|**17.5%**|



**Table 11** Summary of generative technique usages in collected studies. Each usage is counted per study. For example, one method applied in two studies counts as two usages; two methods in one study count as two usages. 

extends this by encoding mixed variables, though specific performance on financial datasets was only reported in aggregate. 

**Vanilla and Wasserstein GANs** : Several studies compared Vanilla GANs with Wasserstein GAN variants, often finding the latter superior for capturing realistic time series and improving predictive performance. For example, Simonetto (2018) observed that WGAN-GP outperformed other GAN variants in both statistical similarity and machine learning efficacy when generating spiking time series. 

**Other GAN Variants** : Many less common GAN variants have been explored (Table 14). For example, TimeGAN (Yoon et al., 2019) was repeatedly observed to perform well across predictive and discriminative tasks, while FCGAN showed mixed 

16 



**Fig. 4** Sunburst chart of generative models used in collected studies. The outer layer shows the specific methods (with the number of studies in parentheses); the inner layer shows the overarching architectures. 

|**Model**|**Description**|**Stu**|**dies**|
|---|---|---|---|
|CGAN|Conditional GAN|[2] [|6] [10] [16] [18] [27] [42] [61]|
|STOCKGAN|Stock Market Order CGAN|[19]||
|CTGAN|Conditional Tabular GAN|[29]|[32] [35] [37]|
|SIGCWGAN|Signature Wasserstein CGAN|[62]||
|RCGAN|Recurrent Conditional GAN|[62]||



**Table 12** Conditional GANs used across studies. 

17 

|**Model**|**Description**|**Studies**|
|---|---|---|
|GAN|Generative Adversarial Network|[5] [26] [51] [53] [56] [71]|
|WGAN-GP|Wasserstein GAN with Gradient Penalty|[8] [36] [38] [39]|
|SIG-WGAN|Signature Wasserstein GAN|[9] [51]|
|WFCGAN|Wasserstein Fully Convolutional GAN|[26]|
|WGAN|Wasserstein GAN|[26] [37] [39] [51]|
|VAE+WGAN|VAE Generator within WGAN|[39]|



**Table 13** Vanilla and Wasserstein GANs. 

results, sometimes improving regression accuracy but often underperforming WGANs. PATE-GAN (Jordon et al., 2018) and G-PATE (Long et al., 2021) demonstrated the feasibility of achieving differential privacy with relatively limited performance degradation. 

**Autoencoders** : Autoencoders, especially VAEs, were primarily used for tabular or time series reconstruction. For example, Desai et al. (2021) introduced TimeVAE to incorporate trend and seasonality into the decoder, achieving comparable results to TimeGAN. Miok et al. (2019) evaluated Monte Carlo Dropout regularisation in VAEs and AEs, finding marginal improvements in some predictive tasks. 

**Other Techniques** : Some studies evaluated methods outside GANs and autoencoders, such as CEGEN, which outperformed GANs in discriminative and predictive metrics for time series (Remlinger et al., 2022). GMMN also achieved strong results for predictive performance. Finally, TABGPT (Padhi et al., 2021) demonstrated promising results for privacy-preserving tabular data generation. 

#### **4.3.2 How are different techniques used across different financial applications?** 

Table 17 summarises the distribution of generative techniques across financial applications. The synthesis of stock market data dominates the literature. Across 34 distinct generative approaches, 27 are GAN variants, including 19 outside the common Conditional, Vanilla, or Wasserstein families. TimeGAN appears most frequently, used in four studies, followed by Vanilla GAN and Conditional GAN, each applied in three studies. This shows that stock market data has been the main focus of synthetic financial data research over the last five to six years. 

A similar pattern is found in studies on currency and commodity data. Although only nine and ten studies focus on these areas, all major categories of generative models are represented. Apart from CGAN, which is applied in two currency studies, most techniques are used only once. This suggests that research in these areas is still exploratory. Some studies generate both currency and commodity datasets, reflecting their related time-series properties. 

For market orders, two studies applied Conditional GANs, including the specialised StockGAN model designed to capture order flow behaviour. Credit and loan data show more diversity. Three autoencoder variants were used for credit risk prediction, and two for fraud detection. However, GANs remain the most common choice overall, 

18 

|**Model Name**|**Description**|**Studies**|
|---|---|---|
|TIMEGAN|Time GAN|[0] [21] [62] [64] [72]|
|FCGAN|Fully Convolutional GAN|[5] [26] [71]|
|RNN-GAN|Recurrent Neural Network GAN|[11] [57]|
|LSTM-GAN|Long Short-Term Memory GAN|[13]|
|GANBLR|GAN inspired by Naive Bayes and Logistic Regression|[15]|
|PATE-GAN|Private Aggregation of Teacher Ensembles GAN|[17]|
|QUANT GAN|Quant GAN|[20]|
|DRAGAN|Deep Regret Analytic GAN|[22]|
|TABLE-GAN|Table GAN|[30]|
|GAN-LSTM|GAN-LSTM|[34]|
|RAGAN|Relativistic Average GAN|[36]|
|TGAN|Tabular GAN|[37]|
|TGAN-SKIP|TGAN with Skip Connections|[38]|
|MTS-TGAN|Multivariate Time Series TGAN|[40]|
|FINGAN|FinGAN|[41]|
|OCT-GAN|NODE-based Conditional Tabular GAN|[43]|
|G-PATE|Generative Private Aggregation of Teacher Ensembles|[44]|
|INVERSE-CDF GAN|Inverse Cumulative Distribution Function GAN|[45]|
|DECAF|Debiasing Causal Fairness GAN|[46]|
|IT-GAN|Invertible Tabular GAN|[47]|
|HT-FED-GAN|Horizontal Tabular Federated GAN|[48]|
|GAN-S|Signature GAN|[51]|
|LSGAN|Least Squares GAN|[51]|
|LSGAN-S|Signature Least Squares GAN|[51]|
|EV-GAN|Extreme-Value GAN|[54]|
|SPARSEGAN|Sparse Self-Attention Guided GAN|[58]|
|RTSGAN|Real World Time Series GAN|[59]|
|MAGAN|Multi-Attention GAN|[60]|
|BIGAN|Bidirectional GAN|[61]|
|GT-GAN|General Purpose Time Series GAN|[63]|
|FIN-GAN|FIN-GAN|[67]|
|COTGAN|Causal Optimal Transport GAN|[72]|
|SIGGAN|Signature GAN|[72]|



**Table 14** Other GAN architectures. 

and they are the only type of model used for generating personal loan, credit card, marketing, churn, and economic scenario data. 

Transaction data is the only application where non-GAN techniques appear more often than GANs. Of the eleven techniques identified, six are non-GAN architectures such as transformers and statistical models, while five are GAN-based. This reflects the challenges of transactional data, such as sparsity and categorical imbalance. In summary, GANs dominate across almost all applications, but there is no single application and generator combination that clearly stands out. This suggests both flexibility in generative modelling and an ongoing search for the most suitable methods for different types of financial data. 

19 

|**Model**|**Description**|**Studies**|
|---|---|---|
|VAE|Variational Autoencoder|[5] [71]|
|TimeVAE|Temporal Variational Autoencoder|[23]|
|DAE + Style Transfer|Denoising Autoencoder with Style Transfer|[24]|
|MCD-VAE|Monte Carlo Dropout VAE|[66]|



**Table 15** Autoencoders used across studies. 

|**Model**|**Description**|**Studies**|
|---|---|---|
|CEGEN|Conditional Euler Generator|[52] [72]|
|GMMN|Generative Moment Matching Network|[5] [62]|
|TABGPT|Transformer for Tabular Generation|[31]|
|Fourier Flows|Time Series via Fourier Transforms|[68]|
|Kamino|Constraint-Aware DP Synthesis|[74]|



**Table 16** Other generative techniques. 

### **4.4 What evaluation methods and criteria have been used?** 

This section analyses the methods used in the literature to evaluate the quality of synthetic financial data. We begin with the broader evaluation criteria applied across studies, followed by a discussion of the specific metrics used for each criterion. 

#### **4.4.1 General Evaluation Criteria** 

Table 18 summaries the general evaluation approaches reported in the collected studies. The results in the table indicate that Statistical Similarity and Machine Learning Efficacy are the two most common evaluation criteria. In addition, 61.6% of studies compare their methods against existing benchmarks. Privacy Preservation was explicitly assessed in only 12.3% of the literature. Finally, one study reported only descriptive observations of the generated data rather than formal evaluation. 

These findings highlight an imbalance in evaluation practices. While most research focuses on similarity to real data and downstream machine learning performance, considerably less attention is given to privacy preservation. This gap suggests opportunities for future work that more rigorously tests the privacy properties of synthetic financial data. 

#### **4.4.2 Statistical Similarity** 

A total of 58 studies in our collection evaluated synthetic financial data in terms of statistical similarity to real data. A common approach is to train a discriminator model to classify between real and synthetic samples, following the same principle as GAN training. Ideally, the classifier should perform no better than random guessing (i.e., an accuracy of 0.5). However, there is no consensus on the choice of classifier. For example, Yoon et al. (2019), Remlinger et al. (2022), and Pei et al. (2021) used LSTM-based 

20 

|**Application**|**Unique**<br>**Techniques**|**Top Categories**<br>**(Count)**|**Most Common**<br>**Techniques**|
|---|---|---|---|
|Stock Market|34|Other GAN (19),<br>Other (5), V/WGAN<br>(5), CGAN (3)|TimeGAN (4), GAN<br>(3), CGAN (3)|
|Market<br>Orders|2|CGAN (2)|CGAN (2),<br>STOCKGAN (1)|
|Currency<br>Exchange|9|Other GAN (3), AE<br>(2), Other (2)|CGAN (2)|
|Commodities|10|Other GAN (5),<br>V/WGAN (2)|WGAN-GP (1),<br>CGAN (1)|
|Credit Risk|9|AE (3), Other GAN<br>(3)|CGAN (3)|
|Credit Fraud|10|Other GAN (5), AE<br>(2)|CTGAN (2),<br>PATE-GAN (1)|
|Loan|3|CGAN (2)|CGAN (1), CTGAN<br>(1)|
|Transaction|11|Other (6),<br>V/WGAN (3)|WGAN-GP (2),<br>TABGPT (1)|
|Marketing|3|CGAN (1),<br>V/WGAN (1)|CTGAN (2)|
|Churn|1|CGAN (1)|CTGAN (1)|
|Retail Prices|2|Other GAN (1),<br>Other (1)|TABLE-GAN (1),<br>CEGEN (1)|
|Economic<br>Scenario|1|V/WGAN (1)|GAN (1)|
|Tax|1|Other (1)|Kamino (1)|



**Table 17** Generative techniques by financial application. 

|**Evaluation Criterion**|**Number of Studies**|**Percentage**|
|---|---|---|
|Statistical Similarity|58|79.5%|
|Machine Learning Efficacy|48|65.8%|
|Comparison to Benchmarks|45|61.6%|
|Privacy Preservation|11|12.3%|
|General Observation|1|1.4%|



**Table 18** Evaluation criteria used in the collected studies. 

21 



**Fig. 5** Example of a t-SNE plot comparing the performance of two generative techniques on stock market data (Yoon et al., 2019). 

classifiers, while others employed neural networks, logistic regression, random forests, support vector machines, or k-nearest neighbours. The lack of consistency suggests that multiple classifiers may need to be combined to strengthen evaluation results. 

Visual inspection was also widely applied to assess statistical similarity. Common practices included comparing cross-correlations, distributional shapes, t-SNE plots for high-dimensional structure, and side-by-side inspection of synthetic and real time series. Visualisation improves the interpretability of results and can support the explainability of model decisions (Kovalerchuk, Ahmad, & Teredesai, 2021). Distributional comparisons were the most frequent, with 18 studies analysing whether synthetic data preserved features such as heavy tails (Allouche et al., 2022; Dogariu et al., 2021; Karlsson, 2020; Ljung, 2021) or categorical frequency distributions. 

t-SNE plots were used in 11 studies to visualise high-dimensional relationships, making it easier to assess whether the structural properties of real data were maintained in synthetic datasets (see Figure 5). Correlation-based measures such as autocorrelation and pairwise feature correlations were also applied in 20 studies, reflecting the importance of capturing dependencies between variables in financial data. 

Distance metrics provided a more formal means of comparison. The most frequently applied measures included Kullback–Leibler (KL) divergence, Jensen–Shannon (JS) divergence, Kolmogorov–Smirnov (KS) statistic, and Earth Mover (EM) distance (also known as Wasserstein distance). KL and JS divergences were often used to compare probability distributions, while EM distance was applied to both time series and tabular data. The KS statistic was the most widely used single metric, appearing in seven studies across domains including stock market, transaction, currency exchange, and credit risk data. Its broad use underscores its general applicability for assessing distributional similarity. Overall, statistical similarity evaluations ranged from qualitative visual analysis to formal statistical tests. Table 19 summarises the main approaches observed across the literature. 

#### **4.4.3 Machine Learning Efficacy** 

With the rise of machine learning in financial organisations, machine learning efficacy has become a central focus for assessing the usability of generated financial data. In 

22 

|**Method**<br>Absolute Kendall Error|**Variation**<br>Absolute Kendall Error|**Number of Studies**<br>**Studies**<br>1<br>[54]|
|---|---|---|
|Basic Statistics|Basic Statistics|7<br>[27] [33] [38] [41] [50] [52] [66]<br>|
|Calmar|Calmar|1<br>[18]|
|Correlation|Autocorrelation Function<br>Correlation Ratio<br>Covariance<br>Feature Correlation<br>Mirror Column Associations<br>Mutual Information<br>Pairwise Association<br>i|4<br>[20] [26] [55] [69]<br>1<br>[38]<br>2<br>[16] [42]<br>7<br>[9] [10] [12] [35] [52] [62] [72]<br>1<br>[38]<br>1<br>[37]<br>1<br>[29]<br><br>|
||field correlation stability|1<br>[64]|
|Cumulative Distributions|Cumulative Distributions|1<br>[48]|
|Deep Structure Stability|Deep Structure Stability|1<br>[64]|
|Dimension Reduction Score|Dimension Reduction Score|2<br>[61] [62]|
|Discriminator|KNN<br>LSTM<br>Logistic Regression<br>Not Given<br>Random Forest|2<br>[62] [63]<br>3<br>[21] [52] [59]<br>1<br>[29]<br>1<br>[23]<br>1<br>[62]|
||SVM|1<br>[39]|
|DY Metric|DY Metric|1<br>[20]|
|EM Distance|EM Distance|5<br>[5] [20] [26] [35] [71]<br>|
|Feature Importance|Global Feature Importance<br>Local Feature Importance|1<br>[70]<br>1<br>[70]|
|FeatureInteraction|Global Feature Interaction|1<br>[70]<br>|
||Local Feature Interaction|1<br>[70]|
|Feature-based Distance|Feature-based Distance|1<br>[14]|
|Field Distribution Stability|Field Distribution Stability|1<br>[64]|
|Frechet Inception Distance|Frechet Inception Distance|1<br>[31]|
|Hurst Index|Hurst Index|1<br>[55]|
|Jenson-Shannon|Jenson-Shannon|3<br>[5] [26] [35]|
|Joint Quantile Exceedance|Joint Quantile Exceedance|1<br>[53]|
|Kendall|Kendall|1<br>[33]|
|KL|KL|3<br>[5] [26] [62]|
|Kolmogorov-Smirnov|Kolmogorov-Smirnov|7<br>[3] [5] [19] [24] [26] [56] [61]|
|Leverage Effect|Leverage Effect|2<br>[20] [67]|
|Local Sensitivity Analysis|Local Sensitivity Analysis|1<br>[70]|
|MDFA|MDFA|1<br>[69]|
|outlier filter|outlier filter|1<br>[64]|
|Overfitting Prevention<br>|Overfitting Prevention<br>|1<br>[64]<br>|
|PCA|PCA|1<br>[38]|
|P|P|5<br>1633373842|
|earson|earson|[] [] [] [] []<br>|
|Power Spectral Density<br>|Power Spectral Density<br>|1<br>[69]<br><br>|
|Probability Density Function|Probability Density Function|3<br>[2] [64] [69]|
|RFE<br>|RFE<br>|1<br>[8]<br>|
|Similarity Filter<br>|Similarity Filter<br>|1<br>[64]<br><br>|
|Single Value Relative Error|Single Value Relative Error|1<br>[8]|
|Spearman|Spearman|3<br>[16] [33] [42]|
|Stylized Facts|Stylized Facts|1<br>[67]|
|Uncertainty Coefficient|Uncertainty Coefficient|1<br>[38]|
|Variation Distance|Variation Distance|2<br>[73] [74]|
||Visual Inspection (Correlations)|6<br>[10] [25] [27] [29] [36] [38]|
|Visual Inspection|Visual Inspection (Distributions)<br>Visual Inspection (PCA)<br>Visual Inspection (Statistics)<br>Visual Inspection (Variance)<br>Visual Inspection (bitmap)<br>Visual Inspection (chi2)|18<br>[2] [6] [9] [10] [19] [26] [27] [29] [30] [31] [33] [38] [41] [50] [55] [56] [63] [69]<br>2<br>[24] [40]<br>1<br>[3]<br>1<br>[27]<br>1<br>[39]<br>1<br>[31]|
||VisualInspection(t-sne)|11<br>[0][1][21][22][23][40][58][59][63][64][68]|
||<br>Visual Inspection (time-series)|<br>13<br>[0] [10] [19] [24] [27] [33] [36] [39] [40] [52] [60] [62] [69]|



**Table 19** Methods and metrics for Statistical Similarity. 

this subsection, we review the metrics used to evaluate the machine learning efficacy of synthetic data generation techniques. 

The predominant approach is the Train–Synthetic–Test–Real (TSTR) protocol, in which a model is trained on synthetic data and evaluated on real data. Performance is typically compared against the same architecture trained on real data. Results may be reported either as the difference between the two test scores or as both scores side by side; these presentations convey the same information. Ideally, models trained on synthetic data perform **at least** as well as those trained on real data. Variation in TSTR assessments largely stems from the choice of comparison metrics. For classification tasks, _accuracy_ and _F1_ are the most common statistics, whereas _mean absolute error (MAE)_ is the standout metric for regression tasks. Several studies also report _precision_ and _recall_ , the components of F1 that capture, respectively, the quality and 

23 

|**Method**|**Variation**|**Number of Studies**|**Studies**|
|---|---|---|---|
|A*|A*|1|[1]|
|Accuracy|Accuracy|12|[3] [5] [11] [15] [16] [29] [32] [35] [36] [42] [71] [74]|
|Adjusted Rand Index|Adjusted Rand Index|1|[66]|
|AUC|AUC|4|[16] [22] [42] [56]|
|AugMAE|AugMAE|1|[1]|
|AUPRC|AUPRC|1|[17]|
|AUROC|AUROC|3|[17] [44] [46]|
|F1|F1|13|[1] [10] [16] [32] [35] [38] [42] [43] [45] [47] [48] [68] [74]|
|F2|F2|1|[65]|
|Investments|Average Return<br>Cumulative Returns<br>Sharpe Ratio<br>Sortino Ratio<br>Winning PCT|1<br>2<br>3<br>1<br>1|[13]<br>[51] [0]<br>[0] [18] [51]<br>[0]<br>[51]|
|Agreement Rate|Agreement Rate|1|[28]|
|Volatility Clustering|Volatility Clustering|1|[26]|
|MAE|MAE|14|[1] [13] [21] [23] [37] [40] [48] [52] [57] [58] [59] [60] [63] [68]|
|MAPE|MAPE|3|[13] [25] [60]|
|MSE|MSE|3|[57] [62] [72]|
|MSLE|MSLE|2|[40] [54]|
|Observation|Observation|1|[12]|
|Precision|Precision|4|[10] [11] [46] [65]|
|R2|R2|2|[55] [60]|
|Recall|Recall|4|[10] [11] [46] [65]|
|Replication Errors|Replication Errors|1|[72]|
|RMSE|RMSE|4|[13] [18] [25] [60]|
|RNSE|RNSE|1|[38]|
|ROC|ROC|2|[35] [56]|
|ROC Curve|ROC Curve|1|[29]|
|ROCAUC|ROCAUC|1|[47]|
|SMAPE|SMAPE|1|[60]|
|Visual Inspection|Visual Inspection (Classifications)<br>Visual Inspection (trading actions)|1<br>1|[30]<br>[0]|



**Table 20** Methods and metrics for Machine Learning Efficacy. 

quantity of positive predictions. For tasks such as fraud detection, recall is especially important because the aim is to identify as many fraudulent actors or transactions as possible; for credit risk assessment, precision is often preferred because the objective is to approve only loans that will be repaid. 

A subset of studies evaluates synthetic financial data by training trading models on generated data and measuring their investment performance. We observe a range of portfolio and risk-adjusted metrics. Liu et al. (2022) reports annual returns alongside the Sharpe and Sortino ratios to analyse performance; these statistics indicate how an equity investment performs relative to a risk-free benchmark. Similarly, J.L. Wu et al. (2023) uses cumulative return and the Sharpe ratio, as well as _winning percentage_ , defined as the fraction of trading pairs with positive returns. Average returns are also used as an efficacy metric in K. Zhang et al. (2019). 

#### **4.4.4 Privacy Preservation** 

Although privacy preservation has received relatively little attention in the literature we collected, a variety of techniques have still been applied to assess synthetic financial datasets (Table 21). Two studies, Park et al. (2018) and Duan et al. (2022), experiment with membership inference attacks to evaluate the privacy of their generative techniques. These attacks attempt to infer whether specific training data were used by testing input samples and observing whether the model makes high-confidence predictions. Duan et al. (2022) provide a detailed description of their procedure and report improved privacy when using higher values of differential privacy. Park et al. (2018), 

24 

|**Method**|**Variation**|**Count**|**Stu**|**dies**|
|---|---|---|---|---|
|Differential Privacy|Differential Privacy|1|[64]||
|Membership Attacks|Membership Attacks|2|[30]|[48]|
||Nearest Neighbour|5|[29]|[35] [38] [62] [73]|
|Nearest Neighbour|Distance and Standard Deviation|1|[25]||
||Nearest Neighbour Distance Ratio|1|[35]||



**Table 21** Methods and metrics for Privacy Preservation. 

in addition to using nearest neighbour evaluation methods, apply a similar approach and likewise find that higher differential privacy values reduce leakage. Both studies note that lower values can lead to data leakage, highlighting the importance of privacy testing in synthetic data evaluation and exposing a concerning gap in the literature where so few studies include privacy assessment in their experiments. 

The distance between synthetic and real samples is the most widely used method for assessing privacy in synthetic financial data. Five studies detect potential violations by identifying synthetic samples that lie within a small Euclidean distance of real data points. Zhao et al. (2021) also employ the Nearest Neighbour Distance Ratio (NNDR). For each synthetic sample, NNDR is calculated as the ratio between the smallest distance to a real sample and the next smallest distance. An NNDR close to 1 indicates the synthetic sample lies in a dense region of real samples, whereas a value close to 0 suggests it is very close to a single real sample and distant from others. 

Similarly, van Bree (2020) use the mean and standard deviation of distances between synthetic and real samples to assess how easily synthetic data could be reversetransformed to recover the original data. They report that a high mean and low standard deviation suggest synthetic samples are generally far from the original data. 

Finally, Juneja et al. (2023) also assess privacy preservation in their generated data, but the methods are not reported and therefore cannot contribute to a deeper understanding of evaluation techniques. 

## **5 Discussion** 

Our review collected 72 studies on the generation of synthetic financial datasets, which to our knowledge is the largest collection of its kind. From this body of work, several key research focuses emerge, alongside clear gaps requiring further study. Most notably, Generative Adversarial Networks (GANs) dominate the field, featuring in 53 of the studies, while other generative approaches appear in only one or two papers each. A similar concentration is seen in the financial applications of synthetic data generation: market data (stock, currency, and commodities), transaction data, and credit-related data (risk and fraud) are the primary areas of focus. By contrast, applications such as tax records, loans, and retail data receive little attention. Perhaps the most striking gap is the limited emphasis on privacy preservation. Only 12% of studies evaluated privacy, compared with 66% that assessed machine learning usability and 80% that examined statistical similarity. This is concerning, as privacy preservation is arguably the most critical feature for synthetic data in financial institutions. A likely explanation 

25 

is the absence of standardised evaluation criteria for synthetic data, particularly within financial applications. 

When placed in the context of other industries, such as healthcare (discussed in Section 1), our results are consistent. For example, Hernandez et al. (2022) also find that GANs dominate and that privacy is rarely evaluated. This cross-domain trend is notable, as both healthcare and finance involve highly sensitive data. For many use cases, privacy preservation should be the primary concern when generating synthetic data. While this does not invalidate the techniques used in the studies we reviewed, it suggests that industry practitioners must take responsibility for evaluating the privacy guarantees of their own implementations, and that decision-makers should prioritise privacy assessment more explicitly. 

Another notable finding is how the studies were sourced. Our database search identified just 20 relevant studies out of more than 3,000, while snowballing from these initial papers yielded an additional 52. This outcome reflects the gap between our search strategy and how financial applications of synthetic data are described in the literature. Like other systematic reviews of synthetic data generation Murtaza et al. (2023), we combined keywords related to synthetic data generation with financespecific terms. The generation-focused terms were broad, to capture variations in terminology, but the finance-specific terms, while not overly narrow, were required for a study to be included. What emerged from the snowball search is that many relevant studies did not explicitly describe finance as a research focus in their abstract, title, or keywords, but mentioned it only when introducing datasets used for experiments. This trend makes it difficult to systematically collect literature on synthetic financial data and highlights a limitation of relying heavily on industry-specific keywords in database searches. 

Another limitation of this study was the inability to compare the performance of models across different papers. Because the collected studies investigated a wide range of use cases and employed diverse evaluation methods, overall comparisons of generative models were not possible. To the best of our knowledge, this review provides the largest analysis and collection of research on the financial applications of synthetic data to date. As a systematic review dedicated to synthetic financial data generation, it is the first of its kind and makes a significant contribution to the literature. Opportunities for future research highlighted by our analysis include: 

- expanding research into generative techniques beyond GANs, including autoencoder-based generators, Generative Moment Matching Networks, and Conditional Euler Generators, 

- greater assessment of applications such as loan data, retail data, marketing data, and tax data, 

- the development of a standard evaluation framework for synthetic financial data, with particular emphasis on privacy preservation. 

Our focus was to build a clear understanding of how synthetic datasets can be used within the financial industry. As a result, other potential uses of generated data in finance, such as the Synthetic Minority Oversampling Technique (SMOTE) and time 

26 

series forecasting, were excluded from our inclusion criteria. The rapid pace of development in generative AI makes time series forecasting an especially promising area. For example, Padhi et al. (2021) investigated tabular time series generation, and more recently Nixtla released TimeGPT (Garza, Challu, & Mergenthaler-Canseco, 2023), a generative pre-trained transformer designed specifically for time series forecasting with a focus on financial applications. Although the released study has clear limitations, the technique itself shows strong potential. Another emerging privacy-preserving technology with applications to finance is homomorphic encryption, which allows datasets to remain encrypted while mathematical operations are performed, with the decrypted results reflecting those operations. 

## **6 Conclusion** 

This study has presented a comprehensive review of the current state of research into the financial applications of synthetic data generation. We critically analysed the focus of research across a range of applications, generative techniques, and evaluation methods. Our findings show that market data and credit data generation have received the most attention over the past five years, while other important use cases such as tax, marketing, and retail data remain comparatively underexplored, despite their sensitivity and relevance. 

Generative Adversarial Networks (GANs) dominate the field, with Conditional GANs, Vanilla GANs, and Wasserstein GANs featuring prominently, and TimeGANs widely used for market data generation. A key concern we identify is the lack of evaluation of privacy preservation within the existing literature. While attributes such as statistical similarity and machine learning usability are assessed in most studies, only a small number include methods for testing the privacy guarantees of synthetic data. We strongly encourage future research to address this gap and incorporate privacy assessment into experimental design. 

We also reflect on the methodological process of this systematic review, which highlights challenges in identifying relevant research given the way financial applications of synthetic data are often reported. Building on our work, future studies could expand into alternative generative approaches, explore additional financial use cases, or examine related privacy-preserving technologies such as homomorphic encryption. 

As the first systematic review dedicated to synthetic data generation for finance, this study fills a notable gap in the literature. It provides clear directions for future research and offers valuable insights for industry practitioners and decision-makers considering the adoption of synthetic data technologies. 

## **References** 

Abay, N.C., Zhou, Y., Kantarcioglu, M., Thuraisingham, B., Sweeney, L. (2019). Privacy preserving synthetic data release using deep learning. _Lecture notes in computer science (including subseries lecture notes in artificial intelligence and lecture notes in bioinformatics)_ (Vol. 11051 LNAI, pp. 510–526). Springer Verlag. 

27 

- Abufadda, M., & Mansour, K. (2021). A survey of synthetic data generation for machine learning. _2021 22nd international arab conference on information technology, acit 2021._ Institute of Electrical and Electronics Engineers Inc. 

- Ahmed, N., & Schmidt-Thieme, L. (2023). Sparse self-attention guided generative adversarial networks for time-series generation. _International Journal of Data Science and Analytics_ , , https://doi.org/10.1007/s41060-023-00416-6 

- Alaa, A., Chan, A.J., van der Schaar, M. (2021). Generative time-series modeling with fourier flows. _International conference on learning representations._ 

- Allouche, M., Girard, S., Gobet, E. (2022). _EV-GAN: Simulation of extreme events with ReLU neural networks_ (Vol. 23; Tech. Rep.). Retrieved from http://jmlr.org/papers/v23/21-0663.html. 

- Assefa, S.A., Dervovic, D., Mahfouz, M., Tillman, R.E., Reddy, P., Veloso, M. (2020). Generating synthetic data in finance: opportunities, challenges and pitfalls. _Proceedings of the first acm international conference on ai in finance_ (pp. 1–8). 

- Azamuke, D., Katarahweire, M., Bainomugisha, E. (2022, 6). Scenario-based Synthetic Dataset Generation for Mobile Money Transactions. _Acm international conference proceeding series_ (pp. 64–72). Association for Computing Machinery. 

- Boursin, N., Remlinger, C., Mikael, J. (2022). Deep generators on commodity markets application to deep hedging. _Risks_ , _11_ (1), 7, 

- Bouzarouata, S. (2023, 10). _Banking and finance report: Future-proof through continuous experimentation._ Retrieved from https://www.us.jll.com/en/trendsand-insights/research/banking-and-finance-outlook 

- Brenninkmeijer, B., & Amro, A. (2019). _On the Generation and Evaluation of Tabular Data using GANs_ (Tech. Rep.). Retrieved from https://www.researchgate.net/publication/344227988 

- Carvajal Patino, D., & Ramos Pollan, R. (2022, 12). Synthetic data generation with deep generative models to enhance predictive tasks in trading strategies. _Research in International Business and Finance_ , _62_ , , https://doi.org/10.1016/ j.ribaf.2022.101747 

- Coletta, A., Moulin, A., Vyetrenko, S., Balch, T. (2022, 11). Learning to simulate realistic limit order book markets from data as a World Agent. _Proceedings of the 3rd acm international conference on ai in finance, icaif 2022_ (pp. 428–436). Association for Computing Machinery, Inc. 

28 

- Coletta, A., Prata, M., Conti, M., Mercanti, E., Bartolini, N., Moulin, A., . . . Balch, T. (2021, 11). Towards Realistic Market Simulations: A Generative Adversarial Networks Approach. _Icaif 2021 - 2nd acm international conference on ai in finance._ Association for Computing Machinery, Inc. 

- Cramer, E., Gorjao, L.R., Mitsos, A., Schafer, B., Witthaut, D., Dahmen, M. (2022). Validation Methods for Energy Time Series Scenarios From Deep Generative Models. _IEEE Access_ , _10_ , 8194–8207, https://doi.org/10.1109/ACCESS.2022 .3141875 

- Da Silva, B., & Shi, S.S. (2019). Style transfer with time series: Generating synthetic financial data. _arXiv preprint arXiv:1906.03232_ , , 

- de Meer Pardo, F. (2019). Enriching financial datasets with generative adversarial networks. _MS thesis, Delft University of Technology, The Netherlands_ , , 

- Desai, A., Freeman, C., Wang, Z., Beaver, I. (2021). Timevae: A variational auto-encoder for multivariate time series generation. _arXiv preprint arXiv:2111.08095_ , , 

- Dogariu, M., Aztefan, L.D., Boteanu, B.A., Lamba, C., Kim, B., Ionescu, B. (2022, 11). Generation of Realistic Synthetic Financial Time-series. _ACM Transactions on Multimedia Computing, Communications and Applications_ , _18_ (4), , https:// doi.org/10.1145/3501305 

- Dogariu, M., S¸tefan, L.D., Boteanu, B.A., Lamba, C., Ionescu, B. (2021). Towards Realistic Financial Time Series Generation via Generative Adversarial Learning. _European signal processing conference_ (Vol. 2021-August, pp. 1341–1345). European Signal Processing Conference, EUSIPCO. 

- Duan, S., Liu, C., Han, P., Jin, X., Zhang, X., He, T., . . . Xiang, X. (2022, 1). HT-FedGAN: Federated Generative Model for Decentralized Tabular Data Synthesis. _Entropy_ , _25_ (1), , https://doi.org/10.3390/e25010088 

- Eckerli, F., & Osterrieder, J. (2021). Generative adversarial networks in finance: an overview. _arXiv preprint arXiv:2106.06364_ , , 

- Efimov, D., Xu, D., Kong, L., Nefedov, A., Anandakrishnan, A. (2020). Using generative adversarial networks to synthesize artificial financial datasets. _arXiv preprint arXiv:2002.02271_ , , 

29 

- El-Laham, Y., & Vyetrenko, S. (2022, 11). StyleTime: Style Transfer for Synthetic Time Series Generation. _Proceedings of the 3rd acm international conference on ai in finance, icaif 2022_ (pp. 489–496). Association for Computing Machinery, Inc. 

- Esteban, C., Hyland, S.L., R¨atsch, G. (2017). Real-valued (medical) time series generation with recurrent conditional gans. _arXiv preprint arXiv:1706.02633_ , , 

- Figueira, A., & Vaz, B. (2022, 8). _Survey on Synthetic Data Generation, Evaluation Methods and GANs_ (Vol. 10) (No. 15). MDPI. 

- Flaig, S., & Junike, G. (2022). Scenario generation for market risk models using generative neural networks. _Risks_ , _10_ (11), 199, 

- Fu, R., Chen, J., Zeng, S., Zhuang, Y., Sudjianto, A. (2019). _Time Series Simulation by Conditional Generative Adversarial Net_ (Tech. Rep.). Retrieved from www.macroadvisers.com. 

- Garza, A., Challu, C., Mergenthaler-Canseco, M. (2023). Timegpt-1. _arXiv preprint arXiv:2310.03589_ , , 

- Gatta, F., Giampaolo, F., Prezioso, E., Mei, G., Cuomo, S., Piccialli, F. (2022, 11). _Neural networks generative models for time series_ (Vol. 34) (No. 10). King Saud bin Abdulaziz University. 

- Ge, C., Mohapatra, S., He, X., Ilyas, I.F. (2020). Kamino: Constraint-aware differentially private data synthesis. _arXiv preprint arXiv:2012.15713_ , , 

- Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., . . . Bengio, Y. (2020). Generative adversarial networks. _Communications of the ACM_ , _63_ (11), 139–144, 

- Goos, G., Bertino, E., Gao, W., Steffen, B., Woeginger, G., Aachen, R., . . . Moti, Y. (2020). _Privacy-Preserving Anomaly Detection Using Synthetic Data_ (Tech. Rep.). Retrieved from http://www.springer.com/series/7409 

- Hayashi, K. (2022). _Fractional SDE-Net: Generation of Time Series Data with Longterm Memory_ (Tech. Rep.). Retrieved from https://github.com/xxx. 

30 

- Hernandez, M., Epelde, G., Alberdi, A., Cilla, R., Rankin, D. (2022, 7). _Synthetic data generation for tabular health records: A systematic review_ (Vol. 493). Elsevier B.V. 

- horacio (2019, 10). _The Critical Role of Artificial Intelligence in Payments Tech._ Retrieved from https://www.fintechnews.org/the-crirital-role-of-artificialinteliigence-in-payments-tech/ 

- James, S., Harbron, C., Branson, J., Sundler, M. (2021, 12). Synthetic data use: exploring use cases to optimise data utility. _Discover Artificial Intelligence_ , _1_ (1), , https://doi.org/10.1007/s44163-021-00016-y 

- Jeon, J., Kim, J., Song, H., Cho, S., Park, N. (2022). Gt-gan: General purpose time series synthesis with generative adversarial networks. _Advances in Neural Information Processing Systems_ , _35_ , 36999–37010, 

- Jordon, J., Szpruch, L., Houssiau, F., Bottarelli, M., Cherubin, G., Maple, C., . . . Weller, A. (2022). Synthetic data–what, why and how? _arXiv preprint arXiv:2205.03257_ , , 

- Jordon, J., Yoon, J., Van Der Schaar, M. (2018). Pate-gan: Generating synthetic data with differential privacy guarantees. _International conference on learning representations._ 

- Juneja, T., Bajaj, S.B., Sethi, N. (2023). Synthetic Time Series Data Generation Using Time GAN with Synthetic and Real-Time Data Analysis. _Lecture notes in electrical engineering_ (Vol. 1011 LNEE, pp. 657–667). Springer Science and Business Media Deutschland GmbH. 

- Karlsson, A. (2020). _Synthesis of Tabular Financial Data using Generative Adversarial Networks_ (Tech. Rep.). Retrieved from www.kth.se/sci 

- Kegel, L., Hahmann, M., Lehner, W. (2018, 7). Feature-based comparison and generation of time series. _Acm international conference proceeding series._ Association for Computing Machinery. 

- Kharkiv, S.K. (2023). _Editura Universitar˘a Danubius 2023_ . 

- Kim, J., Jeon, J., Lee, J., Hyeong, J., Park, N. (2021, 4). OCT-GAN: Neural ODEbased conditional tabular GANs. _The web conference 2021 - proceedings of the world wide web conference, www 2021_ (pp. 1506–1515). Association for Computing Machinery, Inc. 

- Kingma, D.P., & Welling, M. (2013). _Auto-encoding variational bayes._ Banff, Canada. 

31 

- Kondratyev, A., & Schwarz, C. (2020). _The Market Generator_ (Tech. Rep.). Retrieved from https://ssrn.com/abstract=3384948 

- Koshiyama, A., Firoozye, N., Treleaven, P. (2021). Generative adversarial networks for financial trading strategies fine-tuning and combination. _Quantitative Finance_ , _21_ (5), 797–813, 

- Kovalerchuk, B., Ahmad, M.A., Teredesai, A. (2021). Survey of explainable machine learning with visual and granular methods beyond quasi-explanations. _Interpretable artificial intelligence: A perspective of granular computing_ , 217–267, 

- Lee, J., Hyeong, J., Jeon, J., Park, N., Cho, J. (2021). Invertible tabular gans: Killing two birds with one stone for tabular data synthesis. _Advances in Neural Information Processing Systems_ , _34_ , 4263–4273, 

- Li, B., Luo, S., Qin, X., Pan, L. (2021, 10). Improving GAN with inverse cumulative distribution function for tabular data synthesis. _Neurocomputing_ , _456_ , 373–383, https://doi.org/10.1016/j.neucom.2021.05.098 

- Li, J., Liu, H., Yang, Z., Han, L. (2021). A Credit Risk Model with Small Sample Data Based on G-XGBoost. _Applied Artificial Intelligence_ , _35_ (15), 1550–1566, https://doi.org/10.1080/08839514.2021.1987707 

- Li, J., Wang, X., Lin, Y., Sinha, A., Wellman, M. (2020). Generating realistic stock market order streams. _Proceedings of the aaai conference on artificial intelligence_ (Vol. 34, pp. 727–734). 

- Liao, S., Ni, H., Szpruch, L., Wiese, M., Sabate-Vidales, M., Xiao, B. (2020). Conditional sig-wasserstein gans for time series generation. _arXiv preprint arXiv:2006.05421_ , , 

- Liu, C., Ventre, C., Polukarov, M. (2022, 11). Synthetic Data Augmentation for Deep Reinforcement Learning in Financial Trading. _Proceedings of the 3rd acm international conference on ai in finance, icaif 2022_ (pp. 343–351). Association for Computing Machinery, Inc. 

- Ljung, M. (2021). _Synthetic Data Generation for the Financial Industry Using Generative Adversarial Networks._ 

- Long, Y., Wang, B., Yang, Z., Kailkhura, B., Zhang, A., Gunter, C.A., Li, B. (2021). _G-PATE: Scalable Differentially Private Data Generator via Private Aggregation_ 

32 

_of Teacher Discriminators_ (Tech. Rep.). Retrieved from https://github.com/AIsecure/G-PATE. 

- Lu, Y., Shen, M., Wang, H., Wang, X., van Rechem, C., Fu, T., Wei, W. (2023). Machine learning for synthetic data generation: a review. _arXiv preprint arXiv:2302.04062_ , , 

- Martineau, K., & Feris, R. (2021). _What is synthetic data?_ https://research.ibm.com/ blog/what-is-synthetic-data. (Accessed: 2025-07-16) 

- Miok, K., Nguyen-Doan, D., Zaharie, D., Robnik-Sikonja,<sup>ˇ</sup> M. (2019). _Generating Data using Monte Carlo Dropout_ (Tech. Rep.). Retrieved from http://yann.lecun.com/exdb/mnist/ 

- Moher, D., Liberati, A., Tetzlaff, J., Altman, D.G., Altman, D., Antes, G., . . . Tugwell, P. (2009, 7). _Preferred reporting items for systematic reviews and meta-analyses: The PRISMA statement_ (Vol. 6) (No. 7). 

- Murtaza, H., Ahmed, M., Khan, N.F., Murtaza, G., Zafar, S., Bano, A. (2023, 5). _Synthetic data generation: State of the art in health care domain_ (Vol. 48). Elsevier Ireland Ltd. 

- Nickerson, K., Tricco, T., Kolokolova, A., Shoeleh, F., Robertson, C., Hawkin, J., Hu, T. (2022). _Banksformer: A Deep Generative Model for Synthetic Transaction Sequences_ (Tech. Rep.). Retrieved from https://data.world/lpetrocelli/czechfinancial-dataset-real-anonymized-transactions 

- Padhi, I., Schiff, Y., Melnyk, I., Rigotti, M., Mroueh, Y., Dognin, P., . . . Altman, E. (2021). Tabular transformers for modeling multivariate time series. _Icassp 20212021 ieee international conference on acoustics, speech and signal processing (icassp)_ (pp. 3565–3569). 

- Park, N., Gu, Y.H., Yoo, S.J. (2021, 2). Synthesizing individual consumers credit historical data using generative adversarial networks. _Applied Sciences (Switzerland)_ , _11_ (3), 1–15, https://doi.org/10.3390/app11031126 

- Park, N., Mohammadi, M., Gorde, K., Jajodia, S., Park, H., Kim, Y. (2018). Data synthesis based on generative adversarial networks. _Proceedings of the vldb endowment_ (Vol. 11, pp. 1071–1083). Association for Computing Machinery. 

- Pei, H., Yang, Y., Liu, C., Li, D. (2021). _Towards Generating Real-World Time Series Data_ (Tech. Rep.). Retrieved from https://seqml.github.io/rtsgan. 

- Platzer, M., & Reutterer, T. (2021, 6). Holdout-Based Empirical Assessment of MixedType Synthetic Data. _Frontiers in Big Data_ , _4_ , , https://doi.org/10.3389/ 

33 

fdata.2021.679939 

- Raimbault, J. (2019, 12). Second-order control of complex systems with correlated synthetic data. _Complex Adaptive Systems Modeling_ , _7_ (1), , https://doi.org/ 10.1186/s40294-019-0065-y 

- Reiter, J.P. (2023). Synthetic data: A look back and a look forward. _Trans. Data Priv._ , _16_ (1), 15–24, 

- Remlinger, C., Mikael, J., Elie, R. (2022). Conditional loss and deep euler scheme for time series generation. _Proceedings of the aaai conference on artificial intelligence_ (Vol. 36, pp. 8098–8105). 

- Rizzato, M., Morizet, N., Mar´echal, W., Geissler, C. (2022, 8). Stress testing electrical grids: Generative Adversarial Networks for load scenario generation. _Energy and AI_ , _9_ , , https://doi.org/10.1016/j.egyai.2022.100177 

- Rizzato, M., Wallart, J., Geissler, C., Morizet, N., Boumlaik, N. (2023). Generative adversarial networks applied to synthetic financial scenarios generation. _Physica A: Statistical Mechanics and its Applications_ , _623_ , 128899, 

- Simonetto, L. (2018). Generating spiking time series with generative adversarial networks: an application on banking transactions. _MS thesis-Univ. of Amsterdam_ , , 

- Singh, A., & Ogunfunmi, T. (2022, 1). _An Overview of Variational Autoencoders for Source Separation, Finance, and Bio-Signal Applications_ (Vol. 24) (No. 1). MDPI. 

- Soon, G. (2021, 10). _How data sharing drives industry-wide innovation in financial services._ Retrieved from https://www.frontier-enterprise.com/how-datasharing-drives-industry-wide-innovation-in-financial-services/ 

- Strelcenia, E., & Prakoonwit, S. (2023, March). Synthetic data generation in finance: requirements, challenges and applicability. _Ieee international conference on digital management, information science and technology._ Retrieved from http://www.icdmist.com/ 

- Takahashi, S., Chen, Y., Tanaka-Ishii, K. (2019, 8). Modeling Financial Time Series with Generative Adversarial Networks. _Physica A: Statistical Mechanics and its Applications_ , _527_ , , https://doi.org/10.1016/j.physa.2019.121261 

34 

- Tan, X., Zhang, Z., Zhao, X., Wang, S. (2022, 12). DeepPricing: pricing convertible bonds based on financial time-series generative adversarial networks. _Financial Innovation_ , _8_ (1), , https://doi.org/10.1186/s40854-022-00369-y 

- Tang, P., Zhang, Q., Zhang, X. (2023, 6). A Recurrent Neural Network based Generative Adversarial Network for Long Multivariate Time Series Forecasting. (pp. 181–189). Association for Computing Machinery (ACM). 

- van Bree, M. (2020). _Unlocking the potential of synthetic tabular data generation with variational autoencoders_ (Unpublished doctoral dissertation). Tilburg University Tilburg, The Netherlands. 

- Van Breugel, B., Kyono, T., Berrevoets, J., Van der Schaar, M. (2021). Decaf: Generating fair synthetic data using causally-aware generative networks. _Advances in Neural Information Processing Systems_ , _34_ , 22221–22233, 

- Vega-M´arquez, B., Rubio-Escudero, C., Nepomuceno-Chamorro, I. (2022). Generation of synthetic data with conditional generative adversarial networks. _Logic Journal of the IGPL_ , _30_ (2), 252–262, 

- Vega-M´arquez, B., Rubio-Escudero, C., Riquelme, J.C., Nepomuceno-Chamorro, I. (2020). Creation of Synthetic Data with Conditional Generative Adversarial Networks. _Advances in intelligent systems and computing_ (Vol. 950, pp. 231– 240). Springer Verlag. 

- Wiese, M., Knobloch, R., Korn, R., Kretschmer, P. (2020). Quant gans: deep generation of financial time series. _Quantitative Finance_ , _20_ (9), 1419–1440, 

- Wohlin, C. (2014). Guidelines for snowballing in systematic literature studies and a replication in software engineering. _Acm international conference proceeding series._ Association for Computing Machinery. 

- Wu, J., Plataniotis, K., Liu, L., Amjadian, E., Lawryshyn, Y. (2023, 2). Interpretation for Variational Autoencoder Used to Generate Financial Synthetic Tabular Data. _Algorithms_ , _16_ (2), , https://doi.org/10.3390/a16020121 

- Wu, J.L., Tang, X.R., Hsu, C.H. (2023, 6). A prediction model of stock market trading actions using generative adversarial network and piecewise linear representation approaches. _Soft Computing_ , _27_ (12), 8209–8222, https://doi.org/ 10.1007/s00500-022-07716-2 

35 

- Xiao, S., Xu, H., Yan, J., Farajtabar, M., Yang, X., Song, L., . . . Tong, S.J. (2018). _Learning Conditional Generative Models for Temporal Point Processes_ (Tech. Rep.). Retrieved from www.aaai.org 

- Xu, L., Skoularidou, M., Cuesta-Infante, A., Veeramachaneni, K. (2019). Modeling tabular data using conditional gan. _Advances in neural information processing systems_ , _32_ , , 

- Yadav, P., Gaur, M., Fatima, N., Sarwar, S. (2023, 4). Qualitative and Quantitative Evaluation of Multivariate Time-Series Synthetic Data Generated Using MTSTGAN: A Novel Approach. _Applied Sciences (Switzerland)_ , _13_ (7), , https:// doi.org/10.3390/app13074136 

- Yeo, W.J., Van Der Heever, W., Mao, R., Cambria, E., Satapathy, R., Mengaldo, G. (2025). A comprehensive review on financial explainable ai. _Artificial Intelligence Review_ , _58_ (6), 1–49, 

- Yin, X., Han, Y., Sun, H., Xu, Z., Yu, H., Duan, X. (2021). Multi-Attention Generative Adversarial Network for Multivariate Time Series Prediction. _IEEE Access_ , _9_ , 57351–57363, https://doi.org/10.1109/ACCESS.2021.3065969 

- Yoon, J., Jarrett, D., Van der Schaar, M. (2019). Time-series generative adversarial networks. _Advances in neural information processing systems_ , _32_ , , 

- Zhang, K., Zhong, G., Dong, J., Wang, S., Wang, Y. (2019). Stock Market Prediction Based on Generative Adversarial Network. _Procedia computer science_ (Vol. 147, pp. 400–406). Elsevier B.V. 

- Zhang, Y., Zaidi, N., Zhou, J., Li, G. (2023). Interpretable tabular data generation. _Knowledge and Information Systems_ , , https://doi.org/10.1007/ s10115-023-01834-5 

- Zhang, Z., Yang, L., Chen, L., Liu, Q., Meng, Y., Wang, P., Li, M. (2020, 2). A generative adversarial network based method for generating negative financial samples. _International Journal of Distributed Sensor Networks_ , _16_ (2), , https:// doi.org/10.1177/1550147720907053 

36 

- Zhao, Z., Kunar, A., Birke, R., Chen, L.Y. (2021). Ctab-gan: Effective table data synthesizing. _Asian conference on machine learning_ (pp. 97–112). 

37 

