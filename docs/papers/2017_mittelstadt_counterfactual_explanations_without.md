---
title: "Counterfactual Explanations Without Opening the Black Box: Automated Decisions and the GDPR"
authors: "mittelstadt"
year: 2017
arxiv_id: "1711.00399"
original_file: "1711.00399.pdf"
pdf_path: "docs/papers\2017_mittelstadt_counterfactual_explanations_without.pdf"
---

# Counterfactual Explanations Without Opening the Black Box: Automated Decisions and the GDPR

**Authors:** Mittelstadt et al.  
**Year:** 2017 | **arXiv:** [`1711.00399`](https://arxiv.org/abs/1711.00399)  
**Local PDF:** [`2017_mittelstadt_counterfactual_explanations_without.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2017_mittelstadt_counterfactual_explanations_without.pdf)

---

# COUNTERFACTUAL EXPLANATIONS WITHOUT OPENING THE BLACK BOX: AUTOMATED DECISIONS AND THE GDPR 

Sandra Wachter,<sup>*</sup> Brent Mittelstadt,<sup>**</sup> & Chris Russell<sup>***</sup> 

> * Oxford Internet Institute, University of Oxford, 1 St. Giles, Oxford, OX1 3JS, UK and The Alan Turing Institute, British Library, 96 Euston Road, London, NW1 2DB, UK. E- mail: sandra.wachter@oii.ox.ac.uk. This work was supported by The Alan Turing Institute under the EPSRC grant EP/N510129/1. 

> ** Oxford Internet Institute, University of Oxford, 1 St. Giles, Oxford, OX1 3JS, UK, The Alan Turing Institute, British Library, 96 Euston Road, London, NW1 2DB, UK, Department of Science and Technology Studies, University College London, 22 Gordon Square, London, WC1E 6BT, UK. 

> *** The Alan Turing Institute, British Library, 96 Euston Road, London, NW1 2DB, UK, Department of Electrical and Electronic Engineering, University of Surrey, Guildford, GU2 7HX, UK. 

### 2 _COUNTERFACTUAL EXPLANATIONS_ 

## TABLE OF CONTENTS 

|I. Introduction ........................................................................................ 3|
|---|
|II. Counterfactuals ................................................................................. 5|
|_A. Historic Context and The Problem of Knowledge ........................... 7_|
|_B. Explanations in A.I. and Machine Learning .................................. 10_|
|_C. Adversarial Perturbations and Counterfactual Explanations ....... 13_|
|_D. Causality and Fairness .................................................................. 15_|
|III. Generating Counterfactuals ........................................................... 16|
|_A. LSAT dataset .................................................................................. 18_|
|_B. Pima Diabetes Database ................................................................ 20_|
|_C. Causal Assumptions and Counterfactual Explanations ................ 21_|
|IV. Advantages of Counterfactual Explanations .................................. 22|
|V. Counterfactual explanations and the GDPR ................................... 23|
|_A. Explanations to understand decisions ........................................... 25_|
|1. Broader possibilities with the right of access ............................ 32|
|2. Understanding through counterfactuals .................................... 34|
|_B. Explanations to contest decisions .................................................. 35_|
|1. Contesting through counterfactuals .......................................... 40|
|_C. Explanations to alter future decisions ........................................... 42_|
|Conclusion .......................................................................................... 43|
|Appendix 1: Simple Local Models as Explanations ............................. 48|
|Appendix 2: Example Transparency Infographic ................................. 51|



3 

### _COUNTERFACTUAL EXPLANATIONS_ 

## I. INTRODUCTION 

There has been much discussion of the existence of a “right to explanation” in the EU General Data Protection Regulation (“GDPR”), and its merits and disadvantages.<sup>1</sup> Attempts to implement a right to explanation that opens the “black box” to provide insight into the internal decision-making process of algorithms face four major legal and technical barriers. First, a legally binding right to explanation does not exist in the GDPR.<sup>2</sup> Second, even if legally binding, the right would only apply in limited cases (when a negative decision was solely automated and had legal or other similar significant effects).<sup>3</sup> Third, explaining the functionality of complex algorithmic decision-making systems and their rationale in specific cases is a technically challenging problem.<sup>4</sup> Explanations may likewise offer little meaningful information to data subjects, raising questions about their value.<sup>5</sup> Finally, data controllers have an interest in not sharing details of their algorithms to avoid 

> 1 _See, e.g._ , Sandra Wachter, Brent Mittelstadt & Luciano Floridi, _Why a Right to Explanation of Automated Decision-Making Does Not Exist in the General Data Protection Regulation_ , 7 INT’L DATA PRIV. LAW 76, 79–90 (2017); Isak Mendoza & Lee A. Bygrave, _The Right Not to Be Subject to Automated Decisions Based on Profiling_ , _in_ EU INTERNET LAW: REGULATION AND ENFORCEMENT (Tatiani Synodinou et al. eds., 2017), https://papers.ssrn.com/abstract=2964855 [https://perma.cc/XV3T-G98W]; Lilian Edwards & Michael Veale, _Slave to the Algorithm? Why a ‘Right to Explanation’ is Probably Not the Remedy You are Looking For_ , 16 DUKE L. TECH. REV. 18, 18–19 (2017); Tae Wan Kim & Bryan Routledge, _Algorithmic Transparency, a Right to Explanation, and Placing Trust_ , SQUARESPACE (June 2017), https://static1.squarespace.com/static/592ee286d482e908d35b8494/t/59552415579fb3 0c014cd06c/1498752022120/Algorithmic+transparency%2C+a+right+to+explanation+ and+trust+%28TWK%26BR%29.pdf [https://perma.cc/K53W-GVN2]; Gianclaudio Malgieri & Giovanni Comandé, _Why a Right to Legibility of Automated DecisionMaking Exists in the General Data Protection Regulation_ , 7 INT’L DATA PRIV. L. 243, 246–47 (2017); Bryce Goodman & Seth Flaxman, _EU Regulations on Algorithmic Decision-Making and a “Right to Explanation,”_ ARXIV:1606.08813, at 6–7 (2016), http://arxiv.org/abs/1606.08813 [https://perma.cc/5ZTR-WG8R]; Andrew Selbst & Julia Powles, _Meaningful Information and the Right to Explanation_ , 7 INT’L DATA PRIV. L. 233, 233–34 (2017). 

> 2 Wachter, Mittelstadt & Floridi, _supra_ note 1, at 79; Kim & Routledge, _supra_ note 1, at 3. 

> 3 Wachter, Mittelstadt & Floridi, _supra_ note 1, at 78. 

> 4 _See, e.g._ , Wachter, Mittelstadt & Floridi, _supra_ note 1, at 77; Edwards & Veale, _supra_ note 1, at 22; Joshua A. Kroll et al., _Accountable Algorithms_ , 165 U. PA. L. REV. 633, 638 (2016); Tal Zarsky, _Transparent Predictions_ , 2013 U. ILL. L. REV. 1503, 1519–20 (2013). 

> 5 Jenna Burrell, _How the Machine “Thinks:” Understanding Opacity in Machine Learning Algorithms_ , BIG DATA & SOC., Jan.–June 2016, at 5; Kroll et al., _supra_ note 4, at 638. 

### 4 _COUNTERFACTUAL EXPLANATIONS_ 

disclosing trade secrets, violating the rights and freedoms of others (e.g. privacy), and allowing data subjects to game or manipulate the decisionmaking system.<sup>6</sup> 

Despite these difficulties, the social and ethical value (and perhaps responsibility) of offering explanations to affected data subjects remains unaffected. One significant point has been neglected in this discussion. An explanation of automated decisions, both as envisioned by the GDPR and in general, does not necessarily hinge on the general public understanding of how algorithmic systems function. Even though such interpretability is of great importance and should be pursued, explanations can, in principle, be offered without opening the “black box.” Looking at explanations as a means to help a data subject _act_ rather than merely understand, one could gauge the scope and content of explanations according to the specific goal or action they are intended to support. 

Explanations can serve many purposes. To investigate the potential scope of explanations, it seems reasonable to start from the perspective of the data subject, which is the natural person whose data is being collected and evaluated. We propose three aims for explanations to assist data subjects: (1) to inform and help the subject understand why a particular decision was reached, (2) to provide grounds to contest adverse decisions, and (3) to understand what could be changed to receive a desired result in the future, based on the current decision-making model. As we show, the GDPR offers little support to achieve any of these aims. However, none hinge on explaining the internal logic of automated decision-making systems. 

Building trust is essential to increase societal acceptance of algorithmic decision-making. As a solution to close current gaps in transparency and accountability that undermine trust between data controllers and data subjects,<sup>7</sup> we propose to move beyond the limitations 

> 6 Burrell, _supra_ note 5, at 3; Brenda Reddix-Smalls, _Credit Scoring and Trade Secrecy: An Algorithmic Quagmire or How the Lack of Transparency in Complex Financial Models Scuttled the Finance Market_ , 12 U.C. DAVIS BUS. L.J. 87, 94 (2011); Mike Ananny & Kate Crawford, _Seeing without knowing: Limitations of the Transparency Ideal and its Application to Algorithmic Accountability_ , NEW MEDIA & SOC., 2016, at 8, http://journals.sagepub.com/doi/full/10.1177/1461444816676645 

> [https://perma.cc/3HF6-G9DS]; Roger A. Ford & W. Nicholson Price II, _Privacy and Accountability in Black-Box Medicine_ , 23 MICH. TELECOMM. TECH. REV. 1, 3 (2016); Frank A. Pasquale, _Restoring Transparency to Automated Authority_ , 9 J. TELECOMM. HIGH TECH. L. 235, 237 (2011). 

> 7 Wachter, Mittelstadt & Floridi, _supra_ note 1, at 78; Mendoza & Bygrave, _supra_ note 1, at 97. 

### 5 _COUNTERFACTUAL EXPLANATIONS_ 

of the GDPR. We argue that counterfactuals should be used as a means to provide explanations for individual decisions. 

_Unconditional counterfactual explanations_ should be given for positive and negative automated decisions, regardless of whether the decisions are solely (as opposed to predominantly) automated or produce legal or other significant effects. This approach provides data subjects with meaningful explanations to understand a given decision, grounds to contest it, and advice on how the data subject can change his or her behaviour or situation to possibly receive a desired decision (e.g. loan approval) in the future without facing the severely limited applicability imposed by the GDPR’s definition of automated individual decisionmaking.<sup>8</sup> 

In this paper, we present the concept of unconditional counterfactual explanations as a novel type of explanation of automated decisions that overcomes many challenges facing current work on algorithmic interpretability and accountability. We situate counterfactuals in the philosophical history of knowledge, as well as historical and modern research on interpretability and fairness in machine learning. Based on the potential advantages offered to data subjects by counterfactual explanations, we then assess their alignment with the GDPR’s numerous provisions concerning automated decision-making. Specifically, we examine whether the GDPR offers support for explanations that aim to help data subjects understand the scope of automated decision-making as well as the rationale of specific decisions, explanations to contest decisions, and explanations that offer guidance on how data subjects can change their behaviour to receive a desired result. We conclude that unconditional counterfactual explanations can bridge the gap between the interests of data subjects and data controllers that otherwise acts as a barrier to a legally binding right to explanation. 

## II. COUNTERFACTUALS 

Counterfactual explanations take a similar form to the statement: 

“You were denied a loan because your annual income was £30,000. If your income had been £45,000, you would have been offered a loan.” 

> 8 Wachter, Mittelstadt & Floridi, _supra_ note 1, at 87–88; Mendoza & Bygrave, _supra_ note 1, at 83; Edwards & Veale, _supra_ note 1, at 22. 

### 6 _COUNTERFACTUAL EXPLANATIONS_ 

Here the statement of decision is followed by a counterfactual, or statement of how the world would have to be different for a desirable outcome to occur. Multiple counterfactuals are possible, as multiple desirable outcomes can exist, and there may be several ways to achieve any of these outcomes. The concept of the “closest possible world,” or the smallest change to the world that can be made to obtain a desirable outcome, is key throughout the discussion of counterfactuals. In many situations, providing several explanations covering a range of diverse counterfactuals corresponding to relevant or informative “close possible worlds” rather than “the closest possible world” may be more helpful. Knowing the smallest possible change to a variable or set of variables to arrive at a different outcome may not always be the most helpful type of counterfactual. Rather, relevance will depend also upon other casespecific factors, such as the mutability of a variable or real world probability of a change.<sup>9</sup> 

In the existing literature, “explanation” typically refers to an attempt to convey the internal state or logic of an algorithm that leads to a decision.<sup>10</sup> In contrast, counterfactuals describe a dependency on the external facts that led to that decision. This is a crucial distinction. In modern machine learning, the internal state of the algorithm can consist of millions of variables intricately connected in a large web of dependent behaviours.<sup>11</sup> Conveying this state to a layperson in a way that allows them to reason about the behaviour of an algorithm is extremely challenging.<sup>12</sup> 

The machine learning and legal communities have both taken relatively restricted views on what passes for an explanation. The machine learning community has been primarily concerned with debugging<sup>13</sup> and conveying approximations of algorithms that programmers or researchers 

> 9 _See infra_ , Section II.A. 

> 10 _See_ Burrell, _supra_ note 5, at 1 _._ 

> 11 _See, e.g._ , Kaiming He et al., _Deep Residual Learning for Image Recognition_ , _in_ PROCEEDINGS OF THE IEEE CONFERENCE ON COMPUTER VISION AND PATTERN RECOGNITION 770–78 (2016). 

> 12 _See_ Burrell, _supra_ note 5, at 1; Zachary C. Lipton, _The Mythos of Model Interpretability_ , _in_ 2016 WORKSHOP ON HUMAN INTERPRETABILITY IN MACHINE LEARNING 96, 

> http://zacklipton.com/media/papers/mythos_model_interpretability_lipton2016.pdf [https://perma.cc/4JVZ-7T6D]. 

> 13 Osbert Bastani, Carolyn Kim & Hamsa Bastani, _Interpretability via Model Extraction_ , AʀXɪᴠ:1706.09773, at 1 (2017), https://arxiv.org/pdf/1611.07450.pdf [https://perma.cc/8J3J-RE2T]. 

### 7 _COUNTERFACTUAL EXPLANATIONS_ 

could use to understand which features are important<sup>14</sup> while law and ethics scholars have been more concerned with understanding the internal logic of decisions as a means to assess their lawfulness (e.g. prevent discriminatory outcomes), contest them, increase accountability generally, and clarify liability.<sup>15</sup> 

As such, the proposal made here for counterfactuals as explanations lies outside of the taxonomies of explanations proposed previously in machine learning, legal, and ethical literature. In contrast, as we discuss in the next section, analytic philosophy has taken a much broader view of knowledge and how counterfactuals can be used as justifications of beliefs.<sup>16</sup> 

## _A. HISTORIC CONTEXT AND THE PROBLEM OF KNOWLEDGE_ 

Analytic Philosophy has a long history of analysing the necessary conditions for propositional knowledge.<sup>17</sup> Expressions of the type “ _S_ 

> 14 Marco Tulio Ribeiro, Sameer Singh & Carlos Guestrin, _Why Should I Trust You?: Explaining the Predictions of Any Classifier_ , _in_ PROCEEDINGS OF THE 22ND ACM SIGKDD INTERNATIONAL CONFERENCE ON KNOWLEDGE DISCOVERY AND DATA MINING 1135 (2016); Ramprasaath R. Selvaraju et al., _Grad-CAM: Why Did You Say That?_ , ARXIV:1611.07450, at 1 (2016) , https://arxiv.org/abs/1611.07450 [https://perma.cc/AA8F-45XJ]; Karen Simonyan, Andrea Vedaldi & Andrew Zisserman, _Deep inside convolutional networks: Visualising Image Classification Models and Saliency Maps_ , ARXIV:1312.6034, at 1 (2013), https://arxiv.org/abs/1312.6034 [https://perma.cc/Y85R-X9UE]. 

> 15 _See, e.g._ , Finale Doshi-Velez et al., _Accountability of AI Under the Law: The Role of Explanation_ , ARXIV:1711.01134, at 1 (2017); Finale Doshi-Velez, Ryan Budish & Mason Kortz, _The Role of Explanation in Algorithmic Trust_ , TRUSTWORTHY ALGORITHMIC DECISION-MAKING 2, http://trustworthyalgorithms.org/whitepapers/Finale%20Doshi-Velez.pdf [https://perma.cc/4L88-V58A]; Mireille Hildebrandt, _The Dawn of a Critical Transparency Right for the Profiling Era_ , _in_ DIGITAL ENLIGHTENMENT YEARBOOK 2012 41 (Jacques Bus et al. eds., 2012); Tim Miller, _Explanation in Artificial Intelligence: Insights from the Social Sciences_ , ARXIV:1706.07269, at 3 (2017); Pasquale, _supra_ note 6, at 236; Danielle Keats Citron & Frank A. Pasquale, _The Scored Society: Due Process for Automated Predictions_ , 89 WASH. L. REV. 1, 6–7 (2014), https://papers.ssrn.com/abstract=2376209 [https://perma.cc/9CXY-DBTN]; Tal Zarsky, _Transparent Predictions_ , 2013 U. Iʟʟ. L. Rᴇᴠ. 1503, 1506–09 (2013), https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2324240 [https://perma.cc/F8FCYDJG]; Tal Zarsky, _The Trouble with Algorithmic Decisions: An Analytic Road Map to Examine Efficiency and Fairness in Automated and Opaque Decision Making_ , 41 SCI. TECH. HUM. VALUES 118, 118–132 (2016). 

> 16 _See, e.g._ , DAVID LEWIS, COUNTERFACTUALS 1–4, 84–91 (1973); David Lewis, _Counterfactuals and Comparative Possibility_ , 2 J. PHIL. LOGIC 418, 418–446 (1973); Peter Lipton, _Contrastive Explanation_ , 27 ROYAL INST. PHIL. SUPP. 247, 247 (1990); ROBERT NOZICK, PHILOSOPHICAL EXPLANATIONS 172–74 (1981). 

> 17 _See generally_ ALFRED JULES AYER, THE PROBLEM OF KNOWLEDGE (1956). 

### 8 _COUNTERFACTUAL EXPLANATIONS_ 

knows that _p_ ” constitute knowledge, where _S_ refers to the knowing subject, and _p_ to the proposition that is known. Traditional approaches, which conceive of knowledge as “justified true belief,” conceive of three necessary conditions for knowledge: truth, belief, and justification.<sup>18</sup> According to this tripartite approach, in order to know something, it is not enough to simply believe that something is true: rather, you must also have a good reason for believing it.<sup>19</sup> The relevance of this approach comes from the observation that this form of justification of beliefs can serve as a type of explanation,<sup>20</sup> as it is fundamentally a reason that a belief is held and therefore serves as an answer to the question, “Why do you believe _X_ ?” Understanding the different forms these justifications can take opens the door to a broader class of explanations than previously encountered in interpretability research. 

Although influential, “justified true belief” has faced much criticism<sup>21</sup> and inspired substantial analysis of modifications to this tripartite approach as well as proposals for additional necessary conditions for a proposition to constitute knowledge.<sup>22</sup> Modal conditions, including safety<sup>23</sup> and sensitivity,<sup>24</sup> have been proposed as necessary additions to the tripartite built on counterfactual relations.<sup>25</sup> 

Sosa<sup>26</sup> as well as Ichikawa and Steup<sup>27</sup> define sensitivity as: 

<mark>If</mark> _<mark>p</mark>_ <mark>were false,</mark> _<mark>S</mark>_ <mark>would not believe that</mark> _<mark>p</mark>_ <mark>.</mark> 

> 18 _See generally_ Edmund L. Gettier, _Is Justified True Belief Knowledge?_ , 23 ANALYSIS 121 (1963); Julien Dutant, _The Legend of the Justified True Belief Analysis_ , 29 PHIL. PERSP. 95 (2015). 

> 19 _See_ Gettier, _supra_ note 18, at 121. 

> 20 _See_ NOZICK, _supra_ note 16, at 174. 

> 21 _See, e.g._ , Dutant, _supra_ note 18, at 95; Mark Kaplan, _It’s Not What You Know that Counts_ , 82 J. PHIL. 350, 350 (1985). 

> 22 Jonathan Ichikawa & Matthias Steup, _The Analysis of Knowledge_ , _in_ STANFORD ENCYCLOPEDIA OF PHILOSOPHY ARCHIVE (Fall 2017 ed.), https://plato.stanford.edu/archives/fall2017/entries/knowledge-analysis/ [https://perma.cc/6CXB-FTJV]. 

> 23 _See_ Ernest Sosa, _How to Defeat Opposition to Moore_ , 13 PHIL. PERSP. 141, 141–43 (1999). 

> 24 _See_ Jonathan Ichikawa, _Quantifiers, Knowledge, and Counterfactuals_ , 82 PHIL. PHENOMENOLOGICAL RES. 287, 287 (2011); _see also_ NOZICK, _supra_ note 16, at 172–74. 

> 25 _See_ Ichikawa & Steup, _supra_ note 22, Section 5 (reviewing these concepts and their criticisms). 

> 26 Sosa, _supra_ note 23, at 141. 

> 27 Ichikawa & Steup, _supra_ note 22, Section 5.1. 

### 9 _COUNTERFACTUAL EXPLANATIONS_ 

<mark>Here, the statement “If</mark> _<mark>p</mark>_ <mark>were false” is a counterfactual defining a “possible world” close to the world in which</mark> _<mark>p</mark>_ <mark>is true.</mark><sup>28</sup> <mark>The sensitivity condition suggests that “in the nearest possible worlds in which not-</mark> _<mark>p</mark>_ <mark>, the subject does not believe that</mark> _<mark>p.</mark>_ <mark>”</mark><sup>29</sup> <mark>Our notion of counterfactual explanations hinges upon the related concept:</mark> 

<mark>If</mark> _<mark>q</mark>_ <mark>were false,</mark> _<mark>S</mark>_ <mark>would not believe</mark> _<mark>p</mark>_ <mark>.</mark> 

<mark>We claim that in this case,</mark> _<mark>q</mark>_ <mark>serves as an explanation of</mark> _<mark>S</mark>_ <mark>’s belief in</mark> _<mark>p,</mark>_ <mark>inasmuch as</mark> _<mark>S</mark>_ <mark>only holds belief</mark> _<mark>p</mark>_ <mark>while</mark> _<mark>q</mark>_ <mark>is true, and that changing</mark> _<mark>q</mark>_ <mark>would also cause</mark> _<mark>S</mark>_ <mark>’s belief to change. A key point is that such statements only describe</mark> _<mark>S</mark>_ <mark>’s beliefs, which need not reflect reality.</mark><sup>30</sup> <mark>As such, these statements can be made without knowledge of any causal relationship between</mark> _<mark>q</mark>_ <mark>and</mark> _<mark>p</mark>_ <mark>.</mark> 

<mark>We define Counterfactual Explanations as statements taking the</mark> 

<mark>form:</mark> 

<mark>Score</mark> _<mark>p</mark>_ <mark>was returned because variables</mark> _<mark>V</mark>_ <mark>had values (</mark> _<mark>v</mark>_ 1 <mark>,</mark> _<mark>v</mark>_ 2 <mark>,...) associated with them. If</mark> _<mark>V</mark>_ <mark>instead had values (</mark> _<mark>v</mark>_ 1 <mark>',</mark> _<mark>v</mark> 2_ <mark>',...), and all other variables had remained constant, score</mark> _<mark>p</mark>_ <mark>' would have been returned.</mark> 

While many such explanations are possible, an ideal counterfactual explanation would alter values as little as possible and represent a closest world under which score _p_ ' is returned instead of _p_ . The notion of a “closest possible world” is thus implicit in our definition. 

Our version of counterfactuals perhaps most resembles a structural equations approach in execution by identifying alterations to variables. This approach is more similar to Pearl’s “mini-surgeries”<sup>31</sup> than Lewis’ “miracles.”<sup>32</sup> In any case, our approach does not rely on knowledge of the causal structure of the world,<sup>33</sup> or suggest which context-dependent metric of distance between worlds is preferable to establish causality.<sup>34</sup> In many situations, it will be more informative to provide a diverse set of counterfactual explanations, corresponding to different choices of nearby possible worlds for which the counterfactual 

> 28 _See_ LEWIS, _supra_ note 16, at 1–4. 

> 29 Ichikawa & Steup, _supra_ note 22, Section 5.1. 

> 30 For example, _S_ could believe that a person is inherently more trustworthy ( _p_ ) because they are a Capricorn ( _q_ ). 

> 31 _See_ JUDEA PEARL, CAUSATION 223–24 (2000). 

> 32 LEWIS, _supra_ note 16, at 47–48. 

> 33 _See infra,_ Section II.D. 

> 34 _See_ Boris Kment, _Counterfactuals and Explanation_ , 115 MIND 261, 261–309 (2006). 

### 10 _COUNTERFACTUAL EXPLANATIONS_ 

holds or a preferred outcome is delivered, rather than a theoretically ideal counterfactual describing the “closest possible world” according to a preferred distance metric.<sup>35</sup> Case-specific considerations will be relevant to the choice of distance metric and a “sufficient” and “relevant” set of counterfactual explanations. Such considerations may include the capabilities of the individual concerned, sensitivity, mutability of the variables involved in a decision, and ethical or legal requirements for disclosure.<sup>36</sup> 

Similarly, counterfactuals that describe changes to multiple variables within the model can be provided. These would represent possible futures brought about by changes to the individual’s circumstances. As an example, the impact of changes in income could be calculated in combination with changes to career, thereby ensuring the counterfactual represents a realistic possible world. 

## _B. EXPLANATIONS IN A.I. AND MACHINE LEARNING_ 

Much of the early work in A.I. on explaining the decisions made by expert or rule-based systems focused on classes of explanation closely related to counterfactuals. For example, Gregor and Benbasat<sup>37</sup> offer the following example of what they call a type 1 explanation: 

Q: Why is a tax cut appropriate? 

A: Because a tax cut’s preconditions are high inflation and trade deficits, and current conditions include these factors. 

> 35 The merits of different metrics of distance between possible worlds have long been debated in philosophy without the emergence of consensus. Meaningfully addressing this debate goes beyond the scope of this paper which proposes a method for counterfactual explanations, but will be explored in future work. For further discussion of distance metrics and counterfactuals, _see_ LEWIS, _supra_ note 16, at 8–15; Ernest W. Adams, _On the Rightness of Certain Counterfactuals_ , 74 PAC. PHIL. Q. 1, 1–8 (1993); Kment, _supra_ note 34, at 262. 

> 36 A discussion of appropriate metrics for making these choices goes beyond the scope of this paper, but will be addressed in future work. With that said, relevant philosophical discussion can be found on determining relevance of possible causal or contrastive explanations, counterfactuals, and distance metrics. _See, e.g._ , Peter Lipton, _Contrastive Explanation_ , 27 ROYAL INST. PHIL. SUPP. 247, 254–65 (1990); Adams, _supra_ note 35, at 1–8. 

> 37 Shirley Gregor & Izak Benbasat, _Explanations from Intelligent Systems: Theoretical Foundations and Implications for Practice_ , 23 MIS Q. 497, 503 (1999). 

### 11 _COUNTERFACTUAL EXPLANATIONS_ 

Buchanan and Shortliffe<sup>38</sup> offer a similar example: 

**RULE009** IF: 

1) The gram stain of the organism is gramneg, and 

2) The morphology of the organism is coccus THEN: There is strongly suggestive evidence (.8) that the identity of the organism is Neisseria 

As is typical in early A.I., questions we now recognise as hard such as “How do we decide inflation is high?” or “Why are these the preconditions of a tax cut?” are assumed to have been addressed by humans, and are not discussed as part of the explanation.<sup>39</sup> As such, the explanations do not provide insight into what people in machine learning think of as the internal logic of black box classifiers. In fact, the first example can be rewritten as two diverse counterfactual statements: 

“If inflation was lower, a tax cut would not be recommended.” 

“If there was no trade deficit, a tax cut would not be recommended.” 

While the second example is closely related to the counterfactual:<sup>40</sup> 

“If the gram stain was negative or the morphology was 

not coccus, the algorithm would not be confident that the organism is Neisseria.” 

The most important difference between these approaches and counterfactuals is that counterfactuals continue functioning in an end-toend integrated approach. If the gram stain and morphology in the MYCIN example were also determined by the algorithm, counterfactuals would automatically return a close sample with a different classification, while these early methods could not be applied to such involved scenarios. 

> 38 BRUCE G. BUCHANAN & EDWARD D. SHORTLIFFE, RULE-BASED EXPERT SYSTEMS: THE MYCIN EXPERIMENTS OF THE STANFORD HEURISTIC PROGRAMMING PROJECT 344 (1984). 

> 39 _See, e.g._ , Gregor & Benbasat, _supra_ note 37, at 503. 

> 40 However, they are not logically equivalent. The example from MYCIN differs in that it is still possible that some samples that are either gram positive or have a different morphology could still be classified as Neisseria. 

12 _COUNTERFACTUAL EXPLANATIONS_ 

As focus has switched from A.I. and logic-based systems towards machine learning tasks such as image recognition, the notion of an explanation has come to refer to providing insight into the internal state of an algorithm, or to human-understandable approximations of the algorithm.<sup>41</sup> As such, the most related machine learning work to these, and to ours, is Martens and Provost.<sup>42</sup> Uniquely among other works in machine learning, it shares our interest in making interventions to alter the outcome of classifier responses. However, the work is firmly linked to the problem of document classification, and the only interventions it proposes involve the removal of words from documents to stop websites from being classified as “adult.”<sup>43</sup> The heuristic proposed cannot be easily generalised to either continuous variables,<sup>44</sup> or even the addition of words to documents. 

The majority of works in machine learning on explanations and interpreting models concern themselves with generating simple models as local approximations of decisions.<sup>45</sup> Generally, the idea is to create a simple human-understandable approximation of a decision-making algorithm that accurately models the decision given the current inputs, but may be arbitrarily bad for different inputs.<sup>46</sup> However, there are numerous difficulties with treating these approaches as explanations suitable for a lay data subject. 

In general, it is unclear if these models are interpretable by nonexperts. They make a three-way trade-off between the quality of the approximation, the ease of understanding the function, and the size of the domain for which the approximation is valid.<sup>47</sup> As we show in Appendix 1, these local models can produce widely varying estimates of the importance of variables even in simple scenarios such as the single 

> 41 Ribeiro et al., _supra_ note 14, at 1135–37. 

> 42 David Martens & Foster Provost, _Explaining Data-Driven Document Classifications_ , 

> 38 MIS Q. 73, 73–74 (2013). 

> 43 _Id_ . 

> 44 “Continuous variables” refers to variables whose assigned values are not restricted to a small set of discrete values: such as `present’ or `not present’, but instead can take any value in a given range.  Measurements such as height, weight, or how bright a particular pixel is in a photo, are often treated as continuous variables. See for example: <u>http://www.bbc.co.uk/schools/gcsebitesize/maths/statistics/samplinghirev1.shtml</u> 

> 45 Ribeiro et al., _supra_ note 14, at 1135; Selvaraju et al., _supra_ note 14, at 1–3; Simonyan et al., _supra_ note 14, at 1. 

> 46 _See_ Ribeiro et al., _supra_ note 14, at 1143; Selvaraju et al., _supra_ note 14, at 1–3; Simonyan et al., _supra_ note 14, at 1. 

> 47 Bastani et al., _supra_ note 13, at 1; Himabindu Lakkaraju et al., _Interpretable & Explorable Approximations of Black Box Models_ , AʀXɪᴠ:1707.01154, at 1 (2013), https://arxiv.org/pdf/1707.01154.pdf [https://perma.cc/6JFE-N4YD]. 

### 13 _COUNTERFACTUAL EXPLANATIONS_ 

variable case, making it extremely difficult to reason about how a function varies as the inputs change. Moreover, the utility of such approaches outside of model debugging by expert programmers is unclear. Research has yet to be conducted on how to convey the various limitations and unreliabilities of these approaches to a lay audience in such a way that they can make use of such explanations. 

In contrast, counterfactual explanations are intentionally restricted. They are crafted in such a way as to provide a minimal amount of information capable of altering a decision, and they do not require the data subject to understand any of the internal logic of a model in order to make use of it. The downside to this is that individual counterfactuals may be overly restrictive. A single counterfactual may show how a decision is based on certain data that is both correct and unable to be altered by the data subject before future decisions, even if other data exist that could be amended for a favourable outcome. This problem could be resolved by offering multiple diverse counterfactual explanations to the data subject. 

## _C. ADVERSARIAL PERTURBATIONS AND COUNTERFACTUAL EXPLANATIONS_ 

The techniques used to generate counterfactual explanations on deep networks such as resnet<sup>48</sup> are already widely studied in the machine learning literature under the name of “Adversarial Perturbations.”<sup>49</sup> In these works, algorithms capable of computing counterfactuals are used to confuse existing classifiers by generating a synthetic data point close to an existing one such that the new synthetic data point is classified differently than the original one.<sup>50</sup> 

One strength of counterfactuals is that they can be efficiently and effectively computed by applying standard techniques, even to cuttingedge architectures. Some of the largest and deepest neural networks are used in the field of computer vision, particularly in image labelling tasks 

> 48 _See_ He et al., _supra_ note 11, at 770. 

> 49 _See_ Ian J. Goodfellow, Jonathon Shlens & Christian Szegedy, _Explaining and Harnessing Adversarial Examples_ , ARXIV:1412.6572 , at 1 (2014), https://arxiv.org/pdf/1412.6572.pdf [https://perma.cc/64BR-WVE7]; Seyed-Mohsen Moosavi-Dezfooli, Alhussein Fawzi & Pascal Frossard, _Deepfool: A Simple and Accurate Method to Fool Deep Neural Networks_ , _in_ PROCEEDINGS OF THE IEEE CONFERENCE ON COMPUTER VISION AND PATTERN RECOGNITION 2574–82 (2016); Christian Szegedy et al., _Intriguing Properties of Neural Networks_ , ARXIV:1312.6199, at 2 (2013) , https://arxiv.org/pdf/1312.6199.pdf [https://perma.cc/K37R-6NP2]. 

> 50 _See_ Goodfellow, Shlens & Szegedy, _supra_ note 49, at 1; Moosavi-Dezfooli, Fawzi & Frossard, _supra_ note 49, at 2574–82; Szegedy et al., _supra_ note 49, at 2. 

### 14 _COUNTERFACTUAL EXPLANATIONS_ 

such as ImageNet.<sup>51</sup> These classifiers have been shown to be particularly vulnerable to a type of attack referred to as “Adversarial Perturbation” where small changes to a given image can result in the image being assigned to an entirely different class. For example, DeepFool<sup>52</sup> defines an adverse perturbation of an image _x_ , given a classifier, as the smallest change to _x_ such that the classification changes. Essentially, this is a counterfactual by a different name. Finding a closest possible world to _x_ such that the classification changes is, under the right choice of distance function, the same as finding the smallest change to _x_ . 

Importantly, none of the standard works on Adversarial Perturbations make use of appropriate distance functions, and the majority of such approaches tend to favour making small changes to many variables, instead of providing sparse human interpretable solutions that modify only a few variables.<sup>53</sup> Despite this, efficient computation of counterfactuals and Adversarial Perturbations is made possible by virtue of state-of-the-art algorithms being differentiable. Many optimisation techniques proposed in the Adversarial Perturbation literature are directly applicable to this problem, making counterfactual generation efficient. 

One of the more challenging aspects of Adversarial Perturbations is that these small perturbations of an image are barely human perceptible, but result in drastically different classifier responses.<sup>54</sup> Informally, this appears to happen because the newly generated images do not lie in the “space of real-images,” but slightly outside it.<sup>55</sup> This phenomenon serves as an important reminder that when computing counterfactuals by searching for a close possible world, it is at least as important that the solution found comes from a “possible world” as it is that it is close to the starting example. Further research into how data from high-dimensional and highly-structured spaces, such as natural images, can be characterised is needed before counterfactuals can be reliably used as explanations in these spaces. 

> 51 _See_ Jia Deng et al., _Imagenet: A Large-Scale Hierarchical Image Database_ , _in_ IEEE CONFERENCE ON COMPUTER VISION AND PATTERN RECOGNITION 248–55 (2009). 

> 52 _See_ Moosavi-Dezfooli, Fawzi & Frossard, _supra_ note 49, at 2574. 

> 53 _See_ Jiawei Su, Danilo Vasconcellos Vargas & Sakurai Kouichi, _One Pixel Attack for Fooling Deep Neural Networks_ , ARXIV:1710.08864, at 8–9 (2017), http://arxiv.org/abs/1710.08864 [https://perma.cc/5F2N-JBJF]. 

> 54 Niki Kilbertus et al., _Avoiding Discrimination through Causal Reasoning_ , ARXIV:1706,02744, at 1 (2017), https://arxiv.org/pdf/1706.02744.pdf [https://perma.cc/8GZQ-PRSJ]. 

> 55 _See generally_ Simant Dube, _High Dimensional Spaces, Deep Learning and Adversarial Examples_ , ARXIV:1801.00634 (2018), https://arxiv.org/pdf/1801.00634.pdf [https://perma.cc/8FE5-RY4X] (presenting preliminary investigation of this matter). 

15 _COUNTERFACTUAL EXPLANATIONS_ 

## _D. CAUSALITY AND FAIRNESS_ 

Several works have approached the problem of guaranteeing that algorithms are fair, i.e. that they do not exhibit a bias towards particular ethnic, gender, or other protected groups, using causal reasoning<sup>56</sup> and counterfactuals.<sup>57</sup> Kusner et al.<sup>58</sup> consider counterfactuals where the subject belongs to a different race or sex, and require that the decision made remain the same under such a counterfactual for it to be considered fair. In contrast, we consider counterfactuals in which the decision differs from its current state. 

Many works have suggested that transparency might be a useful tool for enforcing fairness. While it is unclear how counterfactuals could be used for this purpose, it is also unclear if any form of explanation of individual decisions can in fact help. Grgic-Hlaca et al.<sup>59</sup> showed how understandable models can easily mislead our intuitions, and that predominantly using features people believed to be fair slightly _increased_ the racism exhibited by algorithms, while decreasing accuracy. In general, the best tools for uncovering systematic biases are likely to be based upon large-scale statistical analysis and not upon explanations of individual decisions.<sup>60</sup> 

With that said, counterfactuals can provide evidence that an algorithmic decision is affected by a protected variable (e.g. race), and that it may therefore be discriminatory.<sup>61</sup> For the types of distance function we consider in the next section, if the counterfactuals found change someone’s race, then the treatment of that individual is dependent on race. However, the converse statement is _not_ true. Counterfactuals which do not modify a protected attribute cannot be used as evidence that the attribute was irrelevant to the decision. This is because counterfactuals describe only some of the dependencies between a particular decision and 

> 56 _See_ Kilbertus et al., _supra_ note 54, at 1. 

> 57 _See_ Matt J. Kusner et al., _Counterfactual Fairness_ , AʀXɪᴠ:1703.06856, at 16 (2017), https://arxiv.org/pdf/1703.06856.pdf [https://perma.cc/4SVN-7J9D]. 

> 58 _Id._ 

> 59 Nina Grgic-Hlaca et al., _The Case for Process Fairness in Learning: Feature Selection for Fair Decision Making_ , _in_ NIPS SYMPOSIUM ON MACHINE LEARNING AND THE LAW 8 (2016). 

> 60 _See_ Andrea Romei & Salvatore Ruggieri, _A Multidisciplinary Survey on Discrimination Analysis_ , 29 KNOWLEDGE ENGINEERING REV. 582, 617 (2014). 

> 61 Establishing the influence of a protected variable on a decision does not, by itself, prove that illegal discrimination has occurred. Mitigating factors may exist which justify the usage of a protected attribute. _See, e.g._ , Solon Barocas & Andrew D. Selbst, _Big Data’s Disparate Impact_ , 104 CAL. L. REV. 671, 676 (2016) (discussing disparate treatment in American anti-discrimination law). 

### 16 _COUNTERFACTUAL EXPLANATIONS_ 

specific external facts. This can be seen clearly in Section III.A, where the counterfactuals proposed for a particular classifier involve ‘black’ people changing their race, while not suggesting that ‘white’ people’s race should be varied. 

## III. GENERATING COUNTERFACTUALS 

In the following section, we give examples of how meaningful counterfactuals can be easily computed. Many of the standard classifiers of machine learning (including Neural Networks, Support Vector Machines, and Regressors) are trained by finding the optimal set of weights _w_ that minimises an objective over a set of training data. 



## Equation 1 

Where _yi_ is the label for data point _xi_ and _ρ(·)_ is a regularizer over the weights. We wish to find a counterfactual _x'_ as close to the original point _xi_ as possible such that _fw(x')_ is equal to a new target _y'._ We can find _x'_ by holding _w_ fixed and minimizing the related objective. 



## Equation 2 

Where _d_ (·,·) is a distance function that measures how far the counterfactual _x'_ and the original data point _xi_ are from one another. In practice, maximisation over λ is done by iteratively solving for _x'_ and increasing λ until a sufficiently close solution is found. 

The choice of optimiser for these problems is relatively unimportant. In practice, any optimiser capable of training the classifier under Equation 1 seems to work equally well, and we use ADAM<sup>62</sup> for all experiments. As local minima are a concern, we initialise each run with different random values for _x'_ and select as our counterfactual the best minimizer of Equation 2. These different minima can be used as a diverse set of multiple counterfactuals. 

> 62 Diederik Kingma & Jimmy Ba, _ADAM: A Method for Stochastic Optimization_ , ARXIV:1412.6980, at 1–4 (2014), https://arxiv.org/pdf/1412.6980.pdf [https://perma.cc/3RH4-WSXG]. 

### 17 _COUNTERFACTUAL EXPLANATIONS_ 

Of particular importance is the choice of distance function used to decide which synthetic data point _x'_ is closest to the original data point _xi_ . As a sensible first choice, which should be refined based on subject- and task-specific requirements, we suggest use of the _L1_ norm, or Manhattan distance, weighted by the inverse median absolute deviation. This is written as MAD _k_ for the median absolute deviation of feature _k,_ over the set of points _P_ : 



## Equation 3 

We chose _d_ (·,·) as: 



Equation 4 

This distance metric has several desirable properties. Firstly, it captures some of the intrinsic volatility of the space, which means that if a feature _k_ varies wildly across the dataset, a synthetic point _x'_ may also vary this feature while remaining close to _xi_ under the distance metric. The use of median absolute difference rather than the more usual standard deviation also makes this metric more robust to outliers. Of equal importance are the sparsity-inducing properties of the _L1_ norm. The _L1_ norm is widely recognised in mathematical and machine learning circles for its tendency to induce sparse solutions in which most entries are zero when paired with an appropriate cost function.<sup>63</sup> 

When computing human-understandable counterfactuals, this property is highly desirable as it corresponds to counterfactuals in which only a small number of variables are changed and most remain constant, making the counterfactuals much easier to communicate and comprehend. This metric works equally well on the examples we consider. 

To demonstrate the importance of the choice of distance function, we illustrate below the impact of varying _d(_ ·,· _)_ on the LSAT dataset. A further challenge lies in ensuring that the synthetic counterfactual _x'_ corresponds to a valid data point. We illustrate some of the pitfalls and 

> 63 _See, e.g._ , Emmanuel J. Candes, Justin K. Romberg & Terence Tao, _Stable Signal Recovery from Incomplete and Inaccurate Measurements_ , 59 COMM. PURE & APPLIED MATHEMATICS 1207, 1212 (2006). 

### 18 _COUNTERFACTUAL EXPLANATIONS_ 

remedies for dealing with discrete features when computing counterfactuals. 

## _A. LSAT DATASET_ 

We first consider the generation of counterfactuals on the LSAT<sup>64</sup> dataset. In particular, we consider a stripped-down version used in the fairness literature<sup>65</sup> that attempts to predict students’ first-year average grade on the basis of their race, grade-point average prior to law school, and law school entrance exam scores. This stripped-down version of the LSAT dataset is used in the fairness literature, as classifiers trained on this data naturally exhibit bias against ‘black’ people.<sup>66</sup> As a result, we will find evidence of this bias in our neural network in some of the counterfactuals we generate. 

We generate a three-layer fully-connected neural-network, with two hidden layers of 20 neurons each feeding into a final classifier. Even a small model like this has 941 different weights controlling its behaviour and 40 neurons that exhibit complex interdependencies, which makes conveying its internal state challenging. 

Choosing _d_ as the unweighted squared Euclidean distance 



## Equation 5 

we consider the Counterfactual, “What would have to be changed to give a predicted score of 0?”<sup>67</sup> Directly solving for Eq. 2 gives the results in the central block labelled “Counterfactuals” in Table 1. 



_Table 1 - Unnormalized L2_ 

> 64 _See_ R. Darrell Bock & Marcus Lieberman, _Fitting a Response Model for_ n _Dichotomously Scored Items_ , 35 PSYCHOMETRIKA 179, 187–96 (1970). 

> 65 _See, e.g._ , Chris Russell et al., _When Worlds Collide: Integrating Different Counterfactual Assumptions in Fairness_ , _in_ ADVANCES IN NEURAL INFORMATION PROCESSING SYSTEMS 6396–6405 (2017); Kusner et al., _supra_ note 57, at 9–12 

> 66 _See_ Russell et al., _supra_ note 65, at 6396–6405; Kusner et al., _supra_ note 57, at 10. 

> 67 The scores being predicted are normalised, with 0 corresponding to the average score. 

### 19 _COUNTERFACTUAL EXPLANATIONS_ 

Two artefacts are immediately apparent. The first is that although in this dataset, race is modelled using a discrete variable that can only take the labels 0 or 1, corresponding to ‘white’ or ‘black’ respectively, a variety of meaningless values, either fractional or negative, have been assigned to it. In the literature on adversarial perturbation, generally values are capped to lie within a sensible range such as [0,1] to stop some of these artefacts from occurring. However, this would still allow the fractional solutions shown in the bottom two examples. Instead, we clamp the race variable forcing it to take either value 0 or 1 in two separate run-throughs, and then take as a solution the closest counterfactual found in either of the runs. These results can be seen in the rightmost column “Counterfactual Hybrid.” The algorithm now suggests always changing the race to ‘white’ as part of the counterfactual. Of particular note is that the counterfactuals show that ‘black’ students would get better scores. 

The second artefact is that the algorithm much prefers significantly varying the GPA than the exam results, and this is down to our choice of distance function. We took as _d_ (·,·), the squared Euclidean distance, and this generally prefers changes that are as small as possible and spread uniformly across all variables. However, the range of the GPA is much smaller than that of the exam scores. Adjusting for this by normalising each component by its standard deviation, i.e. 



## Equation 6 

gives the set of counterfactuals shown in Table 2. 



_Table 2 - Normalised L2_ 

After normalisation, the GPA remains much more consistent, and naturally remains within an expected range of values. Note that for ‘black’ students, race does vary under the computed counterfactual, revealing a dependence between the decision and race (which is often a legally protected attribute). 

Finally, we show the use of the _L1_ norm weighted by the inverse median absolute deviation (Table 3). This returns similar but sparser 

### 20 _COUNTERFACTUAL EXPLANATIONS_ 

results to the weighted squared Euclidean distance, with the GPA not being changed under the counterfactuals. 



_Table 3 - Normalised L1_ 

These final Normalised _L1_ Hybrid Counterfactuals can be expressed in a more accessible text form that only describes the alterations to the original data: 

**Person 1:** If your LSAT was 34.0, you would have an average predicted score (0). 

- **Person 2:** If your LSAT was 32.4, you would have an average predicted score (0). 

**Person 3:** If your LSAT was 33.5, and you were ‘white’, 

you would have an average predicted score (0). 

**Person 4:** If your LSAT was 35.8, and you were ‘white’, 

you would have an average predicted score (0). 

**Person 5:** If your LSAT was 34.9, you would have an average predicted score (0). 

## _B. PIMA DIABETES DATABASE_ 

To demonstrate Counterfactuals on a more complex problem, we consider a database used to predict whether women of Pima heritage are at risk of diabetes.<sup>68</sup> We generate a classifier that returns a risk score between [0, 1] by training a similar three-layer fully-connected neural-network with two hidden layers of 20 neurons to perform logistic regression. This classifier takes as input 8 different variables of varying predictive power, including number of pregnancies, age and BMI. Counterfactuals are generated to answer the question “What would have to be different for this individual to have a risk score of 0.5?” To induce sparsity in the answer and generate counterfactuals that are easy for a human to evaluate, with only a small number of changed variables, we make use of the _L1_ norm, or Manhattan distance, weighted by the inverse median absolute 

> 68 Jack W. Smith et al., _Using the ADAP Learning Algorithm to Forecast the Onset of Diabetes Mellitus_ , PROC. ANN. SYMP. ON COMPUT. APPLICATION MED. CARE 261, 261– 62 (1988). 

### 21 _COUNTERFACTUAL EXPLANATIONS_ 

deviation, instead of the Euclidean distance. We also cap variables to prevent them from going outside the range seen in the training data. 

With this done, the counterfactuals typically vary from the original data only in a small number of variables, and these differences are automatically rendered in human readable text form. 

**Person 1:** If your 2-Hour serum insulin level was 154.3, 

you would have a score of 0.51. 

**Person 2:** If your 2-Hour serum insulin level was 169.5, you would have a score of 0.51. 

**Person 3:** If your Plasma glucose concentration was 158.3 and your 2-Hour serum insulin level was 160.5, you would have a score of 0.51. 

These counterfactuals are similar to the risk factors already used by doctors to communicate, e.g. “If your body mass index is greater than 40 you are morbidly obese, and at greater risk of ill-health.” However, counterfactuals may make use of multiple factors and convey a personalised risk model that takes into account other attributes that may mitigate or increase risk. 

## _C. CAUSAL ASSUMPTIONS AND COUNTERFACTUAL EXPLANATIONS_ 

The reader familiar with causal modelling may have noticed that our counterfactual explanations are not making use of causal models or equivalently, that they make naive assumptions that variables are independent of one another. There are several reasons for this. One important use of counterfactual explanations is to provide the data subject with information to make a guided audit of the data and check for relevant inaccuracies in the data. Treating such errors as independent and drawn from a robust distribution such as the Laplacian (corresponding to use of the _L1_ norm in our objective) is a sensible model for these errors. More importantly, creating and interpreting accurate causal models is difficult. Requiring data controllers to build and convey to a lay audience a causal model that accurately captures the interdependencies between measurements such as the number of pregnancies, age, and BMI is extremely challenging and may be irrelevant. 

Counterfactuals generated from an accurate causal model may ultimately be of use to experts (e.g., to medical professionals trying to 

### 22 _COUNTERFACTUAL EXPLANATIONS_ 

decide which intervention will move a patient out of an at-risk group). However, the purpose of our paper is to illustrate how far you can go with minimal assumptions and that such detailed causal models are unnecessary for counterfactual explanations to be of use. 

## IV. ADVANTAGES OF COUNTERFACTUAL EXPLANATIONS 

Counterfactual explanations differ markedly from existing proposals in the machine learning and legal communities (particularly regarding the GDPR’s “right to explanation”),<sup>69</sup> while offering several advantages. Principally, counterfactuals bypass the substantial challenge of explaining the internal workings of complex machine learning systems.<sup>70</sup> Even if technically feasible, such explanations may be of little practical value to data subjects. In contrast, counterfactuals provide information to the data subject that is both easily digestible and practically useful for understanding the reasons for a decision, challenging them, and altering future behaviour for a better result. 

The reduced regulatory burden of counterfactual explanations is also significant. Current state-of-the-art machine learning methods make decisions based upon deep networks that compose together functions more than a thousand times and with more than ten million parameters controlling their behaviour.<sup>71</sup> As the working memory of humans can contain around seven distinct items,<sup>72</sup> it remains unclear whether “humancomprehensible meaningful information” about the logic involved in a particular decision can ever exist, disregarding whether such information could be meaningfully conveyed to non-experts.<sup>73</sup> As such, regulations that require meaningful information regarding the internal logic to be 

> 69 Although a right to explanation is not itself legally binding, data subjects are entitled to receive “meaningful information about the logic involved, as well as the significance and the envisaged consequences” of automated decision-making under the GDPR's Art. 13–15. Wachter, Mittelstadt & Floridi, _supra_ note 1, at 16. Others have proposed that these provisions require the data subject to be given information about the internal logic and the rationale of specific decisions. The information sought aligns with the type of explanation pursued in the machine learning community. For an explanation of why such information is not legally required, and why Art. 13–15 do not constitute a de facto right to explanation, see Wachter, Mittelstadt & Floridi, _supra_ note 1, at 10–11, 14–19. 

> 70 Burrell, _supra_ note 5, at 9. 

> 71 _See generally_ Kaiming He et al., _Deep Residual Learning for Image Recognition_ , PROC. IEEE CONF. ON COMPUT. VISION & PATTERN RECOGNITION 770, 770–78 (2016); Gao Huang et al., _Deep Networks with Stochastic Depth_ , EUROPEAN CONF. ON COMPUT. VISION 646, 646–61 (2016). 

> 72 George A. Miller, _The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information_ , 63 PSYCHOL. REV. 81, 91 (1956). 

> 73 Burrell, _supra_ note 5, at 9. 

### 23 _COUNTERFACTUAL EXPLANATIONS_ 

conveyable to a lay audience could prohibit the use of many standard approaches. In contrast, counterfactual explanations do not attempt to convey the logic involved and, as shown in the previous section, are simple to compute and convey. 

Such expectations of providing information regarding the internal logic of algorithmic decision-making systems have surfaced recently in relation to the GDPR and in particular, the “right to explanation.” The GDPR contains numerous provisions requiring information to be communicated to individuals about automated decision-making.<sup>74</sup> Significant discussion has emerged in legal and machine learning communities regarding the specific requirements and limitations of the GDPR in this regard and in particular, how to provide information about decisions made by highly complex automated systems.<sup>75</sup> As counterfactuals provide a method to explain some of the rationale of an automated decision while avoiding the major pitfalls of interpretability or opening the “black box,” they may prove a highly useful mechanism to meet the explicit requirements and background aims of the GDPR. 

## V. COUNTERFACTUAL EXPLANATIONS AND THE GDPR 

Although the GDPR’s “right to explanation” is not legally binding, it has nonetheless connected discussion of data protection law to the longstanding question of how algorithmic decisions can be explained to experts as well as non-expert parties affected by the decision.<sup>76</sup> Answering this question largely depends upon the intended purpose of the explanation; the information to be provided must be tailored in terms of structure, complexity, and content with a particular aim in mind. Unfortunately, the GDPR does not explicitly define requirements for explanations of automated decision-making and provides few hints as to the intended purpose of explanations of automated decision-making.<sup>77</sup> Recital 71 of the GDPR, a non-binding provision and the only place where 

> 74 Regulation 2016/679 of Apr. 27, 2016, on the Protection of Natural Persons with Regard to the Processing of Personal Data and on the Free Movement of Such Data, and Repealing Directive 95/46/EC (General Data Protection Regulation) [hereinafter GDPR], GDPR, recitals 63 & 71 & arts. 13(2)(f), 14(2)(g), 15(1)(h) & 22, 2016 O.J. (L 119) 12, 14, 41, 42, 43, 46 (EU). 

> 75 _See generally_ Wachter, Mittelstadt & Floridi, _supra_ note 1; Mendoza & Bygrave, _supra_ note 1; Edwards & Veale, _supra_ note 1; Malgieri & Comandé, _supra_ note 1; Selbst & Powles, _supra_ note 1; Doshi-Velez et al., _supra_ note 15; Christopher Kuner et al., _Machine Learning with Personal Data: Is Data Protection Law Smart Enough to Meet the Challenge?_ , 7 INT’L DATA PRIVACY L. 1 (2017). 

> 76 _See_ Wachter, Mittelstadt & Floridi, _supra_ note 1, at 3–4. 

> 77 _See id._ at 42. 

### 24 _COUNTERFACTUAL EXPLANATIONS_ 

the word explanation is mentioned, states that suitable safeguards against automated decision-making should be implemented and “should include specific information to the data subject and the right to obtain human intervention, to express his or her point of view, to obtain an explanation of the decision reached after such assessment and to challenge the decision.”<sup>78</sup> 

This is the only time where an explanation is mentioned in the GDPR, leaving the reader with little insight into what type of explanation is intended or what purpose it should serve. Based on the text, the only clear indication is that legislators wanted to clarify that some type of explanation can voluntarily be offered _after_ a decision has been made. This can be seen as Recital 71 separates “specific information” which should be given before a decision is made,<sup>79</sup> from safeguards that apply _after_ a decision has been made<sup>80</sup> (“an explanation of the decision _reached after such assessment_ ” (emphasis added)).<sup>81</sup> Further indications are not provided of the intended content of such ex post explanations.<sup>82</sup> 

The content of an explanation must reflect its intended purpose. Given the lack of guidance in the GDPR, many aims for explanations are feasible. Reflecting the GDPR’s emphasis on protections and rights for individuals,<sup>83</sup> here we examine potential purposes for explanations from the perspective of the data subject. We propose three possible aims of 

> 78 Regulation 2016/679, GDPR, recital 71, 2016 O.J. (L 119) 14 (EU). 

> 79 Jörg Hladjk, _DS-GVO Art. 22 Automatisierte Entscheidungen im Einzelfall einschließlich Profiling_ , _in_ DATENSCHUTZ-GRUNDVERORDNUNG 529, 535 (Eugen Ehmann & Martin Selmayr eds., 1st ed. 2017). 

> 80 The European Parliament makes the same distinction (information obligations vs. explanations of automated decisions) in their draft report on civil law rules on robotics when referring to the GDPR. _See_ European Parliament Committee on Legal Affairs, _Draft Report with Recommendations to the Commission on Civil Law Rules on Robotics_ (Mar. 31, 2016), http://www.europarl.europa.eu/sides/getDoc.do?pubRef=//EP//NONSGML%2BCOMPARL%2BPE582.443%2B01%2BDOC%2BPDF%2BV0//EN [https://perma.cc/A2L8-FKMP]; 

> Sandra Wachter, Brent Mittelstadt & Luciano Floridi, _Transparent, Explainable, and Accountable AI for Robotics_ , 2 SCI. ROBOTICS 1, 1 (2017); Hladjk, _supra_ note 79 at 535– 36 (supporting this view that an explanation should be given after a decision has been taken, while recognising that this is not legally binding). 

> 81 Regulation 2016/679, GDPR, recital 71, 2016 O.J. (L 119) 14 (EU). 

> 82 _See generally_ European Commission, _Proposal for a Regulation of the European Parliament and the Council on the Protection of Individuals with Regard to the Processing of Personal Data and On the Free Movement of Such Data (General Data Protection Regulation)_ , COM (2012) 11 final (Jan. 25, 2012), http://ec.europa.eu/justice/data-protection/document/review2012/com_2012_11_en.pdf [https://perma.cc/6QSX-F4JX]. 

> 83 Christopher Kuner, _The European Commission’s Proposed Data Protection Regulation: A Copernican Revolution in European Data Protection Law_ , PRIVACY & SEC. L. REP. 1, 6–7, 8 (2012). 

### 25 _COUNTERFACTUAL EXPLANATIONS_ 

explanations of automated decisions: to enhance understanding of the scope of automated decision-making and the reasons for a particular decision, to help contest a decision, and to alter future behaviour to potentially receive a preferred outcome. This is not an exhaustive list of potential aims of explanations, but rather reflects how the recipient of an automated decision, as with any type of decision, may wish to understand its scope, effects, and rationale and take actions in response. In the following sections, we assess how these three purposes are reflected in the GDPR and the extent to which counterfactual explanations meet and exceed the GDPR’s requirements. 

## _A. EXPLANATIONS TO UNDERSTAND DECISIONS_ 

One potential purpose of explanations is to provide the data subject with understanding of the scope of automated decision-making, and the reasons that led to a particular decision. Several provisions in the GDPR can support a data subject’s understanding of automated decisionmaking, although the types of information that must be shared tend to enhance a broad understanding of automated decision-making systems, as opposed to the rationale of specific decisions.<sup>84</sup> As a result, the GDPR does not appear to require opening the “black box” to explain the internal logic of the decision-making system to data subjects. With this in mind, counterfactuals can provide information aligned with the GDPR’s various informational requirements, while also providing some insight into the reasons that led to a particular decision. Counterfactuals, thus, could meet and exceed the requirements of the GDPR. 

The description of explanations in Recital 71 does not include a requirement to open the “black box.”<sup>85</sup> Understanding the internal logic 

> 84 _See_ Wachter, Mittelstadt & Floridi, _supra_ note 1, at 5. 

> 85 _Id.; see also_ ARTICLE 29 DATA PROTECTION WORKING PARTY, GUIDELINES ON AUTOMATED INDIVIDUAL DECISION-MAKING AND PROFILING FOR THE PURPOSES OF REGULATION 2016/679 29 (2018), http://ec.europa.eu/newsroom/article29/document.cfm?doc_id=49826.  The Guidelines, which are very ambiguous, seem to support the claim that such a requirement is not only absent, but also might not have been intended. On the one hand transparency in how decisions are made (Recital 71) appears to be very important. _See_ Article 29 Data Protection Working Party, _Guidelines_ at 27. However, at the same time, the guidelines state that the aim of Art. 15(1)(h) is not to create individual explanations that require understanding the internal logic of the algorithm. _Id._ at 27. Hence, the guidelines suggest that Art. 15(1)(h) calls for information about general system functionality, as is the case with its counterparts in Art. 13(2)(f) and Art. 14(2)(g). This reading of Articles 13–15 would suggest that the Article 29 Working Party does not view non-binding Recital 71 as a requirement to explain the internal logic of individual decisions, as even the legally 

### 26 _COUNTERFACTUAL EXPLANATIONS_ 

of the algorithmic decision-making system is not explicitly required. Elsewhere, the GDPR contains transparency mechanisms,<sup>86</sup> notification duties,<sup>87</sup> and the right of access,<sup>88</sup> all of which create informational requirements concerning automated decision-making. Art. 13–15 describe what kind of information needs to be provided if data are collected, either immediately when collected from the data subject,<sup>89</sup> the latest after a month when collected from a third party,<sup>90</sup> or at any time if requested from the data subject.<sup>91</sup> Among other things, Art. 12 explains how this information (as defined in Art. 13–14) should be conveyed.<sup>92</sup> Art. 12–14 suggest that data subjects must be provided with “a meaningful overview of the intended processing,”<sup>93</sup> including “the existence of automated decision-making, including profiling, referred to in Art. 22(1) and (4) and, at least in those cases, meaningful information about the logic involved, as well as the significance and the envisaged consequences of such processing for the data subject,”<sup>94</sup> as opposed to a detailed explanation of the internal logic of a system after a decision has been made.<sup>95</sup> Rather they aim to offer a generic overview of intended processing activities, which enhances the data subject’s understanding of the scope and purpose of automated decision-making.<sup>96</sup> 

binding text in Article 15(1)(h), which is sufficiently vague to allow such an interpretation, _see_ Wachter, Mittelstadt & Floridi, _supra_ note 1, is not thought to create such a requirement. For further support that Recital 71 does not hinge on opening the black box, see Martini, _DS-GVO Art. 22 Automatisierte Entscheidungen im Einzelfall einschließlich Profiling, in_ DATENSCHUTZ-GRUNDVERORDNUNG Rn 35-37 (Paal & Pauly eds., 1st ed. 2017). 

86 Regulation 2016/679, GDPR, art. 12, 2016 O.J. (L 119) 39–40 (EU). 

87 Regulation 2016/679, GDPR, arts. 13 & 14, 2016 O.J. (L 119) 40–42 (EU). 

88 Regulation 2016/679, GDPR, art. 15, 2016 O.J. (L 119) 43 (EU). 

89 Regulation 2016/679, GDPR, art. 13–15, 2016 O.J. (L 119) 40–43 (EU). 

90 Regulation 2016/679, GDPR, art. 14, 2016 O.J. (L 119) 41–42 (EU). 

91 Regulation 2016/679, GDPR, art. 15, 2016 O.J. (L 119) 43 (EU). 

> 92 Dirk Heckmann & Anne Paschke, _DS-GVO Art. 12 Transparente Information, Kommunikation_ , _in_ DATENSCHUTZ-GRUNDVERORDNUNG 367, 370 (Eugen Ehmann & Martin Selmayr eds., 1st ed. 2017). 

93 Regulation 2016/679, GDPR, art. 12(7), 2016 O.J. (L 119) 40 (EU). 

94 Regulation 2016/679, GDPR, arts. 13(2)(f) & 14(2)(g), 2016 O.J. (L 119) 41, 42 (EU). 95 Lorenz Franck, _DS-GVO Art. 12 Transparente Information, Kommunikation_ , in DATENSCHUTZ-GRUNDVERORDNUNG VO (EU) 2016/679 316, 320 (Peter Gola ed., 1st ed. 2017); Sebastian Schulz, _DS-GVO Art. 22 Automatisierte Entscheidungen im Einzelfall_ , _in_ DATENSCHUTZ-GRUNDVERORDNUNG VO (EU) 2016/679 410, 418–19 (Peter Gola ed., 1st ed. 2017); Suzanne Rodway, _Just How Fair Will Processing Notices Need to Be Under the GDPR_ , 16 PRIV. & DATA PROT. 16, 16–17 (2016). 

> 96 _See_ Kuner, _supra_ note 75, at 2; ROSEMARY JAY, GUIDE TO THE GENERAL DATA PROTECTION REGULATION: A COMPANION TO DATA PROTECTION LAW AND PRACTICE 226 (4th Revised ed. 2017). 

### 27 _COUNTERFACTUAL EXPLANATIONS_ 

Art. 12(7) clarifies that the aim of Art. 13-14 is to provide “in an easily visible, intelligible and clearly legible manner, a _meaningful overview of the intended processing_ .”<sup>97</sup> Two requirements are notable: (1) that the information provided must be meaningful to its recipient and broad in scope (a “ _meaningful overview_ ”), and (2) that the notification occurs prior to processing (“ _intended_ processing”). 

To understand what would constitute a meaningful overview, the envisioned medium of disclosure is instructive. Broadly applicable information appears to be required, rather than personalised disclosures. Legal scholars have suggested that notification duties can be satisfied via updates to existing privacy statements or notices<sup>98</sup> (e.g. those displayed on websites or using QR codes).<sup>99</sup> This requirement does not change based on the form of data collection.<sup>100</sup> When data are collected from a third party,<sup>101</sup> an email sent to the data subject linking to the data controller’s privacy statement(s) could suffice.<sup>102</sup> The same holds true for personalised links<sup>103</sup> referring to the privacy notice. Tools similar to those currently used to make users aware of the usage of cookies or monitoring shopping behaviour can be envisioned to satisfy the requirements in Art. 14, thus making data subjects immediately aware of data collection.<sup>104</sup> Detailed information appears to not be necessary as Art. 12(7) states that the required information can be provided along with standardised icons.<sup>105</sup> In trilogue, the European Parliament proposed several standardised icons that were ultimately not adopted (see Appendix 2). Despite this, the proposed icons reveal the initial expectations of regulators for simple, easily understood information.<sup>106</sup> 

> 97 Regulation 2016/679, GDPR, art. 12(7), 2016 O.J. (L 119) 40 (EU) (emphasis added). 

> 98 _See, e.g.,_ ALAIN BENSOUSSAN, GENERAL DATA PROTECTION REGULATION: TEXTS, COMMENTARIES AND PRACTICAL GUIDELINES 113 (1st ed. 2017); Franck, _supra_ note 95, at 320; JAY, _supra_ note 96 at 223; Heckmann & Paschke, _supra_ note 92, at 375–76; Rainer Knyrim, _DS-GVO Art. 14 Informationspflicht bei Erhebung von Daten_ , _in_ DATENSCHUTZ-GRUNDVERORDNUNG 412, 417–18 (Eugen Ehmann & Martin Selmayr eds., 1st ed. 2017). 

> 99 Lorenz Franck, _DS-GVO Art. 13 Informationspflicht bei Erhebung von Daten_ , _in_ DATENSCHUTZ-GRUNDVERORDNUNG VO (EU) 2016/679 331, 338–39 (Peter Gola ed., 1st ed. 2017). 

> 100 Article 29 Data Protection Working Party, _supra_ note 85, at 25-6. 

> 101 Regulation 2016/679, GDPR, art. 14, 2016 O.J. (L 119) 41 (EU). 

> 102 Knyrim, _supra_ note 98, at 415–19. 

> 103 Franck, _supra_ note 95, at 322–23. 

> 104 Knyrim, _supra_ note 98, at 420. 

> 105 _Id._ at 417; ARTICLE 29 DATA PROTECTION WORKING PARTY, GUIDELINES ON TRANSPARENCY UNDER REGULATION 2016/679 (2017). 

> 106 The European Commission is tasked in Art. 12(8) to develop such icons. 

### 28 _COUNTERFACTUAL EXPLANATIONS_ 

These examples suggest Art. 13–14 aim to provide a general overview of data processing that will be meaningful to all data subjects involved (e.g., all users of Twitter). The captive audience is more likely to be the general public or user base, not individual users, and their unique circumstances.<sup>107</sup> This format of disclosure suggests notifications should be comprehensible to a general audience with mixed expertise and background knowledge. An “uneducated layperson” may be the envisioned audience for disclosures.<sup>108</sup> This coincides with the general notion of Art. 12(1) that all information and communication with the data subject has to be in a “concise, transparent, intelligible and easily accessible form,” suggesting in-depth technical information and ‘legalese’ would be inappropriate.<sup>109</sup> At a minimum, each provision suggests that information disclosures need to be tailored to their audience, with envisioned audiences including children and uneducated laypeople. 

Notifications regarding automated decision-making<sup>110</sup> face particular constraints within an overall “meaningful overview.” According to the Article 29 Working Party,<sup>111</sup> the UK Information Commissioner’s Office,<sup>112</sup> and other commentators,<sup>113</sup> informing the data subject about the “significance and envisaged consequences of automated decision-making” in a very simple manner, including “how profiling might affect the data subject generally, rather than information about a specific decision” will be sufficient.<sup>114</sup> For instance, an explanation of 

> 107 _See_ Regulation 2016/679, GDPR, recital 58, 2016 O.J. (L 119) 11 (EU); Heckmann & Paschke, _supra_ note 92, at 378. Note that this information can also be provided orally. _See_ JAY, _supra_ note 96, at 216–17 (noting this also but warning that data controllers carry the burden to prove that the information was communicated). 

> 108 Franck, _supra_ note 95, at 322 (noting this for the elderly, uneducated people, foreigners, or children); _see also_ Heckmann & Paschke, _supra_ note 92, at 376–77. 

> 109 JAY, _supra_ note 96, at 218; Heckmann & Paschke, _supra_ note 92, at 376; Article 29 Data Protection Working Party, _supra_ note 85, at 25-6. 

110 Regulation 2016/679, GDPR, art. 13(2), 14(2)(g), 2016 O.J. (L 119) 41–42 (EU). 

> 111 Article 29 Data Protection Working Party, _supra_ note 85. 

> 112 Info. Comm’r Office, _Feedback Request - Profiling and Automated Decision-making_ 15–16 (2017), https://ico.org.uk/media/about-the-ico/consultations/2013894/icofeedback-request-profiling-and-automated-decision-making.pdf [https://perma.cc/PC33-PUS8] Note the UK’s ICO is preparing new guidelines in the form of a living document, which will be continuously updated. See: UK’s Information Commissioner’s Office, RIGHTS RELATED TO AUTOMATED DECISION MAKING INCLUDING PROFILING (2018), https://ico.org.uk/for-organisations/guide-to-the-general-dataprotection-regulation-gdpr/individual-rights/rights-related-to-automated-decisionmaking-including-profiling/ (last visited Mar 18, 2018). 

> 113 _See, e.g.,_ Rodway, _supra_ note 95; Paal, _DS-GVO Art. 13 Informationspflicht bei Erhebung von personenbezogenen Daten bei der betroffenen Person_ , _in_ DATENSCHUTZGRUNDVERORDNUNG (Paal & Pauly eds., 1st ed. 2017). 

> 114 Info. Comm’r Office, _supra_ note 112, at 16. 

### 29 _COUNTERFACTUAL EXPLANATIONS_ 

how a low rating of creditworthiness can affect payment options,<sup>115</sup> how intended data processing may result in a credit or job application being declined,<sup>116</sup> or how driving behaviour might impact insurance premiums would be sufficient.<sup>117</sup> Similarly, “meaningful information about the logic involved” is said to require only “clarifying: of the categories of data used to create a profile; the source of the data; and why this data is considered relevant”<sup>118</sup> as opposed to a “detailed technical description about how an algorithm or machine learning works.”<sup>119</sup> 

This view is echoed in the Article 29 Working Party’s guidelines on automated individual decision-making. First the “right to explanation” is only mentioned once in the guidelines without any further details on scope or purpose. This “right” is clearly separated from the legally binding safeguards in Art. 22(3), implying that the Article 29 Working Party sees a difference in the legal standing of Recitals and legally binding provisions.<sup>120</sup> In fact, the guidelines does not even list the right to explanation in their “good practice suggestions” section.<sup>121</sup> Transparency about the fact that data controllers “are engaging in this type of activity,” referring to automated decision-making, is essential and the main goal of Art. 13 and 14. The aim of these articles is thus to provide ex ante information.<sup>122</sup> This is also evident in the fact that the guidelines states that the phrase ‘significance’ and ‘envisaged consequences’ means “that information must be provided about intended or future processing, and how the automated decision-making might affect the data subject.”<sup>123</sup> Elsewhere, the guidelines state that “details of the main characteristics considered in reaching the decision, the source of this information and the 

> 115 Paal, _supra_ note 113 at Rn. 31-32; Info. Comm’r Office, _supra_ note 112, at 16. 

> 116 Rodway, _supra_ note 95, at 2. 

> 117 Article 29 Data Protection Working Party, _supra_ note 85, at 26. 

> 118 Info. Comm’r Office, _supra_ note 112, at 15. 

> 119 _Id. See also_ Eugen Ehmann, _DS-GVO Art. 15 Auskunftsrecht der betroffenen Person_ , _in_ DATENSCHUTZ-GRUNDVERORDNUNG, 430–31 (Eugen Ehmann & Martin Selmayr eds., 1st ed. 2017) (arguing that Art. 15 only entitles the data subject to know about the abstract logic and principles of data processing, but not the formula or code). Reference is made to Recital 63 in the English and French versions of the GDPR to support this claim. _See also_ Article 29 Data Protection Working Party, _supra_ note 85, at 25 (“The controller should find simple ways to tell the data subject about the rationale behind, or the criteria relied on in reaching the decision without necessarily always attempting a complex explanation of the algorithms used or disclosure of the full algorithm.”). 

> 120 ARTICLE 29 DATA PROTECTION WORKING PARTY, _supra_ note 88 at 27. 

> 121 _Id._ at 32. 

> 122 _Id._ at 25. 

> 123 _Id._ at 26. Further the guidelines state that data controllers can voluntary “to explain how a past decision has been made” which indicates the this is the exception to the rule. 

### 30 _COUNTERFACTUAL EXPLANATIONS_ 

relevance” should be provided under Art 13–14.<sup>124</sup> Further, the “controller should find simple ways to tell the data subject about the rationale behind, or the criteria relied on in reaching the decision. The GDPR requires the controller to provide meaningful information about the logic involved, not necessarily a complex explanation of the algorithms used or disclosure of the full algorithm.”<sup>125</sup> 

However, it must be noted that this requirement, despite referring to the decision-making rationale, seems to refer to general system functionality rather than an explanation of an individual decision.<sup>126</sup> The guidelines state that Art 15(1)(h), which is seen to provide identical information as Art 13(2)(f) and 14(2)(g),<sup>127</sup> requires the data controller to “provide the data subject with information about the envisaged consequences of the processing, rather than an explanation of a particular decision.”<sup>128</sup> The is further supported as the guidelines state that “meaningful information about the logic involved“ means that “Instead of providing a complex mathematical explanation about how algorithms or machine-learning work, the controller should consider using clear and comprehensive ways to deliver the information to the data subject, for example: the categories of data that have been or will be used in the profiling or decision-making process; why these categories are considered pertinent; how any profile used in the automated decision-making process is built, including any statistics used in the analysis; why this profile is relevant to the automated decision-making process; and how it is used for a decision concerning the data subject.”<sup>129</sup> 

Overall, according to the Article 29 Working Party, the aim of Articles 13-15 is to demonstrate how automated processes help data controllers to make more accurate, unbiased, and responsible decisions and illustrate how the data, characteristics, and method used are suitable to achieve this goal.<sup>130</sup> In other words, the process of decision-making and the algorithm itself do not need to be fully disclosed, but rather a 

> 124 _Id._ at 26. 

> 125 _Id._ at 25. 

> 126 For an in-depth analysis between systems functionality and rationale of a decision see Wachter, Mittelstadt & Floridi, _supra_ note 1. 

> 127 _See_ ARTICLE 29 DATA PROTECTION WORKING PARTY, _supra_ note 88 at 26. 

> 128 _Id._ at 27. “The controller should provide the data subject with general information (notably, on factors taken into account for the decision-making process, and on their respective ‘weight’ on an aggregate level) which is also useful for him or her to challenge the decision” is given as an example showing that only information about system functionality will be required. 

> 129 ARTICLE 29 DATA PROTECTION WORKING PARTY, _supra_ note 88 at 31. 

> 130 _See id._ at 26. 

### 31 _COUNTERFACTUAL EXPLANATIONS_ 

description of the logic of the algorithm which may include a list of data sources or variables.<sup>131</sup> This position finds further support in the Working Party’s guidelines on transparency,<sup>132</sup> which state that the notification duties in Art. 13-14 can be satisfied via standardised privacy notices, visualisation tools, and icons. 

Each disclosure under Art. 13–14 must occur prior to data processing<sup>133</sup> or at the time of data collection, but before automated decision-making starts.<sup>134</sup> Evidence of this is seen in the future-oriented language used in Art. 13(2)(f) and Art. 14(2)(g),<sup>135</sup> the obligation for information about the necessity of providing data for processing,<sup>136</sup> the clarification in Art. 12(7) that information must be provided about “intended processing,” the Article 29 Working Party’s guidelines on transparency,<sup>137</sup> and other provisions and jurisprudence.<sup>138</sup> For automated 

> 131 Paal, _supra_ note 113, at Rn. 31-32 (seeing no difference between Art 13-15 in terms what kind of information needs to be provided). _See also_ Paal, _DS-GVO Art. 15 Auskunftsrecht der betroffenen Person_ , _in_ DATENSCHUTZ-GRUNDVERORDNUNG, Rn. 31 (Paal & Pauly eds., 1st ed. 2017). Further support is offered by the text of Recital 51 proposed by the European Parliament during Trilogue, which referred to “the general logic of the data that are undergoing the processing and what might be the consequences of such processing.” European Parliament Committee on Civil Liberties, Justice and Home Affairs, _Report on the Proposal for a Regulation of the European Parliament and of the Council on the Protection of Individuals with Regard to the Processing of Personal Data and on the Free Movement of Such Data (General Data Protection Regulation)_ A7-0402/2013, 21 (Nov. 21, 2013), http://www.europarl.europa.eu/sides/getDoc.do?type=REPORT&reference=A7-20130402&language=EN [https://perma.cc/27B4-5PWC]. 

> 132 ARTICLE 29 DATA PROTECTION WORKING PARTY, _supra_ note 108. 

> <sup>133</sup> Regulation 2016/679, GDPR, art. 12(7), 2016 O.J. (L 119) 40 (EU). 

> 134 _See_ Wachter, Mittelstadt & Floridi, _supra_ note 1, at 15; _see also_ Franck, _supra_ note 99; Knyrim, _supra_ note 98; JAY, _supra_ note 95, at 225 (arguing that the notification duties in Art. 13 need to apply _before_ the data is collected); Franck, _supra_ note 95 at 328 (linking this to Art. 13(2)(e) that obligates the data controllers to state “whether the provision of personal data is a statutory or contractual requirement, or a requirement necessary to enter into a contract, as well as whether the data subject is obliged to provide the personal data and of the possible consequences of failure to provide such data.”). Information about the necessity to provide data must therefore be given before the data is collected. _See also_ Article 29 Data Protection Working Party, _supra_ note 85, at 12-3. 

> 135 _See_ Wachter, Mittelstadt & Floridi, _supra_ note 1, at 15; Frederike Kaltheuner & Elettra Bietti, _Data is power: Towards additional guidance on profiling and automated decision-making in the GDPR_ , 2 J. INF. RIGHTS POLICY PRACT. (2018), https://journals.winchesteruniversitypress.org/index.php/jirpp/article/view/45 (last visited Mar 18, 2018). 

136 Regulation 2016/679, GDPR, art. 13(2)(e), 2016 O.J. (L 119) 41 (EU). 

> 137 ARTICLE 29 DATA PROTECTION WORKING PARTY, _supra_ note 108 at 14 state that “Articles 13 and 14 set out information which must be provided to the data subject at the commencement phase of the processing cycle.” 

> 138 _See_ Rainer Knyrim, _DS-GVO Art. 13 Informationspflicht bei Erhebung von Daten_ , _in_ DATENSCHUTZ-GRUNDVERORDNUNG 391, 411–12 (Eugen Ehmann & Martin Selmayr eds., 1st ed. 2017); Knyrim, _supra_ note 98, at 418–19 (noting that prior notification is 

### 32 _COUNTERFACTUAL EXPLANATIONS_ 

decision-making, it is essential that information is provided before the start, else the right not to be subject of an automated decision can never be realised. The data subject has no chance to assess the associated risks,<sup>139</sup> or whether one of the grounds in Art. 22(2) actually apply that allow automated decision-making. Under Art. 22(2), automated decisionmaking is only lawful if it “is necessary for entering into, or performance of, a contract between the data subject and a data controller,”<sup>140</sup> if it is authorised by Member State law,<sup>141</sup> or if the data subject has given explicit consent.<sup>142</sup> If notifications do not occur prior to processing or decision-making, data subjects would only be able to contest decisions after the fact. This can be time and cost intensive, and unable to repair financial or reputational damage. Hence, one purpose of Art. 13–14 is to make the data subject aware of future processing<sup>143</sup> and to allow them to decide if they want their data to be processed (e.g., consent),<sup>144</sup> assess the legitimacy (based on Member State law or contract), or exercise other rights in the GDPR.<sup>145</sup> 

## 1. Broader possibilities with the right of access 

The requirement for notification prior to processing applies only to the notification duties.<sup>146</sup> In contrast, the right of access<sup>147</sup> can be invoked at any time by the data subject, opening up the possibility of providing 

also in line with the Bara and others judgment of the ECJ (C-201/14; 1.10.2015) which will have major implication for the GDPR as it shows that the court views prior notification of data transfer as essential). The ruling said that when information is gathered from a third party and transferred to another data controller for further processing (e.g. based on Member State law) prior notification of the data subject — even if no consent is required — is essential. Not least because it enables the exercise of Art. 15 (right of access) and Art. 16 (right to data rectification) as soon as data is collected. 

> 139 _See_ Article 29 Data Protection Working Party, _supra_ note 85, at 24-5. 

140 Regulation 2016/679, GDPR, art. 22(2)(a), 2016 O.J. (L 119) 46 (EU). 

141 Regulation 2016/679, GDPR, art. 22(2)(b), 2016 O.J. (L 119) 46 (EU). 

142 Regulation 2016/679, GDPR, art. 22(2)(c), 2016 O.J. (L 119) 46 (EU). 

> 143 Franck, _supra_ note 95, at 326–28. 

144 On the importance to inform the data subject accurately (e.g., risks, safeguards, rights, consequences, etc.) to allow for informed/explicit consent, _see generally_ JAY, _supra_ note 96, at 218; Heckmann & Paschke, _supra_ note 92, at 374–75; Schulz, _supra_ note 95, at 418–19; Article 29 Data Protection Working Party, _supra_ note 85, at 12-3. 

> 145 _See_ Article 29 Data Protection Working Party, _Opinion 10/2004 on More Harmonised Information Provisions_ (Nov. 25, 2004), http://www.statewatch.org/news/2004/dec/wp100.pdf [https://perma.cc/Y2DW-4F9Q] (describing the need to provide meaningful information (to raise awareness) about data collection and the need to move away from long privacy statements); _see also_ Heckmann & Paschke, _supra_ note 92, at 388–89. 

- 146 Regulation 2016/679, GDPR, arts. 13 & 14 2016 O.J. (L 119) 40–42 (EU). 

- 147 Regulation 2016/679, GDPR, art. 15, 2016 O.J. (L 119) 43 (EU). 

### 33 _COUNTERFACTUAL EXPLANATIONS_ 

information available after a decision has been made (i.e., the reasons for a specific decision). However, scholars have argued that the information supplied via notification duties and the right of access is largely identical, meaning the right of access is similarly limited in terms of the scope of “meaningful information about the logic involved as well as the significance and the envisaged consequences.”<sup>148</sup> Information can thus largely be provided with identical tools (e.g., generic icons, privacy statements)<sup>149</sup> or generic templates<sup>150</sup> used for both notification and in response to access requests. 

The narrower interpretation appears to be correct.<sup>151</sup> The Article 29 Working Party supports this view, explaining that the information requirements in Art. 13(2)(f), 14(2)(g), and 15(1)(h) are identical,<sup>152</sup> while Art. 15(1)(h) requires “that the controller should provide the data subject with information about the envisaged consequences of the processing, rather than an explanation of a particular decision.”<sup>153</sup> A similar argument has been made by the ICO stating that Art. 13–15 aim to “provide information about how profiling might affect the data subject generally, rather than information about a specific decision.”<sup>154</sup> Additionally, the GDPR indicates a restricted scope for the right of access when compared to Art. 13–14. Personal data of other data subjects must not be disclosed, as this could infringe their privacy. Access requests can also contravene trade secrets or intellectual property rights (Art. 15(4) and Recital 63), meaning an appropriate balance between the data subject and controller’s interests must be struck.<sup>155</sup> 

> 148 Regulation 2016/679, GDPR, art. 15(1)(h), 2016 O.J. (L 119) 43 (EU). 

> 149 Paal, _supra_ note 131, at Rn. 31; Franck, _supra_ note 95, at 328; Lorenz Franck, _DSGVO Art. 15 Auskunftsrecht der betroffenen Person_ , _in_ DATENSCHUTZGRUNDVERORDNUNG VO (EU) 2016/679 348, 349–50 (Peter Gola ed., 1st ed. 2017); Heckmann & Paschke, _supra_ note 92, at 382–83. 

> 150 Franck, _supra_ note 95, at 320 argues templates will be helpful, because as soon as Art. 15 is lodged data controllers have to inform about all the information in Art. 15, regardless of the actual request. _See also_ Ehmann, _supra_ note 119, at 431–32. 

> 151 _See_ Wachter, Mittelstadt & Floridi, _supra_ note 1; Michael Veale & Lilian Edwards, _Clarity, Surprises, and Further Questions in the Article 29 Working Party Draft Guidance on Automated Decision-Making and Profiling_ , COMPUT. L. & SECURITY REV. (forthcoming 2018) (manuscript at 3), https://papers.ssrn.com/abstract=3071679 [https://perma.cc/Z37Z-TM3W]. 

> 152 Article 29 Data Protection Working Party, _supra_ note 85, at 26-7. 

> 153 _Id._ at 27. 

> 154 The intention of Art. 15 is to provide a control mechanism for data subjects to request at any time more or less the same information as Art. 13–14, without having to rely on legal compliance with the notification duties by data controllers. Ehmann, _supra_ note 119, 426–427; Info. Comm’r’s Office, _supra_ note 112, at 16. 

> 155 Franck, _supra_ note 149, 355; Ehmann, _supra_ note 119, at 434–435. 

### 34 _COUNTERFACTUAL EXPLANATIONS_ 

## 2. Understanding through counterfactuals 

Counterfactual explanations meet and exceed the aims and requirements of the GDPR’s transparency mechanisms<sup>156</sup> , notification duties<sup>157</sup> , and right of access<sup>158</sup> , which provide data subjects with information to understand the scope of automated decision-making. As argued above, Recital 71 does not give any clear indication of the intended purpose or content of explanations, including whether the internal logic of the algorithm must be explained. By providing simple “if-then” statements, counterfactuals align with the requirement to communicate information to data subjects in a “concise, transparent, intelligible and easily accessible form.”<sup>159</sup> They simultaneously provide greater insight into the data subject’s personal situation and the reasons behind relevant automated decisions than an overview tailored to a general audience. Counterfactuals are also less likely to infringe on trade secrets or the rights and freedoms of others (e.g., privacy), since no data of other data subjects or detailed information about the algorithm needs to be disclosed, in line with restrictions on the right of access.<sup>160</sup> 

Perhaps most importantly, counterfactuals offer an explanation of some of the rationale of specific automated decisions, without needing to explain the internal logic of how a decision was reached (beyond a specific, limited set of dependencies between variables and the decision). This type of information is in line with the guidance mentioned above from the Article 29 Working Party<sup>161</sup> and the UK’s ICO.<sup>162</sup> While opening the black box is not legally required, some information about the “logic involved” in automated decision-making must be provided.<sup>163</sup> Under the Data Protection Directive’s right of access, disclosing the algorithm’s source code, formula, weights, full set of variables, and information about reference groups has generally not been required.<sup>164</sup> The GDPR’s right of access is likely to present similar requirements. Counterfactuals largely follow this precedent by disclosing only the influence of select external 

> 156 Regulation 2016/679, GDPR, art. 12, 2016 O.J. (L 119) 39–40 (EU). 

> 157 Regulation 2016/679, GDPR, arts. 13 & 14, 2016 O.J. (L 119) 40–42 (EU). 

> 158 Regulation 2016/679, GDPR, art. 15, 2016 O.J. (L 119) 43 (EU). 

> 159 Regulation 2016/679, GDPR, art. 12(1), 2016 O.J. (L 119) 39 (EU). 

> 160 _See_ Regulation 2016/679, GDPR, recital 63 & art. 15(4), 2016 O.J. (L 119) 12, 43 (EU). 

> 161 _See generally_ Article 29 Data Protection Working Party, _supra_ note 85. 

> 162 _See generally_ Info. Comm’r’s Office, _supra_ note 112. 

> 163 _See_ Regulation 2016/679, GDPR, arts. 13(2)(f), 14(2)(g) & 15(1)(h), 2016 O.J. (L 119) 41–43 (EU). 

> 164 For an in-depth analysis of this jurisprudence, see generally Wachter, Mittelstadt & Floridi, _supra_ note 1. 

### 35 _COUNTERFACTUAL EXPLANATIONS_ 

facts and variables on a specific decision. Although Art. 13(2)(f), Art. 14(2)(g), and Art. 15(1)(h) do not require information about specific decisions,<sup>165</sup> counterfactuals represent a minimal form of disclosure to inform the data subject about the “logic involved” in specific decisions. This form of disclosure regulatory burden for data controllers is minimised, as resolving the technical difficulties of interpretability or explaining the internal logic of complex systems to non-experts is not required to compute and communicate counterfactual explanations. Counterfactuals can thus be recommended as a minimally burdensome and disruptive technique to help data subjects understand the rationale of specific decisions beyond the explicit legal requirements of Art. 13(2)(f), Art. 14(2)(g), and Art. 15(1)(h). 

## _B. EXPLANATIONS TO CONTEST DECISIONS_ 

Another possible purpose of explanations is to provide information that helps contest automated decisions when an adverse or otherwise undesired decision is received. A right to contest decisions is provided as a safeguard against automated decision-making in Art. 22(3). 

Contesting a decision can aim to reverse or nullify the decision and return to a status where no decision has been made, or to alter the result and receive an alternative decision. If the reasons that led to a decision need to be explained, the affected party can assess whether these reasons were legitimate and contest the assessment as required. 

How a decision can be contested depends on whether the safeguards in Art. 22(3) (i.e., rights to obtain human intervention, express views, and contest the decision) are interpreted as a unit that must be invoked together, or as individual rights that can be invoked separately or in any possible combination.<sup>166</sup> To gauge the scope of explanations according to their purpose and aim, different possible models for contesting an automated decision need to be assessed. 

Four models are possible. If the safeguards are a unit and must be invoked together, it is likely that some human involvement is necessary to issue a new decision. This could either be a human making the decision without any algorithmic help, hence the new result is a human decision rather than an automated decision. Alternatively, a person could be required to make a decision taking the algorithmic assessment and/or the data subject’s objections into account, which would be human assessment 

> 165 _See_ Article 29 Data Protection Working Party, _supra_ note 85, at 26-7. 

> 166 _See_ Martini, _supra_ note 85. 

### 36 _COUNTERFACTUAL EXPLANATIONS_ 

with algorithmic elements. In both cases data subjects would lose their safeguards against the subsequent decision, as both types of decision are not based “solely on automated processing” and thus do not meet the definition of automated individual decisions in Art. 22(1).<sup>167</sup> Another possibility is that a person could be required to monitor the input data and processing (e.g., based on the data subject’s objections), with a new decision made solely by the algorithmic system. In this case the Art. 22(3) safeguards still apply to the new decision.<sup>168</sup> Finally, if the safeguards can be separated, and data subjects can invoke their right to contest the decision without invoking their right to obtain human intervention or express their views, a new decision could be issued with no human involvement. This decision could be contested again under Art. 22(3). It is unclear which of these models will be preferred following implementation of the GDPR.<sup>169</sup> 

The question remains what explanations would be helpful to contest decisions. This will depend on the contesting model. The first model where a human makes a new decision and disregards everything the algorithm suggested, an explanation of the rationale of the original decision could be informative, but will not practically impact the new decision made entirely by a human decision-maker. For each of the other models, where algorithmic involvement is envisioned, an explanation of the rationale of the decision could be helpful to identify potential grounds 

> 167 Regulation 2016/679, GDPR, art. 22, 2016 O.J. (L 119) 46 (EU). 

> 168 However, if the new automated decision is communicated to the data subject by a person, it may not be considered “solely automated” and not subject to the Art 22(3) safeguards. The precise limitations on “solely automated” in Art 22(1) remain unclear. _See also_ Article 29 Data Protection Working Party, _supra_ note 85, at 10 (explaining that fabricated human involvement should not be used as a loophole). 

> 169 Either interpretation is possible, as indicated by the European Parliament's proposal to add the following text to Article 20 in an earlier draft of the GDPR, “[t]he suitable measures to safeguard the data subject's legitimate interests referred to in paragraph 2 shall include the right to obtain human assessment and an explanation of the decision reached after such assessment.” This text clarified that a human would need to assess the decision in question. However, this text was not adopted in the end, which leaves implementation of any of the four models possible. With that said, treating the safeguards as individually enforceable may be the most sensible option. Individuals can have an interest in expressing their views or obtaining human intervention when a decision is poorly understood or misunderstood. Both interests do not, however, necessarily lead to challenging the decision, particularly if challenges are costly or have a low likelihood of success. 

### 37 _COUNTERFACTUAL EXPLANATIONS_ 

for contesting, such as inaccuracies in the input data, problematic inferences, or other flaws in the algorithmic reasoning.<sup>170</sup> 

Even though an explanation of the rationale of a decision could be helpful to contest decisions, it does not imply an explanation is required by the GDPR or is the intended aim of the non-binding right to explanation.<sup>171</sup> Recital 71 does not specify the aim of the right or what information should be revealed, and does not explicitly require the algorithm’s internal logic to be explained. An explicit link is not established in the GDPR between the right to explanation and the right to contest, wherein the former would provide information necessary to exercise the latter.<sup>172</sup> Further, there is no reason to assume that the safeguards in Art. 22(3) must be exercised together, rather than independently of one another. Therefore, explanations under Recital 71 are not a necessary precondition to contest unfavourable decisions, even though this might be helpful. 

Similarly, an explicit link has not been made between the right to contest and the transparency mechanisms,<sup>173</sup> notification duties,<sup>174</sup> right of access,<sup>175</sup> meaning the information provided through these rights and duties need not be explicitly tailored to help data subjects successfully contest decisions.<sup>176</sup> 

Nonetheless, information provided by Art. 12–15 may be helpful for contesting. Support is evident in the fact that notification duties aim to facilitate the exercise of other rights in the GDPR to increase individual control over personal data processing.<sup>177</sup> To achieve this, Art. 13(2)(b), 14(2)(c), and 15(1)(e) obligate data controllers to inform data subjects 

> 170  Brent Mittelstadt et al., _The Ethics of Algorithms: Mapping the Debate_ , BIG DATA SOC. (2016), http://bds.sagepub.com/lookup/doi/10.1177/2053951716679679 

> [ <mark>https://perma.cc/YB4Y-9MXD]</mark> . 

> 171 _See_ Regulation 2016/679, GDPR, recital 71, 2016 O.J. (L 119) 14 (EU). 

> 172 _See_ Hladjk, _supra_ note 79, at 535–536; Schulz, _supra_ note 95, 419–420 (arguing that 

> “contesting” and “explaining” the decision are separate and independent safeguards). 

> 173 Regulation 2016/679, GDPR, art. 12, 2016 O.J. (L 119) 39–40 (EU). 

> 174 Regulation 2016/679, GDPR, arts. 13 & 14, 2016 O.J. (L 119) 40–42 (EU). 

> 175 Regulation 2016/679, GDPR, art. 15, 2016 O.J. (L 119) 43 (EU). 

> 176 At the same time, the Article 29 Data Protection Working Party argues that transparency in processing is essential to contesting, and that the reasons for the decisions and the legitimate basis should be known. _See_ Article 29 Data Protection Working Party, _supra_ note 85, at 27. However, the guidelines leave open whether this requires opening the black box and disclosing the algorithm. _See id._ This seems unlikely as the guidelines state that not even Art. 15(1)(h) aims to offer an explanation about an individual decision. _See id._ at 27. Hence it can be assumed that the information provided does not need to include an explanation of the internal logic of a specific decision. 

> 177 _See_ Regulation 2016/679, GDPR, art. 12(2), 2016 O.J. (L 119) 40 (EU). 

### 38 _COUNTERFACTUAL EXPLANATIONS_ 

about their rights in Art. 15–21<sup>178</sup> at the time when the data is collected,<sup>179</sup> within one month when obtained from a third party,<sup>180</sup> or at any time if requested by the data subject.<sup>181</sup> However, Art. 22 appears not to be covered by these provisions due to the odd phrasing of the obligation to inform of “the existence of automated decision-making, including profiling, referred to in Art. 22(1) and (4) and, at least in those cases, meaningful information about the logic involved, as well as the significance and the envisaged consequences of such processing for the data subject.”<sup>182</sup> 

As argued above, Art. 13–15 will provide a meaningful overview of automated decision-making tailored to a general audience. On the surface, such an overview is not immediately useful for contesting decisions, as information about the rationale of individual decisions is not provided. In describing information to be provided about automated decision-making, these Articles explicitly refer only to Art. 22(1) and (4). It follows that data subjects do not need to be informed about the safeguards against automated decision-making such as the right to contest.<sup>183</sup> This limitation is telling. If the aim of Art. 13–15 were to facilitate contesting decisions by providing useful, individual-level information, one would expect the right to contest or Art. 22(3) to be explicitly discussed. Similarly, Art. 13–15 seem not require to inform the data subject about their right not to be subject to an automated individual decision,<sup>184</sup> from which a right to contest decisions could be inferred.<sup>185</sup> 

> 178 _See_ Regulation 2016/679, GDPR, art. 15, 2016 O.J. (L 119) 43 (EU). If invoked via Art. 15(1)(e), data controllers only have to inform about the rights enshrined in Art. 16, 17, 18, 19, and 21. 

> 179 Regulation 2016/679, GDPR, art. 13, 2016 O.J. (L 119) 40–41 (EU). 

> 180 Regulation 2016/679, GDPR, art. 14(3)(a), 2016 O.J. (L 119) 42 (EU). 

> 181 Regulation 2016/679, GDPR, art. 15, 2016 O.J. (L 119) 43 (EU). 

> 182 Regulation 2016/679, GDPR, art. 15(1)(h), 2016 O.J. (L 119) 43 (EU). 

> 183 _See_ Regulation 2016/679, GDPR, art. 22(3), 2016 O.J. (L 119) 46 (EU); Schulz, _supra_ note 95, 419–420 (arguing that data controllers only have to inform about the safeguards after an adverse decision has been issued). In fact, Art. 12(3) introduces a very complicated model where the data controller has to inform upon request what kind of measures have been taken to satisfy a request under Art. 15–22, without being informed about the safeguards beforehand. _See also_ , Martini, _supra_ note 85, at Rn. 39–40 (also acknowledging this loophole). 

> 184 _See_ Regulation 2016/679, GDPR, art. 22(1), 2016 O.J. (L 119) 46 (EU). 

185 It is important to note that Art. 13–15 obligate to inform about the general right to object to processing (which forces data controllers to stop processing) in Art. 21. Together with the information about the legitimate basis for processing provided in Art. 13(1)(c) and Art. 14(1)(c), this information could be used to contest decisions. However, this arrangement may place an unreasonable burden on the data subject. Contesting should be made as easy as possible, not least because the chances of successfully forcing the data controller to stop processing under Art. 21 are different from under Art. 22. For 

### 39 _COUNTERFACTUAL EXPLANATIONS_ 

In fact, in an earlier draft of the GDPR it was suggested that the information rights should refer to Art. 20 as a whole.<sup>186</sup> Ultimately, this approach was not adopted, suggesting that the lack of useful information for contesting decisions was intentional. 

This lack of an explicit link to the safeguards against automated decision-making is in many ways unsurprising. Art. 12–15 aim to inform data subjects about the existence of their rights in the GDPR,<sup>187</sup> and to facilitate their exercise.<sup>188</sup> This does not, however, mean that the controller is required to provide other information to help the data subject to exercise her rights.<sup>189</sup> Rather, the data subject only needs to be informed about the existence of her rights, and provided with the necessary infrastructure for their exercise<sup>190</sup> (e.g., web portals for complaints), including the elimination of unnecessary bureaucratic hurdles,<sup>191</sup> a guarantee of reasonable response time to queries lodged<sup>192</sup> as stated in Art. 12(3), and the opportunity to interact with someone who has the power to change the decision.<sup>193</sup> However, the data subject remains responsible to exercise her rights independently.<sup>194</sup> As one commentator notes, Art. 15 does not create a duty to legal consultancy;<sup>195</sup> rather, it is sufficient that the data controllers inform about the existing rights in the GDPR. Unfortunately, Recital 60, which vaguely states that “any further information necessary to ensure fair and transparent processing taking into account the specific circumstances and context in which the personal data are processed” should be provided to the data subject, does not offer 

> example, legitimate interest of data controller can trump a data subject right to object to data processing under Art. 21. However, Art. 22 does not allow automated decisionmaking on the basis of legitimate interest of the data controller (only explicit consent, law, or contract). This information will be useful for a data subject if they want to prevent data controllers from making decisions or to contest decisions. _See_ Regulation 2016/679, GDPR, arts. 13–15 & 21–22, 2016 O.J. (L 119) 40–43, 45–46 (EU). 

> 186 _See_ EUROPEAN DIGITAL RIGHTS, COMPARISON OF THE PARLIAMENT AND COUNCIL TEXT ON THE GENERAL DATA PROTECTION REGULATION 131 (2016), https://edri.org/files/EP_Council_Comparison.pdf [https://perma.cc/CY6H-P97Z]. 

> 187 _See_ Knyrim, _supra_ note 98, 415–416. 

> 188 _See_ Heckmann & Paschke, _supra_ note 92, at 371–372; Ehmann, _supra_ note 119, at 425. 

> 189 _See_ Heckmann & Paschke, _supra_ note 92, at 378–379 (articulating that easily understood information provided about data subject rights in Art. 15–22 is sufficient to facilitate their exercise). 

> 190 _See_ Bensoussan, _supra_ note 98, at 114. 

> 191 _See_ Heckmann & Paschke, _supra_ note 92, at 379–380. 

> 192 _See_ Franck, _supra_ note 95, at 323–324. 

> 193 Article 29 Data Protection Working Party, _supra_ note 85, at 21. 

> 194 _See_ Heckmann & Paschke, _supra_ note 92, at 379–380. 

> 195 Franck, _supra_ note 149, at 352. 

### 40 _COUNTERFACTUAL EXPLANATIONS_ 

additional assistance to the data subject.<sup>196</sup> This provision was intentionally moved to the non-binding Recitals during trilogue negotiations.<sup>197</sup> Data controllers thus do not have a legal obligation to provide information that will be particularly useful for the data subject to exercise her other rights. 

One final comparable restriction is notable concerning Art. 16, the right for the data subject to rectify inaccurate personal data. Data controllers are not required to specify which records most influenced a specific automated decision, which could be extremely helpful to a data subject attempting to identify inaccuracies as grounds to contest a decision. If large amounts of personal data are held, then the subject may have to check tens of thousands of items for inaccuracies. 

## 1. Contesting through counterfactuals 

Art. 13–15 thus do little to facilitate a data subject’s ability to challenge automated decisions. Information is not provided about the safeguards in Art. 22(3) (e.g., the right to contest). It appears that data subjects do not need to be informed of their right not to be subject to an automated decision, which itself could imply a right to contest objectionable automated decisions. Similarly, Recital 71 has neither an explicit link to contesting decisions nor to understanding the black box. Even though an explanation could be helpful, they do not appear to be intended as a precondition for challenging decisions. If explanations were a precondition for contesting decisions, they would appear in the legally binding text.  To offer greater protection to data subjects, these information gaps should be closed, meaning data controllers should inform about the right not to be subject to an automated decision and its safeguards. However, each of these seemingly intentional limitations on the information provided to data subjects suggests that information about 

> 196 Regulation 2016/679, GDPR, recital 60, 2016 O.J. (L 119) 12 (EU). 

> 197 The European Commission, European Council, and European Parliament in Art. 14(1)(h) proposed to create a legal duty for data controllers to provide any further information beyond those in the notification duties to ensure fair and transparent data processing. _See generally_ EUROPEAN COMMISSION, Regulation of the European Parliament and the Council on the Protection of Individuals with Regard to the Processing of Personal Data and on the Free Movement of Such Data (General Data Protection Regulation) (2012), http://ec.europa.eu/justice/dataprotection/document/review2012/com_2012_11_en.pdf [https://perma.cc/2HSG9HX7]; EUROPEAN DIGITAL RIGHTS, _supra_ note 186, at 126–127, 129. However, this proposal was not adopted and moved to Recital 60, suggesting that there is no legal duty to provide more information than required in Art 13–14; _see_ Franck, _supra_ note 99, at 337. 

### 41 _COUNTERFACTUAL EXPLANATIONS_ 

the internal logic of an automated decision-making system (in compliance with “meaningful information about the logic involved as well as the significance and the envisaged consequences” in Art. 13(2)(4), 14(2)(g), and 15(1)(h)), which could facilitate contesting decisions, does not need to be provided.<sup>198</sup> 

Given these restrictions, counterfactuals could be helpful for contesting decisions, and thus provide greater protection for the data subject than currently envisioned by the GDPR. Regardless of the legal status of the right to explanation, the right to contest is a legally binding safeguard.<sup>199</sup> By providing information about the external factors and key variables that contributed to a specific decision, counterfactuals can provide valuable information for data subjects to exercise their right to contest. This would also be in line with the guidelines of the Article 29 Working Party, which urge that understanding decisions and knowing their legal basis is essential for contesting decisions, and is not necessarily linked to opening the black box.<sup>200</sup> An explanation that low-income led to a loan application being declined could, for example, help the data subject contest the outcome on the grounds of inaccurate or incomplete data regarding her financial situation. Understanding the internal logic of the system that led to income being considered a relevant variable in the decision, which would require a technical explanation unlike a counterfactual explanation (see Appendix 1), may be desirable in its own right, but is not absolutely necessary to contest the decision based on that variable. 

Counterfactuals offer a solution and support for contesting decisions by providing data subjects with information about the reasons for a decision, without the need to open the black box. Although Art. 16 of the GDPR gives the data subject the right to correct inaccurate data used to make a decision, the data subject does not need to be informed which data the decision depended. Where a large corpus of data has been collected, an individual without knowledge of which data is relevant or most influential on a particular decision is forced to vet all of it. This lack of information increases the burden on data subjects seeking a different outcome. Counterfactuals provide a compact and easy way to convey these dependencies (i.e., which data was influential), and to facilitate effective claims that a decision was made on the basis of inaccurate data and contest it. 

> 198 Regulation 2016/679, GDPR, art. 15(1)(h), 2016 O.J. (L 119) 43 (EU). 

> 199 Regulation 2016/679, GDPR, art. 22(3), 2016 O.J. (L 119) 46 (EU). 

> 200 _See_ Article 29 Data Protection Working Party, _supra_ note 85, at 25, 27. 

42 _COUNTERFACTUAL EXPLANATIONS_ 

## _C. EXPLANATIONS TO ALTER FUTURE DECISIONS_ 

From the view of the data subject, alongside understanding and contesting decisions, explanations can also be useful to indicate what could be changed to receive a desired result in the future. This purpose does not necessarily relate to the right to contest. Accurate decisions can produce unfavourable results for the data subject. The chances of successfully challenging the decision will also be low in some cases, or the costs and effort required too high. In these situations, the data subject may prefer to change aspects of her situation by adapting her behaviour, and requesting a new decision once more favourable conditions exist. 

Using explanations as a guide to altering behaviour to receive a desired automated decision is not directly addressed in the GDPR. This does not, however, undermine the interest data subjects have in receiving desired results from automated decision-making systems. For example, if a subject was rejected for a loan due to insufficient income, a counterfactual explanation will indicate if reapplying in the event of an immediate pay rise is reasonable. The Article 29 Working Party seems to agree, stating in relevant guidelines that “tips on how to improve these habits and consequently how to lower insurance premiums” could be useful for the data subject.<sup>201</sup> For reasons outlined in Appendix 1, technical explanations that try to provide “meaningful information about the logic involved, as well as the significance and the envisaged consequences” of automated decision-making are not guaranteed to be useful in this situation.<sup>202</sup> 

Counterfactuals can thus be useful for altering future decisions in favour of the data subject. By providing information about key variables and “close possible worlds” which result in a different decision, data subjects can understand which factors could be changed to receive the desired result. For decision-making models and environments with low variability over time, or models that are “artificially frozen” in time for individuals (i.e., future decisions will be made with the same model as the individual’s original decision), this information can help the data subject to alter her behaviour or situation to receive her desired result in the future. Similarly, data controllers could contractually agree to provide the data subject with the preferred outcome if the terms of a given counterfactual were met within a specified period of time. 

> 201 _Id._ at 26. 

> 202 Regulation 2016/679, GDPR, art. 15, 2016 O.J. (L 119) 43 (EU). 

43 _COUNTERFACTUAL EXPLANATIONS_ 

With that said, unanticipated dependencies between intentionally changed attributes and other variables, such as an increase in income resulting from a change in career, may undermine the utility of counterfactuals as guides for future behaviour. Counterfactual explanations can, however, address the impact of changes to more than one variable on a model’s output at the same time. Further, regardless of the utility of counterfactuals as guidance for future behaviour, their ability to help individuals understand which data and variables were influential in specific prior decisions remains unaffected. 

## CONCLUSION 

We have proposed a novel lightweight form of explanation that we refer to as counterfactual explanations. Unlike existing approaches that try to provide insight into the internal logic of black box algorithms, counterfactual explanations do not attempt to clarify how decisions are made internally. Instead, they provide insight into which external facts could be different in order to arrive at a desired outcome.<sup>203</sup> Importantly, counterfactual explanations are efficiently computable for many standard classifiers, particularly neural networks.  As our new form of explanation significantly differs from existing works, we have justified its nature as an explanation with reference to previous works in the philosophical literature and early A.I. 

From the view of the data subject, we have assessed three purposes of explanations of automated decisions: understanding, contesting and altering. We compared these aims with the provisions of the GDPR and evaluated if they rely upon opening the black box. We concluded that the framework offers little support to achieve these goals, and does not mandate that algorithms are explainable to understand, contest or alter decisions. 

The GDPR itself provides little insight into the intended purpose and content of explanations. Recital 71, the only provision that explicitly mentions explanations, does not reveal their intended purpose or content. Given the final text of the GDPR, it appears that explanations can voluntarily be offered after decisions have been made, and are not a 

> 203 The method described here is compatible with a proposal made by Citron and Pasquale to allow consumers to manually enter “hypothetical alterations” to their credit histories and view their effects. DANIELLE K. CITRON & FRANK A. PASQUALE, THE SCORED SOCIETY: DUE PROCESS FOR AUTOMATED PREDICTIONS, 89 WASH. L. REV. 1, 28 (Jan. 2014) https://papers.ssrn.com/abstract=2376209 [https://perma.cc/VQA62MBT]. 

### 44 _COUNTERFACTUAL EXPLANATIONS_ 

required precondition to contest decisions. Further, there is no clear link that suggests that explanations under Recital 71 require opening the black box. 

Recognising this relative lack of insight into explanations, related provisions addressing automated decision-making were examined. Notification duties defined in Art. 13–14 apply prior to data processing or before a decision is made (i.e. at the time of data collection), and provide a simple and generic overview of intended data processing activities that aims to inform a general audience.<sup>204</sup> This type of “meaningful overview” of automated decision-making is largely unsuitable to understand the rationale of specific decisions. Art. 13–14 similarly do not facilitate contesting decisions, owing to a lack of information to be provided about the right not to be subject to automated individual decision-making,<sup>205</sup> and its safeguards.<sup>206</sup> The right of access<sup>207</sup> provides nearly identical information to Art. 13–14, and thus offers similarly limited value for understanding and contesting decisions. The rights and freedoms of others (e.g. privacy or trade secrets) which are protected in Art. 15(4) and Recital 63 pose an additional barrier to transparency when access requests are lodged. Across each of these Articles, technical explanations of the internal logic of automated decision-making systems are not legally mandated. Finally, offering explanations to give guidance how to receive the desired result in the future does not appear to be an aim of the GDPR, but could still be highly useful for individuals seeking alternative, more desirable outcomes. 

Any future attempt to implement a legally binding right to explanation as a safeguard against automated decision-making within the framework provided by the GDPR faces several notable challenges. Automated decision-making must be based “solely on automated processing,” and have “legal effects” or similarly significant effects.<sup>208</sup> Additionally, exemptions from the safeguards against automated decision-making can be introduced through Member State law.<sup>209</sup> 

However, the data subject’s desire to understand, contest, and alter decisions does not change based on these definitional issues. We therefore 

> 204 Regulation 2016/679, GDPR, art. 12(7), 2016 O.J. (L 119) 40 (EU). 

> 205 Regulation 2016/679, GDPR, art. 22(1), 2016 O.J. (L 119) 46 (EU). 

> 206 Regulation 2016/679, GDPR, art. 22(3), 2016 O.J. (L 119) 46 (EU). 

> 207 Regulation 2016/679, GDPR, art. 15, 2016 O.J. (L 119) 43 (EU). 

> 208 Regulation 2016/679, GDPR, art. 22, 2016 O.J. (L 119) 46 (EU). 

> 209 Regulation 2016/679, GDPR, art. 23, 2016 O.J. (L 119) 46–47 (EU). These exemptions may be based, for example, on national security; the enforcement of civil law claims; or the protection of the data subject or the rights and freedoms of others. 

45 _COUNTERFACTUAL EXPLANATIONS_ 

propose to move past the limitation of the GDPR and to use counterfactuals as unconditional explanations. These unconditional explanations should be given whenever requested, regardless of outcome (positive or negative decision), whether the decision was based on solely automated processes and their (legal or similar significant) effects. 

Counterfactual explanations could be implemented in several ways. The transience of decision-making models suggests that counterfactuals either need to be computed automatically at the time a decision is made, or a copy of the model archived to compute counterfactuals at a later time. As multiple outcomes based on changes to multiple variables may be possible, a diverse set of counterfactual explanations should be provided, corresponding to different choices of nearby possible worlds for which the counterfactual holds. These sets could be disclosed when automated decision-making occurs, or in response to specific requests lodged by individuals or a trusted third party auditor.<sup>210</sup> In any case, disclosures should occur in a reasonable window of time.<sup>211</sup> 

Future research should determine appropriate distance metrics and requirements for a sufficient and relevant set of counterfactuals across use sectors and cases which have very different needs. While prior philosophical debate may prove helpful, the absence of causal models in most modern classifiers, as well as the preferences of the recipient(s) of the set, must be accounted for in choosing appropriate metrics and requirements. Compared to prior discussion of measuring “closest possible worlds,” setting requirements for appropriate “close possible worlds” represents a very different philosophical, social, and legal challenge. 

To minimise bureaucratic burdens for data controllers and delays for data subjects and third party auditors, automated calculation and disclosure of counterfactuals would be preferable. We recommend this type of automated implementation going forward. One possible approach is to provide individuals or third party auditors with access to “auditing APIs,”<sup>212</sup> which allow users to request counterfactual explanations from 

> 210 _See generally_ Wachter, Mittelstadt & Floridi, _supra_ note 1. 

> 211 _See, e.g._ , Regulation 2016/679, GDPR, art. 12(3), 2016 O.J. (L 119) 40 (EU). 

> 212 Who would shoulder the costs of hosting these APIs and computing counterfactuals is an important political issue that would require resolution. This issue goes beyond the scope of this paper. For related discussion of implementing algorithmic auditing, see Christian Sandvig et al., _Auditing Algorithms: Research Methods for Detecting Discrimination on Internet Platforms_ , DATA & DISCRIMINATION: CONVERTING CRITICAL CONCERNS INTO PRODUCTIVE INQUIRY (May 22, 2014), 

### 46 _COUNTERFACTUAL EXPLANATIONS_ 

the service provider, and perhaps compute them directly via the API. Access to historical decision-making models used for the decision at hand, as well as permissive terms of service that allow for such auditing, would be required.<sup>213</sup> This functionality could potentially be embedded in existing APIs. 

Counterfactual explanations provide reasons why a particular decision was received (e.g., low income), offer grounds to contest it (e.g., if the data controller used inaccurate data about the income of the applicant), and provide limited “advice” on how to receive the desired results in the future (e.g., an increase of 4000 pounds/year would have resulted in a positive application). Their usage would help to resolve two primary objections to a legally binding right to explanation: first, that explaining the internal logic of automated systems to experts and nonexperts alike is a highly difficult and perhaps intractable challenge; and second, that an excessive disclosure of information about the internal logic of a system could infringe on the rights of others, either by revealing protected trade secrets or by violating the privacy of individuals whose data is contained in the training dataset. In contrast, counterfactuals allow an individual to receive explanations without conveying the internal logic of the algorithmic black box (beyond a limited set of dependencies), and are less likely to infringe the rights and freedoms of others than full disclosure. Assuming reasonable limitations are set on the number of counterfactuals that must be provided, counterfactuals are also less likely to provide information that reveals trade secrets or allows gaming of decision-making systems. 

As a minimal form of explanation, counterfactuals are not appropriate in all scenarios. In particular, where it is important to understand system functionality, or the rationale of an automated decision, counterfactuals may be insufficient in themselves. Further, counterfactuals do not provide the statistical evidence needed to assess algorithms for fairness or racial bias. Given these limitations, more general forms of explanations and interpretability should still be pursued 

> http://social.cs.uiuc.edu/papers/pdfs/ICA2014-Sandvig.pdf [https://perma.cc/9NKHJ69E]; Brent Mittelstadt, _Auditing for Transparency in Content Personalization Systems_ , 10 INT’L. J. COMM. 12 (2016) http://ijoc.org/index.php/ijoc/article/view/6267 [https://perma.cc/TCN4-56QU]. 

> 213 Counterfactuals must be computed on the basis of the decision-making model at the time the decision was taken. Assuming automated decision-making models change over time, in implementations not involving automatic computation of counterfactuals at the time a decision is made (which may be cost prohibitive), it will be necessary for data controllers to keep ‘audit logs’ indicating the state of the decision-making model at the time of the decision. 

### 47 _COUNTERFACTUAL EXPLANATIONS_ 

to increase accountability and better validate the fairness and functionality of systems. 

However, counterfactuals represent an easy first step that balances transparency, explainability, and accountability with other interests such as minimising the regulatory burden on business interest or preserving the privacy of others, while potentially increasing public acceptance of automatic decisions. Rather than waiting years for jurisprudence to dissolve all these uncertainties, we propose to abandon the narrow definitions and conditions the GDPR imposes on automated decisionmaking, and offer counterfactuals as unconditional explanations at the request of affected individuals. 

### 48 _COUNTERFACTUAL EXPLANATIONS_ 

APPENDIX 1: SIMPLE LOCAL MODELS AS EXPLANATIONS 

As discussed in Section II.B, ‘Explanations in A.I. and Machine Learning,’ approaches such as LIME<sup>214</sup> that generate simple models as local approximations of decisions make a three-way trade-off between the quality of the approximation versus the ease of understanding the function and the size of the domain for which the approximation is valid.<sup>215</sup> 

To illustrate the instabilities of the approach with respect to the size of the domain, we consider a simple function of one variable.  Even for problems such as this, the notion of scale, or how large a region should an explanation try to describe, is challenging with the ideal choice of scale depending on what the explanation would be used for. 

As a real-world example, consider being stopped by someone in a car who asks which direction they should travel in to go north. Fundamentally, this is a difficult question to answer well, with the most appropriate answer depending upon how far north they wish to travel. If they do not intend to travel far, simply pointing north gives them enough information. However, if they intend to travel further, roads that initially point north may double back on themselves or be cul-de-sacs and better directions are needed. If they intend to travel a long way, they may be better off ignoring the compass bearing entirely, and instead try to directly join up with an inter-city network. 

This exact issue is faced when automating explanations of decisions: the generated explanations are generic, and designed to be useful to the recipient of the explanation regardless of how they are used. However, as shown in Figure 1, the explanation — or simplified model — can vary wildly with the scale or range of inputs considered. 

> 214 _See_ Ribeiro, Singh, & Guestrin, _supra_ note 14. 

> 215 _See_ Bastani, Kim & Bastani, _supra_ note 13; Lakkaraju et al., _supra_ note 47. 

49 _COUNTERFACTUAL EXPLANATIONS_ 









**_Figure 1 - Local models varying with choice of scale._** _The red line in each subfigure shows a local approximation of the same blue score curve centred at the same location in each plot. The varying range over which the approximation is computed is given by the region marked by black bars. Different choices of range e.g. top left vs. bottom left can lead to completely opposing explanations where the score either increases or decreases as the value along the bottom axis increase._ 

As can be seen, the direction and magnitude of the linear approximation (red) to underlying function (blue) vary dramatically with choice of domain, and deciding which approximation is most helpful to a layperson trying to understand the decision made about them is nontrivial. 

To show the difficulties that would exist in either trying to use local models to either compute counterfactuals, or simply for the data subject to adjust their score, we assume that the subject desired to know how to obtain a lower score of -10 or below. In this case, none of the local approximations would be useful. The top left model, which is based on exact description of the function around point x predicts that a score of - 10 would be obtained with a value of -2.5—corresponding to an actual score of 91.5, while the two centre approximations suggest that it is not possible to obtain any score except 0, and the bottom left approximation says that -10 occurs at near 0.9—which actually corresponds to a local maxima. 

In contrast, the counterfactual explanation for a query such as “Why was the score not below -10?” would return the answer “Because the x value was not 2.15” (the counterfactual is illustrated in figure 2 by 

### 50 _COUNTERFACTUAL EXPLANATIONS_ 

the green dot). Of course, it should be noted that the two approaches are generally incomparable. In much the same way, if a data subject desired to know a local linear approximation about their data point, knowledge of counterfactuals would not be helpful. However, of the two approaches, counterfactuals are the only one that will provide some indication if it is worth reapplying for a loan in the event of a pay rise. 



**_Figure 2 – Visual representation of the range of a counterfactual explanation_** 

### 51 _COUNTERFACTUAL EXPLANATIONS_ 

## APPENDIX 2: EXAMPLE TRANSPARENCY INFOGRAPHIC 

The figure below shows several icons proposed by the European Parliament during trilogue that were ultimately not adopted as a standard. They nonetheless reveal the level of complexity expected by EU legislators when communicating information to data subjects under Art. 13–14. The reliance on generic icons suggests that individual-level, contextualised information is not required, meaning Art. 13–14 are not intended to provide a ‘de facto’ right to explanation comparable to the right contained in Recital 71. The relative simplicity of the icons also suggests that a broad audience is intended, comparable for example to website privacy notices. Finally, although the icons were rejected, the EC has been tasked with developing such standardised icons in the future (Art. 12(8)), meaning comparable icons are seen as an acceptable way to convey the information required by Art. 13–14. 



52 _COUNTERFACTUAL EXPLANATIONS_ 

