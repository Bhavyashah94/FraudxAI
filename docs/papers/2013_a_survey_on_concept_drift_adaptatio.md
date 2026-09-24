---
title: "A Survey on Concept Drift Adaptation"
year: 2013
original_file: "a_survey_on_concept_drift_adaptatio.pdf"
pdf_path: "docs/papers\2013_a_survey_on_concept_drift_adaptatio.pdf"
---

# A Survey on Concept Drift Adaptation

**Year:** 2013  
**Local PDF:** [`2013_a_survey_on_concept_drift_adaptatio.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2013_a_survey_on_concept_drift_adaptatio.pdf)

---

**1** 

# **A Survey on Concept Drift Adaptation** 

JO AO GAMA<sup>˜</sup> , University of Porto, Portugal INDR E<sup>˙</sup> ZLIOBAIT<sup>ˇ</sup> E<sup>˙</sup> , Aalto University, Finland ALBERT BIFET, Yahoo! Research Barcelona, Spain MYKOLA PECHENIZKIY, Eindhoven University of Technology, the Netherlands ABDELHAMID BOUCHACHIA, Bournemouth University, UK 

Concept drift primarily refers to an online supervised learning scenario when the relation between the input data and the target variable changes over time. Assuming a general knowledge of supervised learning in this paper we characterize adaptive learning process, categorize existing strategies for handling concept drift, discuss the most representative, distinct and popular techniques and algorithms, discuss evaluation methodology of adaptive algorithms, and present a set of illustrative applications. This introduction to the concept drift adaptation presents the state of the art techniques and a collection of benchmarks for researchers, industry analysts and practitioners. The survey aims at covering the different facets of concept drift in an integrated way to reflect on the existing scattered state-of-the-art. 

Categories and Subject Descriptors: I.2.6 [ **Artificial Intelligence** ]: Learning 

General Terms: Design, Algorithms, Performance 

Additional Key Words and Phrases: concept drift, change detection, adaptive learning 

#### **ACM Reference Format:** 

Gama, J., Zliobait˙e, I., Bifet, A., Pechenizkiy, M., and Bouchachia, A. 2013. A Survey on Concept Drift Adap-<sup>ˇ</sup> tation. ACM Comput. Surv. 1, 1, Article 1 (January 2013), 35 pages. DOI = 10.1145/0000000.0000000 http://doi.acm.org/10.1145/0000000.0000000 

### **1. INTRODUCTION** 

Our digital universe is rapidly growing. The volume of data generated in 2012 has been estimated to surpass 2 _._ 8 zetabytes (2 _._ 8 trillion gigabytes) as reported in the IDC survey [Gantz and Reinsel 2012]. Efficient and effective tools and analysis methods for dealing with the ever-growing amount of data in different applications and fields are of paramount need. Very often data comes in the form of streams rendering its analysis and processing even more resource demanding. 

Traditionally in data mining data is first collected and then processed in an _offline_ mode. For instance, predictive models are trained using historical data given as a set of pairs (input, output). Models trained in such a way can be afterwards applied for predicting the output for new unseen input data. However, streaming data can not be processed similarly because data comes continuously over time and possibly is neverending. Accommodating such data in the machine’s main memory is impractical and often infeasible. Hence, only an _online_ processing is suitable. In this case, predictive models can be trained either incrementally by continuous update or by retraining using recent batches of data. 

In dynamically changing and non-stationary environments, the data distribution can change over time yielding the phenomenon of _concept drift_ [Schlimmer and Granger 1986; Widmer and Kubat 1996]. The _real_ concept drift<sup>1</sup> refers to changes in the conditional distribution of the output (i.e., _target variable_ ) given the input ( _input features_ ), while the distribution of the input may stay unchanged. A typical example of the real concept drift is a change in user’s interests when following an online news stream. Whilst the distribution of the incoming news documents often remains the same, the conditional distribution of the interesting (and thus not interesting) news 

> 1The term _real_ refers to one particular type of concept drift. It doesn’t mean that other types of drift are not concept drifts. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

### 1:2 

documents for that user changes. _Adaptive learning_ refers to updating predictive models online during their operation to react to concept drifts. 

Over the last decade research related to learning with concept drift has been increasingly growing and many drift-aware adaptive learning algorithms have been developed. In spite of the popularity of this research topic, no comprehensive survey on concept drift handling techniques is available to the community. One of the reasons for that is that the problem is of a wide scope and spans across different research fields. Moreover, terminology is not well established, thus similar adaptive learning strategies have been developed independently under different names in different contexts. 

Taking account of the current picture of research on concept drift, being very popular but also scattered among various communities, there is a strong need for a comprehensive summary of the research done so far to unify the concepts and terminology among the researchers and to survey the state-of-the-art methodologies and techniques investigated over the past. 

Several reviews related to drift-aware learning are available. However, they either do not focus exclusively on concept drift or relate to specific topics of adaptive learning. Thus these reviews are fragmented and/or are outdated. Currently the most cited survey on concept drift was published back in 2004 in [Tsymbal 2004]. The following overviews which are related to the topic of concept drift focused on ensemble techniques [Kuncheva 2004; 2008], inductive rule learning algorithms [Maloof 2010], or mainly on non-incremental learning techniques [Zliobaite 2009] that can use computational resources unrestrictedly, thus were limited in scope. Reviews on data streams [Gaber et al. 2005; Gama 2010; Bifet et al. 2011a] only partially deal with data drift. Data streams research covers adaptive learning only to some extent, while the main focus remains on making learning algorithms incremental and optimizing the balance of computational resources and the predictive accuracy. 

Several reviews are limited to specific application fields. A focused position paper [Grisogono 2006] presents a set of requirements for complex adaptive systems to be used for defence. A recent focused review [Kadlec et al. 2011] surveys adaptation mechanisms that have been used for soft sensors. Finally, a recent article [Moreno-Torres et al. 2012] focuses on describing various ways how data distribution can change over time and only briefly covers adaptation techniques from dataset shift community perspective, mostly leaving out works on concept drift. A recent review [Alberg et al. 2012] focuses on decision trees. 

The present contribution provides an integrated view on handling concept drift, by surveying adaptive learning methods, presenting evaluation methodologies and discussing illustrative applications. It focuses on online supervised learning when the relation between the input features and the target variable changes over time. 

The paper is organized as follows. In Section 2 we introduce the problem of concept drift, characterize adaptive learning algorithms and present motivating application examples. Section 3 presents a comprehensive taxonomy of methods for adaptive learning. Section 4 discusses the experimental settings and evaluation methodologies of adaptive learning algorithms. Section 5 concludes the survey. 

### **2. ADAPTIVE LEARNING ALGORITHMS** 

Learning algorithms often need to operate in dynamic environments, which is changing unexpectedly. One desirable property of these algorithms is their ability of incorporating new data. If the data generating process is not strictly stationary (as applies to most of the real world applications), the underlying concept, which we are predicting (for example, interests of a user reading news), may be changing over time. The ability to adapt to such _concept drift_ can be seen as a natural extension for the incremental learning systems [Giraud-Carrier 2000] that learn predictive models example by 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:3 

example. _Adaptive learning algorithms_ can be seen as advanced incremental learning algorithms that are able to adapt to evolution of the data generating process over time. This section introduces concept drift and characterizes adaptive learning. 

### **2.1. Setting and definitions** 

In machine learning the supervised learning problem is formally defined as follows. We aim to predict a target variable _y ∈ℜ_<sup>1</sup> in regression tasks (or _y_ categorical in classification tasks) given a set of input features _X ∈ℜ_<sup>_p_</sup> . An _example_ is one pair of ( _X, y_ ). For instance, _X_ is a set of sensor readings of a chemical process at 2 p.m. on the 2<sup>_nd_</sup> of January and _y_ = “ _good_<sup>_′′_</sup> is the true quality of the produced product at that time. In the _training examples_ , that are used for model building, both _X_ and _y_ are known. In the new examples, on which the predictive model is applied, _X_ is known, but _y_ is not known at the time of prediction. 

According to the Bayesian Decision Theory [Duda et al. 2001], a classification can be described by the prior probabilities of the classes _p_ ( _y_ ) and the class conditional probability density functions _p_ ( _X|y_ ) for all classes _y_ = 1 _, . . . , c_ , where _c_ is the number of classes. The classification decision is made according to the posterior probabilities of the classes, which for class _y_ can be represented as 



where _p_ ( _X_ ) =<sup>�</sup><sup>_c_</sup> _y_ =1<sup>_p_(</sup><sup>_y_)</sup><sup>_p_(</sup><sup>_X|y_). Here equal costs of misclassification are assumed.</sup> The type of the target variable space depends on the task. In classification the target variable takes categorical values (class labels), while in regression the target variable takes continuous values. 

We can distinguish two learning modes: _offline_ learning and _online_ learning. In offline learning the whole training data must be available at the time of model training. Only when training is completed the model can be used for predicting. In contrast, online algorithms process data sequentially. They produce a model and put it in operation without having the complete training data set available at the beginning. The model is continuously updated during operation as more training data arrives. 

Less restrictive than online algorithms are _incremental_ algorithms that process input examples one-by-one (or batch-by-batch) and update the decision model after receiving each example. Incremental algorithms may have random access to previous examples or representative/selected examples. In such a case these algorithms are called _incremental algorithms with partial memory_ [Maloof and Michalski 2004]. Typically, in incremental algorithms, for any new presentation of data, the update operation of the model is based on the previous one. _Streaming_ algorithms are online algorithms for processing high-speed continuous flows of data. In streaming, examples are processed sequentially as well and can be examined in only a few passes (typically just one). These algorithms use limited memory and limited processing time per item. 

In the setting that we are considering data arrives _online_ , often in real time, forming a stream which is potentially infinite. The machinery is given input data that has just arrived to predict its target variable(s). That is, a prediction machinery is defined as a mapping function between the input (feature) space and its corresponding output (target) space. For instance, given sensor readings in a chemical production process the task is to predict the quality of the product (output). 

Because data is expected _to evolve over time_ - especially in dynamically changing environments, where non-stationarity is typical, its underlying distribution can change dynamically over time. The general assumption in the concept drift setting is that the change happens unexpectedly and is unpredictable, although in some particular 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

### 1:4 

real-world situations the change can be known ahead of time in correlation with the occurrence of particular environmental events. But solutions for the general case of drift entail the solutions for the particular cases. Moreover the change may take different forms, i.e. the input data characteristics or the relation between the input data and the target variable may change. 

Formally _concept drift_ between time point _t_ 0 and time point _t_ 1 can be defined as 



where _pt_ 0 denotes the joint distribution at time _t_ 0 between the set of input variables _X_ and the target variable _y_ . Changes in data can be characterized as changes in the components of this relation [Kelly et al. 1999; Gao et al. 2007]. In other terms, 

- the prior probabilities of classes _p_ ( _y_ ) may change, 

- the class conditional probabilities _p_ ( _X|y_ ) may change, and 

- as a result, the posterior probabilities of classes _p_ ( _y|X_ ) _may_ change affecting the prediction. 

We are interested to know two implications of these changes: First, we are interested to know (i) whether the data distribution _p_ ( _y|X_ ) changes and affects the predictive decision and (ii) whether the changes are visible from the data distribution without knowing the true labels, i.e. _p_ ( _X_ ) changes. From a predictive perspective only the changes that affect the prediction decision require adaptation. 

We can distinguish the following types of drifts: 

- (1) _Real concept drift_ refers to changes in _p_ ( _y|X_ ). Such changes can happen either with or without change in _p_ ( _X_ ). Real concept drift has been referred to as _concept shift_ in [Salganicoff 1997] and _conditional change_ in [Gao et al. 2007]. 

- (2) _Population drift_ refers to changes in the population from which future samples will be drawn compared the design/training sample was drawn[Kelly et al. 1999]. 

- (3) _Virtual drift_ happens if the distribution of the incoming data changes (i.e., _p_ ( _X_ ) changes) without affecting _p_ ( _y|X_ )[Delany et al. 2005; Tsymbal 2004; Widmer and Kubat 1993]. However virtual drift has had different interpretations in the literature: 

   - Originally a virtual drift has been defined [Widmer and Kubat 1993] to occur due to incomplete data representation rather than change in concepts in reality, 

   - Virtual drift corresponds to change in data distribution that leads to changes in the decision boundary[Tsymbal 2004], 

   - Virtual drift is a drift that does _not_ affect the target concept [Delany et al. 2005], 

   - Virtual drift has been also referred to as _temporary drift_ [Lazarescu et al. 2004], _sampling shift_ [Salganicoff 1997] and _feature change_ [Gao et al. 2007], 

   - In this paper _virtual_ drift refers to change in the data distribution _p_ ( _X_ ). 

**Example:** Consider an online news stream of articles on real estate. The task for a given user is to classify the incoming news into _relevant_ and _not relevant_ . Suppose that the user is searching for a new apartment, then news on dwelling houses are _relevant_ whereas holiday homes are _not relevant_ . If the editor of the news portal changes, the writing style changes as well, but the dwelling houses remain _relevant_ for the user. This scenario corresponds to population drift. If due to a crisis more articles on dwelling houses come out and less articles on holiday homes do, but the editor, the writing style, and the interests of the user remain the same, this situation corresponds to drift in prior probabilities of the classes. If on the other hand the user has bought a house and starts looking for a holiday destination, dwelling houses become _not relevant_ and holiday homes become _relevant_ . This scenario corresponds to the real concept 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:5 

drift. In this case that the writing style and the priors remain the same. It may happen that all types of drifts takes place at the same time. 

Figure 1 illustrates these concepts. We see that only the real concept drift changes the decision boundary and the previous decision model becomes obsolete. In reality the virtual drift, changing priors or novelties may appear in combination with the real drift, in those cases the decision boundary is also affected. 



<!-- Start of picture text -->
Original data Real concept drift Virtual drift<br>p(y|X) changes  p(X) changes, but not p(y|X)<br><!-- End of picture text -->

Fig. 1. Types of drifts: circles represent instances, different colors represent different classes. 

This survey primarily focuses on handling the real concept drift which is not visible from the input data distribution. In many cases the techniques that handle the real concept drift can also handle drifts that manifest in the input data distributions, but not vice versa. The techniques that handle real concept drift typically rely on the feedback about the predictive performance. In this present paper, drift that can be detected from the incoming data distribution is not covered. This corresponds to tracking drifting priors (an interested reader is referred to [Zhang and Zhou 2010]), and novelty detection (an interested reader is referred to [Markou and Singh 2003; Masud et al. 2011]). Furthermore, semi-supervised drift handling techniques based on clustering (an interested reader is referred to [Aggarwal 2005; Bouchachia et al. 2010]) are not discussed in this paper. 

### **2.2. Changes in data over time** 

Changes in data distribution over time may manifest in different forms, as illustrated in Figure 2 on a one-dimensional data. There changes happen in the data mean. Drift 



<!-- Start of picture text -->
time sudden/abrupt incremental gradual reoccuring concepts outlier (not concept drift)<br>data mean<br><!-- End of picture text -->

Fig. 2. Patterns of changes over time (outlier is not concept drift). 

may happen _suddenly/abruptly_ by switching from one concept to another (e.g. replacing a sensor in a chemical plant that has a different calibration), or _incrementally_ consisting on many intermediate concepts in between (e.g. a sensor slowly wears off and becomes less accurate). Drift may happen suddenly (e.g. the topics of interest that one is surveying as a credit analyst may suddenly switch from, for instance, meat prices to public transportation) or _gradually_ (e.g. relevant news topics change from dwelling to holiday homes, while the user does not switch abruptly, but rather keeps going back to the previous interest for some time). One of the challenges for concept drift handling algorithms is not to mix the true drift with an _outlier_ or noise which refers to a once-off random deviation or anomaly (see [Chandola et al. 2009] for outlier detection). No adaptivity is needed in the latter case. Finally, drifts may introduce new concepts that were not seen before, or previously seen concepts may _reoccur_ after some time 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

### 1:6 

J. Gama et al. 

(e.g. in fashion). Changes can be further characterized by severity, predictability and frequency [Minku et al. 2010; Kosina et al. 2010]. 

Most of adaptive learning techniques implicitly or explicitly assume and specialize in some subset of concept drifts. Many of them assume sudden non-reoccurring drifts. But in reality often mixtures of many types can be observed. 

### **2.3. Requirements for predictive models in changing environments** 

Predictive models that operate in these settings need to have mechanisms to detect and adapt to evolving data over time, otherwise their accuracy will degrade. As time passes, the decision model may need update taking into account the new data or gets completely replaced to meet the changed situation. Predictive models are required to: 

- (1) detect to concept drift (and adapt if needed) as soon as possible; 

- (2) distinguish drifts from noise and be adaptive to changes, but robust to noise; 

- (3) operate in less than example arrival time and use not more than a fixed amount of memory for any storage. 

### **2.4. Online adaptive learning procedure** 

The online adaptive learning is formally defined as follows. A _decision model_ is a function _L_ that maps the input variables to the target: _y_ = _L_ ( _X_ ). A _learning algorithm_ specifies how to build a model from a set of data instances. 

Online adaptive learning procedure is the following. 

- (1) _Predict._ When new example _Xt_ arrives, a prediction _y_ ˆ _t_ is made using the current model _Lt_ . 

- (2) _Diagnose._ After some time we receive the true label _yt_ and can estimate the _loss_ as _f_ (ˆ _yt, yt_ ), and 

- (3) _Update._ we can use the example ( _Xt, yt_ ) for model update to obtain _Lt_ +1. 

Depending on the computational resources, the data may need to be discarded once processed using the latest version of the model _Lt_ +1 = `train` (( _Xt, yt_ ) _, Lt_ ). Alternatively, some of the past data may remain accessible _Lt_ +1 = `train` (( _Xi, yi_ ) _, . . . ,_ ( _Xt, yt_ ) _, Lt_ ). There are different ways of handling data online (e.g., partial memory: some of the examples are stored and used regularly in the training, window-based: data is presented as chunks, instance-based: an example is processed upon its arrival). More details on various schemes related to data presentation will follow in Section 3. 

After updating the model new example _Xt_ +1 arrives and the loop of receivingpredicting-feedback-model update continues infinitely. At some time steps one may choose to preserve the current model _Lt_ +1 = _Lt_ . 

Figure 3 depicts a generic schema for an online adaptive learning algorithm. In a nutshell, the memory module defines how and which data is presented to the learning algorithm (learning module). The loss estimation module tracks the performance of the learning algorithm and sends information to the control module to update the model if necessary. Section 3 will discuss the four modules of the system (Data Management, Learning, Change Detection, Loss Estimation) in detail. 

This setting has variations where, for instance, the true values for the target variable (feedback) come with a delay or are not available at all. Moreover, new examples for prediction may arrive before we get feedback for the data that has already been processed. In such a case model update would be delayed, but the principles of operation remain the same. Finally, in some settings we may need to process examples in batches rather than one-by-one. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:7 



<!-- Start of picture text -->
input system output<br>data 1Memory Learning 1 prediction<br>3 prediction<br>part<br>feedback 2 2 3 3 diagnostic<br>(delay) part<br>Loss  Change alarm<br>estimation 2 Detection 2<br>1 predict<br>mandatory<br>2 diagnose<br>optional<br>3 update<br><!-- End of picture text -->

Fig. 3. A generic schema for an online adaptive learning algorithm. 

### **2.5. Illustrative applications** 

The problem of concept drift has been recognized and addressed in multiple domains and application areas, including medicine [Kukar 2003; Tsymbal et al. 2006], industry [Pechenizkiy et al. 2009], education [Castillo et al. 2003], and business [Klinkenberg 2003]. Applications requiring adaptation can be grouped into four categories: 

- _Monitoring and control._ includes detection of anomalous behavior and adversary activities on the web, computer networks, telecommunications, financial transactions and other application areas where an abnormal behavior needs to be signaled, and it is often formulated as a detection task. 

- _Management and strategic planning._ includes predictive analytics tasks, such as evaluation of creditworthiness, demand prediction, food sales, bus travel time prediction, crime prediction by region. 

- _Personal assistance and information._ includes recommender systems, categorization and organization of textual information, customer profiling for marketing, personal mail categorization and spam filtering. 

- _Ubiquitous environment applications._ includes a wide spectrum of moving and stationary systems, which interact with changing environments, for instance moving robots, mobile vehicles, smart household appliances. 

Next we discuss motivating application cases within each category to illustrate the demand of adaptive learning systems that can handle concept drift. 

_2.5.1. Monitoring and Control._ In monitoring and control applications data is often presented in a form of time series. Two most typical learning tasks are time-series forecasting (regression task) or anomaly detection (classification task). 

Online mass flow prediction in an industrial boiler [Pechenizkiy et al. 2009] is an example application in the monitoring and control category. Mass flow prediction would help to improve operation and control of the boiler. In steady operation, combustion is affected by the disturbances in the feed rate of the fuel and by the incomplete mixing of the fuel in the bed. Knowing the mass flow is important for boiler control. The system takes fuel that is continuously mixed inside and transferred from a container to the boiler. Scaling sensors located under the container provide streaming data. The task is to predict (estimate) the mass flow in real time. 

Concept drift happens due to the following reasons. Fuel feeding is a manual and non standardized process, which is not necessarily smooth and can have short interruptions. Each operator can have different habits. The process characteristics may depend on the type and the quality of fuel used. The main focus for an adaptive learning algorithm is to handle two types of changes: an abrupt change to feeding and slower 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

### 1:8 

but still abrupt switch to burning. One challenge for learning is that the feedback (the ground truth of mass flow) is not available at all, it can only be approximately estimated by retrospectively inspecting the historical data. An additional challenge is to deal with specific one-sided outliers that can be easily mistaken for changes. 

Traditional approaches (such as ADWIN) for explicit change detection based on the monitoring of the raw sensor signal or streaming error of the regressors give reasonable results. They can be improved by considering the peculiarities of the application. 

_2.5.2. Management and strategic planning._ The Smart Grid (SG) is an electric system that uses two-way digital information, cyber-secure communication technologies, and computational intelligence in an integrated fashion across heterogeneous and distributed electricity generation, transmission, distribution and consumption to achieve energy efficiency. A key and novel characteristic of SG’s is the intelligent layer that analyzes the data produced by smart meters allowing companies to develop powerful new capabilities in terms of grid management, planning and customer services for energy efficiency. The advent of SG’s has changed the way energy is produced, priced and billed. The key aspect of SG’s is distributed energy production, namely renewable energies. The penetration of renewable energies (solar, wind, etc.) is increasing fast and power forecasting becomes an important factor in defining the operation planning policies to be adopted by a Transmission System Operator. 

When observing the literature in wind power prediction [Monteiro et al. 2009], one realizes that most proposals are based on an off-line training mode, building a static model that is then used to produce predictions. This option rely in assumptions of stationarity of the wind electric power model, which must be strongly questioned [Bremnes 2004; Bessa et al. 2009]. Using real data from three distinct wind parks, [Bessa et al. 2009] presents the merits of on-line training against off-line training of neural networks. The authors point out the evolving nature of data and the presence of concept drift in wind pattern behavior. 

_2.5.3. Personal assistance and information._ Text classification has been a popular topic in machine learning for decades. However, interesting applications related to the problem of concept drift appeared relatively recently. Examples of text stream applications include e-mail classification [Carmona-Cejudo et al. 2010], e-mail spam detection [Lindstrom et al. 2010] and sentiment classification [Bifet and Frank 2010]. Sentiment classification is a popular task in social media monitoring, customer feedback analysis and other applications. 

The main source of concept drift in e-mail classification and spam filtering are due to changing e-mail content and presentation (virtual drift), as well as adaptive behaviour of spammers trying to overcome spam filters (may be virtual or real). Besides, users may change their attitude towards particular categories of e-mails starting or stopping to consider them spam (real drift). In sentiment classification the vocabulary used to express positive and negative sentiments may change over time. Since the collection of documents is not static (virtual drift, novelties), the feature space representing the current collection is dynamic that may require specific updates of the models. 

Various adaptive learning strategies have been used in this domain, including individual methods like case-based reasoning, and ensembles, either evolving or with an explicit detection of changes by means of change detectors (Section 3.2). 

Availability of feedback is a serious challenge in personal assistance and information. The dilemma is that if feedback is easily available, that implies no need for automated predictions. In e-mail classification we can hope that from time to time we will receive feedback from the user in case of misclassifications or can design an active learning system (e.g. [Zliobaite et al. 2013]), which from time to time asks the user to 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:9 

provide labels on demand. However, when possible we need to aim at automatic ways for obtaining the true labels. 

Suppose for monitoring the attitude of people towards a political party we want to classify the polarity or sentiment of tweets from Twitter. Labelling tweets manually as positive or negative is a laborious and expensive task. However, tweets may have author-provided sentiment indicators: changing sentiment is implicit in the use of various types of emoticons. Hence we may use these to label the training data. Smileys or emoticons are visual cues that are associated with emotional states. They are constructed using the characters available on a standard keyboard, representing a facial expression of emotion. By using emoticons, authors of tweets annotate their own text with an emotional state. Annotated tweets can be used to train a sentiment classifier. 

Building a content-based filter for adaptive news access present rather different perspective on text classification in streaming settings. The goal is to learn incrementally and keep up to date a user model for news story classification. A simple yet effective approach has been proposed in [Billsus and Pazzani 2000]. For each user an adaptive learning system is built consisting of a simple ensemble with separate models for short-term and long-term interests of users. A stable Naive Bayes classifier is used for modelling the long term interests of a user and the Nearest Neighbour classifier captures the short term interests of the user. For the short-term interests model a fixed size window over the liked news stories is maintained and/or instances are weighed with respect to their age. No explicit change detection is used for monitoring either of the short-term or long-term interests. The true labels of some of the instances come naturally due to a positive relevance feedback, i.e. a user accessing a particular news item provides the signal that the item is relevant to his or her interests. 

On the other hand, recommender systems is a broad application in the personal assistance and information category [Bobadilla et al. 2013; Adomavicius and Tuzhilin 2005]. Interests of the data mining community in recommender systems domain have been boosted by the NetFlix competition<sup>2</sup> . One of the lessons learnt by the winning teams was that taking temporal dynamics into account substantially contributes towards building accurate models. Modelling user interests and handling concept drift were the other interesting aspects. In collaborative filtering, modelling of user interests relies primarily on the availability of other ratings already provide by the users. In a realistic application case, the data is highly imbalanced. Some movies are very popular, while most of the movies are not; some users rate many movies, but many other rate only a few. The rating matrix is high-dimensional and extremely sparse containing only about 1% of non-zero elements. Such properties make the application of most supervised learning techniques inapplicable and motivate the development of advanced collaborative filtering approaches. The sources and the nature of change can be diverse. Both items and users are changing over time. The item-side effects include first of all changing product perception and popularity. Popularity of some movies is expected to follow seasonal patterns. The user-side effects include changing tastes and preferences of users, some of which may be short-term or contextual and therefore likely reoccurring (mood, activity, company), changing perception of rating scale, possible change of rater within household and alike problems. The winning team developed an ensemble approach including multiple models for handling these various kinds of changes. As suggested in [Koren 2010] popular windowing and instance weighing approaches for handling concept drift are not the best choice for each kind of changing behaviour, simply because in collaborative filtering e.g. the relations between ratings is of the main importance for predictive modelling. 

> 2 `www.netflixprize.com` 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:10 

_2.5.4. Ubiquitous environment applications._ Autonomous vehicle control is an application case in the ubiquitous environment category. DARPA Grand Challenge was a prize competition open for teams developing fully autonomous driverless vehicles. Stanley, the car of the winning team of the second long distance competition<sup>3</sup> organized in 2005, had a highly reliable system on board that allowed the car to drive through different off-road environments at relatively high speeds. Among other intelligent components of the systems, Stanley had to perform identification and avoidance of obstacles and road finding [Thrun et al. 2006]. 

The Stanley team combined several ideas for automated terrain labelling using streaming laser sensor data for short and medium range obstacle avoidance and streaming data from the colour camera to learn the concept of the drivable surface and use it for velocity control (if the surface further ahead in non-drivable the car should slow down). That is the vision module had to maintain an accurate classifier for identifying drivable and non-drivable regions in the image stream. An adaptive learning approach was necessary for performing this task reliably because of many changing and not easily measurable factors such as surface material, lighting conditions or dust or dirt on the camera itself that effect the target concept. 

The classification task was to model the colour of the drivable terrain. The Stanley team used an adaptive Mixture of Gaussians. The model had to adapt to slowly changing lighting conditions and to abruptly changing surface colours, e.g., moving from a paved to an unpaved road. For gradual adaptation the internal Gaussian was adjusted, for the rapid adaptation the Gaussians were replaced with new ones. The required speed of adaptation depended on the road conditions. 

These real-world application cases present evidence that adaptive learning makes it possible to address complex learning problems which would not be feasible to tackle in the stationary settings. These examples also illustrate that it is important first to understand the nature and source of drift and only then engineer an effective adaptive learning strategy. 

### **3. TAXONOMY OF METHODS FOR CONCEPT DRIFT ADAPTATION** 

In this section we propose a new taxonomy for adaptive algorithms that learn a predictive model from evolving data with unknown dynamics. The two main abstract concepts are _memory_ and _forgetting_ data and/or models. We discuss a set of representative and popular algorithms that implement adaptation strategies. The discussion is organized around the four modules of adaptive learning algorithms that were identified in Figure 3: _memory_ , _change detection_ , _learning_ , and _loss estimation_ . The main idea behind presenting the taxonomy in four separate modules rather than a tree of methods is to see adaptive learning systems as consisting of modular components. An overview of the taxonomy is presented in Figure 4, and the methods within each module are further detailed in Figures 5, 6, 7 and 8. 

### **3.1. Memory** 

Learning under concept drift requires not only to update the predictive model with new information, but also forget the old information. We consider two types of memory: short term memory represented as data and long term memory represented as generalization of data – models. In this subsection, we analyze the short term memory under two dimensions as illustrated in Figure 5: _i) Data management_ specifies which data is used for learning; and _ii) Forgetting mechanism_ specifies how old data is discarded. The issues of long term memory will be discussed in Section 3.3. 

> 3 `http://archive.darpa.mil/grandchallenge05/` 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:11 



<!-- Start of picture text -->
Data<br>Management<br>Memory<br>Forgetting<br>Mechanism<br>Change Detection Detection Models<br>Learning Mode<br>Learning Adaption Methods<br>Model Management<br>Model dependent<br>Loss Estimation<br>Model independent<br><!-- End of picture text -->



<!-- Start of picture text -->
Fig. 4. Four modules of adaptive learning systems with a taxonomy of methods.<br><!-- End of picture text -->



<!-- Start of picture text -->
Single Example<br>Data<br>Management Multiple Examples Fixed Size<br>(windows)<br>Variable Size<br>Fixed Size<br>Temporal Sequence<br>Abrupt forgetting<br>Forgetting (window) Variable Size<br>Mechanism<br>Sampling<br>Gradual forgetting<br>(Selection)<br>MEMORY<br><!-- End of picture text -->

Fig. 5. Taxonomy of memory properties of methods. 

_3.1.1. Data Management._ The assumption behind most of the adaptive learning algorithms is that the most recent data is the most informative for the current prediction. Hence, data management typically aims at learning from the most recent data: either a single example or multiple examples. 

**Single Example** _._ Storing only a single example in memory has roots in online learning algorithms that learn from one example at a time. An online algorithm can process its input example by example in the order of arrival without keeping the entire training dataset in memory. Most online learners maintain a single hypothesis (which can originate from a complex predictive model) and model updates are error-driven. When a new example _Xt_ is available, the current hypothesis makes a prediction _y_ ˆ _t_ . When the true target value _yt_ is received, loss is computed and the current hypothesis is updated if necessary. An example of such algorithms is `Winnow` [Littlestone 1987], which is a linear classifier system that uses a multiplicative weight-update scheme. The key characteristic of `Winnow` is its robustness to irrelevant features. 

Online learning algorithms can be seen as naturally adaptive to evolving distributions, mainly due to the update mechanism that continuously updates the model with the most recent examples. However, online learning systems do not have explicit forgetting mechanisms. Adaptation happens only as the old concepts are diluted due to the new incoming data. Systems like `WINNOW` [Littlestone 1987], and `VFDT` [Domingos and Hulten 2000] can adapt to slow changes over time. The main limitation is their slow adaptation to abrupt changes, which depends on how sensible the model update with a new example is set to be. Setting these parameters requires a tradeoff between stability and sensitivity [Carpenter et al. 1991b]. Representative _single instance memory_ systems explicitly dealing with concept drift include `STAGGER` [Schlim- 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:12 

mer and Granger 1986], `DWM` [Kolter and Maloof 2003; 2007], `SVM` [Syed et al. 1999], `IFCS` [Bouchachia 2011a]. 

**Multiple Examples** _._ Another approach to data management is to maintain a predictive model consistent with a set of recent examples. The algorithm family `FLORA` [Widmer and Kubat 1996] is one of the first supervised incremental learning systems for evolving data. The original `FLORA` algorithm uses a sliding window of a fixed length, which stores the most recent examples in the _first-in-first-out (FIFO)_ data structure. At each time step, the learning algorithm builds a new model using the examples from the training window. The model is updated following two processes: a learning process (update the model based on the new data) and a forgetting process (discard data that is moving out of the window). The key challenge is to select an appropriate window size. A short window reflects the current distribution more accurately, thus it can assure fast adaptation in periods with concept changes, but in stable periods too short window worsens the performance of the system. A large window gives a better performance in stable periods, but it reacts to concept changes slower. In general the training window size can be _fixed_ or _variable_ over time. 

- _Sliding windows of a fixed size._ These methods store in memory a fixed number of the most recent examples. Whenever a new example arrives, it is saved to memory and the oldest one is discarded. This simple adaptive learning method is often used as a baseline in evaluation of algorithms. 

- _Sliding windows of variable size._ Here the number of examples in a window varies over time, typically depending on the indications of a change detector. A straightforward approach is to shrink the window whenever a change is singled such that the training data reflects the most recent concept, and grow the window otherwise. 

One of the first algorithms using an adaptive window size is the `FLORA2` [Widmer and Kubat 1996]. Incoming examples are added to the window and the oldest ones are deleted. Addition and deletion keeps the window (and the predictive model) consistent with the current concept. Further versions of the algorithm deal with recurring concepts ( `FLORA3` ) and noisy data ( `FLORA4` ). A later study [Klinkenberg and Joachims 2000] presents a theoretically supported method to recognize and handle concept changes with Support Vector Machines. This method maintains a window over the training examples with an appropriate size. The key idea is to adjust the window-size based on the estimate of the generalization error. At each time step the algorithm builds a number of SVM models using various window sizes and selects the the window size that minimizes the leave-one-out error estimate as the training window. 

Learning windows of variable length appear in [Maloof and Michalski 1995; Klinkenberg 2004; Gama et al. 2004; Kuncheva and Zliobaite 2009]. The assumption behind relying on windowing is that the recency of the data is associated with relevance and importance. Unfortunately, this assumption may not be true in every circumstance. For instance, when the data is noisy or concepts reoccur, recency of data does not mean relevance. Moreover, if slow change lasts longer than the window size, windowing may fail as well. 

_3.1.2. Forgetting Mechanism._ The choice of a forgetting mechanism depends on the expectations that we have regarding changes of data and what tradeoff between reactivity of the system and robustness to noise is required. The more abrupt is forgetting, the higher the reactivity, but also the higher risk of capturing noise is. The most common approach to deal with evolving data generated from processes with unknown dynamics is forgetting the outdated observations. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:13 

**Abrupt Forgetting** _._ At each time, a set of observations defines a window of the information considered for learning. Abrupt forgetting, or partial memory, refers to the mechanisms where a given observation either is inside the window or outside the window. Several window models have been presented in the literature. Two basic types of sliding windows are [Babcock et al. 2002]: _i) Sequence based._ The size of the window is defined in terms of the number of observations. Two different models are _sliding windows_ of size _j_ and _landmark windows_ ; _ii) Timestamp based._ The size of the window is defined in terms of _duration_ . A sliding window stores only the most recent examples in the _first-in-first-out (FIFO)_ data structure; while a landmark window stores all the examples after the landmark timestamp. A landmark window is a window of variable size. A timestamp window of size _t_ consists of all elements whose timestamp is within a time interval _t_ of the current time period. Systems that use abrupt forgetting where discussed in the previous section. 

