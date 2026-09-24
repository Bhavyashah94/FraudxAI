---
title: "Impossibility Theorems for Feature Attribution"
authors: "unknown"
year: 2022
arxiv_id: "2209.11370"
original_file: "2209.11370.pdf"
pdf_path: "docs/papers\2022_unknown_impossibility_theorems_for_feature.pdf"
---

# Impossibility Theorems for Feature Attribution

**Authors:** Unknown et al.  
**Year:** 2022 | **arXiv:** [`2209.11370`](https://arxiv.org/abs/2209.11370)  
**Local PDF:** [`2022_unknown_impossibility_theorems_for_feature.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2022_unknown_impossibility_theorems_for_feature.pdf)

---

ON THE CONVEXITY OF GENERAL INVERSE σk EQUATIONS 

## CHAO-MING LIN 

Abstract. We prove that if a level set of a degree n general inverse σk equation f (λ1, · · · , λn) := λ1 · · · λn −<sup>�n</sup> k=0<sup>−1ckσk(λ)=0iscontainedinq+Γnforsomeq∈Rn,whereckarereal</sup> numbers not necessary to be non-negative and Γn is the positive orthant, then this level set is convex. As an application, this result justifies the convexity of the level set of all general inverse σk type equations, for example, the Monge–Amp`ere equation, the Hessian equation, the J-equation, the deformed Hermitian–Yang–Mills equation, the special Lagrangian equation, etc. Moreover, we find a numerical condition to verify whether a level set of a general inverse σk equation is contained in q + Γn for some q ∈ R<sup>n</sup> , which is a way to determine the convexity of this level set. 

# 1. Introduction 

Let (M, ω) be a compact connected K¨ahler manifold of complex dimension n with a K¨ahler form ω and [χ0] ∈ H<sup>1,1</sup> (M ; R), where H<sup>1,1</sup> (M ; R) is the (1, 1)-Dolbeault cohomology group. The study of the solvability of the following equation is widely considered: 



where ck are real functions on M and χ ∈ [χ0] is a real smooth, closed (1, 1)-form. We call an equation having the same format as equation (1.1) a degree n general inverse σk type equation. A general inverse σk type equation (1.1) is very likely to be ill-posed, but some special combinations of the coefficients raise some famous equations. For example, by letting [χ0] be a K¨ahler class, ck = 0 for all k ∈{1, · · · , n−1}, and c0 be a positive function, equation (1.1) becomes the complex Monge– Amp`ere equation in the Calabi conjecture [8, 9], which was solved by Yau [60]. Inspired by the study of the Hermitian–Yang–Mills connections by Donaldson [21] and Uhlenbeck–Yau [58], Donaldson [22] studied the J-equation using the moment map. The J-equation was studied extensively by Collins–Sz´ekelyhidi [16], Chen [11], Song–Weinkove [53], and the references therein. The J-equation can be obtained by letting [χ0] be a K¨ahler class, ck = 0 for all k ∈{0, · · · , n − 2}, and cn−1 be a positive constant. Lejmi–Sz´ekelyhidi [39] conjectured that the existence of the solution to the J-equation is equivalent to a certain stability condition. Chen [10] studied the solvability and the stability of the J-equation using a Nakai–Moishezon type criterion and proved this conjecture under a slightly stronger condition. The Nakai–Moishezon type criterion was inspired by the work of Demailly–P˘aun [20]. Song [54] extended the method of Chen [10] and confirmed the conjecture by Lejmi–Sz´ekelyhidi [39]. Chen [10] also extended the J-equation slightly so that the real function c0 can be slightly negative but satisfies the integral condition. The general inverse σk equation was raised by Chen [11] and some special cases were treated by Collins–Sz´ekelyhidi [16] and Fang– Lai–Ma [24]. Collins–Sz´ekelyhidi [16] considered the case when ck, for k ∈{0, · · · , n − 1}, are non-negative constants satisfying the integral condition. Collins–Sz´ekelyhidi proved that if there exists a C-subsolution (introduced by Sz´ekelyhidi [56] and Guan [27] and will be discussed later in Section 2.2), then this special case is solvable. Datar–Pingali [19] extended the techniques in Chen [10] and Song [54] to this special case of the general inverse σk equation. Motivated 

1 

by mirror symmetry in string theory, the deformed Hermitian–Yang–Mills equation, which will be abbreviated to the dHYM equation from now on, was discovered around the same time by Mari˜no– Minasian–Moore–Strominger [44] and Leung–Yau–Zaslow [38] using different points of view. The dHYM equation was initiated by Jacob–Yau [34] and can be formulated as follows: 



Here ℑ and ℜ are the imaginary and real parts, respectively, and θ is a topological constant determined by the cohomology classes [ω] and [χ0]. If the phase θ lies in<sup>�</sup> (n − 2)π/2, nπ/2<sup>�</sup> , that is, if θ is a supercritical phase, Collins–Jacob–Yau [14] showed that if there exists a supercritical C- subsolution (which will be introduced and defined later in Section 2.2), then the dHYM equation is solvable. Collins–Jacob–Yau conjectured that the existence of the solution to the dHYM equation (1.2) is equivalent to a certain stability condition for all analytic subvarieties and confirmed this numerical conjecture for complex surfaces. Chen [10] proved a Nakai–Moishezon type criterion for the dHYM equation when the phase is supercritical under a slightly stronger condition that these holomorphic intersection numbers have a uniform lower bound independent of analytic subvarieties. Chu–Lee–Takahashi [12] improved the result by Chen [10] without assuming a uniform lower bound for these holomorphic intersection numbers on projective manifolds. Collins–Jacob–Yau [14] also conjectured that when θ is supercritical, if there exists a C-subsolution, then the dHYM equation is solvable. Lin [41] confirmed this conjecture by Collins–Jacob–Yau [14] of the solvability of the dHYM equation when the complex dimension equals three or four. We should emphasize that there are many significant works that have been done recently. The interested reader is referred to [13, 15, 17, 18, 32, 33, 35, 40, 43, 45, 46, 47, 48, 49, 50, 51, 59] and the references therein. We also want to remark that equation (1.1) also plays an important role on reals. For example, Caffarelli– Nirenberg–Spruck [7], Krylov [36, 37], and Trudinger [57] on the study of the Dirichlet problem for the Hessian equations on various settings. Also, Guan–Zhang [28] studied the solvability of a general class of curvature equations in convex geometry. 

Throughout all these works, the convexity of either the equation itself or the level set plays a crucial role. To be more precise, to get a priori estimates, we highly rely on convexity. If we write equation (1.1) in terms of the eigenvalues of the Hermitian endomorphism Λ = ω<sup>−1</sup> χ at a point, then we can rewrite equation (1.1) as 



where λi are the eigenvalues of Λ, σk(λ1, · · · , λn) is the k-th elementary symmetric polynomial of {λ1, · · · , λn}, and we denote σk(λ1, · · · , λn) by σk(λ) for convenience. The following multivariate polynomial in n variables {λ1, · · · , λn} 



is a special case of multilinear polynomials, that is, multivariate polynomials in which no variable occurs to a power of two or higher. We will call a multilinear polynomial having the same format as (1.4) a general inverse σk type multilinear polynomial. 

For the classical example, the complex Monge–Amp`ere equation considered by Yau [60], at a fixed point, can be rewritten as 



2 

where c is a positive value. If we write h = c/(λ1 · · · λn), then the Hessian of h will always be positive-definite when (λ1, · · · , λn) ∈ Γn, where Γn is the positive orthant. This implies that equation (1.5) is strictly convex, hence the level set {λ1 · · · λn − c = 0} is convex as well. In Fang– Lai–Ma [24], Fang–Lai–Ma considered some special combinations of non-negative constants ck for k ∈{0, · · · , n − 1} and proved the convexity of equation (1.3). Collins–Sz´ekelyhidi [16] generalized their results and proved the convexity of equation (1.3) when ck are non-negative constants for k ∈{0, · · · , n − 1}. For the special Lagrangian equation and the dHYM equation, Yuan [61] showed that if the phase is supercritical, then the level set of equation (1.2) is a smooth convex hypersurface even though the equation might not be convex. Collins–Jacob–Yau [14] obtained a priori estimates from the convexity of the level set of equation (1.2). Since we mainly focus on the general inverse σk equations in this work and because of the space limitations, the interested reader is referred to [6, 7, 10, 16, 23, 24, 25, 26, 31, 39, 52, 57] and the references therein. 

In this work, we will concentrate on the convexity of the level set of equation (1.3), which gives a huge hope on the solvability of equation (1.3). In [41], when complex dimension equals three or four, the author gave some constraints on the coefficients of equation (1.3) and proved the strict convexity of the level set of equation (1.3). The author also proved the solvability by finding a nice path under these constraints connecting the supercritical dHYM equation (1.2) to the general inverse σk equation with non-negative coefficients considered by Collins–Sz´ekelyhidi [16] and Fang–Lai–Ma [24] and by obtaining a priori estimates on this path. 

Let us state some of our settings, definitions, and results now. First, we introduce the following stableness condition for general inverse σk type multilinear polynomials. 

Definition 1.1 (Υ-stableness). Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσk</sup> type multilinear polynomial and Γ<sup>n</sup> f<sup>beaconnectedcomponentof{f(λ)>0}.Wesaythatthis</sup> connected component Γ<sup>n</sup> f<sup>off(λ)isΥ-stableif</sup> 

Γ<sup>n</sup> f<sup>⊆q + Γnforsomeq∈Rn,</sup> 

where Γn is the positive orthant of R<sup>n</sup> . We say that this connected component Γ<sup>n</sup> f<sup>isstrictly</sup> Υ-stable if it is Υ-stable and the boundary ∂Γ<sup>n</sup> f<sup>iscontainedintheΥ1-cone.</sup> 

The Υk-cones will be defined later in Section 2.2 for k ∈{1, · · · , n − 1}. In particular, the Υ1-cone is the C-subsolution cone introduced by Sz´ekelyhidi [56] and Guan [27]. With the Υ- stableness condition, in Section 3, we prove that the boundary ∂Γ<sup>n</sup> f<sup>ofΓn</sup> f<sup>willbeconvexifΓn</sup> f<sup>is</sup> strictly Υ-stable. In addition, we show that a connected component of {f = 0} is contained in q + Γn for some q ∈ R<sup>n</sup> is equivalent to Γ<sup>n</sup> f<sup>ofthisconnectedcomponentbeingstrictlyΥ-stable.</sup> In this case, this connected component equals ∂Γ<sup>n</sup> f<sup>.Wehavethefollowingmainresult.</sup> 

Theorem 1.1 (Convexity of the general inverse σk equation). Consider the following general inverse σk equation f (λ) := σn(λ) −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ) = 0,whereσkisthek-th elementarysymmetric</sup> polynomial and ck are real numbers not necessary to be non-negative. Let Γ<sup>n</sup> f<sup>beaconnected</sup> component of {f (λ) > 0}. If Γ<sup>n</sup> f<sup>isstrictlyΥ-stable,thentheboundary∂Γn</sup> f<sup>isconvex.</sup> 

The following general inverse σk type equations are all strictly Υ-stable, we will verify some of them in Section 4. 

Remark 1.1. The following general inverse σk type equations are all strictly Υ-stable: 

- Complex Monge–Amp`ere equation. 

- J-equation. 

- Hessian equation. 

3 

- Deformed Hermitian–Yang–Mills equation with supercritical phase. 

- Special Lagrangian equation with supercritical phase. 

- General inverse σk equation with non-negative ck for k ∈{0, · · · , n − 1}. 

In practice, verifying the Υ-stableness condition is not easy. Here, we introduce the following class of special univariate polynomials which plays an important role in determining the convexity of general inverse σk equations. In Section 2.1, we will show more special properties of these special univariate polynomials. Now, we list some definitions and some interesting and important results. 

Definition 1.2 (Noetherian polynomial). We say a degree n real univariate polynomial p(x) is right-Noetherian if for all k ∈{0, · · · , n − 2}, there exists a real root of p<sup>(k)</sup> which is greater than or equal to the largest real root of p<sup>(k+1)</sup> ; left-Noetherian if for all k ∈{0, · · · , n − 2}, there exists a real root of p<sup>(k)</sup> which is less than or equal to the smallest real root of p<sup>(k+1)</sup> . Here p<sup>(k)</sup> is the k-th derivative of p. We say a right-Noetherian polynomial p(x) is strictly right-Noetherian if the largest real root of p(x) is strictly greater than the largest real root of p<sup>′</sup> (x). 

In Section 2.2, we will show that the right-Noetherianness condition is equivalent to the Υ- stableness condition in the following sense. We get the following Positivstellensatz-type result generalizing the work in [41]. When the degree is small, we can explicitly write down the constraints using the resultants, see Section 4 for more examples when the degree equals three or four. 

Theorem 1.2 (Positivstellensatz). A general inverse σk type multilinear polynomial 



has a connected component Γ<sup>n</sup> f<sup>whichisΥ-stableifandonlyifthediagonalrestrictionrf(x)of</sup> f (λ), which is defined by the following 



is right-Noetherian. Moreover, Γ<sup>n</sup> f<sup>isstrictlyΥ-stableifandonlyifrfisstrictlyright-Noetherian.</sup> 

As an application of the Positivstellensatz Theorem, in Section 4, we will verify some general inverse σk type equations including the general inverse σk equation with non-negative coefficients and the dHYM equation. As a quick consequence of the Positivstellensatz Theorem, we can show that the level set of the following general inverse σk equation is convex. This is also numerical checkable, which gives a large quantity of new convex sets. 

Example 1.1. The following univariate polynomial rf (x) = x<sup>5</sup> −<sup>�3</sup> k=0<sup>ck</sup> �k5�xk with c3 = 19, c2 = −64, c1 = 9, and c0 = −20 is strictly right-Noetherian. This is checkable using any computer. By rounding off to the third decimal place, we have 



Here, for k ∈{0, · · · , n − 1}, we denote by xk the largest real root of the k-th derivative rf<sup>(k)(x).</sup> This implies that the level set of the following general inverse σk equation is convex 



4 

If a general inverse σk type multilinear polynomial has an Υ-stable connected component, then, for convenience, we say this general inverse σk type multilinear polynomial is Υ-stable. In the following setting, we can also compare two Υ-stable general inverse σk type multilinear polynomials. Definition 1.3 (Υ-dominance). Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)andg(λ):=λ1 · · · λn−</sup> �kn=0−1<sup>dkσk(λ) be two Υ-stable general inverse σktype multilinear polynomials.For k∈{0, · · ·, n−</sup> 1}, we write xk the largest real root of the diagonal restriction rf<sup>(k)</sup> of f and yk the largest real root of the diagonal restriction rg<sup>(k)</sup> of g. If yk ≥ xk for all k ∈{0, · · · , n − 1}, then we say g ⋗ f . 

We then get another Positivstellensatz-type result. This result implies that for Υ-stable general inverse σk type multilinear polynomials, the Υ-dominance is equivalent to the set inclusion. Theorem 1.3 (Υ-dominance). Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)andg(λ):=λ1 · · · λn−</sup> �kn=0−1<sup>dkσk(λ)betwoΥ-stablegeneralinverseσktypemultilinearpolynomials.Theng ⋗fifand</sup> only if Γ<sup>n</sup> g<sup>⊂Γn</sup> f<sup>.</sup> 

Example 1.2. The following univariate polynomial rg(x) = x<sup>5</sup> −<sup>�3</sup> k=0<sup>dk</sup> �k5�xk with d3 = 19, d2 = 65, d1 = −2, and d0 = −24 is strictly right-Noetherian with roots: 



Here, for k ∈{0, · · · , 4}, we denote by yk the largest real root of the k-th derivative rg<sup>(k)(x).We</sup> compare this Υ-stable general inverse σk type multilinear polynomial with the one in Example 1.1. Since y0 > x0, y1 > x1, y2 > x2, y3 = x3, and y4 = x4, we have g ⋗ f . By Theorem 1.3, we get 





In this work, we find a way to determine the convexity of any general inverse σk equation f (λ) = λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ) = 0usingeitherthestrictΥ-stablenessconditionorequivalently</sup> the strict right-Noetherianness condition. Our next goal is to determine the solvability of any general inverse σk equation on a compact connected K¨ahler manifold satisfying either condition at every point on the manifold. 

Special univariate and multivariate polynomials are widely studied in many different fields. For example, for multivariate polynomials, the class of Lorentzian polynomials considered by Br¨and´en– Huh [5] and Huh–Matherne–M´esz´aros–Dizier [30], which contains the class of homogeneous stable polynomials including volume polynomials of convex bodies and projective varieties, is important in the study of matroid theory. In addition, the classes of strongly log-concave polynomials in Gurvits [29], completely log-concave multivariate polynomials in Anari–Gharan–Vinzant [1], Anari–Liu– Gharan–Vinzant [2, 3], and Anari–Liu–Gharan–Vinzant–Vuong [4], are also crucial in the matroid theory. In [5], Br¨and´en–Huh proved that a homogeneous polynomial with non-negative coefficients is Lorentzian if and only if it is strongly log-concave. 

Here, we list one of many special properties of right-Noetherian polynomials. We will state the definitions explicitly and more properties in Section 2.1. We define the log-concavity ratio αf (x) of an analytic univariate function f (x) in Section 2.1. Roughly speaking, it is defined by 



If f (x) > 0 and αf (x) ≤ 1 on an open interval I, then f will be logarithmically concave on I. We prove that this log-concavity ratio will be monotonic for right-Noetherian polynomials. In 

5 



Figure 1. αp(x) of p(x) = x<sup>5</sup> − 19<sup>�</sup> 3<sup>5</sup> �x3 + 64�25�x2 − 9�15�x1 + 20�05�x0 

Figure 1, we plot the log-concavity ratio αp(x) of p(x) = x<sup>5</sup> −19<sup>�</sup> 3<sup>5</sup> �x3+64�25�x2−9�15�x1 +20�05�x0 = x<sup>5</sup> − 190x<sup>3</sup> + 640x<sup>2</sup> − 45x + 20, which is right-Noetherian by Example 1.1. 

Theorem 1.4 (Monotonicity of log-concavity ratio). Let p(x) be a real univariate polynomial of degree n which is right-Noetherian. Then the log-concavity ratio αp(x) of p is monotonically increasing on (x1, ∞) with value from −∞ to 1 − 1/n if x0 > x1 and on [x0, ∞) with value from 1 − 1/m to 1 − 1/n if x0 = x1. Here, x0 is the largest real root of p, x1 is the largest real root of p<sup>′</sup> , and m is the multiplicity of p at x0. In particular, if p is right-Noetherian, then p is always logarithmically concave when x > x0. 

As a quick consequence, we show that after a translation, the right-Noetherian polynomials will be strongly log-concave. The definitions are stated in Section 2.1. 

Lemma 1.1. Let p(x) be a real univariate polynomial of degree n which is right-Noetherian, then p is strongly log-concave after the translation x �→ x − x0. Here, x0 is the largest real root of p(x). 

In Theorem 1.1, we prove that the level set will be convex. But it is still open whether the level set will be strictly convex in the following sense. 

Conjecture 1.1 (Strict convexity of the general inverse σk equation). Consider the following general inverse σk equation f (λ) := σn(λ) −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ) = 0.Ifthediagonal restrictionrf(x)off(λ)is</sup> strictly right-Noetherian, then the level set {f = 0} is strictly convex. That is, the n − 1 × n − 1 Hessian matrix Ä ∂λ∂2iλ∂λn j äi,j∈{1,··· ,n−1}<sup>,where</sup> 



is positive-definite on the level set {f = 0}. 

When the degree equals three, Pingali [49] showed that the 2 × 2 Hessian matrix of λ3 for the dHYM equation will be positive-definite. In [41], the author showed that the Hessian matrix of the dHYM equation will be positive-definite on the level set when the degree equals four. Here, we prove the following result, which gives convincing evidence that Conjecture 1.1 is true. 

Lemma 1.2. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσktypemultilinear</sup> polynomial. If the diagonal restriction rf (x) of f is strictly right-Noetherian, then on the curve {λ1 = · · · = λn−1} of the level set {f = 0} with λ1 > x1, the positive definiteness of the following n − 1 × n − 1 Hessian matrix 



6 

The layout of this paper is as follows: in Section 2, we discuss some background materials. In Section 2.1, we introduce the class of right-Noetherian polynomials, which is related to the largest real roots of the derivatives of the polynomials. We show some special properties of the class of right-Noetherian polynomials. In Section 2.2, we consider some special semialgebraic sets in real algebraic geometry, which are defined by systems of inequalities of polynomials with real coefficients. To be more precise, we introduce the notion of Υ-cones, which is an extension of the C- subsolution cone introduced by Sz´ekelyhidi [56]. Roughly speaking, we consider the C-subsolution cone, the C-subsolution cone of the C-subsolution cone, the C-subsolution cone thereof, etc. We define the Υ-stableness condition and show that the Υ-stableness condition is equivalent to the right-Noetherianness condition for any general inverse σk type multilinear polynomial. We also obtain a Positivstellensatz-type result over these semialgebraic sets and another Positivstellensatztype result comparing two general inverse σk type multilinear polynomials. In Section 3, we prove that if a level set of any general inverse σk equation after translation is contained in the positive orthant, then this level is convex. In Section 4, we show that the convexities of some classical general inverse σk type equations are immediate consequences of our main theorem. For example, we verify the convexity of any general inverse σk equation with degree less than or equal to four, the convexity of the general inverse σk equation with non-negative coefficients, and the convexity of the dHYM equation with supercritical phase. 

Acknowledgements: The author is grateful to Zhiqin Lu and Xiangwen Zhang for giving me enlightening help. The author would like to thank Tristan Collins for his interest in this work. The author would like to thank Chen-Yu Chi for several helpful conversations and Hsin-Po Wang for some programming support. The author would like to thank Biao Ma and Hao Fang for pointing out a mistake in the proof of the convexity theorem in the previous version, we give a new proof and fix this mistake. 

# 2. Preliminaries 

2.1. Definition and Properties of right-Noetherian Polynomials. In this subsection, we introduce the class of Noetherian polynomials, which will be used throughout this paper. The class of Noetherian polynomials has some special properties and will help us determine the convexity of the level set of any general inverse σk type equation. We will see this in the later sections. 

Definition 2.1 (Noetherian polynomial). We say a degree n real univariate polynomial p(x) is right-Noetherian if for all k ∈{0, · · · , n − 2}, there exists a real root of p<sup>(k)</sup> which is greater than or equal to the largest real root of p<sup>(k+1)</sup> ; left-Noetherian if for all k ∈{0, · · · , n − 2}, there exists a real root of p<sup>(k)</sup> which is less than or equal to the smallest real root of p<sup>(k+1)</sup> . Here p<sup>(k)</sup> is the k-th derivative of p. We say a right-Noetherian polynomial p(x) is strictly right-Noetherian if the largest real root of p(x) is strictly greater than the largest real root of p<sup>′</sup> (x). 

Proposition 2.1. Let p(x) be a real univariate polynomial of degree n which is right-Noetherian. Then for any k ∈{0, · · · , n − 1}, there exists a unique (ignoring multiplicity) real root of p<sup>(k)</sup> (x) which is greater than or equal to the largest real root of p<sup>(k+1)</sup> (x). Moreover, this real root is the largest real root of p<sup>(k)</sup> (x). In particular, if we denote xk to be the largest real root of p<sup>(k)</sup> (x), then 

x0 ≥ x1 ≥· · · ≥ xn−1. 

Proof. We prove this statement by mathematical induction on the degree n. When n = 1, there is nothing to prove. When n = 2, p<sup>′</sup> (x) is a degree 1 polynomial and the only root will be the midpoint of the roots of p(x). By the definition of right-Noetherianness, there exists a real root of 

7 

p(x) which is greater than or equal to the largest real root of p<sup>′</sup> (x). Thus p(x) is real rooted and if we ignore the multiplicity, then there exists a unique real root of p(x) which is greater than or equal to the largest real root of p<sup>′</sup> (x). Moreover, this real root will be the largest real root of p(x). Suppose the statement is true when n = m − 1. When n = m, it suffices to check p(x), the rest follows by mathematical induction. If there exists x0 and x˜0 with 



where x1 is the largest real root of p<sup>′</sup> (x). For convenience, we assume that the polynomial p(x) is monic, we write 



Then p<sup>′</sup> (x) = nx<sup>n−1</sup> +<sup>�</sup> k<sup>n</sup> =1<sup>−1kckxk−1.Sincex1isthelargest realroot of p′(x),foranyx > x1,we</sup> have p<sup>′</sup> (x) > 0. By the fundamental theorem of calculus, we have 



which is a contradiction. This finishes the proof. 



We give a quick example of right-Noetherian polynomial, the right-Noetherianness condition is checkable by any computer using long division algorithm and Sturm’s theorem. 

Example 2.1. The following univariate polynomial p(x) = x<sup>5</sup> −<sup>�3</sup> k=0<sup>ck</sup> �k5�xk with c3 = 19, c2 = 65, c1 = −2, and c0 = −24 is strictly right-Noetherian. This is checkable using any computer. By rounding off to the third decimal place, we have 



Here, for k ∈{0, · · · , 4}, we denote by xk the largest real root of the k-th derivative p<sup>(k)</sup> (x). 

Proposition 2.2. Let p(x) be a real univariate polynomial of degree n which is real rooted, that is, all roots are real numbers, then p(x) is both right-Noetherian and left-Noetherian. 

Proof. This follows immediately by the Gauss–Lucas theorem. If p(x) is real rooted, then the roots of p<sup>′</sup> (x) will be contained in the convex hull of the set of roots of p(x). So p<sup>′</sup> (x) will also be real rooted, the rest follows directly by mathematical induction. This finishes the proof. □ 

Remark 2.1. A right-Noetherian polynomial might not be real rooted, a simple example will be p(x) = x<sup>3</sup> − 1. Then we have p<sup>′</sup> (x) = 3x<sup>2</sup> and p<sup>′′</sup> (x) = 6x. If we denote by xi the largest real root of p<sup>(i)</sup> (x), then x0 = 1, x1 = 0, and x2 = 0. So p(x) will be right-Noetherian due to x0 ≥ x1 ≥ x2. But the roots of p(x) = x<sup>3</sup> − 1 are: 1, (−1 +<sup>√</sup> −3)/2, and (−1 −<sup>√</sup> −3)/2. 

The log-concavity property of special univariate or multivariate polynomials were studied extensively by Br¨and´en–Huh [5], Gurvits [29], Anari–Gharan–Vinzant [1], Anari–Liu–Gharan–Vinzant [2, 3], and Anari–Liu–Gharan–Vinzant–Vuong [4]. For the class of right-Noetherian polynomials, we not only show that any right-Noetherian polynomial will be strongly log-concave after translation, but we also show that the ratio, which will be defined now, will be monotone. 

8 

Definition 2.2 (Log-concavity ratio). Let f : I → R be an analytic function, I be an open interval in R, and define Cf := {x ∈ I : f<sup>′</sup> (x) = 0}. For any point x ∈ I, we define the log-concavity ratio αf (x) of f (x) to be the following 



if x ∈/ Cf . If x ∈ Cf is a limit point of Cf , then we define αf (x) to be 0, otherwise we define 

where we allow αf (x) = ∞ or αf (x) = −∞. 

Remark 2.2. Let f : I → R be an analytic function and I be an open interval in R, if αf (x) ≤ 1 for all x ∈ I, then f is logarithmically concave on {f > 0}. 

The following Proposition 2.3 shows that for any real univariate polynomial p(x), p(x) (or −p(x)) will eventually be logarithmically concave when x is sufficiently large. 

Proposition 2.3. Let p be a real univariate polynomial of degree n, then 



In particular, there exists a N > 0 sufficiently large such that p (or −p depends on the sign of the leading coefficient) is logarithmically concave on (N, ∞). 

Proof. For x sufficiently large, if we write p(x) =<sup>�n</sup> k=0<sup>ckxk,thenbyequation(2.1),wehave</sup> 



Since p is a polynomial, by letting x approach ∞, we can avoid critical points and get 

This finishes the proof. 

□ 

The derivative of the log-concavity ratio in Definition 2.2 of any real univariate polynomial will satisfy the following. 

Lemma 2.1. Let p(x) be a real univariate polynomial of degree n. For k ∈{1, · · · , n − 1} and x > xk, where xk is the largest real root of p<sup>(k)</sup> , then α<sup>′</sup> p<sup>(k−1)(x)<0when2>αp(k)(x)and</sup> αp(k−1) (x) > 1/(2 − αp(k) (x)). On the other hand, α<sup>′</sup> p<sup>(k−1)(x) > 0 when αp(k)(x) ≥2 or 2 > αp(k)(x)</sup> and 1/(2 − αp(k) (x)) > αp(k−1) (x). 

Proof. By taking the derivative of αp(k−1) (x) with respect to x, we get 



9 

Then the numerator of equation (2.3) will give us 



For convenience, we assume the leading coefficient is positive. When 2 > αp(k) (x) and αp(k−1) (x) > 1/(2 − αp(k) (x)), then since x is greater than the largest real root of p<sup>(k)</sup> , we get 



On the other hand, when αp(k) (x) ≥ 2 or 2 > αp(k) (x) and 1/(2 − αp(k) (x)) > αp(k−1) (x), we get 



Now, with all these preparations, we are able to prove the following important result for the class of right-Noetherian polynomials. 

Theorem 2.1 (Monotonicity of log-concavity ratio). Let p(x) be a real univariate polynomial of degree n which is right-Noetherian. Then the log-concavity ratio αp(x) of p(x) is monotonically increasing on (x1, ∞) with value from −∞ to 1 − 1/n if x0 > x1 and on [x0, ∞) with value from 1 − 1/m to 1 − 1/n if x0 = x1. Here, x0 is the largest real root of p, x1 is the largest real root of p<sup>′</sup> , and m is the multiplicity of p at x0. In particular, if p is right-Noetherian, then p is always logarithmically concave when x > x0. 

Proof. For convenience, we may assume that p(x) is monic. By the definition of right-Noetherian, if we denote xi by the largest real root of p<sup>(i)</sup> (x), then by Proposition 2.1, we have 



We use mathematical induction on the degree of polynomial. For the base case, when p is a degree 2 polynomial, since p has a real root x0, we write 

(2.4) p(x) = (x − x0)(x − (2x1 − x0)) 

with x0 ≥ x1. If x > x1, then by equation (2.4), we have 



So, for degree 2 polynomial, αp(x) is monotonically increasing from 0 to 1/2 from x0 to ∞ if x0 = x1 and from −∞ to 1/2 from x1 to ∞ if x0 > x1. Suppose the statement holds when the degree equals n − 1. When the degree equals n, say the multiplicity of the largest real root x0 equals m ≥ 1. We have 



10 

by using the Taylor series expansion of p(x) at x0 and set 



So the first and the second derivative of (2.5) with respect to x can be written as 

(2.6) p<sup>′</sup> (x) = (x − x0)<sup>m−1�</sup> mp˜(x) + (x − x0)˜p<sup>′</sup> (x)<sup>�</sup> ; 

(2.7) p<sup>′′</sup> (x) = (x − x0)<sup>m−2�</sup> m(m − 1)˜p(x) + 2m(x − x0)˜p<sup>′</sup> (x) + (x − x0)<sup>2</sup> p˜<sup>′′</sup> (x)<sup>�</sup> . 

If m = 1, then similar to before, we get αp(x0) = 0 and limx→x+1<sup>αp(x) = −∞.Ifm ≥2,then</sup> 



There are two cases to consider: m = 1 or m ≥ 2. For the case m = 1, since p<sup>′</sup> is again rightNoetherian, αp′ is monotonically increasing on [x1, ∞) with value from 1 − 1/ ˜m to 1 − 1/(n − 1), where m˜ is the multiplicity of p<sup>′</sup> at x1. When x > x1, by Lemma 2.1, α<sup>′</sup> p<sup>(x) > 0when2 > αp′(x)</sup> and 1/(2 − αp′ (x)) > αp(x). We have 2 > 1 − 1/(n − 1) > αp′ (x) and 



If we consider the set I :=<sup>�</sup> x ∈ (x1, ∞): 1/(2 − αp′ (x)) > αp(x)<sup>�</sup> , then the set I is not empty. If we can show that I = (x1, ∞), then we are done. I will be open by the continuity of functions αp and αp′ . If I̸ = (x1, ∞), then we can find a smallest x˜ ∈ (x1, ∞) such that 1/(2 − αp′ (x)) = αp(x). This is ensured because p is a polynomial and 







On the other hand, since p<sup>′</sup> is right-Noetherian and by mathematical induction, we have 

(2.9) 



11 

We get a contradiction. Otherwise by standard calculus argument and equation (2.8), there exists a δ > 0 sufficiently small such that if |h| < δ, then we have 



Since x˜ is the smallest value such that 1/(2 − αp′ (x)) = αp(x) and limx→x+1<sup>αp(x)=−∞,bythe</sup> intermediate value theorem, we have x˜ − h ∈ I where δ > h > 0. Hence, by inequalities (2.10) and (2.11), we obtain 



This is a contradiction because α<sup>′</sup> p<sup>′(x)>0bymathematicalinduction.SoI=(x1, ∞).Ifthe</sup> multiplicity of x0 equals 1, then αp is increasing on (x1, ∞) with value from −∞ to 1 − 1/n. 

For the second case, if the multiplicity of x0 is greater than or equal to 2, then at x0 we have αp(x0) = 1 − 1/m and αp<sup>′</sup> (x0) = 1 − 1/(m − 1). This gives 



We need to do some local analysis near x0. First, we have 



Same as before, we only need to consider the term p<sup>′</sup> (x)<sup>2</sup> p<sup>′′</sup> (x) + p(x)p<sup>′</sup> (x)p<sup>′′′</sup> (x) − 2p(x)p<sup>′′</sup> (x)<sup>2</sup> . By equations (2.6) and (2.7), we get 





When x > x0 is sufficiently close to x0, since 2mp˜(x)<sup>2</sup> p˜<sup>′</sup> (x) > 0, we get 



12 

Similarly, we define the set I := �x ∈ (x0, ∞): 1/(2 − αp′ (x)) > αp(x)� which is open and nonempty. Same as the previous argument, we get I = (x0, ∞), which implies that αp is increasing on [x0, ∞) with value from 1 − 1/m to 1 − 1/n. This finishes the proof. □ 

As an application, we immediately obtain that for a right-Noetherian polynomial p(x), the roots of p(x), the roots of p<sup>′</sup> (x), and the root of p<sup>′′</sup> (x) will satisfy the following relation. 

Proposition 2.4. Let p(x) be a real univariate polynomial of degree n which is right-Noetherian. If we denote all the roots of p(x) by α1, · · · , αn, all the roots of p<sup>′</sup> (x) by β1, · · · , βn−1, and all the roots of p<sup>′′</sup> (x) by γ1, · · · , γn−2. If we write xk the largest real root of p<sup>(k)</sup> (x), then for x > x1, 



is monotonically increasing to 1 when x approaches infinity. 

Proposition 2.5. Let p(x) be a real univariate polynomial of degree n which is right-Noetherian, then 



for x ≥ x1, where x1 is the largest real root of p<sup>′</sup> (x). In particular, for x ≥ x1, 



Proof. By Theorem 2.1, for x > x1, we have 



By multiplying them together, we always get the following upper bound: 



Moreover, for x = x1, since p is right-Noetherian, we have 



Also, for x > x1, we have 

This finishes the proof. 

For the class of right-Noetherian polynomials, we show that this class will be strongly log-concave after translation. We state the definitions here. 

Definition 2.3 (Strongly log-concave). Let p(x1, · · · , xn) be a multivariate polynomial, we say p is strongly log-concave if any order partial derivative is either identically zero or log-concave on R<sup>n</sup> >0<sup>.</sup> 

Lemma 2.2. Let p(x) be a real univariate polynomial of degree n which is right-Noetherian, then p is strongly log-concave after the translation x �→ x − x0. 

Proof. This follows directly by Theorem 2.1. 

□ 

13 



<!-- Start of picture text -->
3/4<br>2/3<br>1/2<br>x<br><!-- End of picture text -->

Figure 2. Value of αP along the deformation of (x − 5)<sup>2</sup> (x<sup>2</sup> + 10x + 51) 

We prove the following deformation result for the class of right-Noetherian polynomials. The idea here is to deform the largest real root x0 of p to the next largest real root xm of p<sup>(m)</sup> for some m ∈{1, · · · , n − 1} and keep the m-th partial derivative same. Along this deformation, the rightNoetherianness is remained and this deformation will be monotone. In Figure 2, we plot the value of the log-concavity ratio along the deformation of (x−5)<sup>2</sup> (x<sup>2</sup> +10x+51) = x<sup>4</sup> −24x<sup>2</sup> −260x+1275. 

Theorem 2.2. Let p(x) be a real univariate polynomial which is right-Noetherian with x0 ≥ x1 ≥ · · · ≥ xn−1, where xi is the largest real root of p<sup>(i)</sup> (x). Consider the following deformation 



where y ∈ [xm, x0] and m is the multiplicity of x0. Then for n − 1 ≥ m ≥ 1 and x > y > xm, 



Here, αP (x, y) is defined by 



Notice that because p(x) is right-Noetherian, p<sup>(k)</sup> (y) > 0 for y ∈ (xm, x0], k ∈{m, · · · , n}, and p<sup>(m)</sup> (xm) = 0. In particular, this deformation is a foliation that foliates the following set 



Proof. The idea of P (x, y) is to deform the largest real root x0 of p with multiplicity to the largest real root xm of p<sup>(m)</sup> and keep the m-th partial derivative concerning x the same. Along this deformation, the right-Noetherianness is remained and the multiplicity of the largest real root will be remained m but jump to at least m + 1 when y = xm. First, we have the following properties 



14 

for l ∈{0, · · · , m − 1}. With these, for y ∈ �xm, x0�, if we treat y as a fixed value, then 



which implies that y is the largest real root of P (x, y) with multiplicity m for y ∈<sup>�</sup> xm, x0�. If y = xm, then since p<sup>(m)</sup> (xm) = 0, we get 



The largest real root xm of P (x, xm) has multiplicity greater than or equal to m + 1. For l ∈ {0, · · · , m − 1}, we have 



Now, for convenience, we denote ∂<sup>l</sup> P/∂x<sup>l</sup> by P<sup>(l)</sup> (x, y). For x > y, by equation (2.12), we may compute 





Hence, by combining equations (2.13), (2.14), and (2.15), we obtain 





When m = 1 or 2, every terms of (2.16) are negative, then we are done. When m = n − 1, we have P<sup>˜′′</sup> = 0, the remaining terms of (2.16) are all negative. When n − 2 ≥ m ≥ 3, we consider 

15 

the following term: 



Similarly, we obtain 



for k ∈{0, · · · , n − m − 1}. When k = n − m − 1, P<sup>˜(n−m−1)</sup> is a polynomial of degree 1, so we automatically have αP ˜<sup>(n−m−1)≡0.Wehave2>α</sup> P<sup>˜(n−m−1)and1/(2 −α</sup> P<sup>˜(n−m−1))=1/2.When</sup> k = n − m − 2, by inequality (2.19), when x = y we have 



On the other hand, we have 

By Lemma 2.1, αP ˜<sup>(n−m−2)(x, y)willbedecreasingifthevalueα</sup> P<sup>˜(n−m−2)(x, y)exceeds1/(2−</sup> αP ˜<sup>(n−m−1)(x, y)) = 1/2.Combinethese,wehaveanupperbound</sup> 



for x ≥ y. In addition, for x ≥ y, we get 



One can check that 



Similar to the previous argument, by Lemma 2.1, we have the following upper bound 



16 

for x ≥ y. We claim that for any k ∈{0, · · · , n − m − 2}, we always have 

and 



The proof of these claims should be straightforward. Same as the previous argument, we have the following upper bound for x ≥ y, 



Thus, for n − 2 ≥ m ≥ 3, by the above upper bound, the quantity (2.17) will satisfy 



2.2. General Inverse σk Equations and Υ-Cones. In this subsection, we introduce the notion of Υ-cones, which is an extension of the C-subsolution cone introduced by Sz´ekelyhidi [56] and Guan [27]. The arguments in this subsection might be tedious because any set in this subsection might have more than one connected components, we need to specify which connected component we are considering. After all the arguments in this subsection, there will be no ambiguity, so we may assume the set is the connected component we are interested in. 

First, let us state some widely used notations, see Spruck [55] for more details. For an n-tuple numbers λ = {λ1, · · · , λn}, for k ∈{1, · · · , n}, the k-th elementary symmetric polynomial σk(λ) of λ will be 



We also define σ0(λ) := 1 for convenience. For l ∈{1, · · · , n} and pairwise distinct indices i1, · · · , il, where ij ∈{1, · · · , n} for all j ∈{1, · · · , l}, we denote the set λ −{λi1 , · · · , λil } by λ;i1,··· ,il. Consider the following general inverse σk type multilinear polynomial 



By doing the substitution µ = λ−cn−1, we get a new general inverse σk type multilinear polynomial: 



where µi = λi − cn−1. We have the following change of variables formula. 

Lemma 2.3. By doing the substitution µi = λi − cn−1 for all i ∈{1, · · · , n}, we have 



17 

and the coefficients dj for j ∈{1, · · · , n − 2} will be 



In addition, after substitution, the original general inverse σk type multilinear polynomial becomes 



and for all positive integer l and ia ∈{1, · · · , n} for all a ∈{1, · · · , l}, we have 

Proof. First, by doing the substitution µ = λ − cn−1, we have λ = µ + cn−1. Hence, 



Thus, we get 



So, for any j ∈{1, · · · , n − 2}, we have 



The rest follows by the change of variables formula. This finishes the proof. 



For convenience, by above Lemma 2.3, we may assume that cn−1 = 0 by doing a translation. In most of the proofs in this subsection, we will do this substitution to simplify the proofs. We consider the following general inverse σk type multilinear polynomial instead. 

(2.22) 



Now, we state the definition of C-subsolution here which was introduced by Sz´ekelyhidi [56] and Guan [27]. We will slightly adjust the settings in [56] because in this work we mainly focus on the level set not a global section on the manifold M . 

Definition 2.4 (C-Subsolution. Sz´ekelyhidi [56], Guan [27] and Trudinger [57]). Consider an equation f (λ1, · · · , λn) = h, where f (λ1, · · · , λn) is a smooth symmetric function of variables {λ1, · · · , λn}. We assume that f is defined in an open symmetric cone Γf ⊂ R<sup>n</sup> satisfying f > 0, 

18 

∂f/∂λi > 0 for all i ∈{1, · · · , n} on Γf , and sup∂Γf f < h. We say that µ = (µ1, · · · , µn) ∈ R<sup>n</sup> is a C-suboslution to the equation f = h if the following set 



is bounded. By collecting all the C-subsolutions, we call this collection the C-subsolution cone. 

Definition 2.5 (Alternative definition of Definition 2.4. Sz´ekelyhidi [56] and Trudinger [57]). Suppose that f is defined in an open symmetric cone Γf ⊂ R<sup>n</sup> satisfying f > 0, ∂f/∂λi > 0 for all i ∈{1, · · · , n} on Γf , and sup∂Γf f < h. Define 



For µ ∈ R<sup>n</sup> , set (2.23) F<sup>h</sup> (µ) is bounded if and only if limt→∞ f (µ + tei) > h for all i ∈{1, · · · , n}, where ei is the i-th standard vector. We denote by Γ<sup>n</sup> f<sup>−1,h</sup> the projection of Γ<sup>h</sup> f<sup>ontoRn−1by</sup> dropping the last entry. Then for any µ<sup>′</sup> = (µ1, · · · , µn−1) ∈ Γ<sup>n</sup> f<sup>−1,h</sup> , define the function f<sup>(n−1)</sup> on Γ<sup>n</sup> f<sup>−1,h</sup> by the following limit 



First, the set F<sup>h</sup> (µ) is bounded if and only if f<sup>(n−1)�</sup> µs(1), · · · , µs(n−1)� > h for every s ∈ Sn, where Sn is the symmetric group. This is well-defined since f is a symmetric function. We can show that for any µ ∈ R<sup>n</sup> , F<sup>h</sup> (µ) is bounded if and only if<sup>�</sup> µs(1), · · · , µs(n−1)� ∈ Γnf −1,h for every s ∈ Sn. 

Let Γ<sup>n</sup> f<sup>beaconnectedcomponentof{f(λ)>0},weareinterestedinwhetherthereexists</sup> a connected component of {f (λ) > 0} contained in the positive orthant Γn after translation. Inspired by the work of Trudinger [57] on the Dirichlet problem (over the reals) for equations of the eigenvalues of the Hessian, the results of Caffarelli–Nirenberg–Spruck [7], and the results of Collins–Sz´ekelyhidi [16]. In [41], the author introduced the Υ-cones to keep track of the information of the original equation as much as possible. We abstractly define the following sets. 

Definition 2.6 (Υ-cones. Lin [41]). Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneral inverse σk</sup> type multilinear polynomial and Γ<sup>n</sup> f<sup>beaconnectedcomponentof{f(λ) > 0},wedenotebyΓ</sup> f<sup>n−1</sup> the projection of Γ<sup>n</sup> f<sup>ontoRn−1bydroppingthelastentry.Wedefine</sup> 



where Sn is the symmetric group. For n − 1 ≥ k ≥ 2, we define the following Υ-cones 

Υk :=<sup>�</sup> µ ∈ R<sup>n</sup> :<sup>�</sup> µs(1), · · · , µs(n−k)� ∈ Γfn−k, ∀s ∈ Sn�, where we define Γf<sup>n−k</sup> inductively by the projection of Γ<sup>n</sup> f<sup>+1−k</sup> onto R<sup>n−k</sup> by dropping the last entry. 

Definition 2.7 (Υ-stableness). Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσk</sup> type multilinear polynomial and Γ<sup>n</sup> f<sup>beaconnectedcomponentof{f(λ)>0}.Wesaythatthis</sup> connected component Γ<sup>n</sup> f<sup>off(λ)isΥ-stableif</sup> 



where Γn is the positive orthant of R<sup>n</sup> . We say that this connected component Γ<sup>n</sup> f<sup>isstrictly</sup> Υ-stable if it is Υ-stable and the boundary ∂Γ<sup>n</sup> f<sup>iscontainedintheΥ1-cone.</sup> 

19 

Remark 2.3. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ) be a general inverse σktype multilinear polyno-</sup> mial and Γ<sup>n</sup> f<sup>be a connected component of {f(λ) > 0}.We willshow that if Γn</sup> f<sup>isstrictly Υ-stable,</sup> then the symmetric cone Γf in Definition 2.4 will always be contained in the Υ1-cone. Normally, we consider the largest possible Γf , which is in fact the Υ1-cone. So the Υ1-cone is the same as the C-subsolution cone introduced by Sz´ekelyhidi [56]. 

Lemma 2.4. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσktypemultilinearpoly-</sup> nomial and Γ<sup>n</sup> f<sup>beaconnectedcomponentof{f(λ) >0}.IfΓn</sup> f<sup>isΥ-stable,sayΓn</sup> f<sup>⊆q + Γnwith</sup> q = (q1, · · · , qn), then (2.25) Γ<sup>n</sup> f<sup>⊆Υ1⊆Υ2⊆· · · ⊆Υn−1= (cn−1, · · ·, cn−1) + Γn,</sup> cn−1 ≥ qi for all i ∈{1, · · · , n}. For any l ∈{1, · · · , n − 1}, we have Υl is open, connected, and 



∂<sup>l</sup> f Here, we write fi1···il as the l-th partial derivative ∂λi1 ···∂λil<sup>.</sup> 

Remark 2.4. Notice that for the above Lemma 2.4, we need to specify each connected component inductively on the subindices to avoid ambiguity. For example, when l = n − 2, the set 



will have two connected components. We specify the one which is contained in the next Υ-cone Υn−1 = (cn−1, · · · , cn−1) + Γn. Similarly, we specify the connected component inductively til Υ1 by decreasing the subindices. But for notational convention, we abbreviate these expressions. 

The Υ-stableness in fact gives us some constraints on the coefficients {ck}k=0,··· ,n−1. For example, if Γ<sup>n</sup> f<sup>isΥ-stable,thenc</sup> n<sup>2</sup> −1<sup>+ cn−2≥0.Otherwise,ifc2</sup> n−1<sup>+ cn−2< 0,then</sup> 



is not contained in Υn−1 = (cn−1, · · · , cn−1) + Γn, which violates the above Lemma 2.4. Later on, we will prove that the Υ-stableness condition is equivalent to the right-Noetherianness condition for the class of general inverse σk type multilinear polynomials. So the constraints can be derived using the resultants and can be written explicitly when the degree is low, see [41]. We will show some examples in Section 4 when the degree is less than or equal to four. 

Proof of Lemma 2.4. We prove this by mathematical induction on the degree n. We also show that there exists a unique connected component that intersects and is entirely contained in the next Υ-cone if Γ<sup>n</sup> f<sup>isΥ-stable.Aftertranslation,wemayassumecn−1= 0forconvenience andsay</sup> Γ<sup>n</sup> f<sup>iscontainedinq + Γnwithq= (q1, · · ·, qn) ∈Rn.Whenn = 1,f= λ1,weimmediatelyget</sup> 



So c1−1 = c0 = 0 ≥ q1, otherwise Γ<sup>1</sup> f<sup>willnotbecontainedinq + Γ1.Whenn = 2,f= λ1λ2 −c0,</sup> several cases must be considered. If c0 < 0, then {λ1λ2 − c0 > 0} will not be contained in q + Γ2 for any q ∈ R<sup>2</sup> , which contradicts the hypothesis that Γ<sup>2</sup> f<sup>isΥ-stable.Ifc0=0,then{λ1λ2>0}</sup> 

20 

has two connected components. Since Γ<sup>2</sup> f<sup>isΥ-stable,Γ2</sup> f<sup>isactuallythepositiveorthant,whichis</sup> one of the connected components of {λ1λ2 > 0}. So c2−1 = c1 = 0 ≥ qi for any i ∈{1, 2}. By the definition of Υ-cones, we get 



Similarly, if c0 > 0, then {λ1λ2 − c0 > 0} has two connected components. Since Γ<sup>2</sup> f<sup>isΥ-stable,Γ2</sup> f is the one contained in the positive orthant Γ2 and c2−1 = c1 = 0 ≥ qi for any i ∈{1, 2}. By the definition of Υ-cones, we get 



In conclusion, when n = 2, Γ<sup>2</sup> f<sup>istheuniqueconnectedcomponentof{f(λ) > 0}containedin</sup> 



Suppose that the statement is true when n = m − 1. When n = m, we have 



Suppose that there exists (λ1, · · · , λm) ∈ Γ<sup>m</sup> f<sup>,suchthat</sup> 



for some i ∈{1, · · · , m} and we denote ∂f/∂λi by fi. By fixing other entries, for λ<sup>˜</sup> i ≤ λi, we get 



This implies that (λ1, · · · , λi−1, λ<sup>˜</sup> i, λi+1, · · · , λm) ∈ Γ<sup>m</sup> f<sup>forallλ˜i≤λiduetotheassumptionthat</sup> Γ<sup>m</sup> f is connected. By letting λ<sup>˜</sup> i < qi, we see that Γ<sup>m</sup> f will not be contained in q + Γm, which leads to a contradiction. So for any i ∈{1, · · · , m}, Γ<sup>m</sup> f<sup>willbecontainedinoneoftheconnected</sup> component of 



For any (λ1, · · · , λm) ∈ Γ<sup>m</sup> f<sup>, since Γm</sup> f<sup>is contained in �σm−1(λ;i)−�m</sup> k=1<sup>−2ckσk−1(λ;i) > 0�for all i ∈</sup> {1, · · · , m}, we may construct a piecewise linear path connecting (λ1, · · · , λm) to (λmax, · · · , λmax), where λmax := max{λ1, · · · , λm}. Similarly, we can construct a piecewise linear path connecting (λs(1), · · · , λs(m)) to (λmax, · · · , λmax) for all s ∈ Sm. For any (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> m) on these continuity paths, we always have 



21 

This implies that (λs(1), · · · , λs(m)) are in the same connected component as (λ1, · · · , λm) for all s ∈ Sm. Hence, (λs(1), · · · , λs(m)) ∈ Γ<sup>m</sup> f for all s ∈ Sm. As a consequence, we similarly obtain that each connected component of<sup>�</sup> σm−1(λ;i) −<sup>�m</sup> k=1<sup>−2ckσk−1(λ;i)>0�willbethesame</sup> for all i ∈{1, · · · , m} after change of variables. Next, we prove that this connected component of<sup>�</sup> σm−1(λ;i) −<sup>�m</sup> k=1<sup>−2ckσk−1(λ;i)>0�iscontainedin(q1, · · ·, qi−1, qi+1, · · ·, qm) + Γm−1by</sup> ignoring the Cartesian product R term. Without loss of generality, we only consider the case i = 1. Let (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> m) ∈ Γ<sup>m</sup> f<sup>andconsiderthefollowingsection</sup> 



where f (λ<sup>˜</sup> ) = σm(λ<sup>˜</sup> ) −<sup>�m</sup> k=0<sup>−2ckσk(˜λ)>0.Noticethatthissectionλ1inΓm</sup> f<sup>isdefinedonthis</sup> connected component of<sup>�</sup> σm−1(λ;1) −<sup>�m</sup> k=1<sup>−2ckσk−1(λ;1) > 0�,continuous,and</sup> 



Moreover, for any (λ2, · · · , λm) ∈<sup>�</sup> σm−1(λ;1) −<sup>�m</sup> k=1<sup>−2ckσk−1(λ;1) > 0�weget</sup> 



Thus, if this connected component of<sup>�</sup> σm−1(λ;1) −<sup>�m</sup> k=1<sup>−2ckσk−1(λ;1)>0�isnotcontainedin</sup> (q2, · · · , qm) + Γm−1, then Γ<sup>m</sup> f<sup>isnotcontainedinq+ Γm.Thiscontradictsthehypothesisthat</sup> Γ<sup>m</sup> f is Υ-stable. Similarly, for all i ∈{1, · · · , m}, this connected component of<sup>�</sup> σm−1(λ;i) − �mk=1−2<sup>ckσk−1(λ;i) > 0</sup> � is contained in (q1, · · · , qi−1, qi+1, · · · , qm) + Γm−1 by ignoring the Cartesian product R term. Hence, this connected component of<sup>�</sup> σm−1(λ;i) −<sup>�m</sup> k=1<sup>−2ckσk−1(λ;i)>0�</sup> is Υ-stable and will be the unique connected component contained in the Υ1-cone of Γ<sup>m</sup> fi<sup>−1</sup> by mathematical induction. 

We now show that the Υ1-cone of Γ<sup>m</sup> f<sup>isexactly</sup> 



Then, the rest follows from mathematical induction. By the previous arguments, we know 



For any (λ1, · · · , λm) ∈ Γ<sup>m</sup> f<sup>andi∈{1, · · ·, m},wehaveσm−1(λ;i) −�m</sup> k=1<sup>−2ckσk−1(λ;i)>0.By</sup> the definition of Υ1, we obtain that Υ1 ⊆<sup>�</sup> 1≤i≤m�σm−1(λ;i) − �mk=1−2<sup>ckσk−1(λ;i)>0�.Onthe</sup> other hand, for any (λ1, · · · , λm) ∈<sup>�</sup> 1≤i≤m�σm−1(λ;i) − �mk=1−2<sup>ckσk−1(λ;i)>0�,wedefinethe</sup> following continuous section 



22 

where λ<sup>˜</sup> ∈ Γ<sup>m</sup> f<sup>.Similartobefore,wecanshowthat</sup> 

�λ1, · · · , λi−1, λi(λ1, · · · , λi−1, λi+1, · · · , λm), λi+1, · · · , λm� ∈ Γmf<sup>.</sup> This implies that (λ1, · · · , λi−1, λi+1, · · · , λm) ∈ Γ<sup>m</sup> f<sup>−1</sup> for any i ∈{1, · · · , m}. Hence, by the definition of Υ1-cone, we get (λ1, · · · , λm) ∈ Υ1. In conclusion, we obtain 



By mathematical induction and (2.26), since<sup>�</sup> σm−1(λ;i) −<sup>�m</sup> k=1<sup>−2ckσk−1(λ;i) > 0�isΥ-stable,</sup> 



Last, we show that there exists a unique connected component of {f (λ) > 0} so that the intersection with Υ1 is not empty. Let (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> m) ∈ Υ1\Γ<sup>m</sup> f<sup>and</sup> 



Similar to before, because (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> m) ∈ Υ1, we can find a piecewise linear path connecting (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> m) to (λ, · · · , λ) for some λ > 0 large. In addition, along this path, any point will satisfy f > 0. We can connect any point in Γ<sup>m</sup> f<sup>to(˜λ1, · · ·, ˜λm),thus(˜λ1, · · ·, ˜λm)willbeinthesame</sup> connected component, which is a contradiction. This finishes the proof. □ 

In the proof of Lemma 2.4, we also obtain the following result, let us list this result here. 

Lemma 2.5. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσktypemultilinearpoly-</sup> nomial and Γ<sup>n</sup> f<sup>beaconnectedcomponentof{f(λ) > 0}.IfΓ</sup> f<sup>nisΥ-stable,thenforanyλ ∈Υl,</sup> 



for l ∈{0, 1, · · · , n − 1}. Here, we write Γ<sup>n</sup> f<sup>= Υ0and</sup> Γn is the closure of Γn. As a consequence, Υl will be a connected open set for any l ∈{0, 1, · · · , n − 1} and as a set, 



In particular, for any λ ∈ �λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−2ckσk(λ) > 0</sup> � ∩ Υ1, we have λ ∈ Γ<sup>n</sup> f<sup>.</sup> Remark 2.5. By Lemma 2.4, the Υ-cones are defined by systems of inequalities of polynomials, so they are semialgebraic sets in real algebraic geometry. 

We consider the boundary of the Υ-cones, they will have the following relations. 

Lemma 2.6. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)be a general inverse σktype multilinear polyno-</sup> mial and Γ<sup>n</sup> f<sup>be a connected component of {f(λ) > 0}.If Γn</sup> f<sup>is Υ-stable and Υl̸= �cn−1, · · ·, cn−1</sup> �+ Γn for some l ∈{0, · · · , n − 2}, then either (2.27) ∂Υl ∩ ∂Υl+1 = ∅ or {(xl, · · · , xl)}. 

23 

Here xl will be the largest real value satisfies both 



Moreover, if Γ<sup>n</sup> f<sup>isstrictlyΥ-stable,then</sup> 



Proof. We use mathematical induction to prove this, for convenience, we assume cn−1 = 0. First, when n = 1, there is nothing to prove. Second, when n = 2, f (λ) = λ1λ2 − c0 with c0 ≥ 0. If c0 = 0, then Υ0 = Γ<sup>2</sup> f<sup>=Γ2andΥ1=Γ2.Ifc0>0,thenΥ0=Γ2</sup> f<sup>={λ1λ2>c0}and</sup> Υ1 = Γ2. The intersection ∂Υ0 ∩ ∂Υ1 = ∅. Suppose the statement is true when n = m − 1. Then, when n = m, we only need to prove the case that Υ0 = Γ<sup>m</sup> f̸<sup>=Γm,therestfollowsdirectlyby</sup> mathematical induction. If Υ1 = Γm, then f = λ1 · · · λm − c0 with c0 > 0 by Lemma 2.4. For this case, ∂Υ0 ∩ ∂Υ1 = ∅. We consider the case that Υ1 ⊊ Γm, for any (λ1, · · · , λm) ∈ ∂Υ0, we have 



Due to Lemma 2.4, Υ0 is contained in Υ1. This implies that 



If ∂Υ0 ∩ ∂Υ1̸ = ∅, we use the method of Lagrange multipliers to find the local extrema of �mk=0−2<sup>ckσk(λ;1)undertheconstraintλ2 · · · λm −�m</sup> k=1<sup>−2ckσk−1(λ;1) = 0.Let</sup> 



By taking the partial derivative of quantity (2.28) with respect to µ and λi, we have 



for i ∈{2, · · · , m}. At those points with ∇F = 0, we subtract equation (2.30) by (2.29) and get 



for all i ∈{2, · · · , m}. By mathematical induction, ∂Υ1 ∩ ∂Υ2 = ∅ or {(x1, · · · , x1)}. Here x1 is the largest real value satisfies both 



24 

No matter which case, there exists only one local minimum (x1, · · · , x1), where 



Since we assume ∂Υ0 ∩ ∂Υ1̸ = ∅ and by above, there exists only one critical point. It is a global minimum, ∂Υ0 ∩ ∂Υ1 = {(x1, · · · , x1)}, and x1 also satisfies 



This finishes the proof. 

□ 

Proposition 2.6. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσktypemultilinear</sup> polynomial. For any q ∈ R<sup>n</sup> , there exists at most one connected component of {f (λ)̸ = 0} which is contained in q + Γn and this connected component will be a connected component of {f (λ) > 0}. 

Proof. We use mathematical induction to prove this, for convenience, we assume cn−1 = 0. First, when n = 1, there is nothing to prove. Second, when n = 2, f (λ) = λ1λ2 − c0. If c0 < 0, then no connected component of {f (λ)̸ = 0} will be contained in q+Γ2 for any q ∈ R<sup>2</sup> . If c0 ≥ 0, there exists one connected component of {f (λ)̸ = 0} which will be contained in Γ2. This connected component is a connected component of {f (λ) > 0}. Suppose the statement is true when n = m − 1. Then, when n = m, for any connected component of {f (λ)̸ = 0} which is contained in q + Γm for some q ∈ R<sup>m</sup> . If there exists a point (λ1, · · · , λm) such that fi(λ1, · · · , λm) = 0 for some i ∈{1, · · · , m}. Then for any λ<sup>˜</sup> i ≤ λi, we always have 



This gives a contradiction. By induction and similar to previous proofs, we see that this connected component of {f (λ)̸ = 0} will be contained in ∩i∈{1,··· ,m}{fi > 0}. Here, by ignoring the Cartesian product R term, for convenience, we write {fi > 0} as the unique connected component of {fi > 0} which is contained in (q1, · · · , qi−1, qi+1, · · · , qm) + Γm−1. By the proof in Lemma 2.4, this connected component of {f (λ)̸ = 0} will be a connected component of {f > 0} and is unique by Lemma 2.5. This finishes the proof. □ 

Proposition 2.7. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσktypemultilinear</sup> polynomial and Γ<sup>n</sup> f<sup>beaconnectedcomponentof{f(λ)>0}whichisΥ-stable.</sup> Then for any l ∈{0, · · · , n − 1}, the boundary ∂Υl of the Υl-cone separates the ambient space R<sup>n</sup> into two disjoint connected components. 

Proof. For convenience, we assume that cn−1 = 0. By Lemma 2.4, we have 



For any l ∈{0, · · · , n − 1}, we consider the following two open sets Υl and R<sup>m</sup> \Υl. By Lemma 2.5, Υl is connected. Similar to the proof in Lemma 2.4, we can also show that R<sup>m</sup> \Υl is connected. For any (λ1, · · · , λn) ∈ R<sup>m</sup> \Υl, we have a straight path connecting (λ1, · · · , λm) to (λmin, λ2, · · · , λn), where λmin := min{λ1, · · · , λm}. Suppose that there exists (λ, λ<sup>˜</sup> 2, · · · , λn) on this path such that (λ, λ<sup>˜</sup> 2, · · · , λn) ∈ Υl. Then, by Lemma 2.5, we get (λ1, · · · , λn) ∈ Υl, which gives a contradiction. We can find a piecewise linear path connecting (λ1, · · · , λm) to (λmin, · · · , λmin) and for any point on this path, this point is in R<sup>m</sup> \Υl. Hence, R<sup>m</sup> \Υl is open and connected. By standard point-set topology arguments, the boundary ∂Υl separates R<sup>n</sup> into two disjoint connected components. This finishes the proof. □ 

25 

Proposition 2.8. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσktypemultilinear</sup> polynomial and Γ<sup>n</sup> f<sup>beaconnectedcomponentof{f(λ)>0}whichis(strictly)Υ-stable.Forany</sup> l ∈{1, · · · , n − 1}, suppose (µ1, · · · , µl) ∈ Γ<sup>l</sup> f<sup>.Thenforanys∈Sn,byfixingthes(k)-thentry</sup> λs(k) equals µk for all k ∈{1, · · · , l}, and treat the rest as variables. f/(µ1 · · · µl) is a degree n − l general inverse σk type multilinear polynomial and the cross section will be (strictly) Υ-stable. Proof. We use mathematical induction to prove this, for convenience, we assume cn−1 = 0. First, when n = 1, there is nothing to prove. Second, when n = 2, f (λ) = λ1λ2 − c0 with c0 ≥ 0. We obtain Γ<sup>1</sup> f<sup>=Γ1=R>0andforanyµ1∈Γ1</sup> f<sup>,wehaveµ1>0.Forconvenience,wefixλ1=µ1,</sup> then 



is a degree 1 general inverse σk type multilinear polynomial. The cross section is 



and will be Υ-stable. Suppose the statement is true when n = m − 1. Then, when n = m, it suffices to prove the statement by fixing a single entry, say µ1 ∈ Γ<sup>1</sup> f<sup>=Γ1=R>0forconvenience,</sup> the rest follows by induction. By symmetry, we fix λ1 = µ1, then we get 



By hypothesis, Γ<sup>m</sup> f<sup>isΥ-stable,sothereexistsq= (q1, · · ·, qm) ∈RmsuchthatΓm</sup> f<sup>iscontainedin</sup> q + Γm. Thus, we can also verify that this connected component of 



is contained in (q2, · · · , qm) + Γm−1 by ignoring the first entry µ1. So the cross section λ1 = µ1 is Υ-stable. For the strict Υ-stableness, the proof is similar, so this finishes the proof. □ 

We prove the following Positivstellensatz-type result and a proposition to finish this subsection. In Section 4, we compute some examples when the degree is less than or equal to four using the resultants. 

Theorem 2.3 (Positivstellensatz). Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverse</sup> σk type multilinear polynomial. There exists a connected component Γ<sup>n</sup> f<sup>of{f(λ)>0}whichis</sup> Υ-stable if and only if the diagonal restriction rf (x) of f (λ), which is defined by the following 



is right-Noetherian. Moreover, Γ<sup>n</sup> f<sup>isstrictlyΥ-stableifandonlyifrfisstrictlyright-Noetherian.</sup> Proof. For convenience, we assume cn−1 = 0. If Γ<sup>n</sup> f<sup>isΥ-stable,byLemma2.4,thenwehave</sup> Γ<sup>n</sup> f<sup>⊆Υ1⊆Υ2⊆· · · ⊆Υn−1= Γn.</sup> 

26 

For λ > 0 sufficiently large, by Lemma 2.5, we have (λ, · · · , λ) ∈ Γ<sup>n</sup> f<sup>.Bydecreasing thevalueof λ,</sup> since Γ<sup>n</sup> f<sup>iscontainedinΓn,thereexistsalargestx0≥0suchthat</sup> 



Otherwise we will get a contradiction. Similarly, there exists a largest x1 ≥ 0 such that 



If x1 > x0, then f (x1) = f (x1, · · · , x1) > 0. So, we have (x1, · · · , x1) ∈ Γ<sup>n</sup> f<sup>⊆Υ1,whichimplies</sup> that fn(x1) > 0. This contradicts fn(x1) = 0. If we inductively let xi be the largest real root of r<sup>(i)</sup> f<sup>(x)fori ∈{0, · · ·, n −1},thensimilarly weobtainthefollowingright-Noetherianness ofrf(x):</sup> 



On the other hand, for convenience, we assume that cn−1 = 0. If the diagonal restriction rf (x) = x<sup>n</sup> −<sup>�</sup> k<sup>n</sup> =0<sup>−2ck</sup> �nk�xk is right-Noetherian, then we use mathematical induction on the degree n. When n = 1, this is immediately true. When n = 2, we have rf (x) = x<sup>2</sup> − c0, c0 ≥ 0 due to the assumption that rf is right-Noetherian. For f (λ1, λ2) = λ1λ2 − c0, there exists a connected component Γ<sup>2</sup> f<sup>of{f(λ)>0}whichisΥ-stableforc0≥0.Supposethestatementistruewhen</sup> n = m − 1. When n = m, for any i ∈{1, · · · , m} we get 



This implies that rfi is still right-Noetherian. By mathematical induction, there exists a connected component Γ<sup>m</sup> fi<sup>−1</sup> of {fi > 0} which is Υ-stable for all i ∈{1, · · · , m}. As a consequence, by Lemma 2.4, Γ<sup>m</sup> fi<sup>−1</sup> is contained in Γm−1. If Γ<sup>m</sup> fi<sup>−1</sup> = Γm−1 for some i ∈{1, · · · , m}, then by Lemma 2.4, we can use mathematical induction and get 



We have c0 ≥ 0, which is guaranteed by the right-Noetherianness of rf . Let Γ<sup>m</sup> f<sup>betheconnected</sup> component of {f (λ) > 0} which is contained in Γm, then Γ<sup>m</sup> f<sup>willbeΥ-stable.</sup> 

Now, let Γ<sup>m</sup> f<sup>betheopenconnectedcomponentof{f(λ) > 0}containingtheray{(x, · · ·, x) ∈</sup> R<sup>m</sup> : x > x0}. For the case Γ<sup>m</sup> fi<sup>−1</sup> ⊊ Γm−1, suppose that Γ<sup>m</sup> f is not contained in Γ<sup>m</sup> fi<sup>forsome</sup> i ∈{1, · · · , m}. Here Γ<sup>m</sup> fi<sup>= Γm</sup> fi<sup>−1</sup> × R. By Proposition 2.7, since Γ<sup>m</sup> fi<sup>−1</sup> is Υ-stable, the boundary ∂Γ<sup>m</sup> fi<sup>−1</sup> separates R<sup>m−1</sup> into two disjoint connected components. Thus, Γ<sup>m</sup> fi<sup>separatesRmintotwo</sup> disjoint connected components. Since any connected set in R<sup>m</sup> is also path connected, there exists (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> m) ∈ Γ<sup>m</sup> f<sup>∩∂Γ</sup> f<sup>m</sup> i<sup>.Thatis,</sup> 



for some i ∈{1, · · · , m}. Say i = 1 for convenience. At this point (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> m), we get 



27 

Similar to the proof in previous Lemma 2.6, we use the method of Lagrange multipliers to find the local extrema of<sup>�m</sup> k=0<sup>−2ckσk(λ;1) under the constraint λ2 · · · λm−�m</sup> k=1<sup>−2ckσk−1(λ;1) = 0.There</sup> exists only one local extremum at (x1, · · · x1), where x1 is the largest real root of rf1 (x). Since Γ<sup>m</sup> fi<sup>−1</sup> is Υ-stable, by Lemma 2.6, we can treat λm as a function in terms of λ2, · · · , λm−1 and smooth when (λ2, · · · , λm)̸ = (x1, · · · , x1). By taking the derivative of the quantity<sup>�m</sup> k=0<sup>−2ckσk(λ;1)and</sup> the equation f1 = 0 with respect to i ∈{2, · · · , m − 1}, we get 





By combining equations (2.33) and (2.34), we get 

(2.35) 



By setting λi ≥ λm for any i ∈{2, · · · , m− 1} and since Γ<sup>m</sup> fi<sup>−1</sup> is Υ-stable, quantity (2.35) is always positive on the level set {f1 = 0}. By (2.35), for any (λ2, · · · , λm−1, λm) on {f1 = 0}, we have 

(2.36) 



Since x1 is a root of rf1 , we obtain, 



By combining inequalities (2.32), (2.36), and (2.37), we get 



Here x0 is the largest real root of rf . This gives a contradiction, in conclusion, Γ<sup>m</sup> f<sup>iscontained</sup> in Γ<sup>m</sup> fi<sup>foralli ∈{1, · · ·, m}.ThisimpliesthatΓm</sup> f<sup>isΥ-stable.Similarly,wecanshowthatΓ</sup> f<sup>nis</sup> strictly Υ-stable if and only if rf is strictly right-Noetherian. This finishes the proof. □ 

Proposition 2.9. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσktypemultilinear</sup> polynomial. If a level set of {f (λ) = 0} is contained in q + Γn for some q ∈ R<sup>n</sup> , then this level set 

28 

is unique and there exists a unique connected component of {f (λ) > 0}, which is strictly Υ-stable and the boundary will be this level set. 

Proof. We use mathematical induction to prove this, for convenience, we assume cn−1 = 0. First when n = 1, there is nothing to prove. Second, when n = 2, f (λ) = λ1λ2 − c0. If c0 ≤ 0, then no level set will be contained in q + Γ2 for any q ∈ R<sup>2</sup> . Suppose the statement is true when n = m − 1. Then, when n = m, if there exists a point (λ1, · · · , λn) on this level set {f = 0} such that fi(λ1, · · · , λn) = 0 for some i ∈{1, · · · , n}, then for λ<sup>˜</sup> i ≤ λi, we always have 



By letting λ<sup>˜</sup> i approach −∞, this gives a contradiction. By Proposition 2.6, this level set of {f = 0} will be contained in ∩i∈{1,··· ,m}{fi > 0}. Hence, this level set will be the following graph 



over {fm > 0}. We define Γ<sup>m</sup> f<sup>by</sup> 



We have Γ<sup>m</sup> f<sup>isopenandconnected.IfΓm</sup> f<sup>isnotaconnectedcomponentof{f(λ) > 0},saythere</sup> exists (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> m) ∈/ Γ<sup>m</sup> f<sup>inthisconnectedcomponent.Thenitsufficestocheckthecasethat</sup> (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> m−1) ∈{/ fm > 0}. Since connected set in R<sup>m</sup> is also path connected and by induction, there exists (λ<sup>ˆ</sup> 1, · · · , λ<sup>ˆ</sup> m) such that 



The rest follows by the proof in Theorem 2.3, we use the method of Lagrange multipliers to get a contradiction. So, Γ<sup>m</sup> f<sup>isanopenconnectedcomponentof{f(λ) > 0}whichisstrictlyΥ-stable</sup> and the boundary ∂Γ<sup>m</sup> f<sup>willbethislevelset.Similarly,aconnectedcomponentof{f(λ)>0}</sup> satisfies these properties will be unique. This finishes the proof. □ Definition 2.8 (Υ-dominance). Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)andg(λ):=λ1 · · · λn−</sup> �kn=0−1<sup>dkσk(λ) be two Υ-stable general inverse σktype multilinear polynomials.For i ∈{0, · · ·, n−</sup> 1}, we write xi the largest real root of the diagonal restriction rf<sup>(i)</sup> of f and yi the largest real root of the diagonal restriction rg<sup>(i)</sup> of g. If yi ≥ xi for all i ∈{0, · · · , n − 1}, then we say g ⋗ f . Theorem 2.4 (Υ-dominance). Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)andg(λ):=λ1 · · · λn−</sup> �kn=0−1<sup>dkσk(λ)betwoΥ-stablegeneralinverseσktypemultilinearpolynomials.Theng ⋗fifand</sup> only if Γ<sup>n</sup> g<sup>⊂Γn</sup> f<sup>.</sup> 

Proof. We use mathematical induction to prove this, for convenience, we assume dn−1 = 0. First when n = 1, the proof should be straightforward. Second, when n = 2, g(λ) = λ1λ2 − d0 and f (λ) = λ1λ2 − c1(λ1 + λ2) − c0. If g ⋗ f , then we have 



29 

This is a contradiction, since 



On the other hand, if Γ<sup>2</sup> g<sup>⊂Γ2</sup> f<sup>,then one can verify that g ⋗f.Supposethe statement is true when</sup> n = m − 1. Then, when n = m, if Γ<sup>m</sup> g<sup>⊂Γm</sup> f<sup>,by denoting the largest real root of r</sup> f<sup>(k)</sup> by xk and the largest real root of rg<sup>(k)</sup> by yk, we immediately get y0 ≥ x0. The rest follows from mathematical induction, thus g ⋗ f . On the other hand, if g ⋗ f , suppose Γ<sup>m</sup> g̸<sup>⊂Γ</sup> f<sup>m,thereexists(˜λ1, · · ·, ˜λm)</sup> such that 



In addition, under the constraint g = g(λ<sup>˜</sup> ) > 0, we consider the partial derivative of f with respect to λi for i ∈{1, · · · , m − 1}. Under the constraint g = g(λ<sup>˜</sup> ) > 0, we obtain 



So the quantity gmfim − gimfm is independent of the value of λi and λm. By Theorem 2.3 and Proposition 2.9, since rg is right-Noetherian, we have g = g(λ<sup>˜</sup> ) is contained in the Υ1-cone Υ1<sup>gof</sup> g − g(λ<sup>˜</sup> ). By fixing the values of λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> i−1, λ<sup>˜</sup> i+1, · · · , λ<sup>˜</sup> m and decreasing the value of the i-th entry, it will intersect with Υ<sup>g</sup> 1<sup>inparticular{gm=0}.Atthisintersectionpoint,thequantity</sup> gmfim − gimfm will be gmfim − gimfm = −gimfm ≤ 0. The last inequality is due to mathematical induction, gm⋗fm if and only if Γ<sup>m</sup> gm<sup>−1</sup> ⊂ Γ<sup>m</sup> fm<sup>−1.Let λm be the smallest value between {λ1, · · ·, λm},</sup> equation (2.38) will satisfy 



If we write y˜0 the largest real root of g − g(λ<sup>˜</sup> ), then we obtain 



This is a contradiction, hence we finish the proof. 

□ 

Here, we skip the proof of the following Lemma. By using mathematical induction, the proof should be straightforward. 

Lemma 2.7. Let f (λ) := λ1 · · · λn−<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ) and g(λ) := λ1 · · · λn−�</sup> k<sup>n</sup> =0<sup>−1dkσk(λ) be two Υ-</sup> stable general inverse σk type multilinear polynomials. If g⋗f , then for any (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> n) ∈{g > 0}, we have f (λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> n) ≥ g(λ<sup>˜</sup> 1, · · · , λ<sup>˜</sup> n). 

By considering the difference of two Υ-stable general inverse σk type multilinear polynomials with one Υ-dominant another, we get the following Positivstellensatz-type result. We hope we can find a nicer statement in the future, comparing an Υ-stable general inverse σk multilinear polynomial with a Sn-invariant multilinear polynomial of smaller degree. 

30 

Lemma 2.8. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)andg(λ) := λ1 · · · λn −�</sup> k<sup>n</sup> =0<sup>−1dkσk(λ)betwo</sup> Υ-stable general inverse σk type multilinear polynomials. If g ⋗ f , then 



Proof. The proof follows from Theorem 2.4 and Lemma 2.7. 

Note that similar to before, we might need to specify a connected component of {g − f > 0}. A simple application of Lemma 2.8 will be the inequality of arithmetic and geometric means. 

2.3. New Materials to Prove the Convexity Theorem. We state an algebra result in [42] that will be used when proving the convexity of the level set. We can collect all strictly Υ-stable multilinear polynomials and get the following space. 

Definition 2.9 (L. [42]). Consider the following set C<sup>˜</sup> n ⊂ R<sup>n−1</sup> , which is defined by 



Here, we let C˜n be a topological space using the subspace topology induced from the standard Euclidean topology of the Euclidean space. 

By Theorem 2.3, strictly Υ-stable general inverse σk multilinear polynomials correspond to strictly right-Noetherian polynomials. Let c ∈ C<sup>˜</sup> n, if we denote xl(c) the largest real root of the l-th derivative of x<sup>n</sup> −<sup>�</sup> k<sup>n</sup> =0<sup>−2ck</sup> �nk�xk for l ∈{0, · · · , n − 1}, then we have 



So, any c ∈ C<sup>˜</sup> n gives us an (n − 1)-tuple (xn−2(c), · · · , x1(c), x0(c)) in the following polyhedron. Definition 2.10 (L. [42]). Let X<sup>˜</sup> n be the following polyhedron in R<sup>n−1</sup> : 



Here, we let X<sup>˜</sup> n be a topological space using the subspace topology induced from the standard Euclidean topology of the Euclidean space. 

Naturally, we consider the following maps. Let ϕ : C<sup>˜</sup> n → R<sup>n−1</sup> be a map defined by 



where xl(c) is the largest real root of the l-th derivative of x<sup>n</sup> −<sup>�</sup> k<sup>n</sup> =0<sup>−2ck</sup> �nk�xk for l ∈{0, · · · , n−2}. Let ψ : X<sup>˜</sup> n → R<sup>n−1</sup> be a map defined by 



where dl for l ∈{0, 1, · · · , n − 2} is defined recursively by 



from n − 2 back to 0. 

In [42], the author showed that the spaces C<sup>˜</sup> n and X<sup>˜</sup> n are homeomorphic. Lemma 2.9 (L. [42]). The map ϕ : C<sup>˜</sup> n → X<sup>˜</sup> n is a homeomorphism with inverse ψ : X<sup>˜</sup> n → C<sup>˜</sup> n. 

31 

Remark 2.6. In fact, ϕ can be extended to a map from C˜n, the closure of C˜n, to X˜n, the closure of X<sup>˜</sup> n. Moreover, similar to the proof of Lemma 2.9, the extension is still a homeomorphism. 

The following are some new results that will also be used when proving the convexity of the level set. 

Lemma 2.10. Let c ∈ C˜n and ϕ(c) = (xn−2, · · · , x1, x0), then for l ∈{0, · · · , n − 2}, 





and equality holds if and only if xl = xl+1. 





Lemma 2.12. Let c ∈ C˜n and ϕ(c) = (xn−2, · · · , x1, x0). For any µ > ν > 0, we have x˜l(ν) ≥ x˜l(µ) for any l ∈{0, · · · , n − 2} and equality happens only if xl = xl+1. In particular, if c ∈ C<sup>˜</sup> n, then x˜0(ν) > x˜0(µ). 

Proof. For any l ∈{0, · · · , n − 2}, x˜l(µ) satisfies 



32 

The last inequality is due to Lemma 2.11, we obtain x˜l(µ) ≥ xl+1 and xl+1 is the largest real root ifof cx<sup>n</sup> ∈<sup>−l</sup> C<sup>−</sup> ˜n<sup>1</sup> ,−then<sup>�</sup> k<sup>n</sup> =<sup>−</sup> xl<sup>2</sup> +10 ><sup>ck</sup> x�nk1−−. ll−−By11�xLemmak−l−1. Notice2.11, wethathavex˜l(µx˜)0(=µ)x>l+1x1onlywhichif xlimplies= xl+1that. In xparticular,˜0<sup>n−1</sup> (µ) − �kn=1−2<sup>ck</sup> �nk−−11�x˜0k−1(µ) > 0 and x˜0(ν) > x˜0(µ). This finishes the proof. □ 

3. Convexity of General Inverse σk Equations 

In this section, let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσktypemultilinear</sup> polynomial. If {f (λ) = 0} is contained in q + Γn for some q ∈ R<sup>n</sup> , then we use a classical way to prove the convexity of this level set {f (λ) = 0}. 

By doing the substitution (2.21), we may assume cn−1 = 0 and consider the following general inverse σk equation 



There are two ways to compute the convexity, first, if we write 

(3.1) 

then we have the following. 



then the level set {h = c} is convex. Here, hi := ∂h/∂λi and hij := ∂<sup>2</sup> h/∂λi∂λj. 

Proof. Let V = (V1, · · · , Vn) ∈ Tλ�h = c� be a tangent vector, which gives, �i<sup>hiVi=0.Then,</sup> to get convexity, which is equivalent to the following quantity (3.3) � hijViV¯j 



is non-negative. Since V is a tangent vector, we can write Vn = −<sup>�</sup> i<sup>n</sup> =1<sup>−1hiVi/hn.Bypluggingin</sup> quantity (3.3), we obtain 



then the quantity (3.4) is non-negative. This implies that the level set {h = c} is convex. If we write 

□ 



33 

then the Hessian of λn is related to n − 1 × n − 1 Hermitian matrix (3.3) as follows. 



where we denote by hi := ∂h/∂λi and hij := ∂<sup>2</sup> h/∂λi∂λj. Moreover, we have 



Here, we denote 



Proof. First, we have the following 

This implies that 



where we denote C0;i,j =<sup>�</sup> k<sup>n</sup> =0<sup>−2ckσk(λ;i,j).By(3.8),weobtain</sup> (3.9) C0;i,j = C0;i + C0;j − C + λiλj C2;i,j. For i = j, on h =<sup>�</sup> k<sup>n</sup> =0<sup>−2ckσk(λ)/σn(λ),wehave</sup> 



34 



35 

Here, for convenience, we denote 



This finishes the proof. 

36 

Theorem 3.1 (Convexity of the general inverse σk equation). Let f (λ) := λ1 · · · λn−<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)</sup> be a general inverse σk type multilinear polynomial. If the diagonal restriction rf (x) = x<sup>n</sup> − �kn=0−1<sup>ck</sup> �nk�x<sup>k</sup> is strictly right-Noetherian, then {f = 0} is strictly convex. 

Proof. We assume cn−1 = 0 for convenience. We prove the statement by mathematical induction on the degree n. When n = 2, f (λ) = λ1λ2 − c0 with c0 > 0. Let (µ1, µ2), (ν1, ν2) ∈{f ≥ 0}. That is, f (µ1, µ2) = µ1µ2 − c0 ≥ 0 and f (ν1, ν2) = ν1ν2 − c0 ≥ 0. For any t ∈ (0, 1), we have 



and equality holds when (µ1, µ2) = (ν1, ν2) and µ1µ2 = c0 = ν1ν2. Hence, the set {f (λ) = λ1λ2 − c0 ≥ 0} is strictly convex. 

Suppose the statement is true when n = m − 1. When n = m ≥ 3, let µ = (µ1, · · · , µm), ν = (ν1, · · · , νm) ∈{f ≥ 0}. If µi = νi for some i ∈{1, · · · , m}, then by fixing the i-th position and Proposition 2.8, we may view f (•, µi, •) as a degree m − 1 strictly Υ-stable general inverse σk equation. By mathematical induction, for any t ∈ (0, 1), we have f ((1 − t)µ + tν) > 0. So, we only need to consider the case that µi̸ = νi for all i ∈{1, · · · , m}. In addition, it suffices to show that {f ≥ 0} is convex. We show that if {f ≥ 0} is convex, then {f ≥ 0} is indeed strictly convex. If {f ≥ 0} is convex, let µ, ν ∈{f ≥ 0} with µi̸ = νi for all i ∈{1, · · · , m}. We can view f ((1−t)µ+tν) as a degree m polynomial in terms of t, so there are finitely many roots by the fundamental theorem of algebra. Suppose that there exists t<sup>˜</sup> ∈ (0, 1) such that f ((1 − t<sup>˜</sup> )µ + tν<sup>˜</sup> ) = 0. Let µ˜ and ν˜ denote the (m − 1)-tuples (µ2, · · · , µm) and (ν2, · · · , νm), respectively. Since f ((1 − t)µ + tν) only has finitely many roots, there exists 0 < t0 < t<sup>˜</sup> and 1 > t1 > t<sup>˜</sup> such that f ((1 − t0)µ + t0ν) > 0 and f ((1−t1)µ+t1ν) > 0. For ǫ > 0 sufficiently small, we get f ((1−t0)µ1 +t0ν1 −ǫ, (1−t0)˜µ+t0ν˜) > 0 and f ((1 − t<sup>˜</sup> )µ1 + tν<sup>˜</sup> 1 − t<sup>t</sup> 1<sup>1</sup> −<sup>−</sup> t<sup>t˜</sup> 0<sup>ǫ, (1 −t˜)˜µ + ˜tν˜) < 0,whichisacontradictionif{f≥0}isconvex.</sup> 

LetMoreover,c ∈ C˜m itnotsufficesin thetogenericshow thatstrata{fand(λ) ≥suppose0} is convex{f (λ) =if cλ1∈ · · ·C λ˜mmis−in<sup>�</sup> the<sup>m</sup> k=0<sup>−2</sup> generic<sup>ckσk(λ)</sup> strata.<sup>≥0}</sup> is not convex. If there exists µ, ν ∈{f (λ) = λ1 · · · λm −<sup>�m</sup> k=0<sup>−2ckσk(λ)≥0}andt˜∈(0, 1)</sup> such that f ((1 − t<sup>˜</sup> )µ + tν<sup>˜</sup> ) < 0. By choosing ǫ > 0 sufficiently small, we get f (µ1 + ǫ, ˜µ) > 0, f (ν1 + ǫ, ˜ν) > 0, and f ((1 − t<sup>˜</sup> )µ1 + tν<sup>˜</sup> 1 + ǫ, (1 − t<sup>˜</sup> )˜µ + t<sup>˜</sup> ν˜) < 0. We claim that there exists c˜ ∈ C<sup>˜</sup> m in the generic strata with {λ1 · · · λm −<sup>�m</sup> k=0<sup>−2c˜kσk(λ)≥0}⊂{λ1 · · · λm−�m</sup> k=0<sup>−2ckσk(λ)≥</sup> 0{}λ1such · · · λmthat−<sup>�</sup> (µ<sup>m</sup> k1=0<sup>−</sup> +<sup>2</sup> ǫ,<sup>c˜k</sup> ˜<sup>σ</sup> µ<sup>k</sup> )<sup>(</sup> , (<sup>λ</sup> ν<sup>)</sup> 1<sup>≥</sup> +<sup>0</sup> ǫ,<sup>}</sup> ˜ν<sup>is</sup> ) ∈{<sup>convex</sup> λ1 · · ·<sup>when</sup> λm −<sup>c˜�∈m</sup> kC=0<sup>−</sup> ˜m<sup>2c˜</sup> is<sup>kσ</sup> in<sup>k(λ</sup> the<sup>)≥</sup> generic<sup>0}.If</sup> strata,<sup>claim1</sup> then<sup>holds</sup> we<sup>and</sup> get ((1−t<sup>˜</sup> )µ1 +tν<sup>˜</sup> 1 +ǫ, (1−t<sup>˜</sup> )˜µ+t<sup>˜</sup> ν˜) ∈{λ1 · · · λm −<sup>�m</sup> k=0<sup>−2c˜kσk(λ) ≥0} ⊂{λ1 · · · λm−�m</sup> k=0<sup>−2ckσk(λ) ≥</sup> 0}, which leads to a contradiction. 

To justify claim 1, for any µ ∈{f (λ) = λ1 · · · λm −<sup>�m</sup> k=0<sup>−2ckσk(λ)>0},weconsiderthe</sup> following continuous function, which is the composition of two continuous functions: 



Here, ψ : X<sup>˜</sup> m → C˜m is the map in Lemma 2.9. Let xl(c) be the largest real root of the l-th derivative of x<sup>m</sup> −<sup>�m</sup> k=0<sup>−2ck</sup> �mk �xk for l ∈{0, · · · , m − 2}. Since µ ◦ ψ(xm−2(c), · · · , x1(c), x0(c)) = 

37 

µ1 · · · µm −<sup>�m</sup> k=0<sup>−2ckσk(µ)>0,bythecontinuityofthefunctionµ◦ψ,thereexistsNµ>0</sup> sufficiently large such that for any N ≥ Nµ, we have 



Here, x0(c) + N<sup>1>x1(c) +</sup> 21N<sup>>· · ·>xm−2(c) +</sup> (m−11)N<sup>,soitisthegenericstrata.Bypicking</sup> N ≥ max{N(µ1+ǫ,µ˜), N(ν1+ǫ,ν˜)} and by the Υ-dominance Theorem, we get 



Now, to prove {f ≥ 0} is convex when c ∈ C<sup>˜</sup> m is in the generic strata, by the intermediate value theorem, it suffices to consider µ, ν ∈ ∂{f ≥ 0} and show that (1 − t)µ + tν ∈{f ≥ 0} for any t ∈ (0, 1). First, for convenience, we assume µ1 > ν1. By fixing µ1, we may view µ˜ = (µ2, · · · , µm) is on the level set of the following degree m − 1 strictly Υ-stable general inverse σk equation: 

(3.15) 



Similarly, we view ν˜ = (ν2, · · · , νm) is on the level set of the following degree m−1 strictly Υ-stable general inverse σk equation: 





Let x˜l(µ1) be the largest real root of the l-th derivative of the diagonal restriction µ1(x<sup>m−1</sup> − �mk=1−2<sup>ck</sup> �mk−−11�x<sup>k−1</sup> ) −<sup>�m</sup> k=0<sup>−2ck</sup> �mk−1�x<sup>k</sup> of quantity (3.15) for l ∈{0, · · · , m − 2}. Similarly, let x˜l(ν1) be the largest real root of the l-th derivative of the diagonal restriction ν1(x<sup>m−1</sup> − �mk=1−2<sup>ck</sup> �mk−−11�xk−1)−�mk=0−2<sup>ck</sup> �mk−1�xk of quantity (3.16) for l ∈{0, · · · , m−2}. Since µ1 > ν1, by Lemma 2.12, we have x˜l(µ1) < x˜l(ν1) for all l ∈{0, 1, · · · , m − 2}. By the Υ-dominance Theorem, we have the following set inclusion relation: 



We show that for any µ˜ ∈{f (µ1, •) = 0}, ν˜ ∈{f (ν1, •) = 0}, s ∈ (0, 1), and let τ1 := (1−s)µ1+sν1, there exists a unique s˜ = s˜(s, ˜µ, ˜ν) ∈ (0, 1) such that f (τ1, (1 − s˜)˜µ + ˜sν˜) = 0. We have 



38 

and 



These imply that ν˜ ∈{f (τ1, •) > 0} and µ˜ ∈{/ f (τ1, •) ≥ 0}. By the intermediate value theorem, there exists s˜ ∈ (0, 1) such that f (τ1, (1 − s˜)˜µ + ˜sν˜) = 0. The uniqueness of s˜ is ensured because the set {f (τ1, •) ≥ 0} is strictly convex, which is obtained by mathematical induction. 

We claim that s˜ = s˜(s, ˜µ, ˜ν) ≤ s for any µ˜ ∈{f (µ1, •) = 0}, ν˜ ∈{f (ν1, •) = 0}, and s ∈ (0, 1). By the strict convexity of the set {f (τ1, •) ≥ 0}, for any t ∈ [˜s, 1], we have f (τ1, (1 − t)˜µ + tν˜) ≥ 0. So, if claim 2 holds, then f (τ1, (1 − s)˜µ + sν˜) = f ((1 − s)µ + sν) ≥ 0. This implies that {f ≥ 0} is convex. Hence, we finish the proof if claim 2 holds. 

First, to justify claim 2, we fix µ1 and treat µm as a function with variables {µ2, · · · , µm−1}. Similarly, we fix ν1 and treat νm as a function with variables {ν2, · · · , νm−1}. For j ∈{2, · · · , m−1}, we have 



Moreover, if we let τi = (1 − s˜)µi + sν˜ i for any i ∈{2, · · · , m} and denote the (m − 1)-tuple (τ2, · · · , τm) by τ˜. For any i, j ∈{2, · · · , m − 1}, we have 



Second, on {f (τ1, •) = 0}, by taking the partial derivative of f (τ1, •) = 0 with respect to µj and νj for j ∈{2, · · · , m − 1}, by above, we obtain 



Since {f (τ1, •) ≥ 0} is convex, by the supporting hyperplane theorem, we have<sup>�m</sup> k=2<sup>fk(τ)(νk−</sup> µk) ≥ 0. Moreover, ν˜ ∈{f (τ1, •) > 0}, so ν˜ cannot be on the tangent plane to {f (τ1, •) = 0} at the point τ˜ := (τ2, · · · , τm). Thus, we have<sup>�m</sup> k=2<sup>fk(τ)(νk−µk)>0.Bytheimplicitfunction</sup> theorem, ∂µ∂s˜j<sup>and</sup> ∂ν∂s˜j<sup>existforallj∈{2, · · ·, m −1}.Atthelocalextremaofs˜,wehave</sup> ∂µ∂s˜j<sup>= 0</sup> and ∂ν∂s˜j<sup>= 0forallj∈{2, · · ·, m −1}.Theseimplythatatthelocalextremaofs˜,wehave</sup> 



So, at any local extremum of s˜, for any j ∈{2, · · · , m − 1}, by (3.17), we have 



39 

If ξj = 1 for all j ∈{2, · · · , m − 1}, then µ2 = · · · = µm = x˜0(µ1), τ2 = · · · = τm = x˜0(τ1), and ν2 = · · · = νm = x˜0(ν1). Here, we denote x˜0(τ1) the largest real root of τ1(x<sup>m−1</sup> − �mk=1−2<sup>ck</sup> �mk−−11�x<sup>k−1</sup> ) −<sup>�m</sup> k=0<sup>−2ck</sup> �mk−1�x<sup>k</sup> . We consider the diagonal restriction rf (x) := x<sup>m</sup> − �mk=0−2<sup>ck</sup> �mk �x<sup>k</sup> of f (λ), then rf (x) is strictly right-Noetherian because c ∈ C<sup>˜</sup> m. We show that the following rational function is convex on {x > x1}: 





Consider the second derivative of rational function (3.18) with respect to x, we get 



rf (x)rf<sup>′′(x)</sup> Here, αf (x) := (rf<sup>′(x))2</sup> is the log-concavity ratio and the last inequality is due to Theorem 2.1. So, rational function (3.18) is convex on {x > x1}. In addition, by Lemma 2.11 and Lemma 2.12, we have x˜0(ν1) > x˜0(τ1) > x˜0(µ1) > x1. Thus, by the convexity of rational function (3.18), we obtain 



By simplifying inequality (3.19), we get 



This implies that (1 − s)˜x0(µ1) + sx˜0(ν1) > x˜0(τ1) and ((1 − s)˜x0(µ) + sx˜0(ν), · · · , (1 − s)˜x0(µ) + sx˜0(ν)) ∈{f (τ1, •) ≥ 0} = {f ((1 − s)µ1 + sν1, •) ≥ 0}. 

If ξj̸ = 1 for some j ∈{2, · · · , m − 1}, for convenience, we say ξm−1 ∈ (0, 1). We consider the following set {fm−1 − ξm−1fm ≥ 0} and we show that {fm−1 − ξm−1fm ≥ 0} is convex. We have 



40 

On the level set {fm−1 − ξm−1fm = 0}, by combining equations (3.20) and (3.21), we get 



So, the level set {fm−1 − ξm−1fm = 0} is actually a graph with domain Rλm−1 × {fm−1m > 0}. Since c ∈ C<sup>˜</sup> m is in the generic strata and by mathematical induction, we have 



Thus, the following m − 1 × m − 1 matrix is also positive semi-definite: 

Hence, the graph {fm−1 − ξm−1fm = 0} is convex. 

Let µ, ν ∈{fm−1 − ξm−1fm ≥ 0}. We can view (fm−1 − ξm−1fm)((1 − t)µ + tν) as a polynomial in terms of t. If it is not a zero polynomial, then there are finitely many roots by the fundamental theorem of algebra. Suppose that there exists t<sup>˜</sup> ∈ (0, 1) such that (fm−1 − ξm−1fm)((1 − t<sup>˜</sup> )µ+ tν<sup>˜</sup> ) = 0. Since (fm−1 − ξm−1fm)((1 − t)µ + tν) only has finitely many roots, there exists t0 < t<sup>˜</sup> and t1 > t<sup>˜</sup> such that (fm−1 − ξm−1fm)((1 − t0)µ + t0ν) > 0 and (fm−1 − ξm−1fm)((1 − t1)µ + t1ν) > 0. For ǫ > 0 sufficiently small, we get (fm−1 − ξm−1fm)((1 − t0)µ1 + t0ν1, · · · , (1 − t0)µm−1 + t0νm−1, (1 − t0)µm + t0νm − ǫ) > 0 and (fm−1 − ξm−1fm)((1 −<sup>˜</sup> t)µ1 + tν<sup>˜</sup> 1, · · · , (1 −<sup>˜</sup> t)µm−1 +<sup>˜</sup> tνm−1, (1 −<sup>˜</sup> t)µm + tν˜ m − t<sup>t</sup> 1<sup>1</sup> −<sup>−</sup> t<sup>t˜</sup> 0<sup>ǫ) < 0.Thisleadstoacontradictionbecause{fm−1 −ξm−1fm≥0}isconvex.</sup> 

If (fm−1 − ξm−1fm)((1 − t)µ + tν) is a zero polynomial, then the line {(1 − t)µ + tν): t ∈ R} lies in {fm−1 − ξm−1fm = 0}. In particular, the line {(1 − t)µ1 + tν1, · · · , (1 − t)µm−2 + tνm−2): t ∈ R} lies in {fm−1 m > 0}, which implies that µi = νi for all i ∈{1, · · · , m − 2}. Hence, the line {((1 − t)µm−1 + tνm−1, (1 − t)µm + tνm): t ∈ R} is actually the line 



In conclusion, if (fm−1 − ξm−1fm)((1 − t)µ + tν) is a zero polynomial, then µi = νi for all i ∈ {1, · · · , m − 2} and (νm − µm) − ξm−1(νm−1 − µm−1) = 0. 

At this local extremum, we have τ˜ = (1 − s˜)˜µ + s˜ν˜. Since {fm−1 − ξm−1fm ≥ 0} is convex, µ, ν ∈ ∂{fm−1 − ξm−1fm ≥ 0} with µi̸ = νi for all i ∈{1, · · · , m}, and by above argument, we get (1 − s˜)µ + ˜sν ∈{fm−1 − ξm−1fm > 0}. Similar to before, we have {fm−1 − ξm−1fm ≥ 0} ⊂ {f1m−1 − ξm−1f1m > 0} and by the fact that (τ1, (1 − s˜)˜µ + ˜sν˜) = ((1 − s)µ1 + sν1, (1 − s˜)˜µ + ˜sν˜) ∈ ∂{fm−1 − ξm−1fm ≥ 0}. Hence, (1 − s˜)µ1 + ˜sν1 > (1 − s)µ1 + sν1, which implies that s > s˜. Thus, we confirm claim 2 for all local extrema. 

Last, we study the asymptotic behavior, we show that if (1 − s)µj + sνj is sufficiently large for some j ∈{2, · · · , n}, then (1 − s)˜µ + sν˜ ∈{f (τ1, •) ≥ 0} = {f ((1 − s)µ1 + sν1, •) ≥ 0}. We use mathematical induction on the degree n to prove this. When n = 2, we consider f (λ) = λ1λ2 − c0 with c0 > 0. By fixing µ1 > ν1 and let τ1 = (1 − s)µ1 + sν1, we have 



ofWhenC˜3. nBy = 3,fixingwe considerµ1 > ν1fand(λ) =let λ1τλ12λ=3 −(1 −c1(λs)1µ +1 λ+2 sν + λ1,3we) − considerc0 with (c(1µ, c2, µ0)3in) ∈{thefgeneric(µ1, •) strata= 0}, 

41 

(ν2, ν3) ∈{f (ν1, •) = 0}, and ((1 − s)µ2 + sν2, (1 − s)µ3 + sν3). By picking N1 > 0 sufficiently large such that if (1 − s)µ2 + sν2 ≥ N1 and (1 − s)µ3 + sν3 ≥ N1, then 



Hence, ((1−s)µ2 +sν2, (1−s)µ3+sν3) ∈{f (τ1, •) = f ((1−s)µ1+sν1, •) ≥ 0} in this case. Without loss of generality, we consider the case that (1 − s)µ2 + sν2 ≥ N2 > N1 and (1 − s)µ3 + sν3 is bounded above by N1, where N2 will be determined later. In this case, by the fact that ν3 > c1/ν1, µ3 > c1/µ1, (1 − s)/µ1 + s/ν1 − 1/τ1 > ǫs,µ1,ν1 > 0, and c1 > 0, we get 



provided that N2 is sufficiently large. Hence, if (1 − s)µj + sνj ≥ N2 for some j ∈{2, 3}, then ((1 − s)µ2 + sν2, (1 − s)µ3 + sν3) ∈{f (τ1, •) = f ((1 − s)µ1 + sν1, •) ≥ 0} in this case. 

Suppose the statement is true when n = m − 1 ≥ 3. When n = m ≥ 4, we consider the point (1−s)˜µ+sν˜. Similar to the above, we can pick N1 > 0 sufficiently large such that if (1−s)µj +sνj ≥ N1 for all j ∈{2, · · · , m}, then (1 − s)˜µ + sν˜ ∈{f (τ1, •) ≥ 0}. Here, we iteratively show that for k from 2 to m − 1, there exists Nk > Nk−1 sufficiently large such that if (1 − s)µj + sνj ≥ Nk for all j ∈{2, · · · , m − k + 1} and Nk−1 ≥ (1 − s)µj + sνj for all j ∈{m − k + 2, · · · , m}, then (1 − s)˜µ + sν˜ ∈{f (τ1, •) ≥ 0}. When k = 2, by the previous argument, we consider the leading Sinceterm ofwef (assumeτ1, (1 −thats)˜µ +c s=ν˜),(cthatm−2,is, · · ·f, c2···1m, c−01)(τ∈1, (1C˜m −iss)˜inµ +the sν˜)generic= τ1((1strata, − s)µmso+c sνm−m2 )> − 0cmand−2. f2···m−1(λ) = λ1λm − cm−1 is strictly Υ-stable. Similar to above, there exists ǫs,µ1,ν1 > 0 such that 



Hence, f2···m−1(τ1, (1 − s)˜µ+ sν˜) = τ1((1 − s)µm + sνm)− cm−2 has a uniform positive lower bound. This implies that there exists N2 > N1 sufficiently large such that if (1 − s)µj + sνj ≥ N2 for all j ∈{2, · · · , m − 1} and N1 ≥ (1 − s)µm + sνm, then (1 − s)˜µ + sν˜ ∈{f (τ1, •) ≥ 0}. 

Suppose that when k = l − 1 ≥ 2, the leading term f2···m−l+2(τ1, (1 − s)˜µ + sν˜) has a uniform positive lower bound. When k = l, we consider the leading term f2···m−l+1(τ1, (1 − s)˜µ + sν˜). Since c ∈ C<sup>˜</sup> m is in the generic strata, by mathematical induction, the set {f2···m−l+1(λ) ≥ 0} is strictly convex. We consider the cross sections when λ1 = µ1 and λ1 = ν1, that is, {f2···m−l+1(µ1, •) ≥ 0} and {f2···m−l+1(ν1, •) ≥ 0}. For any 



and 



because the set {f2···m−l+1(λ) ≥ 0} is strictly convex, we get 



42 



<!-- Start of picture text -->
λ3<br>1 − s˜<br>ν1 = 0.8<br>s˜<br>s = 1/2<br>µ1 = 3<br>λ2<br><!-- End of picture text -->

Figure 3. λ1λ2λ3 − 4(λ1 + λ2 + λ3) + 9 = 0 with ν1 = 0.8, τ1 = 1.9, and µ1 = 3. 

In addition, since {f2···m−l+1(µ1, •) ≥ 0} ∩ [cm−2/µ1, Nl−1/(1 − s)]<sup>l−1</sup> and {f2···m−l+1(ν1, •) ≥ 0} ∩ [cm−2/ν1, Nl−1/s]<sup>l−1</sup> are both compact subsets, we obtain 



This implies that the leading term f2···m−l+1(τ1, (1 − s)µm−l+2 + sνm−l+2, · · · , (1 − s)µm + sνm) has a uniform positive lower bound. By letting Nl > Nl−1 sufficiently large, for (1−s)µj +sνj ≥ Nl for all j ∈{2, · · · , m − l + 1} and Nl−1 ≥ (1 − s)µj + sνj for all j ∈{m − l + 2, · · · , m}, we have f ((1−s)µ+sν) > 0. Hence, (1−s)˜µ+sν˜ ∈{f ((1−s)µ1+sν1, •) ≥ 0} provided that Nl is sufficiently large. By doing this process iteratively, if (1 − s)µj + sνj ≥ Nm−1 for some j ∈{2, · · · , m}, then (1 − s)˜µ + sν˜ ∈{f ((1 − s)µ1 + sν1, •) ≥ 0}, which finishes the proof. □ 

Remark 3.1. In Figure 3, we plot the level set λ1λ2λ3 − 4(λ1 + λ2 + λ3) + 9 = 0 with ν1 = 0.8, τ1 = 1.9, and µ1 = 3. τ1 = 1.9 when s = 1/2. The ratio s˜ : 1 − s˜ is the ratio of the distance dist((µ2, µ3), (τ2, τ3)) to the distance dist((τ2, τ3), (ν2, ν3)). 

We prove the following Lemma to end this section, which shows that Theorem 2.1 is equivalent to the positive definiteness of the Hessian matrix of λn on the curve {λ1 = · · · = λn−1} on {f = 0}. The author believes that the following result gives a promising hope that Conjecture 1.1 is true. Lemma 3.3. Let f (λ) := λ1 · · · λn −<sup>�</sup> k<sup>n</sup> =0<sup>−1ckσk(λ)beageneralinverseσktypemultilinear</sup> polynomial. If the diagonal restriction rf (x) of f is strictly right-Noetherian, then on the curve {λ1 = · · · = λn−1} of the level set {f = 0} with λ1 > x1, the positive definiteness of the following n − 1 × n − 1 Hessian matrix 



is equivalent to the monotonicity of log-concavity ratio of rf (x) = x<sup>n</sup> −<sup>�</sup> k<sup>n</sup> =0<sup>−1</sup> the largest real root of rf<sup>′.</sup> 



Proof. For convenience, we assume that cn−1 = 0. By Lemma 3.2, we show that the following matrix is positive-definite at every point on the curve {λ1 = · · · = λn−1 = x} with x > x1: 



43 

By Lemma 3.2, we have 



Now, it suffices to show that the following n − 1 × n − 1 matrix is positive semi-definite (3.22) C˜ := 2(x<sup>n−2</sup> λn − C1;1)(x<sup>n−2</sup> − C2;1,n) `1` n−1×n−1 

where `1` n−1×n−1 is the n − 1 × n − 1 all-ones matrix and we have 

By change of basis, to show C<sup>˜</sup> is positive-definite, it is equivalent to showing that the following matrix is positive-definite 



where 



The column vectors of matrix O are in fact the eigenvectors of `1` n−1×n−1, which makes the new matrix O<sup>∗</sup> CO<sup>˜</sup> and the computations simpler. We have 



44 



The n − 2 × n − 2 matrix 

is a positive-definite matrix with eigenvalues {1, · · · , 1, n − 1}. So to prove whether O<sup>∗</sup> CO<sup>˜</sup> is positive-definite, it is equivalent to showing whether the following quantity is positive. (3.24) 2(n − 1)(x<sup>n−2</sup> λn − C1;1)(x<sup>n−2</sup> − C2;1,n) − (n − 2)(x<sup>n−1</sup> − C1;n)(x<sup>n−3</sup> λn − C2;1,2). Now, we use the equation itself, that is, 

(3.25) 



Then by (3.24) and (3.25), we obtain the following 

(3.26) 2(n − 1)(x<sup>n−2</sup> λn − C1;1)(x<sup>n−2</sup> − C2;1,n) − (n − 2)(x<sup>n−1</sup> − C1;n)(x<sup>n−3</sup> λn − C2;1,2) 



45 





So, we can rewrite equation (3.26) as 



Here, for notational convention, we denote αrf (x) as αf (x). In conclusion, we have shown that on the curve {λ1 = · · · = λn−1}, the positive definiteness of the Hessian matrix of λn is equivalent to the monotonicity of log-concavity ratio αf . □ 

46 

# 4. Some Applications 

In this section, we use our convexity Theorem to verify some examples. First, when the degree is low, the Positivstellensatz Theorem can be verified using the resultants and the discriminant. Here, we give a different proof of the Positivstellensatz results in [41]. 

Definition 4.1 (Resultant). The resultant of two univariate polynomials p1(x) and p2(x) is defined as the determinant of their Sylvester matrix. To be more precise, if we write 



then the resultant of p1 and p2 is defined by the following. 



Definition 4.2 (Discriminant). Let p(x) = anx<sup>n</sup> + an−1x<sup>n−1</sup> + · · · + a1x + a0 be a polynomial of degree n and the coefficient a0, · · · , an are real numbers. The discriminant of p is defined by 

(4.2) 



Proposition 4.1. The level set of the following general inverse σk equations are all convex. 



where c0 > 0; 









Proof. Here, we only prove the degree four case: 



First, the diagonal restriction and its derivatives (after dividing by the leading coefficient) will be 

{x<sup>4</sup> − 6c2x<sup>2</sup> − 4c1x − c0, x<sup>3</sup> − 3c2x − c1, x<sup>2</sup> − c2, x}. 

47 

Second, for the largest real roots, if we denote the largest real root of k-th derivative by xk, then we have x2 =<sup>√</sup> c2, x3 = 0. Then, for the depressed cubic polynomial x<sup>3</sup> − 3c2x − c1, we want 



That is, c1 ≥−2c<sup>3</sup> 2<sup>/2</sup> . We compute the discriminant of the cubic polynomial x<sup>3</sup> − 3c2x − c1, by (4.1) and (4.2), we have 



When 4c<sup>3</sup> 2<sup>−c2</sup> 1<sup>≥0,thenthisisthecasecasusirreducibilis.When4c3</sup> 2<sup>−c2</sup> 1<sup>≤0,thentherootcan</sup> be represented using hyperbolic functions. So the largest real root x1 will be 



Here, we take the branch arccos(•) ∈ [0, π] and arccosh is the inverse hyperbolic cosine. Last, we plug x1 in to the quartic polynomial x<sup>4</sup> − 6c2x<sup>2</sup> − 4c1x − c0. Because we want x0 > x1, so we want the following to be true. 





In [28], Guan–Zhang studied the solvability of a general class of curvature equations. These curvature equations can be viewed as generalizations of the equations for Christoffel–Minkowski problem in convex geometry. Guan–Zhang considered the following class of equations 



where n is the dimension of the space, n ≥ m ≥ 2, ck ≥ 0 for k ∈{0, · · · , m − 2}, and cm−1 ∈ R. They obtained a priori estimates for the admissible solutions. Here, for the special case m = n, without assuming the admissible condition, we can show that the level set is convex. The following result can also be applied to the general inverse σk equations with non-negative coefficients considered by Collins–Sz´ekelyhidi [16] and Fang–Lai–Ma [24]. 

Lemma 4.1. The level set of the following general inverse σk equation 



is convex if ck ≥ 0 for k ∈{0, · · · , n − 2} with<sup>�</sup> k<sup>n</sup> =0<sup>−2ck> 0andcn−1∈R.</sup> 

48 

Proof. Consider the following diagonal restriction rf (x) of equation (4.4), that is, 



By Theorem 3.1, if rf is strictly right-Noetherian, then we are done. We prove this by mathematical induction on the degree n. We also claim that when n ≥ 2, if the coefficients ck satisfy the hypothesis, then x0 > 0. When n = 1, we have rf (x) = x + c0, which is strictly right-Noetherian. When n = 2, we have rf (x) = x<sup>2</sup> + 2c1x − c0; rf<sup>′(x) = 2x + 2c1.Ifwewritex1= −c1thelargest</sup> real root of rf<sup>′,thenbythehypothesis�</sup> k<sup>2−</sup> =0<sup>2ck= c0> 0,weget</sup> 



This implies that rf is strictly right-Noetherian. Moreover, we have rf (0) = −c0 < 0, which implies that x0 > 0. So the claim is true when n = 2. When n = 3, we obtain 



We have x2 = −c2. If c1 > 0, then x1 > max{x2, 0}. In addition, we obtain 



Thus, the largest real root x0 of rf is greater than x1, rf is strictly right-Noetherian. If c1 = 0, then x1 = max{0, −2c2}. If c2 < 0, then similar to above, we get rf (x1) < 0. This implies that x0 > x1, rf is strictly right-Noetherian. Otherwise, if c2 ≥ 0, then x1 = 0. For this case, by the hypothesis, we have<sup>�3</sup> k<sup>−</sup> =0<sup>2ck= c0 + c1= c0> 0.Thisimpliesthat</sup> 



Thus, x0 > x1 = 0, rf is again strictly right-Noetherian. No matter which case, the claim is true. Suppose the statement and the claim is true when n = m − 1. When n = m, by equation (4.5), we have 



If we consider the first derivative of rf (x) with respect to x, then we obtain 



There are two cases to be considered. First, if<sup>�m</sup> k=1<sup>−2ck>0,thenr</sup> f<sup>′satisfiesthehypothesis,so</sup> rf<sup>′isstrictlyright-Noetherian.Moreover,thelargestrealrootx1ofr</sup> f<sup>′willbepositive.Also,</sup> 



49 

In this case, x0 > x1 > 0, rf is strictly right-Noetherian. Second, if<sup>�m</sup> k=1<sup>−2ck= 0,thenck= 0for</sup> all k ∈{1, · · · , m − 2}. By hypothesis, we have c0 > 0, so rf (x) = x<sup>m</sup> + mcm−1x<sup>m−1</sup> − c0. For k ∈{1, · · · , m − 1}, we have xk = max{0, −(m − k)cm−1}. We are done if cm−1 < 0. Otherwise, we have x1 = · · · = xm−1 = 0 and x0 > x1 = 0. Hence, no matter which case, rf is strictly right-Noetherian, and the claim is true. This finishes the proof. □ 

Lemma 4.2. The level set of the deformed Hermitian–Yang–Mills equation 

(4.6) ℑ<sup>�</sup> ω + √−1χ<sup>�n</sup> = tan<sup>�</sup> θ<sup>�</sup> · ℜ<sup>�</sup> ω + √−1χ<sup>�n</sup> is convex if θ is in the supercritical phase, that is, θ ∈ �(n − 2)π/2, nπ/2�. In addition, the level set is also convex if θ ∈ �−nπ/2, −(n − 2)π/2�. 

Proof. First, it is well-known that the dHYM equation (4.6) can be rewritten as the following equation 



Since θ ∈<sup>�</sup> (n − 2)π/2, nπ/2<sup>�</sup> , we have 



for k ∈{0, 1, · · · , n − 1}. Second, by Theorem 3.1, we consider the diagonal restriction, we get 



for k ∈{0, 1, · · · , n − 1}, where xk is the largest real root of the k-th derivative of the diagonal restriction. We claim that: 



Since tan(x) is increasing on (−π/2, π/2), to check (4.7), it suffices to check whether 



This is true because the function f (x) = (θ − xπ/2)/(n − x) is decreasing on (−∞, n). By Theorem 3.1, the level set is convex. 

In addition, we see that the dHYM equation is real-rooted, by Proposition 2.2, the dHYM equation is both strictly right-Noetherian and strictly left-Noetherian. So if θ ∈ �−nπ/2, −(n − 2)π/2<sup>�</sup> , then the level set will also be convex. □ 

# References 

- [1] N. Anari, S. O. Gharan, and C. Vinzant, Log-concave polynomials, entropy, and a deterministic approximation algorithm for counting bases of matroids, 2018 IEEE 59th Annual Symposium on Foundations of Computer Science (FOCS), pp. 35–46, 2018. 

- [2] N. Anari, K. Liu, S. O. Gharan, and C. Vinzant, Log-concave polynomials II: high-dimensional walks and an FPRAS for counting bases of a matroid, Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, pp. 1–12, 2019. 

- [3] N. Anari, K. Liu, S. O. Gharan, and C. Vinzant, Log-concave polynomials III: Mason’s ultra-log-concavity conjecture for independent sets of matroids, arXiv preprint arXiv:1811.01600, 2018. 

50 

- [4] N. Anari, K. Liu, S. O. Gharan, C. Vinzant, and T.-D. Vuong, Log-concave polynomials IV: approximate exchange, tight mixing times, and near-optimal sampling of forests, Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing, pp. 408–420, 2021. 

- [5] P. Br¨and´en and J. Huh, Lorentzian polynomials, Annals of Mathematics, vol. 192, no. 3, pp. 821–891, 2020. 

- [6] L. Caffarelli and Y. Yuan, A priori estimates for solutions of fully nonlinear equations with convex level set, Indiana University Mathematics Journal, vol. 49, no. 2, pp. 681–695, 2000. 

- [7] L. Caffarelli, L. Nirenberg, and J. Spruck, The Dirichlet problem for nonlinear second order elliptic equations, III: Functions of the eigenvalues of the Hessian, Acta Mathematica, vol. 155, no. 3-4, pp. 261–301, 1985. 

- [8] E. Calabi, The space of K¨ahler metrics, Proceedings of the International Congress of Mathematicians Amsterdam, pp. 206–207, 1954 

- [9] E. Calabi, On K¨ahler manifolds with vanishing canonical class, Algebraic geometry and topology. A symposium in honor of S. Lefschetz, Princeton Mathematical Series, vol. 12, pp. 78–89, 1957. 

- [10] G. Chen, The J-equation and the supercritical deformed Hermitian–Yang–Mills equation, Inventiones Mathematicae, vol. 225, no. 2, pp. 529–602, 2021. 

- [11] X. Chen, On the lower bound of the Mabuchi energy and its application, International Mathematics Research Notices, vol. 2000, no. 12, pp. 607–623, 2000. 

- [12] J. Chu, M.-C. Lee, and R. Takahashi, A Nakai–Moishezon type criterion for supercritical deformed Hermitian– Yang–Mills equation, Journal of Differential Geometry, (accepted). 

- [13] J. Chu and M.-C. Lee, Hypercritical deformed Hermitian–Yang–Mills equation revisited, Journal f¨ur die Reine und Angewandte Mathematik, vol. 801, pp. 161–172, 2023. 

- [14] T. C. Collins, A. Jacob, and S.-T. Yau, (1, 1) forms with specified Lagrangian phase: a priori estimates and algebraic obstructions, Cambridge Journal of Mathematics, vol. 8, no. 2, pp. 407–452, 2020. 

- [15] T. C. Collins and Y. Shi, Stability and the deformed Hermitian–Yang–Mills equation, Surveys in Differential Geometry, (accepted). 

- [16] T. C. Collins and G. Sz´ekelyhidi, Convergence of the J-flow on toric manifolds, Journal of Differential Geometry, vol. 107, no. 1, pp. 47–81, 2017. 

- [17] T. C. Collins and S.-T. Yau, Moment maps, nonlinear PDE and stability in mirror symmetry, I: Geodesics, Annals of PDE, vol. 7, no. 1, pp. 1–73, 2021. 

- [18] T. C. Collins, D. Xie, and S.-T. Yau, The deformed Hermitian–Yang–Mills equation in geometry and Physics, Geometry and Physics: A Festschrift in Honour of Nigel Hitchin, vol. 1, pp. 69–90, 2018. 

- [19] V. Datar and V. P. Pingali, A numerical criterion for generalised Monge–Amp`ere equations on projective manifolds, Geometric and Functional Analysis, vol. 31, no. 4, pp. 767–814, 2021. 

- [20] J.-P. Demailly and M. P˘aun, Numerical characterization of the K¨ahler cone of a compact K¨ahler manifold, Annals of Mathematics, vol. 159, no. 3, pp. 1247–1274, 2004. 

- [21] S. K. Donaldson, Anti self-dual Yang–Mills connections over complex algebraic surfaces and stable vector bundles, Proceedings of the London Mathematical Society, vol. 3, no. 1, pp. 1–26, 1985. 

- [22] S. K. Donaldson, Moment maps and diffeomorphisms, Asian Journal of Mathematics, vol. 3, no. 1, pp. 1–15, 1999. 

- [23] H. Fang and M. Lai, Convergence of general inverse σk-flow on K¨ahler manifolds, Transactions of the American Mathematical Society, vol. 365, no. 12, pp. 6543–6567, 2013. 

- [24] H. Fang, M. Lai, and X. Ma, On a class of fully nonlinear flows in K¨ahler geometry, Journal f¨ur die Reine und Angewandte Mathematik, vol. 653, pp. 189–220, 2011. 

- [25] D. Gilbarg and N. S. Trudinger, Elliptic partial differential equations of second order, Classics in Mathematics, Springer-Verlag, Berlin, reprint of the 1998 edition, 2001 

- [26] B. Guan, The Dirichlet problem for Hessian equations on Riemannian manifolds, Calculus of Variations and Partial Differential Equations, vol. 8, no. 1, pp. 45–69, 1999. 

- [27] B. Guan, Second-order estimates and regularity for fully nonlinear elliptic equations on Riemannian manifolds, Duke Mathematical Journal, vol. 163, no. 8, pp. 1491–1524, 2014. 

- [28] P. Guan and X. Zhang, A class of curvature type equations, Pure and Applied Mathematics Quarterly, vol. 17, no. 3, pp. 865–907, 2021. 

- [29] L. Gurvits, On multivariate Newton-like inequalities, Advances in Combinatorial Mathematics, pp. 61–78, 2009. 

- [30] J. Huh, J. Matherne, K. M´esz´aros, and A. St. Dizier, Logarithmic concavity of Schur and related polynomials, Transactions of the American Mathematical Society, vol. 375, no. 6, pp. 4411–4427, 2022. 

- [31] Z. Hou, X. Ma, and D. Wu, A second order estimate for complex Hessian equations on a compact K¨ahler manifold, Mathematical Research Letters, vol. 17, no. 3, pp. 547–561, 2010. 

51 

- [32] A. Jacob, Weak geodesics for the deformed Hermitian–Yang–Mills equation, Pure and Applied Mathematics Quarterly, vol. 17, no. 3, pp. 1113–1137, 2021. 

- [33] A. Jacob and N. Sheu, The deformed Hermitian–Yang–Mills equation on the blowup of P<sup>n</sup> , Asian Journal of Mathematics, vol. 26, no. 6, pp. 847–864, 2022. 

- [34] A. Jacob and S.-T. Yau, A special Lagrangian type equation for holomorphic line bundles, Mathematische Annalen, vol. 369, no. 1-2, pp. 869–898, 2017. 

- [35] D. Joyce, Y.-I. Lee, and R. Schoen, On the existence of Hamiltonian stationary Lagrangian submanifolds in symplectic manifolds, American Journal of Mathematics, vol. 133, no. 4, pp. 1067–1092, 2011. 

- [36] N. V. Krylov, Lectures on fully nonlinear second order elliptic equations, Lipschitz Lectures, Bonn University, 1993. 

- [37] N. V. Krylov, Fully nonlinear second order elliptic equations: recent development, Annali della Scuola Normale Superiore di Pisa-Classe di Scienze, vol. 25, no. 3-4, pp. 569–595, 1997. 

- [38] N. C. Leung, S.-T. Yau, and E. Zaslow, From special Lagrangian to Hermitian–Yang–Mills via Fourier–Mukai transform, Advances in Theoretical and Mathematical Physics, vol. 4, no. 6, pp. 1319–1341, 2000. 

- [39] M. Lejmi and G. Sz´ekelyhidi, The J-flow and stability, Advances in Mathematics, vol. 274, pp. 404–431, 2015. 

- [40] C.-M. Lin, Deformed Hermitian–Yang–Mills equation on compact Hermitian manifolds, Mathematical Research Letters, (accepted). 

- [41] C.-M. Lin, The deformed Hermitian–Yang–Mills Equation, the positivstellensatz, and the solvability, Advances in Mathematics, vol. 433, pp. 109312, 2023. 

- [42] C.-M. Lin, On the solvability of general inverse σk equations, arXiv:2310.05339, 2023. [43] S. Lu, On the Dirichlet problem for Lagrangian phase equation with critical and supercritical phase, Discrete and Continuous Dynamical Systems, vol. 43, no. 7, pp. 2561–2575, 2023. 

- [44] M. Mari˜no, R. Minasian, G. Moore, and A. Strominger, Nonlinear instantons from supersymmetric p-branes, Journal of High Energy Physics, vol. 2000, no. 1, 2000. 

- [45] D. H. Phong, S. Picard, and X. Zhang, The Fu–Yau equation with negative slope parameter, Inventiones Mathematicae, vol. 209, no. 2, pp. 541–576, 2017. 

- [46] D. H. Phong, S. Picard, and X. Zhang, The Anomaly flow and the Fu–Yau equation, Annals of PDE, vol. 4, no. 2, pp. 1–60, 2018. 

- [47] D. H. Phong, S. Picard, and X. Zhang, On estimates for the Fu–Yau generalization of a Strominger system, Journal f¨ur die Reine und Angewandte Mathematik (Crelles Journal), vol. 2019, no. 751, pp. 243–274, 2019. 

- [48] D. H. Phong, S. Picard, and X. Zhang, Fu–Yau Hessian equations, Journal of Differential Geometry, vol. 118, no. 1, pp. 147–187, 2021. 

- [49] V. P. Pingali, The deformed Hermitian Yang–Mills equation on three-folds, Analysis and PDE, vol. 15, no. 4, pp. 921–935, 2022. 

- [50] E. Schlitzer and J. Stoppa, Deformed Hermitian Yang–Mills connections, extended gauge group and scalar curvature, Journal of the London Mathematical Society, vol. 104, no. 2, pp. 770–802, 2021. 

- [51] R. Schoen and J. Wolfson, The volume functional for Lagrangian submanifolds, Lectures on Partial Differential Equations, 2003. 

- [52] Y.-T. Siu, Lectures on Hermitian–Einstein metrics for stable bundles and K¨ahler–Einstein metrics: delivered at the German Mathematical Society Seminar in D¨usseldorf in June, 1986, vol. 8, 1987. 

- [53] J. Song and B. Weinkove, On the convergence and singularities of the J-Flow with applications to the Mabuchi energy, Communications on Pure and Applied Mathematics, vol. 61, no. 2, pp. 210–229, 2008. 

- [54] J. Song, Nakai–Moishezon criterions for complex Hessian equations, arXiv:2012.07956, 2020. 

- [55] J. Spruck, Geometric aspects of the theory of fully nonlinear elliptic equations, Global Theory of Minimal Surfaces, vol. 2, pp. 283–309, 2005. 

- [56] G. Sz´ekelyhidi, Fully non-linear elliptic equations on compact Hermitian manifolds, Journal of Differential Geometry, vol. 109, no. 2, pp. 337–378, 2018. 

- [57] N. Trudinger, On the Dirichlet problem for Hessian equations, Acta Mathematica, vol. 175, no. 2, pp. 151–164, 1995. 

- [58] K. Uhlenbeck and S.-T. Yau, On the existence of Hermitian–Yang–Mills connections in stable vector bundles, Communications on Pure and Applied Mathematics, vol. 39, no. S1, pp. S257–S293, 1986. 

- [59] D. Wang and Y. Yuan, Singular solutions to special Lagrangian equations with subcritical phases and minimal surface systems, American Journal of Mathematics, vol. 135, no. 5, pp. 1157–1177, 2013. 

- [60] S.-T. Yau, On the Ricci curvature of a compact K¨ahler manifold and the complex Monge–Amp`ere equation, I, Communications on Pure and Applied Mathematics, vol. 31, no. 3, pp. 339–411, 1978. 

52 

- [61] Y. Yuan, Global solutions to special Lagrangian equations, Proceedings of the American Mathematical Society, vol. 134, no. 5, pp. 1355–1358, 2006. 

Chao-Ming Lin, Department of Mathematics, Ohio State University, OH E-mail address: lin.4579@osu.edu Personal Website: https://chaominl.github.io 

53 

