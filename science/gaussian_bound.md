# Exact Gaussian cooling law from the maximally mixed state

For a register of $n\geq 1$ fermionic modes, the maximum vacuum population obtainable from the maximally mixed state with Gaussian Markovian controls and dissipative action at most $A\geq0$ is

$$
\boxed{F_{\mathrm G}(n,A)=\left(1-\frac12 e^{-A/n}\right)^n.}
\tag{1}
$$

The controls include arbitrary quadratic Hamiltonians, arbitrary linear Lindblad jump operators, instantaneous Gaussian unitary pulses, and classical randomization with an action bound for every realization. Equal loss exposure of all modes attains (1), including through a single reset port. This is an exact state-preparation result for a specified maximally mixed input. It supplies a converse for universal reset, but does not assert that (1) is the exact finite-action fidelity of the universal reset problem.

All logarithms below are natural. Vacuum population means the overlap $\langle\Omega|\rho|\Omega\rangle$, without taking its square root.

## 1. Model, normalization, and admissible controls

Let $w=(w_1,\ldots,w_{2n})^T$ be Majorana operators satisfying

$$
w_j=w_j^\dagger,\qquad \{w_j,w_k\}=2\delta_{jk}I,
\qquad c_j=\frac{w_{2j-1}+i w_{2j}}2.
\tag{2}
$$

The vacuum is $c_j|\Omega\rangle=0$ for every $j$. The initial state is

$$
\tau_n=\frac{I}{2^n}.
\tag{3}
$$

An even density operator is one commuting with total parity $P=(-1)^{\sum_j c_j^\dagger c_j}$; both parity sectors may be populated. The initial state is even. The dynamics below preserve this property because the Hamiltonian is even and every linear jump is odd.

Between instantaneous pulses, the density operator solves the ordinary GKSL equation

$$
\dot\rho=-i[H(t),\rho]+\sum_\alpha
\left(L_\alpha(t)\rho L_\alpha(t)^\dagger
-\frac12\{L_\alpha(t)^\dagger L_\alpha(t),\rho\}\right),
\tag{4}
$$

with

$$
H(t)=\frac{i}{4}w^TK(t)w,\qquad K(t)\in\mathbb R^{2n\times2n},
\quad K(t)^T=-K(t),
\qquad L_\alpha(t)=l_\alpha(t)^Tw.
\tag{5}
$$

Define the positive semidefinite Hermitian matrix

$$
M(t)=\sum_\alpha l_\alpha(t)l_\alpha(t)^\dagger\succeq0.
\tag{6}
$$

On a finite time interval, assume $K$ is Lebesgue integrable and $M$ is measurable with $\int\operatorname{Tr}M(t)\,dt<\infty$. These conditions include piecewise continuous and piecewise constant controls of arbitrary strength. They also allow countably many jumps when the sum in (6) is well defined and has integrable trace. Equivalently, a measurable factorization of the finite matrix $M$ uses at most $2n$ linear jumps. No differentiability of the individual jump coefficients is needed.