One of the alternatives to overcome windowing, especially fixed windowing, is sampling. The goal is to capture/summarize the underlying features of the data stream over long periods of time such that the selected sample is drawn uniformly from the stream. One of well known algorithms is the Reservoir Sampling [Vitter 1985]. The goal of reservoir sampling is to obtain a sound representative sample for the stream so far seen. It operates as follows. When the _i_ th item arrives, it is added to the reservoir with probability _p_ = _k/i_ ( _k_ is the size of the reservoir). Then a randomly chosen item is discarded from the reservoir to free space for the new item if added. The _i_ th item is discarded with probability 1 _− p_ . A number of sampling techniques have been investigated like in [Al-Kateb et al. 2007; Efraimidis and Spirakis 2006; Aggarwal 2006; Rusu and Dobra 2009]. Reservoir sampling has been discussed in some studies related to drift, change detection and as an alternative to windowing in [Ng and Dash 2008; Yao et al. 2012; Zhao et al. 2011]. 

**Gradual Forgetting.** _._ Gradual forgetting is a full memory approach, which means that no examples are are dropped out of memory. However, examples in memory are associated with a weight that reflects their age. Example weighting is based on a simple intuition that the importance of an example in the training set should decrease with its age. Suppose that at time _i_ , the stored sufficient statistics is _Si−_ 1 and we observe an example _Xi_ . Assuming an aggregation function _G_ ( _X, S_ ), the new sufficient statistics is computed as _Si_ = _G_ ( _Xi, αSXi−_ 1), where _α ∈_ (0 _,_ 1) is the fading factor, this way the oldest information becomes the least important. 

