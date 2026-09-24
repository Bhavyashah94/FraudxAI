---
title: "FRAUD-RLA: Reinforcement Learning Attacks on Fraud Detection Systems"
authors: "unknown"
year: 2025
arxiv_id: "2502.02290"
original_file: "2502.02290.pdf"
pdf_path: "docs/papers\2025_unknown_fraudrla_reinforcement_learning_att.pdf"
---

# FRAUD-RLA: Reinforcement Learning Attacks on Fraud Detection Systems

**Authors:** Unknown et al.  
**Year:** 2025 | **arXiv:** [`2502.02290`](https://arxiv.org/abs/2502.02290)  
**Local PDF:** [`2025_unknown_fraudrla_reinforcement_learning_att.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2025_unknown_fraudrla_reinforcement_learning_att.pdf)

---

# **FRAUD-RLA: A new reinforcement learning adversarial attack against credit card fraud detection** 

Daniele Lunghi<sup>1,2,3</sup> , Yannick Molinghen<sup>1</sup> , Alkis Simitsis<sup>2</sup> , Tom Lenaerts<sup>1,4,5</sup> , and Gianluca Bontempi<sup>1</sup> 

> 1 _Université Libre de Bruxelles_ 

> 2 _Athena Research Center_ 

> 3 _National and Kapodistrian University of Athens_ 

> 4 _Vrije Universiteit Brussel_ 

> 5 _Center for Human-Compatible AI, UC Berkeley_ 

## **Abstract** 

Adversarial attacks pose a significant threat to data-driven systems, and researchers have spent considerable resources studying them. Despite its economic relevance, this trend largely overlooked the issue of credit card fraud detection. To address this gap, we propose a new threat model that demonstrates the limitations of existing attacks and highlights the necessity to investigate new approaches. We then design a new adversarial attack for credit card fraud detection, employing reinforcement learning to bypass classifiers. This attack, called FRAUD-RLA, is designed to maximize the attacker’s reward by optimizing the exploration-exploitation tradeoff and working with significantly less required knowledge than competitors. Our experiments, conducted on three different heterogeneous datasets and against two fraud detection systems, indicate that FRAUD-RLA is effective, even considering the severe limitations imposed by our threat model. 

## **1 Introduction** 

In the first half of 2023, credit card payments in the euro area accounted for over 50 trillion euros [5]. Given the size of the domain and its economic relevance, ensuring the robustness of payment systems is paramount, and vast resources are continuously being spent on improving the quality of credit card fraud detection systems. In particular, the role played by machine learning can hardly be overestimated [1]. Research on fraud detection, however, has focused on the statistical properties of frauds [14, 48], and proper assessments of the risk posed by adaptive fraudsters’ strategies are lacking in the literature. In most domains, robustness is assessed through _adversarial attacks_ [38, 43], i.e., attacks designed against machine learning models. Although many such attacks have been created over the past decade (see Section 2.2), the majority of them focus on image recognition [11,43], posing a significant challenge in terms of their generalization to credit card fraud detection. 

Notably, only a handful of works have studied adversarial machine learning in the context of credit card fraud detection. 

The main works [10, 11] attack the same realistic fraud detection engine called BankSealer [9]. In both works, the authors rightfully consider domain-specific challenges generally absent in other adversarial works, such as the intricate feature engineering process performed in fraud detection. However, they operate under the assumption that fraudsters can access the customers’ transaction history. As the authors point out, this may be achieved through the introduction of malware into the victim’s devices. However, this considerably increases the difficulty of performing any attack, as fraudsters must first compromise the customer’s device and observe past transaction history, which constitutes a significantly more complex undertaking than stealing or cloning a card. This may limit the scalability of such attacks and, therefore, their capacity to compromise the overall system security. 

Our work aims to fill the gap in the literature between the fields of credit card fraud detection and adversarial machine learning. To achieve this, our work makes two contributions. First, it provides a novel formulation for adversarial attacks against fraud detection systems. Past works have discussed the lack of human supervision [30] and the significance of aggregated features [31]. These works focused on how constraints impacted existing adversarial attacks against fraud detection but did not lead to the development of a systemic analysis of the threat posed. In this work, we overcome such limitations by proposing a new threat model (Section 2.1) specifically designed to tailor the main characteristics of credit card fraud detection. The definition of the primary challenges and advantages that fraudsters encounter compared to our domains results in the design of Table 1, which demonstrates how existing approaches fail to cope with unknown features, restricted access to the fraud detection engine, and the inability to exploit the absence of human investigation. 

Our main contribution is a novel adversarial attack against credit card fraud detection systems based on Reinforcement Learning [46, RL]. We model the problem of generating fraudulent transactions not detectable by the classifier as an RL problem where the agent is assigned the task of crafting the fraudulent transactions. In that context, the agent is rewarded 

1 

when it successfully fools the classifier. We identify Proximal Policy Optimization [42, PPO] as a suitable RL algorithm, and we use it to create a new attack named FRAUD-RLA (Reinforcement Learning Attack). Our analysis and experiments show that FRAUD-RLA is the most effective attack against credit card fraud detection systems. Unlike previous works, FRAUD-RLA does not require the same degree of access to the model or the users’ transaction history. Moreover, using RL allows us to explicitly model the tradeoff between the quality of the attack pattern found and the time required to find it. As we discuss in Section 2.1, this tradeoff, also known in RL literature as the exploration-exploitation tradeoff [33], is an essential feature of attacking fraud detection systems. To assess the effectiveness of FRAUD-RLA, we test our method against fraud detection engines on real and synthetic datasets. Our experiments, reported in Section 4.2, show the effectiveness of the reinforcement learning approach. 

**Outline** . The rest of the paper is structured as follows. Section 2 provides the background for this work, explaining the threat model we use and introducing the main attack approaches in the literature. Section 3 introduces FRAUD-RLA and explains its functioning. Section 4 discusses the experimental assessment of our method, and Section 5 concludes the paper. 

## **2 Background** 

This Section is composed of two main parts. First, we define the threat model describing the target, i.e., the fraud detection system and the attackers. Then, we present existing attack approaches and compare them against this model. 

## **2.1 Threat model** 

### **2.1.1 Credit Card Fraud Detection** 

In online payment systems, cardholders use their card to access a terminal and perform transactions. Essentially, a transaction consists of an amount paid to a merchant by a cardholder at a given time [28]. Specific features, such as the card brand and the merchant country, characterize cards and terminals. We call _raw features_ these features and the ones directly chosen by the user, such as the transaction amount. Furthermore, cards and terminals have an identifier, allowing the fraud detection system to aggregate transactions based on the card or terminal used in the process. These aggregations are then used to generate a set of features called _aggregated features_ . Such transactions can be built around the customer [9] or terminal [29] history. Raw and aggregated features are then used to train a fraud detection system. This system is built on a composition of human-made rules and machine learning [8, 14], which combine to signal the most likely frauds to the investigators. 

### **2.1.2 Attackers** 

Discussing attackers’ goals, knowledge, and capabilities is crucial to designing realistic attacks, which can be used for robustness assessments [25]. 

In credit card fraud detection, the attackers’ goal is straightforward: deceive the fraud detection system into misclassifying their frauds as genuine transactions. However, two main details differentiate this field from other domains. First, fraudsters can access a limited set of cards, which may be blocked over time. Hence, they need to maximize the number of successful frauds from the beginning through an explorationexploitation tradeoff [33]. This is particularly true as fraud detection data are subject to concept drift [14], forcing the classifiers to adapt to be up-to-date with reality. While these transformations may be too slow to effectively block attacks, given the speed at which they could be performed, fraudsters may discover that the attack patterns they found do not work once the model has been updated. Furthermore, adversarial attacks generally work under the implicit assumption that humans may observe the attacks and detect anomalies, forcing the attackers’ perturbation to be imperceptible [27, 32] to bypass such a human check. In fraud detection, imperceptibility should not be part of the attackers’ goal. Since humans observe only a few suspicious transactions, bypassing the automatic checks is enough to perform a successful attack. 

Defining attackers’ knowledge is more complex. A common principle in computer security literature is "no security through obscurity" [40], meaning that it is better to assume secret information could always fall into the wrong hands. Therefore, considering the attackers’ perfect system knowledge is generally better. Credit card fraud detection, however, presents a peculiar situation. While it is true that a skillful attacker may, in principle, retrieve any information (for instance, through social engineering [39]), such attacks are unlikely to be scalable enough to pose a significant threat to fraud detection systems. For this reason, we assume that attackers may know the principles around which the system is built, like its features engineering process, but not the weights of the trained classifier, which change over time. 

A second form of knowledge, specific to this application, is _data knowledge_ , not to be confused with the _features knowledge_ described in [44]. While _features knowledge_ focuses on knowing the features engineering technique applied by the classifier, it still assumes that the attacker has complete knowledge of the observation location in the original data space. In credit card fraud detection, however, each transaction is also evaluated based on aggregated features. To know these, fraudsters must reconstruct the card’s and terminal’s transaction history, which is challenging. Skillful attackers may achieve this through the use of malware previously injected into the devices [11], but this poses a strong requirement on the attackers’ side and may limit the number of attacks they can perform. For this reason, we work under the more general 

2 



Figure 1: Visual representation of attacks in image recognition (left) and fraud detection (right) 

assumption that attackers know the feature transformation and the general model characteristics and may know some fixed card features, but do not know the aggregate features. Previous literature corroborates this hypothesis, as most fraudsters seem not to be influenced by the cardholder’s behavior before their first fraud with a new stolen card [29]. 

Let us now define attackers’ capabilities. First, they are able to decide the value of transaction features, such as the amount. Instead, they cannot modify fixed card features. They may, in principle, find values that allow them to adjust as they want the aggregated features [11]. However, this would require a complete knowledge of the feature generation process and the previous transactions performed with the used card and terminal, which they do not generally have. 

A graphical representation of the differences between fraud detection and other adversarial attacks in terms of indistinguishability and the query loop is illustrated in Figure 1, highlighting differences between the two settings. First, image recognition attacks are designed to be indistinguishable by humans, but investigators can only observe the most likely frauds in fraud detection. The attacks loop is also different: while standard adversarial attacks perform multiple queries before submitting each attack, fraudsters are evaluated over each transaction, with no difference between query and attack time. 

based on their approach, we group these attacks into four main groups. Then, how some of these attacks have been used in the context of credit card fraud detection. 

### **2.2.1 Taxonomy** 

**Image recognition / Query-based** Query-based attacks acquire information through queries, i.e., attempted attacks, and use feedback provided by the target classifier to improve their attack quality. Most attacks designed against image recognition systems fall into this category [7, 12, 13]. For instance, Boundary Attack [7] first samples the data space to find a valid attack and then gets closer to the original observation by moving along the decision boundary of the model. Notably, this requires continuously estimating the decision boundary locally, which can only be obtained by sending observations to the target model and observing the associated decisions. Applying these attacks to credit card fraud detection is exceptionally challenging. First, they have no mechanism to optimize the exploration-exploitation tradeoff, as the locality of their attacks means a constant number of queries for each attack. Similarly, image recognition attacks are designed to be imperceptible to human eyes, making them incredibly inefficient when such constraint is irrelevant [30]. Finally, they assume full data knowledge to estimate the local boundaries. 

## **2.2 Adversarial Attacks** 

Let us use the defined threat model to design a taxonomy of existing adversarial attacks based on their applicability against credit card fraud detection. Coherently with our threat model, we focus here on attacks that do not require knowing the target classifier, also called _Black Box attacks_ [25]. First, 

**Surrogate Model** The idea behind surrogate models [17, 18] is relatively straightforward. Since querying the target classifier may not always be feasible or efficient, if the attacker can access a labeled training set, they can train a surrogate model whose properties should mimic the ones of the target. Attackers then test their attack on the resulting classifier, also called surrogate, and use attacks transferability [18] to break 

3 

the target classifier. Fraud detection datasets, however, are realistically challenging for an attacker to obtain, especially considering these attacks generally require a labeled dataset. Their reduced availability makes model surrogate attacks extremely hard to apply. 

**Mimicry** The idea behind Mimicry is that if an attacker has access to some data from a class, they might craft attacks that mimic those data so that the classifier recognizes them as belonging to that class [49]. Attackers mimic the behavior of a particular user while satisfying a set of domain constraints [10]. The key advantage compared to Surrogate Model attacks is that Mimicry attacks only need genuine data. Credit card fraud detection data are highly unbalanced, meaning that any random sample of data is likely to be composed mainly of genuine data. As such, an unsupervised dataset is likely composed primarily of genuine transactions [16] and would be a good choice to train Mimicry. 

**Reinforcement Learning** Reinforcement learning has been used as an adversarial attack tool in cross-site scripting [21] and malware detection [23, 47]. These works, however, are domain-specific, and their application to credit card fraud detection leaves many unanswered questions. First, these attacks are designed to modify malicious code while maintaining its functionality. Therefore, they require a starting point (for instance, the original malware) and a set of possible transformations to perform on it. In credit card fraud detection, however, attackers can choose the values of their features freely, without a starting point to modify. Moreover, these attacks are designed with the assumption that once an attack is found, the attacker can reproduce it to infect any number of devices employing the same detection system. This is not true in fraud detection, where attackers have a limited number of cards and have a strong incentive to find working attacking patterns in the shortest possible time. 

### **2.2.2 Attacks on Credit Card Fraud Detection** 

Previous works describing attacks against card fraud detection ( _Fraud attacks_ in Table 1) assume that fraudsters can inject the victim’s device with a banking Trojan, which allows them to perform frauds and, crucially, observe the transactions previously performed using the card [10, 11]. These works use different approaches to solve the problem. First, fraudsters can use a previously acquired dataset of genuine transactions to build a model for genuine users’ behavior and then generate sequences of frauds that avoid detection by blending into genuine transactions’ patterns [10]. Alternatively, if the attacker has access to a set of transactions resembling those used in the training set of the algorithm, they can train a substitute model, called Oracle, and use it to craft their frauds [10]. Interestingly, such a training set can be old or belong to a different institution if the patterns behind the data are close enough to 

allow for attack transferability. The attacker then generates raw transactions; the fraud detection engine aggregates and evaluates them. 

Both attacks can be performed in a Black-Box setting, and using a training set to model the target classifier before starting the attacks implicitly solves the exploration-exploitation tradeoff. The flip side is that they require data to build a surrogate training set, which may be hard to acquire for most attackers and can be a costly operation. More importantly, attacking a customer requires injecting their device with a banking Trojan, which is generally a much stronger assumption than simply cloning or stealing the card. This may limit the number of attackers capable of implementing such a strategy, reducing the threat such attacks pose to fraud detection engines, as they cannot be performed with the same frequency of attacks with fewer requirements. Finally, these attacks assume that classifiers use only raw and customer-based features, as is the case for [9]. However, various works in the literature also use terminal-based aggregations [8, 24]. To attack them using these methods, fraudsters would also need to control the terminal, further increasing the difficulty of performing these attacks. 

## **3 FRAUD-RLA: Reinforcement Learning Against Credit Card Fraud Detection** 

In this Section we present our main contribution, a new attack against credit card fraud detection called FRAUD-RLA. The design of FRAUD-RLA involves three core elements: 

- **Problem Formulation** , where we formalize the concepts of transaction and fraud detection engine and the attacker’s task as discussed in Section 2.1. 

- **Task definition** , where we reformulate the problem as a single-step Partially Observable Markov Decision Process (POMDP) [35,46], allowing us to employ reinforcement learning algorithms. 

- **Solution design** , where we describe how we find the solution through Proximal Policy Optimization [42, PPO], a gradient-based technique capable of online learning the best attack policy. 

## **3.1 Problem Formulation** 

To formulate the problem definition of the attack, we define the attack’s objects (the transactions), the target (the classifier), and the attacker. First, we define a transaction as a triplet: 



where _xc ∈_ R<sup>_C_</sup> are the features _controllable_ by the attacker, such as the amount of the transaction, _xk ∈_ R<sup>_K_</sup> are the features _known_ to the attacker, such as the card number, and _xu ∈_ R<sup>_U_</sup> 

4 

|**Attacks**|**Black Box**|**Imperceptibility**|**Starting point**|**Data**<br>**Knowledge**|**Exploration-Exploitation**<br>**Tradeoff**|**Training Set**<br>**Access**|
|---|---|---|---|---|---|---|
|Query-Based|YES|NO|NO|NO|NO|YES|
|Surrogate Model|YES|Partially|Partially|Partially|YES|NO|
|Mimicry|YES|YES|Partially|Partially|YES|Partially|
|Fraud Attacks|YES|YES|YES|NO|YES|NO/Partially|
|FRAUD-RLA|YES|YES|YES|YES|YES|YES|



Table 1: Compliance of prominent adversarial attack families to fraud detection constraints. Attacks can completely fulfill the requirement (YES), be designed in a way that makes it exceptionally challenging to tackle (NO), or partially fulfill the requirement because their design does not explicitly make it difficult to do so. With FRAUD-RLA we refer to the attack proposed in this paper. 

**Algorithm 1** FRAUD-RLA to maximize the sum of successful frauds (total reward) over training time 

- **Require:** Time budget _t_ max, Fraud Detection Engine _f_ , Set of fraudulent transactions _X_ , environment _M_ 

- 1: Initialize _PPO_ parameters θ 2: _t ←_ 0 3: _total_  reward ←_ 0 4: **while** _t < t_ max **do** 5: Receive _xk, xu_ from _M_ 6: _µ,_ Σ _← PPO.compute_  means_  and_  covariance_ ( _xk_ ) 7: _xc ∼ N_ ( _µ,_ Σ) 8: _reward ←_ 1 _− f_ ( _xc, xk, xu_ ) 9: _PPO.store_ ( _xk, xc, reward_ ) 

- 10: Update θ according to PPO loss 11: _t ← t_ + 1 12: _total_  reward ← total_  reward_ + _reward_ 13: **end while** 

are the features _unknown_ to the attacker, such as the history of previous transactions. We note _C_ the number of controllable features, _U_ the number of unknown features, and _K_ the number of known features. 

Let us now consider a fraud detection engine called _f_ , which takes a transaction _x_ as input and returns a decision _f_ ( _x_ ) = _{_ 0 _,_ 1 _}_ on whether to block the transaction (and the associated card). This fraud detection engine is internally composed of a mix of rule-based and data-driven classification algorithms called _fr_ and _fd_ , respectively. A transaction is considered genuine if accepted by both classifiers, i.e., _f_ ( _x_ ) = 0 if _fr_ ( _x_ ) = 0 and _fd_ ( _x_ ) = 0. Such a classifier is inspired by previous works in the literature (e.g., [8, 14]). In the decision-making process, the attacker observes _xk_ and then determines the values of _xc_ . Then, they submit _xc_ to the fraud detection engine, which evaluates the composed transaction _x_ = _⟨xc, xk, xu⟩_ , and returns the associated label _f_ ( _x_ ). The fraudster can then perform another transaction, which will, in principle, have different values of _xk_ and _xu_ . To model the limited number of frauds an attacker can perform, this operation is repeated for _tmax_ rounds. 

## **3.2 RL environment** 

We model the environment as a single-step Partially Observable Markov Decision Process (POMDP) [35, 46], denoted as _M_ . Formally, this can be written as: _M_ = _⟨S, O, A, T, R,_ Ω _⟩_ , where _S_ is state space, _O_ is the observation space, _A_ is action space, _T_ is the transition function, _R_ is the reward function, and Ω is the observation function. Each of these components is defined as follows. 

- _S_ is a continuous space of size R<sup>_U_+</sup><sup>_K_+</sup><sup>_C_</sup> , i.e. every possible transaction. 

- _O_ is the continuous space set of possible observations of size R<sup>_K_</sup> , i.e. every possible known features. 

- _A_ is a continuous action space of size R<sup>_C_</sup> . 

- _T_ : _S × A → S_ is a deterministic transition function that maps each state-action ( _s, a_ ) pair to a next state _s_<sup>_′_</sup> . Note that _s_ is always an initial state and that _s_<sup>_′_</sup> is always a terminal state since there is a single step to the POMDP. 



- Ω : _S → O_ is the observation function that extracts the observation from the state, i.e. extracts _xk_ from _x_ . 

## **3.3 RL agent** 

We identify Proximal Policy Optimization [42, PPO] as a suitable single-agent Deep Reinforcement Learning algorithm for FRAUD-RLA due to its ability to handle continuous action spaces. Additionally, PPO is known to require little hyperparameter tuning compared to other Deep RL methods and has been proven to perform well in a wide variety of tasks [41,50]. The high-level working principle of FRAUD-RLA is shown in Algorithm 1. At each round, FRAUD-RLA receives the fixed known features as input (line 5). It passes them to PPO, 

5 

Table 2: Actor network architecture of PPO. 

|**Layer type**|**Activation**|**Output size**|
|---|---|---|
|Input||_K_|
|Linear|Tanh|32|
|Linear|Tanh|32|
|Linear||_C_+_C_<sup>2</sup>|



Table 3: Critic network architecture of PPO 

|**Layer type**|**Activation**|**Output size**|
|---|---|---|
|Input||_K_|
|LayerNorm||_K_|
|Linear|Tanh|32|
|Linear|Tanh|32|
|Linear||1|



domain [20, 42] only learn the means of a normal distribution and either use a hand-crafted constant or an annealed value for the variance. 

Our choice to learn the covariance matrix is motivated by two reasons. First, we assume that the features of a transaction (i.e. the action) are correlated. For example, the fact that a terminal is located in a luxury store will influence other parameters such as the amount of the transaction and the type of credit card. Then, we assume that the attackers operate without prior knowledge of the data, forcing them to learn it throughout the training. The need to learn the covariance matrix is the reason why the Actor-Network has _C_ + _C_<sup>2</sup> outputs (see Table 2) because _C_ values are used as the means and _C_<sup>2</sup> values as the covariance matrix of the multivariate normal distribution from which actions are sampled. 

### **3.3.2 Partial observability** 

which generates a conditional multivariate Gaussian distribution over the controllable features space _R_<sup>_C_</sup> (line 6). FRAUDRLA then samples from the distribution a set of controllable features _xc_ (line 7), passes them to the classifier, and receives the reward (line 8), measured as 1 _− f_ ( _xc, xk, xu_ ), where _xu_ are the unknown features at this round. FRAUD-RLA then uses the reward and the fixed and controllable observations to train PPO (lines 9-10). The mechanism repeats at each round. 

Internally, PPO uses an actor-critic architecture [6]. The actor network (Table 2) takes as input the agent observation and outputs the action to take. The critic network (Table 3) takes the agent observations as input and outputs the observations’ value, expressed as the sum of discounted rewards until the end of the episode. Since we are working in a single-step environment, we can express it as the reward associated with the observation. 

The training process uses the reward as feedback to iteratively optimize the actor’s policy using a clipped objective function to maximize the updates’ stability. It also optimizes the critic’s value function using a mean squared error loss to minimize the difference between predicted and actual returns. We show the structure of the actor and critic networks in Table 2 and Table 3, respectively. Since we want FRAUD-RLA to work in different settings and on different datasets without specific hyperparameter tuning, we opted for a straightforward architecture, with both networks presenting only two fully connected inner layers of 32 nodes each. A normalization layer in the Critic Network was added to facilitate the algorithm convergence. 

### **3.3.1 Correlations in the action space** 

Although the network architectures are similar to other works in the field of single-agent RL with continuous action spaces, we differ from most of them by learning the parameters (both the means and the covariance matrix) of a multivariate normal distribution for the action space. In contrast, most works in the 

Note that, unlike other works in the field of partially observable RL [22, 45], we do not use recurrent neural networks (RNN). The reason is that RNNs are typically used for an agent to remember what it has observed in the previous steps of an episode. Since we work in an environment where there is only one step in an episode, there is no need for recurrent networks. 

## **4 Experiments Design** 

In this section, we present an experimental analysis of our work. We first describe our experimental setup including our datasets, our baselines, and our methodology. 

## **4.1 Experimental Setup** 

### **4.1.1 Datasets** 

We evaluate our approach on three different datasets, each selected to represent different properties of fraud detection. Because class balance does not directly affect FRAUD-RLA, all datasets have been balanced for these experiments. To guarantee Mimicry is not negatively affected by this change, we train it using only genuine transactions. Our three datasets are as follows. 

- **Generator** Dataset generated employing the synthetic credit card fraud detection generator from [28]. The generator, used in previous works on fraud detection [29,36], is built on a set of customers interacting with terminals to create transactions, where frauds are inserted according to previously defined patterns. Contrary to other works, the resulting datasets maintain the features’ semantics, allowing aggregated features to be composed. This allows us to divide features into purely transaction-based (like the amount), aggregated on the customer, and aggregated on the terminal. Depending on the threat model, 

6 

the two types of aggregated features can be controllable, known, and unknown features, respectively. 

- **Credit card fraud detection (Kaggle)** Dataset [15] obtain by applying a PCA transformation [34] on 250K real transactions performed in September 2013 by European cardholders. It is one of the most widely used datasets in fraud detection. Each transaction has a label (genuine or fraudulent) and 30 features, including the amount. Since the PCA transformation lost the semantics of the original columns, we randomly select features as known, controllable, and unknown. While not semantically meaningful, this allows us to randomly assign a number of features as unknown and uncontrollable, measuring the impact of their number on attacks’ performance. 

- **SKLearn** A binary classification problem composed of clusters of normally distributed points generated using SKLearn [37]. Although it, too, lacks the original feature semantics, it provides the possibility of selecting different class distributions and problem dimensionalities, which helps us generalize our findings. 

Attackers may be unable to fine-tune their method before testing it against the classifier on a given dataset. For this reason, we will conduct all tests using the same PPO implementation and hyperparameters. While this is a pessimistic assumption for the attacker, it still provides a lower bound on the attack’s effectiveness. Furthermore, this approach allows for a lower entrance barrier for deploying the attack, which, as discussed in Section 2.1, makes the attack’s potential consequences even more severe. 

### **4.1.2 Baseline: Mimicry** 

As discussed in Section 2.1, an attack that does not require access to a training set before it begins is generally easier to deploy. However, no attack reported in related literature can be employed against fraud detection engines under this condition. Hence, to provide a fair baseline in our experiments, we assume that an attacker may access an unlabeled training set, which comprises an easier-to-meet condition than accessing the labeled one. Since data in fraud detection are typically highly skewed towards the genuine class [15], fraudsters may perform a Mimicry attack under this condition, therefore modeling genuine users’ behavior. Since FRAUD-RLA does not need or use such a training set, we effectively put FRAUDRLA at a disadvantage as we compare it with attacks operating in a less challenging environment. Although this could potentially result into a pessimistic assessment of its relative effectiveness, still, it allows us to provide a reasonable baseline for FRAUD-RLA performance. Should FRAUD-RLA remain competitive in such a setting, this would further showcase its effectiveness. 

Mimicry has been employed to replicate the behavior of genuine users, including time-dependent features [10]. However, in our case, we assume that attackers lack knowledge of time-dependent features. Therefore, we adopt a simplified version of Mimicry that approximates user behavior using straightforward statistical methods. While more complex distributions may, in principle, be used, our approach has the significant advantage of requiring significantly less hyperparameter tuning, which aligns with the considered threat model. 

The resulting algorithm, illustrated in Algorithm 2, works as follows. First, the attacker accesses a small training set and uses it to fit a statistical model (line 3). We test different data distributions: a uniform, various univariate normal distribution, a multivariate normal distribution, and a Gaussian mixture with 10 mixture components. Concerning the training set size, we consider two cases: the realistic one, where the attacker can observe a small training set of 1000 observations, and the pessimistic case, where we allow the attacker to observe the complete training set. At each round, the attacker randomly samples the values of the controllable features from the trained distribution (line 6) and sends them to the classifier. The resulting transaction combines the controllable features generated by Mimicry, as well as the fixed and the unknown features, and is evaluated by the classifier (line 7). 

**Algorithm 2** Mimicry to maximize the sum of successful frauds (total reward) over training time 

- **Require:** Time budget _t_ max, Fraud Detection Engine _f_ , Set of fraudulent transactions _X_ , environment _M_ , small training set _TR_<sup>_′_</sup> , distribution family _g_ 

- 1: _t ←_ 0 2: _total_  reward ←_ 0 3: Fit distribution _g ← g_ ( _TR_<sup>_′_</sup> ) inside domain _R_<sup>_C_</sup> 

- 4: **while** _t < t_ max **do** 5: Receive _xk, xu_ from _M_ 6: _xc ←_ sample from _g_ 7: _reward ←_ 1 _− f_ ( _xc, xk, xu_ ) 8: _t ← t_ + 1 

- 9: _total_  reward ← total_  reward_ + _reward_ 

- 10: **end while** 

### **4.1.3 Methodology** 

The first step of our evaluation is constructing our fraud detection engine. For this work, we imagine a simplified engine comprising two models: a machine-learning and a rulebased classifier. In line with previous works on credit card fraud detection [2, 16], we test two different machine learning classifiers: a Random Forest (RF) and a feed-forward neural network (NN). Both algorithms are trained with a standard random grid cross-validation strategy for hyperparameters tuning [37]. To penalize strategies based on extreme values, 

7 

||Accuracy|Precision|Recall|F1|
|---|---|---|---|---|
|Generator: RF|0.89|0.95|0.82|0.88|
|Generator: NN|0.89|0.95|0.81|0.88|
|Kaggle: RF|0.95|1.00|0.91|0.95|
|Kaggle: NN|0.93|0.97|0.90|0.93|
|SKLearn 0: RF|1.00|1.00|1.00|1.00|
|SKLearn 0: NN|1.00|1.00|1.00|1.00|
|SKLearn 1: RF|0.99|0.99|0.99|0.99|
|SKLearn 1: NN|0.99|0.99|0.99|0.99|
|SKLearn 2: RF|0.74|0.75|0.74|0.75|
|SKLearn 2: NN|0.82|0.82|0.83|0.82|



Table 4: Classifiers Performance over the tested datasets. 

we pair the machine learning model with a rule-based classifier rejecting transactions where any feature would fall into the 10% most extreme values in the training set. Finally, we run the attacks and measure their improvement over time. We use the average success rate to evaluate the attacks’ success, calculated as the percentage of successful frauds. In particular, we measure it over the first 300, 1000, and 4000 frauds. 

## **4.2 Experimental Findings** 

Next, we present our experimental analysis first using the synthetic data generator, and then, using real data and the SKLearn generator. 

**Synthetic data generator.** First, we analyze the Mimicry results, which provide a baseline for attackers’ performance. To do so, we first compare the performance of the different Mimicry techniques we used. We show the analysis results in Table 5 and Table 6, where we measure the attacks’ success rate over different settings, where each setting is defined by the types of fixed, known features ( _FIXED_ in the tables) and those unknown to the attacker ( _UNKNOWN_ ). We group here features as terminal-based ( _T_ ) and customer-based ( _C_ ) aggregations. For datasets without feature semantics, such as Kaggle and SKLearn, we will instead use the percentage of features belonging to each group. This table, comparing the performance of multiple baselines trained over a dataset of 1000 observations ( _1K_ ) or over the full Training Set ( _100%_ ), allows us to make some considerations. 

First, increasing the size of the training set over 1000 samples does not significantly improve the performance of the algorithms. Second, while the recall of Random Forest and Neural Network on the test is set is practically the same (as shown in Table 4), all Mimicry attacks achieve a significantly higher success rate against Neural Networks, showing the superior robustness of Random Forests. This aligns with previous findings in the literature, where Random Forests proved to be more robust than deep learning algorithms against traditional adversarial attacks [19]. Finally, when fraudsters con- 

trol all the features, Mimicry attacks achieve a very high success rate against classifiers having recalls of over 0 _._ 9 on non-adversarial data. However, attacks’ effectiveness dramatically decreases when we reduce the number of controllable features, as shown by the decreasing success rate. 

Next, we compare FRAUD-RLA with the best-performing baseline under all settings. We show the results in Table 7 and Table 8. Here, for each setting, we compare the best baseline ( _Best Baseline_ in the table) with the average success of FRAUD-RLA after 300, 1000 and 4000 attacks, respectively. Both tables show an increase in the success rate over time as FRAUD-RLA learns the best attack policy. In the case of random forests, FRAUD-RLA starts with an average cumulative reward that is significantly lower than the baseline but increases until it reaches or surpasses that value. Neural Networks instead are breached from the first rounds by FRUAD-RLA, confirming their inferior robustness. Above all, FRAUD-RLA in most settings surpasses the baselines in Average Cumulative Reward from early rounds, optimizing the exploration-exploitation tradeoff. It should be noted that, in the case of this dataset, knowing fixed features without being able to control them does not help FRAUD-RLA improve its performance, as customers’ and terminals’ features are created by independent processes in the generator [28]. 

**Real data and SKLearn generator.** We continue our analysis over one real and various synthetic datasets, starting with the real dataset, named in the experiments the Kaggle Dataset. 

Table 4 shows that the classifiers perform better on this dataset than on the generator data, with recall values from 0 _._ 9 for both RF and NN. Looking at the cumulative success rate, we see in Table 9 and Table 10 how the baseline is still highly effective when having full control over the features. However, this quickly decreases with the number of fixed and unknown features. Instead, FRAUD-RLA average success rate decreases very slowly with the number of fixed or unknown features, with only some configuration of Random Forest leading to a success rate below 0 _._ 9. Interestingly, in this dataset, known fixed features seem to improve the performance of FRAUD-RLA compared to unknown features. More tests should be performed to study the significance of this effect. 

Finally, we use SKLearn to study the impact of dimensionality and task complexity on the attack’s effectiveness. To do so, we focus on three specific settings: 

- Scenario 1 (easy): A problem with 16 features, 1 cluster per class, and high separation between the classes. 

- Scenario 2 (intermediate): A problem with 64 features, 8 cluster per, class and high separation between the classes. 

- Scenario 3 (hard): A problem with 64 features, 16 cluster per class, and small separation between the classes. 

8 

|**Fe**|**atures**|||**B**|**aseline A**|**lgorith**|**ms**|||
|---|---|---|---|---|---|---|---|---|---|
|||**Mu**|**ltivar**|**Un**|**ivar**|**Uni**|**form**|**Mi**|**xture**|
|**Fixed**|**Unknown**|**1k**|**100%**|**1k**|**100%**|**1k**|**100%**|**1k**|**100%**|
|/|/|0.84|0.83|0.67|0.66|0.68|0.69|0.85|0.86|
|/|T|0.52|0.52|0.40|0.39|0.39|0.39|0.57|0.57|
|/|C|0.60|0.60|0.60|0.60|0.66|0.65|0.56|0.56|
|/|C,T|0.23|0.23|0.23|0.23|0.26|0.26|0.23|0.23|
|T|/|0.52|0.52|0.40|0.39|0.39|0.39|0.57|0.58|
|T|C|0.23|0.23|0.23|0.23|0.26|0.26|0.23|0.23|
|C|/|0.60|0.60|0.60|0.60|0.66|0.65|0.56|0.56|
|C|T|0.23|0.23|0.23|0.23|0.26|0.26|0.23|0.23|
|C,T|/|0.23|0.23|0.23|0.23|0.26|0.26|0.23|0.23|



Table 5: Generator, Random Forest. Baselines Success Rate comparison under various scenarios. Each baseline is trained in two ways: on 1000 observations and over the whole training set. 

|**Fe**|**atures**|||**B**|**aseline A**|**lgorith**|**ms**|||
|---|---|---|---|---|---|---|---|---|---|
|**Fixed**|**Unknown**|**Mu**<br>**1k**|**ltivar**<br>**100%**|**Un**<br>**1k**|**ivar**<br>**100%**|**Uni**<br>**1k**|**form**<br>**100%**|**Mi**<br>**1k**|**xture**<br>**100%**|
|/|/|0.90|0.89|0.72|0.71|0.67|0.66|0.89|0.89|
|/|T|0.58|0.58|0.45|0.44|0.43|0.43|0.60|0.60|
|/|C|0.69|0.69|0.70|0.69|0.75|0.72|0.66|0.66|
|/|C,T|0.32|0.32|0.32|0.31|0.33|0.33|0.32|0.32|
|T|/|0.58|0.57|0.45|0.44|0.43|0.43|0.60|0.60|
|T|C|0.32|0.32|0.32|0.32|0.33|0.33|0.31|0.32|
|C|/|0.70|0.69|0.70|0.69|0.75|0.72|0.66|0.66|
|C|T|0.32|0.32|0.32|0.32|0.33|0.33|0.31|0.32|
|C,T|/|0.32|0.32|0.32|0.32|0.33|0.33|0.31|0.32|



Table 6: Generator, Neural Network. Baselines Success Rate comparison under various scenarios. Each baseline is trained in two ways: on 1000 observations and over the whole training set. 

|**Fe**<br>**Fixed**|**atures**<br>**Unknown**|**FRAU**<br>**300**|**D-RLA**<br>**1000**|**Time**<br>**4000**|**Best**<br>**Baseline**|
|---|---|---|---|---|---|
|/|/|0.15|0.37|0.75|0.86|
|/|T|0.12|0.28|0.53|0.57|
|/|C|0.32|0.57|0.74|0.66|
|/|C, T|0.24|0.25|0.28|0.26|
|T|/|0.13|0.30|0.53|0.58|
|T|C|0.24|0.25|0.28|0.26|
|C|/|0.33|0.57|0.73|0.66|
|C|T|0.24|0.25|0.28|0.26|
|C, T|/|0.24|0.25|0.28|0.26|



|**Fe**<br>**Fixed**|**atures**<br>**Unknown**|**FRAU**<br>**300**|**D-RLA**<br>**1000**|**Time**<br>**4000**|**Best**<br>**Baseline**|
|---|---|---|---|---|---|
|/|/|0.72|0.86|0.89|0.90|
|/|T|0.64|0.85|0.91|0.60|
|/|C|0.79|0.90|0.92|0.75|
|/|C T|0.80|0.93|0.97|0.33|
|T|/|0.62|0.85|0.91|0.60|
|T|C|0.77|0.92|0.97|0.33|
|C|/|0.79|0.91|0.93|0.75|
|C|T|0.78|0.92|0.97|0.33|
|C, T|/|0.79|0.93|0.97|0.33|



Table 7: Generator, Random Forest. Comparison between the average Cumulative Reward of FRAUD-RLA over 300, 1000 and 4000 frauds with the best baseline in each setting. 

Table 8: Generator, Neural Network. Comparison between the average Cumulative Reward of FRAUD-RLA over 300, 1000 and 4000 frauds with the best baseline in each setting. 

9 

|**Fe**<br>**Fixed**|**atures**<br>**Unknown**|**FRAU**<br>**300**|**D-RLA**<br>**1000**|**Time**<br>**4000**|**Best**<br>**Baseline**|
|---|---|---|---|---|---|
|0%|0%|0.87|0.90|0.91|0.99|
|0%|25%|0.83|0.89|0.90|0.91|
|25%|0%|0.86|0.91|0.91|0.92|
|0%|50%|0.76|0.86|0.89|0.71|
|25%|25%|0.77|0.88|0.90|0.71|
|50%|0%|0.76|0.87|0.90|0.65|
|25%|50%|0.46|0.57|0.64|0.34|
|50%|25%|0.48|0.62|0.69|0.35|



Table 9: Kaggle, Random Forest. Comparison between the average Cumulative Reward of FRAUD-RLA over 300, 1000 and 4000 frauds with the best baseline in each setting. 

|**Fe**<br>**Fixed**|**atures**<br>**Unknown**|**FRAU**<br>**300**|**D-RLA**<br>**1000**|**Time**<br>**4000**|**Best**<br>**Baseline**|
|---|---|---|---|---|---|
|0%|0%|0.87|0.90|0.93|0.94|
|0%|25%|0.87|0.91|0.94|0.58|
|25%|0%|0.86|0.92|0.94|0.60|
|0%|50%|0.88|0.92|0.95|0.41|
|25%|25%|0.88|0.93|0.95|0.39|
|50%|0%|0.87|0.92|0.95|0.41|
|25%|50%|0.88|0.94|0.96|0.26|
|50%|25%|0.88|0.94|0.96|0.28|



Table 10: Kaggle, Neural Network. Comparison between the average Cumulative Reward of FRAUD-RLA over 300, 1000 and 4000 frauds with the best baseline in each setting. 

Table 4 illustrates that both classifiers perform nicely when applied in the first two scenarios while struggling in the third one. We show the best baseline performance and how FRAUD-RLA compares with it in Table 11 and Table 12. In both tables, we only report the variation of FRAUD-RLA from the baseline after 4000 attacks. 

Similarly to the other datasets, Neural Networks, despite being more powerful than random forests on the original datasets, are more frequently breached by FRAUD-RLA, confirming their inferior robustness. Concerning the attacks, FRAUD-RLA is the best attack against Neural Networks, where it achieves an excellent success rate in all scenarios, particularly compared to Mimicry. Experiments conducted on Random Forests give a more complex picture. FRAUD-RLA is still the best method in Scenario 3, with attacks breaking the classifier even when most features are uncontrollable or unknown. Scenarios 1 and 2 are difficult for all attacks, but in Scenario 2, the baseline outperforms FRAUD-RLA. Investigating this in greater detail, it turns out that the current implementation of FRAUD-RLA performs better in exploration scenarios, and hence, it outperforms Mimicry when more features are hidden. Instead, Mimicry thrives in a set- 

ting where classes are clearly divided and all features are controllable. This is more evident in the first three lines where Mimicry performs better than FRAUD-RLA. It is worth noting that such cases, although useful in a thorough analysis, are very unlikely in real-world settings where most features are routinely unknown or fixed. Hence, we expect FRAUD-RLA to be an excellent tool for most practical scenarios. 

## **5 Conclusions and future work** 

Adversarial attacks are a growing threat, and credit card fraud detection systems are sensitive targets. The lack of research at the intersection of the two domains is a potential vulnerability for existing fraud detection engines. It increases the likelihood of catastrophic consequences should fraudsters identify and implement an effective attack strategy. This work aimed to mitigate this problem by analyzing the domain’s main features, focusing on differences with more traditional domains, such as image recognition and malware detection. 

Understanding the challenges attackers face is crucial when designing and modeling the threat of advanced machine learning for fraud detection. Therefore, we expanded existing threat models to adapt them to credit card fraud detection. Specifically, we updated existing approaches to consider the lack of human supervision, the limited data knowledge and control, and the exploration-exploitation tradeoff. Using the defined threat model as a blueprint, we developed FRAUD-RLA, a novel attack designed explicitly to tackle the aforementioned issues. To do so, we modeled the problem of finding a successful fraudulent pattern in the shortest possible time as a Partially Observable Markov Decision Process, where the known fixed features represent the visible state and the action corresponds to selecting the optimal values for the controllable features. To optimize this problem, we employed Proximal Policy Optimization (PPO), a robust algorithm able to optimize continuous policies with little hyperparameter optimization. Our experiments show that FRAUD-RLA quickly achieves a high average success rate under most settings, consistently beating the baselines without optimizing the hyperparameters against the different datasets and target classifiers. 

It is worth noting that we do not aiming at developing an "off-the-shelf" attack that could be directly applied in a real-world scenario. The presence of categorical variables, eventual limitations to the frequency at which frauds can be performed without raising any alarm, and, in general, the need to adapt the attack to various challenges that may arise in the real case, all serve to illustrate why FRAUD-RLA does not constitute an immediate threat to any real-world system, and is not, as such, a valuable tool for malignous agents. On the contrary, improving our understanding of adversarial security of fraud detection systems will be crucial in developing effective defenses. As security is frequently evaluated through the lens of red teaming [4], it is imperative to use the appropriate tools for comprehensive assessments and improvements, and 

10 

|**Fe**<br>**Fixed**|**atures**<br>**Unknown**|<br>**Dataset 1**|**Best Baselin**<br>**Dataset 2**|**e**<br>**Dataset 3**|**FRAUD-R**<br>**Dataset 1**|**LA Variatio**<br>**Dataset 2**|**n from baseline**<br>**Dataset 3**|
|---|---|---|---|---|---|---|---|
|0 %|0 %|1|1|0.72|-0.12|-0.47|0.02|
|0 %|25%|0.97|0.93|0.62|-0.12|-0.41|0.17|
|25%|0%|0.99|0.94|0.63|-0.11|-0.43|0.09|
|0 %|50%|0.53|0.45|0.5|0.08|-0.05|0.13|
|25%|25%|0.43|0.46|0.5|0.17|-0.04|0.12|
|50%|0%|0.58|0.46|0.5|0.05|0.12|0.10|
|25%|50%|0.03|0.04|0.37|0.00|0.03|0.24|
|50%|25%|0.01|0.04|0.38|0.00|0.02|0.23|



Table 11: SKLearn, Random Forest. Best baseline performance over different datasets and FRAUD-RLA improvement over it measured after 4000 frauds. 

|**Fe**<br>**Fixed**|**atures**<br>**Unknown**|**Dataset 1**|**Baseline**<br>**Dataset 2**|**Dataset 3**|**FRAUD-R**<br>**Dataset 1**|**LA Variatio**<br>**Dataset 2**|**n from baseline**<br>**Dataset 3**|
|---|---|---|---|---|---|---|---|
|0%|0%|1.00|1.00|0.80|-0.08|-0.22|-0.07|
|0%|25%|0.91|0.87|0.65|0.02|-0.06|0.10|
|25%|0%|0.97|0.87|0.66|0.04|-0.06|0.10|
|0 %|50%|0.39|0.44|0.49|0.54|0.39|0.30|
|25%|25%|0.42|0.45|0.50|0.51|0.39|0.31|
|50%|0%|0.45|0.41|0.49|0.49|0.43|0.31|
|25%|50%|0.02|0.08|0.33|0.94|0.80|0.54|
|50%|25%|0.04|0.09|0.33|0.92|0.75|0.55|



Table 12: SKLearn, Neural Network. Best baseline performance over different datasets and FRAUD-RLA improvement over it measured after 4000 frauds. 

we designed FRAUD-RLA to fill that role eventually. 

Future work may span several challenging directions. First, different reinforcement learning algorithms could be tried, such as contextual bandit algorithms [26, 51], that are dedicated to stateful single-step problems. Moreover, FRAUDRLA could be extended to tackle other fraud detection aspects that we did not consider in this work, such as the presence of categorical variables and the possibility of delayed feedback caused by the presence of humans in the loop. More generally, assessing FRAUD-RLA in even more realistic environments is a necessary step to move over the lab-only evaluation phase [3] and transform it into a proper system to evaluate the robustness of the existing engines in production. Another promising direction would be to use FRAUD-RLA to develop solid defenses that can limit the effectiveness of attacks based on reinforcement learning against credit card fraud detection. Following this direction, we are currently researching the effectiveness of training a classifier to prioritize learning from features that are uncontrollable or unknown to the attacker to achieve _robust by design_ credit card fraud detection. 

## **6 Ethics Considerations** 

Machine learning systems are employed in various applications, and research should always make them more secure. 

Unresponsable disclosure of vulnerabilities can give attackers a head start and severely limit the systems’ security. Researching vulnerabilities, however, remains crucial to mitigate the risk posed by zero-day threats. Adversarial machine learning literature, for instance, is built on the assumption that published attacks improve our understanding of machine learning models’ vulnerabilities. 

In this work, we did not aim to exploit vulnerabilities of any specific system. Instead, we used open research as a baseline to define how fraud detection engines work. Our threat model and the attack we designed are not intended to directly apply to any system in production. As stated in Section 5, this would require updating the attack to tackle issues like categorical variables, transaction frequency caps, and, in general, multiple challenges real-world systems present that are not described in the literature. However, reinforcement learning does threaten fraud detection, as it has been shown to do in malware detection [23] and as we showed in this work. In reality, the lack of research on the topic is arguably one of the main vulnerabilities, as it increases the chance attackers may find successful strategies that employ reinforcement learning before the community has a solid understanding of the threat. 

Therefore, this work’s primary goal is to provide a framework to study these attacks and how they can challenge systems’ robustness. First, this could be used by fraud detection practitioners to evaluate their systems, possibly extending and 

11 

modifying FRAUD-RLA to use it for their own tests. Ultimately, however, our work is intended to help us understand how to defend against RL-based attacks. Hopefully, FRAUDRLA will help us and other researchers towards achieving this goal in the shortest possible time. Finally, all experiments were conducted on openly available data without targeting any in-production system. Therefore, no participant was harmed in the writing of this paper nor in the design and test of the attack. 

## **7 Open Science** 

The threat model and the theoretical analysis were based on published works, and this paper is designed to be fully open and reproducible. Specifically, the Generator code is available at [28], the Kaggle Dataset at Kaggle Dataset, and SKLearn is an open library. The code of the experiments will be released and openly available on Github, toghether with the instructions to set up the datasets and the experiments. Finally, the experiments were designed to be open and fair. Metrics, hyperparameters, and datasets were chosen for their applicability to credit card fraud detection and are coherent with previous works and the problem. 

## **References** 

- [1] Aisha Abdallah, Mohd Aizaini Maarof, and Anazida Zainal. Fraud detection system: A survey. _Journal of Network and Computer Applications_ , 68:90–113, 2016. 

- [2] Aderemi O Adewumi and Andronicus A Akinyelu. A survey of machine-learning and nature-inspired based credit card fraud detection techniques. _International Journal of System Assurance Engineering and Management_ , 8:937–953, 2017. 

- [3] Daniel Arp, Erwin Quiring, Feargus Pendlebury, Alexander Warnecke, Fabio Pierazzi, Christian Wressnegger, Lorenzo Cavallaro, and Konrad Rieck. Dos and don’ts of machine learning in computer security. In _31st USENIX Security Symposium (USENIX Security 22)_ , pages 3971– 3988, 2022. 

- [4] Shahar Avin, Haydn Belfield, Miles Brundage, Gretchen Krueger, Jasmine Wang, Adrian Weller, Markus Anderljung, Igor Krawczuk, David Krueger, Jonathan Lebensold, et al. Filling gaps in trustworthy development of ai. _Science_ , 374(6573):1327–1329, 2021. 

- [5] Europea Central Bank. Payments statistics: first half of 2023, 2024. 

- [6] Andrew G Barto, Richard S Sutton, and Charles W Anderson. Neuronlike adaptive elements that can solve difficult learning control problems. _IEEE transactions on systems, man, and cybernetics_ , (5):834–846, 1983. 

- [7] Wieland Brendel, Jonas Rauber, and Matthias Bethge. Decision-based adversarial attacks: Reliable attacks against black-box machine learning models. _arXiv preprint arXiv:1712.04248_ , 2017. 

- [8] Fabrizio Carcillo, Andrea Dal Pozzolo, Yann-Aël Le Borgne, Olivier Caelen, Yannis Mazzer, and Gianluca Bontempi. Scarff: a scalable framework for streaming credit card fraud detection with spark. _Information fusion_ , 41:182–194, 2018. 

- [9] Michele Carminati, Roberto Caron, Federico Maggi, Ilenia Epifani, and Stefano Zanero. Banksealer: A decision support system for online banking fraud analysis and investigation. _computers & security_ , 53:175–186, 2015. 

- [10] Michele Carminati, Mario Polino, Andrea Continella, Andrea Lanzi, Federico Maggi, and Stefano Zanero. Security evaluation of a banking fraud analysis system. _ACM Transactions on Privacy and Security (TOPS)_ , 21(3):1–31, 2018. 

- [11] Michele Carminati, Luca Santini, Mario Polino, and Stefano Zanero. Evasion attacks against banking fraud detection systems. In _23rd International Symposium on Research in Attacks, Intrusions and Defenses (RAID 2020)_ , pages 285–300, 2020. 

- [12] Jianbo Chen, Michael I Jordan, and Martin J Wainwright. Hopskipjumpattack: A query-efficient decision-based attack. In _2020 ieee symposium on security and privacy (sp)_ , pages 1277–1294. IEEE, 2020. 

- [13] Pin-Yu Chen, Huan Zhang, Yash Sharma, Jinfeng Yi, and Cho-Jui Hsieh. Zoo: Zeroth order optimization based black-box attacks to deep neural networks without training substitute models. In _Proceedings of the 10th ACM workshop on artificial intelligence and security_ , pages 15–26, 2017. 

- [14] Andrea Dal Pozzolo, Giacomo Boracchi, Olivier Caelen, Cesare Alippi, and Gianluca Bontempi. Credit card fraud detection: a realistic modeling and a novel learning strategy. _IEEE transactions on neural networks and learning systems_ , 29(8):3784–3797, 2017. 

- [15] Andrea Dal Pozzolo, Olivier Caelen, Reid A Johnson, and Gianluca Bontempi. Calibrating probability with undersampling for unbalanced classification. In _2015 IEEE symposium series on computational intelligence_ , pages 159–166. IEEE, 2015. 

- [16] Andrea Dal Pozzolo, Olivier Caelen, Yann-Ael Le Borgne, Serge Waterschoot, and Gianluca Bontempi. Learned lessons in credit card fraud detection from a practitioner perspective. _Expert systems with applications_ , 41(10):4915–4928, 2014. 

12 

- [17] Islam Debicha, Benjamin Cochez, Tayeb Kenaza, Thibault Debatty, Jean-Michel Dricot, and Wim Mees. Adv-bot: Realistic adversarial botnet attacks against network intrusion detection systems. _Computers & Security_ , 129:103176, 2023. 

- [18] Ambra Demontis, Marco Melis, Maura Pintor, Matthew Jagielski, Battista Biggio, Alina Oprea, Cristina NitaRotaru, and Fabio Roli. Why do adversarial attacks transfer? explaining transferability of evasion and poisoning attacks. In _28th USENIX security symposium (USENIX security 19)_ , pages 321–338, 2019. 

- [19] Yifan Ding, Liqiang Wang, Huan Zhang, Jinfeng Yi, Deliang Fan, and Boqing Gong. Defending against adversarial attacks using random forest. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops_ , pages 0–0, 2019. 

- [20] Yan Duan, Xi Chen, Rein Houthooft, John Schulman, and Pieter Abbeel. Benchmarking deep reinforcement learning for continuous control, 2016. 

- [21] Yong Fang, Cheng Huang, Yijia Xu, and Yang Li. Rlxss: Optimizing xss detection model to defend against adversarial attacks based on reinforcement learning. _Future Internet_ , 11(8):177, 2019. 

- [22] Matthew Hausknecht and Peter Stone. Deep recurrent q-learning for partially observable mdps. In _2015 aaai fall symposium series_ , 2015. 

- [23] S. Anderson Hyrum, Kharkar Anant, Filar Bobby, Evans David, and Roth Phil. Learning to evade static PE machine learning malware models via reinforcement learning. _CoRR_ , abs/1801.08917, 2018. 

- [24] Sanjeev Jha, Montserrat Guillen, and J Christopher Westland. Employing transaction aggregation strategy to detect credit card fraud. _Expert systems with applications_ , 39(16):12650–12657, 2012. 

- [25] Anthony D Joseph, Blaine Nelson, Benjamin IP Rubinstein, and JD Tygar. _Adversarial machine learning_ . Cambridge University Press, 2019. 

- [26] Parnian Kassraie and Andreas Krause. Neural contextual bandits without regret. In Gustau Camps-Valls, Francisco J. R. Ruiz, and Isabel Valera, editors, _Proceedings of The 25th International Conference on Artificial Intelligence and Statistics_ , volume 151 of _Proceedings of Machine Learning Research_ , pages 240–278. PMLR, 28–30 Mar 2022. 

- [27] Samer Y Khamaiseh, Derek Bagagem, Abdullah AlAlaj, Mathew Mancino, and Hakam W Alomari. Adversarial deep learning: A survey on adversarial attacks and defense mechanisms on image classification. _IEEE Access_ , 10:102266–102291, 2022. 

- [28] Yann-Aël Le Borgne, Wissam Siblini, Bertrand Lebichot, and Gianluca Bontempi. _Reproducible Machine Learning for Credit Card Fraud Detection - Practical Handbook_ . Université Libre de Bruxelles, 2022. 

- [29] Daniele Lunghi, Gian Marco Paldino, Olivier Caelen, and Gianluca Bontempi. An adversary model of fraudsters’ behavior to improve oversampling in credit card fraud detection. _IEEE access_ , 11:136666–136679, 2023. 

- [30] Daniele Lunghi, Alkis Simitsis, and Gianluca Bontempi. Assessing adversarial attacks in real-world fraud detection. In _2024 IEEE International Conference on Web Services (ICWS)_ , pages 27–34, 2024. 

- [31] Daniele Lunghi, Alkis Simitsis, Olivier Caelen, and Gianluca Bontempi. Adversarial learning in real-world fraud detection: Challenges and perspectives. In _Proceedings of the Second ACM Data Economy Workshop_ , pages 27–33, 2023. 

- [32] Bo Luo, Yannan Liu, Lingxiao Wei, and Qiang Xu. Towards imperceptible and robust adversarial example attacks against neural networks. In _Proceedings of the AAAI conference on artificial intelligence_ , volume 32, 2018. 

- [33] William G Macready and David H Wolpert. Bandit problems and the exploration/exploitation tradeoff. _IEEE Transactions on evolutionary computation_ , 2(1):2–22, 1998. 

- [34] Andrzej Ma´ckiewicz and Waldemar Ratajczak. Principal components analysis (pca). _Computers & Geosciences_ , 19(3):303–342, 1993. 

- [35] Frans A. Oliehoek and Christopher Amato. _A Concise Introduction to Decentralized POMDPs_ . SpringerBriefs in Intelligent Systems. Springer International Publishing, 2016. 

- [36] Gian Marco Paldino, Bertrand Lebichot, Yann-Aël Le Borgne, Wissam Siblini, Frédéric Oblé, Giacomo Boracchi, and Gianluca Bontempi. The role of diversity and ensemble learning in credit card fraud detection. _Advances in Data Analysis and Classification_ , 18(1):193–217, 2024. 

- [37] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine learning in Python. _Journal of Machine Learning Research_ , 12:2825–2830, 2011. 

- [38] Maura Pintor, Daniele Angioni, Angelo Sotgiu, Luca Demetrio, Ambra Demontis, Battista Biggio, and Fabio 

13 

Roli. Imagenet-patch: A dataset for benchmarking machine learning robustness against adversarial patches. _Pattern Recognition_ , 134:109064, 2023. 

- [39] Fatima Salahdine and Naima Kaabouch. Social engineering attacks: A survey. _Future internet_ , 11(4):89, 2019. 

- [40] Karen Scarfone, Wayne Jansen, Miles Tracy, et al. Guide to general server security. _NIST Special Publication_ , 800(123), 2008. 

- [41] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. pages 1–12. 

   - [49] David Wagner and R Dean. Intrusion detection via static analysis. In _Proceedings 2001 IEEE Symposium on Security and Privacy. S&P 2001_ , pages 156–168. IEEE, 2000. 

   - [50] Chao Yu, Akash Velu, Eugene Vinitsky, Jiaxuan Gao, Yu Wang, Alexandre Bayen, and Yi Wu. The surprising effectiveness of ppo in cooperative multi-agent games. _Advances in Neural Information Processing Systems_ , 35:24611–24624, 2022. 

   - [51] Dongruo Zhou, Lihong Li, and Quanquan Gu. Neural contextual bandits with UCB-based exploration. In _Proceedings of the 37th International Conference on Machine Learning_ , 2020. 

- [42] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _CoRR_ , abs/1707.06347, 2017. 

- [43] Wei Song, Xuezixiang Li, Sadia Afroz, Deepali Garg, Dmitry Kuznetsov, and Heng Yin. Mab-malware: A reinforcement learning framework for attacking static malware classifiers. _arXiv preprint arXiv:2003.03100_ , 2020. 

- [44] Octavian Suciu, Radu Marginean, Yigitcan Kaya, Hal Daume III, and Tudor Dumitras. When does machine learning _{_ FAIL _}_ ? generalized transferability for evasion and poisoning attacks. In _27th USENIX Security Symposium (USENIX Security 18)_ , pages 1299–1316, 2018. 

- [45] Peter Sunehag, Guy Lever, Audrunas Gruslys, Wojciech Marian Czarnecki, Vinicius Zambaldi, Max Jaderberg, Marc Lanctot, Nicolas Sonnerat, Joel Z. Leibo, Karl Tuyls, and Thore Graepel. Value-decomposition networks for cooperative multi-agent learning. 

- [46] Richard S. Sutton and Andrew G. Barto. _Reinforcement learning: an introduction_ . Adaptive computation and machine learning series. The MIT Press, second edition edition, 2018. 

- [47] Ilias Tsingenopoulos, Ali Mohammad Shafiei, Lieven Desmet, Davy Preuveneers, and Wouter Joosen. Adaptive malware control: Decision-based attacks in the problem space of dynamic analysis. In _Proceedings of the 1st Workshop on Robust Malware Analysis_ , pages 3–14, 2022. 

- [48] Véronique Van Vlasselaer, Cristián Bravo, Olivier Caelen, Tina Eliassi-Rad, Leman Akoglu, Monique Snoeck, and Bart Baesens. Apate: A novel approach for automated credit card transaction fraud detection using network-based extensions. _Decision support systems_ , 75:38–48, 2015. 

14 

