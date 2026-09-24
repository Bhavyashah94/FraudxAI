---
title: "Spade: A Real-Time Fraud Detection Framework on Evolving Graphs"
authors: "version)"
year: 2022
arxiv_id: "2211.06977"
original_file: "2211.06977.pdf"
pdf_path: "docs/papers\2022_version_spade_a_realtime_fraud_detection_fr.pdf"
---

# Spade: A Real-Time Fraud Detection Framework on Evolving Graphs

**Authors:** Version) et al.  
**Year:** 2022 | **arXiv:** [`2211.06977`](https://arxiv.org/abs/2211.06977)  
**Local PDF:** [`2022_version_spade_a_realtime_fraud_detection_fr.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2022_version_spade_a_realtime_fraud_detection_fr.pdf)

---

# **Spade: A Real-Time Fraud Detection Framework on Evolving Graphs (Complete Version)** 

Jiaxin Jiang Yuan Li National University of Singapore National University of Singapore jxjiang@nus.edu.sg li.yuan@u.nus.edu 

Bingsheng He National University of Singapore hebs@comp.nus.edu.sg 

Bryan Hooi Jia Chen National University of Singapore GrabTaxi Holdings bhooi@comp.nus.edu.sg jia.chen@grab.com 

Johan Kok Zhi Kang GrabTaxi Holdings johan.kok@grabtaxi.com 



<!-- Start of picture text -->
Periodical updates: ∆G<br>2) Graph updates G = G ⊕ ∆G<br>Transaction logs Transaction graph: G Fraudsters<br>3) Detection New fraudsters<br>Fraud semantics 4) Action<br>-- DGDW Moderators<br>- FD a) ban b) analyse c) supervise<br>Figure 1: Grab’s data pipeline for fraud detection<br>New fraudster Suspicious activities<br>Fraudulent community<br>Fraudsters<br>Normal users T0 T1 T2<br>1)Graphconstruction<br><!-- End of picture text -->

## Abstract 

Real-time fraud detection is a challenge for most financial and electronic commercial platforms. To identify fraudulent communities, Grab, one of the largest technology companies in Southeast Asia, forms a graph from a set of transactions and detects dense subgraphs arising from abnormally large numbers of connections among fraudsters. Existing dense subgraph detection approaches focus on static graphs without considering the fact that transaction graphs are highly dynamic. Moreover, detecting dense subgraphs from scratch with graph updates is time consuming and cannot meet the real-time requirement in industry. To address this problem, we introduce an incremental real-time fraud detection framework called Spade. Spade can detect fraudulent communities in hundreds of microseconds on millionscale graphs by incrementally maintaining dense subgraphs. Furthermore, Spade supports batch updates and edge grouping to reduce response latency. Lastly, Spade provides simple but expressive APIs for the design of evolving fraud detection semantics. Developers plug their customized suspiciousness functions into Spade which incrementalizes their semantics without recasting their algorithms. Extensive experiments show that Spade detects fraudulent communities in real time on million-scale graphs. Peeling algorithms incrementalized by Spade are up to a million times faster than the static version. 

Figure 2: An example of fraud detection on evolving graphs 

robustness, and theoretical worst-case guarantee. However, existing peeling algorithms [6, 19, 31] assume a static graph without considering the fact that social and transaction graphs in online marketplaces are rapidly evolving in recent years. One possible solution for fraud detection on evolving graphs is to perform peeling algorithms periodically. We take Grab’s fraud detection pipeline as an example. 

#### PVLDB Reference Format: 

Fraud detection pipeline in Grab (Figure 1). Grab is one of the largest technology companies in Southeast Asia and offers digital payments and food delivery services. On the Grab’s e-commerce platform, 1) the transactions form a transaction graph 퐺. 2) Grab updates the transaction graphs periodically 퐺 = 퐺 ⊕ ∆퐺. Our experiments show that it takes 28s to carry out Fraudar (FD) [19] on a transaction graph with 6M vertices and 25M edges. Therefore, we can execute fraud detection every 30 seconds. 3) The dense subgraph detection algorithm and its variants are used to detect fraudulent communities. 4) After identifying the fraudsters, the moderators ban or freeze their accounts to avoid further economic loss. A classic fraud example is customer-merchant collusion. Assume that Grab provides promotions to new customers and merchants. However, fraudsters create a set of fake accounts and do fictitious trading to use the opportunity of promotion activities to earn the bonus. Such fake accounts (vertices) and the transactions among them (edges) form a dense subgraph. 

Jiaxin Jiang, Yuan Li, Bingsheng He, Bryan Hooi, Jia Chen, and Johan Kok Zhi Kang. Spade: A Real-Time Fraud Detection Framework on Evolving Graphs (Complete Version). PVLDB, 16(3): XXX-XXX, 2022. doi:XX.XX/XXX.XX 

## 1 Introduction 

Graphs have been found in many emerging applications, including transaction networks, communication networks and social networks. The dense subgraph problem is first studied in [17] and is effective for link spam identification [4, 16], community detection [8, 11] and fraud detection [7, 19, 29]. Standard peeling algorithms [2, 5, 7, 19, 31] iteratively peel the vertex that has the smallest connectivity (e.g., vertex degree or sum of the weights of the adjacent edges) to the graph. Peeling algorithms are widely used because of their efficiency, 

This work is licensed under the Creative Commons BY-NC-ND 4.0 International License. Visit https://creativecommons.org/licenses/by-nc-nd/4.0/ to view a copy of this license. For any use beyond those covered by this license, obtain permission by emailing info@vldb.org. Copyright is held by the owner/author(s). Publication rights licensed to the VLDB Endowment. Proceedings of the VLDB Endowment, Vol. 16, No. 3 ISSN 2150-8097. doi:XX.XX/XXX.XX 

EXAMPLE 1.1. Consider the transaction graph in Figure 2, where a vertex is a user or a store, and an edge represents a transaction. Suppose a fraudulent community is identified at time 푇0 and a normal user becomes a fraudster and participates in suspicious activities at 

Table 1: Comparison of Spade and previous algorithms 



<!-- Start of picture text -->
DG [6] DW [18] FD [19] Spade<br>Dense subgraph detection ✓ ✓ ✓ ✓<br>Accuracy guarantees ✓ ✓ ✓ ✓<br>Weighted graph ✗ ✓ ✓ ✓<br>Incremental updates ✗ ✗ ✗ ✓<br>Edge reordering ✗ ✗ ✗ ✓<br><!-- End of picture text -->

푇1. Applying peeling algorithms at 푇1, the new fraudster is detected at 푇2. However, many new suspicious activities have occurred during the time period [푇1,푇2] that could cause huge economic losses. 

As reported in recent studies [1, 35], 21.4% of the traffic to e- commerce portals are malicious bots in 2018. Fraud detection is challenging since many fraudulent activities occur in a very short timespan. Hence, identifying fraudsters and reducing response latency to fraudulent transactions are key tasks in real-time fraud detection. 

To address real-time fraud detection on evolving graphs, a better solution would be to incrementally maintain dense subgraphs. There are two main challenges of incremental maintenance. First, operational demands require that fraudsters should be identified in 100 milliseconds in industry. Maintaining the dense subgraph incrementally in such a short timespan is challenging. Second, fraud semantics continue to evolve and it is not trivial to incrementalize each of them. Implementing a correct and efficient incremental algorithm is, in general, a challenge. It is impractical to train all developers with the knowledge of incremental graph evaluation. To the best of our knowledge, there are no generic approaches to minimize the cost of incremental peeling algorithms. Motivated by the challenges, we design a real-time fraud detection framework, named Spade to detect fraudulent communities by incrementally maintaining dense subgraphs. The comparison between Spade and the previous algorithms (dense subgraphs (DG) [6], dense weighted subgraph (DW) [18] and Fraudar (FD) [19]) is summarized in Table 1. 

Contributions. In this paper, we focus on incremental peeling algorithms. In summary, this paper makes the following contributions. 

- (1) We build three fundamental incremental techniques for peeling algorithms to avoid detecting fraudulent communities from scratch. Spade inspects the subgraph that is affected by graph updates and reorders the peeling sequence incrementally, which theoretically guarantees the accuracy of the worst case. 

- (2) Spade enables developers to design their fraud semantics to detect fraudulent communities by providing the suspiciousness functions of edges and vertices. We show that a variety of peeling algorithms can be incrementalized in Spade (Section 3) including DG, DW and FD. 

- (3) We conduct extensive experiments on Spade with datasets from industry. The results show that Spade speeds up fraud detection up to 6 orders of magnitude since Spade minimizes the cost of incremental maintenance by inspecting the affected area. Furthermore, the latency of the response to fraud activities can be significantly reduced. Lastly, once a user is spotted as a fraudster, we identify the related transactions as potential fraud transactions and pass them to system moderators. Up to 88.34% potential fraud transactions can be prevented. 

Table 2: Frequently used notations 

|Notation|Meaning|
|---|---|
|퐺/∆퐺|a transaction graph / updates to graph퐺|
|퐺⊕∆퐺|the graph obtained by updating∆퐺to퐺|
|푎푖/푐푖푗|the weight on vertex푢푖/ on edge(푢푖,푢푗)|
|푓(푆)|the sum of the suspiciousness of induced subgraph퐺[푆]|
|푔(푆)|the suspiciousness density of vertex set푆|
|푤푢(푆)|peeling weight,i.e.,the decrease in푓by removing푢from푆|
|푄|a peeling algorithm|
|푂|the peeling sequence orderw.r.t.푄|
|푆<sup>푃</sup><br>|the vertex set returned by a peeling algorithm<br>|
|푆<sup>∗</sup>|the optimal vertex set,i.e.,푔(푆<sup>∗</sup>)is maximized|



Organization. The rest of this paper is organized as follows: Section 2 presents the background and the problem statement. We introduce the framework of Spade in Section 3 and three incremental peeling algorithms in Section 4. Section 5 reports on the experimental evaluation. After reviewing related work in Section 6, we conclude in Section 7. 

## 2 Background 

## 2.1 Preliminary 

Graph 퐺. We consider a directed and weighted graph 퐺 = (푉, 퐸), where 푉 is a set of vertices and 퐸 ⊆ (푉 × 푉 ) is a set of edges. Each edge (푢푖,푢 푗 ) ∈ 퐸 has a nonnegative weight, denoted by 푐푖푗 . We use 푁 (푢) to denote the neighbors of 푢. 

Induced subgraph. Given a subset 푆 of 푉 , we denote the induced subgraph by 퐺[푆] = (푆, 퐸[푆]), where 퐸[푆] = {(푢,푣)|(푢, 푣) ∈ 퐸 ∧ 푢,푣 ∈ 푆 }. We denote the size of 푆 by |푆 |. 

Density metrics 푔. We adopt the class of metrics 푔 in previous studies [6, 18, 19], 푔(푆) =<sup>푓</sup> |푆<sup>(푆</sup> |<sup>), where푓is the total weightof 퐺[푆], i.e.,</sup> the sum of the weight of 푆 and 퐸[푆]: 



The weight of a vertex 푢푖 measures the suspiciousness of user 푢푖, denoted by 푎푖 (푎푖 ≥ 0). The weight of the edge (푢푖,푢 푗 ) measures the suspiciousness of transaction (푢푖,푢 푗 ), denoted by 푐푖푗 > 0. Intuitively, 푔(푆) is the density of the induced subgraph 퐺[푆]. The larger 푔(푆) is, the denser 퐺[푆] is. 

Graph updates ∆퐺. We denote the set of updates to 퐺 by ∆퐺 = (∆푉, ∆퐸). We denote the graph obtained by updating ∆퐺 to 퐺 as 퐺 ⊕ ∆퐺. Since transaction graphs continue to evolve, we consider edge insertion rather than edge deletion. Therefore, 퐺 ⊕ ∆퐺 = (푉 ∪ ∆푉, 퐸 ∪ ∆퐸). Specifically, we consider two types of updates, edge insertion (i.e., |∆퐸|= 1) and edge insertion in batch (i.e., |∆퐸|> 1). 

## 2.2 Peeling algorithms 

Peeling algorithms (푄) are widely used in dense subgraph mining [6, 19, 31]. They follow the execution paradigm in Algorithm 1 and differ mainly in density metrics. They are categorized to three categories: unweighted [6], edge-weighted [18] and hybrid-weighted [19]. Peeling weight. Specifically, we use 푤푢푖 (푆) to indicate the decrease in the value of 푓 when the vertex 푢푖 is removed from a vertex set 푆, i.e., the peeling weight. Previous work [19] formalizes 푤푢푖 (푆) as follows: 

### Algorithm 1: Execution paradigm of peeling algorithms 

Input: A graph 퐺 = (푉, 퐸) and a density metric 푔(푆) Output: The peeling sequence order 푂 = 푄(퐺) and the fraudulent community 1 푆0 = 푉 2 for 푖 = 1, . . ., |푉 | do 3 select the vertex 푢 ∈ 푆푖−1 such that 푔(푆푖−1 \ {푢 }) is maximized 4 푆푖 = 푆푖−1 \ {푢 } 5 푂.add(푢) 6 return 푂 and arg max푆푖 푔(푆푖 ) 



Peeling sequence. We use 푆푖 to denote the vertex set after 푖-th peeling step. Initially, the peeling algorithms set 푆0 = 푉 . They iteratively remove a vertex 푢푖 from 푆푖−1, such that 푔(푆푖−1 \ {푢푖 }) is maximized (Line 3∼4). The process repeats recursively until there are no vertices left. This leads to a series of sets over 푉 , denoted by 푆0, . . . , 푆 |푉 | of sizes |푉 |, . . . , 0. Then 푆푖 (푖 ∈ [0, |푉 |]), which maximizes the density metric 푔(푆푖), is returned, denoted by 푆<sup>푃</sup> . For simplicity, we denote ∆푖 = 푤푢푖 (푆푖 ). Instead of maintaining the series 푆0, . . . ,푆 |푉 |, we record the peeling sequence 푂 = [푢1, . . .푢 |푉 |] such that {푢푖 } = 푆푖−1 \ 푆푖. 

EXAMPLE 2.1. Consider the graph 퐺 in Figure 3. 푢1 is peeled since its peeling weight is the smallest among all vertices. Similarly, 푢3,푢2,푢4,푢5 will be peeled accordingly. Therefore, the peeling sequence is 푂 = [푢1,푢3,푢2,푢4,푢5]. 

Complexity and accuracy guarantee. In Algorithm 1, Min-Heap is used to maintain the peeling weights, the insertion cost is 푂(log|푉 |). There are at most |퐸| insertions. Therefore, the complexity of Algorithm 1 is 푂(|퐸|log|푉 |). We denote the vertex set that maximizes 푔 by 푆<sup>∗</sup> . Previous studies [6, 19, 23] conclude that: 

LEMMA 2.1. Let 푆<sup>푃</sup> be the vertex set returned by the peeling algorithms and 푆<sup>∗</sup> be the optimal vertex set, 푔(푆<sup>푃</sup> ) ≥<sup>1</sup> 2<sup>푔(푆∗).</sup> 

Although peeling algorithms are scalable and robust, we remark that these algorithms are proposed for static graphs, which takes several minutes on million-scale graphs. For evolving graphs, computing from scratch is still time-consuming, which cannot meet the realtime requirement. Moreover, it is not trivial to design incremental algorithms for peeling algorithms. In this paper, we investigate an auto-incrementalization framework for peeling algorithms. 

Problem definition. Given a graph 퐺 = (푉, 퐸), a peeling algorithm 푄, and the peeling result of 푄 on 퐺, 푆<sup>푃</sup> = 푄(퐺), our problem is to efficiently identify the result of 푄 on 퐺 ⊕ ∆퐺, 푆<sup>푃′</sup> = 푄(퐺 ⊕ ∆퐺), where ∆퐺 is the graph updates. 

## 3 The Spade Framework 

In this section, we present an overview of our proposed framework Spade and sample APIs. Subsequently, we demonstrate some examples on how to implement different peeling algorithms with Spade. 

## 3.1 Overview of Spade and APIs 

We follow two design goals to satisfy operational demands. 

- Programmability. We provide a set of user-defined APIs for developers to develop their dense subgraph-based semantics 



<!-- Start of picture text -->
Intialization: G Iteration 1: peel u1<br>u1 u3 u4 u3 u4<br>2 1 2 1<br>2 4 4<br>2 2<br>u2 u5 u2 u5<br>Iteration 2: peel u3 Iteration 3: peel u2 Iteration 4: peel u4<br>u4 u4<br>2 4 4 u5<br>u2 u5 u5<br>Peeling sequence order: O = [u1, u3, u2, u4, u5]<br><!-- End of picture text -->

Figure 3: Example of peeling algorithms 



<!-- Start of picture text -->
moderators developer LoadGraph<br>analyse/ban fraud semantics InsertEdge()<br>Fraudulent community Auto. Incrementalization For an edge insertion<br>Spade engine Spade API VSusp ESusp<br>Edge Grouping Metrics VSusp<br>ESusp IsBenign<br>Edge update Batch updates<br>InsertEdge ReorderSeq<br>Graph loading InsertBatchEdges<br>Storage system (DFS) SaveResult<br>(a) Architecture (b) Edge insertion<br><!-- End of picture text -->

Figure 4: Architecture of Spade and workflow of an edge insertion 

to detect fraudsters. Moreover, Spade can auto-incrementalize their semantics without recasting the algorithms. 

- Efficiency. Spade allow efficient and scalable fraud detection on evolving graphs in real-time. 

Architecture of Spade. Figure 4 shows the architecture of Spade and the workflow of an edge insertion. Spade automatically incrementalizes peeling algorithms with the user-defined suspiciousness functions. To avoid computing from scratch on evolving graphs, the engine of Spade maintains the fraudulent community incrementally with an edge update (Section 4.1). Batch execution is developed to improve the efficiency of handling edge updates in batch (Section 4.2). The updated fraudulent community is identified in real time and returned to the moderators for further analysis. Given an edge insertion, the workflow of Spade contains the following components: 

- VSusp and ESusp. Given a new vertex/edge, these components are responsible for deciding the suspiciousness of the endpoint of the edge or the edge with a user-defined strategy. 

- IsBenign. This component is responsible for deciding whether a new edge is benign (Section 4.3). If the edge is benign, it is inserted into an edge vector pending reordering; otherwise, peeling sequence reordering is triggered immediately for the edge buffer with this new edge. 

- ReorderSeq. This component is responsible for incrementally maintaining the peeling sequence and deciding the new fraudulent community with the graph updates detailed in Section 4. 

APIs and data structure (Listing 1). We provide APIs for developers to customize and deploy their peeling algorithms for different application requirements. Developers can customize VSusp and ESusp to develop their fraud detection semantics. We design two 

APIs for edge insertion, namely InsertEdge and InsertBatchEdges. The Detect function spots the fraudulent community on the current graph. IsBenign and ReorderSeq are two built-in APIs which are transparent to developers. They are activated when new edges are inserted. Spade uses the adjacency list to store the graph. Two vectors _seq and _weight are used to store the peeling sequence and the peeling weights. 

### Listing 1: Overview of Spade 



|1<br>2<br>3|class Spade {<br>public:<br>Graph LoadGraph(string path){} //Load graph from disk<br>|
|---|---|
|4|//Plug in vertex suspiciousness function|
|5|void VSusp(function<double(Vertex u, Graph g)> susp) {}<br>|
|6|//Plug in edge suspiciousness function|
|7|void ESusp(function<double(Edge e, Graph g)> susp) {}|
|8|//Detect the fraudsters on graph _g|
|9|set<Vertex> Detect() {}<br>|
|10|//Insert an edge and detect the new fraudsters|
|11|set<Vertex> InsertEdge(Edge e) {}|
|12|//Insert a batch of edges and detect the new fraudsters|
|13|set<Vertex> InsertBatchEdges(Edge* e_arr) {}|
|14|private:<br>|
|15|Graph _g; //Graph|
|16|vector<Vertex> _seq; //Peeling sequence|
|17|vector<double> _weight; //Peeling weights<br>|
|18|vector<Edge> _benign_edges; //Store the benign edges|
|19|bool IsBenign(Edge e) {} //Judge if an edge is benign|
|20<br>21|void ReorderSeq(){} //Reorder the peeling sequence<br>}|





Characteristic of density metrics. We next formalize the sufficient condition of the density metrics that can be supported by Spade. 

PROPERTY 3.1. If 1) 푔(푆) is an arithmetic density, i.e., 푔 =<sup>|푓</sup> |푆<sup>(푆</sup> |<sup>)|,</sup> 2) 푎푖 ≥ 0, and 3) 푐푖푗 > 0, then 푔(푆) is supported by Spade. 

The correctness is satisfied since Spade correctly returns the peeling sequence order (detailed in Section 4). We also characterize the properties of these popular density metrics in Appendix E of [20]. Instances. We show that popular peeling algorithms are easily implemented and supported by Spade, e.g., DG [6], DW [18] and FD [19]. We take FD as an example and leave the discussion of the other instances in the Appendix F of [20]. To resist the camouflage of fraudsters, Hooi et al. [19] proposed FD to weight edges and set the prior suspiciousness of each vertex with side information. Let 푆 ⊆ 푉 . The density metric of FD is defined as follows: 

## 4 Incremental peeling algorithms 

In this section, we propose several techniques to incrementally identify fraudsters by reordering the peeling sequence 푂 with graph updates, i.e., the peeling sequence on 퐺 ⊕ ∆퐺, denoted by 푂<sup>′</sup> . 

## 4.1 Peeling sequence reordering with edge insertion 

Given a graph 퐺 = (푉, 퐸), the peeling sequence 푂 on 퐺 and the graph updates ∆퐺 = (∆푉, ∆퐸), where |∆퐸|= 1, Spade returns the peeling sequence 푂<sup>′</sup> on 퐺 ⊕ ∆퐺. 

Vertex insertion. Given a new vertex 푢, we insert it into the head of the peeling sequence and initialize its peeling weight by ∆0 = 0. Insertion of an edge (푢푖,푢 푗 ). Without loss of generality, we assume 푖 < 푗 and denote the weight of (푢푖,푢 푗 ) by ∆= 푐푖푗 . Given an edge insertion (푢푖,푢 푗 ), we observe that a part of the peeling sequence will not be changed. We formalize the finding as follows. 

LEMMA 4.1. 푂<sup>′</sup> [1 : 푖 − 1] = 푂[1 : 푖 − 1]. 

Due to space limitations, all the proofs in this section are presented in Appendix A of [20]. 

Affected area (퐺 T ) and pending queue (푇 ). Given updates ∆퐺 to graph 퐺 and an incremental algorithm T , we denote by 퐺 T = (푉T, 퐸 T ) the subgraph inspected by T in 퐺 that indicates the necessary cost of incrementalization. Moreover, we construct a priority queue 푇 for the vertices pending reordering in ascending order of the peeling weights. 

Incremental algorithm (T ). T initializes an empty vector for the updated peeling sequence 푂<sup>′</sup> and append 푂[1 : 푖 − 1] to 푂<sup>′</sup> due to the Lemma 4.1. We iteratively compare 1) the head of 푇 , denoted by 푢min and 2) the vertex 푢푘 in the peeling sequence 푂, where 푘 > 푖. The corresponding peeling weights are denoted by ∆min and ∆푘 . We consider the following three cases: 

Case 1. If ∆min < ∆푘 , we pop the 푢min from 푇 and insert it to 푂<sup>′</sup> . Then we update the priorities in 푇 for the neighbors of 푢min, 푁 (푢min). Case 2. If ∆min ≥ ∆푘 and ∃푢푇 ∈ 푇, (푢푇 ,푢푘 ) ∈ 퐸 or (푢푘,푢푇 ) ∈ 퐸, we insert 푢푘 into 푇 . The peeling weight is 푤푢푘 (푇 ∪ 푆푘 ) = ∆푘 + �(푢푇 ∈푇 )<sup>�</sup> ((푢푇 ,푢푘 )∈퐸)<sup>푐</sup> 푇푘<sup>+ �</sup> (푢푇 ∈푇 )<sup>�</sup> ((푢푘 ,푢푇 )∈퐸)<sup>푐</sup> 푘푇<sup>, 푘= 푘+ 1.</sup> Case 3. If ∆min ≥ ∆푘 and ∀푢푇 ∈ 푇, (푢푇 ,푢푘 )̸ ∈ 퐸 and (푢푘,푢푇 )̸ ∈ 퐸, we insert 푢푘 to 푂<sup>′</sup> , 푘 = 푘 + 1. 

We repeat the above iteration until 푇 is empty. 



To implement FD on Spade, users only need to plug in the suspiciousness function vsusp for the vertices by calling VSusp and the suspiciousness function esusp for the edges by calling ESusp. Specifically, 1) vsusp is a constant function, i.e., given a vertex 푢, vsusp(푢) = 푎푖 and 2) esusp is a logarithmic function such that given an edge (푢푖,푢 푗 ), esusp(푢푖,푢 푗 ) = log(1푥+푐)<sup>,where푥isthedegreeof</sup> the object vertex between 푢푖 and 푢 푗 , and 푐 is a small positive constant [19]. 

Developers can easily implement customized peeling algorithms with Spade, which significantly reduces the engineering effort. For example, users write only about 20 lines of code (compared to about 100 lines in the original FD [19]) to implement FD. 

EXAMPLE 4.1. Consider the graph 퐺 in Figure 3 and its peeling sequence 푂 = [푢1,푢3,푢2,푢4,푢5]. Suppose that a new edge (푢1,푢5) is inserted into 퐺 and its weight is 4 as shown in the LHS of Figure 5. The reordering procedure is presented in the RHS of Figure 5. 푢1 is pushed to the pending queue 푇 . Since the peeling weight of the next vertex in 푂, 푢3, is the smallest, it will be inserted directly into 푂<sup>′</sup> . Since 푢2 ∈ 푁 (푢1), we recover its peeling weight and push it into 푇 . Since the peeling weights of 푢2 and 푢1 are smaller than those of 푢4, they will pop out of 푇 and insert into 푂<sup>′</sup> . Once 푇 is empty, the rest of the vertices, 푢4 and 푢5, in 푂 are appended to 푂<sup>′</sup> directly. Therefore, the reordered peeling sequence is 푂<sup>′</sup> = [푢3,푢2,푢1,푢4,푢5]. 

Remarks. If the peeling weight of 푢푘 is greater than that of the head of 푇 (i.e., 푢min), then 푢min has the smallest peeling weight among 푇 ∪ 푆푘 . We formalize this remark as follows. 



<!-- Start of picture text -->
Peeling Sequence after reordering: O ′ = [u3, u2, u1, u4, u5]<br>Graph G and<br>O = [u1, u3, u2, u4, u5] [u1, u3, u2, u4, u5] [u1, u3, u2, u4, u5] [u1, u3, u2, u4, u5] [u1, u3, u2, u4, u5] [u1, u3, u2, u4, u5]<br>u1 u3 u4 T T T T T<br>2 1 O ′ u1 O ′ u1 O ′ u2 O ′ u1 O ′ O ′<br>2 4 2 4 u3 u3 u1 u3 u2 u3 u2 u1 u3 u2 u1 u4 u5<br>u2 u5<br>5) u4 and u5 are ap-<br>insertion of (u1, u5) 1) u3 has smallest peel- 2) u2 is inserted into T 3) u2 has smallest peeling 4) u1 has smallest peeling pended to O ′ when T<br>LHS ing weight weight. Pop u2 from T . weight. Pop u1 from T . is empty<br>RHS<br>Figure 5: Peeling sequence reordering with edge insertion (A running example)<br>Case 1: if ∆min < ∆k Case 2: if ∆min ≥ ∆k insert uk to T<br>T T Case 2(a): uk is black or gray Algorithm 2: Peeling sequence reordering in batch<br>insertO ′ umin utominO ′ uumini uukk . . .. . .Or uunn O ′ uk uumini cckjjk Caseuk . . .2(b)color: uk Nis(whiteuukn) gray 1 Input:Output:sort ∆푉 Graph Peeling sequence orderin the ascending order of indices in 퐺 = (푉, 퐸), 푂, density metric 푂 ′ = 푄(퐺  푂 푔⊕(푆∆and color)퐺, ∆) and fraudulent community퐺 = (∆ ∆푉푉,black ∆퐸)<br>O[k : n] insert uk to O ′ uk O. . .[k : n] un 32 init an empty vectorinit a priority pending queue 푂 ′  푇 in the ascending order of peeling weights<br>T : Pending queue N (u): the neighbors of u O: the peeling sequence order 4 for 푢푖 = 푂[푖] ∈ ∆푉 do<br>5 add 푢푖 into 푇<br>Figure 6: Peeling sequence reordering in batch 6 color its neighbors 푂[푗] (푗 > 푖) gray<br>7 푘 = 푖 + 1<br>8 while 푇 is not empty do<br>ui 1 9 if ∆min < ∆푘 then // Case 1<br>10 pop 푢min from 푇 and insert it to 푂 ′<br>4 11 update the priorities of 푁 (푢min) in 푇<br>fraudulent community S P 12 else<br>2 13 if 푢푘 is black or gray then // Case 2(a)<br>uj 3 1 2 3 4 : four new transaction edges 1415 addcolor its neighbors 푢푘 into 푇 and recover its peeling weight 푁 (푢푘 ) gray<br>16 else // Case 2(b) : 푢푘 is white<br>Figure 7: Illustration of stale incremental maintenance 17 insert 푢푘 to 푂 ′<br>18 푘 = 푘 + 1<br>19 append 푂[푘 : 푖 ′ − 1] to 푂 ′ , where 푢푖′ = 푂[푖 ′ ] is the next black vertex<br>20 return 푂 ′ and arg max푆푖 푔(푆푖 )<br><!-- End of picture text -->



Correctness and accuracy guarantee. In Case 1 of T , if ∆푘 > ∆min, 푢min is chosen to insert to 푂<sup>′</sup> since it has the smallest peeling weight due to Lemma 4.2. In Case 3 of T , ∆푘 is the smallest peeling weight and 푢푘 is chosen to insert to 푂<sup>′</sup> . The peeling sequence is identical to that of 퐺 ⊕ ∆퐺, since in each iteration the vertex with the smallest peeling weight is chosen. The accuracy of the worst-case is preserved due to Lemma 2.1. 

reorder the sequence in batch with the last transaction ⃝4 , we are not required to change the positions of 푢푖 and 푢 푗 . 

Peeling weight recovery. Given a vertex 푢 푗 = 푂[푗] and a set of vertex 푆푖 (푖 < 푗, i.e., 푆 푗 ⊆ 푆푖), the peeling weight 푤푢 푗 (푆푖 ) can be calculated by 푤푢 푗 (푆푖 ) = ∆푗 +<sup>�</sup> (푖 ≤푘<푗)<sup>�</sup> ((푢 푗 ,푢푘 )∈퐸)<sup>푐</sup> 푗푘<sup>+�</sup> (푖 ≤푘<푗)<sup>�</sup> ((푢푘 ,푢 푗 )∈퐸)<sup>푐</sup> 푘푗<sup>.</sup> Vertex sorting. Intuitively, the increase in peeling weight of 푢푖 does not change the subsequence of 푂[1 : 푖 − 1] due to Lemma 4.1. We sort the vertices in ∆푉 by the indices in the peeling sequence. Then we reorder the vertices in ascending order of the indices in 푂. For simplicity, we color the vertices in ∆푉 black, affected vertices (i.e., vertices pending reordering) gray and unaffected vertices white. 

Time complexity. The complexity of the incremental maintenance is 푂(|퐸 T |+|퐸 T |log|푉T |). The complexity is bounded by 푂(|퐸|log|푉 |) and is small in practice. 

## 4.2 Peeling sequence reordering in batch 

Incremental maintenance in batch (Algorithm 2 and Figure 6). We initialize a pending queue 푇 to maintain the vertices pending reordering (Line 2). Iteratively, we add the vertex 푂[푖] ∈ ∆푉 to 푇 and color its neighbors 푂[푗] gray (Line 5-6). If 푇 is not empty, we compare the peeling weight ∆푘 of the vertex 푢푘 = 푂[푘] (푘 > 푖) with the peeling weight ∆min of the head of 푇 , 푢min. We consider the following two cases as shown in Figure 6. Case 1: If ∆min < ∆푘 , we pop 푢min from 푇 , insert it to 푂<sup>′</sup> and update the priorities of its neighbors in 푇 (Line 9-11); Case 2(a): if ∆min ≥ ∆푘 and 푢푘 is gray or black, we recover its peeling weight in 푆푘 ∪ 푇 and insert it to 푇 . Then we color the vertices in 푁 (푢푘 ) gray (Line 12-15); otherwise Case 2(b): if ∆min ≥ ∆푘 and 푢푘 is white, we insert 푢푘 to 푂<sup>′</sup> directly (Line 16-18). We repeat the above procedure until the pending queue 푇 is empty. Then we append 푂[푘 : 푖<sup>′</sup> − 1] to 푂<sup>′</sup> , where 푢푖<sup>′</sup> is the next vertex 

Since the peeling sequence reordering by early edge insertions could be reversed by later ones, some reorderings are stale and duplicate. Suppose that the insertion is a subgraph ∆퐺 = (∆푉, ∆퐸). A direct way to reorder the peeling sequence is to insert the edges one by one. The complexity is 푂(|∆퐸|(|퐸 T |log|푉T |)) which is time consuming. To reduce the amount of stale computation, we propose a peeling sequence reordering algorithm in batch. 

EXAMPLE 4.2. Consider a fraudulent community, 푆<sup>푃</sup> , identified by the peeling algorithm in Figure 7. 푢푖 and 푢 푗 are two normal users. Suppose that they have the same peeling weight and that 푢푖 is peeled before 푢 푗 . When a new transaction ⃝1 is generated, we should reorder 푢푖 and 푢 푗 by exchanging their positions. When ⃝2 and ⃝3 are inserted, positions of 푢푖 and 푢 푗 will be re-exchanged. However, if we 

in ∆푉 . We insert 푢푖<sup>′</sup> into 푇 and repeat the reordering until there is no black vertex. The correctness and accuracy guarantee are similar to those of peeling sequence reordering with edge insertion. Due to space limitations, we present them in Appendix D of [20]. Complexity. The time complexity of Algorithm 2 is 푂(|퐸 T |+|퐸 T | log|푉T |) which is bounded by 푂(|퐸|log|푉 |). 

## 4.3 Peeling sequence reordering with edge grouping 

Update steam ∆퐺<sup>휏</sup> . In a transaction system, the edge updates are coming in a stream manner (i.e., a timestamp on each edge) which is denoted by ∆퐺<sup>휏</sup> . Formally, we denote it by ∆퐺<sup>휏</sup> = [(푒0,휏0), . . . (푒푛,휏푛)] where 휏푖 is the timestamp on the edge 푒푖 = (푢푖,푣푖 ). 

Latency of activities L(∆퐺<sup>휏</sup> ). Suppose that 푒푖 = (푢푖, 푣푖 ) is a labeled fraudulent activity which is generated at 휏푖 and is responded/inserted at 휏푖<sup>푟. The latencyof 푒푖is 휏</sup> 푖<sup>푟−휏푖. Givenanupdatestream∆퐺휏, the</sup> latency of fraudulent activities is defined as follows. 



Prevention ratio R. If a fraudster is identified, we ban the following related transactions to prevent economic loss. We denote the ratio of suspicious transactions prevented to all suspicious transactions by R. 

EXAMPLE 4.3. Consider an update steam in Figure 8. 푒푖 (푖 ∈ [1, 6]) are a set of labeled fraudulent transactions and 휏푖 (푖 ∈ [1, 6]) are their timestamps. Regarding the reordering in batch, the new transactions are queueing until the size of the queue is equal to the batch size. The reordering is triggered at 휏푠 and finished at 휏푓 . Therefore, they are inserted at 휏푖<sup>푟= 휏푓The queueing time for each edge is</sup> 휏푠 − 휏푖 while the latency is 휏푓 − 휏푖 . Suppose the fraudster is identified . at 휏푓 , the prevention ratio is R =<sup>|{푒푖</sup> |{<sup>|휏</sup> 푒<sup>푖</sup> 푖<sup>></sup> }|<sup>휏푓}|</sup> 

Spade aims to reduce L and increase R as much as possible. In Figure 8, if the reordering is triggered at 휏푠 = 휏2 and responded at 휏푓 = 휏3, the following fraudulent activities can be prevented. 

Intuitively, some transactions are generated by normal users (benign edges), while others are generated by potential fraudsters (urgent edges). Spade groups the benign edges and reorders the peeling sequence in batch. It can both improve the performance of reordering and reduce the latency of the response to potential fraudulent transactions. We define the benign and urgent edges as follows. 

DEFINITION 4.1. Given an edge 푒 = (푢푖,푢 푗 ) and its weight 푐푖푗 , if 푤푢푖 (푆0) + 푐푖푗 ≥ 푔(푆<sup>푃</sup> ) or 푤푢 푗 (푆0) + 푐푖푗 ≥ 푔(푆<sup>푃</sup> ), 푒 is an urgent edge; otherwise 푒 is a benign edge. 

Given a benign edge insertion (푢푖,푢 푗 ), neither 푢푖 nor 푢 푗 belongs to the densest subgraph (Lemma 4.3). And the insertion cannot produce a denser fraudulent community by peeling algorithms (Lemma 4.4). 

LEMMA 4.3. Given an edge 푒 = (푢푖,푢 푗 ), if 푒 is a benign edge, after the insertion of 푒, 푢푖̸ ∈ 푆<sup>∗</sup> and 푢 푗̸ ∈ 푆<sup>∗</sup> . 

We denote the vertex subset returned after reordering by 푆<sup>푃′</sup> . 

LEMMA 4.4. Given a benign edge 푒 = (푢푖,푢 푗 ) insertion, at least one of the following two conditions is established: 1) 푢푖̸ ∈ 푆<sup>푃′</sup> and 푢 푗̸ ∈ 푆<sup>푃′</sup> ; and 2) 푔(푆<sup>푃′</sup> ) < 푔(푆<sup>푃</sup> ). 



<!-- Start of picture text -->
finish reordering<br>start reordering<br>τs τf<br>e1e2e3e4e5e6<br>. . . . . .<br>. . . τ1τ2τ3τ4τ5τ6 . . . τs τf Timeline<br>normal transaction fraudulent transaction<br>first time to be recognized<br><!-- End of picture text -->

Figure 8: Metrics for a set of fraudulent transactions made by a fraudster (latency: 휏푓 − 휏푖 , queueing time: 휏푠 − 휏푖 , prevention ratio: R = |{푒푖 |휏푖 >휏푓 }| |{푒푖 }| ) 

Algorithm 3: Paradigm of edge grouping 

Input: A graph 퐺 = (푉, 퐸), 푂, a density metric 푔(푆), ∆퐺<sup>푇</sup> Output: Peeling sequence order 푂<sup>′</sup> = 푄(퐺 ⊕ ∆퐺<sup>푇</sup> ) and fraudulent community 1 init an empty buffer ∆퐺 for updates 2 for 푖 = 1, . . . ,푚 do 3 ∆퐺.add(푒푖 ) 4 if 푒푖 is an urgent edge then 5 푂<sup>′</sup> = 푄(퐺 ⊕ ∆퐺) by Algorithm 2 6 clear ∆퐺 7 return 푂<sup>′</sup> and arg max푆푖 푔(푆푖 ) 

Table 3: Statistics of real-world datasets 

|Datasets||푉|||퐸||avg. degree|Increments|Type|
|---|---|---|---|---|---|
|Grab1|3.991M|10M|5.011|1M|Transaction|
|Grab2|4.805M|15M|6.243|1.5M|Transaction|
|Grab3|5.433M|20M|7.366|2M|Transaction|
|Grab4|6.023M|25M|8.302|2.5M|Transaction|
|Amazon [26]|28K|28K|2|2.8K|Review|
|Wiki-vote [25]|16K|103K|12.88|10.3K|Vote|
|Epinion [25]|264K|841K|6.37|84.1K|Who-trust-whom|



Therefore, we postpone the incremental maintenance of the peeling sequence for benign edges which provide two benefits. First, we can perform a batch update that avoids stale computation. Second, an urgent edge insertion, which is caused by a potential fraudster, triggers incremental maintenance immediately. These fraudsters are identified and reported to the moderators in real time. 

Edge grouping. We next present the paradigm of peeling sequence reordering by edge grouping. We first initialize an empty buffer ∆퐺 for the updates (Line 1). When an edge 푒푖 enters, we insert it into ∆퐺. If 푒푖 is an urgent edge, we incrementally maintain the peeling sequence by Algorithm 2 and clear the buffer (Line 4-6). 

## 5 Experimental Evaluation 

Our experiments are run on a machine that has an X5650 CPU, 16 GB RAM. The implementation is made memory-resident and implemented in C++. All codes are compiled by GCC-9.3.0 with -푂3. Datasets. We conduct the experiments on seven datasets (Table 3). Four industrial datasets are from Grab (Grab1-Grab4). Given a set of transactions, each transaction is represented as an edge. We replay the edges in the increasing order of their timestamp. If a user 푢푖 purchases from a store 푢 푗 , we add an edge (푢푖,푢 푗 ) to 퐸. Specifically, we construct the graph 퐺 as initialization (푉 and 90% of 퐸 as the initial graph), and the remaining 10% of 퐸 as increments for testing. The increments are decomposed into a set of graph updates ∆퐺 in the increasing order of their timestamp with different batch sizes |∆퐸|. We 

||Peeling|algorith|ms (seconds)||∆|퐸|= 1(푢푠|)||∆|퐸|= 10(푢|푠)||∆|퐸|= 100(|푢푠)||∆|퐸|= 1K (푢|푠)||∆퐸||= 100K|(푢푠)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Datasets|DG|DW|FD|IncDG|IncDW|IncFD|IncDG|IncDW|IncFD|IncDG|IncDW|IncFD|IncDG|IncDW|IncFD|IncDG|IncDW|IncFD|
|Grab1|12|14|12|6517|17469|6|3117|11613|6|519|1983|6|108|281|6|5|10|1|
|Grab2|17|20|16|6604|18413|8|3484|11280|8|634|1782|8|138|249|8|7|8|2|
|Grab3|23|27|22|6716|18862|11|3864|10892|11|750|1560|10|186|211|10|8|7|2|
|Grab4|27|28|28|6562|17469|14|4108|11661|12|878|1970|13|206|267|12|10|9|3|
|Amazon|0.49|0.53|0.43|350|342|1|186|191|-|29|30|-|7|6|-|-|-|-|
|Wiki-Vote|0.022|0.021|0.017|184|149|2|98|84|1|29|28|1|5|5|-|-|-|-|
|Epinion|0.25|0.26|0.23|170|151|5|83|80|3|32|30|2|10|10|2|1|1|-|



Table 4: Time taken for incremental maintenance with Spade by varying batch sizes (avg. time for one edge, - means < 1푢푠) 



<!-- Start of picture text -->
Peeling algorithms (seconds) |∆퐸 |= 1K (푢푠) Edge grouping (푢푠)<br>DG DW FD IncDG IncDW IncFD IncDGG IncDWG IncFDG<br>Datast<br>E L E L E L E L E L E L E L E L E L<br>Grab1 12 1 14 1 12 1 108 2.93 281 2.51 6 2.93 24 0.024 29 0.029 5 0.0042<br>Grab2 17 1 20 1 16 1 138 1.37 249 1.21 8 1.43 28 0.028 32 0.032 7 0.0050<br>Grab3 23 1 27 1 22 1 186 0.98 211 0.87 10 1.03 28 0.028 29 0.019 8 0.0066<br>Grab4 27 1 28 1 28 1 206 0.76 211 0.74 10 0.76 29 0.029 33 0.024 10 0.0073<br><!-- End of picture text -->

Table 5: Elapsed time (E) and latency (L) of static algorithms, incremental algorithms and edge grouping (E: The average elapsed time for one edge; L is defined by Equation 4. L of IncDG (resp. IncDW and IncFD) is normalized to L of DG (resp. DW and FD)) 



<!-- Start of picture text -->
 1 IncFDG  9×10 4 Static algos. vs Incremental algos.<br> 0.9 0.8 0.7 IncDW-1KIncDG-1KIncFD-1KIncDWGIncDGG  8 7 6×××101010 444 1010 1210 IncDWIncDGDWDG<br> 0.6 0.5 0.4  5 4 3×××101010 444 1010 86 IncFDFD<br> 0.3  2×10 4 10 4<br> 0.2 0.1 0 Latency (ms) 200  1 0××1010 40  0  500  1000  1500Degree 2000  2500  3000  3500 1010 20<br>(a) Prevention ratio vs. la-(b) Graph degree distribution<br>tency<br>Grab1 Grab2 Grab3 Grab4 Amazon Wiki-VoteEpinion<br>Prevention ratio Frequency Elapsed Time (us)<br><!-- End of picture text -->

Figure 9: Graph characteristic 

Figure 10: Efficiency comparison between peeling algorithms and corresponding incremental versions on Spade (|∆퐸|= 1) 

also use three popular open datasets including Amazon [26], Wikivote [25] and Epinion [25]. Since there are no timestamps on these three datasets, we randomly select 10% edges from 퐸 as increments for evaluation. 

Competitors. We choose three common peeling algorithms (DG, DW and FD) as a baseline. Given an edge insertion, these algorithms identify the fraudulent community on the entire graph from scratch. We demonstrate the performance improvement of our proposal (IncDG, IncDW and IncFD) implemented in Spade. We denote batch updates by IncDG-푥, IncDW-푥 and IncFD-푥, where 푥 = |∆퐸| is the batch size. We also denote the reordering of the peeling sequence with edge grouping by IncDGG, IncDWG and IncFDG. 

## 5.1 Efficiency of Spade 

Improvement of incremental peeling algorithms. We first investigate the efficiency of Spade by comparing the performance between incremental peeling algorithms and peeling algorithms. In Figure 10, our experiments show that IncDG (resp. IncDW and IncFD) is up to 4.17 × 10<sup>3</sup> (resp. 1.63 × 10<sup>3</sup> and 1.96 × 10<sup>6</sup> ) times faster than DG (resp. DW and FD) with an edge insertion. The reason for such a significant speedup is that only a small part of the peeling sequence is affected for most edge insertions. This is also consistent with the 

time complexity comparison of those algorithms. In fact, our algorithm on average processes only 3.5 × 10<sup>−4</sup> , 7.2 × 10<sup>−4</sup> and 2.5 × 10<sup>−7</sup> of edges compared with DG, DW and FD (on the entire graph), respectively. Spade identifies and maintains the affected peeling subsequence rather than recomputes the peeling sequence from scratch. Thus, Spade significantly outperforms existing algorithms. 

Impact of batch sizes |∆퐸|. We evaluate the efficiency of batch updates by varying batch sizes |∆퐸| from 1 to 100K. As shown in Table 4, IncDG-100K (resp. IncDW-100K and IncFD-100K) is up to 1211 (resp. 3448 and 4.47) times faster than IncDG (resp. IncDW and IncFD). When the batch size increases, the average elapsed time for an edge insertion keeps decreasing. As indicated in Example 4.2, the reordering of the peeling sequence by early edge insertions could be reversed by later ones. Reordering the peeling sequence in batch avoids such stale incremental maintenance by reducing the reversal. 

Impact of edge grouping. As shown in Table 5, IncDGG (resp. IncDWG and IncFDG) is up to 7.1 (resp. 9.7 and 1.25) times faster than IncDG1K (resp. IncDW-1K and IncFD-1K) since the edge grouping technique generally accumulates more than 1K edges. Another evidence is that the graph follows the power law, as shown in Figure 9b. Most edge insertions are benign and are processed in batch. Scalability. We next evaluate the scalability of Spade on Grab’ s datasets (Grab1-Grab4) of different sizes which is controlled by the 



<!-- Start of picture text -->
 1600 Grab1 Grab1  21 Grab1<br>Grab2  2400 Grab 2  18 Grab 2<br>Grab3 Grab3 Grab3<br>Grab4 Grab4  15 Grab 4<br> 1600<br> 800  12<br> 800  9<br> 6<br> 0 0  200  400  600  800  10 00  0 0  200  400  600  800  10 00  3 0  200  400  600  800  10 00<br>Batch size Batch size Batch size<br>(a) IncDG (b) IncDW (c) IncFD<br> 3 Grab1  3 Grab1  3 Grab1<br>Grab2 Grab2 Grab2<br>Grab3 Grab3 Grab3<br> 2 Grab 4  2 Grab 4  2 Grab 4<br> 1  1  1<br> 0 0  200  400  600  800  10 00  0 0  200  400  600  800  10 00  0 0  200  400  600  800  10 00<br>Batch size Batch size Batch size<br>(d) IncDG (e) IncDW (f) IncFD<br>Elapsed Time  (us) E Elapsed Time  (us) E Elapsed Time  (us) E<br>Latency  L Latency  L Latency  L<br><!-- End of picture text -->



<!-- Start of picture text -->
M1 M2 M3 M4 M5<br>. . . . . .<br>. . .<br>. . . . . .<br>U1 U2 U3 U4 U5<br>(a) Customer-merchant (b) Deal-hunter (c) Click-farming<br>collusion<br>(d) Details of Case(a)<br>1 18 738 # of transaction<br>720 transactions<br>. . . DG: continue . . . . . .<br>DG: start ban ban<br>IncDG: start IncDG: detect fraud at T1 DG: detect fraud at T2<br>T0 T1 = T0 + 1s T2 = T0 + 60s Timeline (T)<br><!-- End of picture text -->

Figure 11: Elapsed time and latency by varying batch sizes 

Figure 12: Case study: three fraud patterns 

number of edges |퐸|. We vary |퐸| from 10M to 25M as shown in Table 3 and report the results in Table 4. All peeling algorithms scale reasonably well with the increase of |퐸|. With |퐸| increasing by 2.5 times, the running time of Spade increases by up to 2 (resp. 2 and 3) times for DG (resp. DW and FD). 

We also compare the efficiency of DG, DW and FD. As shown in Columns 2 ∼ 4 of Table 4, the peeling algorithms have a similar performance. However, IncFD is much faster than IncDG and IncDW since the affected peeling subsequence is smaller due to the suspiciousness function of FD [19]. 

We investigate the details of the customer-mercant collusion in Figure 12(d). IncDG and DG start both at 푇0. Under the semantic of DG, the user becomes a fraudster at 푇1 (one second after 푇0). IncDG spots the fraudster at 푇1 with negligible delay. However, DG cannot detect this fraud at 푇1, as it is still evaluating the graph snapshot at 푇0. By DG, this fraudster will be detected after the second round detection of DG at 푇2 (about 60 seconds after 푇0). During the time period [푇1,푇2], there are 720 potential fraudulent transactions generated. Similar observations are made in the other two cases. Due to space limitations, they are presented in Appendix B of [20]. 

## 5.2 Effectiveness of Spade 

Latency. Our experiment reveals that when the batch size increases, the latency of the batch peeling sequence increases (shown in Figure 11). For example, the latency of IncDG (resp. IncDW and IncFD) is 0.76 (resp. 0.74 and 0.76). We remarked that 99.99% of the latency of IncDG, IncDW and IncFD is the queueing time, i.e., Spade accumulates enough transactions and processes them together. Furthermore, the latency in Grab1 is higher than that in Grab4. For example, the latency of IncFD in Grab1 (resp. Grab4) is 2.93 (resp. 0.76). This is because the queueing time on Grab1 is longer than that on Grab4. Prevention ratio. As shown in Figure 9a, the prevention ratio continues to decrease as latency increases on Grab’s datasets. Our results show that IncDGG (resp. IncDWG and IncFDG) can prevent 88.34% (resp. 86.53% and 92.47%) of fraudulent activities. IncDG-1퐾 (resp. IncDW-1퐾 and IncFD-1퐾) can prevent 28.6% (resp. 41.18% and 92.47%) of fraudulent activities by excluding queueing time. 

Case studies. We next present the effectiveness of Spade in discovering meaningful fraud through case studies in the datasets of Grab. There are three popular fraud patterns as shown in Figure 12. First, customer-merchant collusion is the customer and the merchant performing fictitious transactions to use the opportunity of promotion activities to earn the bonus (Figure 12(a)). Second, there is a group of users who take advantage of promotions or merchant bugs, called deal-hunter (Figure 12(b)). Third, some merchants recruit fraudsters to create false prosperity by performing fictitious transactions, called click-farming (Figure 12(c)). All three cases form a dense subgraph in a short period of time. 

## 6 Related work 

Dense subgraph mining. A series of studies have utilized dense subgraph mining to detect fraud, spam, or communities on social networks and review networks [19, 28, 29]. However, they are proposed for static graphs. Some variants [2, 13] are designed to detect dense subgraphs in dynamic graphs. [30] is proposed to spot generally dense subtensors created in a short period of time. Unlike these studies, Spade detects the fraudsters on both weighted and unweighted graphs in real time. Moreover, we propose an edge grouping technique which distinguishes potential fraudulent transactions from benign transactions and enables incremental maintenance in batch. 

Graph clustering. A common practice is to employ graph clustering that divides a large graph into smaller partitions for fraud detection. DBSCAN [14, 15] and its variant hdbscan [27] use local search heuristics to detect dense clusters. K-Means [12] is a clustering method of vector quantization. [34] detects medical insurance fraud by recognizing outliers. Unlike these studies, Spade is robust with worst-case guarantees in search results. Moreover, Spade provides simple but expressive APIs for developers, which allows their peeling algorithms to be incremental in nature on evolving graphs. Fraud detection using graph techniques. COPYCATCH [4] and GETTHESCOOP [22] use local search heuristics to detect dense subgraphs on bipartite graphs. Label propagation [33] is an efficient and effective method of detecting community. [9] explores link analysis to detect fraud. [32] and [10] explore the GNN to detect fraud on 

the graph. Unlike these studies, Spade detects fraud in real-time and supports evolving graphs. 

## 7 Conclusion 

In this paper, we propose a real-time fraud detection framework called Spade. We propose three fundamental peeling sequence reordering techniques to avoid detecting fraudulent communities from scratch. Spade enables popular peeling algorithms to be incremental in nature and improves their efficiency. Our experiments show that Spade speeds up fraud detection up to 6 orders of magnitude and up to 88.34% fraud activities can be prevented. 

The results and case studies demonstrate that our algorithm is helpful to address the challenges in real-time fraud detection for the real problems in Grab but also goes beyond for other graph applications as shown in our datasets. 

## Acknowledgments 

This work was funded by the Grab-NUS AI Lab, a joint collaboration between GrabTaxi Holdings Pte. Ltd. and National University of Singapore. We thank the reviewers for their valuable feedback. 

## References 

- [1] Distil networks: The 2019 bad bot report. https://www.bluecubesecurity.com/wp-content/uploads/bad-bot-report-2019LR.pdf. 

- [2] B. Bahmani, R. Kumar, and S. Vassilvitskii. Densest subgraph in streaming and mapreduce. Proceedings of the VLDB Endowment, 5(5), 2012. 

- [3] Y. Ban, X. Liu, T. Zhang, L. Huang, Y. Duan, X. Liu, and W. Xu. Badlink: Combining graph and information-theoretical features for online fraud group detection. arXiv preprint arXiv:1805.10053, 2018. 

- [4] A. Beutel, W. Xu, V. Guruswami, C. Palow, and C. Faloutsos. Copycatch: stopping group attacks by spotting lockstep behavior in social networks. In Proceedings of the 22nd international conference on World Wide Web, pages 119–130, 2013. 

- [5] D. Boob, Y. Gao, R. Peng, S. Sawlani, C. Tsourakakis, D. Wang, and J. Wang. Flowless: Extracting densest subgraphs without flow computations. In Proceedings of The Web Conference 2020, pages 573–583, 2020. 

- [6] M. Charikar. Greedy approximation algorithms for finding dense components in a graph. In International Workshop on Approximation Algorithms for Combinatorial Optimization, pages 84–95. Springer, 2000. 

- [7] C. Chekuri, K. Quanrud, and M. R. Torres. Densest subgraph: Supermodularity, iterative peeling, and flow. In Proceedings of the 2022 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA), pages 1531–1555. SIAM, 2022. 

- [8] J. Chen and Y. Saad. Dense subgraph extraction with application to community detection. IEEE Transactions on knowledge and data engineering, 24(7):1216– 1230, 2010. 

- [9] C. Cortes, D. Pregibon, and C. Volinsky. Computational methods for dynamic graphs. Journal of Computational and Graphical Statistics, 12(4):950–970, 2003. 

- [10] Y. Dou, Z. Liu, L. Sun, Y. Deng, H. Peng, and P. S. Yu. Enhancing graph neural network-based fraud detectors against camouflaged fraudsters. In Proceedings of the 29th ACM International Conference on Information and Knowledge Management (CIKM’20), 2020. 

- [11] Y. Dourisboure, F. Geraci, and M. Pellegrini. Extraction and classification of dense communities in the web. In Proceedings of the 16th international conference on World Wide Web, pages 461–470, 2007. 

- [12] R. O. Duda, P. E. Hart, et al. Pattern classification and scene analysis, volume 3. Wiley New York, 1973. 

- [13] A. Epasto, S. Lattanzi, and M. Sozio. Efficient densest subgraph computation in evolving graphs. In Proceedings of the 24th international conference on world wide web, pages 300–310, 2015. 

- [14] M. Ester, H.-P. Kriegel, J. Sander, X. Xu, et al. A density-based algorithm for discovering clusters in large spatial databases with noise. In kdd, volume 96, pages 226–231, 1996. 

- [15] J. Gan and Y. Tao. Dbscan revisited: Mis-claim, un-fixability, and approximation. In Proceedings of the 2015 ACM SIGMOD international conference on management of data, pages 519–530, 2015. 

- [16] D. Gibson, R. Kumar, and A. Tomkins. Discovering large dense subgraphs in massive graphs. In Proceedings of the 31st international conference on Very large data bases, pages 721–732. Citeseer, 2005. 

- [17] A. V. Goldberg. Finding a maximum density subgraph. 1984. [18] N. V. Gudapati, E. Malaguti, and M. Monaci. In search of dense subgraphs: How good is greedy peeling? Networks, 77(4):572–586, 2021. 

- [19] B. Hooi, H. A. Song, A. Beutel, N. Shah, K. Shin, and C. Faloutsos. Fraudar: Bounding graph fraud in the face of camouflage. In Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining, pages 895–904, 2016. 

- [20] J. Jiang, Y. Li, B. He, B. Hooi, J. Chen, and J. K. Z. Kang. Spade: A real-time fraud detection framework on evolving graphs (complete version). https://www.comp.nus.edu.sg/%7Ehebs/pub/spade-2022.pdf, 2022. 

- [21] M. Jiang, A. Beutel, P. Cui, B. Hooi, S. Yang, and C. Faloutsos. A general suspiciousness metric for dense blocks in multimodal data. In 2015 IEEE International Conference on Data Mining, pages 781–786. IEEE, 2015. 

- [22] M. Jiang, P. Cui, A. Beutel, C. Faloutsos, and S. Yang. Inferring strange behavior from connectivity pattern in social networks. In Pacific-Asia conference on knowledge discovery and data mining, pages 126–138. Springer, 2014. 

- [23] S. Khuller and B. Saha. On finding dense subgraphs. In International colloquium on automata, languages, and programming, pages 597–608. Springer, 2009. 

- [24] S. Kumar, W. L. Hamilton, J. Leskovec, and D. Jurafsky. Community interaction and conflict on the web. In Proceedings of the 2018 world wide web conference, pages 933–943, 2018. 

- [25] J. Leskovec, D. Huttenlocher, and J. Kleinberg. Signed networks in social media. In Proceedings of the SIGCHI conference on human factors in computing systems, pages 1361–1370, 2010. 

- [26] J. McAuley and J. Leskovec. Hidden factors and hidden topics: understanding rating dimensions with review text. In Proceedings of the 7th ACM conference on Recommender systems, pages 165–172, 2013. 

- [27] L. McInnes, J. Healy, and S. Astels. hdbscan: Hierarchical density based clustering. J. Open Source Softw., 2(11):205, 2017. 

- [28] Y. Ren, H. Zhu, J. Zhang, P. Dai, and L. Bo. Ensemfdet: An ensemble approach to fraud detection based on bipartite graph. In 2021 IEEE 37th International Conference on Data Engineering (ICDE), pages 2039–2044. IEEE, 2021. 

- [29] K. Shin, T. Eliassi-Rad, and C. Faloutsos. Corescope: Graph mining using k-core analysis—patterns, anomalies and algorithms. In 2016 IEEE 16th international conference on data mining (ICDM), pages 469–478. IEEE, 2016. 

- [30] K. Shin, B. Hooi, J. Kim, and C. Faloutsos. Densealert: Incremental densesubtensor detection in tensor streams. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pages 1057– 1066, 2017. 

- [31] C. Tsourakakis. The k-clique densest subgraph problem. In Proceedings of the 24th international conference on world wide web, pages 1122–1132, 2015. 

- [32] C. Wang, Y. Dou, M. Chen, J. Chen, Z. Liu, and S. Y. Philip. Deep fraud detection on non-attributed graph. In 2021 IEEE International Conference on Big Data (Big Data), pages 5470–5473. IEEE, 2021. 

- [33] M. Wang, C. Wang, J. X. Yu, and J. Zhang. Community detection in social networks: an in-depth benchmarking study with a procedure-oriented framework. Proceedings of the VLDB Endowment, 8(10):998–1009, 2015. 

- [34] K. Yamanishi, J.-I. Takeuchi, G. Williams, and P. Milne. On-line unsupervised outlier detection using finite mixtures with discounting learning algorithms. Data Mining and Knowledge Discovery, 8(3):275–300, 2004. 

- [35] C. Ye, Y. Li, B. He, Z. Li, and J. Sun. Gpu-accelerated graph label propagation for real-time fraud detection. In Proceedings of the 2021 International Conference on Management of Data, pages 2348–2356, 2021. 

## A Proofs of lemmas 

In this section, we provide all the formal proofs in Section 4 of the main paper. 

LEMMA 4.1. 푂<sup>′</sup> [1 : 푖 − 1] = 푂[1 : 푖 − 1]. 

PROOF. ∀푘 ∈ [1,푖 − 1], 푤푢푖 (푆푘 ) and 푤푢 푗 (푆푘 ) increase by ∆. Therefore, 푤푢푘 (푆푘 ) is still the smallest among 푆푘 . Hence, 푢푘 will be removed at 푘-th iteration. By induction, 푂<sup>′</sup> [1 : 푖 − 1] = 푂[1 : 푖 − 1]. □ 

LEMMA A.1. If 푆푖 ⊆ 푆 푗 and 푢푘 ∈ 푆푖, 푤푢푘 (푆 푗 ) ≥ 푤푢푘 (푆푖 ). 





PROOF. Consider a vertex 푢<sup>′</sup> ∈ 푇 ∪푆푘 , where 푢<sup>′̸</sup> = 푢푘 or 푢<sup>′̸</sup> = 푢min. 1) If 푢<sup>′</sup> ∈ 푆푘 , due to Lemma A.1, 푤푢<sup>′</sup> (푇 ∪푆푘 ) > 푤푢<sup>′</sup> (푆푘 ) > 푤푢푘 (푆푘 ) ≥ 푤푢푘 (푇 ∪푆푘 ) = ∆푘 > ∆min. 2) If 푢<sup>′</sup> ∈ 푇 , 푤푢<sup>′</sup> (푇 ∪푆푘 ) > 푤푢min (푇 ∪푆푘 ) = ∆min. Hence, 푢<sup>′</sup> is not the vertex that has the smallest peeling weight. Therefore, 푢min has the smallest peeling weight. □ 

LEMMA A.2. If ∃푢 ∈ 푆, such that 푤푢 (푆) < 푔(푆<sup>∗</sup> ), then 푆̸ = 푆<sup>∗</sup> . 

PROOF. We prove it in contradiction by assuming that 푆 = 푆<sup>∗</sup> . By peeling 푢 from 푆, we have the following. 



A better solution can be obtained by peeling 푢푖 from 푆<sup>∗</sup> . This contradicts the notion that 푆<sup>∗</sup> is the optimal solution. Hence, 푆푖̸ = 푆<sup>∗</sup> . □ 

LEMMA 4.3. Given an edge 푒 = (푢푖,푢 푗 ), if 푒 is a benign edge, after the insertion of 푒, 푢푖̸ ∈ 푆<sup>∗</sup> and 푢 푗̸ ∈ 푆<sup>∗</sup> . 

PROOF. We prove this lemma in contradiction by assuming that 푢푖 ∈ 푆<sup>∗</sup> . 푤푢푖 (푆<sup>∗</sup> ) ≤ 푤푢푖 (푆0) + 푐푖푗 < 푔(푆<sup>푃</sup> ) ≤ 푔(푆<sup>∗</sup> ). We have 푆<sup>∗̸</sup> = 푆<sup>∗</sup> due to Lemma A.2. We can conclude that 푢푖̸ ∈ 푆<sup>∗</sup> . Similarly, 푢 푗̸ ∈ 푆<sup>∗</sup> . □ 

LEMMA A.3. If ∃푢 ∈ 푆푖 , 푤푢 (푆푖) < 푔(푆푖), then 푆푖̸ = 푆<sup>푃</sup> . 

PROOF. We prove this in contradiction by assuming that 푆푖 = 푆<sup>푃</sup> . Suppose that 푢푖 is peeled from 푆푖. Hence, 푤푢푖 (푆<sup>푃</sup> ) ≤ 푤푢 (푆<sup>푃</sup> ) due to the peeling definition. The proof can be obtained as follows: 



LEMMA 4.4. Given a benign edge 푒 = (푢푖,푢 푗 ) insertion, at least one of the following two conditions is established: 1) 푢푖̸ ∈ 푆<sup>푃′</sup> and 푢 푗̸ ∈ 푆<sup>푃′</sup> ; and 2) 푔(푆<sup>푃′</sup> ) < 푔(푆<sup>푃</sup> ). 



<!-- Start of picture text -->
M1 M2 M3 M4 M5<br>. . . . . .<br>. . .<br>. . . . . .<br>U1 U2 U3 U4 U5<br>(a) Customer-merchant (b) Deal-hunter (c) Click-farming<br>collusion<br>(d) Details of Case(a)<br>1 18 738 # of transaction<br>720 transactions<br>. . . DG: continue . . . . . .<br>DG: start ban ban<br>IncDG: start IncDG: detect fraud at T1 DG: detect fraud at T2<br>T0 T1 = T0 + 1s T2 = T0 + 60s Timeline (T)<br>(e) Details of Case(b)<br>1 9 80 # of transaction<br>71 transactions<br>. . . DW: continue . . .<br>DW: start ban ban<br>IncDW: start IncDW: detect fraud at T1 DW: detect fraud at T2<br>T0 T1 = T0 + 0.7s T2 = T0 + 60s Timeline (T)<br>(f) Details of Case(c)<br>1 46 1899 # of transaction<br>1853 transactions<br>FD: continue<br>. . . . . .<br>FD: start ban ban<br>IncFD: start IncFD: detect fraud at T1 FD: detect fraud at T2<br>T0 T1 = T0 + 1.6s T2 = T0 + 60s Timeline (T)<br><!-- End of picture text -->

Figure 13: Case study: three fraud patterns 

PROOF. Without loss of generality, we assume 푖 ≤ 푗. We prove this in contradiction by assuming 푔(푆<sup>푃′</sup> ) ≥ 푔(푆<sup>푃</sup> ) and 푢푖 ∈ 푆<sup>푃′</sup> or 푢 푗 ∈ 푆<sup>푃′</sup> after inserting the edge 푒. 

Due to Lemma A.1 and 푆<sup>푃′</sup> ⊆ 푆0, we have 

푤푢푖 (푆<sup>푃′</sup> ) ≤ 푤푢푖 (푆0) < 푤푢푖 (푆0) + 푐푖푗 < 푔(푆<sup>푃</sup> ) < 푔(푆<sup>푃′</sup> ) (8) Therefore, 푆<sup>푃′</sup> is not the result returned by peeling algorithms due to Lemma A.3 which contradicts that 푆<sup>푃′</sup> maximizes 푔. 

□ 



<!-- Start of picture text -->
A dense subgraph G = Gs1 ⊕ Gs2 ⊕ Gs3 is returned<br>Gs1 Gs2 Gs3<br>4 4 4 4 4 4 3 3 3 3<br>g(G) = g(Gs1 ) = g(Gs2 ) = g(Gs3 ) = 3<br><!-- End of picture text -->

Figure 14: Multiple fraud instances 

take advantage of promotions or merchant bugs, called deal-hunter (Figure 13(b)). Third, some merchants recruit fraudsters to create false prosperity by performing fictitious transactions, called clickfarming (Figure 13(c)). All three cases form a dense subgraph in a short period of time. 

Customer-merchant collusion. We detail the customer-mercant collusion in Figure 13(d). IncDG and DG start both at 푇0. Under the semantic of DG, the user becomes a fraudster at 푇1 (one second after 푇0). IncDG spots the fraudster at 푇1 with negligible delay. However, DG cannot detect this fraud at 푇1, as it is still evaluating the graph snapshot at 푇0. By DG, this fraudster will be detected after the second round detection of DG at 푇2 (about 60 seconds after 푇0). During the time period [푇1,푇2], there are 720 potential fraudulent transactions generated. 

Deal-hunter. We investigate the details of customer-merchant collusion in Figure 13(e). IncDW and DW start both at 푇0. Under the semantic of DW, the user becomes a fraudster at 푇1 (0.7 second after 푇0). IncDW identifies the fraudster at 푇1 with negligible delay. However, DW cannot detect this fraud at 푇1, as it is still evaluating the graph snapshot at 푇0. By DW, this fraudster will be detected after the second round detection of DW at 푇2 (about 60 seconds after 푇0). During the time period [푇1,푇2], there are 71 potential fraudulent transactions generated. 

Click-farming. Last but not least, we present the details of clickfarming in Figure 13(f). IncFD and FD start both at 푇0. Under the semantic of FD, the group of users becomes fraudsters at 푇1 (1.6 second after 푇0). IncFD spots the fraudsters at 푇1 with negligible delay. However, FD cannot detect this fraud at 푇1, as it is still evaluating the graph snapshot at 푇0. By FD, these fraudsters will be detected after the second round detection of FD at 푇2 (about 60 seconds after 푇0). During the time period [푇1,푇2], there are 1853 potential fraudulent transactions generated. 

Consider a dense subgraph 퐺, it could consists of multiple fraud instances as shown in Figure 14. 퐺 consists of 퐺푠1 , 퐺푠2 and 퐺푠3 and all of their densities are equal to 3. Therefore, all will be returned, since they commonly form a dense subgraph 퐺. We enumerate these instances once new fraudsters are identified. 

Fraud enumeration. Figure 15 depicts the new fraudsters identified 

## B More case studies 

We next present the effectiveness of Spade in discovering meaningful fraud through case studies in the datasets of Grab. There are three popular fraud patterns as shown in Figure 13. First, customermerchant collusion is the customer and the merchant performing fictitious transactions to use the opportunity of promotion activities to earn the bonus (Figure 13(a)). Second, there is a group of users who 

by Spade in 28 timespans. Once new fraudsters are detected, Spade enumerates them and reports them to the moderators. In Figure 15, each bar represents the number of fraudulent instances are detected in the corresponding timespan. We investigated the detected fraudsters and found that most of their transactions corresponded to actual fraud, including customer-merchant collusion, deal-hunter and clickfarming. 



<!-- Start of picture text -->
Customer-merchant collusion Deal-hunter Click-farming<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 T12 T13 T14 T15 T16 T17 T18 T19 T20 T21 T22 T23 T24 T25 T26 T27 T28<br>Day 1 Day 2 Day 3 Day 4 Day 5 Day 6 Day 7<br>Timeline<br># of instances<br><!-- End of picture text -->

Figure 15: Spade spots and enumerates the new fraudsters. The appearances of dense subgraphs indicates various types frauds including customer-merchant collusion, deal-hunter and click-farming. We show that fraudulent instances are identified in a week. Each bar represents the number of fraudulent instances are detected in the corresponding timespan. The numbers are normalized to the number of fraudulent instances during the first timespan. 

## C Future extensions 

We discuss a few possible extensions of our current system, including edge deletion, enumeration and fraud detection within a given period of time. 

## C.1 Peeling sequence reordering with edge deletion 

The company will delete some outdated transactions since they are not of much value for fraud detection in some operational demands, e.g., some transactions generated several years ago. Given such an operational demand, we consider the extension of incremental maintenance with edge deletion of (푢푖,푢 푗 ) (without loss of generality, we assume 푖 < 푗). A straightforward solution is also to reorder the peeling sequence. We summarize the key steps as follows and leave the extension details of Spade in future work. 

Incremental algorithm (T<sup>푑</sup> ). T<sup>푑</sup> initializes an empty vector for the updated peeling sequence 푂<sup>′</sup> . Spade maintains a pending queue 푇 to store the vertices pending reordering. We iteratively compare 1) the head of 푇 , denoted by 푢min and 2) the vertex 푢푘 in the peeling sequence 푂, where 푘 < 푖. The corresponding peeling weights are denoted by ∆min and ∆푘 . We consider the following two cases. 

Case 1. If the peeling weight 푤푢푘 (푆0) > ∆min, we insert 푢푘 into 푇 and update the priorities in 푇 for the neighbors of 푢푘 , 푁 (푢max), 푘 = 푘 − 1. Case 2. If the peeling weight 푤푢푘 (푆0) ≤ ∆min, we append 푂[1 : 푘] to 푂<sup>′</sup> [1 : 푘]. 

While 푇 is non-empty, we iteratively compare 1) the head of 푇 and 2) the vertex 푢푘 in the peeling sequence 푂, where 푘 ≥ 푖 + 1. The incremental maintenance is identical to that of edge insertion in Section 4.1. Specifically, we consider the following three cases: Case 1. If ∆min < ∆푘 , we pop the 푢min from 푇 and insert it to 푂<sup>′</sup> . Then we update the priorities in 푇 for the neighbors of 푢min, 푁 (푢min). Case 2. If ∆min ≥ ∆푘 and ∃푢푇 ∈ 푇, (푢푇 ,푢푘 ) ∈ 퐸 or (푢푘,푢푇 ) ∈ 퐸, we insert 푢푘 into 푇 . The peeling weight is 푤푢푘 (푇 ∪ 푆푘 ) = ∆푘 + �(푢푇 ∈푇 )<sup>�</sup> ((푢푇 ,푢푘 )∈퐸)<sup>푐</sup> 푇푘<sup>+ �</sup> (푢푇 ∈푇 )<sup>�</sup> ((푢푘 ,푢푇 )∈퐸)<sup>푐</sup> 푘푇<sup>, 푘= 푘+ 1.</sup> Case 3. If ∆min ≥ ∆푘 and ∀푢푇 ∈ 푇, (푢푇 ,푢푘 )̸ ∈ 퐸 and (푢푘,푢푇 )̸ ∈ 퐸, we insert 푢푘 to 푂<sup>′</sup> , 푘 = 푘 + 1. 

We repeat the above iteration until 푇 is empty. 

EXAMPLE C.1. Consider the graph 퐺 in Figure 16 and its peeling sequence 푂 = [푢3,푢2,푢1,푢4,푢5]. Suppose that an outdated edge (푢1,푢5) is deleted from 퐺 as shown in the LHS of Figure 16. The reordering procedure is presented in the RHS of Figure 16. 푢1 is pushed to the pending queue 푇 . Since the peeling weights 푤푢2 (푆0) and 푤푢3 (푆0) are larger than the peeling weight of 푢1. 푢2 and 푢3 are inserted into 푇 . Since the peeling weight of 푢1 is less than that of 푢4, it will be appended to 푂<sup>′</sup> . Similarly 푢3 and 푢2 are appended to 푂<sup>′</sup> accordingly. Once 푇 is empty, the rest of the vertices, 푢4 and 푢5, in 푂 are appended to 푂<sup>′</sup> directly. Therefore, the reordered peeling sequence is 푂<sup>′</sup> = [푢1,푢3,푢2,푢4,푢5]. 

## C.2 Dense subgraph enumeration 

In case of the enumeration of dense subgraphs due to some operational demands, we consider both static graphs and dynamic graphs. Static graphs. Given a graph 퐺 = (푉, 퐸), peeling algorithm 푄 returns 푆<sup>푃</sup> . To enumerate dense subgraphs, we can perform the peeling algorithm 푄 by removing 푆<sup>푃</sup> from 퐺, denoted by 퐺<sup>′</sup> = (푉<sup>′</sup> , 퐸<sup>′</sup> ). Specifically, 푉<sup>′</sup> = 푉 \ 푆<sup>푃</sup> and 퐸<sup>′</sup> = 퐸 \ 퐸<sup>푃</sup> , where ∀(푢푖,푢 푗 ) ∈ 퐸<sup>푃</sup> ,푢푖 ∈ 푆<sup>푃</sup> or 푢 푗 ∈ 푆<sup>푃</sup> . Therefore, 푆<sup>푃′</sup> will be returned as the second densest subgraph. We can perform the peeling algorithm 푄 recursively to enumerate all dense subgraphs. 

It is remarkable that we do not have to compute 푆<sup>푃′</sup> from scratch. Instead, we can perform the incremental maintenance of edge deletion as introduced in Section C.1. 

Dynamic graphs. Given a graph 퐺 and graph updates ∆퐺 = (∆푉, ∆퐸), a straightforward solution is to reorder the peeling sequence by Algorithm 2 first. For the enumeration, we can think of this dynamic graph 퐺 ⊕ ∆퐺 as a static graph. 

## C.3 Fraud detection during some time period 

Given a graph 퐺 = (푉, 퐸) generated during a timespan [휏푠,휏푒 ] (휏푠 < 휏푒 ) and the peeling sequence 푂 = 푄(퐺). Taking a new graph 퐺<sup>′</sup> = (푉<sup>′</sup> , 퐸<sup>′</sup> ) generated during a timespan [휏푠<sup>′</sup> ,휏푒<sup>′</sup> ], we would like to identify the peeling sequence on 퐺<sup>′</sup> , i.e., 푂<sup>′</sup> = 푄(퐺<sup>′</sup> ). To simply our discussion, we denote a set of edges generated during timespan [휏푠,휏푒 ] by 퐸[푠,푒] 



<!-- Start of picture text -->
Peeling Sequence after reordering: O ′ = [u1, u3, u2, u4, u5]<br>Graph G and<br>O = [u3, u2, u1, u4, u5]<br>[u3, u2, u1, u4, u5] [u3, u2, u1, u4, u5] [u3, u2, u1, u4, u5] [u3, u2, u1, u4, u5]<br>u1 u3 u4<br>T T T T<br>2 4 2 1 4 O ′ u1 0 O ′ u1 2 O ′ u1 2 O ′ O ′<br>2 u2 4 u3 3 u1 u3 u2 u1 u3 u2 u4 u5<br>u2 u5 u2 6<br>deletion of (u1, u5)<br>LHS and1) u2recoveris insertedthe peelinginto T and2) u3recoveris insertedthe peelinginto T 3)fromPopT . u1, u3 and u2 4)pendedu4 andto Ou5 ′ whenare ap-T<br>weight of u1 weight of u2 is empty<br>RHS<br><!-- End of picture text -->

Figure 16: Peeling sequence reordering with edge deletion (A running example) 



<!-- Start of picture text -->
G ′ G G ′<br>Case 1<br>τs′ τe′ τs τe τs′ τe′ Timeline<br>G ′ Algo 2: insert E[s′,s]<br>E[s′ ,s] G E[e,e′ ] and E[e,e′]<br>Case 2<br>τs′ τs τe τe′ Timeline<br>G Sec B.1: delete E[s,s′]<br>E[s,s′ ] G ′ E[e′ ,e] and E[e′,e]<br>Case 3<br>τs τs′ τe′ τe Timeline<br>E[s′ ,s] G ′ G E[e,e′ ] SecAlgoB.1:2: insertdeleteEE[s[′e,s′,e] ]<br>Case 4<br>τs′ τs τe′ τe Timeline<br>E[s,s′ ] G G ′ E[e,e′ ] SecAlgoB.1:2: insertdeleteEE[e,e[s,s′]′]<br>Case 5<br>τs τs′ τe τe′ Timeline<br><!-- End of picture text -->



We use 푓퐸 (푆) to denote the total suspiciousness of the edges 퐸[푆] and 푓푉 (푆) to denote the total suspiciousness of 푆, i.e., 



and 

Figure 17: Fraud detection during some time period 

Case 1. If 휏푒<sup>′</sup> < 휏푠 or 휏푒 < 휏푠<sup>′</sup> , 퐺 and 퐺<sup>′</sup> do not overlap. Therefore, we directly apply the peeling algorithm 푄 on 퐺<sup>′</sup> . 

Case 2. If 휏푠<sup>′</sup> < 휏푠 and 휏푒 < 휏푒<sup>′</sup> , we perform Algorithm 2 by inserting two sets of edges, 퐸[푠′,푠] and 퐸[푒,푒′] to 퐺. Then we can identify the peeling sequence 푂<sup>′</sup> on 퐺<sup>′</sup> . 

Case 3. If 휏푠 < 휏푠<sup>′</sup> and 휏푒<sup>′</sup> < 휏푒 , we perform incremental maintenance in Section C.1 by deleting two sets of edges, 퐸[푠,푠′] and 퐸[푒′,푒] from 퐺. Then we can identify the peeling sequence 푂<sup>′</sup> on 퐺<sup>′</sup> . 

Case 4. If 휏푠<sup>′</sup> < 휏푠 < 휏푒<sup>′</sup> < 휏푒 , we perform Algorithm 2 by inserting a set of edges, 퐸[푠′,푠] to 퐺 and perform incremental maintenance in Section C.1 by deleting a set of edges 퐸[푒′,푒] from 퐺. 

Case 5. If 휏푠 < 휏푠<sup>′</sup> < 휏푒 < 휏푒<sup>′</sup> , we perform Algorithm 2 by inserting a set of edges, 퐸[푒,푒′] to 퐺 and perform incremental maintenance in Section C.1 by deleting a set of edges 퐸[푠,푠′] from 퐺. 



The density metric defined in Equation 9 satisfies Axiom 1-3. We adapted these basic properties from [21]. 

AXIOM 1. [Vertex suspiciousness] If 1) |푆 |= |푆<sup>′</sup> |, 2) 푓퐸 (푆) = 푓퐸 (푆<sup>′</sup> ), and 3) 푓푉 (푆) > 푓푉 (푆<sup>′</sup> ), then 푔(푆) > 푔(푆<sup>′</sup> ). 





With slight abuse of definition, we use 푔(푆(푉, 퐸)) to denote the total suspiciousness of 푆 on the graph 퐺 = (푉, 퐸). 

AXIOM 2. [Edge suspiciousness] If 푒 = (푢푖,푢 푗 )̸ ∈ 퐸, then 푔(푆(푉, 퐸∪ {푒 })) > 푔(푆(푉, 퐸)). 

## D Accuracy guarantee of Algorithm 2 

Correctness and accuracy guarantee. In Case 1, if ∆푘 > ∆min, 푢min is chosen to insert to 푂<sup>′</sup> since it has the smallest peeling weight due to Lemma 4.2. In Case 2(b), ∆푘 is the smallest peeling weight and 푢푘 is chosen to insert to 푂<sup>′</sup> . The peeling sequence is identical to that of 퐺 ⊕ ∆퐺, since in each iteration the vertex with the smallest peeling weight is chosen. The accuracy of the worst-case is preserved due to Lemma 2.1. 

## E Properties of density metrics 

Density metrics 푔. We adopt the class of metrics 푔 in previous studies [6, 18, 19], 푔(푆) =<sup>푓</sup> |푆<sup>(푆</sup> |<sup>), where푓is the total weightof 퐺[푆], i.e.,</sup> the sum of the weight of 푆 and 퐸[푆]: 





AXIOM 3. [Concentration] If |푆 |< |푆<sup>′</sup> | and 푓 (푆) = 푓 (푆<sup>′</sup> ), then 푔(푆) > 푔(푆<sup>′</sup> ). 

PROOF. 



## F Instances of Spade Spade 



<!-- Start of picture text -->
double vsusp(Vertex v, Graph g){<br>return g.weight[v]; //side information on vertex<br>}<br>double esusp(Edge e, Graph g){<br>return 1/log(g.deg[e.src]+5); //user-defined function<br>}<br>int main() {<br>Spade spade;<br>spade.VSusp(vsusp); //plug in vsusp (line 1-3)<br>spade.ESusp(esusp); //plug in esusp (line 4-6)<br>spade.TurnOnEdgeGrouping(); //enable edge grouping<br>spade.LoadGraph("graph_sample_path");<br>vector<Vertex> fraudsters = spade.Detect();<br>//edge insertions prepared by developers<br>vector<Edge> edge_insertions;<br>for(Edge e: edge_insertions){<br>fraudsters = spade.InsertEdge(e);<br>}<br>return 0;<br>}<br><!-- End of picture text -->

Instances of Spade Spade 1 2 We show that the popular peeling algorithms can be easily imple3 4 mented and supported by Spade, e.g., DG [6], DW [18] and FD [19]. 5 6 Instance 1. Dense subgraphs (DG) [6]. DG is designed to quantify 7 8 the connectivity of substructures. It is widely used to detect fake com9 ments [24] and fraudulent activities [3] on social graphs. Let 푆 ⊆ 푉 . 1011 The density metric of DG is defined by 푔(푆) =<sup>|퐸</sup> |<sup>[</sup> 푆<sup>푆</sup> |<sup>]|. To implement</sup> 1213 DG on Spade, developers only need to design and plug in the suspi1415 ciousness function esusp by calling ESusp. Specifically, esusp is a 16 17 constant function for edges, i.e., esusp(푢푖,푢 푗 ) = 1. 18 19 Instance 2. Dense weighted subgraphs (DW) [18]. On transaction graphs,20 there are weights on the edges in usual, such as the transaction amount. 

To implement FD on Spade, users only need to plug in the suspiciousness function vsusp for the vertices by calling VSusp and the suspiciousness function esusp for the edges by calling ESusp. Specifically, 1) vsusp is a constant function, i.e., given a vertex 푢, vsusp(푢) = 푎푖 and 2) esusp is a logarithmic function such that given an edge (푢푖,푢 푗 ), esusp(푢푖,푢 푗 ) = log(1푥+푐)<sup>,where푥isthedegreeof</sup> the object vertex between 푢푖 and 푢 푗 , and 푐 is a small positive constant [19]. 

�(푢푖,푢푗 )∈퐸[푆]<sup>푐</sup> 푖푗 The density metric of DW is defined by 푔(푆) = |푆 | , where 푐푖푗 is the weight of the edge (푢푖,푢 푗 ) ∈ 퐸. To implement DW, users only need to plug in the suspiciousness function esusp, i.e., given an edge, esusp(푢푖,푢 푗 ) = 푐푖푗 . 

Instance 3. Fraudar (FD) [19]. To resist the camouflage of fraudsters, Hooi et al. [19] proposed FD to weight edges and set the prior suspiciousness of each vertex with side information. Let 푆 ⊆ 푉 . The density metric of FD is defined as follows: 

Developers can easily implement customized peeling algorithms with Spade, which significantly reduces the engineering effort. For example, users write only about 20 lines of code (compared to about 100 lines in the original FD [19]) to implement FD as shown in List 2. Spade enables FD to be incrmental by nature. Similar observations are made in DG and DW. 



Listing 2: Implementation of FD on Spade 