Linear decay techniques can be found in [Koychev 2000; 2002], and a technique for exponential decay is presented in [Klinkenberg 2004]. The latter technique weights examples according to their age using an exponential ageing function _wλ_ ( _X_ ) = _exp_ ( _−λj_ ), where the example _X_ appeared _j_ time steps ago. The parameter _λ_ controls how fast the weights decrease. For larger values of _λ_ less weight is assigned to the examples and less importance they have. If _λ_ = 0, all the examples have the same weight. Memory methods are summarized in Table I. 

### **3.2. Change Detection** 

The change detection component refers to the techniques and mechanisms for explicit drift and change detection. It characterizes and quantifies concept drift by indicating change-points or small time-intervals of change [Basseville and Nikiforov 1993]. We consider the following dimensions as illustrated in Figure 6: _i)_ methods based on sequential analysis; _ii)_ methods based on control charts; _iii)_ methods based on differences between two distributions; _iv)_ heuristic methods. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:14 

Table I. Categorization of Memory Techniques. 

|**Data Management**|||
|---|---|---|
|Single Example<br>Multiple Examples|Fixed Size|[Schlimmer and Granger 1986],[Littlestone 1987]<br>[Domingos and Hulten 2000],<br>[Kuncheva and Plumpton 2008],[Kelly et al. 1999]<br>[Bouchachia 2011a],[Ikonomovska et al. 2011]<br>[Salganicoff 1997], [Widmer and Kubat 1996],<br>[Syed et al. 1999], [Hulten et al. 2001], [Lazarescu et al. 2004],<br>[Bifet and Gavalda 2006;2007],[Gomes et al. 2011]|
||Variable Size<br>|[Maloof and Michalski 1995], [Klinkenberg 2004],<br>[Gama et al. 2004],<br>[Zhanget al. 2008],[Kuncheva and Zliobaite 2009]|
|**Forgetting Mechani**|**sms**||
|Abrupt Forgetting|Temporal Sequences<br>Sampling|[Salganicoff 1997], [Widmer and Kubat 1996],<br>[Forman 2006],[Klinkenberg2004],[Pechenizkiyet al. 2009]<br>[Ng and Dash 2008],[Yao et al. 2012], [Delany et al. 2005]<br>[Zliobaite 2011a],[Zhao et al. 2011],[Salganicoff 1993]|
|Gradual Forgetting||[Koychev 2000; 2002], [Helmbold and Long 1994],<br>[Klinkenberg2004],[Koren 2010]|
||Detection<br>CHANGE DETECTION|Methods<br>Sequential analysis<br>Control Charts<br>Monitoring<br>two distributions<br>Contextual|



Fig. 6. Taxonomy of control properties of methods. 

We already point-out that online learning systems, without any explicit change detection mechanism can adapt to evolving data. The advantage of explicit change detection is the information about the dynamics of the process generating data. 

A typical control strategy monitors the evolution of the performance indicators [Widmer and Kubat 1996; Zeira et al. 2004] or raw data and statistically compares them to a fixed baseline. A seminal work in adaptive learning with monitoring performance indicators is the `FLORA` family of algorithms. The `FLORA2` algorithm [Widmer and Kubat 1996] includes a window adjustment heuristic for a rule-based classifier. To detect concept changes, the accuracy and the coverage of the current model are monitored and the window size is adapted accordingly. In the context of information filtering monitoring the values of three performance indicators: _accuracy_ , _recall_ and _precision_ has been proposed [Klinkenberg and Renz 1998]. The posterior of each indicator is compared to the standard sample errors of a moving average value. 

_3.2.1. Detectors based on Sequential Analysis._ The _Sequential Probability Ratio Test_ (SPRT) [Wald 1947] is the basis for several change detection algorithms. Let _X_ 1<sup>_n_bea</sup> sequence of examples, where the subset of examples _X_ 1<sup>_w,_1</sup><sup>_<w<n_is generated from</sup> an unknown distribution _P_ 0, and the subset _Xw_<sup>_n_isgeneratedfromanotherunknown</sup> distribution _P_ 1. When the underlying distribution changes from _P_ 0 to _P_ 1 at point _w_ , the probability of observing subsequences under _P_ 1 is expected to be _significantly_ higher than that under _P_ 0: _Significant_ means that the ratio of the two probabilities is no smaller than a threshold. Assuming that observations _Xi_ are independent, the statistic for testing the hypothesis that a change point occurred at time _w_ against the null hypothesis of no change at time _w_ , is given by 



ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:15 

and a change is detected if _Tw_<sup>_n> L_, where</sup><sup>_L_is a user defined threshold.</sup> 

The _cumulative sum_ (CUSUM) is a sequential analysis technique due to [Page 1954] that uses the SPRT rational. It is often used for change detection. The test outputs an alarm when the mean of the incoming data significantly deviates from zero. The input for the test is a residual from any predictor, for instance, the prediction error from a Kalman filter. The CUSUM test is given by _gt_ = max(0 _, gt−_ 1 + ( _xt − δ_ )) ( _g_ 0 = 0), and the decision rule is `if` _gt > λ_ `then signal an alarm` followed by setting _gt_ = 0. Here _xt_ stands for the current observed value, _δ_ corresponds to the magnitude of changes that are allowed, _t_ is the current time and _λ_ is a user defined threshold. Since this expression only detects changes in the positive direction, when negative changes need to be found, the min operation should be used instead of max. In this case, a change is detected when the value of _S_ is below the (negative) value of the threshold. The CUSUM test is memoryless, and its accuracy depends on the choice of parameters _δ_ and _λ_ . Both parameters control the trade-off between earlier detecting the true changes and allowing more false alarms. Low values of _δ_ allow faster detection, at the cost of increasing the number of false alarms. CUSUM has been applied in stream mining, for example, by [Muthukrishnan et al. 2007]. 

The _Page-Hinkley_ [Page 1954] test (PH) is a variant of CUSUM. It is a sequential analysis technique typically used for change detection in signal processing. It allows efficient detection of changes in the normal behaviour of a process established by a model. The PH test is a sequential adaptation of the detection of an abrupt change in the average of a Gaussian signal [Mouss et al. 2004]. The test variable _mT_ is defined as the cumulative difference between the observed values and their mean up until the current time: _mT_ =<sup>�</sup><sup>_T_</sup> _t_ =1<sup>(</sup><sup>_xt−x_¯</sup><sup>_T−δ_),where</sup><sup>_x_¯</sup><sup>_T_=</sup> _T_ <u>1</u> � _Tt_ =1<sup>_xt_and</sup><sup>_δ_specifiesthe</sup> tolerable magnitude of changes. The minimum _mT_ is defined as _MT_ = min( _mt, t_ = 1 _. . . T_ ). PH tests for the difference between _MT_ and _mT_ : _PHT_ = _mT − MT_ . When this difference is greater than a threshold ( _λ_ ) (user defined) a change is flagged. Larger _λ_ will entail fewer false alarms, but might miss some changes. 

Similar to the online versions of CUSUM test, and PH test presented here, Shiryaev & Roberts method, Shiryae’s Bayesian test [Shiryaev 2009; Tartakovsky and Moustakides 2010] rely on online thresholding, that is, as soon as the computed statistic exceeds a pre-set threshold _ε_ , the change is diagnosed. The accuracy of such detection methods often relies on indicators like the false alarm rate and the mis-detection rate. Some of these methods are further explained below. 

_3.2.2. Detectors based on Statistical Process Control._ Control charts, or Statistical Process Control (SPC), are standard statistical techniques to monitor and control the quality of a product during a continuous manufacturing. SPC considers learning as a process, and monitors the evolution of this process. Drift detection methods based on SPC appear in [Klinkenberg and Renz 1998; Lanquillon 2002; Gama et al. 2004; Gomes et al. 2011; Bouchachia 2011a]. 

Let pairs ( _Xi, yi_ ) form a sequence of examples. For each example, the model predicts _y_ ˆ _i_ , that can be either `true` ( ˆ _yi_ = _yi_ ) or `false` ( ˆ _yi̸_ = _yi_ ). For a set of examples, the error is a random variable from Bernoulli trials. The Binomial distribution gives a general form of the probability for the random variable that represents the number of errors in a set of _n_ examples. For each point _i_ in the sequence, the error-rate is the probability _pi_ of observing `false` with the standard deviation _σi_ = ~~�~~ _pi_ (1 _− pi_ ) _/i_ . The drift detector manages two registers during the model operation, _pmin_ and _σmin_ . At time _i_ after casting the prediction for the current example and verifying the prediction error, if _pi_ + _σi_ is lower than _pmin_ + _σmin_ , then _pmin_ = _pi_ and _σmin_ = _σi_ . 

For a sufficiently large number of observations, the Binomial distribution is closely approximated by the Normal distribution with the same mean and variance. Consider- 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:16 

ing that the probability distribution should not change unless a concept drift happens, the 1 _− δ/_ 2 confidence interval for _pi_ with _n >_ 30 examples is approximately _pi ± α × σi_ . The parameter _α_ depends on the desired confidence level. A commonly used confidence level for `Warning` is 95% with the threshold _pi_ + _σi ≥ pmin_ + 2 _∗ σmin_ , and for `Out-of-Control` is 99% with the threshold _pi_ + _σi ≥ pmin_ + 3 _∗ σmin_ . 

Suppose at time _j_ an example ( _Xj, yj_ ) arrives and the model prediction leads to _pj_ and _σj_ . The system is defined to be in one of the following three states: 

- (1) `In-Control` while _pj_ + _σj < pmin_ + 2 _× σmin_ . The error of the system is stable. The example _Xj_ is deemed to come from the same distribution as the previous examples. 

- (2) `Out-of-Control` whenever _pj_ + _σj ≥ pmin_ + 3 _× σmin_ . The error has increased significantly as compared to the recent past examples. With the probability 1 _− δ/_ 2 the recent examples come from a different distribution than the previous examples. 

- (3) `Warning` state is in between of the two previous states. The error is increasing but has not reached `Out-of-Control` yet. This is a not a decisive state. The error may be increasing due to noise, drift, or due to a small deficiency of the predictive model. This state signals that more examples are required for confirming a drift. 

`SPC` can be used to measure the _rate of change_ as the time between `Warning` and `Out-of-Control` . Short times indicate fast changes, longer distances indicate slower changes. The _rate of change_ can also be measured as the rate errors to the number of examples during `Warning` . `SPC` relies on the estimates of the error variance to define action bounds, which shrink as the confidence in the error estimates increases. `SPC` can be implemented inside incremental learning algorithms, or as a wrapper to batch algorithms. (Algorithm 3 in the Appendix). 

The _exponentially weighted moving average_ (EWMA) algorithm [Ross et al. 2012] advances on similar ideas. The EWMA computes a recent estimate of the error rate, _µt_ , by progressively down-weighting older data: _Z_ 0 = _µ_ 0 and _Zt_ = (1 _− λ_ ) _Zt−_ 1 + _λet, t >_ 0, where _et_ is the error at the current example. It can be shown that, independently of the distribution of _Xt_ <u>,</u> the mean and standard deviation of _Zt_ are: _µZt_ = _µt_ and _<u>λ</u> σZt_ = � 2 _−λ_<sup>(1</sup><sup>_−_(1</sup><sup>_−λ_)2</sup><sup>_t_)</sup><sup>_σE_.Assumethatbeforethechangepointthat</sup><sup>_µt_=</sup><sup>_µ_0.The</sup> EWMA estimator _Zt_ fluctuates around this value. When a change occurs, the value of _µt_ changes to _µc_ and _Zt_ will react to this by diverging from _µ_ 0 towards _µc_ . We can signal a change when _Zt > µ_ 0 + _LσZt_ . The parameter _L_ , the control limit, determines how far from _Zt_ must diverge from _µ_ 0 before a change is flagged. 

_3.2.3. Monitoring distributions on two different time-windows._ These methods typically uses a fixed reference window that summarizes the past information, and a sliding detection window over the most recent examples. Distributions over the two windows are compared using statistical tests with the null hypothesis stating that the distributions are equal. If the null hypothesis is rejected, a change is declared at the start of the recent window. The windows can monitor univariate or multivariate raw data (separately for each class), evolving model parameters of performance indicators [Dries and Ruckert 2009]. The two windows can be of equal or progressive sizes and different window positioning strategies may be employed [Adae and Berthold 2013]. 

Comparing distributions on two detection windows<sup>4</sup> in the context of data streams has been introduced in [Kifer et al. 2004]. Examples from two windows are compared with statistical tests based on the Chernoff bound to decide whether the two distributions are different. In the same line, the technique `VFDTc` [Gama et al. 2006] has 

> 4Note that the detection windows are conceptually different from training windows. They may coincide in size. The detection windows are used for estimating data distribution and are typically paired. The training windows determine training data set for the learning algorithm when producing a model. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:17 

the ability to deal with concept drift, by continuously monitoring differences between two distributions classes of examples: the distribution when a node was a leaf and the weighted sum of the distributions in the children leaves of that node. 

[Vorburger and Bernstein 2006] present an entropy-based metric to measure the distribution inequality between two sliding windows including respectively older and more recent examples. If the distributions are equal, the entropy measure results in a value of 1, and if they are absolutely different the measure will result in a value of 0. The entropy measure is continuously monitored over time, and a concept drift is signalled when the entropy measure decreases below a given fixed user-defined threshold. Additional examples include the change detection methods proposed by [Dasu et al. 2006] and [Sebasti˜ao and Gama 2007]. Both use the Kullback-Leibler (KL) divergence to measure the distance between the probability distributions of two different windows (old and recent) to detect possible changes. 

An illustrative example is presented in [Bach and Maloof 2008]. It uses two models: _stable_ and _reactive_ . The stable model predicts based on a long history, whereas the reactive model predicts based on a short recent time window. The technique uses the reactive model as an indicator of concept drift, and it uses the stable model to make predictions, since the stable model performs better than the reactive model when acquiring a target concept. The drift detection method uses the differences in accuracy between the two models to determine when to replace the current stable model, since the stable model performs worse than the reactive model when the target concept changes. Also [Nishida and Yamauchi 2007], consider two accuracies. The accuracy estimated over all the stream and the accuracy estimated over a sliding window of the most recent examples. A concept drift is signalled, whenever a significant decrease of the recent accuracy is observed. 

The `AD` aptive sliding `WIN` dow ( `ADWIN` ) [Bifet and Gavalda 2006; 2007] is a change detector and estimator using a _detection_ window. `ADWIN` takes as inputs a (possibly infinite) sequence of real values _x_ 1, _x_ 2, _x_ 3, . . . , _xt_ , . . . and a confidence parameter _δ ∈_ (0 _,_ 1). Each _xt_ is generated according to some distribution _Dt_ , independently for every _t_ and the value of _xt_ is available only at time _t_ . Denote as _µt_ the expected value of _xt_ when it is drawn according to _Dt_ . Assuming that always _xt ∈_ [0 _,_ 1] by an easy re-scaling the algorithm can handle any case in which we know an interval [ _a, b_ ] such that _a ≤ xt ≤ b_ with probability 1. `ADWIN` slides a fixed detection window _W_ on the most recently read _xi_ . Let _µ_ ˆ _W_ denote the (known) average of the examples within _W_ , and _µW_ the (unknown) average of _µt_ for _t ∈ W_ . We use _|W |_ to denote the length of a (sub)window _W_ . `ADWIN` is summarized in Figure 2 in the Appendix, it operates as follows. Whenever two _large enough_ (sub)windows of _W_ exhibit _distinct enough_ means, the algorithm concludes that the expected values within those windows are different, and the older (sub)window is dropped. _Large enough_ and _distinct enough_ are defined by the Hoeffding bound, testing whether the average of the two (sub)windows is larger 

than _ϵcut_ computed as _ϵcut_ := � 21 _m_<sup>_·_ln4</sup><sup>_<u>|W</u>_</sup> _δ_<sup>_<u>|</u>_</sup> , where _m_ is the harmonic mean of _|W_ 0 _|_ and _|W_ 1 _|_ , i.e. _m_ = 1 _/|W_ 0 _|_ +12 _/|W_ 1 _|_<sup>.</sup><sup>`ADWIN`doesnotassumeanyparticulardatadistribution.</sup> _δ_ is a user defined confidence parameter, the suggested default value is 0 _._ 2. `ADWIN` is equipped with compression using a variant of the exponential histogram [Datar et al. 2002]. Therefore, it does not need to store all the examples from the detection window _W_ , it stores this data in only _O_ (log _W_ ) memory and _O_ (log _W_ ) processing time per item, rather than the _O_ ( _W_ ). 

The adaptation techniques discussed next have originally been coupled with specific change detectors. In general, a strategy can deploy any detector, since the main information that is needed from a detector is whether a change has occurred or not. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:18 

Table II. Complexity of change detection algorithms, _W_ is the size of the detection window. 

|Approach|Memoryat_t_<br>|Processingat_t_<br>|Example algorithms|
|---|---|---|---|
|sequential analysis|_O_(1)|_O_(1)|CUSUM, PH|
|statistical process control|_O_(1)|_O_(1)|SPC|
|monitoringtwo distributions|_O_(log_W_ )_−O_(_W_ )|_O_(log_W_ )_−O_(_W_ )|ADWIN|



