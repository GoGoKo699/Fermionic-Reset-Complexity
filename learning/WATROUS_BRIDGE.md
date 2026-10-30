# From Watrous to fermionic reset complexity

The educational anchor is John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018). The [author's book page](https://jhwatrous.github.io/books-and-courses.html) provides a manuscript, chapter files, and [errata](https://jhwatrous.github.io/TQI.errata.pdf). The pointers below were checked against the current author-hosted **standard-layout** files on 30 October 2026. They refer to section and theorem numbers, avoiding differences between PDF page counters and printed pagination. The manuscript is available for personal use; this repository links to it rather than reproducing it.

Watrous supplies the language of states, channels, reference systems, distinguishability, and source coding. The fermionic dynamics and the action bounds require additional arguments supplied by this project's [model](../science/model.md), [Gaussian proof](../science/gaussian_bound.md), [interacting construction](../science/interacting_reset.md), and [finite-size protocol](../science/finite_size.md). The research papers cited below retain their roles as primary sources.

## 1. Verified reading map

| Watrous pointer | Connection to the project |
|---|---|
| [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §1.1.3 | Spectral decomposition, singular values, and trace norms used in both converses. |
| Chapter 1, §§1.2.1–1.2.2 | Convexity, expectation, and concentration; background for averaging and compression estimates. |
| [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.1.2–2.1.3 | Density operators, mixtures, joint states, marginals, and purifications. |
| Chapter 2, §§2.2.1–2.2.2; Theorem 2.22 and Corollary 2.27 | Complete positivity and equivalent channel representations. |
| [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.1.1, Theorem 3.4; §3.2, Definition 3.11 | Operational state distance and the book's fidelity convention. |
| Chapter 3, §3.3.1 | Why a channel comparison includes an untouched reference. |
| Chapter 3, §3.3.2, Definition 3.43, Theorem 3.46, Proposition 3.48 | Completely bounded trace norm, sufficient reference dimension, and composition estimates. |
| Chapter 3, §3.3.3, Theorem 3.51 | Optimization over joint states for Hermitian-preserving maps, including differences of channels. |
| [Chapter 5](https://jhwatrous.github.io/TQI.5.pdf), §§5.1.1 and 5.2.1 | Entropy conventions for distributions and density operators. |
| Chapter 5, §5.3.1, Theorem 5.40 | Fixed-length coding of an independent, identically distributed classical source. |

Sections 3.3.1–3.3.2 motivate and define the channel norm. Theorem 3.51 in **§3.3.3** is also needed when expressing it as a maximum over input states and references. The relevant source-coding section is **§5.3.1**.

## 2. Notation translation

| Book notation or convention | Convention used here |
|---|---|
| A register has an associated space $`\mathcal X`$ | The occupation space of $`n`$ modes has dimension $`d=2^n`$. The mode count and Hilbert-space dimension differ exponentially. |
| The adjoint is $`B^*`$ | The project writes $`B^\dagger`$. Both denote the conjugate transpose. |
| A pure state is $`uu^*`$ | The project uses $`\lvert u\rangle\langle u\rvert`$. |
| Marginals can be written $`\rho[\mathrm R]`$ | The project writes $`\rho_R=\mathrm{Tr}_S\rho_{SR}`$. |
| §1.1.3 calls $`\lVert\rho-\sigma\rVert_1`$ the trace distance | The project uses the normalized distance $`D(\rho,\sigma)=\tfrac12\lVert\rho-\sigma\rVert_1`$. |
| The completely bounded trace norm has triple-bar notation | The project writes $`\lVert\Phi\rVert_\diamond`$ and uses **half** this norm for channel error. |
| $`\log`$ is base two; $`\ln`$ is natural | Action formulas use natural logarithms. Binary entropy $`h_2`$ uses base two. |

One further translation affects the exact theorem. Watrous defines $`F_{\rm W}(\rho,\sigma)=\lVert\sqrt\rho\sqrt\sigma\rVert_1`$. For a vacuum target, the project's population $`f=\langle\Omega|\rho|\Omega\rangle`$ equals **$`F_{\rm W}(\rho,|\Omega\rangle\langle\Omega|)^2`$**. Thus the project's symbol $`F_{\rm G}`$ denotes an optimized population, not the book's unsquared fidelity.

## 3. From a channel to a reset specification

The replacement channel is $`\mathcal R_n(B)=\mathrm{Tr}(B)|\Omega_n\rangle\langle\Omega_n|`$. Applying the Chapter 3 framework to $`\Phi-\mathcal R_n`$ gives the operational requirement

```math
\begin{aligned}
d_{\rm reset}(\Phi)
&=\frac12\|\Phi-\mathcal R_n\|_\diamond\\
&=\max_{\rho_{SR}}\frac12
\|\omega_{SR}-|\Omega_n\rangle\langle\Omega_n|\otimes\rho_R\|_1,\\
\omega_{SR}&=(\Phi\otimes\mathrm{id}_R)(\rho_{SR}).
\end{aligned}
```

A reference of dimension $`2^n`$ suffices. It is a test of what happens to correlations with an external system, not an ancillary register available to the controller. The project proves this ordinary matrix-algebra guarantee, which also covers the physically restricted parity-compatible tests.

Channel representations also need a resource interpretation. A Stinespring representation can describe a bath mathematically. It does not authorize an extra clean register, a freely chosen interaction with that register, or its disposal. Those operations would change the reset problem. The admissible physical resource here is the specified loss port, with action $`A=\int\kappa(t)\,dt`$; coherent pulses have the explicit idealized cost convention in the model.

### A one-mode calculation: specified input versus universal reset

For one loss interval with survival $`q=e^{-a}`$, Kraus operators are

```math
\begin{aligned}
K_0&=\begin{pmatrix}1&0\\0&\sqrt q\end{pmatrix},\qquad
K_1=\sqrt{1-q}\,|0\rangle\langle1|,\\
K_0^\dagger K_0+K_1^\dagger K_1&=I.
\end{aligned}
```

The maximally mixed input becomes $`\mathrm{diag}(1-q/2,q/2)`$, while the occupied input becomes $`\mathrm{diag}(1-q,q)`$. Their trace errors from vacuum are respectively $`q/2`$ and $`q`$.

At $`a=\ln5`$, the maximally mixed input therefore reaches vacuum population $`0.9`$, saturating the one-mode Gaussian theorem. The same channel has error $`0.2`$ on the occupied input. A sharp answer for the specified witness consequently does not identify the universal-channel optimum. Conversely, every universal reset must pass that witness, so the exact state theorem gives a valid channel lower bound.

## 4. Why reference correlations appear in the proof

A small error in the system marginal can conceal a larger joint error. For example, consider the joint pure state
$`|\psi_\eta\rangle=\sqrt{1-\eta}|00\rangle+\sqrt\eta|11\rangle`$, with $`0 \lt \eta \lt 1`$. Its system marginal is $`\mathrm{diag}(1-\eta,\eta)`$ and has vacuum trace error $`\eta`$. Direct diagonalization of the nonzero two-by-two block of the joint difference gives

```math
\begin{aligned}
&\frac12\bigl\||\psi_\eta\rangle\langle\psi_\eta|
-|0\rangle\langle0|\otimes\rho_R\bigr\|_1\\
&\qquad=\frac{\eta+\sqrt{4\eta-3\eta^2}}2.
\end{aligned}
```

This is of order $`\sqrt\eta`$ for small $`\eta`$. The example explains why a marginal population estimate cannot simply be reused as a joint trace-distance estimate. An exactly pure system marginal does force a product state; the issue here is quantitative approximation.

The [interacting proof, §§2–3](../science/interacting_reset.md) handles this issue explicitly. Averaging over even Majorana monomials is an allowed mixture of Gaussian unitaries. It removes all system information except parity. With $`P_m=(-1)^{\sum_jc_j^\dagger c_j}`$ the active-block parity, the twirled state has the form $`2^{-m}(I\otimes\rho_R+P_m\otimes\Delta_R)`$, where $`\|\Delta_R\|_1\le1`$. Equal loss with survival $`q`$ then gives

```math
\begin{aligned}
\omega_{SR}&=\sigma_q^{\otimes m}\otimes\rho_R
+\frac{q^mP_m}{2^m}\otimes\Delta_R,\\
\sigma_q&=\mathrm{diag}(1-q/2,q/2).
\end{aligned}
```

The second term contributes at most $`q^m/2`$ to half-trace distance. The comparison state is an independent biased source with the correct reference marginal. Deriving this identity requires the Majorana twirl and the action of fermionic loss on diagonal operators; it is additional to the textbook channel formalism.

The classical random seed is ignored in the output specification. Both control classes receive this same resource. The proof does not assert decoupling conditioned on that seed, and every seed realization has the prescribed action cap.

## 5. From matrix spectra to the Gaussian action law

The covariance matrix $`\gamma`$ is $`2n`$ by $`2n`$, whereas $`\rho`$ is $`2^n`$ by $`2^n`$. For an even Gaussian state, covariance eigenvalues $`\pm i\nu_j`$ determine the density spectrum as products of binary factors $`(1\pm\nu_j)/2`$. Here even means that $`\rho`$ commutes with parity; both parity sectors may be populated. This special spectral relation does not hold for general states. Its dynamical setting is supplied by [Onuma-Kalu et al., Eqs. (31)–(35)](https://arxiv.org/abs/1902.02239v2) and [Barthel and Zhang, Proposition 1 and Gaussian-state discussion](https://arxiv.org/abs/2112.08344v5).

The textbook spectral tools become useful once that fermionic structure has been established. Put $`\delta_j=1-\nu_j`$. The [Gaussian proof, §§3–6](../science/gaussian_bound.md) establishes

```math
\begin{aligned}
\prod_{j=1}^n\delta_j&\ge e^{-A},\\
\lambda_{\max}(\rho)&=\prod_{j=1}^n(1-\delta_j/2),\\
F_{\rm G}(n,A)&=\left(1-\frac12e^{-A/n}\right)^n.
\end{aligned}
```

For this converse, the Gaussian proof permits arbitrary linear jump operators under its total-rate action. This agrees with the single-port loss exposure, which already attains the frontier.

The first inequality is the essential dynamical step. Complete positivity gives a positive affine term in the equation for $`G=I+i\gamma`$; conjugate spectral pairing converts its contribution into a lower bound on the rate of change of $`\sum_j\ln\delta_j`$. Finite-action positivity justifies the logarithms, and the proof treats spectral degeneracies and pulses. General channel positivity or a density-matrix spectral decomposition alone does not supply this constraint.

For the optimization, write $`x_j=\ln\delta_j`$. The function $`f(x)=\ln(1-e^x/2)`$ is concave and decreasing. Jensen's inequality, followed by $`\sum_jx_j\ge-A`$, bounds $`\sum_jf(x_j)`$ by $`nf(-A/n)`$. Equal loss exposure gives $`\delta_j=e^{-A/n}`$ and attains equality. Since the attaining state is occupation-diagonal, its trace error from vacuum is exactly $`1-F_{\rm G}`$.

For randomized control, the argument is applied to each Gaussian branch. Vacuum population is linear in the output state, and the largest eigenvalue is convex, so the bounds survive averaging. This reasoning does not presume that a mixture of Gaussian states remains Gaussian.

## 6. From source coding to reversible parity-preserving compression

Watrous §5.3.1 gives the classical coding perspective: sufficiently probable strings from an independent source can be represented using fewer binary coordinates. Here the source is supplied by the twirl-and-loss calculation, with occupation probability $`p=q/2`$ and binary entropy $`h_2(p)`$. The entropy is measured in bits, while producing this bias costs $`m\ln(1/q)`$ of action.

There are three additional implementation requirements. Compression must act unitarily on the existing modes; it must preserve fermion parity; and it must give a bound valid with an arbitrary reference. The [one-stage lemma](../science/interacting_reset.md) meets them by counting good occupation strings, embedding their even and odd subsets separately, and completing both injections to permutations of the entire parity sectors. No additional clean output tape is supplied. This parity restriction concerns the coherent control: a loss event changes the register's particle-number parity, allowing eventual vacuum reset from either sector.

For a threshold $`p \lt r \lt 1/2`$, the good set contains strings of weight at most $`\lfloor rm\rfloor`$ and has size at most $`2^{m h_2(r)}`$. Choosing $`m'=\lceil m h_2(r)\rceil+1`$ gives $`2^{m'-1}`$ possible outputs in each trash parity sector, enough even when one sector contains all good strings. The finite-size implementation uses an additional spare mode, hence its $`+2`$ rather than the lemma's $`+1`$.

**Small counting illustration.** On four modes, strings of weight at most one comprise one even string and four odd strings. Three trash modes have four strings of each parity, so these five inputs can be mapped to a zero first mode while preserving parity. Two trash modes have only two odd strings and cannot accommodate that particular good set. This illustrates the capacity requirement; it is not an application of the more conservative entropy-threshold schedule.

The failure probability becomes a joint-state error through a direct block calculation. For a state diagonal on the proposed cold prefix, write $`\theta_{BZ}=\sum_b|b\rangle\langle b|\otimes C_b`$, with $`C_b\succeq0`$ and $`Z`$ containing the trash and reference. Then

```math
\begin{aligned}
&\frac12\left\|\theta_{BZ}
-|0\rangle\langle0|_B\otimes\mathrm{Tr}_B\theta_{BZ}\right\|_1\\
&\qquad=\sum_{b\ne0}\mathrm{Tr}C_b.
\end{aligned}
```

The right side is exactly the probability of a nonzero cold prefix. Positivity of the operator-valued blocks makes the estimate valid even with quantum correlations in $`Z`$. The prefix replacement displayed here is an analytical comparison, not a free operation implemented by the controller.

The one-sided tail constant used in the project comes from [Hoeffding's original Theorem 2](https://doi.org/10.1080/01621459.1963.10500830). Watrous Theorem 1.16 is a two-sided statement with prefactor two; substituting it unchanged would alter the allocated finite error. The cooling-and-compression mechanism itself is established algorithmic cooling, with primary antecedents in [Boykin et al.](https://arxiv.org/abs/quant-ph/0106093) and the [single-port control work of Bergholm, Wilhelm and Schulte-Herbrüggen](https://arxiv.org/abs/1605.06473v2).

## 7. Closing the proof with finite error and action accounting

Each new stage acts on an active block that may again be correlated. Its twirl restores the controlled source form. Contractivity of joint trace distance propagates the existing error; the next stage adds its own error. The [interacting proof, §5](../science/interacting_reset.md) also checks the fermionic parity strings across the frozen prefix. Treating a loss on an arbitrary fermionic suffix as an ordinary tensor-local qubit channel would omit that step.

The [finite-size rule](../science/finite_size.md) allocates $`\delta_m=\epsilon/[4m(m+1)]`$ to each of the tail and parity terms, uses an explicit rounded threshold, and performs a stage only when its capacity and error conditions hold. Active sizes strictly decrease, so the total stage allocation is at most $`\epsilon/2`$. Final cleanup uses $`q_f=\epsilon/(2m_f)`$, costing $`m_f\ln(2m_f/\epsilon)`$ and contributing at most the remaining $`\epsilon/2`$. The schedule is fixed independently of the input and seed.

For fixed $`q,\epsilon`$, the ratio of successive large active sizes approaches $`h_2(q/2) \lt 1`$. Summing their action yields the achievable limiting coefficient $`\ln(1/q)/[1-h_2(q/2)]`$; at $`q=1/5`$ this is about $`3.03`$. This is a coefficient for the stated construction. Finite-register calculations retain threshold rounding and cleanup costs.

The Gaussian witness forces $`n\ln n+O_\epsilon(n)`$ action at fixed global error, and a Gaussian universal protocol achieves that order. For arbitrary coherent control, the direct spectral bound $`\lambda_{\max}(\rho(T))\le e^A\lambda_{\max}(\rho(0))`$ supplies a lower bound $`n\ln2+\ln(1-\epsilon)`$ from the same maximally mixed input; the compression protocol supplies the linear upper bound. The [primary-source comparison](../references/RELATED_WORK.md) separates the inherited control and compression tools from these specific claims.

The resulting hierarchy is $`A_{\rm G}(n,\epsilon)=\Theta_\epsilon(n\ln n)`$ versus $`A_{\rm I}(n,\epsilon)=\Theta_\epsilon(n)`$, with all modes retained, the same single loss port, the same allowed randomization, and fixed global channel error. The Gaussian state-preparation frontier is exact; the finite-action universal optima and the optimal interacting leading coefficient remain unidentified. Coherent gate count, geometry, strength, duration, heat, and work are outside the charged action in this model.
