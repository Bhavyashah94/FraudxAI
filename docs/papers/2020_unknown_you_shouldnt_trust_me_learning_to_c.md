---
title: "You Shouldn't Trust Me: Learning to Conceal Biases in Explanation Methods"
authors: "unknown"
year: 2020
arxiv_id: "2004.04018"
original_file: "2004.04018.pdf"
pdf_path: "docs/papers\2020_unknown_you_shouldnt_trust_me_learning_to_c.pdf"
---

# You Shouldn't Trust Me: Learning to Conceal Biases in Explanation Methods

**Authors:** Unknown et al.  
**Year:** 2020 | **arXiv:** [`2004.04018`](https://arxiv.org/abs/2004.04018)  
**Local PDF:** [`2020_unknown_you_shouldnt_trust_me_learning_to_c.pdf`](file:///C:/Users/bhavy/Documents/Projects/FraudxAI/docs/papers/2020_unknown_you_shouldnt_trust_me_learning_to_c.pdf)

---

# On the Hellmann-Feynman theorem in statistical mechanics 

Paolo Amore<sup>1</sup> 

Facultad de Ciencias, CUICBAS, Universidad de Colima,Bernal D´ıaz del Castillo 

340, Colima, Colima,Mexico 

Francisco M. Fern´andez<sup>2</sup> 

INIFTA, Divisi´on Qu´ımica Te´orica, 

Blvd. 113 y 64 (S/N), Sucursal 4, Casilla de Correo 16, 

1900 La Plata, Argentina 

Abstract 

In this paper we develop the Hellmann-Feynman theorem in statistical mechanics without resorting to the eigenvalues and eigenvectors of the Hamiltonian operator. Present approach does not require the quantum-mechanical version of the theorem at T = 0 and bypasses any discussion about degenerate states. 

Key words: Hellman-Feynman theorem; statistical mechanics; canonical ensemble; arbitrary basis set 

> 1 e–mail: paolo@ucol.mx 

> 2 e–mail: fernande@quimica.unlp.edu.ar 

Preprint submitted to Elsevier 

4 May 2020 

## 1 Introduction 

Many years ago Feynman [1] developed a method for the calculation of forces in molecules that does not require the explicit use of the derivative of the energy. This expression, known as the Hellmann-Feynman theorem (HFT), is discussed in almost every book on quantum mechanics and quantum chemistry [2, 3] and some pedagogical articles discuss its utility in quantum mechanics [4, 5]. The HFT has also been applied to perturbation theory [4], even for degenerate states [5]. It is worth pointing out that the theorem had been developed by G¨uttinger [6] several years earlier (and in its more general offdiagonal form!!). However, in what follows we adhere to the common usage and will refer to the theorem by the usual and widely accepted name. 

Some time ago Zhang and George [7] reported a supposedly failure of the theorem in the case of degenerate states and proposed a remedy. Such assessment resulted curious in the light that the proof of the theorem does not require that the states are nondegenerate [1–5]. Several authors commented on this paper proving Zhang and George wrong with respect to the failure of the HFT [8–11]. In particular, Fern´andez [9] showed that the expression for the supposed remedy is correct but unnecessary because the original diagonal HFT is valid for degenerate states provided that one chooses the correct linear combinations of the degenerate eigenfunctions for the calculation. Such linear combinations appear naturally when one considers the off-diagonal version of the HFT and the limit λ → λ0, where λ is a parameter in the Hamiltonian operator H and λ0 the particular value of λ at which degeneracy occurs [9]. Despite all these proofs of the validity of the HFT the problem still seems to be poorly understood [12, 13]. This fact motivated a recent article with the purpose of clarifying the main points about the application of the HFT to degenerate states [14]. 

There has also been interest in the form of the HFT in statistical mechan- 

2 

ics where the authors have resorted to suitable sums over eigenstates of the Hamiltonian operator in their calculations [12,15,16] (and references therein). In particular, Rai [12] took into account the degenerate subspaces explicitly and argued that his results were a generalization of those of Fan and Chen [15] who had not considered degeneracy explicitly. More precisely, the former author resorted to the remedy of Zhang and George [7] that, as has already been proved, is unnecessary if one assumes that the mathematical procedure of Fan and Chen [15] is based on the degenerate eigenstates of the Hamiltonian operator that satisfy the HFT [9]. It is worth noticing that both strategies made use of the quantum-mechanical HFT (T = 0) in their derivation. 

The purpose of this paper is to show that one can easily obtain those results without using the eigenvalues and eigenvectors of the Hamiltonian operator and therefore bypass the quantum-mechanical HFT. In section 2 we develop the HFT in the canonical ensemble by means of an arbitrary basis set of states that do not depend on the parameter that is commonly varied to derive the HFT in quantum and statistical mechanics. One of the results in this section enables one to derive the HFT in the grand canonical ensemble. Finally, in section 3 we summarize the main results and draw conclusions. 

## 2 The Hellmann-Feynman theorem for the canonical ensemble 

The statistical average of an observable A in the canonical ensemble is given by 



where H is the Hamiltonian operator of the system and β = 1/(kBT ). 

Suppose that a function f (H) can be expanded as 



3 

and that H depends on a parameter λ. Therefore, 



where the prime stands for derivative with respect to λ. Obviously, we are assuming that the coefficients fj do not depend on λ. 

Taking into account a well known property of the trace 



we conclude that 



where 



It is clear that equation (5) is valid even when [H<sup>′</sup> , H]̸ = 0. Since the basis set used in the calculation of the trace is arbitrary we assume that it is independent of λ and equation (5) becomes 



that is the main result of this paper which will enable us to derive all the other necessary expressions. For example, 



and 



Since we have derived the result of Fan and Chen [15] and Rai [12] without resorting to the eigenstates of H, it is clear that it is valid whether there are degenerate states or not. Equation (4) is strictly valid in the case of a space 

4 

of finite dimension. If the dimension is infinite we may proceed as indicated in the Appendix A. 

The result above can be simplified a little bit further by means of the relationship 



so that 



In what follows we discuss the variation of the statistical average of an observable A with respect to λ although it has nothing to do with the HFT. One of the reasons for the analysis of this problem is that it was discussed by Fan and Chen [15], the other is that the result will prove useful for developing the form of the HFT in the grand canonical ensembel. For simplicity, we first consider an observable A that commutes with H ([H, A] = 0). On arguing as before we have 



so that 



Therefore, 



This expression is a particular case of the one developed by Fan and Chen [15] and both agree when the third and fourth terms in their equation (15) vanish. 

If [H, A]̸ = 0 we can obtain a compact expression by defining the operator F ∂ as ∂λ<sup>eβH=FeβH.DifferentiatingbothsidesofeβHe−βH=1withrespectto</sup> 

5 

λ we obtain ∂λ∂<sup>e−βH= −e−βHFsothatthederivativeof⟨A⟩</sup> av<sup>becomes</sup> 



Equation (14) enables one to derive the HFT in the grand canonical ensemble. To this end we turn to the notation of Rai [12] and write 



where H is the Hamiltonian operator in the Fock space, µ is the chemical potential and N<sup>ˆ</sup> a particle-number operator. It is clear that �H, N<sup>ˆ</sup> � = 0 because these operators have a common set of eigenvectors and ∂N/∂λ<sup>ˆ</sup> = 0. Therefore, [K, H] = 0 and K<sup>′</sup> = H<sup>′</sup> so that we can substitute K and H for H and A, respectively, in equation (14) thus obtaining Rai’s result [12] 



In order to test equation (11) we consider the dimensionless harmonic oscillator 



In this case we have 



and 



that already satisfy equation (11). 

## 3 Conclusions 

Earlier derivations of the HFT in statistical mechanics [12, 15, 16] resorted to the sum over states of the Hamiltonian operator H and, consequently, 

6 

required the HFT in quantum mechanics (T = 0) [1]. This fact motivated an unnecessary discussion about the validity of the mathematical proofs in the case of degeneracy [12]. Here, on the other hand, we have developed some of those expressions without taking into account neither the eigenstates nor the eigenvalues of the Hamiltonian operator thus showing that the occurrence of degeneracy is irrelevant. It is worth noticing that the main expressions derived by Fan and Chen [15], by Rai [12], as well as present ones, apply under exactly the same conditions. They merely differ in the strategies for their derivation. In addition to what has just been said, we have derived a simpler expression for the HFT in the canonical ensemble (11). 

In the case of the variation of the statistical weight of an observable A we have also derived a simple expression when [H, A] = 0 which has proved useful for the derivation of the HFT in the grand canonical ensemble. For the non-commuting case our expression, although simple, depends on an operator F that cannot be obtained in closed form for the general case. It is worth noticing that the result of Fan and Chen [15] depends on an operator O<sup>ˆ</sup> that exhibits the same difficulty. We have also argued that the approach of Rai [12] is by no means a generalization of that one of Fan and Chen [15] that applies to degenerate states provided that one chooses the correct eigenvectors of the Hamiltonian operator [9]. 

## Acknowledgements 

The research of P.A. was supported by Sistema Nacional de Investigadores (M´exico). 

7 

## A Convergence of the traces 

In principle, the trace in equation (4) may not exist in the case of an infinite basis set {|i⟩ , i = 1, 2, . . .}. To overcome this problem we define 



so that 



Therefore, if we repeat the argument given in section 2 we have 



and recover equation (7) in the limit M →∞. 

A more detailed discussion of infinite sums like (A.2) is available in a recent comprehensible paper [17] and the references therein. 

## References 

- [1] R. P. Feynman, Phys. Rev. 56 (1939) 340-343. 

- [2] C. Cohen-Tannoudji, B. Diu, and F. Lalo¨e, Quantum Mechanics, (John Wiley & Sons, New York, 1977). 

- [3] F. L. Pilar, Elementary Quantum Chemistry, (McGraw-Hill, New York, 1968). 

- [4] S. T. Epstein, Am. J. Phys. 22 (1954) 613-614. 

- [5] S. Brajamani Singh and C. A. Singh, Am. J. Phys. 57 (1989) 894-899. 

- [6] P. G¨uttinger, Z. Phys. 73 (1932) 169-184. 

- [7] G. P. Zhang and T. F. George, Phys. Rev. B 66 (2002) 033110. 

- [8] O. E. Alon and L. S. Cederbaum, Phys. Rev. B 68 (2003) 033105. 

8 

- [9] F. M. Fern´andez, Phys. Rev. B 69 (2004) 037101. 

- [10] S. R. Vatsya, Phys. Rev. B 69 (2004) 037102. 

- [11] R. Balawender, A. Holas, and N. H. March, Phys. Rev. B 69 (2004) 037103. 

- [12] D. Rai, Phys. Rev. A 75 (2007) 032514. 

- [13] N. Roy and A. Sharma, Phys. Rev. B 100 (2019) 195143. 

- [14] F. M. Fern´andez, On the Hellmann-Feynman theorem for degenerate states, arXiv:1912.04876 [quant-ph] 

- [15] H. Fan and B. Chen, Phys. Lett. A 203 (1995) 95-101. 

- [16] F. M. Fern´andez, J. Math. Chem. 52 (2014) 2128-2132. 

- [17] C. M. Bender, D. C. Brody, and M. F. Parry, Am. J. Phys. 88 (2020) 148-152. 

- [18] M. V. Berry and K. Burke, J. Phys. A 53 (2020) 095203. 

9 