_3.2.4. Contextual approaches._ `Splice` system [Harries et al. 1998] presents a metalearning technique that implements a context sensitive batch learning approach. `Splice` is designed to identify intervals with stable hidden context and to induce and refine local concepts associated with these contexts. The idea is to use a time-stamp of the examples as an input feature for a batch classifier. In a first stage, examples are augmented with a time-stamp feature, and a decision tree inducer learns a decision tree. If the decision tree finds splits on the time-stamp feature, the partitions on that feature suggest different contexts. In the second phase, C4.5 is applied to each partition to find interim (temporal) concepts. In the next stage, all examples and interim concepts are given a score based on the accuracy of the concepts in given fixed window (over the time-stamp). This is followed by clustering examples with the highest score for the same concept. Another application of C4.5 then creates new interim concepts. 

Independently of use of any time windowing, very often robust approaches that yield a balance between incremental learning and forgetting are needed to deal with changing environments. This idea was applied in the IFCS algorithm [Bouchachia 2011a] in the context of classification. There three mechanisms, called staleness, penalization and overall accuracy, which are associated with the individual prototypes that form the classifier, are combined. The first two measures intend to tackle the problem of model complexity, but also gradual drift. If one of the two measure values falls below a very small threshold, called removal threshold, the prototype is removed. The last one is intended for handling gradual and abrupt drift. Staleness tracks the activity of the prototype in making decisions about the new input and such an activity indicates that the recent incoming new input emanate from the input space covered by the prototype. Stale prototypes tend to cover obsolete regions. To express the staleness mechanism, the following formula is used: _w_ ( _i_ ) = _ζ_<sup>_t−at_</sup> where _t_ and _at_ indicate, respectively, the current time index and the last time the prototype _i_ was a winner. Small values of the forgetting factor _ζ_ accelerates the reduction in the weight. The weights are associated with the prototypes. Their value for stale prototypes decays and for active prototypes it reinforces. Clearly, if the staleness is long (that is _t − at_ is large enough, _wi_ diminishes and then the prototype vanishes. 

The second mechanism is about tracking the accuracy of the decisions made and thus observing the evolution of the model in terms of consistency with the recent input patterns. The aim is to ensure that the accuracy does not deteriorate (at least significantly). The following formula has been used: _zi_ = _λ_<sup>_si_</sup> where _si_ is number of errors made by the prototype since it has been created. The weight decreases exponentially as the number of errors increases. The smaller the value of _λ_ , the more quickly are the forgetting speed and the model update. The third mechanism is the Statistical Process Control (SPC) criterion which is explained in Section 3.2.2 and which aims at handling gradual and abrupt changes based on the number of errors produced by the learning model during prediction. 

Table II summarizes properties of the presented change detection algorithms. Overall, comparing two distributions for change detection requires more computational resources than detecting based on the evolution of indicators, but potentially may give more precise information about the location of change. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:19 

Table III. Categorization of Change Detection Techniques. 

||Detection Methods|
|---|---|
|Sequential analysis|[Wald 1947], [Page 1954], [Mouss et al. 2004]<br>[Muthukrishnan et al. 2007],[Ikonomovska et al. 2011]|
|Control Charts|[Lanquillon 2002],[Gama et al. 2004]<br>[Kuncheva 2009],[Gomes et al. 2011],[Ross et al. 2012]|
||[Kifer et al. 2004], [Bifet and Gavalda 2006; 2007]|
|Monitoring two distributions|[Vorburger and Bernstein 2006], [Leeuwen and Siebes 2008]<br>[Gama et al. 2006], [Nishida and Yamauchi 2007], [Bach and Maloof 2008],<br>[Dries and Ruckert 2009],[Kuncheva 2013]|
|Contextual|[Harries et al. 1998],[Klinkenberg2004]|





<!-- Start of picture text -->
Incremental<br>Retraining<br>Learning Mode Online<br>Incremental<br>Streaming<br>Blind<br>Adaption Methods Local or partial<br>Informed replace/updating<br>Global or complete<br>replacement<br>Single model Reoccurrence<br>Model Management<br>Active model pool management<br>Ensemble<br>Model selection<br>Model weighting<br>LEARNING<br><!-- End of picture text -->

Fig. 7. Taxonomy of learning properties of methods. 

### **3.3. Learning** 

The Learning component refers to the techniques and mechanisms for generalizing from examples and updating the predictive models from evolving data. This Section is organized as follows: _i) Learning mode_ referring to model updating when new data points are available; _ii) Model adaptation_ analyze the behaviour of predictive models in time-evolving data; _iii) Model management_ refers to the techniques to maintain active predictive models. 

_3.3.1. Learning Mode._ Whenever new labeled examples are available, the learning system might update the model. We consider two different learning modes: **Retraining** that discards the current model and builds a new model from scratch using buffered data; **Incremental** adaptation updates of the model. 

Retraining approaches need some data buffer to be stored in memory. Retraining have been used to emulate incremental learning with batch learning algorithms [Gama et al. 2004]. At the beginning a model is trained with all the available data. Next, whenever new data arrives, the previous model is discarded, the new data is merged with the previous data, and a new model is learned on this data [Street and Kim 2001], [Zeira et al. 2004], [Klinkenberg and Joachims 2000]. 

Incremental approaches update the current model using the most recent data. **Incremental** algorithms process input examples one-by-one and update the sufficient statistics stored in the model after receiving each example. They might have access to previous examples or summaries of examples. This is the case of `CVFDT` [Hulten et al. 2001] described in the next section. The **Online** learning mode updates the current model with the most recent example. They are error-driven updating the current model depending on it misclassifies the current example. Examples include `WINNOW` [Littlestone 1987], `MBW` [Carvalho and Cohen 2006]. `MBW` [Carvalho and Cohen 2006] refers 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:20 

that well-known algorithms, including `perceptron` and _Multi-layer perceptrons_ , that have been traditionally trained using several passes through the training data, when restricted to a single training pass over the data are particularly relevant for massive and streaming data [Carvalho and Cohen 2006]. The origins of online learning origin goes back to the late 60s, with `Perceptron` [Rosenblatt 1958], and early 2000 with the advent of the paradigm of ”prediction with expert advice” [Cesa-Bianchi and Lugosi 2006]. The early work appeared in a number of seminal papers [Littlestone 1987; Littlestone and Warmuth 1994; Herbster and Warmuth 1998; Vovk 1998]. The model is updated with the current example. As time goes on, the newly arrived data tend to erase away the prior patterns. In models, such as artificial neural networks, learning is inevitably connected with forgetting. The ability to continuously learn from a stream of examples while preserving previously learned knowledge is known as the _stabilityplasticity_ dilemma [Carpenter et al. 1991a]. It is a dilemma because there needs to be a balance between being stable to handle noise and being able to learn new patterns. Some artificial neural networks completely forget the past patterns when exposed to a new set of patterns; this phenomenon is known as the _catastrophic forgetting_ [French 1994; Polikar et al. 2001]. 

**Streaming** algorithms are online algorithms for processing high-speed continuous flow of data. Examples are processed sequentially and can be examined in only a few passes (typically just one). These algorithms use limited memory and control the available memory. For example Hoeffding trees [Domingos and Hulten 2000] and variants `VFDTc` [Gama et al. 2006] or `FIMT-DD` [Ikonomovska et al. 2011], are able to freeze leaves when memory becomes scarce. 

_3.3.2. Adaptation Methods._ The adaptation strategies manage adaptation of the predictive model. They fall into two major types: _blind_ and _informed_ . 

The **blind** adaptation strategies adapt the model without any explicit detection of changes. **Blind** adaptation, typically use techniques as _fixed size sliding windows_ that take a window size _w_ as a parameter and periodically retrain the model with the latest _w_ examples, and _example weighting_ that consider the importance of training examples [Widmer and Kubat 1996; Klinkenberg and Renz 1998; Klinkenberg and Joachims 2000; Lanquillon 2002]. 

A special case of blind adaptation are incremental and online learning where the model evolves with data. Without any strategy to explicitly detect concept drift, the model adapts to the most recent data. A paradigmatic example is VFDT [Domingos and Hulten 2000]. In VFDT, new examples update statistics in the leaves of the current model. As the tree grows and new leaves are generated, the label in the these leaves reflect the most recent concepts. The blind strategies are proactive, they update the model based on the loss function. The main limitation of the blind approaches is slow reaction to concept drift in data. The blind approaches forget old concepts at a constant speed independently of whether changes are happening or not. When changes are happening it may be more beneficial to discard old data faster, and discard old data slower or not discard at all at times when changes are not happening. 

The **informed** strategies are reactive, their actions depend on whether a trigger has been flagged [Bifet and Gavalda 2006; Hulten et al. 2001]. Triggers can be either change detectors (examples described in Section 3.2) or specific data descriptors that we will see in the _reoccurring concept management_ techniques [Widmer and Kubat 1996]. Change detectors can be independent from the adaptation strategy (e.g. the _adaptive training window_ technique) or they can be closely integrated with the adaptation strategy [Gama et al. 2006; Ikonomovska et al. 2011] which we refer to as _model integrated detectors_ [Gama et al. 2006]. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:21 

The reaction to a drift signal might apply to the model as a whole, or might explore characteristics of the language used to represent generalization of examples. 

**Global Replacement** _._ Informed adaptation in global models (such as linear regression, discriminant classifiers, naive Bayes) require full reconstruction of the model. This is the most radical reaction to a drift. The full model is deleted and a new model is started from scratch. This strategy has been widely used, for example in [Gama et al. 2004],[Street and Kim 2001], [Zeira et al. 2004], [Klinkenberg and Joachims 2000]. 

**Local Replacement** _._ In many cases changes occur only in some regions of the data space. For example, in spam filtering the spammers may start using combinations of words such as ”Facebook support” that were previously associated with legitimate e- mails. This change in the concept of spam will affect only a small subset of all the incoming e-mails [Carmona-Cejudo et al. 2010]. 

_Granular_ models, such as decision rules or decision trees, can adapt parts of the model. In a decision tree (or decision rules), each node (or rule) covers a hyper-rectangle in the data space. Thus, such decomposable models only need to adapt those nodes that cover the region of the data space affected by concept drift. `CVFDT` [Hulten et al. 2001] continuously monitors the quality of previous decisions (splitting features) with respect to a sliding window of fixed size over the most recent data stream. `CVFDT` maintains a window of training examples and keeps its learned tree up-to-date with this window by monitoring the quality of its old decisions as data moves into and out of the window. In particular, whenever a new example is read it is added to the statistics at all the nodes in the tree that it passes through, the last example in the window is forgotten from every node where it had previously had an effect, and the validity of all statistical tests are checked. If `CVFDT` detects a change it starts growing an alternate tree in parallel which is rooted at the newly-invalidated node. When the alternate is more accurate on new data than the original the original is replaced by the alternate and freed. 

Each node in a Hoeffding tree captures statistics from a time window over the stream. The root node receives the oldest examples, the leaf nodes receive the most recent examples. Nodes near the root were generated using examples older than those that generated nodes near the leaves. This observation is on the basis of _Sequential regularization_ [Gama et al. 2006; Ikonomovska et al. 2011]. The technique compares the distribution of the errors at leaves to the distribution of the errors at upper nodes in the tree. Recall that the leaves contain the most recent information and the upper nodes contain older information. Thus, if the two error distributions are significantly different that is interpreted as a concept drift. In [Gama et al. 2006], when a concept change is detected, the system adapts the model, assuming that the most recent information contains the useful information about the current concept. The statistics of the most recent examples incorporated in the tree are stored in the leaves. Therefore, supposing that the change of concept was detected in the node _i_ , the reaction method _pushes up_ all the information of the descending leaves to the node _i_ , namely the sufficient statistics and the classes distributions. The decision node becomes a leaf and the sub-tree rooted at the decision tree is pruned. This forgetting mechanism removes the outdated information. 

_3.3.3. Model Management._ Ensemble learning maintains in memory an ensemble of multiple models that make a combined prediction. Adaptive ensembles are often motivated by the assumption that during a change, data is generated from a mixture distribution, which can be seen as a weighted combination of distributions characterizing the target concepts, each individual model models a distribution [Scholz and 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:22 

Klinkenberg 2007]. The final prediction is typically a weighted average of the individual predictions, where the weight reflects the performance of the individual models on the most recent data. The weights change over time. 

Ensemble methods for dynamically changing data can be categorized [Kuncheva 2004] into three types: ( **i** ) dynamic combination where the base learners are trained in advance and dynamically combined to respond to the changes in the environment by changing the combination rule ( `WINNOW` and weighted majority are often used [Littlestone 1987; Blum 1997; Tsymbal et al. 2006; Widmer and Kubat 1996]); ( **ii** ) continuous update of the learners such that the learners are either retrained in batch mode or updated online using the new data [Breiman 1999; Fern and Givan 2003; Oza 2001] (the combination rule may or may not change in the process); ( **iii** ) structural update where new learners are added (or existing ones are activated if they deactivated) and inefficient ones are removed (or deactivated) [Kolter and Maloof 2003; Street and Kim 2001; Bouchachia 2011b]. These three categories do not necessarily need to be mutually exclusive, an ensemble combining two or all three types of strategies is technically possible. 

In connection to data drift and online learning, the application of ensemble learning has been the subject of some investigations over the recent past years. For instance, in [Elwell and Polikar 2011] a batch-based ensemble of classifiers, called Learn++.NSE, is proposed to deal with concept drift. The proposed algorithm aims at coping with drift regardless of the rate and type of drift and the number concept classes present at any time. For each new batch of data, a new classifier is trained and combined using a dynamically weighted majority voting strategy. 

In [Minku et al. 2010] diversity of learning ensemble is investigated in presence of different types of drifts. The study shows that before the drift occurs, ensembles with less diversity obtain lower test errors, but shortly after the drift occurs, highly diverse ensembles are better regardless the type of drift. Longer after the drift, high diversity becomes less important. 

The SEA algorithm [Street and Kim 2001] is one of the first techniques to handle concept drift with classifier ensembles learned from streaming data. It trains a separate classifier on each sequential batch of training examples. A trained classifier is added to a fixed-size ensemble, while the worst performing classifier is discarded. The final prediction is made using a simple majority voting. 

A seminal work is the Dynamic Weighted Majority algorithm (DWM) [Kolter and Maloof 2003; 2007] that is an adaptive ensemble based on the Weighted Majority algorithm [Littlestone 1987]. It can be used with any on-line learning algorithm in timechanging problems with unknown dynamics. `DWM` maintains an ensemble of predictive models, each with an associated weight. Models are generated by the same learning algorithm on different batches of data. `DWM` dynamically creates and deletes experts in response to changes in performance. `DWM` makes predictions using a weighted-majority vote of these models, and the weights are dynamically changing. The weights of all the models that misclassified the current example are decreased by a multiplicative constant _β_ . If the overall prediction is incorrect, a new expert is added to the ensemble with weight equal to 1. Finally, all the models are incrementally updated with the current example. To avoid creating an excessive number of models `DWM` prunes the ensemble by removing the poorly performing experts with a weight less than a threshold. A variant of DWM called AddExp [Kolter and Maloof 2005] is an extension for classification and regression that is intelligently prunes some of the previously generated models. 

A similar approach, but using a weight schema similar to boosting and explicit change detection appears in [Chu and Zaniolo 2004]. A boosting-like approach to train a classifier ensemble from evolving data streams is also proposed in [Scholz and 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:23 



<!-- Start of picture text -->
Model dependent<br>Sliding Window<br>Model Independent<br>Fading Factor<br>LOSS ESTIMATION<br><!-- End of picture text -->

Fig. 8. Taxonomy of loss estimation properties of methods. 

Klinkenberg 2007], where the dynamics of classifier weights is controlled by the _lift_ measure instead of accuracy, which measures the correlation between predictions and their true label. 

A general framework for mining concept-drifting data streams using weighted ensemble classifiers has been proposed in [Wang et al. 2003]. An ensemble of predictive models (e.g. `C4.5` , `RIPPER` , Naive Bayes) are trained on sequential batches of a data stream. Weighted voting is used to make the final prediction, the weights follow the expected predictive accuracy of each model. Suppose we have a training data set _D_ and a classifier _Li_ . Let _c_ be the true label of example _X_ and _Mc_ ( _X_ ) be the probability that _X_ belongs to class _c_ output by _Li_ . The mean square error of the classifier is _MSE_ = _|D_ <u>1</u> _|_ � _X∈D_<sup>(1</sup><sup>_−Mc_(</sup><sup>_X_))2.Theweightoftheclassifier</sup><sup>_L_shouldbere-</sup> versely proportional to its MSE, the weight reflects the benefit of using this individual model in comparison to a random classifier. The MSE of a random classifier is _MSEr_ =<sup>�</sup> _c_<sup>_p_(</sup><sup>_c_)</sup><sup>_×_(1</sup><sup>_−p_(</sup><sup>_c_))2, where</sup><sup>_p_(</sup><sup>_c_) is the probability of observing class</sup><sup>_c_. Thus,</sup> the weight _wi_ of a classifier _Li_ is _wi_ = _MSEr − MSEi_ . 

A notable technique `DDD` [Minku and Yao 2011] equips a dynamic ensemble with a diversity control mechanism, and also uses an internal drift detection to speed up adaptation. Initially the model is composed of two ensembles: a low diversity ensemble and a high diversity ensemble. Both ensembles are trained with incoming examples, but only the low diversity ensemble is used for predicting. The weights of individual models are proportional to the prequential accuracy (described in Section 4). `DDD` assumes that, if there is no convergence of the underlying distributions to a stable concept, there is a drift. `DDD` then allows to use the high diversity ensemble for predictions. Online bagging (corresponding to sampling with replacement) is used to control diversity levels in the two ensembles. 

**Reoccurring concept management.** `FLORA3` [Widmer and Kubat 1996] is the first adaptive learning technique for the tasks where concepts may reoccur over time. More recent works discussing reoccurring concepts appear in [Widmer 1997; Yang et al. 2006; Katakis et al. 2010; Gama and Kosina 2011] . In such settings, instead of discarding outdated models, it might be useful to store the learned models in a sleeping mode. Following this idea, the work presented in [Gama and Kosina 2011], discuss a generic framework that identifies context using drift detection, characterizes contexts using meta-learning, and select the most appropriate predictive model for the incoming data using unlabeled examples. The proposed framework is based on a meta-learning schema which aims to recognize the area of applicability of the individual model. 

