---
title: "The Explanation Game: Explaining Machine Learning Models Using Shapley Values"
authors: "unknown"
year: 2019
arxiv_id: "1909.08157"
original_file: "1909.08157.pdf"
pdf_path: "docs/papers\2019_unknown_the_explanation_game_explaining_mac.pdf"
---

# The Explanation Game: Explaining Machine Learning Models Using Shapley Values

**Authors:** Unknown et al.  
**Year:** 2019 | **arXiv:** [`1909.08157`](https://arxiv.org/abs/1909.08157)  
**Local PDF:** [`2019_unknown_the_explanation_game_explaining_mac.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2019_unknown_the_explanation_game_explaining_mac.pdf)

---

Anticommutative Engel algebras of the first five levels. 

# Yury Volkov 

### Abstract 

Anticommutative Engel algebras of the first five degeneration levels are classified. All algebras appearing in this classification are nilpotent Malcev algebras. 

Keywords: level of algebra, orbit closure, degeneration, nilpotent algebra. 2010 MSC: 17A01, 14J10, 14L30. 

## 1 Introduction 

Algebras in this paper are not assumed to be associative. The main object considered in this paper is the degeneration of algebras. Roughly speaking, the algebra A degenerates to the algebra B if there is a family of algebra structures parameterized by an element of the ground field such that infinitely many structures in the family represent A and there exists a structure belonging to this family representing B. Note that the notion of a degeneration is closely related to the notions of contraction and deformation. 

The notion of the level of an algebra was introduced in [5]. The algebra under consideration is an algebra of level n if the maximal length of a chain of non-trivial degenerations starting at it equals n. Roughly speaking, the level estimates the complexity of the multiplication of the given algebra. For example, the unique algebra of the level zero is the algebra with zero multiplication. 

Anticommutative algebras of the first level were classified correctly in [5] and all algebras of the first level were classified in [13] (see also [8]). In [6] the author introduced the notion of the infinite level. The infinite level can be expressed in terms of the usual level, and because of this the classification of algebras with a given infinite level is much easier than the classification of algebras with a given usual level. Anticommutative algebras of the second infinite level were classified in [6]. The classification of algebras of the third infinite level given in the same paper occurs to be incorrect and can not be taken in account. Finally, associative, Lie, Jordan, Leibniz and nilpotent algebras of the level two were classified in [12, 3] before the full classification of algebras of the second level appeared in [11]. 

This paper is a natural continuation of [11] and constitute the first natural step in the classification of algebras of the third level and of anticommutative algebras (or, more generally, algebras of the generation type 1) of the first five levels. Let us explain why this step is really constitute a part of these classifications. First of all, as explained in [11], it is natural to classify algebras depending on their generation type, i.e. the maximal dimension 

1 

2 Background on degenerations 

2 

of a one-generated subalgebra. Two main cases in the classification of algebras of the third level are the algebras of generation type 1 and the algebras of generation type 2. As it was shown in [11], there is also the case of generation type 3, but there are almost no algebras of level 3 with generation type 3 and we will leave this small part of classification for the paper where we will finish the classification of algebras of level 3. The case of generation type 2 requires some tedious calculations using the results of [10] and will be done in some of proceeding papers. The algebras of generation type 1 admit so-called one-dimensional standard In¨on¨u-Wigner contractions with respect to any element. These contractions are classified for algebras of generation type 1 until level 5 in [11]. In the same paper it is explained how obtain their classification until any level. It is natural for our aim to divide the algebras of generation type 1 to classes depending on what one-dimensional standard In¨on¨u-Wigner contractions they admit. If for an algebra A of generation type 1 a one-dimensional standard In¨on¨u-Wigner contraction of maximal possible level is nilpotent, then A is anticommutative and Engel. Since the classification of one-dimensional standard In¨on¨u-Wigner contractions presented in [11] is divided into nilpotent, solvable and non-solvable cases, it is natural to consider anticommutative Engel algebras first. This is exactly what we will do in this paper. Namely, we will classify these algebras until fifth level. We will also present the classification of anticommutative Engel algebras of the first five infinite levels that will easily follow from our classification and will not differ from it very much. Note that the class of anticommutative Engel algebras includes the class of anticommutative nilpotent algebras. In this paper we will show that until fifth level these classes coincide. 

Note that except the inclusion of one algebra of level four, the classification of anticommutative nilpotent algebras of the third infinite level that can be extracted from [6] is correct and coincides with the classification of anticommutative nilpotent algebras of the third level that we will obtain in this work. Thus, part of our results confirms the nilpotent part of the results of [6]. Contrariwise, the non-nilpotent part of the classification in [6] has more problems and will be corrected in our proceeding paper. 

## 2 Background on degenerations 

In this section we introduce some notation and recall some well known definitions and results about degenerations that we will need in this work. 

All vector spaces in this paper are over some fixed algebraically closed field k and we write simply dim, Hom and ⊗ instead of dimk, Homk and ⊗k. An algebra in this paper is simply a vector space with a bilinear binary operation called multiplication. This operation does not have to be associative unlike to the case of usual algebras. For an algebra A and a, b ∈ A we will denote the result of the application of multiplication to the pair (a, b) by ab. We will write also a<sup>2</sup> instead of aa. If V is a linear space and S is a subset of V , then we denote by ⟨S⟩ the subspace of V generated by S. For two subspace A1, A2 of A we set A1A2 := ⟨{a1a2}a1∈A1,a2∈A2⟩. 

Let V be a fixed n-dimensional space. Then the set of n-dimensional algebra structures on V is An = Hom(V ⊗V, V )<sup>∼</sup> = V<sup>∗</sup> ⊗V<sup>∗</sup> ⊗V . Any n-dimensional algebra can be represented by some element of An. Two algebras are isomorphic if and only if they can be represented by the same structure. The set An has a structure of the affine variety k<sup>n3</sup> . There is a natural action of the group GL(V ) on An defined by the equality (g ∗ µ)(x ⊗ y) = gµ(g<sup>−1</sup> x ⊗ g<sup>−1</sup> y) for x, y ∈ V , µ ∈An and g ∈ GL(V ). Two structures represent the same algebra if and only 

2 Background on degenerations 

3 

if they belong to the same orbit. By k<sup>n</sup> we will denote the n-dimensional algebra with zero multiplication and the structure representing it. For brevity, we will write µ(u, v) or, if the structure µ is clear from the context, even uv instead of µ(u ⊗ v) for u, v ∈ V . Let A and B be n-dimensional algebras. Suppose that µ, χ ∈An represent A and B respectively. We say that A degenerates to B and write A → B if χ belongs to O(µ). Here, as usually, O(X) denotes the orbit of X and X denotes the closure of X. We also write A̸ → B if χ̸ ∈ O(µ). We say that the degeneration A → B is trivial if A̸<sup>∼</sup> = B. We will write ∼ A −→= B to emphasize that the degeneration A → B is not trivial. 

Whenever an n-dimensional space named V appears in this paper, we assume that there is some fixed basis e1, . . . , en of V . In this case, for µ ∈An, we denote by µ<sup>k</sup> i,j<sup>(1⩽</sup> i, j, k ⩽ n) the structure constants of µ in this fixed basis, i.e. elements of k such that µ(ei, ej) = �n µ<sup>k</sup> i,j<sup>ek.Toprovedegenerationsandnondegenerationswewillusethesame</sup> k=1 technique that has been already used in [17] and [9, 10]. In particular, we will be free to use [9, Lemma 1] and facts that easily follow from it. This lemma asserts the following. If A → B, µ ∈An represents A and there is a closed subset R ⊂An invariant under lower triangular transformations of the basis e1, . . . , en such that µ ∈R, then there is a structure χ ∈R representing B. Invariance under lower triangular transformations of the basis e1, . . . , en means that if ω ∈R and g ∈ GL(V ) has a lower triangular matrix in the basis e1, . . . , en, then g ∗ ω ∈R (see [9] for a more detailed discussion). The mentioned lemma implies, in particular, that if A → B, then dim A<sup>2</sup> ⩾ dim B<sup>2</sup> . We will denote by Ann(A) the set of such a ∈ A that aA = Aa = 0. Another consequence of the mentioned lemma states that if A → B, then dim Ann(A) ⩽ dim Ann(B). More generally, let λ ∈ An be an n-dimensional algebra structure. For two subspaces U, W of V we will write λ(U, W ) for the subspace of V generated by λ(u, w) for all u ∈ U and w ∈ W . We also set Vi = ⟨ei, . . . , en⟩ for 1 ⩽ i ⩽ n + 1. Then a condition of the form λ(Vi, Vj) ⊂ Vk determines a closed subset of An invariant under lower triangular transformations of the basis e1, . . . , en. In particular, the condition dim A<sup>2</sup> ⩽ m is equivalent to the fact that A can be represented by a structure from the set {λ ∈An | λ(V, V ) ⊂ Vn−m+1} and the condition dim Ann(A) ⩾ m is equivalent to the fact that A can be represented by a structure from the set {λ ∈An | λ(V, Vn−m+1) + λ(Vn−m+1, V ) = 0}. If there are integer s and 1 ⩽ i1, . . . , is, j1, . . . , js, k1, . . . , ks ⩽ n such that 



satisfies the conditions O(µ) ∩R̸ = ∅ and O(χ) ∩R = ∅, where µ represents A and χ represents B, then we will write A̸ →(i1,j1,k1),...,(is,j1,k1) B to emphasize a reason for the corresponding non-degeneration. Note that dim A<sup>2</sup> = m < dim B<sup>2</sup> is equivalent to A̸ →(1,1,n−m+1) B and dim Ann(A) = m > dimAnn(B) is equivalent to A̸ →(n−m+1,1,n+1),(1,n−m+1,n+1) B. In some more complicated situation we will define R explicitly. 

In fact, in this paper we will mainly consider the closed subvariety ACn of the variety An formed by anticommutative algebra structures, i.e. structures µ such that µ<sup>k</sup> i,i<sup>=0and</sup> µ<sup>k</sup> i,j<sup>+ µk</sup> j,i<sup>=0forall1⩽i, j, k, ⩽n.InthiscasewewilldescribeRbyanexpressionof</sup> the form R = {λ ∈ACn | . . . }. Note that many things simplify in the anticommutative case. For example, dim Ann(A) = m > dimAnn(B) is equivalent to A̸ →(1,n−m+1,n+1) B for anticommutative algebras A and B. 

3 Generation type one and one-dimensional IW contractions 

4 

To prove degenerations, we will use the technique of contractions. Namely, let µ, χ ∈An represent A and B respectively. Suppose that there are some elements Ei<sup>t∈V(1⩽i⩽n,</sup> t ∈ k<sup>∗</sup> ) such that E<sup>t</sup> = (E1<sup>t, . . . , E</sup> n<sup>t)isabasisofVforanyt∈k∗andthestructure</sup> constants of µ in this basis are µ<sup>k</sup> i,j<sup>(t)forsomepolynomialsµk</sup> i,j<sup>(t) ∈k[t].If µk</sup> i,j<sup>(0) = χk</sup> i,j<sup>for</sup> all 1 ⩽ i, j, k ⩽ n, then A → B. To emphasize that the parameterized basis E<sup>t</sup> = (E1<sup>t, . . . , E</sup> n<sup>t)</sup> (t ∈ k<sup>∗</sup> ) gives a degeneration between algebras represented by the structures µ and χ, we E<sup>t</sup> will write µ −→ χ. Usually we will simply write down the parameterized basis explicitly above the arrow. 

An important role in this paper will be played by a particular case of a degeneration called a standard In¨on¨u-Wigner contraction (see [7]). We will call it IW contraction for short. Suppose that A0 is an m-dimensional subalgebra of the n-dimensional algebra A and µ ∈An is a structure representing A such that A0 corresponds to the subspace ⟨e1, . . . , em⟩ (e1,...,em,tem+1,...,ten) of V . Then µ −−−−−−−−−−−−−→ χ for some χ ∈An and the algebra B represented by χ is called the IW contraction of A with respect to A0. The isomorphism class of the resulting algebra does not depend on the choice of the structure µ satisfying the condition stated above and always has an ideal I ⊂ B and a subalgebra B0 ⊂ B such that B = B0 ⊕ I as a vector space, I<sup>2</sup> = 0 and B0<sup>∼</sup> = A0 as an algebra. We will call an algebra of such a form a trivial singular extension of A0 by k<sup>n−m</sup> . 

To finish this section, let us introduce the notion of a level related to the notion of a degeneration. This notion will be the main object of interest in this paper. 

Definition 2.1. The level of the n-dimensional algebra A is the maximal number m such that there exists a sequence of non-trivial degenerations A −→∼= Am−1 −→∼= . . . −→∼= A1 −→∼= A0 for some n-dimensional algebras Ai (0 ⩽ i ⩽ m − 1). The level of A is denoted by lev(A). The infinite level of the algebra A is the number defined by the equality lev∞(A) = mlim→∞<sup>lev(A ⊕km).</sup> 

The aim of this paper is to classify up to isomorphism the anticommutative Engel algebras with level not greater than 5. This will automatically give us also the classification of algebras with infinite level not greater than 5 in the same variety. 

## 3 Generation type one and one-dimensional IW contractions 

In this section we recall some general ideas of [11] on how to classify algebras of small levels. Let us first recall the definition of a generation type. 

Definition 3.1. Let A be an n-dimensional algebra. For a ∈ A, we denote by A(a) the subalgebra of A generated by a. The generation type of A is the dimension of a maximal 1-generated subalgebra of A, i.e. the number G(A) defined by the equality G(A) = max �dim A(a)�. a∈A 

By the results of [11], if G(A) ⩾ 3 for an n-dimensional algebra A, then lev(A) ⩾ G(A). Moreover, there are no many algebras with G(A) = 3 that can have level 3 and all of them are described in the same work. Thus, the main problems in the classification of algebras of level 3 are the classifications of algebras of level 3 with generation types one and two. Moreover, a more detailed consideration would show that this cases constitute the main parts of classifications of algebras of levels not greater than 5. The case of generation type 2 

3 Generation type one and one-dimensional IW contractions 

5 

will be considered in one of our proceeding works and at this moment it seems to be difficult to classify algebras with generation type 2 that have levels four and five. Nevertheless, we are going to classify algebras with generation type one that have levels not greater than 5. The first part of this classification we present in this paper. 

Definition 3.2. The algebra A is called anticommutative if a<sup>2</sup> = 0 for any a ∈ A. The algebra A is called nilpotent if there exists m such that A<sup>m</sup> = 0, where we define A<sup>i</sup> by induction on i ⩾ 1 in the following way. We set A<sup>1</sup> = 1 and A<sup>i</sup> = A(A<sup>i−1</sup> ) + (A<sup>i−1</sup> )A for i > 1. The algebra A is called m-Engel if (La)<sup>m</sup> = 0 for any a ∈ A. We will call the algebra A Engel if it is m-Engel for some m > 0. 

Let A be an n-dimensional algebra. If G(A) = 1, then for any a ∈ A the IW contraction of A with respect to A(a) is defined. We will denote the resulting algebra by IWa(A). Algebras of the form IWa(A) with G(A) = 1 and a ∈ A were studied in [11]. Their degenerations are well understood due to the results of the last mentioned paper. It is natural to consider separately the case where IWa(A) is nilpotent for any a ∈ A and the case where there exists a ∈ A such that IWa(A) is not nilpotent. Since in the first case the algebra A clearly does not have idempotents, it is anticommutative. During this paper, for a ∈ A, we will denote by La the operator of left multiplication by a, i.e. La is a linear map from A to itself defined by the equality La(b) = ab for b ∈ A. For anticommutative A, the nilpotence of IWa(A) is equivalent to the nilpotence of the operator induced by La on the space A/⟨a⟩. Note that dim A/⟨a⟩ = n − 1. Hence, if IWa(A) is nilpotent, then L<sup>k</sup> a<sup>(A)⊂⟨a⟩forsome</sup> integer 0 < k < n. On the other hand, if L<sup>k</sup> a<sup>(b)=αaforsomeb∈Aandα∈k∗,</sup> then IWLka−1(b)<sup>(A)isnotnilpotentthatcontradictsourassumptions.Thus,AisEngeland</sup> the minimal integer m such that (La)<sup>m</sup> = 0 for all a ∈ A is the same as the minimal integer such that IWa(A)<sup>m+1</sup> = 0 for all a ∈ A. Thus, the consideration of algebras with generation type one that have only nilpotent one-dimensional IW contractions is equivalent to the consideration of anticommutative Engel algebras. This motivated us to classify first anticommutative Engel algebras until the fifth level. 

Remark 3.3. It is clear that any nilpotent algebra is Engel. It follows also from [15, Theorem 4] that any finite dimensional anticommutative 3-Engel algebra is nilpotent. On the other hand, due to the examples of [14] finite dimensional anticommutative 4-Engel algebra does not have to be nilpotent. 

Lemma 3.4. Let A be an n-dimensional anticommutative Engel algebra. There exists c ∈ A such that IWc(A) → IWa(A) for any a ∈ A. 

Proof. For a ∈ A, we denote by rm(a) the rank of the operator (La)<sup>m</sup> . Due to the results of [11], IWa(A) → IWb(A) if and only if rm(a) ⩾ rm(b) for any m > 0. Let us pick c such that IWa(A)̸ → IWc(A) whenever IWa(A)̸<sup>∼</sup> = IWc(A) for some a ∈ A. Suppose that IWc(A)̸ → IWb(A) for some b ∈ A. This means that rm0(b) > rm0(c) for some m0 > 0. Let us consider the elements c + αb with α ∈ k. Since the condition rm(x) ⩾ max(rm(b), rm(c)) determines an open subset of A considered as a affine variety k<sup>n</sup> with Zariski topology, for a fixed m, we have rm(c + αb) ⩾ max(rm(b), rm(c)) for all α ∈ k except a finite number of values. Since the mentioned inequality is satisfied for m > n, there exists α ∈ k such that rm(c + αb) ⩾ max(rm(b), rm(c)) for any m > 0. Since rm0(c + αb) > rm0(c), we have IWc+αb(A)̸<sup>∼</sup> = IWc(A). On the other hand, it follows from the argument above that IWc+αb(A) → IWc(A) that contradicts the choice of c. 

4 Nilpotent one-dimensional IW contractions of small levels 

6 

It follows from Lemma 3.4 that any n-dimensional anticommutative Engel algebra A has a unique one-dimensional IW contraction of maximal level. We will denote this contraction by IW1<sup>max</sup> (A). We will use in this paper also the next auxiliary fact. 

Lemma 3.5. Let A and B be n-dimensional anticommutative Engel algebras. If A → B, then IW1<sup>max</sup> (A) → IW1<sup>max</sup> (B). 

Proof. Let us denote by L<sup>B</sup> b<sup>:B→Btheoperatorofleftmultiplicationbyb∈Bandby</sup> L<sup>A</sup> a<sup>:A →Atheoperatorofleftmultiplicationbya ∈A.IfIW</sup> 1<sup>max</sup> (A)̸ → IW1<sup>max</sup> (B), then there is some b ∈ B and integer m such that the rank R of (L<sup>B</sup> b<sup>)mis greater than the rank of</sup> (L<sup>A</sup> a<sup>)mfor any a ∈A.It is not difficultto see that the set of structuresrepresentingalgebras</sup> C such that the rank of (L<sup>C</sup> c<sup>)mislessthanRforanyc∈CisaclosedsubsetofACn.It</sup> is clear that A can be represented by a structure from this subset and B cannot. Thus, A̸ → B. 

## 4 Nilpotent one-dimensional IW contractions of small levels 

From here on we consider only anticommutative Engel algebras. Any algebra that will appear is assumed to be so if the opposite is not stated. 

Our strategy is to classify separately algebras with different IW1<sup>max</sup> (A). Note that lev�IW1<sup>max</sup> (A)� ⩽ lev(A), and hence to classify anticommutative Engel algebras of the first five levels, we need the classification of their possible one-dimensional IW contractions until level five. Such a classification is presented in [11] and we give it here with small changes corresponding to permutations of basic elements. Table 1. Nilpotent one-dimensional IW contractions of algebras with generation type 1 of the first 5 levels. 

|level|notation|multiplication table|dimension|
|---|---|---|---|
|1|n3|e1e2 =en|n⩾3|
|2|T <sup>3</sup><br>T <sup>2,2</sup>|e1e2 =e3, e1e3 =e4<br>e1e2 =en−1, e1e3 =en|n= 4<br>n⩾5|
|3|T <sup>3</sup><br>T <sup>2,2,2</sup>|e1e2 =e3, e1e3 =en<br>e1ei+1 =ei+n−3, 1⩽i⩽3|n⩾5<br>n⩾7|
||T <sup>4</sup>|e1ei =ei+1, 2⩽i⩽4|n= 5|
|4|T <sup>3,2</sup>|e1e2 =en−1, e1e3 =e4, e1e4 =en|n⩾6|
||T <sup>2,2,2,2</sup>|e1ei+1 =ei+n−4, 1⩽i⩽4|n⩾9|
|5|T <sup>4</sup><br>T <sup>3,3</sup><br>T <sup>3,2,2</sup>|e1e2 =e3, e1e3 =e4, e1e4 =en<br>e1ei =ei+1, i∈{2,3,5,6}<br>e1e2 =en−2, e1e3 =en−1, e1e4 =e5, e1e5 =en|n⩾6<br>n= 7<br>n⩾8|
||T <sup>2,2,2,2,2</sup>|e1ei+1 =ei+n−5, 1⩽i⩽5|n⩾11|



Here and in all other multiplication tables, we give only nonzero products of the form eiej with i < j. The values of products of basic elements that are not determined by the given ones and the anticommutativity are zero. 

It follows from the results of [11] that if IW1<sup>max</sup> (A) can be represented by n3, then A is isomorphic to one of the Heisenberg Lie algebras defined in the next table. 

5 Algebras with maximal IW contraction T<sup>2,2</sup> 

7 

||T|able 2. Heisenberg Lie algebras.||
|---|---|---|---|
|level|notation|multiplication table|dimension|
|m|ηm|e2i−1e2i =e2m+1, 1⩽i⩽m|n⩾2m+ 1|



This immediately gives the classification of anticommutative Engel algebras of level two. 

Theorem 4.1 ([11]). Let A be an n-dimensional anticommutative Engel algebra of level two. Then either n = 4 and A can be represented by T<sup>3</sup> or n ⩾ 5 and A can be represented by T<sup>2,2</sup> or η2. 

Since, for an algebra A of level not greater than 5 such that IW1<sup>max</sup> (A) has level five, one obviously has A<sup>∼</sup> = IW1<sup>max</sup> (A), we need to consider algebras with IW1<sup>max</sup> (A) represented by a structure from the set {T<sup>2,2</sup> , T<sup>2,2,2</sup> , T<sup>2,2,2,2</sup> , T<sup>3</sup> , T<sup>3,2</sup> , T<sup>4</sup> } to finish our classification. All of these algebras except T<sup>4</sup> are 3-Engel, and hence nilpotent by Remark 3.3. Moreover, we need to consider the case of the algebra T<sup>4</sup> only in the dimension 5. Note that any nilpotent algebra A can be represented by a structure µ ∈An such that µ<sup>k</sup> i,j<sup>=0fork⩽max(i, j).Notethatifv∈VissuchthatIWv(µ)∼=IW</sup> 1<sup>max</sup> (µ), then IWe1+αv(µ)<sup>∼</sup> = IW1<sup>max</sup> (µ) for all α ∈ k except finite number of values (see the proof of Lemma 3.4). Thus, we may assume that µ<sup>k</sup> i,j<sup>= 0 for k⩽max(i, j) and IWe</sup> 1<sup>(µ) ∼= IW</sup> 1<sup>max</sup> (µ) at the same time. Note that this properties are preserved with respect to lower triangular transformations g ∈ GL(V ) such that g(e1) = e1. Then we may assume that IWe1(µ) is exactly one of the structures described in Table 1 up to some permutation of the basic elements e2, . . . , en. Later in all cases, except the case IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>4</sup> , we will represent A by a structure µ satisfying the described conditions. 

## 5 Algebras with maximal IW contraction T<sup>2,2</sup> 

This section is devoted to the classification of algebras A such that IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2</sup> . 

m ���� Let us start with a general observation about algebras A such that IW1<sup>max</sup> (A)<sup>∼</sup> = T 2,...,2, where m is an arbitrary integer. Such an algebra can be represented by a structure µ such that µ(e1, eir ) = ejr and µ(e1, ei) = 0 for i̸ ∈{i1, . . . , im}, where 2 ⩽ i1, . . . , im, j1, . . . , jm ⩽ n are 2m different integers such that ir < jr for all 1 ⩽ r ⩽ m. Without loss of generality we will assume that 2 ⩽ i1 < · · · < im ⩽ n. We may assume that at the same time µ<sup>k</sup> i,j<sup>=0if</sup> k ⩽ max(i, j). 

Lemma 5.1. In the settings described above 

1. if µ<sup>k</sup> i,j̸<sup>= 0forsome2 ⩽i, j, k⩽n,theneitherk∈{j1, . . . , jm}ori, j∈{i1, . . . , im};</sup> 



Proof. 1. Suppose that k̸ ∈{j1, . . . , jm} and j̸ ∈{i1, . . . , im}. Let us consider the element vα = e1 + αei for α ∈ k. Note that Lvα(eir ) = ejr + αµ(ei, eir ) and Lvα(ej) = αµ(ei, ej). Hence, the matrix of Lvα in the basis e1, . . . , en contains the (m + 1) × (m + 1) minor 



5 Algebras with maximal IW contraction T<sup>2,2</sup> 

8 

which is a polynomial in α with coefficient of the term α equal to αµ<sup>k</sup> i,j<sup>.Thismeans</sup> that this polynomial is not constantly zero, and hence, for some α ∈ k, the rank of m ���� Lvα is not less than m + 1 that contradicts IW1<sup>max</sup> (A)<sup>∼</sup> = T 2,...,2. 

2. By our assumptions, we have (Le1+ei)<sup>2</sup> = (Le1)<sup>2</sup> = (Lei)<sup>2</sup> = 0, and hence Le1Lei + LeiLe1 = 0. On the other hand, 

(Le1Lei + LeiLe1)(eis) = µ�e1, µ(ei, eis)� + µ(ei, ejs). 

Calculating the coefficient of ejr in the obtained expression, one gets the required equality. 

m ���� Corollary 5.2. If IW1<sup>max</sup> (A)<sup>∼</sup> = T 2,...,2, then A can be represented by a structure µ such that µ(e1, ei+1) = ei+n−m for 1 ⩽ i ⩽ m, µ(e1, ei) = 0 for m + 2 ⩽ i ⩽ n and µ<sup>k</sup> i,j<sup>=0if</sup> k ⩽ max(i, j). Proof. It is enough to take the structure µ described above and consider it in the basis e1, ei1, . . . , eim, ek1, . . . , ekn−2m−1, ej1, . . . , ejm, where k1, . . . , kn−2m−1 are all elements of {2, . . . , n} \ {i1, . . . , im, j1, . . . , jm} in the increasing order. Lemma 5.1 guarantees that the new structure µ˜ still satisfies the condition µ˜<sup>k</sup> i,j<sup>= 0fork⩽max(i, j).</sup> 

Let us now return to the case IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2</sup> . Let us introduce the algebra 



Let U be an (n − 2)-dimensional vector space and φ : U × U → k<sup>2</sup> be a skew-symmetric bilinear map. We define a binary product on the space U ⊕k<sup>2</sup> by the equality (u1, v1)(u2, v2) = �0, φ(u1, u2)� and denote the resulting algebra by U ⋉φ k<sup>2</sup> . 

Corollary 5.3. One has IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2</sup> if and only if A either can be represented by T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2)orisisomorphic toU ⋉φk2forsome (n−2)-dimensionalvectorspaceUandsome</sup> surjective skew-symmetric bilinear map φ : U × U → k<sup>2</sup> . 

Proof. It is easy to check that IW1<sup>max</sup> �T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2)</sup> � = T<sup>2,2</sup> . If A<sup>∼</sup> = U ⋉φ k<sup>2</sup> , then clearly A<sup>3</sup> = 0, dim A<sup>2</sup> = 2, and hence IW1<sup>max</sup> (A) can be represented either by n3 or by T<sup>2,2</sup> . But in the first case, one has A<sup>∼</sup> = ηm for some integer m and, in particular, dim A<sup>2</sup> = 1. The obtained contradiction shows that IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2</sup> . 

Suppose now that IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2</sup> . Let us represent A by a structure µ satisfying conditions of Corollary 5.2. Lemma 5.1 implies that µ<sup>k</sup> i,j<sup>=0ifk<n −1,2⩽i, j⩽n</sup> and {i, j}̸ = {2, 3}. By the same lemma, we have also µ(V, en−1) = µ(V, en) = 0. Hence, if µ<sup>k</sup> 23<sup>= 0 for k< n−1, then A ∼= U⋉φk2 for some (n−2)-dimensional vector space Uand some</sup> surjective skew-symmetric bilinear map φ : U × U → k<sup>2</sup> . Suppose now that µ<sup>k</sup> 23̸<sup>= 0 for some</sup> k < n−1. Changing the basis, we may assume that µ(e2, e3) = en−2. Since (Le2)<sup>2</sup> = (Le3)<sup>2</sup> = 0, we have µ(e2, en−2) = µ(e3, en−2) = 0. Since dim Im Le2 ⩽ 2, µ(e2, e1) = −en−1 and µ(e2, e3) = en−2, we have Im Le2 = ⟨en−2, en−1⟩. Analogously, Im Le3 = ⟨en−2, en⟩. Then we have µ(e2, ei) = µ2<sup>n</sup> ,i<sup>−1en−1 and µ(e3, ei) = µ</sup> 3<sup>n</sup> ,i<sup>en for 4 ⩽i ⩽n−3.Since Le</sup> 2<sup>+e</sup> 3<sup>(e1) = en−1+en,</sup> 

5 Algebras with maximal IW contraction T<sup>2,2</sup> 

9 

Le2+e3(e3) = en−2, Le2+e3(ei) = µ2<sup>n</sup> ,i<sup>−1en−1 + µ</sup> 3<sup>n</sup> ,i<sup>enanddim Im Le</sup> 2<sup>+e</sup> 3<sup>⩽2,one has µ</sup> 2<sup>n</sup> ,i<sup>−1</sup> = µ<sup>n</sup> 3,i for all 4 ⩽ i ⩽ n − 3. 

Replacing ei by ei + µ2<sup>n</sup> ,i<sup>−1e1= ei +µ</sup> 3<sup>n</sup> ,i<sup>e1for 4 ⩽i ⩽n−3, we may assume that µ(e2, ei) =</sup> µ(e3, ei) = 0 for 4 ⩽ i ⩽ n. Let us pick some 4 ⩽ i ⩽ n − 2. Since Le2+ei(e1) = −en−1, Le2+ei(e3) = en−2 and dim Im Le2+ei ⩽ 2, one has µ(ei, ej) ⊂⟨en−1⟩ for all 4 ⩽ j ⩽ n − 2. Considering Le3+ei, we get also µ(ei, ej) ⊂⟨en⟩. Thus, µ(ei, ej) = 0 for 4 ⩽ i, j ⩽ n − 2, and hence all nonzero products of basic elements are µ(e1, e2) = en−1, µ(e1, e3) = en and µ(e2, e3) = en−2, i.e. µ = T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2).</sup> 

The classification of algebras of the form U ⋉φ k<sup>2</sup> is strongly related to the classification of skew-symmetric matrix pairs considered, for example, in [1, 4, 16]. In fact, one has to factorize the classification obtained in these papers by an action of the group GL(k<sup>2</sup> ). In terms of the algebra U ⋉φ k<sup>2</sup> , this action is defined by the equality g ∗ (U ⋉φ k<sup>2</sup> ) = U ⋉gφ k<sup>2</sup> for g ∈ GL(k<sup>2</sup> ). All the mentioned works consider the case char k̸ = 2 while the more complicated characteristic two case is considered in [18] in a little more general settings than here. The deformation theory of skew-symmetric matrix pairs was considered in [2]. In our settings this problem differs a little but it still seems to be possible to give the general criteria of degenerations between algebras of the form U ⋉φ k<sup>2</sup> . In the current paper we will not solve this general problem and restrict us to the classifications of such algebras having level not greater than five. To do this we introduce the list of algebras below. 



Note that T<sup>2,2</sup> (ǫ<sup>n</sup> 34<sup>)∼=n</sup> 3<sup>⊕n</sup> 3<sup>.Toshowthisonehastosimplyreplacee</sup> 1<sup>bye</sup> 1<sup>+ e</sup> 4<sup>.It</sup> was stated in [6] that this algebra has level three. We will show that in fact it has level four while this result is not new, see, for example, [17]. Lemma 5.4. One has T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>)</sup> −→∼= T<sup>2,2</sup> (ǫ<sup>n</sup> 34<sup>)</sup> −→∼= T<sup>2,2</sup> (ǫ<sup>n</sup> 24<sup>)</sup> −→∼= T<sup>2,2</sup> . In particular, lev�T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>)</sup> � ⩾ 5. 

Proof. Since IWe1�T<sup>2,2</sup> (ǫ<sup>n</sup> 24<sup>)</sup> � = T<sup>2,2</sup> and T<sup>2,2</sup> (ǫ<sup>n</sup> 24<sup>)̸ ∼= T 2,2,wehaveT 2,2(ǫn</sup> 24<sup>)</sup> −→∼= T 2,2. Let us now construct the remaining degenerations. One has 



Since T<sup>2,2</sup> (ǫ<sup>n</sup> 24<sup>)̸→</sup> (1,3,n),(3,3,n+1)<sup>T 2,2(ǫn</sup> 34<sup>)̸→</sup> (1,5,n+1)<sup>T 2,2(ǫ</sup> 45<sup>n),theconstructeddegenerations</sup> are non-trivial. 

Lemma 5.5. Suppose that A<sup>∼</sup> = U ⋉φ k<sup>2</sup> for some (n − 2)-dimensional vector space U and some surjective skew-symmetric bilinear map φ : U × U → k<sup>2</sup> . If A cannot be represented by T<sup>2,2</sup> , T<sup>2,2</sup> (ǫ<sup>n</sup> 24<sup>),T 2,2(ǫn</sup> 34<sup>)orT 2,2(ǫn</sup> 45<sup>),thenA</sup> −→∼= T 2,2(ǫn45<sup>)and,inparticular,lev(A) ⩾6.</sup> 

5 Algebras with maximal IW contraction T<sup>2,2</sup> 

10 

Proof. We may assume that A is represented by a structure µ such that µ(e1, e2) = en−1, µ(e1, e3) = en and µ(e1, ei) = 0 for all i ⩾ 3. Replacing e2 by e2 − µ<sup>n</sup> 2,3<sup>e1ande3by e3+ µ</sup> 2<sup>n</sup> ,<sup>−</sup> 3<sup>1,</sup> we may assume also that µ(e2, e3) = 0. If there exist 4 ⩽ i, j ⩽ n − 2 such that µ(ei, ej)̸ = 0, 



κ1(t)e1,...,κn(t)en We have the degeneration µ −−−−−−−−−−→ T<sup>2,2</sup> (µ<sup>n</sup> i,j<sup>−1</sup> ǫ<sup>n</sup> i,j<sup>−1</sup> +µ<sup>n</sup> i,j<sup>ǫn</sup> i,j<sup>),</sup> where T<sup>2,2</sup> (µ<sup>n</sup> i,j<sup>−1</sup> ǫ<sup>n</sup> i,j<sup>−1</sup> +µ<sup>n</sup> i,j<sup>ǫn</sup> i,j<sup>)isthealgebrawiththemultiplicationtablee1e2=en−1,e1e3=en,</sup> eiej = µi,j<sup>n−1en−1 + µ</sup> i,j<sup>nen.ItisclearthatT 2,2(µ</sup> i,j<sup>n−1</sup> ǫ<sup>n</sup> i,j<sup>−1</sup> +µ<sup>n</sup> i,j<sup>ǫn</sup> i,j<sup>) ∼= T 2,2(ǫ</sup> 45<sup>n).</sup> If µ(ei, ej) = 0 for all 4 ⩽ i, j ⩽ n − 2, then µ is determined by the matrices Mi = 2,i µ3<sup>n</sup> ,i<sup>−1</sup> (4 ⩽ i ⩽ n−2). Note that T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>) is isomorphic to the algebra determined by</sup> �µµn<sup>n</sup> 2−,i1 µ<sup>n</sup> 3,i � 0 0 matrices M4 = , M5 = and Mi = 0 for 6 ⩽ i ⩽ n−2. To see this, it is enough 1 0 0 1 �0 � �0 � to calculate the structure constants of T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>) inthe basis −e</sup> 2<sup>−e</sup> 5<sup>, e</sup> 1<sup>, e</sup> 4<sup>, e</sup> 3<sup>, e</sup> 5<sup>, . . . , e</sup> n<sup>.Let</sup> T<sup>2,2</sup> (ǫ24<sup>n+ǫn</sup> 35<sup>)∼=T 2,2(ǫn</sup> 45<sup>)denotethestructurecorrespondingtothecollectionofthematrices</sup> defined above. 

Replacing ei by ei + αie1, we can replace our collection of matrices by the collection Mi − αiE for any αi ∈ k (4 ⩽ i ⩽ n − 2), where E denotes the matrix of the identity map. We also can apply any linear transformation to the elements e4, . . . , en−2 that will induce the corresponding linear transformation of our collection of matrices. Then we may assume that, for some 3 ⩽ r ⩽ n − 2, Mi = 0 for i > r and the matrices E, M4, . . . , Mr are linearly independent, in particular, r ⩽ 6, where the case r = 3 corresponds to the structure T<sup>2,2</sup> . Replacing e2 by α2,2e2 + α2,3e3, e3 by α3,2e2 + α3,3e3, en−1 by α2,2en−1 + α2,3en and en by α3,2 α3,2en−1 + α3,3en, where S = is a nonsingular matrix, we can conjugate all �αα22,,32 α3,3� matrices Mi simultaneously by S. 

If the number r above equals to 6, then the matrices M4, M5 and M6 can be turned to any triple of matrices such that E, M4, M5 and M6 are linearly independent. In particular we 0 0 0 0 e1,...,e5,te6,e7,...,en may assume that M4 = , M5 = and get the degeneration µ −−−−−−−−−−−→ 1 0 0 1 � � � � T<sup>2,2</sup> (ǫ24<sup>n+ǫn</sup> 35<sup>).</sup> 

If the number r above equals to 4, then we choose some eigenvalue γ of M4 and replace M4 by M4 − γE. If after this M4 has some nonzero eigenvalue, we rescale it to turn this 0 value to 1. Finally, we transform M4 to its Jordan normal form and get either M4 = 1 0 �0 � 0 or M4 = , i.e. A can be represented by T<sup>2,2</sup> (ǫ<sup>n</sup> 24<sup>)orT 2,2(ǫn</sup> 34<sup>).</sup> 0 1 �0 � It remains to consider the case r = 5. Using the transformations described above, we 0 0 can turn M4 either to the matrix or to the matrix . Let us consider these 1 0 0 1 �0 � �0 � two possibilities separately 

0 α 1. Suppose that M4 = . We may assume that M5 = for some α, β ∈ �00 1� �β0 0� k not both zero. If β = 0, then, replacing M4 and M5 by α1<sup>SM5SandS(E−</sup> 

6 Algebras with maximal IW contraction of the form T<sup>2,...,2</sup> 

11 



0 α 2. Suppose that M4 = . We may assume that M5 = for some α, β ∈ k �10 0� �00 β� 0 not both zero. If β̸ = 0, then we can turn M5 to the form M5 = , interchange 0 1 �0 � M4 and M5, and return to the previous case. If β = 0, then we may assume that 1 e3,e5,−e1,te2,<sup>1</sup> t<sup>e4,e6,...,en</sup> M5 = . Then µ −−−−−−−−−−−−−−→ T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>).</sup> 0 0 �0 � 

Lemma 5.6. Suppose that IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2</sup> . Then 



- lev(A) = 5 if and only if A can be represented by T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>).</sup> 

Proof. By Corollary 5.3 either A can be represented by T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2)orA∼=U⋉</sup> φ<sup>k2for</sup> some (n − 2)-dimensional vector space U and some surjective skew-symmetric bilinear map φ : U × U → k<sup>2</sup> . In the last mentioned case if A cannot be represented by T<sup>2,2</sup> , T<sup>2,2</sup> (ǫ<sup>n</sup> 24<sup>),</sup> T<sup>2,2</sup> (ǫ<sup>n</sup> 34<sup>) or T 2,2(ǫn</sup> 45<sup>), then lev(A) ⩾6 by Corollary 5.5.If T 2,2representsA,then lev(A) = 2.</sup> Suppose that A can be represented by T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2) or T 2,2(ǫn</sup> 24<sup>).Since T 2,2(ǫn</sup> 23<sup>−2) and T 2,2(ǫn</sup> 24<sup>)</sup> degenerate to T<sup>2,2</sup> , we have lev(A) ⩾ 3. Note that T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2)̸→</sup> (1,4,n+1)<sup>T 2,2(ǫ</sup> 24<sup>n)and</sup> T<sup>2,2</sup> (ǫ<sup>n</sup> 24<sup>)̸→</sup> (1,1,n−1)<sup>T 2,2(ǫn</sup> 23<sup>−2).Iflev(A)>3,thenAdegeneratestosomealgebraBoflevel</sup> three. Since IW1<sup>max</sup> (A) → IW1<sup>max</sup> (B), we have either IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2</sup> or IW1<sup>max</sup> (B)<sup>∼</sup> = n3. In the first case B<sup>∼</sup> = A, because all algebras with maximal one-dimensional IW contraction T<sup>2,2</sup> except T<sup>2,2</sup> , T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2)andT 2,2(ǫn</sup> 24<sup>)havelevelnotlessthanfourbyLemmas5.4and</sup> 5.5. If IW1<sup>max</sup> (B)<sup>∼</sup> = n3, then B can be represented by η3 that contradicts the assertions T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2)̸→</sup> (1,6,n+1)<sup>η3andT 2,2(ǫn</sup> 24<sup>)̸→</sup> (1,6,n+1)<sup>η</sup> 3<sup>.Hence,T 2,2(ǫ</sup> 23<sup>n−2)andT 2,2(ǫn</sup> 24<sup>)havelevel</sup> three. The same argument shows that lev�T<sup>2,2</sup> (ǫ<sup>n</sup> 34<sup>)</sup> � = 4 and lev�T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>)</sup> � = 5. 

## 6 Algebras with maximal IW contraction of the form T<sup>2,...,2</sup> 

This section is devoted to the classification of algebras A such that either IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2,2</sup> or IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2,2,2</sup> . We start with some general observations about degenerations of m ���� algebras of the form T 2,...,2 with m ⩾ 3. Analogously to the case m = 2, 3, 4, this algebra has dimension n ⩾ 2m +1 and the multiplication table defined by the equalities e1ei+1 = ei+n−m (1 ⩽ i ⩽ m). 

m ���� Lemma 6.1. Let A be an n-dimensional algebra with IW1<sup>max</sup> (A)<sup>∼</sup> = T 2,...,2 for some m ⩾ 3. If dim A<sup>2</sup> > m, then A degenerates to one of the algebras 

6 Algebras with maximal IW contraction of the form T<sup>2,...,2</sup> 

12 





Proof. Due to Corollary 5.2, A can be represented by a structure µ such that µ(e1, ei+1) = ei+n−m for 1 ⩽ i ⩽ m, µ(e1, ei) = 0 for m + 2 ⩽ i ⩽ n and µ<sup>k</sup> i,j<sup>= 0ifk⩽max(i, j).</sup> 

If dim A<sup>2</sup> > m, then µ<sup>k</sup> i,j̸<sup>=0forsome1⩽i<j<k⩽n −m.DuetoLemma5.1,we</sup> have 2 ⩽ i < j ⩽ m + 1. Let us consider two cases. 





Due to Lemma 5.1, we have the degeneration µ −−−−−−−−−−→ T 2,...,2(ǫki,j<sup>),where</sup> m ���� T 2,...,2(ǫki,j<sup>)isthealgebrawiththemultiplicationtablee</sup> 1<sup>e</sup> s+1<sup>=e</sup> s+n−m<sup>(1⩽s⩽m),</sup> m m ���� ���� eiej = ek. It is clear that T 2,...,2(ǫki,j<sup>) ∼= T</sup> 2,...,2(ǫ23n−m). 



Due to Lemma 5.1, we have the degeneration 





It is clear that 



To finish the proof, it remains to note that if n > 2m + 1, then 



6 Algebras with maximal IW contraction of the form T<sup>2,...,2</sup> 

13 

m ���� Lemma 6.2. Let A be an n-dimensional algebra with IW1<sup>max</sup> (A)<sup>∼</sup> = T 2,...,2 for some m ⩾ 3 and dim A<sup>2</sup> = m. If dim Ann(A) < n − m − 1, then A degenerates to the algebra 



Proof. We again represent A by a structure µ such that µ(e1, es+1) = es+n−m for 1 ⩽ s ⩽ m, µ(e1, es) = 0 for m + 2 ⩽ s ⩽ n and µ<sup>k</sup> i,j<sup>=0ifk⩽max(i, j).Sincedim A2=m,we</sup> also have µ<sup>k</sup> i,j<sup>=0ifeitherk⩽n −mormax(i, j)>n −mbyLemma5.1.Replacing</sup> es by es + µ<sup>n</sup> 2,s<sup>−m+1</sup> e1, we may assume that µ<sup>n</sup> 2,s<sup>−m+1</sup> = 0 for all m + 2 ⩽ s ⩽ n − m. Since dim Ann(A) < n − m − 1, we have µ<sup>k</sup> i,j̸<sup>= 0forsome2 ⩽i, j, k⩽nwithj⩾m + 2.Byour</sup> assumptions, we have n − m + 1 ⩽ k ⩽ n. We also may assume that 2 ⩽ i ⩽ m + 1. Indeed, if i ⩾ m + 2, then either µ<sup>k</sup> 3,j̸<sup>= 0andwecantakereplaceiby3 orµ</sup> 3<sup>k</sup> ,j<sup>= 0 andthenwecan</sup> first replace e3 by e3 + ei and after that i by 3. 



m m ���� ���� κ1(t)e1,...,κn(t)en We have the degeneration µ −−−−−−−−−−→ T 2,...,2(ǫki,j<sup>),whereT</sup> 2,...,2(ǫki,j<sup>)isthealgebra</sup> with the multiplication table e1es+1 = es+n−m (1 ⩽ s ⩽ m), eiej = ek. It is clear that m m ���� ���� T 2,...,2(ǫki,j<sup>) ∼= T</sup> 2,...,2(ǫn2,m+2<sup>).</sup> If k = i + n − m − 1, then we have i̸ = 2 and there is α ∈ k such that µi,j<sup>i+n−m−1</sup> α<sup>2̸</sup> = µ<sup>k</sup> i,j<sup>α + µ</sup> 2<sup>i+</sup> ,j<sup>n−m−1</sup> . Then replacing e2 and en−m+1 by e2 + αei and en−m+1 + αek, we may assume that µ<sup>k</sup> 2,j̸<sup>= 0andreturntothecasethatwehavealreadyconsidered.</sup> 

m ���� Lemma 6.3. Let A be an n-dimensional algebra with IW1<sup>max</sup> (A)<sup>∼</sup> = T 2,...,2 for some m ⩾ 3. m ���� If A̸<sup>∼</sup> = T 2,...,2, then A degenerates to the algebra 







6 Algebras with maximal IW contraction of the form T<sup>2,...,2</sup> 

14 

it remains to consider the case where A is represented by a structure µ such that µ(e1, es+1) = es+n−3 for 1 ⩽ s ⩽ m and µ<sup>k</sup> i,j<sup>=0ifeithermax(i, j)>m + 1ork<n −m + 1.Wewill</sup> consider three cases. 





2. For any pairwise different 2 ⩽ i, j, k ⩽ m + 1 one has µ<sup>k</sup> i,j<sup>+n−m−1</sup> = 0, but there are pairwise different 2 ⩽ i, j, k ⩽ m + 1 such that µ<sup>j</sup> i,j<sup>+n−m−1</sup> = µ<sup>k</sup> i,k<sup>+n−m−1</sup> . Then replacing ej and ej+n−m+1 by ej +ek and ej+n−m−1+ek+n−m−1, we may assume that µi,j<sup>k+n−m−1</sup> = 0 and return to the previous case. 

3. There are αi ∈ k (2 ⩽ i ⩽ m + 1) such that, for any 2 ⩽ i, j ⩽ m + 1, one has µ(ei, ej) = αiej+n−m−1 − αjei+n−m−1. Replacing ei by ei − αie1 for 2 ⩽ i ⩽ m + 1, one m 

���� 

sees that µ<sup>∼</sup> = T 2,...,2 in this case that contradicts our assumptions. 

Since the considered cases cover all possibilities, we are done. 

To fulfill the part of our classification announced in the beginning of this section, we will need the algebra structures presented in the next table. 

|Tab|le 4. Algebras with IW <sup>max</sup><br>1<br>(A) =T <sup>2,2,2</sup>.||
|---|---|---|
|notation|multiplication table|dimension|
|T <sup>2,2,2</sup>(ǫ<sup>n</sup><br>23<sup>)</sup>|e1ei+1 =ei+n−3, 1⩽i⩽3, e2e3 =en|n⩾7|
|T <sup>2,2,2</sup>(ǫ<sup>n</sup><br>24<sup>)</sup>|e1ei+1 =ei+n−3, 1⩽i⩽3, e2e4 =en|n⩾7|
|T <sup>2,2,2</sup>(ǫ<sup>4</sup><br>23<sup>−ǫ7</sup><br>26<sup>+ǫ7</sup><br>35<sup>)</sup>|e1ei+1 =ei+4, 1⩽i⩽3,<br>e2e3 =e4, e2e6 =−e7, e3e5 =e7|n= 7|



It will follow from Lemma 6.1 and what we will prove later that lev∞�T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)</sup> � ⩾ 7. In contrast to this, in dimension 7 the algebra T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)haslevelfive.Toprove</sup> this, we need to show that it does not degenerate to T<sup>2,2</sup> (ǫ45<sup>n)andT 2,2,2(ǫ</sup> 24<sup>n).Unfortunately</sup> we have not found some short prove of this fact, and so give a very tedious calculation proving it in the next lemma. 

Lemma 6.4. In the variety AC7 one has T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)̸ →T 2,2(ǫn</sup> 45<sup>), T 2,2,2(ǫn</sup> 24<sup>).</sup> 

6 Algebras with maximal IW contraction of the form T<sup>2,...,2</sup> 

15 

Proof. Let us consider the set 



Direct verifications show that R is a closed subset of An invariant under lower triangular transformations. Considering the basis e1, e2, e3, e5, e6, e4, e7, one sees that λ ∩ O�T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)</sup> � = ∅. On the other hand, a direct calculation shows that 



We will fulfill this calculation in the more difficult case of the algebra T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>)andleavethe</sup> second case to the reader. 

Suppose that we have found some λ ∈R and a basis f1, . . . , f7 of V such that the structure constants of λ in the basis f1, . . . , f7 are the same as the structure constants of T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>)inthebasise</sup> 1<sup>, . . . , e</sup> 7<sup>,i.e.λ(f</sup> 1<sup>, f</sup> 2<sup>)=f</sup> 6<sup>,λ(f</sup> 1<sup>, f</sup> 3<sup>)=λ(f</sup> 4<sup>, f</sup> 5<sup>)=f</sup> 7<sup>.Letuspick</sup> some v = �7 αifi ∈ V4. Using the condition λ(V, V4) ⊂ V7, we see that α2f6 + α3f7, i=1 α1f6, α1f7, α4f7 and α5f7 belong to ⟨e7⟩. If ⟨e7⟩̸ = ⟨f7⟩, then we have α1 = α4 = α5 for any element of V4, and hence the dimension argument implies V4 = ⟨f2, f3, f6, f7⟩. But in this case λ(V, V4) = ⟨f6, f7⟩ and we get a construction. Thus, we may assume that e7 = f7 and α1 = α2 = 0 for any v ∈ V4. Using the condition V4<sup>2=0,weseethat</sup> V4 = ⟨f3, αf4 + βf5, f6, f7⟩ for some α, β ∈ k. Without loss of generality we may assume that V4 = ⟨f3, f5, f6, f7⟩ and ⟨e1, e2, e3⟩ = ⟨f1, f2, f4⟩. Suppose first that f6̸ ∈ V5. Since R is invariant under lower triangular transformations, we may assume that e4 = f6. Using the condition λ(V, V3) ⊂ V5, we get e3 = f4. But in this case λ(V3, V5)̸ = 0 and we get a contradiction. 

We get f6̸ ∈ V5, and hence we may assume that e4 ∈{f3, f5}. In particular, we have λ<sup>4</sup> 12<sup>= 0,andhenceλ5</sup> 12<sup>λ7</sup> 25<sup>= λ5</sup> 13<sup>λ7</sup> 25<sup>= 0.Nowwehavetwocases.</sup> 

1. λ<sup>5</sup> 12<sup>=λ5</sup> 13<sup>=0.Withtheconditionsλ(V2, V3)⊂V6andf6̸∈V5thisimpliesthat</sup> λ(V, V ) ⊂ V6, i.e. we may assume that e6 = f6, ⟨e4, e5⟩ = ⟨f3, f5⟩. Suppose that ei = αi,1f1 + αi,2f2 + αi,4f4 for 1 ⩽ i ⩽ 3 and ei = αi,3f3 + αi,5f5 for i = 4, 5, where all αi,j are from k. Rewriting the conditions λ35<sup>7=0,λ6</sup> 23<sup>λ7</sup> 15<sup>=λ6</sup> 13<sup>λ7</sup> 25<sup>and</sup> λ<sup>6</sup> 23<sup>λ</sup> 14<sup>7−λ6</sup> 13<sup>λ</sup> 24<sup>7+ λ6</sup> 12<sup>λ7</sup> 34<sup>= 0intermsofαi,j,weget</sup> 



and 



6 Algebras with maximal IW contraction of the form T<sup>2,...,2</sup> 

16 

Noting that 



and 



one sees that the equalities λ<sup>7</sup> 35<sup>=0,λ7</sup> 15<sup>λ6</sup> 23<sup>=λ6</sup> 13<sup>λ7</sup> 25<sup>implyα55=0andtheequality</sup> λ<sup>7</sup> 14<sup>λ6</sup> 23<sup>−λ</sup> 24<sup>7λ6</sup> 13<sup>+ λ7</sup> 34<sup>λ</sup> 12<sup>6= 0impliesα45= 0thatcontradictsthelinearindependence</sup> of e4 and e5. 

2. λ<sup>7</sup> 25<sup>=0.Withtheconditionsλ(V2, V6) + λ(V3, V5)=0andλ(V, V4)⊂V7thisimplies</sup> that λ(V2, V5) = 0. Note that λ<sup>7</sup> 15<sup>λ6</sup> 23<sup>= λ7</sup> 16<sup>λ6</sup> 23<sup>= 0.Ifλ7</sup> 15<sup>= λ7</sup> 16<sup>= 0,then,usingother</sup> conditions assumed and obtained earlier, we get λ(V, V5) = 0 that is impossible. Hence, we have λ<sup>6</sup> 23<sup>=0.Sinceλ(V2, V3)⊂V6andλ7</sup> 23<sup>=0,wehaveλ(e2, e3)=0.Notethat</sup> f2 ∈⟨e2, e3⟩ because in the opposite case we would have λ<sup>7</sup> 15<sup>= λ7</sup> 16<sup>= 0 that have already</sup> been proved to be impossible. Hence, ⟨e2, e3⟩ = ⟨f2, f4⟩ and the condition λ(V2, V5) = 0 gives also ⟨e5, e6⟩ = ⟨f3, f6⟩. Then we also may assume that e1 = f1 and e4 = f5. Let α, β ∈ k be such that f4 = αe2 + βe3. Then αλ<sup>5</sup> 12<sup>+ βλ5</sup> 13<sup>=αλ</sup> 12<sup>6+ βλ6</sup> 13<sup>=0and</sup> αλ<sup>7</sup> 24<sup>+ βλ7</sup> 34̸<sup>= 0.Thenthe equalitiesλ</sup> 12<sup>5λ7</sup> 34<sup>= λ</sup> 13<sup>5λ</sup> 24<sup>7andλ6</sup> 23<sup>λ</sup> 14<sup>7−λ</sup> 24<sup>7λ6</sup> 13<sup>+ λ</sup> 12<sup>6λ7</sup> 34<sup>= 0</sup> imply λ<sup>5</sup> 12<sup>= λ5</sup> 13<sup>= λ</sup> 12<sup>6= λ6</sup> 13<sup>= 0thatisimpossible.</sup> 

The obtained contradiction shows that λ ∩ O�T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>)</sup> � = ∅. 

Lemma 6.5. Suppose that IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2,2</sup> . Then 

- lev(A) = 4 if and only if A can be represented by T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>);</sup> 

- lev(A) = 5 if and only if either A can be represented by T<sup>2,2,2</sup> (ǫ<sup>n</sup> 24<sup>)ordim A = 7andA</sup> can be represented by T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>).</sup> 

Proof. We have A → T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)byLemma6.3.</sup> Since T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> −→∼= T 2,2,2, we have lev�T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> � ⩾ 4. Hence, if lev(A) = 4, then A can be represented by T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>).</sup> If lev�T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> � > 4, then T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)hastodegeneratetosomealgebraBwith</sup> lev(B) = 4. Since in this case IW1<sup>max</sup> �T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> � → IW1<sup>max</sup> (B), we have IW1<sup>max</sup> (B)<sup>∼</sup> = n3, IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2</sup> or IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2,2</sup> . In the last case B<sup>∼</sup> = T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)byLemma</sup> 6.3. In the remaining cases B is isomorphic to η4 or T<sup>2,2</sup> (ǫ<sup>n</sup> 34<sup>)(seeLemma5.6).</sup> Since T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> →(1,5,n+1) η4 and T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> →(1,4,n),(2,3,n),(2,4,n+1) T<sup>2,2</sup> (ǫ<sup>n</sup> 34<sup>),</sup> we have lev�T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> � = 4. Since both T<sup>2,2,2</sup> (ǫ<sup>n</sup> 24<sup>)andT 2,2,2(ǫ</sup> 23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)degeneratenon-triviallytoT 2,2,2(ǫn</sup> 23<sup>),bothof</sup> these algebras have levels not less than five. Let us show now that if IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2,2</sup> and A̸<sup>∼</sup> = T<sup>2,2,2</sup> , T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>),theneitherA→</sup> T<sup>2,2,2</sup> (ǫ<sup>n</sup> 24<sup>)ordim A=7andA→T 2,2,2(ǫ</sup> 23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>).Ifdim A2>3,theneitherdim A=</sup> 7 and A → T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)ordim A>7andA→T 2,2,2(ǫn</sup> 23<sup>−3)byLemma6.1.</sup> Since e1,e2,e4,te3,e5...,en−4,en−3−en−1,en−2,en,ten−1 T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>−3)</sup> −−−−−−−−−−−−−−−−−−−−−−−−−−−→ T<sup>2,2,2</sup> (ǫ<sup>n</sup> 24<sup>), we may assume that dim A2= 3.</sup> 

6 Algebras with maximal IW contraction of the form T<sup>2,...,2</sup> 

17 

If dim Ann(A) < n − 4, then A → T<sup>2,2,2</sup> (ǫ<sup>n</sup> 25<sup>)byLemma6.2.Since</sup> 



it remains to consider the case where A is represented by a structure µ such that µ(e1, ei+1) = ei+n−3 for 1 ⩽ i ⩽ 3 and µ<sup>k</sup> i,j<sup>= 0ifeithermax(i, j) > 4ork< n −2.</sup> We also may assume that µ<sup>n</sup> 23̸<sup>=0(seetheproofofLemma6.3).</sup> Replacing e4 by µ<sup>2</sup> 23<sup>e2+ µ3</sup> 23<sup>e3+ µ4</sup> 23<sup>e4andenbyµ(e2, e3),wemayassumethatµ(e2, e3)=en.Letγbean</sup> eigenvalue of the matrix 24 µ34<sup>n−2</sup> . Then there are some α, β ∈ k not all zero such that �µµ24<sup>n</sup> n<sup>−</sup> −<sup>1</sup> 2 µ34<sup>n−1</sup> � (µ24<sup>n−2</sup> − γ)e2 + µ24<sup>n−1e3, µ</sup> 34<sup>n−2e2+ (µ</sup> 34<sup>n−1</sup> − γ)e3 ∈⟨αe2 + βe3⟩. We may assume that β̸ = 0. Then replacing e3 by αe2 + βe3, en−1 by αen−2 + βen−1 and e4 by e4 + γe1, we may assume that µ<sup>2</sup> 24<sup>= µ2</sup> 34<sup>= 0.</sup> 

It remains to consider two cases. 

- e1,te2,e3,...,en−3,ten−2,en−1,en 

- 1. If µ(e3, e4) = 0, then µ −−−−−−−−−−−−−−−−−→ T<sup>2,2,2</sup> (µ34<sup>n−1</sup> ǫ<sup>n</sup> 34<sup>−1</sup> +µ<sup>n</sup> 34<sup>ǫn</sup> 34<sup>),where</sup> T<sup>2,2,2</sup> (µ<sup>n</sup> 34<sup>−1</sup> ǫ<sup>n</sup> 34<sup>−1</sup> +µ<sup>n</sup> 34<sup>ǫn</sup> 34<sup>)isthealgebrawiththemultiplicationtablee</sup> 1<sup>e</sup> s+1<sup>=e</sup> s+n−3 (1 ⩽ s ⩽ 3), e3e4 = µ34<sup>n−1en−1 +µn</sup> 34<sup>en.It is clear that T 2,2,2(µ</sup> 34<sup>n−1</sup> ǫ<sup>n</sup> 34<sup>−1</sup> +µ<sup>n</sup> 34<sup>ǫn</sup> 34<sup>) ∼= T 2,2,2(ǫn</sup> 24<sup>).</sup> 

2. If µ(e3, e4) = 0, then we consider the operator Le2 : ⟨e3, e4⟩→⟨en−1, en⟩ and put it in the Jordan normal form. Thus, replacing e3 and e4 by their linear combinations and making the same linear replacement with en−1 and en, we may assume that either µ(e2, e3) = γen−1 + en and µ(e2, e4) = γen for some γ ∈ k or µ(e2, e3) = γ3en−1 and µ(e2, e4) = γ4en for some γ3, γ4 ∈ k. In the first case, replacing e2 by e2 − γe1, one sees that µ<sup>∼</sup> = T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>).Ifthesecondcase,replacinge</sup> 2<sup>bye</sup> 2<sup>−γ</sup> 3<sup>e</sup> 1<sup>,wegetthe</sup> algebra T<sup>2,2,2</sup> ((γ4−γ3)ǫ<sup>n</sup> 24<sup>)withthemultiplicationtablee</sup> 1<sup>e</sup> s+1<sup>=e</sup> s+n−3<sup>(1⩽s⩽3),</sup> e2e4 = (γ4 − γ3)en. If γ3 = γ4, then we have µ<sup>∼</sup> = T<sup>2,2,2</sup> . If γ3̸ = γ4, then µ<sup>∼</sup> = T<sup>2,2,2</sup> (ǫ24<sup>n).</sup> 

It remains to show that if A is represented by T<sup>2,2,2</sup> (ǫ<sup>n</sup> 24<sup>) or dim A = 7 and A is represented</sup> by T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>), then lev(A) ⩽5.If it is not so, then A has to degenerate to some algebra</sup> B of level 5 and we have IW1<sup>max</sup> (B)<sup>∼</sup> = n3, IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2</sup> or IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2,2</sup> . Then B can be represented by η5, T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>),T 2,2,2(ǫn</sup> 24<sup>)orT 2,2,2(ǫ</sup> 23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>),wherethelastcaseis</sup> possible only if dim A = 7. 

Note that T<sup>2,2,2</sup> (ǫ<sup>n</sup> 24<sup>), T 2,2,2(ǫ</sup> 23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)</sup> →(1,10,n+1) η5. If n = 7, then we have T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)̸ →T 2,2(ǫn</sup> 45<sup>), T 2,2,2(ǫn</sup> 24<sup>)byLemma6.4,andhencelev</sup> �T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)</sup> � ⩽ 5. Finally, we have T<sup>2,2,2</sup> (ǫ<sup>n</sup> 24<sup>)̸→</sup> (1,5,n+1)<sup>T 2,2(ǫ</sup> 45<sup>n)andT 2,2,2(ǫn</sup> 24<sup>)̸→</sup> (1,1,n−2)<sup>T 2,2,2(ǫ</sup> 23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)that</sup> provides lev�T<sup>2,2,2</sup> (ǫ<sup>n</sup> 24<sup>)</sup> � ⩽ 5. 

Remark 6.6. Note that, due to the proof of Lemma 6.5, one has T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>) ⊕k→</sup> T<sup>2,2,2</sup> (ǫ<sup>6</sup> 24<sup>) ∼= T 2,2,2(ǫ5</sup> 24<sup>) ⊕kwhileT 2,2,2(ǫ</sup> 23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)̸ →T 2,2,2(ǫ5</sup> 24<sup>)byLemma6.4.Thissituation</sup> is in contrast with the fact that A<sup>∼</sup> = B if and only if A ⊕ k<sup>∼</sup> = B ⊕ k. 

Lemma 6.7. Suppose that IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2,2,2</sup> . If A̸<sup>∼</sup> = T<sup>2,2,2,2</sup> , then lev(A) ⩾ 7. 

Proof. By Lemma 6.3 we have a degeneration A → T<sup>2,2,2,2</sup> (ǫ<sup>n</sup> 23<sup>),andhenceitisenough</sup> to prove that lev�T<sup>2,2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> � ⩾ 7. This follows from the non-trivial degeneration e1,...,e4,te5,e6,...,en−4,en,en−3,...,en−1 T<sup>2,2,2,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> −−−−−−−−−−−−−−−−−−−−−→ T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>−3)</sup> (see Lemma 6.1) and that lev�T<sup>2,2,2</sup> (ǫ<sup>n</sup> 23<sup>−3)</sup> � ⩾ 6 by Lemma 6.5. 

7 Algebras with maximal IW contractions T<sup>3</sup> and T<sup>3,2</sup> 

18 

## 7 Algebras with maximal IW contractions T<sup>3</sup> and T<sup>3,2</sup> 

In this section we classify algebras A of first five levels such that either IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> and dim A ⩾ 5 or IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3,2</sup> . The remaining cases will be considered in the next section. As usually, we start with a structure µ representing A such that µ<sup>k</sup> i,j<sup>= 0 for k⩽max(i, j)</sup> and 

- if IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> , then there are three integers 2 ⩽ i1 < i2 < i3 ⩽ n such that µ(e1, ei1) = ei2, µ(e1, ei2) = ei3 and µ(e1, es) = 0 for s̸ ∈{i1, i2}; 

- if IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3,2</sup> , then there are five different integers 2 ⩽ i1 < i2 < i3 ⩽ n and 2 ⩽ j1 < j2 ⩽ n such that µ(e1, ei1) = ei2, µ(e1, ei2) = ei3, µ(e1, ej1) = ej2 and µ(e1, es) = 0 for s̸ ∈{i1, i2, j1}. 

Let us set J = {i1, i2} and K = {i2, i3} in the case IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> and J = {i1, i2, j1} and K = {i2, i3, j2} in the case IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3,2</sup> . We will need the following analog of Lemma 5.1. 

Lemma 7.1. In the settings described above, if µ<sup>k</sup> i,j̸<sup>= 0forsome2 ⩽i, j, k⩽n,theneither</sup> k ∈ K or i, j ∈ J. 

Proof. If µ<sup>k</sup> i,j̸<sup>= 0 for some 2 ⩽i, j, k⩽n such that k̸∈Kand j̸∈J, then one can show that</sup> for some α ∈ K the elements Le1+αei(es) (s ∈ J) and Le1+αei(ej) are linearly independent (see the proof of Lemma 5.1). This would mean that the rank of Le1+αei is not less than |J| + 1, and hence IW1<sup>max</sup> (µ)̸ → IWe1+αei(µ) that is impossible. 

Let now concentrate on the case IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> , dim A ⩾ 5. In this case Lemma 7.1 implies that µ<sup>i</sup> i,j<sup>1=µ</sup> i,i<sup>j</sup> 3<sup>=0forany1⩽i, j⩽n.Inparticular,wemayassumefor</sup> convenience that i1 = 2 and i3 = n. Thus, for some 2 < r < n, the structure µ satisfies the conditions µ(e1, e2) = er, µ(e1, er) = en and µ(e1, es) = 0 for s̸ ∈{2, r}. Lemma 7.2. If IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> and dim A<sup>2</sup> > 2, then A can be represented by the structure 



for some m ⩾ 1 such that dim A ⩾ 2m + 3. 

Proof. Let us represent A by a structure µ satisfying the conditions described above. Due to Lemma 7.1, dim A<sup>2</sup> > 2 if and only if µ(e2, er), er and en are linearly independent. In this case µ(V, V ) = ⟨er, µ(e2, er), en⟩ and we may assume that µ(e2, er) = es for some r < s < n. Replacing ei by ei + µ<sup>r</sup> 2,i<sup>e1for3⩽i⩽r −1,wemayassumethatµr</sup> 2,i<sup>=0foralli⩾3.</sup> Note that µ<sup>s</sup> i,j<sup>=0forall1⩽i <j⩽nexcept(i, j) =(2, r)byLemma7.1.Thenwehave</sup> µ(e2, ei) ⊂⟨en⟩ for 3 ⩽ i ⩽ n, i̸ = r. Since er and es belong to Im Le2, we have µ(e2, ei) = 0 for i̸ ∈{1, r}. If we interchange e1 and e2 and apply Lemma 7.1 to the obtained algebra structure, we will see that µ<sup>n</sup> i,j<sup>=0for1⩽i<j⩽nexcept(i, j)=(1, r).Thenwemay</sup> assume that s = n − 1 and µ(ei, ej) ⊂⟨er⟩ for all 1 ⩽ i < j ⩽ n except (i, j) = (1, r) and (i, j) = (2, r). Then the whole structure µ is determined by a skew-symmetric map µ : ⟨e3, . . . , er−1⟩× ⟨e3, . . . , er−1⟩→⟨er⟩. Then we can use the canonical form for a skewsymmetric bilinear map and get the required isomorphism µ<sup>∼</sup> = ηm(ǫ<sup>n</sup> 1,<sup>−</sup> 2m<sup>1</sup> +1<sup>+ǫ</sup> 2<sup>n</sup> ,2m+1<sup>)forsome</sup> m ⩾ 1. 

7 Algebras with maximal IW contractions T<sup>3</sup> and T<sup>3,2</sup> 

19 

Lemma 7.3. If IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> and dim A<sup>2</sup> = 2, then either dim A ⩾ 6 and A degenerates to the algebra 



or A can be represented by a structure µ such that µ(e1, e2) = e3, µ(e1, e3) = en, µ(e1, ei) = 0 for i ⩾ 4, µ(e2, e3) = 0 and µ<sup>k</sup> i,j<sup>= 0ifk< nandmax(i, j) ⩾3.</sup> Proof. As it is observed above, we may represent A by a structure µ such that µ<sup>k</sup> i,j<sup>=0for</sup> k ⩽ max(i, j) and, for some 2 < r < n, one has µ(e1, e2) = er, µ(e1, r) = en and µ(e1, es) = 0 for s̸ ∈{2, r}. Since dim A<sup>2</sup> = 2, we have µ<sup>k</sup> i,j<sup>=0wheneverk̸∈{r, n}.Replacinge2by</sup> e2 − µ<sup>n</sup> 2,r<sup>e1,wemayassumealsothatµ(e2, er) = 0.</sup> 

Replacing ei by ei + µ<sup>r</sup> 2,i<sup>e1for3 ⩽i ⩽r −1,wemayassumethatµ(e2, ei) ⊂⟨en⟩forall</sup> 2 ⩽ i ⩽ n. If µ<sup>r</sup> i,j<sup>= 0for all 3 ⩽i < j< r, thenwe clearlycanpermutese3anderand geta</sup> structure representing A and satisfying the required conditions. Suppose now that µ<sup>r</sup> i,j̸<sup>=0</sup> 



κ1(t)e1,...,κn(t)en We have µ −−−−−−−−−−→ T (ǫ<sup>r</sup> 1,2<sup>+ǫn</sup> 1,r<sup>+µr</sup> i,j<sup>ǫr</sup> i,j<sup>+µn</sup> i,j<sup>ǫn</sup> i,j<sup>),whereT(ǫ</sup> 1<sup>r</sup> ,2<sup>+ǫn</sup> 1,r<sup>+µr</sup> i,j<sup>ǫr</sup> i,j<sup>+µn</sup> i,j<sup>ǫn</sup> i,j<sup>)isthe</sup> algebra with the multiplication table e1e2 = er, e1er = en, eiej = µ<sup>r</sup> i,j<sup>er+ µn</sup> i,j<sup>en.Itisclear</sup> that T (ǫ<sup>r</sup> 1,2<sup>+ǫn</sup> 1,r<sup>+µr</sup> i,j<sup>ǫr</sup> i,j<sup>+µn</sup> i,j<sup>ǫn</sup> i,j<sup>) ∼= η2(ǫ</sup> 15<sup>n).</sup> 

To classify the algebras A with IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> of levels not greater than five, we will need the algebra structures presented in the next table. 

Table 5. Algebras with IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> . 

|notation|multiplication table|dimension|
|---|---|---|
|T <sup>3</sup>(ǫ<sup>n−1</sup><br>23 <sup>)</sup><br>|e1e2 =e3, e1e3 =en, e2e3 =en−1|n⩾5|
|T <sup>3</sup>(ǫ<sup>n</sup><br>24<sup>)</sup>|e1e2 =e3, e1e3 =e2e4 =en|n⩾5|
|T <sup>3</sup>(ǫ<sup>n</sup><br>34<sup>)</sup>|e1e2 =e3, e1e3 =e3e4 =en|n⩾5|
|T <sup>3</sup>(ǫ<sup>n</sup><br>45<sup>)</sup>|e1e2 =e3, e1e3 =e4e5 =en|n⩾6|



Lemma 7.4. Suppose that IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> and dim A ⩾ 5. Then 

- lev(A) = 4 if and only if A can be represented by T<sup>3</sup> (ǫ<sup>n</sup> 23<sup>−1)orT 3(ǫn</sup> 24<sup>);</sup> 

- lev(A) = 5 if and only if either A can be represented by T<sup>3</sup> (ǫ34<sup>n)ordim A=6andA</sup> can be represented by T<sup>3</sup> (ǫ45<sup>6).</sup> 

Proof. Note first that we have non-trivial degenerations T<sup>3</sup> (ǫ<sup>n</sup> 23<sup>−1), T 3(ǫ</sup> 24<sup>n)</sup> → T<sup>3</sup> , te1,e2+e3,te3+ten,t<sup>2</sup> e4,e5...,en−1,t<sup>2</sup> en e1,e2−e5,e3,e4,te5,e6...,en T<sup>3</sup> (ǫ34<sup>n)</sup> −−−−−−−−−−−−−−−−−−−−−→ T<sup>3</sup> (ǫ24<sup>n)andT 3(ǫ</sup> 45<sup>n)</sup> −−−−−−−−−−−−−−→ T<sup>3</sup> (ǫ24<sup>n),and</sup> hence lev�T<sup>3</sup> (ǫ<sup>n</sup> 23<sup>−1)</sup> � ⩾ 4, lev�T<sup>3</sup> (ǫ24<sup>n)</sup> � ⩾ 4, lev�T<sup>3</sup> (ǫ34<sup>n)</sup> � ⩾ 5 and lev�T<sup>3</sup> (ǫ45<sup>n)</sup> � ⩾ 5. e1,...,en−2,<sup>1</sup> t<sup>en,en−1</sup> Note that ηm(ǫ<sup>n</sup> 1,<sup>−</sup> 2m<sup>1</sup> +1<sup>+ǫ</sup> 2<sup>n</sup> ,2m+1<sup>)→η</sup> 2<sup>(ǫ</sup> 15<sup>n−1</sup> +ǫ<sup>n</sup> 25<sup>)</sup> −−−−−−−−−−−→ η2(ǫ<sup>n</sup> 15<sup>)form⩾2and</sup> te1,e2−e5,te5−ten,te3,te4,e6,...,en−1,t<sup>2</sup> en η2(ǫ15<sup>n)</sup> −−−−−−−−−−−−−−−−−−−−−−−→ T<sup>3</sup> (ǫ45<sup>n).Due to Lemmas 7.2 and 7.3, if A has level not</sup> greater than five, then it can be represented either by the structure η1(ǫ13<sup>n−1</sup> +ǫ<sup>n</sup> 23<sup>) ∼= T 3(ǫn</sup> 23<sup>−1) or</sup> by a structure µ such that µ(e1, e2) = e3, µ(e1, e3) = en, µ(e1, ei) = 0 for i ⩾ 4, µ(e2, e3) = 0 and µ<sup>k</sup> i,j<sup>=0ifk<nandmax(i, j)⩾3.Itremainstoconsiderthelastcasetoprovethat</sup> there are no algebras A of levels four and five with IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> except the algebras mentioned in the statement of this lemma. Let us consider three cases. 

7 Algebras with maximal IW contractions T<sup>3</sup> and T<sup>3,2</sup> 

20 

1. µ(ei, ej) = 0 for all 3 ⩽ i, j ⩽ n − 1. In this case the multiplication table of µ is defined by the equalities e1e2 = e3, e1e3 = en, e2ei = αien (4 ⩽ i ⩽ n − 1), where αi are some elements of the field k. It is clear that if all αi are zero, then µ<sup>∼</sup> = T<sup>3</sup> and if minimum one of the elements αi is not zero, then µ<sup>∼</sup> = T<sup>3</sup> (ǫ<sup>n</sup> 24<sup>).</sup> 



κ1(t)e1,...,κn(t)en Then we have the degeneration µ −−−−−−−−−−→ T<sup>3</sup> (ǫ<sup>n</sup> i,j<sup>),whereT 3(ǫn</sup> i,j<sup>)isthealgebra</sup> with the multiplication table e1e2 = e3, e1e3 = eiej = en. It is clear that T<sup>3</sup> (ǫ<sup>n</sup> i,j<sup>)∼=</sup> T<sup>3</sup> (ǫ<sup>n</sup> 45<sup>).</sup> 

3. µ(e3, ei)̸ = 0 for some 4 ⩽ i ⩽ n − 1. We may assume in this case that µ(e3, ei) = en. 1t<sup>e1,t2e2,te3, 1</sup> t<sup>ei,t2e4...,t2ei−1,t2ei+1...,t2en−1,en</sup> Then we have the degeneration µ −−−−−−−−−−−−−−−−−−−−−−−−−−−→ T<sup>3</sup> (ǫ<sup>n</sup> 34<sup>).</sup> 

It remains to note that if n ⩾ 7, then T<sup>3</sup> (ǫ<sup>n</sup> 45<sup>)</sup> −−−−−−−−−−−−−−→e1,te2,e3−<sup>1</sup> t<sup>en−1,e4,...,en</sup> T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>).</sup> It remains to show that lev�T<sup>3</sup> (ǫ<sup>n</sup> 23<sup>−1)</sup> � ⩽ 4, lev�T<sup>3</sup> (ǫ<sup>n</sup> 24<sup>)</sup> � ⩽ 4, lev�T<sup>3</sup> (ǫ<sup>n</sup> 34<sup>)</sup> � ⩽ 5 and, in the case n = 6, lev�T<sup>3</sup> (ǫ<sup>6</sup> 45<sup>)</sup> � ⩽ 5. Suppose that A is represented by T<sup>3</sup> (ǫ<sup>n</sup> 23<sup>−1)orT 3(ǫn</sup> 24<sup>).</sup> If lev(A) > 4, then A degenerates to some algebra B of level 4 and we have IW1<sup>max</sup> (B)<sup>∼</sup> = n3, IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2</sup> or IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>3</sup> . Then B can be represented by η4, T<sup>2,2</sup> (ǫ<sup>n</sup> 34<sup>),T 3(ǫn</sup> 23<sup>−1)orT 3(ǫn</sup> 24<sup>).Notethat</sup> T<sup>3</sup> (ǫ<sup>n</sup> 23<sup>−1)̸→</sup> (1,4,n+1)<sup>η4, T 2,2(ǫ</sup> 34<sup>n), T 3(ǫ</sup> 24<sup>n);T 3(ǫn</sup> 24<sup>)̸→</sup> (1,8,n+1)<sup>η</sup> 4<sup>;T 3(ǫ</sup> 24<sup>n)̸→</sup> (1,3,n),(3,3,n+1)<sup>T 2,2(ǫ</sup> 34<sup>n)</sup> and T<sup>3</sup> (ǫ<sup>n</sup> 24<sup>)̸ →</sup> (1,1,n−1)<sup>T 3(ǫn</sup> 23<sup>−1).Thus,lev</sup> �T<sup>3</sup> (ǫ<sup>n</sup> 23<sup>−1)</sup> � ⩽ 4 and lev�T<sup>3</sup> (ǫ24<sup>n)</sup> � ⩽ 4. Suppose that either A is represented by T<sup>3</sup> (ǫ34<sup>n)ordim A=6andAisrepresented</sup> by T<sup>3</sup> (ǫ45<sup>n).</sup> If lev(A) > 5, then A degenerates to some algebra B of level 5 and we again have IW1<sup>max</sup> (B)<sup>∼</sup> = n3, IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2</sup> or IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>3</sup> . Then B can be represented by η5, T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>),T 3(ǫn</sup> 34<sup>)orT 3(ǫn</sup> 45<sup>),wherethecaseT 2,2(ǫn</sup> 45<sup>)ispossibleonlyif</sup> dim A ⩾ 7. Note that T<sup>3</sup> (ǫ<sup>n</sup> 34<sup>)̸→</sup> (1,5,n+1)<sup>η</sup> 5<sup>, T 2,2(ǫ</sup> 45<sup>n), T 3(ǫn</sup> 45<sup>);T 3(ǫn</sup> 45<sup>)̸→</sup> (1,10,n+1)<sup>η</sup> 5<sup>and</sup> T<sup>3</sup> (ǫ<sup>n</sup> 45<sup>)̸→</sup> (1,1,n−1),(1,3,n),(2,n−1,n+1)<sup>T 3(ǫ</sup> 34<sup>n).Thus,lev</sup> �T<sup>3</sup> (ǫ<sup>n</sup> 34<sup>)</sup> � ⩽ 5 and, in the case n = 6, lev�T<sup>3</sup> (ǫ<sup>n</sup> 45<sup>)</sup> � ⩽ 5. 

Let us now consider the case IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3,2</sup> . For this piece of our classification, we will need one more algebra structure. 



Proof. We want to show first that if IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3,2</sup> and A̸<sup>∼</sup> = T<sup>3,2</sup> , then A → T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>).</sup> We represent the algebra A by a structure µ such that µ<sup>k</sup> i,j<sup>= 0fork⩽max(i, j)andthere</sup> are five different integers 2 ⩽ i1 < i2 < i3 ⩽ n and 2 ⩽ j1 < j2 ⩽ n such that µ(e1, ei1) = ei2, µ(e1, ei2) = ei3, µ(e1, ej1) = ej2 and µ(e1, es) = 0 for s̸ ∈{i1, i2, j1}. Due to Lemma 7.1, we also have µ<sup>k</sup> i,j<sup>=0ifk̸∈{i2, i3, j2}andj̸∈{i1, i2, j1}.Inparticular,µi</sup> i,j<sup>1=0forany</sup> 1 ⩽ i, j ⩽ n. 

7 Algebras with maximal IW contractions T<sup>3</sup> and T<sup>3,2</sup> 

21 

Note first that, for 2 ⩽ i ⩽ n and any α ∈ k, one has 

0 = (Le1+αei)<sup>3</sup> (ei1) = α�µ(ei, ei3) + Le1µ(ei, ei2) + (Le1)<sup>2</sup> µ(ei, ei1)� + α<sup>2</sup> v, where v ∈ V does not depend on α. Note that µ<sup>i</sup> i,i<sup>1</sup> 1<sup>=0,andhence(Le</sup> 1<sup>)2µ(ei, ei</sup> 1<sup>)=0.</sup> Since µ<sup>i</sup> i,i<sup>1</sup> 2<sup>= µi</sup> i,i<sup>2</sup> 2<sup>= 0,wegetµ(ei</sup> 3<sup>, ei) = µj</sup> i,i<sup>1</sup> 2<sup>ej</sup> 2<sup>,inparticular,µ(ei, ei</sup> 3<sup>) = 0fori̸ = i1.</sup> If µi<sup>j</sup> 1<sup>1</sup> ,i2̸<sup>= 0,thenitisenoughtoprovethatχ →T 3,2(ǫ</sup> 23<sup>n)forthestructureχdefinedby</sup> 



The algebra χ has multiplication table 



Replacing χ by an isomorphic structure, we may assume that i1 = 2, i2 = 3, i3 = n − 1, j1 = 4, j2 = n and µ<sup>j</sup> i1<sup>1</sup> ,i2<sup>= 1,µj</sup> i1<sup>2</sup> ,i2<sup>= 0.Thenwehave</sup> 



Note also that, for 2 ⩽ i ⩽ n and any α ∈ k, one has 



where v ∈ V does not depend on α. It follows from µ<sup>i</sup> i,j<sup>1</sup> 1<sup>= 0thatµ</sup> i,j<sup>i2</sup> 2<sup>= 0.</sup> 

Now we may assume that µ<sup>j</sup> i1<sup>1</sup> ,i2<sup>=0,andhenceµ(ei</sup> 1<sup>, ei</sup> 3<sup>)=0bytheargumentabove.</sup> Then without loss of generality we may assume that i1 = 3, i3 = n, j1 = 2 and j2 = n − 1. From here on we denote also i2 by r. Replacing ei by ei + µ<sup>r</sup> 3,i<sup>e1for2⩽i ⩽r −1,wemay</sup> assume that µ<sup>r</sup> 3,i<sup>=0forall2⩽i⩽n.Supposethatthereare2⩽i<j⩽r −1suchthat</sup> µ<sup>r</sup> i,j̸<sup>=0.Ifµ</sup> 2<sup>r</sup> ,j<sup>=0,thewecanreplacee2bye2+ eiandassumethatµr</sup> 2,j̸<sup>=0forsome</sup> 4 ⩽ j ⩽ r − 1. 



The algebra χ has multiplication table 



Replacing χ by an isomorphic structure, we may assume that j = 4, r = 5, µ<sup>r</sup> 2,j<sup>=1and</sup> µ<sup>n</sup> 2,j<sup>= 0.Thenwehave</sup> 



8 Algebras with maximal IW contractions of non-stable level 

22 

Hence, we may assume that µ<sup>r</sup> i,j<sup>=0for1⩽i<j⩽n,(i, j)̸=(1, 3).Thenwemay</sup> assume also that r = 4. Suppose now that dim A<sup>2</sup> > 3. Then there is some 5 ⩽ i ⩽ n − 3 such that one of the elements µ<sup>i</sup> 2,3<sup>,µi</sup> 2,4<sup>andµi</sup> 3,4<sup>isnonzero.Sincewecanreplacee3ande4</sup> by e3 + e4 and e4 + en or e2 and en−1 by e2 + e4 and en−1 + en, we may assume that µ<sup>i</sup> 23̸<sup>= 0.</sup> It is enough to prove that χ → T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>)forthestructureχdefinedbythedegeneration</sup> 



The algebra χ has multiplication table e1e2 = en−1, e1e3 = e4, e1e4 = en, e2e3 = µ<sup>i</sup> 23<sup>ei +</sup> µ<sup>n</sup> 23<sup>en.Replacingχbyanisomorphicstructure,wemayassumethatµi</sup> 23<sup>=µn</sup> 23<sup>=1.Then</sup> we have 



From here on we may assume that µ(V, V ) = {e4, en−1, en}. Note that if µ<sup>n</sup> 23̸<sup>= 0,then</sup> 



If µ23<sup>n−1+µn</sup> 34̸<sup>= 0 or µ</sup> 34<sup>n−1</sup> = 0, then for some α ∈ k one has µ(e2 + αe4, e3)̸ ∈⟨en−1 + αen⟩, i.e. we can replace e2 and en−1 by e2 + αe4 and en−1 + αen that returns us to the case µ<sup>n</sup> 23̸<sup>= 0.</sup> Suppose that µ<sup>n</sup> 23<sup>= µ</sup> 23<sup>n−1</sup> + µ<sup>n</sup> 34<sup>= µ</sup> 34<sup>n−1</sup> = 0. Replacung e3 by e3 − µ<sup>n</sup> 34<sup>e1, we may assume that</sup> µ(e2, e3) = µ(e3, e4) = 0. If µ(e2, e4)̸ = 0, then replacing e3 and e4 by e3 + e4 and e4 + en, we may assume that µ(e2, e3)̸ = 0 and µ(e3, e4) = 0 that comes down to the case µ<sup>n</sup> 23̸<sup>=0</sup> as was explained above. Analogously, if µ(e3, ei) or µ(e4, ei) is nonzero for some i ⩾ 5, then adding ei to e2 we can reduce everything to the case µ<sup>n</sup> 23̸<sup>= 0.Ifµ(e3, ei) = µ(e4, ei) = 0and</sup> µ(e2, ei) is nonzero for some i ⩾ 5, then we are done by the replacement of e3 by e3 + ei. Finally, if µ(ei, ej)̸ = 0 for two integers i, j ⩾ 5, then we can add ej to e2 and return to the case µ(e2, ei)̸ = 0. If µ(ei, ej) = 0 for all 2 ⩽ i, j ⩽ n, then A is represented by T<sup>3,2</sup> that contradicts our assumptions. 

Note that T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>)</sup> −→∼= T 3,2, and hence lev�T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>))</sup> � ⩾ 5 and algebra A with IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3,2</sup> can have level five only if A is represented by T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>).Iflev</sup> �T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>))</sup> � > 5, then T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>) degenerates to some algebra Bof level five.Since IW</sup> 1<sup>max</sup> (A) → IW1<sup>max</sup> (B), we have IW1<sup>max</sup> (B)<sup>∼</sup> = n3, IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2</sup> , IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>3</sup> , IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2,2</sup> or IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>3,2</sup> . Then B can be represented by η5, T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>),T 3(ǫn</sup> 34<sup>),T 3(ǫn</sup> 45<sup>),T 2,2,2(ǫn</sup> 24<sup>),T 2,2,2(ǫ</sup> 23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)</sup> or T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>).InthelastcaseB∼= Abyourarguments.Wehavealso</sup> 



T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>)̸→T 3(ǫn</sup> 34<sup>)becauseT 3,2(ǫn</sup> 23<sup>)isaLiealgebraandT 3(ǫn</sup> 34<sup>)isnot,andfinally</sup> T<sup>3,2</sup> (ǫ<sup>n</sup> 23<sup>)̸ →</sup> (1,4,n),(2,4,n+1),(2,3,n)<sup>T 2,2,2(ǫ</sup> 24<sup>n).</sup> 

## 8 Algebras with maximal IW contractions of non-stable level 

In this section we consider algebras A such that lev�IW1<sup>max</sup> (A)� < lev∞�IW1<sup>max</sup> (A)�. Due to Table 1, this occurs when either IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> and dim A = 4 or IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>4</sup> and dim A = 5. 

8 Algebras with maximal IW contractions of non-stable level 

23 

Lemma 8.1. If IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> and dim A = 4, then A can be represented by T<sup>3</sup> . 

Proof. Since in the considered case A is nilpotent, we may assume that A is represented by a structure µ such that µ(e1, e2) = e3, µ(e1, e3) = e4 and µ<sup>k</sup> i,j<sup>= 0ifk⩽max(i, j).Thenthe</sup> only nonzero product except ones we have already mentioned is µ(e2, e3) = µ<sup>4</sup> 23<sup>e4.Thenin</sup> the basis e1, e2 − µ<sup>4</sup> 23<sup>e1, e3, e4thestructureµhasthesamestructureconstantsasT 3,i.e.A</sup> can be represented by T<sup>3</sup> . 

It remains to study the case of five-dimensional algebra A with IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>4</sup> . The main difficulty of this case is that we do not have nilpotence of the algebra A automatically. Let us now introduce the five-dimensional algebra T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>)withIW</sup> 1<sup>max</sup> �T (ǫ<sup>5</sup> 23<sup>)</sup> � ∼= T 4. 



Lemma 8.2. Suppose that IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>4</sup> and dim A = 5. Then A has level five if and only if it can be represented by T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>).</sup> 

Proof. Let us show first that if IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>4</sup> , dim A = 5 and A̸<sup>∼</sup> = T<sup>4</sup> , then A → T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>).</sup> We may assume that A is represented by a structure µ such that IWe1(µ) = T<sup>4</sup> . This means that µ(e1, ei) = µ<sup>1</sup> 1,i<sup>e1 + ei+1for2⩽i⩽4andµ(e1, e5)=µ</sup> 15<sup>1e1.Wehaveµ1</sup> 15<sup>=0bythe</sup> nilpotence of the operator Le5. Replacing ei by µ<sup>1</sup> 1,i−1<sup>e1 + eifor3⩽i⩽5,wemayassume</sup> that µ<sup>1</sup> 1,i<sup>= 0forall2 ⩽i ⩽5.</sup> 

Let us pick some α, β ∈ k and consider a new basis of V defined by the equalities f1 = e1, f2 = e2 + αe3 + βe4, f3 = e3 + αe4 + βe5, e4 = e4 + αe5, f5 = e5. Note that for any choice of α and β we have µ(f1, fi) = fi+1 for 2 ⩽ i ⩽ 4 and µ(f1, f5) = 0. We will consider two cases. 

- Suppose that µ(f2, f3) ⊂⟨f4⟩ = ⟨e4 + αe5⟩ for any choice of α, β ∈ k. Note that 



Now one sees that the condition µ(f2, f3) ⊂⟨f4⟩ is equivalent to the qualities 



with µ<sup>5</sup> 24<sup>= µ4</sup> 23<sup>,µ5</sup> 25<sup>= µ5</sup> 34<sup>= µ</sup> 24<sup>4andµ5</sup> 35<sup>= µ4</sup> 25<sup>.ThenilpotenceofLe</sup> 3<sup>impliesµ5</sup> 35<sup>= 0,</sup> and hence µ(e2, e5) = µ<sup>5</sup> 25<sup>e5.Then the nilpotence of Le</sup> 2<sup>implies µ5</sup> 25<sup>= 0, and hence µ is</sup> a structure whose nonzero products of basic elements are µ(e1, ei) = ei+1 for 2 ⩽ i ⩽ 4, µ(e2, e3) = γe4 and µ(e2, e4) = γe5 for some γ ∈ k. Considering the basis e1, e2 − γe1, e3, e4, e5, one sees that µ<sup>∼</sup> = T<sup>4</sup> . • Suppose that µ(f2, f3)̸ ⊂⟨f4⟩ for some choice of α, β ∈ k. Then we may assume that µ(e2, e3)̸ ∈⟨e4⟩. Suppose that µ<sup>5</sup> 23<sup>=0.Letusdenotebyvthevectorµ1</sup> 23<sup>e1 + µ2</sup> 23<sup>e2 +</sup> µ<sup>3</sup> 23<sup>e3whichisnonzerobyourassumption.Thenonehas</sup> 



9 Main Theorem 

24 

The nilpotence of Le2−µ423<sup>e1impliesµ</sup> 23<sup>3=µ1</sup> 23<sup>+ µ2</sup> 23<sup>µ4</sup> 23<sup>=0.NowwehaveLe</sup> 3<sup>(v)=</sup> −µ<sup>2</sup> 23<sup>vandthenilpotenceofLe</sup> 3<sup>impliesµ2</sup> 23<sup>=0,andhenceµ1</sup> 23<sup>=0thatcontradicts</sup> te1,<sup>t2</sup> e2,<sup>t3</sup> e3,<sup>t4</sup> e4,<sup>t5</sup> e5 the fact that v̸ = 0. Thus, we have µ<sup>5</sup> 23̸<sup>= 0.Thenµ</sup> −−−−−−−−−−−−−−−−→µ<sup>5</sup> 23 µ<sup>5</sup> 23 µ<sup>5</sup> 23 µ<sup>5</sup> 23 T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>).</sup> 

Note that T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>)</sup> −→∼= T 4, and hence lev�T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>)</sup> � ⩾ 5 and algebra A with IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>4</sup> can have level five only if A is represented by T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>).</sup> If lev�T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>)</sup> � > 5, then T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>)</sup> degenerates to some algebra B of level five. Since IW1<sup>max</sup> (A) → IW1<sup>max</sup> (B), we have IW1<sup>max</sup> (B)<sup>∼</sup> = n3, IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>2,2</sup> , IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>3</sup> or IW1<sup>max</sup> (B)<sup>∼</sup> = T<sup>4</sup> . Then B can be represented by T<sup>3</sup> (ǫ<sup>5</sup> 34<sup>)orT 4(ǫ5</sup> 23<sup>)becauseallotheralgebraswiththesemaximalone-</sup> dimensional IW contractions and level five have dimensions greater than five. In the last case B<sup>∼</sup> = A by our arguments. Finally, T<sup>4</sup> (ǫ<sup>5</sup> 23<sup>)̸ →</sup> (1,5,6),(1,4,5),(1,1,3),(2,4,6),(2,3,5)<sup>T 3(ǫ</sup> 34<sup>5).</sup> 

## 9 Main Theorem 

In this section we state and prove the theorems giving the classification of anticommutative Engel algebras of levels from three to five, which is the main aim of this paper. We will give also some consequences of our classification. Let us recall that the finite dimensional algebras A and B are stably isomorphic if A ⊕ k<sup>k∼</sup> = B ⊕ k<sup>l</sup> for some integers k, l. 

Theorem 9.1. Let A be an n-dimensional anticommutative Engel algebra. 

- If dim A ⩽ 4, then A has level not greater than two. 

- If dim A = 5, then A has level 3 if and only if it can be represented by T<sup>3</sup> . 

- If dim A = 6, then A has level 3 if and only if it can be represented by T<sup>2,2</sup> (ǫ<sup>4</sup> 23<sup>), T 2,2(ǫ6</sup> 24<sup>)</sup> or T<sup>3</sup> . 

- If dim A ⩾ 7, then A has level 3 if and only if it can be represented by η3, T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2),</sup> T<sup>2,2</sup> (ǫ<sup>n</sup> 24<sup>),T 3orT 2,2,2.</sup> 

Proof. The algebra A can have level 3 only if lev�IW1<sup>max</sup> (A)� ⩽ 3. Then IW1<sup>max</sup> (A) is isomorphic to one of the structures n3, T<sup>2,2</sup> , T<sup>3</sup> and T<sup>2,2,2</sup> . In the first case A has level 3 if and only if it is represented by η3. If either IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2,2</sup> or dim A ⩾ 5 and IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3</sup> , then A has level 3 if and only if A<sup>∼</sup> = IW1<sup>max</sup> (A). The remaining part of the theorem follows from Lemmas 5.6 and 8.1. 

Now we can recover the nilpotent part of the classification from [6] in a correct form. Corollary 9.2. An anticommutative Engel algebra A has infinite level 3 if and only if it is stably isomorphic to η3, T<sup>2,2</sup> (ǫ<sup>n</sup> 23<sup>−2),T 2,2(ǫn</sup> 24<sup>),T 3orT 2,2,2.</sup> 

Theorem 9.3. Let A be an n-dimensional anticommutative Engel algebra. 

- If dim A = 5, then A has level 4 if and only if it can be represented by T<sup>3</sup> (ǫ<sup>4</sup> 23<sup>),T 3(ǫ5</sup> 24<sup>)</sup> or T<sup>4</sup> . 

- If dim A = 6, then A has level 4 if and only if it can be represented by T<sup>2,2</sup> (ǫ<sup>6</sup> 34<sup>),T 3(ǫ5</sup> 23<sup>),</sup> T<sup>3</sup> (ǫ<sup>6</sup> 24<sup>)orT 3,2.</sup> 

9 Main Theorem 

25 

- If dim A = 7, 8, then A has level 4 if and only if it can be represented by T<sup>2,2</sup> (ǫ<sup>n</sup> 34<sup>),</sup> T<sup>3</sup> (ǫ<sup>n</sup> 23<sup>−1),T 3(ǫ</sup> 24<sup>n),T 2,2,2(ǫ</sup> 23<sup>n)orT 3,2.</sup> 

- If dim A ⩾ 9, then A has level 4 if and only if it can be represented by η4, T<sup>2,2</sup> (ǫ34<sup>n),</sup> T<sup>3</sup> (ǫ<sup>n</sup> 23<sup>−1),T 3(ǫ</sup> 24<sup>n),T 2,2,2(ǫ</sup> 23<sup>n),T 3,2orT 2,2,2,2.</sup> 

Proof. The algebra A can have level 4 only if lev�IW1<sup>max</sup> (A)� ⩽ 4. Then IW1<sup>max</sup> (A) is isomorphic to one of the structures n3, T<sup>2,2</sup> , T<sup>3</sup> , T<sup>2,2,2</sup> , T<sup>3,2</sup> , T<sup>2,2,2,2</sup> or T<sup>4</sup> , where the last case can occur only if dim A = 5. In the first case A has level 4 if and only if it is represented by η4. If IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3,2</sup> , IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2,2,2</sup> or IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>4</sup> , where in the last case dim A = 5, then A has level 4 if and only if A<sup>∼</sup> = IW1<sup>max</sup> (A). The remaining part of the theorem follows from Lemmas 5.6, 6.5, 7.4 and 8.1. 

Corollary 9.4. An anticommutative Engel algebra A has infinite level 4 if and only if it is stably isomorphic to η4, T<sup>2,2</sup> (ǫ<sup>n</sup> 34<sup>),T 3(ǫn</sup> 23<sup>−1),T 3(ǫn</sup> 24<sup>),T 2,2,2(ǫn</sup> 23<sup>),T 3,2orT 2,2,2,2.</sup> 

Corollary 9.5. Any anticommutative Engel algebra of level not greater than 4 is a Lie algebra. 

Theorem 9.6. Let A be an n-dimensional anticommutative Engel algebra. 

- If dim A = 5, then A has level 5 if and only if it can be represented by T<sup>3</sup> (ǫ<sup>5</sup> 34<sup>) or T 4(ǫ5</sup> 23<sup>).</sup> 

- • If dim A = 6, then A has level 5 if and only if it can be represented by T<sup>3</sup> (ǫ<sup>6</sup> 34<sup>),T 3(ǫ6</sup> 45<sup>),</sup> T<sup>3,2</sup> (ǫ<sup>6</sup> 23<sup>)orT 4.</sup> 

- If dim A = 7, then A has level 5 if and only if it can be represented by T<sup>2,2</sup> (ǫ<sup>7</sup> 45<sup>),T 3(ǫ7</sup> 34<sup>),</sup> T<sup>2,2,2</sup> (ǫ<sup>7</sup> 24<sup>),T 2,2,2(ǫ</sup> 23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>),T 3,2(ǫ7</sup> 23<sup>),T 4orT 3,3.</sup> 

- If 8 ⩽ dim A ⩽ 10, then A has level 5 if and only if it can be represented by T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>),</sup> T<sup>3</sup> (ǫ<sup>n</sup> 34<sup>),T 2,2,2(ǫn</sup> 24<sup>),T 3,2(ǫn</sup> 23<sup>),T 4orT 3,2,2.</sup> 

- If dim A ⩾ 11, then A has level 5 if and only if it can be represented by η5, T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>),</sup> T<sup>3</sup> (ǫ<sup>n</sup> 34<sup>),T 2,2,2(ǫn</sup> 24<sup>),T 3,2(ǫn</sup> 23<sup>),T 2,2,2,2,2,T 3,2,2orT 4.</sup> 

Proof. The algebra A can have level 5 only if lev�IW1<sup>max</sup> (A)� ⩽ 5. Then IW1<sup>max</sup> (A) is isomorphic to one of the structures n3, T<sup>2,2</sup> , T<sup>3</sup> , T<sup>2,2,2</sup> , T<sup>3,2</sup> , T<sup>2,2,2,2</sup> , T<sup>4</sup> , T<sup>3,2,2</sup> , T<sup>2,2,2,2,2</sup> or T<sup>3,3</sup> where the last case can occur only if dim A = 7. In the first case A has level 5 if and only if it is represented by η5. If IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>4</sup> , IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3,2,2</sup> , IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>2,2,2,2,2</sup> or IW1<sup>max</sup> (A)<sup>∼</sup> = T<sup>3,3</sup> , where in the first case dim A ⩾ 6 and in last case dim A = 7, then A has level 5 if and only if A<sup>∼</sup> = IW1<sup>max</sup> (A). The remaining part of the theorem follows from Lemmas 5.6, 6.5, 6.7, 7.4, 7.5, 8.1 and 8.2. 

Corollary 9.7. An anticommutative Engel algebra A has infinite level 5 if and only if it is stably isomorphic to η5, T<sup>2,2</sup> (ǫ<sup>n</sup> 45<sup>),T 3(ǫn</sup> 34<sup>),T 2,2,2(ǫn</sup> 24<sup>),T 3,2(ǫn</sup> 23<sup>),T 2,2,2,2,2,T 3,2,2orT 4.</sup> 

Corollary 9.8. Any anticommutative Engel algebra of level not greater than 5 is a Malcev algebra. Moreover, any such an algebra is a Lie algebra except the algebra T<sup>3</sup> (ǫ<sup>n</sup> 34<sup>)andthe</sup> seven-dimensional algebra T<sup>2,2,2</sup> (ǫ23<sup>4−ǫ7</sup> 26<sup>+ǫ7</sup> 35<sup>)incharacteristicnotequalto3.</sup> 

Corollary 9.9. Any anticommutative Engel algebra of level not greater than five is nilpotent. 

9 Main Theorem 

26 

Remark 9.10. Since all algebras in our classification are nilpotent Malcev algebras by Corollaries 9.9 and 9.8, the classification of anticommutative Engel algebras with level not greater than five of dimension six can be obtained from [9, Theorem 8]. 

Acknowledgements. The work was supported by the Russian Science Foundation research project number 19-71-10016. The author is a Young Russian Mathematics award winner and would like to thank its sponsors and jury. 

## References 

- [1] Bovdi V., Gerasimova T., Salim M., Sergeichuk V., Reduction of a pair of skewsymmetric matrices to its canonical form under congruence, Linear Algebra Appl., 534 (2018), 17–30. 

- [2] Dmytryshyn A., K˚agstr¨om B., Orbit closure hierarchies of skew-symmetric matrix pencils, SIAM J. Matrix Anal. Appl., 35 (2014), 1429–1443. 

- [3] Francese J., Khudoyberdiyev A., Rennier B., Voloshinov A., Classification of algebras of level two in the variety of nilpotent algebras and Leibniz algebras, J. Geom. Phys., 134 (2018), 142–152. 

- [4] Gantmacher F. R., The Theory of Matrices, Vol. 2, AMS Chelsea Publishing, Providence, RI (1998). 

- [5] Gorbatsevich V., On contractions and degeneracy of finite-dimensional algebras, Soviet Math. (Iz. VUZ), 35 (1991), 10, 17–24. 

- [6] Gorbatsevich V., Anticommutative finite-dimensional algebras of the first three levels of complexity, St. Petersburg Math. J., 5 (1994), 505–521. 

- [7] In¨on¨u E., Wigner E.P., On the contraction of groups and their representations, Proc. Natl. Acad. Sci. USA, 39 (1953), 510–524. 

- [8] Ivanova N. M., Pallikaros C. A., On degenerations of algebras over an arbitrary field, AGTA, 7 (2019), 39–83. 

- [9] Kaygorodov I., Popov Yu., Volkov Yu., Degenerations of binary Lie and nilpotent Malcev algebras, Comm. Algebra, 46 (2018), 11, 4929–4941. 

- [10] Kaygorodov I., Volkov Yu., The variety of 2-dimensional algebras over an algebraically closed field, Canad. J. Math., 71 (2019), 4, 819–842. 

- [11] Kaygorodov I., Volkov Yu., Complete classification of algebras of level two, Moscow Math. J., 19 (2019), 3, 485–521. 

- [12] Khudoyberdiyev A., The classification of algebras of level two, J. Geom. Phys., 98 (2015), 13–20. 

- [13] Khudoyberdiyev A., Omirov B., The classification of algebras of level one, Linear Algebra Appl., 439 (2013), 11, 3460–3463. 

9 Main Theorem 

27 

- [14] Koreshkov N. A., Haritonov D. U., About Nilpotency of Engel Algebras, Russ. Math., 45 (2001), 11, 15–18. 

- [15] Kuz’min E. N., On anticommutative algebras satisfying the engel condition, Sib. Math. J., 8 (1967), 5, 779–785. 

- [16] Scharlau R., Paare alternierender Formen, Math. Z., 147 (1976), 13–19. 

- [17] Seeley C., Degenerations of 6-dimensional nilpotent Lie algebras over C, Comm. Algebra, 18 (1990), 3493–3505. 

- [18] Waterhouse W., Pairs of symmetric bilinear forms in characteristic 2, Pacific J. Math., 69 (1977), 1, 275–283. 

Addresses: Yury Volkov Saint-Petersburg State University Universitetskaya nab. 7-9, St. Peterburg, Russia e-mail: wolf86 666@list.ru 