These assumptions give an integrable finite-dimensional master-equation generator and a unique absolutely continuous solution. One can approximate $K$ and $M$ in $L^1$ by step functions while preserving skew symmetry and positive semidefiniteness, respectively. The associated propagators converge, preserving complete positivity and trace. The same approximation extends Gaussian preservation from piecewise constant quasi-free dynamics to these integrable controls. The covariance formulation and Gaussian preservation for quadratic Hamiltonians and linear jumps are standard; see [Onuma-Kalu et al., Eqs. (31)–(35)](https://arxiv.org/pdf/1902.02239v2) and [Barthel and Zhang, Proposition 1 and the discussion of Gaussian states](https://arxiv.org/pdf/2112.08344v5).

A Gaussian pulse acts by $\rho\mapsto U\rho U^\dagger$, with $U^\dagger wU=Ow$ and $O\in SO(2n)$. Finitely many such pulses are allowed and carry no dissipative action. We also include limits of these protocols whenever their final states converge and their action bounds are uniform; the bound below is continuous in the final state. This includes well-defined limits of increasingly rapid pulses, without assigning a differentiable Hamiltonian to an instantaneous pulse.

Controls are prescribed independently of the unknown state and of any bath measurement record. Classical randomization over prescribed protocols is allowed provided every realization has action at most $A$. No additional controlled register modes, pure ancillary states, measurements, postselection, or free reset maps are supplied. An average-action constraint alone is a different resource model and is not the condition used here.

## 2. Covariance equation and physical rate

Use the real antisymmetric covariance convention

$$
\gamma_{jk}=\frac{i}{2}\operatorname{Tr}\bigl(\rho[w_j,w_k]\bigr).
\tag{7}
$$

In particular, a vacuum mode has $\gamma_{12}=-1$. With the normalization in (4), direct use of the canonical anticommutation relations gives

$$
\dot\gamma=X\gamma+\gamma X^T+C,
\qquad
X=K-2\operatorname{Re}M,
\qquad C=4\operatorname{Im}M.
\tag{8}
$$

For clarity, the adjoint dissipator on a quadratic observable follows from

$$
\mathcal D_L^\dagger(O)
=\frac12\bigl(L^\dagger[O,L]+[L^\dagger,O]L\bigr),
\qquad
[w_jw_k,w_a]=2(\delta_{ka}w_j-\delta_{ja}w_k)
\quad(j\ne k).
\tag{9}
$$

Substituting $L=l^Tw$ into (9), using
$\operatorname{Tr}(\rho w_jw_k)=\delta_{jk}-i\gamma_{jk}$, gives the dissipative contribution
$-2(\operatorname{Re}M)\gamma-2\gamma(\operatorname{Re}M)+4\operatorname{Im}M$.
The Hamiltonian convention in (5) gives $\dot w=Kw$, and hence the remaining terms in (8). This fixes both the factors and the sign of $C$; references using the opposite covariance convention have the opposite sign for the affine term.

Define

$$
\Gamma(t)=2\operatorname{Tr}M(t)=-\operatorname{Tr}X(t),
\qquad a(t)=\int_0^t\Gamma(s)\,ds.
\tag{10}
$$

For one loss operator $L=\sqrt\kappa\,c$,

$$
l=\frac{\sqrt\kappa}{2}\begin{pmatrix}1\\ i\end{pmatrix},
\quad
M=\frac\kappa4\begin{pmatrix}1&-i\\ i&1\end{pmatrix},
\quad X=-\frac\kappa2I,
\quad C=\kappa\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\tag{11}
$$

Thus $\Gamma=\kappa$, and the excited population obeys
$\dot p=-\kappa p$. For independent losses with rates $\kappa_j$,
$\Gamma=\sum_j\kappa_j$. The action therefore counts ordinary loss exposure, rather than a convention-dependent multiple of it.

No restriction to losses or number-conserving Hamiltonians was used in (8). The jumps may mix annihilation and creation operators, may be Hermitian, and need not be canonical annihilation modes. The proof uses their full generality through $M\succeq0$.

## 3. Finite-action positivity

Set

$$
G=I+i\gamma.
\tag{12}
$$

Covariance physicality gives $0\preceq G\preceq2I$, and the real antisymmetry of $\gamma$ gives $\overline G=2I-G$. Equation (8) becomes

$$
\dot G=XG+GX^T+D,
\qquad
D=-X-X^T+iC=4M\succeq0.
\tag{13}
$$

Let $S(t,s)$ be the fundamental matrix of $\dot S=X S$, with $S(s,s)=I$. For integrable $X$, it exists, is absolutely continuous, and is invertible. Variation of constants, with $G(0)=I$, yields

$$
G(t)=S(t,0)S(t,0)^T+
\int_0^t S(t,s)D(s)S(t,s)^T\,ds
\succeq S(t,0)S(t,0)^T\succ0.
\tag{14}
$$

There is also an action-only lower bound. Since
$X+X^T=-4\operatorname{Re}M$ and
$0\preceq\operatorname{Re}M\preceq(\operatorname{Tr}M)I$,

$$
\frac{d}{dt}\|S(t,s)v\|^2
\ge -2\Gamma(t)\|S(t,s)v\|^2.
\tag{15}
$$

Gronwall's inequality gives

$$
\sigma_{\min}(S(t,s))\ge e^{-[a(t)-a(s)]},
\qquad
\boxed{G(t)\succeq e^{-2a(t)}I.}
\tag{16}
$$

Orthogonal pulses preserve eigenvalues and the lower bound in (16), so the conclusion extends across all pulse intervals. In particular, finite action leaves every eigenvalue of $G$ strictly positive. This justifies the logarithms used below before any spectral inequality has been proved.

## 4. Spectral pairing at degeneracies

Write the eigenvalues of $G$ as

$$
1-\nu_1,\ldots,1-\nu_n,
1+\nu_n,\ldots,1+\nu_1,
\qquad 1>\nu_1\ge\cdots\ge\nu_n\ge0,
\tag{17}
$$

and put

$$
\delta_j=1-\nu_j\in(0,1].
\tag{18}
$$

These are the $n$ smallest ordered eigenvalues of $G$. Ordered eigenvalues of Hermitian matrices obey the operator-norm perturbation bound, so they are absolutely continuous whenever $G$ is absolutely continuous. On an interval with action at most $A$, (16) bounds every $\delta_j$ below by $e^{-2A}$. Therefore each $\log\delta_j$, and their sum, is absolutely continuous as well.

The following pairing fact permits an almost-everywhere derivative argument without choosing globally differentiable eigenvectors.

**Pairing lemma.** At almost every time between pulses, there is an orthonormal basis

$$
v_1,\overline v_1,\ldots,v_n,\overline v_n
\tag{19}
$$

such that

$$
Gv_j=\delta_jv_j,
\qquad G\overline v_j=(2-\delta_j)\overline v_j,
\qquad
\dot\delta_j=v_j^\dagger\dot Gv_j.
\tag{20}
$$

**Proof.** Work at a time where $G$ and its ordered eigenvalues are differentiable; these conditions hold almost everywhere. Within a degenerate eigenvalue space $E_\lambda$, first-order Hermitian perturbation theory identifies the right eigenvalue derivatives with the eigenvalues of the compression
$P_\lambda\dot G P_\lambda$ to $E_\lambda$. This follows directly by inserting
$G(t+h)=G(t)+h\dot G(t)+o(h)$ into the eigenvalue equation: the complementary spectral subspace is separated by a fixed nonzero gap, so its elimination changes the first-order block only by $o(h)$.

Complex conjugation maps $E_\lambda$ onto $E_{2-\lambda}$. Because $\overline{\dot G}=-\dot G$, it pairs their first-order compressions with opposite eigenvalue derivatives. For $\lambda<1$, choose an orthonormal eigenbasis of the compressed derivative and use its conjugates for the partner space.

The only remaining case is $E_1$, the kernel of $\gamma$. This space has even dimension and admits a real orthonormal basis. In that basis the compression of $\dot G$ is $i$ times a real antisymmetric matrix, so its eigenvalues occur in opposite pairs. Choose the nonpositive member of each pair for the lower half of the spectrum, with the conjugate vector for the other member. Its zero eigenspace has even dimension; pairing real orthonormal vectors as $(e_{2r-1}+ie_{2r})/\sqrt2$ and their conjugates handles zero shifts. These choices give the right derivatives of the lower ordered eigenvalues. At the differentiability times under consideration, the right derivatives equal their ordinary derivatives. Thus (19)–(20) hold, including at persistent degeneracies. No assumption that crossings are isolated is needed. ∎

## 5. Integrated log-defect inequality

Define

$$
\Phi(t)=\sum_{j=1}^n\log\delta_j(t).
\tag{21}
$$

At an almost-everywhere differentiability time, use the basis in the pairing lemma and let
$b_j=\operatorname{Re}(v_j^\dagger Xv_j)$. Since $X$ is real,
$\operatorname{Re}(\overline v_j^\dagger X\overline v_j)=b_j$. The completeness of the paired basis gives

$$
2\sum_{j=1}^n b_j=\operatorname{Tr}X.
\tag{22}
$$

Equations (13) and (20) give

$$
\dot\delta_j
=2\delta_j b_j+v_j^\dagger Dv_j.
\tag{23}
$$

Consequently,

$$
\dot\Phi
=\operatorname{Tr}X+
\sum_{j=1}^n\frac{v_j^\dagger Dv_j}{\delta_j}
\ge\operatorname{Tr}X=-\Gamma.
\tag{24}
$$

Absolute continuity permits integration of this almost-everywhere inequality. Initially $\delta_j(0)=1$, so $\Phi(0)=0$. A Gaussian pulse leaves every $\delta_j$ unchanged, and hence adds no jump to $\Phi$. Therefore

$$
\boxed{
\sum_{j=1}^n\log(1-\nu_j(t))\ge-a(t),
\qquad
\prod_{j=1}^n(1-\nu_j(t))\ge e^{-a(t)}.
}
\tag{25}
$$

This establishes the resource inequality for the full integrable control class, including all crossings and pulse boundaries.

## 6. Exact fidelity bound

For an even fermionic Gaussian state, the canonical covariance form gives a density-matrix spectrum consisting of all products of the binary spectra $(1+\nu_j)/2,(1-\nu_j)/2$. Thus

$$
\lambda_{\max}(\rho)
=\prod_{j=1}^n\frac{1+\nu_j}{2}
=\prod_{j=1}^n\left(1-\frac{\delta_j}{2}\right).
\tag{26}
$$

This Gaussian normal-form fact is reviewed in [Barthel and Zhang](https://arxiv.org/pdf/2112.08344v5). Starting from $\tau_n$, every deterministic protocol in Sections 1–2 stays in this Gaussian class.

Let $x_j=\log\delta_j\le0$ and define

$$
f(x)=\log\left(1-\frac{e^x}{2}\right),
\quad
f'(x)=-\frac{e^x}{2-e^x}<0,
\quad
f''(x)=-\frac{2e^x}{(2-e^x)^2}<0.
\tag{27}
$$

Using concavity, then (25) and monotonicity,

$$
\begin{aligned}
\log\lambda_{\max}(\rho(T))
&=\sum_j f(x_j)\\
&\le n f\!\left(\frac1n\sum_j x_j\right)\\
&\le n f\!\left(-\frac{a(T)}n\right).
\end{aligned}
\tag{28}
$$

Every pure-state overlap is bounded above by the largest eigenvalue. Since the right side of (1) increases with action, every protocol with $a(T)\le A$ obeys

$$
\langle\psi|\rho(T)|\psi\rangle
\le\lambda_{\max}(\rho(T))
\le F_{\mathrm G}(n,A)
\quad\text{for every normalized }|\psi\rangle.
\tag{29}
$$

For a randomized protocol, apply (29) to each realization. Target population is linear in the averaged state, while $\lambda_{\max}$ is convex; both bounds therefore survive averaging when the action cap holds for every realization. The averaged state need not be Gaussian. Finally, continuity of target overlap and largest eigenvalue extends (29) to the protocol limits specified in Section 1.

## 7. Attainment by equal exposure

Give each physical mode a pure-loss exposure $a_j=A/n$, with no coherent evolution required. From the initial population $1/2$, its final excited population is

$$
p_j=\frac12e^{-a_j}=\frac12e^{-A/n}.
\tag{30}
$$

The state remains diagonal and factorized in the occupation basis:

$$
\rho(T)=\bigotimes_{j=1}^n
\operatorname{diag}\left(1-\frac12e^{-A/n},\frac12e^{-A/n}\right).
\tag{31}
$$

Its vacuum population and largest eigenvalue are both $F_{\mathrm G}(n,A)$, attaining the bound. Equivalently, $\delta_j=e^{-A/n}$, so (25) and the concavity step both saturate.

The same final state is achievable with one loss port $L=\sqrt{\kappa(t)}c_1$. Move one logical mode at a time to the port with Gaussian mode permutations, expose it for integrated rate $A/n$, and restore the mode labels. Fermionic exchange phases do not affect the diagonal states in this construction. Exactly $n$ equal exposures give total action $A$. Thus allowing many simultaneous linear jumps strengthens the converse without being necessary for attainment.

Let $\mathsf D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1$. A measurement of the vacuum projector implies

$$
\mathsf D(\rho,|\Omega\rangle\!\langle\Omega|)
\ge1-\langle\Omega|\rho|\Omega\rangle.
\tag{32}
$$

Equality holds for (31). Therefore the exact optimal trace error for preparing vacuum from $\tau_n$ is also $1-F_{\mathrm G}(n,A)$.

## 8. Error thresholds and asymptotics

For $0\le\epsilon\le1$, the minimum action to obtain vacuum population at least $1-\epsilon$ from $\tau_n$ is

$$
\boxed{
A_{\mathrm G}^{\tau}(n,\epsilon)=
\begin{cases}
+\infty,&\epsilon=0,\\[3pt]
\displaystyle n\log\frac{1}{2\left[1-(1-\epsilon)^{1/n}\right]},
&0<\epsilon<1-2^{-n},\\[8pt]
0,&1-2^{-n}\le\epsilon\le1.
\end{cases}}
\tag{33}
$$

At zero action the overlap is $2^{-n}$; finite action cannot produce a pure state exactly. These observations account for both endpoint cases.

For fixed $\epsilon\in(0,1)$, let $b=-\log(1-\epsilon)>0$. As $n\to\infty$,

$$
A_{\mathrm G}^{\tau}(n,\epsilon)
=n\log n-n\log(2b)+\frac b2+O_\epsilon(n^{-1})
=n\log n+O_\epsilon(n).
\tag{34}
$$

In the small-error regime, the leading form is $n\log[n/(2\epsilon)]$.

Any channel whose half-diamond distance from vacuum replacement is at most $\epsilon$ must, in particular, prepare vacuum from $\tau_n$ with trace error at most $\epsilon$. Equation (33) is therefore a lower bound on the action of every universal Gaussian reset protocol under the same action convention. Establishing this converse does not identify the exact finite-action universal optimum.

## 9. Independent convention check

[gaussian_hilbert_conventions.py](../verification/gaussian_hilbert_conventions.py) independently constructs Jordan–Wigner Majorana matrices and the full finite-dimensional generator (4), then compares its exact matrix-exponential evolution with (8). The fixed-seed examples cover one, two, and three modes, general linear jumps, uniform losses, and a mixture of gain and a Hermitian Majorana jump, with arbitrary quadratic Hamiltonians. They also compare the actual density-matrix largest eigenvalue with (26) and check equal-exposure saturation.

The recorded run passed all nine examples at a tolerance of $10^{-10}$. Its maximum covariance discrepancy was below $1.4\times10^{-15}$ and maximum density-spectrum discrepancy was below $2.8\times10^{-16}$. These finite examples check conventions and implementation; the proof of the arbitrary-control statement is Sections 3–6.

## References

1. Marvellous Onuma-Kalu, Daniel Grimmer, Robert B. Mann, and Eduardo Martín-Martínez, **A classification of Markovian fermionic Gaussian master equations**, [arXiv:1902.02239v2](https://arxiv.org/abs/1902.02239v2), [DOI:10.1088/1751-8121/ab40e1](https://doi.org/10.1088/1751-8121/ab40e1). The Majorana and dissipator normalizations in that article differ from (2) and (4); equations (8)–(11) provide the convention used here.
2. Thomas Barthel and Yikang Zhang, **Solving quasi-free and quadratic Lindblad master equations for open fermionic and bosonic systems**, *Journal of Statistical Mechanics* **2022**, 113101, [arXiv:2112.08344v5](https://arxiv.org/abs/2112.08344v5), [DOI:10.1088/1742-5468/ac8e5c](https://doi.org/10.1088/1742-5468/ac8e5c). The present Gaussian theorem uses the quasi-free subclass with linear jumps; additional quadratic Hermitian jumps do not in general preserve Gaussian states.