### **3.4. Loss estimation** 

Supervised adaptive systems rely loss estimation based on environment feedback. The discussion in this section is close related with the performance related metrics discussed in Section 4.2. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:24 

Table IV. Categorization of Learning Techniques. 

|**Learning Mode**||
|---|---|
|Retraining<br>|[Street and Kim 2001],[Zeira et al. 2004],[Klinkenbergand Joachims 2000]<br>|
|Incremental<br>|[Schlimmer and Granger 1986],[Littlestone 1987],<br>[Bifet et al. 2009],[Hulten et al. 2001],[Polikar et al. 2001]<br>|
|Streaming|[Gama et al. 2006],[Ikonomovska et al. 2011]|
|**Adaptation Methods**||
|Blind|[Littlestone 1987], [Maloof and Michalski 2000], [Klinkenberg and Renz 1998]<br>[Chu and Zaniolo 2004],[Bessa et al. 2009]|
|Informed|[Hulten et al. 2001],[Gama et al. 2006],[Ikonomovska et al. 2011]|
|**Model Adaptation**||
|Model Specific<br>Model Independent|[Hulten et al. 2001], [Gama et al. 2006], [Harries et al. 1998]<br>[Wald 1947], [Gama et al. 2004], [Wang et al. 2003]<br>[Bifet and Gavalda 2006],[Kuncheva and Zliobaite 2009]|
|**Model Management**||
|Single Model<br>Recurrent|[Hulten et al. 2001], [Gama et al. 2006], [Ikonomovska et al. 2011]<br>[Widmer 1997], [Gama and Kosina 2011]|
|Ensemble<br>Recurrent|[Polikar et al. 2001], [Street and Kim 2001],[Kolter and Maloof 2005],<br>[Gao et al. 2007], [Minku and Yao 2011], [Elwell and Polikar 2011]<br>[Yanget al. 2006],[Katakis et al. 2010],[Gomes et al. 2011]|



**Model Dependent** _._ As we previously referred [Klinkenberg and Joachims 2000] recognize and handle concept changes using properties of Support Vector Machines. Their method maintains a window over the training examples that minimizes the leave-one-out error estimate. The key idea is to get an estimate of the generalization error using the so-called _ςα_ -estimates, an efficient method for estimating the leaveone-out error of SVM. Leave-one-out estimators are accurate estimators but usually very expensive: one must run the learner so many times as the number of training examples. For SVM _ςα_ -estimate can be computed for free once a SVM has been trained. It is computed as the percentage of training points that are between the margins. The theoretical properties of this estimator is discussed in [Joachims 2000]. Analytical loss estimation for the linear discriminant classifiers can be found in [Zliobaite and Kuncheva 2009]. 

**Model Independent** _._ As already referred, several works [Bach and Maloof 2008] [Nishida and Yamauchi 2007] [Gama et al. 2013], propose to detect changes using two sliding windows: a short window containing the most recent information and a large window, used as reference, containing a larger set of recent data including the data in the short window. The rationale behind this approach is that the short window is more reactive while the large window is more conservative. When a change occurs, statistics computed in the short window will capture the event faster than using the statistics in the larger window. Similarly, using fading factors, a smooth forgetting mechanism, a smaller fading factor will detect drifts earlier than larger ones. Based on this assumption, [Gama et al. 2013] propose to perform the PH test with the ratio between two error estimates: a long term error estimate (using a large window or a fading factor close to one) and a short term error estimate (using a short window or a fading factor smaller than the first one). A drift is signaled when the short term error estimator is significantly greater than the long term error estimator. The PH test monitors the evolution of ratio of both estimators and signals a drift when a significant increase of this variable is observed. The authors refer that the choice of _α_ in fading factors and the window size is critical. Their experiments show that drift detection based on the ratio of fading estimates is somewhat faster that with sliding windows. 

### **3.5. Discussion** 

Supervised adaptive learning algorithms rely on immediate arrival of feedback (true labels). In reality labels may become known immediately in the next time step after casting the prediction (e.g., food sales prediction). However, feedback can come with an 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:25 

Table V. Categorization of Loss estimation Techniques. 

|**Loss Estimation**|||
|---|---|---|
|Model Dependent||[Klinkenbergand Joachims 2000],[Zliobaite and Kuncheva 2009]|
|Model Independent|Slidind Window|[Maloof and Michalski 1995], [Klinkenberg 2004], [Bach and Maloof 2008],|
|||[Nishida and Yamauchi 2007], [Gama et al. 2013]|
||FadingFactors|[Koychev 2000] [Koychev 2002],[Gama et al. 2013]|



uncontrollable delay, be unreliable, biased or costly. Labels may arrive within a fixed or variable time lag (in credit scoring typically the horizon of bankruptcy prediction is fixed, for instance, to one year, thus the true labels become known after one year has passed). Alternatively, the setting may allow to obtain labels on demand (e.g. in email spam categorization we can ask the user the true status of a given message). 

### **4. EVALUATION** 

In order to perform an experimental evaluation of any machine learning technique, we need to consider first of all (i) performance evaluation metrics chosen according to the goal of a learning task and the operational settings, and (ii) a methodology allowing to compute the corresponding estimates in the streaming settings. Besides, we may need to find a justify whether one model (or technique) is superior to the other or not. 

In this section we consider typical choices peculiar for evaluating an adaptive learning technique capable to handle concept drift. First, we discuss the performance evaluation metrics, then present possible experiment designs and conclude with pointers to the performance benchmarking. 

### **4.1. Performance evaluation metrics** 

Performance evaluation metrics may be selected from the traditional accuracy measures, such as precision and recall or their weighed average in retrieval tasks, sensitivity and specificity or their weighed average in medical diagnostics, mean absolute scaled errors in regression or time-series prediction tasks, root mean square error in recommender systems. 

It is important to consider appropriate reference points or baseline approaches in particular settings. For example, one common baseline in time series prediction is a moving average prediction, in its simplest form known as _tomorrow will look the same like today_ prediction. Such a baseline gives reference points allowing to judge how much improvement a supposedly intelligent adaptive technique can achieve over a naive approach. 

In addition, taking into account practical considerations of the streaming settings, we may consider the following measures: 

- _A one-dimensional measure of the (computational) cost of the mining process._ For example, in [Bifet et al. 2010b] the use of RAM-Hours was introduced as an evaluation measure of the resources used by streaming algorithms. Every GB of RAM deployed for 1 hour equals one RAM-Hour. It is based on rental cost options of cloud computing services. 

- _A real-time unbalanced class measure of accuracy._ The Kappa-Statistic may be a good measure for such cases. Besides taking into account class-imbalance it is also very efficient to compute as compared to e.g. the area under the ROC curve. 

Besides evaluating the performance of the learning strategy as a whole we may like to estimate the accuracy of change detection for those strategies that employ explicit drift detection as part of the concept drift handling strategy. The following criteria are relevant for evaluating change detection methods. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:26 

- _Probability of true change detection._ This measure characterizes the capacity of the learning system to detect and react to drifts when they occur. 

- _Probability of false alarms._ This measure characterizes the resilience to false alarms when there is no drift, that is detecting drift when there is no change in the target concept. Instead of reporting the commonly used false positive rate for change detections, in the streaming settings we may use the inverse of the _time to detection_ or the _average run length_ , the expected time between false positive detections as potentially more meaningful performance characteristic. This measure can be computed appropriately using data without drifts, then all the detections are counted as false alarms. Although, it could be possible to count false alarms in the case of gradual drifts, where more than one drift detection may appropriately occur, it is recommended to count false alarms only in the case that there is no drift in the data. 

- _Delay in or time lag of detection._ These measures give the estimate of how many new instances are required to detect a change after the actual occurrence of a change (or how much time would elapse before the change is detected). 

- _Detection point accuracy._ Besides the delay in detection we may want to know the accuracy of change localization. We can estimate it by counting the number of instances from the point that is detected as a change point to the true change point. 

When we know how well the employed change detection methods perform we can also quantify the effect of particular error (or delay) in change detection on the overall performance of the adaptive model. 

### **4.2. Experimental design** 

The most common procedure for estimating the performance of supervised learning techniques in the traditional settings with static data is cross-validation. In traditional batch learning the problem of limited data is overcome by analyzing and averaging multiple models produced with different random arrangements of training and test data. However, cross-validation is not directly applicable to the streaming settings with evolving data because it would mix the temporal order of data. 

In the stream setting the problem of effectively unlimited data poses different challenges. One solution involves taking snapshots at different times during the induction of a model to see how much the model improves. The evaluation procedure of a learning algorithm determines which instances are used for training the algorithm, and which are used to test the model output by the algorithm. When considering what procedure to use in the data stream setting, one of the main concerns is how to build a picture of accuracy over time: one classifier may do well on the first half on the stream, and badly on the second. It is important to notice that streaming evaluation measures may be evolving over time. 

_4.2.1. Evaluation on time-ordered data._ We discuss two common procedures peculiar to the evaluation of adaptive supervised learning techniques: _holdout_ and _prequential_ evaluation, and point to a recent idea of the controlled permutations. 

**Holdout.** When traditional batch learning reaches a scale where cross-validation is too time consuming, it is often accepted to instead measure performance on a single holdout set. This is most useful when the division between train and test sets has been pre-defined, so that results from different studies can be directly compared. When testing a model at time _t_ , the holdout set represents exactly the same context at that time _t_ . The loss estimated in the holdout is an unbiased estimator. Unfortunately, it is not always possible to use holdout because it is not always possible to know for sure what examples belong to the concept that is active at time _t_ . 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:27 

**Interleaved Test-Then-Train or Prequential.** Each individual instance can be used to test the model before it is used for training, and from this the accuracy can be incrementally updated. When intentionally performed in this order, the model is always being tested on instances it has not seen before. This scheme has the advantage that no holdout set is needed for testing, making maximum use of the available data. It also ensures a smooth plot of accuracy over time, as each individual instance will become increasingly less significant to the overall average. The prequential error is computed based on an accumulated sum of a loss function between the prediction and observed values: _S_ =<sup>�</sup><sup>_n_</sup> _t_ =1<sup>_f_(ˆ</sup><sup>_yt, yt_).</sup> 

There are three prequential evaluations: using a landmark window( _Interleaved Test-Then-Train_ ) a sliding window, or forgetting mechanism. The holdout evaluation gives a good estimation of the accuracy of the model on recent data. However, it requires recent test data that it is difficult to obtain for real datasets. In such a case a forgetting mechanism for estimating holdout accuracy [Gama et al. 2013] can be used, that is based on the prequential accuracy over a sliding window of size _w_ with the most recent observations, or fading factors that weigh observations using a decay factor _α_ . These mechanisms give an estimation of the accuracy that is approximate to the accuracy estimation obtained doing a holdout evaluation. 

**Controlled permutations.** Averaging the accuracy over time has a potential problem, it may mask the adaptation properties of adaptive learning algorithms. For example, if one algorithm does very well on the first half of data, and very badly on the second; while another algorithm would show and average, but consistent performance, taking an average over accuracies would mask that. Even the prequential evaluation may produce biased results towards the fixed order of data in a sequence, as it runs only one test in a fixed order of data. To reduce this risk, _controlled permutations_ evaluation [Zliobaite 2011b] runs multiple tests with randomized copies of a data stream, in a theoretical way restricted, so that different distributions from the original data are approximately preserved in permutations. Randomization aims at keeping the instances, that were originally nearby in time, close together. The technique suits best to data streams with sudden drifts, but is also applicable to streams with other drifts. Controlled permutations allow to generate multiple test sets for testing adaptive techniques that enable assessing volatility and robustness of models, optimize their parameters and this way reduce the risk of overfitting the order of data in a sequence. 

_4.2.2. Cross-validation with aligned series of data._ In many cases we use an adaptive learning technique to learn not a single adaptive model for the data stream associated with an individual object (e.g. predicting antibiotic resistance within a particular hospital), but to learn multiple models, one adaptive model per object, e.g. we want to predict food sales for each of the product in the stock or popularity of each moving in a movie renting store. Each object corresponds to a data steam on which we apply an adaptive model. Each data stream is an analogue of a dataset (when we compare the performance of different classification techniques over multiple datasets), but in this settings, different data streams would be still alike, i.e. sharing the same feature space or being of the same nature. In such cases it is logical to estimate the performance of the adaptive learning strategy across multiple objects. 

This method is rather generic for many real problems when a need for a more exact evaluation setting justifies the use of large computational resources, for example e.g. sales, recommendations, advertising, sentiment classification across topics or sources. Figure 9 illustrates the estimation of the generalization performance of the technique(s) across multiple individual (but related) data streams by cross validating the data streams. For every individual data stream we can use one of the described (prequential, hold-out or controlled permutations) evaluation procedures. A subset of 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:28 



<!-- Start of picture text -->
TRAINING part TESTING part<br>series 1<br>TRAINING-VALIDATION series 2 Fold 1<br>series for<br>model selection or<br>parametrization Fold 2<br>final TEST series for<br>estimating the  Fold 3<br>generalization error series N<br><!-- End of picture text -->

Fig. 9. Estimating the generalization performance of the technique(s) across multiple individual (but related) data streams by cross validating the data streams. 

data streams can be used to run the the learning strategy with different parameterizations to identify to most reasonable parameter settings for the particular domain and then verify them on the remaining testing data streams. The values of the performance metrics can be averaged over data stream in the test basket (and averaged over the multiple cross-validation runs). 

_4.2.3. Statistical significance._ Evaluating classifiers, we should be concerned with the statistical significance of the results at particular points of the learning process. Looking at the performance of only one classifier, it is convenient to give some insights about its statistical significance. We may use _confidence intervals_ , that are interval estimates of parameters to indicate the reliability of an estimate. To do that, we can use Chernoff or Hoeffding bounds, sharper inequalities than Markov’s or Chebyshev bounds. 

When comparing two classifiers we need to distinguish between random and nonrandom differences in the experimental accuracies. The McNemar test [McNemar 1947] is a non-parametric test used in the stream mining literature to assess the statistical significance of differences in performance of two classifiers. This test needs to store and update two variables: the number of instances misclassified by the first classifier and not by the second one _a_ , and _b_ the number of instances misclassified by the second classifier and not by the first one. The McNemar statistic ( _M_ ) is given as _M_ = _sign_ ( _a−b_ ) _×_ ( _a−b_ )<sup>2</sup> _/_ ( _a_ + _b_ ). The test follows the _χ_<sup>2</sup> distribution. At 0 _._ 99 confidence it rejects the null hypothesis (the performances are equal) if _M >_ 6 _._ 635. 

When comparing more than two classifiers, the Nemenyi test [Demsar 2006] is used for computing significance: it is an appropriate test for comparing all classifiers to all classifiers over multiple datasets, being based on the average ranks of the algorithms across all datasets. The Nemenyi is recommended for use after a rejection of the null hypothesis by Friedman. The Nemenyi test is the following: two classifiers are performing differently if the corresponding average ranks differ by at least the critical difference _CD_ = _qα_ � _k_ ( _k_ + 1) _/_ 6 _N_ where _k_ is the number of learners, _N_ is the number of datasets, and critical values _qα_ are based on the Studentized range statistic divided by _√_ 2. Other tests can be recommended when all classifiers are compared to a control classifier [Demsar 2006]. For example, the Dunnett test can be used [Dunnett 1955]. 

### **4.3. Performance benchmarking** 

To perform a benchmarking comparing several methods, we need to use some large datasets and software implementations of the algorithms. There are two types of dataset: artificial or real datasets. Artificial datasets are useful because they give the ground truth of the data, for example, all the points when the changes occur. However, real datasets are more interesting as they correspond to real-world applications where the algorithms usability is tested. Some authors use the term _real world dataset_ to refer to data sets using real world data with forced drifts, that cannot be considered as completely real. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:29 

Appendix B presents popular artificial and real datasets that are publicly available. MOA is an open-source software to run data streaming experiments. It is written in Java and it is based on the experience of WEKA. It contains methods for classification, regression, clustering and frequent pattern mining. Online appendix C shows an example of evaluating classification under concept drift using MOA. 

### **5. CONCLUSIONS** 

We presented the conceptual categorization of many existing adaptive learning strategies, capable of handling concept drift, along with the concrete state-of-the-art techniques. We highlighted the peculiarities of the evaluation methodology for experimenting with adaptive learning techniques in the data stream settings. The problem of concept drift has been recognized in different application domains. Further interest to adaptive learning has been boosted by the outcomes of several recently organized contests or challenges in AI (controlling driverless cars at the DARPA challenge), data mining and knowledge discovery (credit risk assessment competition at PAKDD’09), and recommender systems (Netflix movie recommendation) fields. Winning teams in each of these competitions emphasize that one of key factors in their success was due to addressing temporal dynamics and various (hidden) contexts affecting their concepts of interest. Therefore, we also referred to the conceptual categorization of typical application settings in which adaptive learning systems have to operate and discussed the lessons learnt from the real world cases of handling concept drift. We hope that besides serving as an introduction into the research area of adaptive learning under concept drift this article will help to position a new adaptive learning technique and application settings to which they apply. 

Most of the work on concept drift assumes that the changes happen in hidden context that is not observable to the adaptive learning system. Hence, concept drift is considered to be unpredictable and its detection and handling is mostly reactive. However, there are various application settings in which concept drift is expected to reappear along the time line and across different objects in the modeled domain. Seasonal effects with vague periodicity for a certain subgroup of object would be common e.g. in food demand prediction [Zliobaite et al. 2012a]. Availability of external contextual information or extraction of hidden contexts from the predictive features may help to better handle recurrent concept drift , e.g. with use of a meta-learning approach [Gama and Kosina 2011]. 

Temporal relationships mining can be used to identify related drifts, e.g. in the distributed or peer-to-peer settings in which concept drift in one peer may precede another drift in related peer(s) [Ang et al. 2012]. In all these settings more accurate, more proactive and more transparent change detection may become possible. 

The vast majority of the work on concept drift detection summarized in this survey does not address the problem of representation bias that is common to most of the adaptive systems that enforce or suggest particular type of behavior. Whenever there is a reinforcement feedback or a closed-loop control of the learning mechanism, we cannot evaluate and compare the performance of concept drift handling techniques by replaying historical data. Therefore, we can speculate that there will be more studies that try to embed concept drift handling technique in real operational settings for proper validation. While the majority of work on handling concept drift has focused on supervised settings with immediate availability of labels, the actual problem space is much wider. In unsupervised learning over evolving data, and in case of delayed and on-demand labeling in supervised learning, validation of change detection and adaptation mechanisms only start to be investigated. 

Research on concept drift goes beyond the areas of machine learning, data mining, and pattern recognition in which the term was originally coined and studied most. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

1:30 

Thus, in Process Mining<sup>5</sup> [van der Aalst 2012; 2011], the area of research dealing with the different kinds of analyses of (business) processes by extracting information from event logs recorded by an information system, handling concept drift has been recognized as an important problem [Carmona and Gavald`a ; Bose et al. 2013]. 

### **5.1. Next challenges** 

The next challenges for concept drift research include: improving scalability, robustness and reliability, moving from so called _black box_ adaptation to more interpretable and explainable adaptation, reducing the dependence on timely and accurate feedback (true labels) and moving from adaptive algorithms towards adaptive systems that would automate full knowledge discovery process in addition to automating adaptation of the decision models. Some of these challenges have been discussed in [Zliobaite et al. 2012b]. 

Studying how to integrate expert knowledge in concept drift handling and how to interact with domain experts brings new challenges as well. Relying on non interpretabe black-box models is not popular among the domain experts. They may need to trust that e.g. a control system is really going to react to changes when they happen and to understand how these changes are detected and what adaptation would happen. Furthermore, experts may have valuable knowledge how to improve the concept drift handling mechanism or to validate the system. The continuous or incremental learning nature of adaptive systems makes it challenging to come up with a strategy to incorporate expert knowledge into the adaptive learning process and to communicate with experts as the process evolves. 

Studying how to perform localization and explanation of changes, e.g. by means of visualization or a rule-based approach would be helpful in improving usability and trust in adaptive learning systems. 

### **REFERENCES** 

ADAE, I. AND BERTHOLD, M. 2013. Eve: a framework for event detection. _Evolving systems 4_ , 61–70. 

ADOMAVICIUS, G. AND TUZHILIN, A. 2005. Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. _IEEE Trans. Knowl. Data Eng. 17,_ 6, 734–749. 

AGGARWAL, C. 2005. On change diagnosis in evolving data streams. _IEEE Trans. on Knowl. and Data Eng. 17_ , 587–600. 

AGGARWAL, C. 2006. On biased reservoir sampling in the presence of stream evolution. In _Proc. of the 32nd int. conf. on Very large data bases_ . VLDB. 607–618. 

AGRAWAL, R., GHOSH, S. P., IMIELINSKI, T., IYER, B. R., AND SWAMI, A. N. 1992. An interval classifier for database mining applications. In _Proc. of the 18th int. conf. on Very Large Data Bases_ . VLDB. 560–573. AGRAWAL, R., IMIELINSKI, T., AND SWAMI, A. 1993. Database mining: A performance perspective. _IEEE Trans. on Knowl. and Data Eng. 5,_ 6, 914–925. 

AL-KATEB, M., BYUNG SUK, L., AND WANG, X. 2007. Adaptive-size reservoir sampling over data streams. In _Proc. of Int. Conf. on Scientific and Statistical Database Management_ . SSBDM. 22. 

ALBERG, D., LAST, M., AND KANDEL, A. 2012. Knowledge discovery in data streams with regression tree methods. _Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery 2_ , 69 – 78. ANG, H., GOPALKRISHNAN, V., M., I. Z., PECHENIZKIY, AND HOI, S. 2012. Predictive handling of asynchronous concept drifts in distributed environments. _IEEE Trans. on Knowl. and Data Eng._ . 

BABCOCK, B., BABU, S., DATAR, M., MOTWANI, R., AND WIDOM, J. 2002. Models and issues in data stream systems. In _Proc. of the 21st SIGMOD-SIGACT-SIGART symp. on Princi. of database syst._ PODS. 1–16. BACH, S. H. AND MALOOF, M. A. 2008. Paired learners for concept drift. In _Proc. of the 8th IEEE Int. Conf. on Data Mining_ . ICDM. 23–32. 

BACHE, K. AND LICHMAN, M. 2013. UCI machine learning repository. Tech. rep. 

BASSEVILLE, M. AND NIKIFOROV, I. 1993. _Detection of Abrupt Changes - Theory and Application_ . online. 

> 5 `http://www.processmining.org` 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:31 

BESSA, R. J., MIRANDA, V., AND GAMA, J. 2009. Entropy and correntropy against minimum square error in off-line and on-line 3-day ahead wind power forecasting. _IEEE Trans. on Power Syst. 24,_ 4, 1657–1666. BIFET, A. AND FRANK, E. 2010. Sentiment knowledge discovery in twitter streaming data. In _Proc. of the 13th int. conf. on Discovery science_ . DS. 1–15. 

BIFET, A. AND GAVALDA, R. 2006. Kalman filters and adaptive windows for learning in data streams. In _Proc. of the 9th int. conf. on Discovery science_ . DS. 29–40. 

BIFET, A. AND GAVALDA, R. 2007. Learning from time-changing data with adaptive windowing. In _Proc. of SIAM int. conf. on Data Mining_ . SDM. 443–448. 

BIFET, A., HOLMES, G., KIRKBY, R., AND PFAHRINGER, B. 2011a. DATA STREAM MINING: A practical approach. Technical report, University of Waikato. 

BIFET, A., HOLMES, G., AND PFAHRINGER, B. 2010a. Leveraging bagging for evolving data streams. In _Proc. of the Eur. conf. on Mach. learn. and knowledge discovery in databases_ . ECMLPKDD. 135–150. 

BIFET, A., HOLMES, G., PFAHRINGER, B., AND FRANK, E. 2010b. Fast perceptron decision tree learning from evolving data streams. In _Proc. of the 14th PA Conf. on Knowl. Discov. and Data Mining_ . 299–310. BIFET, A., HOLMES, G., PFAHRINGER, B., KIRKBY, R., AND GAVALDA, R. 2009. New ensemble methods for evolving data streams. In _Proc. of the int. conf. on Knowl. discov. and data mining_ . 139–148. 

BIFET, A., HOLMES, G., PFAHRINGER, B., READ, J., KRANEN, P., KREMER, H., JANSEN, T., AND SEIDL, T. 2011b. MOA: A real-time analytics open source framework. In _Proc. Eur. conf. on Mach. Learn. and Principles and Practice of Knowledge Discovery in Databases_ . ECMLPKDD. 617–620. 

BILLSUS, D. AND PAZZANI, M. J. 2000. User modeling for adaptive news access. _User Modeling and UserAdapted Interaction 10_ , 147–180. 

BLUM, A. 1997. Empirical support for winnow and weighted-majorityalgorithms: Results on a calendar scheduling domain. _Mach. Learn. 26,_ 1, 5–23. 

BOBADILLA, J., ORTEGA, F., HERNANDO, A., AND GUTIE<sup>´</sup> RREZ, A. 2013. Recommender systems survey. _Know.-Based Syst. 46_ , 109–132. 

BOSE, R. P. J. C., VAN DER AALST, W. M. P., ZLIOBAITE, I., AND PECHENIZKIY, M. 2013. Dealing with concept drift in process mining. _(accepted to) IEEE Trans. on Neur. Net. and Lear. Syst._ . 

BOUCHACHIA, A. 2011a. Fuzzy classification in dynamic environments. _Soft Comput. 15,_ 5, 1009–1022. 

BOUCHACHIA, A. 2011b. Incremental learning with multi-level adaptation. _Neurocomp. 74,_ 11, 1785–1799. BOUCHACHIA, A., PROSSEGGER, M., AND DUMAN, H. 2010. Semi-supervised incremental learning. In _In Proc. of the IEEE Int. Conf. on Fuzzy Systems_ . FUZZ-IEEE. 1–6. 

BREIMAN, L. 1999. Pasting small votes for classification in large databases and on-line. _Machine Learning 36_ , 85–103. 

BREIMAN, L. ET AL. 1984. _Classification and Regression Trees_ . Chapman & Hall, New York. 

BREMNES, J. 2004. Probabilistic wind power forecasts using local quantile regression. _Wind En. 7,_ 1, 47–54. CARMONA, J. AND GAVALDA<sup>`</sup> , R. Online techniques for dealing with concept drift in process mining. In _Advances in Intelligent Data Analysis XI - 11th Int. Symp._ 

CARMONA-CEJUDO, J., BAENA-GARCIA, M., DEL CAMPO-AVILA, J., BUENO, R., AND BIFET, A. 2010. GNUsmail: Open framework for on-line email classification. In _Proc. of the 19th Eur. conf. on Art. Intell._ ECAI. 1141–1142. 

CARPENTER, G., GROSSBERG, S., AND REYNOLDS, J. 1991a. ARTMAP: Supervised real-time learning and classification of nonstationary data by a self-organizing neural network. _Neural Networks 4_ , 565–588. CARPENTER, G., GROSSBERG, S., AND ROSEN, D. 1991b. Fuzzy ART: Fast stable learning and categorization of analog patterns by an adaptive resonance system. _Neural Networks 4,_ 6, 759–771. 

CARVALHO, V. AND COHEN, W. 2006. Single-pass online learning: performance, voting schemes and online feature selection. In _Proc. of the 12th ACM SIGKDD int. conf. on Kn. disc. and data min._ KDD. 548–553. CASTILLO, G., GAMA, J., AND BREDA, A. 2003. Adaptive bayes for a student modeling prediction task based on learning styles. In _Proc. of the 9th int. conf. on User modeling_ . UM. 328–332. 

CESA-BIANCHI, N. AND LUGOSI, G. 2006. _Prediction, learning, and games_ . Cambridge University Press. 

CHANDOLA, V., BANERJEE, A., AND KUMAR, V. 2009. Anomaly detection: A survey. _ACM Computer Surveys 41_ , 15:1–15:58. 

CHU, F. AND ZANIOLO, C. 2004. Fast and light boosting for adaptive mining of data streams. In _Proc. of the 5th Pac.-Asia conf. on Knowledge Discovery and Data Mining_ . PAKDD. 282–292. 

- DASU, T., KRISHNAN, S., VENKATASUBRAMANIAN, S., AND YI, K. 2006. An information-theoretic approach to detecting changes in multi-dimensional data streams. In _Proc. of the 38th Symp. on the Interface of Statistics, Computing Science, and Applications_ . 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

### 1:32 

DATAR, M., GIONIS, A., INDYK, P., AND MOTWANI, R. 2002. Maintaining stream statistics over sliding windows. _SIAM J. Comput. 31_ , 1794–1813. 

DELANY, S., CUNNINGHAM, P., TSYMBAL, A., AND COYLE, L. 2005. A case-based technique for tracking concept drift in spam filtering. _Knowledge-Based Systems 18,_ 4-5, 187–195. 

DEMSAR, J. 2006. Statistical comparisons of classifiers over multiple data sets. _J. Mach. Learn. Res. 7_ , 1–30. DOMINGOS, P. AND HULTEN, G. 2000. Mining high-speed data streams. In _Proc. of the 6th ACM SIGKDD int. conf. on Knowledge discovery and data mining_ . KDD. 71–80. 

DRIES, A. AND RUCKERT, U. 2009. Adaptive concept drift detection. _Stat. Anal. Data Min. 2,_ 5-6, 311–327. DUDA, R., HART, P., AND STORK, D. 2001. _Pattern Classification_ . Wiley. 

DUNNETT, C. W. 1955. A multiple comparison procedure for comparing several treatments with a control. _Journal of the American Statistical Association_ , 1096–1121. 

EFRAIMIDIS, P. AND SPIRAKIS, P. 2006. Weighted random sampling with a reservoir. _Inf. Proc. Lett. 97,_ 5, 181–185. 

ELWELL, R. AND POLIKAR, R. 2011. Incremental learning of concept drift in nonstationary environments. _IEEE Trans. on Neural Networks 22,_ 10, 1517–1531. 

FERN, A. AND GIVAN, R. 2003. Online ensemble learning: An empirical study. _Mach. Learn. 53,_ 1-2, 71–109. FORMAN, G. 2006. Tackling concept drift by temporal inductive transfer. In _Proc. of the 29th int. ACM SIGIR conf. on Research and development in inf. retrieval_ . SIGIR. 252–259. 

FRENCH, R. M. 1994. Catastrophic forgetting in connectionist networks: Causes, consequences and solutions. In _Trends in Cognitive Sciences_ . 128–135. 

GABER, M. M., ZASLAVSKY, A., AND KRISHNASWAMY, S. 2005. Mining data streams: a review. _SIGMOD Rec. 34_ , 18–26. 

GAMA, J. 2010. _Knowledge Discovery from Data Streams_ . Chapman & Hall/CRC. 

GAMA, J., FERNANDES, R., AND ROCHA, R. 2006. Decision trees for mining data streams. _Intelligent Data Analysis 10,_ 1, 23–46. 

GAMA, J. AND KOSINA, P. 2011. Learning about the learning process. In _Proc. of the 10th int. conf. on Advances in intelligent data analysis_ . IDA. Springer, 162–172. 

GAMA, J., MEDAS, P., CASTILLO, G., AND RODRIGUES, P. 2004. Learning with drift detection. In _Proc. of the 17th Brazilian symp. on Artif. Intell._ SBIA. 286–295. 

GAMA, J., SEBASTIAO<sup>˜</sup> , R., AND RODRIGUES, P. 2013. On evaluating stream learning algorithms. _Machine Learning 90,_ 3, 317–346. 

GANTZ, J. AND REINSEL, D. 2012. IDC: The digital universe in 2020: Big data, bigger digital shadows, and biggest growth in the far east. _International Data Corporation, sponsored by EMC Corporation_ . 

GAO, J., FAN, W., HAN, J., AND YU, P. S. 2007. A general framework for mining concept-drifting data streams with skewed distributions. In _Proc. of the 7th SIAM Int. Conf. on Data Mining_ . SDM. 

GEHRKE, J., RAMAKRISHNAN, R., AND GANTI, V. 1998. RainForest - a framework for fast decision tree construction of large datasets. In _Proc. of the 24rd Int. Conf. on Very Large Data Bases_ . VLDB. 416–427. GIRAUD-CARRIER, C. 2000. A note on the utility of incremental learning. _AI Commun. 13,_ 4, 215–223. GOMES, J. B., RUIZ, E. M., AND SOUSA, P. A. C. 2011. Learning recurring concepts from data streams with a context-aware ensemble. In _Proc. of the ACM symp. on Appl. Comp._ SAC. 994–999. 

GRISOGONO, A.-M. 2006. The implications of complex adaptive systems theory for C2. In _State of the Art State of the Practice_ . Vol. CCRTS. 

HALL, M., FRANK, E., HOLMES, G., PFAHRINGER, B., REUTEMANN, P., AND WITTEN, I. H. 2009. The WEKA data mining software: an update. _SIGKDD Explor. Newsl. 11,_ 1, 10–18. 

HARRIES, M. 1999. SPLICE-2 comparative evaluation: Electricity pricing. Tech. rep., South Wales Univ. HARRIES, M., SAMMUT, C., AND HORN, K. 1998. Extracting hidden context. _Machine Learning 32_ , 101–126. HELMBOLD, D. P. AND LONG, P. M. 1994. Tracking drifting concepts by minimizing disagreements. _Mach. Learn. 14,_ 1, 27–45. 

HERBSTER, M. AND WARMUTH, M. 1998. Tracking the best expert. _Machine Learning 32,_ 2, 151–178. 

HULTEN, G., SPENCER, L., AND DOMINGOS, P. 2001. Mining time-changing data streams. In _Proc. of the 7th ACM SIGKDD int. conf. on Knowledge Discovery and Data Mining_ . KDD. 97–106. 

IKONOMOVSKA, E., GAMA, J., AND DZEROSKI, S. 2011. Learning model trees from evolving data streams. _Data Mining Knowledge Discovery 23,_ 1, 128–168. 

JOACHIMS, T. 2000. Estimating the generalization performance of an svm efficiently. In _Proc. of the 17th Int. Conf. on Mach. Learn._ ICML. 431–438. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:33 

KADLEC, P., GRBIC, R., AND GABRYS, B. 2011. Review of adaptation mechanisms for data-driven soft sensors. _Computers & Chemical Engineering 35,_ 1, 1–24. 

KATAKIS, I., TSOUMAKAS, G., AND VLAHAVAS, I. 2010. Tracking recurring contexts using ensemble classifiers: an application to email filtering. _Knowledge and Information Systems 22,_ 3, 371–391. KELLY, M. G., HAND, D. J., AND ADAMS, N. M. 1999. The impact of changing populations on classifier performance. In _Proc. of the 5th ACM SIGKDD int. conf. on Knowl. disc. and dat. min._ KDD. 367–371. KIFER, D., BEN-DAVID, S., AND GEHRKE, J. 2004. Detecting change in data streams. In _Proc. of the 13th int. conf. on Very large data bases_ . VLDB. 180–191. 

KLINKENBERG, R. 2003. Predicting phases in business cycles under concept drift. In _Proc. of the Ann. Worksh. on Machine Learning of the National German Computer Science Society_ . LLWA. 3–10. 

- KLINKENBERG, R. 2004. Learning drifting concepts: Example selection vs. example weighting. _Intelligent Data Analysis 8,_ 3, 281–300. 

- KLINKENBERG, R. AND JOACHIMS, T. 2000. Detecting concept drift with support vector machines. In _Proc. of the 17th int. conf. on Machine Learning_ . ICML. 487–494. 

- KLINKENBERG, R. AND RENZ, I. 1998. Adaptive information filtering: Learning in the presence of concept drifts. In _Workshop Notes of the ICML/AAAI-98 Workshop on Learning for Text Categorization_ . 33–40. 

- KOLTER, J. AND MALOOF, M. 2003. Dynamic weighted majority: A new ensemble method for tracking concept drift. In _Proc. of the 3rd IEEE Int. Conf. on Data Mining_ . ICDM. 123–130. 

- KOLTER, J. AND MALOOF, M. 2005. Using additive expert ensembles to cope with concept drift. In _Proc. of the 22th int. conf. on Machine Learning_ . ICML. 449–456. 

- KOLTER, J. AND MALOOF, M. 2007. Dynamic weighted majority: An ensemble method for drifting concepts. _Journal of Machine Learning Research 8_ , 2755–2790. 

KOREN, Y. 2010. Collaborative filtering with temporal dynamics. _Commun. ACM 53,_ 4, 89–97. 

KOSINA, P., GAMA, J., AND SEBASTIAO, R. 2010. Drift severity metric. In _Proc. of the 19th Eur. Conf. on Artificial Intelligence_ . ECAI. 1119–1120. 

- KOYCHEV, I. 2000. Gradual forgetting for adaptation to concept drift. In _Proc. of ECAI Workshop on Current Issues in Spatio-Temporal Reasoning_ . 101–106. 

- KOYCHEV, I. 2002. Tracking changing user interests through prior-learning of context. In _Proc. of the 2nd int. conf. on Adaptive Hypermedia and Adaptive Web-Based Systems_ . 223–232. 

- KUKAR, M. 2003. Drifting concepts as hidden factors in clinical studies. In _Proc. of AIME 2003, 9th Conference on Artificial Intelligence in Medicine in Europe_ . 355–364. 

- KUNCHEVA, L. 2008. Classifier ensembles for detecting concept change in streaming data: Overview and perspectives. In _Proc. of the 2nd Workshop SUEMA 2008_ . 

- KUNCHEVA, L. AND ZLIOBAITE, I. 2009. On the window size for classification in changing environments. _Intelligent Data Analysis 13,_ 6, 861–872. 

- KUNCHEVA, L. I. 2004. Classifier ensembles for changing environments. In _Proc. of the 5th Int. Worksh. on Multiple Classifier Systems_ . MCS. 1–15. 

- KUNCHEVA, L. I. 2009. Using control charts for detecting concept change in streaming data. Tech. Rep. BCS-TR-001-2009, School of Computer Science, Bangor University, UK. 

- KUNCHEVA, L. I. 2013. Change detection in streaming multivariate data using likelihood detectors. _IEEE Transactions on Knowledge and Data Engineering 25_ . 

- KUNCHEVA, L. I. AND PLUMPTON, C. O. 2008. Adaptive learning rate for online linear discriminant classifiers. In _Proc. of Int. Worksh. on Structural and Syntactic Pattern Recognition_ . SSPR. 510–519. 

- LANQUILLON, C. 2002. Enhancing text classification to improve information filtering. _K¨unstliche Intelligenz, 16,_ 2, 37–38. 

- LAZARESCU, M. M., VENKATESH, S., AND BUI, H. H. 2004. Using multiple windows to track concept drift. _Intelligent Data Analysis 8,_ 1, 29–59. 

- LEEUWEN, M. AND SIEBES, A. 2008. Streamkrimp: Detecting change in data streams. In _Proc. of the Eur. Conf. on Mach. Learn. and Knowledge Discovery in Databases_ . ECMLPKDD. 672–687. 

- LINDSTROM, P., DELANY, S. J., AND NAMEE, B. M. 2010. Handling concept drift in a text data stream constrained by high labelling cost. In _Proc. of the 23rd Int. Florida Art. Intell. Research Society Conf._ 

- LITTLESTONE, N. 1987. Learning quickly when irrelevant attributes abound: A new linear-threshold algorithm. _Machine Learning 2,_ 4, 285–318. 

- LITTLESTONE, N. AND WARMUTH, M. 1994. The weighted majority algorithm. _Inf. Comput. 108,_ 2, 212–261. MALOOF, M. AND MICHALSKI, R. 2000. Selecting examples for partial memory learning. _Machine Learning 41_ , 27–52. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

### 1:34 

J. Gama et al. 

MALOOF, M. AND MICHALSKI, R. 2004. Incremental learning with partial instance memory. _Artificial Intelligence 154_ , 95–126. 

- MALOOF, M. A. 2010. The AQ methods for concept drift. In _Advances in Machine Learning I: Dedicated to the Memory of Professor Ryszard S. Michalski_ . 23–47. 

- MALOOF, M. A. AND MICHALSKI, R. S. 1995. A method for partial-memory incremental learning and its application to computer intrusion detection. In _In Proc. of the 7th IEEE Int. Conf. on Tools with Artif. Intell._ 392–397. 

- MARKOU, M. AND SINGH, S. 2003. Novelty detection: a review - part 1: statistical approaches. _Signal Processing 83_ , 2481–2497. 

- MASUD, M., GAO, J., KHAN, L., HAN, J., AND THURAISINGHAM, B. 2011. Classification and novel class detection in concept-drifting data streams under time constraints. _IEEE TKDE 23,_ 6, 859–874. 

- MCNEMAR, Q. 1947. Note on the sampling error of the difference between correlated proportions or percentages. _Psychometrika 12,_ 2, 153–157. 

- MEHTA, M., AGRAWAL, R., AND RISSANEN, J. 1996. SLIQ: A fast scalable classifier for data mining. In _Proc. of the 5th Int. Conf. on Extending Database Technol.: Advances in Database Technol._ EDBT. 18–32. 

- MINKU, L., WHITE, A., AND YAO, X. 2010. The impact of diversity on online ensemble learning in the presence of concept drift. _IEEE Transactions on Knowledge and Data Engineering 22_ , 730–742. 

- MINKU, L. AND YAO, X. 2011. DDD: A new ensemble approach for dealing with concept drift. _IEEE Transactions on Knowledge and Data Engineering 24,_ 4, 619– 633. 

- MONTEIRO, C., BESSA, R., MIRANDA, V., BOTTERUD, A., WANG, J., AND CONZELMANN, G. 2009. Wind power forecasting: State-of-the-art 2009. Tech. Rep. ANL/DIS-10-1, Argonne National Laboratory. 

- MORENO-TORRES, J. G., RAEDER, T., ALAIZ-RODRIGUEZ, R., CHAWLA, N. V., AND HERRERA, F. 2012. A unifying view on dataset shift in classification. _Pattern Recognition 45,_ 1, 521 – 530. 

- MOUSS, H., MOUSS, D., MOUSS, N., AND SEFOUHI, L. 2004. Test of Page-Hinkley, an approach for fault detection in an agro-alimentary production system. In _Proc. of the Asian Control Conference_ . 815–818. 

- MUTHUKRISHNAN, S., VAN DEN BERG, E., AND WU, Y. 2007. Sequential change detection on data streams. In _Workshop Proc. of the 7th IEEE Int. Conf. on Data Mining_ . ICDMW. 551–550. 

- NG, W. AND DASH, M. 2008. A test paradigm for detecting changes in transactional data streams. In _Proc. of the 13th int. conf. on Database systems for advanced applications_ . DASFAA. 204–219. 

- NISHIDA, K. AND YAMAUCHI, K. 2007. Detecting concept drift using statistical testing. In _Proceedings of the 10th international conference on Discovery science_ . DS’07. Springer-Verlag, Berlin, Heidelberg, 264–269. 

- OZA, N. 2001. Online ensemble learning. Ph.D. thesis, University of California Berkeley. 

- PAGE, E. S. 1954. Continuous inspection schemes. _Biometrika 41,_ 1/2, 100–115. 

- PECHENIZKIY, M., BAKKER, J., ZLIOBAITE, I., IVANNIKOV, A., AND K ARKK<sup>¨</sup> AINEN<sup>¨</sup> , T. 2009. Online mass flow prediction in CFB boilers with explicit detection of sudden concept drift. _SIGKDD Explor. 11,_ 2, 109–116. 

- POLIKAR, R., UDPA, L., UDPA, S., MEMBER, S., MEMBER, S., AND HONAVAR, V. 2001. Learn++: An incremental learning algorithm for supervised neural networks. _IEEE Tr. on Sys., Man and Cyber.C 31_ , 497–508. 

- ROSENBLATT, F. 1958. The perceptron: A probabilistic model for information storage and organization in the brain. _Psychological Review 65,_ 6, 386–408. 

- ROSS, G. J., ADAMS, N. M., TASOULIS, D. K., AND HAND, D. J. 2012. Exponentially weighted moving average charts for detecting concept drift. _Pattern Recogn. Lett. 33_ , 191–198. 

- RUSU, F. AND DOBRA, A. 2009. Sketching sampled data streams. In _Proc. of the 2009 IEEE Int. Conf. on Data Eng._ ICDE. 381–392. 

- SALGANICOFF, M. 1993. Density-adaptive learning and forgetting. In _Proc. of the Int. Conf. on Mach. Learn._ ICML. 276–283. 

- SALGANICOFF, M. 1997. Tolerating concept and sampling shift in lazy learning using prediction error context switching. _Artificial Intelligence Review 11,_ 1-5, 133–155. 

- SCHLIMMER, J. AND GRANGER, R. 1986. Incremental learning from noisy data. _Mach. Learn. 1,_ 3, 317–354. SCHOLZ, M. AND KLINKENBERG, R. 2007. Boosting classifiers for drifting concepts. _Intell. Data Ana. 11,_ 1, 3–28. 

- SEBASTIAO<sup>˜</sup> , R. AND GAMA, J. 2007. Change detection in learning histograms from data streams. In _Progress in Artificial Intelligence: Proc. of the Portuguese Conf. on Art. Intell._ 112–123. 

- SHAFER, J. C., AGRAWAL, R., AND MEHTA, M. 1996. SPRINT: A scalable parallel classifier for data mining. In _Proc. of the 22th Int. Conf. on Very Large Data Bases_ . VLDB. 544–555. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

1:35 

SHIRYAEV, A. 2009. On stochastic models and optimal methods in the quickest detection problems. _Theory Probab. Appl. 53,_ 3, 385–401. 

STREET, W. AND KIM, Y. 2001. A streaming ensemble algorithm SEA for large-scale classification. In _Proc. 7th ACM SIGKDD Int. Conf. on Knowledge Discovery and Data Mining_ . KDD. 377–382. 

SYED, N., LIU, H., AND SUNG, K. 1999. Handling concept drifts in incremental learning with support vector machines. In _Proc. of the 5th ACM SIGKDD int. conf. on Knowl. disc. and data mining_ . KDD. 317–321. TARTAKOVSKY, A. AND MOUSTAKIDES, G. 2010. State-of-the-art in bayesian changepoint detection. _Sequential Analysis 29_ , 125–145. 

THRUN, S., M. MONTEMERLO, H. DAHLKAMP, D. STAVENS, A. ARON, J. DIEBEL, P. FONG, J. GALE, M. HALPENNY, G. HOFFMANN, K. LAU, C. OAKLEY, M. PALATUCCI, V. PRATT, P. STANG, S. STROHBAND, C. DUPONT, L. JENDROSSEK, ET AL. 2006. Stanley: the robot that won the darpa challenge. _J. Field Robot. 23,_ 9, 661–692. 

TSYMBAL, A. 2004. The problem of concept drift: Definitions and related work. Technical report, Department of Computer Science, Trinity College: Dublin. 

TSYMBAL, A., PECHENIZKIY, M., CUNNINGHAM, P., AND PUURONEN, S. 2006. Handling local concept drift with dynamic integration of classifiers: Domain of antibiotic resistance in nosocomial infections. In _Proc. of 19th IEEE int. symp. on Computer-Based Medical Syst._ CBMS. 679–684. 

VAN DER AALST, W. M. P. 2011. _Process Mining - Discovery, Conformance and Enhancement of Business Processes_ . Springer. 

VAN DER AALST, W. M. P. 2012. Process mining. _Commun. ACM 55,_ 8, 76–83. 

VITTER, J. 1985. Random sampling with a reservoir. _ACM Trans. Math. Softw. 11,_ 1, 37–57. 

VORBURGER, P. AND BERNSTEIN, A. 2006. Entropy-based concept shift detection. In _Proc. of the 6th Int. Conf. on Data Mining_ . ICDM. 1113–1118. 

VOVK, V. 1998. A game of prediction with expert advice. _J. Comput. Syst. Sci. 56,_ 2, 153–173. 

WALD, A. 1947. _Sequential Analysis_ . John Wiley and Sons, Inc. 

WANG, H., FAN, W., YU, P., AND HAN, J. 2003. Mining concept-drifting data streams using ensemble classifiers. In _Proc. of the 9th ACM SIGKDD int. conf. on Knowl. disc. and data mining_ . KDD. 226–235. 

WIDMER, G. 1997. Tracking context changes through meta-learning. _Mach. Learn. 27,_ 3, 259–286. 

WIDMER, G. AND KUBAT, M. 1993. Effective learning in dynamic environments by explicit context tracking. In _Proc. of the Eur. Conf. on Mach. Learn._ ECML. 227–243. 

WIDMER, G. AND KUBAT, M. 1996. Learning in the presence of concept drift and hidden contexts. _Mach. Learn. 23,_ 1, 69–101. 

YANG, Y., WU, X., AND ZHU, X. 2006. Mining in anticipation for concept change: Proactive-reactive prediction in data streams. _Data Mining and Knowledge Discovery 13,_ 3, 261–289. 

YAO, R., SHI, Q., SHEN, C., ZHANG, Y., AND VAN DEN HENGEL, A. 2012. Robust tracking with weighted online structured learning. In _Proc. of the 12th Eur. Conf. on Computer Vision_ . ECCV. 158–172. 

ZEIRA, G., MAIMON, O., LAST, M., AND ROKACH, L. 2004. Change detection in classification models induced from time-series data. In _Data Mining in Time Series Databases_ . Vol. 57. 101–125. 

ZHANG, P., ZHU, X., AND SHI, Y. 2008. Categorizing and mining concept drifting data streams. In _Proc. of the 14th ACM SIGKDD int. conf. on Knowl. disc. and data mining_ . KDD. 812–820. 

ZHANG, Z. AND ZHOU, J. 2010. Transfer estimation of evolving class priors in data stream classification. _Pattern Recogn. 43,_ 9, 3151–3161. 

ZHAO, P., HOI, S., JIN, R., AND YANG, T. 2011. Online AUC maximization. In _Proc. of the 28th Int. Conf. on Machine Learning_ . ICML. 233–240. 

ZLIOBAITE, I. 2009. Learning under concept drift: an overview. Technical report, Vilnius University. 

- ZLIOBAITE, I. 2011a. Combining similarity in time and space for training set formation under concept drift. _Intelligent Data Analysis 15,_ 4, 589–611. 

- ZLIOBAITE, I. 2011b. Controlled permutations for testing adaptive classifiers. In _Proc. of the 14th Int. Conf. on Discovery Science_ . DS. 365–379. 

- ZLIOBAITE, I., BAKKER, J., AND PECHENIZKIY, M. 2012a. Beating the baseline prediction in food sales: How intelligent an intelligent predictor is? _Expert Syst. Appl. 39,_ 1, 806–815. 

- ZLIOBAITE, I., BIFET, A., GABER, M. M., GABRYS, B., GAMA, J., MINKU, L. L., AND MUSIAL, K. 2012b. Next challenges for adaptive learning systems. _SIGKDD Explorations 14,_ 1, 48–55. 

- ZLIOBAITE, I., BIFET, A., PFAHRINGER, B., AND HOLMES, G. 2013. Active learning with drifting streaming data. _IEEE Trans. on Neural Networks and Learning Systems_ . 

- ZLIOBAITE, I. AND KUNCHEVA, L. 2009. Determining the training window for small sample size classification with concept drift. In _Proc. of IEEE Int. Conf. on Data Mining Workshops_ . ICDMW. 447–452. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

# **Online Appendix to: A Survey on Concept Drift Adaptation** 

JO AO GAMA<sup>˜</sup> , University of Porto, Portugal INDR E<sup>˙</sup> ZLIOBAIT<sup>ˇ</sup> E<sup>˙</sup> , Aalto University, Finland ALBERT BIFET, Yahoo! Research Barcelona, Spain MYKOLA PECHENIZKIY, Eindhoven University of Technology, the Netherlands ABDELHAMID BOUCHACHIA, Bournemouth University, UK 

### **A. PSEUDOCODE OF CONCEPT DRIFT ALGORITHMS** 

|**ALGORITHM 1:** Page-Hinkley Algorithm|
|---|
|**input**: Admissible change_δ_, Drift threshold_λ_, Loss at example_t_:_et_ ;<br>**output**: _drift ∈{TRUE, FALSE}_;<br>/* Initialize the error estimators */ ;<br>_SR_(0)_←_0;_mT_(0)_←_0;_MT ←_1;<br>/* Page Hinkley test */ ;<br>Let_SR_(_t_)_←SR_(_t −_1) +_R_(_t_);<br>Let_mT_(_t_)_←mT_(_t −_1) +_R_(_t_)_−_<sup>_SR_(</sup><sup>_t_)</sup><br>_t_<br>_−δ_ ;<br>Let_MT ←min_(_MT , mT_(_t_));<br>**if**_mT_(_t_)_−MT ≥λ_**then**<br>_drift ←TRUE_ ;<br>**else**<br>_drift ←FALSE_ ;<br>**end**|
|**ALGORITHM 2:** The`ADWIN` change detection algorithm<br>**begin**<br>Initialize Window_W_;<br>**foreach** (_t_)_>_0**do**<br>_W ←W ∪{xt}_(i.e., add_xt_ to the head of_W_);<br>**repeat**<br>Drop elements from_W_<br>**until**_|_ˆ_µW_0 _−_ˆ_µW_1_| < ϵcut holds for every split of W into W_ =_W_0_∪W_1;<br>**end**<br>Output ˆ_µW_<br>**end**|



_⃝_ c 2013 ACM 0360-0300/2013/01-ART1 $10.00 DOI 10.1145/0000000.0000000 http://doi.acm.org/10.1145/0000000.0000000 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

App–2 

### **ALGORITHM 3:** The `SPC` change detection algorithm 

**input** : Current decision model _L_ ; _X, y_<sup>_T_</sup> : Training Set with class _y ∈ Y_ ; _α_ and _β_ parameters **begin** Let _Xt, yt_ be the current instance and _y_ ˆ _t ←L_ ( _Xt_ ) be the prediction; Let _errort ← E_ (ˆ _yt, yt_ ), compute mean _pt_ and variance _σt_ of with _errort_ ; **if** _pt_ + _σt < pmin_ + _σmin_ **then** _pmin ← pt_ and _σmin ← st_ ; **end if** _pt_ + _σt < pmin_ + _β × σmin_ **then** `In-control` : Warning? _← False_ ; update _L_ with the instance _Xt, yt_ ; **else if** _pt_ + _σt < pmin_ + _α × σmin_ **then if** _NOT Warning_ **then** `Warning` : Warning? _← True_ ; start buffer _←{Xt, yt}_ ; **else** `Warning` : buffer _←_ buffer _∪{Xj, yj}_ ; **end else** `Out-control` : train a new decision model using the instances in the buffer; Warning? _← False_ ; re-start _pmin_ and _σmin_ ; **end end end** 

### **ALGORITHM 5:** Algorithm for Dynamic Weighted Majority (DWM) 

**Input** : _{_<sup>_−→_</sup> _x , y}_<sup>1</sup> _n_<sup>: training data, feature vector and class label;</sup><sup>_c ∈_N</sup><sup>_∗_: number of classes</sup><sup>_c ≥_2;</sup><sup>_β_:</sup> factor for decreasing weights, 0 _≤ β <_ 1; _θ_ : threshold for deleting experts; _p_ : period between expert removal, creation, and weight update; _{e, w}_<sup>1</sup> _m_<sup>: set of experts and their weights;</sup> Λ _, λ ∈{_ 1 _, ..., c}_ : global and local predictions;<sup>_−→_</sup> _σ ∈_ R<sup>_c_</sup> : sum of weighted predictions for each class. **begin** _m ←_ 1 _em ←_ Create-New-Expert() _wm ←_ 1 **foreach** _i ←_ 1 _, ..., n_ **do** _−→σ ←_ 0 **foreach** _i ←_ 1 _, ..., m_ **do** _λ ←_ Classify( _ej,_<sup>_−→_</sup> _xi_ ) **if** _λ̸_ = _yi ∧ i_ mod _p_ = 0 **then** _wj ← βwj_ **end** _σλ ← σλ_ + _wj_ **end** _Λ ← argmaxjσj_ **if** _i_ mod _p_ = 0 **then** _w ←_ Normalize-Weights (w) _{e, w } ←_ Remove-Experts ( _{e, w}, θ_ ) **if** Λ _̸_ = _yi_ **then** _m ← m_ + 1 _em ←_ Create-New-Expert() _wm ←_ 1 **end end foreach** _j ←_ 1 _, ..., m_ **do** _ej ←_ Train( _ej,_<sup>_−→_</sup> _xi , yi_ ) ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. **end return** Λ **end end** 

A Survey on Concept Drift Adaptation 

App–3 

|**ALGORITHM 4:** The CVFDT algorithm|
|---|
|**intput**: _S_<br>is a sequence of examples,<br>_X_<br>is a set of symbolic attributes,<br>_G_(_._)is a split evaluation function,<br>_δ_<br>is one minus the desired probability of<br>choosing the correct attribute at any given node,<br>_τ_<br>is a user-supplied tie threshold,<br>_w_<br>is the size of the window,|
|_nmin_ is the # examples between checks for growth,<br>_f_<br>is the # examples between checks for drift.|
|**output**: _HT_ is a decision tree.|
|**Procedure**<br>**CVFDT(**_S, X, G, δ, τ, w, nmin_**)**<br>/* Initialize */|
|Let_HT_ be a tree with a single leaf_l_1 (the root).|
|Let_ALT_(_l_1)be an initially empty set of alternate tree for_l_1.|
|Let_W_ be the window of examples, initially empty.<br>Inicialize sufficient statistics to compute_G_.|
|i<br>/* Process the examples */|
|**foreach**_example (x, y) in S_ **do**|
|Sort (_x, y_) into a set of leaves_L_using_HT_ and all trees in_ALT_ of any node (_x, y_) passes<br>through.|
|Let_ID_ be the maximum id of the leaves in_L_.<br>Add ((_x, y_),_ID_) to the beginning of_W_.<br>|
|**if**_|W| > w_ **then**|
|<br>Let ((_xw, yw_),_IDw_) be the last element of_W_<br>ForgetExamples(_HT, n,_(_xw, yw_)_, IDw_)<br>Let_W_ =_W_ with ((_xw, yw_),_IDw_) removed<br>**end**|
|CVFDTGrow(_HT, n, G,_(_x, y_)_, δ, nmin, τ_)|
|<br>**if**_there have been f examples since the last checking of alternate trees_**then**<br>CheckSplitValidity(_HT, n, δ_)<br>**end**|
|**end**|
|**return**_HT_.|



### **B. DATASETS FOR CONCEPT DRIFT** 

### **B.1. Synthetic** 

Synthetic data has several benefits: they are easy to reproduce and bear little cost of storage and transmission. Seven popular changing data generators are summarized in Table VI and described below. Synthetic data provides an advantage of knowing the ground truth (e.g. where exactly concept drift happens, what is the drift, what are classification accuracies achievable on each concept). The main limitation of synthetic data is uncertainty weather corresponding drifts happen in reality. 

- _SEA Concepts Generator._ This data model due to [Street and Kim 2001] presents abrupt concept drifts (real). The data contains three independent real valued attributes in [0 _,_ 10], only the first two attributes are relevant for prediction. The original data model produces four different concepts. The class decision boundary is defined as _x_ 1 + _x_ 2 _≤ θ_ , where _x_ 1 and _x_ 2 are the first two attributes and _θ_ is a threshold value different for each concept: (1) _θ_ = 9, (2) _θ_ = 8, (3) _θ_ = 7 and (4) _θ_ = 9 _._ 5. 

- _STAGGER Concepts Generator._ This data model due to [ **?** ] presents abrupt concept drifts (real). The data contains three independent categorical attributes: size _∈_ small, medium, large, color _∈_ red, green, blue and shape _∈_ square, circular, trian- 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

App–4 

### **ALGORITHM 6:** The `AddExp` algorithm for discrete classes 

**input** : _X, y_<sup>_T_</sup> A Training Set with class _y ∈ Y β ∈_ [0 _,_ 1]: factor for decreasing weights; _τ ∈_ [0 _,_ 1]: loss required to add a new expert **begin** Set the initial number of experts: _N_ 1 _←−_ 1; Set the initial expert weight: _w_ 1 _,_ 1 _←−_ 1; **for** _t ←_ 1 **to** _T_ **do** Get expert predictions: _ϵt,_ 1 _, . . . , ϵt,Nt ∈ Y_ ; Compute prediction: _y_ ˆ _t_ = _argmaxc∈Y_ � _Ni_ =1 _t_<sup>_wt,i_[</sup><sup>_c_=</sup><sup>_ϵt,i_];</sup> Update experts weights: _wt_ +1 _,i ←− wt,iβ_<sup>[</sup><sup>_yt̸_=</sup><sup>_ϵt,i_]</sup> ; **if** _y_ ˆ _t̸_ = _yt_ **then** Add a New Expert; _Nt_ +1 _←− Nt_ + 1; _wt_ +1 _,Nt_ +1 _←− γ_<sup>�</sup> _i_<sup>_N_</sup> =1<sup>_twt,i_;</sup> **end** Train each expert on instance _Xt, yt_ ; **end end** 

**ALGORITHM 7:** The `AddExp` algorithm for continuous classes **input** : _X, y_<sup>_T_</sup> A Training Set with class _y ∈_ [0 : 1]; _β ∈_ [0 _,_ 1]: factor for decreasing weights _γ ∈_ [0 _,_ 1]: factor for new expert weight; _τ ∈_ [0 _,_ 1]: loss required to add a new expert **begin** Set the initial number of experts: _N_ 1 _←−_ 1; Set the initial expert weight: _w_ 1 _,_ 1 _←−_ 1; **for** _t ←_ 1 **to** _T_ **do** Get expert predictions: _ϵt,_ 1 _, . . . , ϵt,Nt ∈_ [0 _,_ 1]; <u>�</u> _Nti_ <u>=1</u><sup>_wt,iϵt,i_</sup> Compute prediction: _y_ ˆ _t_ = ; <u>�</u> _Nti_ =1<sup>_wt,i_</sup> Suffer loss _∥y_ ˆ _t − yt∥_ ; Update experts weights: _wt_ +1 _,i ←− wt,iβ_<sup>_∥ϵt,i−yt∥_</sup> ; **if** _∥y_ ˆ _t − yt∥≥ τ_ **then** Add a New Expert; _Nt_ +1 _←− Nt_ + 1; _wt_ +1 _,Nt_ +1 _←− γ_<sup>�</sup> _i_<sup>_N_</sup> =1<sup>_twt,i∥ϵt,i −yt∥_;</sup> **end** Train each expert on instance _Xt, yt_ ; **end end** 

#### Table VI. Models for synthetic data generation 

|Name<br>#|of concepts|Task||Type of|drift||
|---|---|---|---|---|---|---|
||||real CD|virtual CD|priors|novelties|
|SEA|4|classification (2)|✓|–|✓|–|
|STAGGER|3|classification (2)|✓|–|✓|–|
|Rotating hyperplane|any|classification (2)|✓|–|–|–|
|RBF generator|any|classification (any)|✓|✓|✓|–|
|Function Generator|10|classification (2)|✓|–|✓|–|
|LED Generator|–|classification (10)|–|✓|–|–|
|Waveform Generator|–|classification(3)|–|✓|–|–|



ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

App–5 

gular. A binary classification task is defined by a disjunct of conjuncts. There are three concepts: (1) positive class _if_ size = small _and_ color = red, (2) color = green _or_ shape = circular, (3) size = medium _or_ size = large. 

- _Rotating Hyperplane._ This data model was first used to test CVFDT against VFDT in [Hulten et al. 2001]. Data is generated uniformly from a hyperplane _d_ - dimensional space. The decision boundary is defined as<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_wixi_=</sup><sup>_w_0=�</sup><sup>_d_</sup> _i_ =1<sup>_wi_,</sup> where where _xi_ , is the _i_<sup>_th_</sup> attribute. Examples for which<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_wixi≥w_0arela-</sup> beled positive, and examples for which<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_wixi<w_0arelabelednegative.Con-</sup> cept changes are introduced by modifying the weights _wi_ (they need to satisfy the constraint _w_ 0 =<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_wi_to keep the priors fixed). Hyperplanes are useful for simu-</sup> lating time-changing concepts, because we can change the orientation and position of the hyperplane in a smooth manner by changing the relative size of the weights. Noise can be added by randomly swapping class labels. 

- _Random RBF Generator._ This generator was devised to offer an alternate complex concept type that is not straightforward to approximate with a decision tree model. The RBF (Radial Basis Function) [Bifet et al. 2009] generator works as follows. A fixed number of random centroids are generated. Each center has a random position, a single standard deviation, class label and weight. New examples are generated by selecting a center at random, taking weights into consideration so that centers with higher weight are more likely to be chosen. A random direction is chosen to offset the attribute values from the central point. The length of the displacement is randomly drawn from a Gaussian distribution with standard deviation determined by the chosen centroid. The chosen centroid also determines the class label of the example. This effectively creates a normally distributed hypersphere of examples surrounding each central point with varying densities. Only numeric attributes are generated. Drift is introduced by moving the centroids with constant speed. 

- _Function Generator._ It originates from [Agrawal et al. 1992], and was a popular data model for early work on scaling up decision tree learners [Agrawal et al. 1993; Mehta et al. 1996; Shafer et al. 1996; Gehrke et al. 1998]. The generator produces a stream containing nine attributes, six numeric and three categorical. Although not explicitly stated by the authors, a sensible conclusion is that these attributes describe hypothetical loan applications. There are ten functions defined for generating binary class labels from the attributes, presumably meaning approval os the loan. The original data model has no drift. Concept drift may be introduced by switching between functions to generate class labels. 

- _LED Generator._ This data source originates from the CART book [Breiman et al. 1984] and an implementation in C is available from the UCI repository [Bache and Lichman 2013]. The goal is to predict the digit displayed on a seven-segment LED display, where each attribute has a 10% chance of being inverted. The optimal Bayes classification accuracy is 74%. The original data model has no drift. Drift may be introduced by swapping the positions of attributes. 

- _Waveform Generator._ It shares its origins with LED, and is available from the UCI repository. The goal of the task is to distinguish three classes of a waveform, each of which is generated from a combination of two or three base waves. The optimal Bayes classification accuracy is 86%. There are two versions of the problem, wave21 which has 21 numeric attributes, all of which include noise, and wave40 which introduces an additional 19 irrelevant attributes. The original data model has no drift. Drift may be introduced by swapping the positions of attributes. 

## Implementations of these data models are available in MOA [Bifet et al. 2011b]. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

App–6 

### **B.2. Real-World Data** 

Nowadays, it is easier than in the past, to find large real-world datasets for public benchmarking with concept change. The UCI machine learning repository [Bache and Lichman 2013] contains some real-world benchmark data for evaluating machine learning techniques, however they are not large datasets. 

The main real data domains of the large datasets mentioned in the _Concept Drift_ page of Wikipedia<sup>6</sup> are the following ones. 

- _Text mining._ Documents of text that contains words or combinations of words as the features to use to process the data. A collection of text mining datasets with concept drift is maintained by I. Katakis<sup>7</sup> . Data recollected from Twitter may be also be considered for text mining. 

- _Electricity._ A widely used dataset is the Electricity Market Dataset introduced in [Harries 1999]. This time series based data was collected from the Australian New South Wales Electricity Market, available from J. Gama<sup>8</sup> . In this market, the prices are not fixed and are affected by demand and supply of the market. The prices in this market are set every five minutes. The _ELEC2_ dataset contains 45 _,_ 312 instances. Each example of the dataset refers to a period of 30 minutes, i.e. there are 48 instances for each time period of one day. The class label identifies the change of the price related to a moving average of the last 24 hours. The class level only reflect deviations of the price on a one day average and removes the impact of longer term price trends. 

- _Email Spam._ Datasets of email messages used to predict if they are unsolicited messages or not. For example, _ECUE Spam_ datasets are two datasets each consisting of more than 10,000 emails collected over a period of approximately 2 years referring to a one user compiled by S.J.Delany<sup>9</sup> . 

- _Business oriented._ Datasets that contains data used in decision management systems in companies. _PAKDD’09 competition_ dataset<sup>10</sup> is used for a credit evaluation task. It is collected over a five year period, unfortunately the true labels are released only for the first part of the data. Another dataset called _Airline_ , contains approximately 116 million flight arrival and departure records (cleaned and sorted) and it is compiled by E. Ikonomovska<sup>11</sup> . 

- _Games._ Datasets obtained from online or non-online games: for example, a dataset _Chess.com_ (online games) compiled by I.Zliobait˙e<sup>ˇ12</sup> . 

### **C. EVALUATION EXAMPLE** 

We give an example on evaluation of data stream classification, using the MOA software framework [Bifet et al. 2011b]. MOA is an open-source framework for dealing with massive evolving data streams. MOA is related to WEKA [Hall et al. 2009], the Waikato Environment for Knowledge Analysis, which is an award-winning opensource workbench containing implementations of a wide range of batch machine learning methods. 

> 6 `http://en.wikipedia.org/wiki/Concept_drift` retrieved 12/11/2012 

> 7 `http://mlkd.csd.auth.gr/concept_drift.html` 

> 8 `http://www.liaad.up.pt/kdus/products/datasets-for-concept-drift` 

> 9 `http://www.comp.dit.ie/aigroup/?page_id=729` 

> 10 `http://sede.neurotech.com.br:443/PAKDD2009/arquivo.do?method=load` 

> 11 `http://kt.ijs.si/elena_ikonomovska/data.html` 

> 12 `https://sites.google.com/site/zliobaite/resources-1` 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

App–7 

MOA enables evaluation of data stream classification algorithms on large streams, in the order of tens of millions of instances under explicit memory limits. Any less than this does not actually test data stream algorithms in a realistically challenging setting. 

MOA is written in Java. The main benefits of Java are portability, where applications can be run on any platform with an appropriate Java virtual machine, and the strong and well-developed support libraries. Use of the language is widespread, and features such as automatic garbage collection help to reduce programmer burden and error. 

MOA contains stream generators, classifiers and evaluation methods. Figure 10 shows the MOA graphical user interface. A command line interface is also available. 





Fig. 10. MOA Graphical User Interface 

Considering data streams as data generated from pure distributions, MOA models a concept drift as a weighted combination of two pure distributions that characterizes the target concepts before and after the drift. Within the framework, it is possible to define the probability that instances of the stream belong to the new concept after the drift using the sigmoid function, as an elegant and practical solution [Bifet et al. 2009]. 

MOA contains the popular data generators described in Appendix B. MOA streams can be built using generators, reading ARFF files, joining several streams, or filtering streams. They allow for the simulation of a potentially infinite sequence of data. The following generators are currently available: Random Tree Generator, SEA Concepts Generator, STAGGER Concepts Generator, Rotating Hyperplane, Random RBF Generator, LED Generator, Waveform Generator, and Function Generator. 

MOA contains several classifier methods such as: Naive Bayes, Decision Stump, Hoeffding Tree, Hoeffding Option Tree, Adaptive Hoeffding Tree, Bagging, Boosting, Bagging using `ADWIN` [Bifet et al. 2009], and Leveraging Bagging [Bifet et al. 2010a]. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

J. Gama et al. 

App–8 



Fig. 11. Evaluation for a stream of a million of instances comparing hold-out, prequential with landmark window and prequential with sliding window. 

Figure 11 shows a comparison between a hold-out evaluation, a prequential evaluation using a landmark window ( _InterleavedTestThenTrain_ ), and a prequential evaluation using a sliding window of size 1000. We observe that the prequential evaluation using a sliding window is a good approximation to the hold-out evaluation. 

We run also on MOA the following experiment simulating a concept drift scenario: a prequential evaluation using a sliding window of size 1000 for a stream of a million of instances generated by the Random RBF Generator, with the following learners: Hoeffding Tree, Adaptive Hoeffding Tree, and `ADWIN` Bagging and Leveraging Bagging. The stream is evolving and the centroids are moving with constant speed 10<sup>_−_4</sup> : this speed is defined as the distance moved each new instance arrives and it is initialized by a drift parameter. 

Figure 12 shows accuracy, Kappa statistic and RAM-Hours for this experiment. We observe that the Hoeffding Tree is the method with lower capacity of adaption. Ensemble methods perform better than single classifiers, but they have a higher cost in RAM-Hours. Leveraging Bagging is the method with higher accuracy and Kappa statistic, but the number of resources that it needs is considerably larger. Data stream evaluation is a two-dimensional process with a trade-off between accuracy results and resource costs. 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

A Survey on Concept Drift Adaptation 

App–9 







Fig. 12. Prequential Evaluation for a RBF stream of a million of instances where the centers are moving with a speed of 10<sup>_−_4</sup> . 

ACM Computing Surveys, Vol. 1, No. 1, Article 1, Publication date: January 2013. 

