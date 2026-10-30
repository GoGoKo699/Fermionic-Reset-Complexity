# The reset task and its control resources

Reset prepares a register for reuse and removes its correlations with everything outside it. This requires control of the error of the entire register. Small mean occupation per mode is a different target: many small residual excitation probabilities can still make the probability of a completely empty register small.

This project asks how much integrated Markovian damping is needed to reset all modes when coherent controls are Gaussian, and how that cost changes when interactions can rearrange populations. The proofs allow fast global coherent control. The charged resource is dissipation; gate synthesis and geometric locality are outside this model.

## 1. Register, reference, and error

The register consists of $`n\geq1`$ fermionic modes with occupation space $`\mathcal H_n\cong\mathbb C^{2^n}`$. Fix an ordering and annihilation operators $`c_j`$ satisfying the canonical anticommutation relations. Write

```math
w_{2j-1}=c_j+c_j^\dagger,\qquad
w_{2j}=-i(c_j-c_j^\dagger),\qquad
\{w_a,w_b\}=2\delta_{ab}I.
```

The target is the vacuum $`|\Omega_n\rangle=|0\rangle^{\otimes n}`$ and the replacement channel

```math
\mathcal R_n(X)=\mathrm{Tr}(X)|\Omega_n\rangle\langle\Omega_n|.
```

For a channel $`\Phi`$ define

```math
\begin{aligned}
d_{\rm reset}(\Phi)
&=\frac12\|\Phi-\mathcal R_n\|_\diamond\\
&=\sup_{\rho_{AR}}\frac12\left\|
(\Phi\otimes\mathrm{id}_R)(\rho_{AR})
-|\Omega_n\rangle\langle\Omega_n|\otimes\rho_R\right\|_1.
\end{aligned}
```

The supremum can be taken over a reference of dimension $`2^n`$. Here the diamond norm is the ordinary completely bounded trace norm on the specified matrix algebra; the reference is an abstract quantum system. The construction proves this stronger mathematical guarantee, which includes every parity-compatible input/reference test. It is not merely a statement about mean occupation, one chosen input, or vacuum population without reference control. Background on the channel norm is given in [Watrous, Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/).

The regime of the main hierarchy is $`n\to\infty`$ with a fixed $`0\lt \epsilon\lt 1`$. All modes must be retained at the output. There are no supplied pure quantum ancillas, measurements, postselection, feedback from bath records, or coherent non-Markovian swaps with fresh bath modes.

## 2. The common loss resource

Both control classes can switch a single vacuum-loss port,

```math
\begin{aligned}
\dot\rho&=-i[H(t),\rho]+\kappa(t)\mathcal D[c_1](\rho),
\qquad \kappa(t)\geq0,\\
\mathcal D[L](\rho)&=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
\end{aligned}
```

The dissipative action is

```math
A=\int_0^T\kappa(t)\,dt.
```

For one freely damped occupation, the survival factor is $`q=e^{-A}`$. Gaussian mode permutations route any register mode through the one port. Parallel independent loss ports, if used instead, are charged by the integral of their **sum** of rates; they do not supply free parallel dissipation.

If the total damping rate is capped at $`\Gamma_{\max}`$, then every protocol takes at least $`A/\Gamma_{\max}`$ of dissipative exposure. The constructive protocols can attain this exposure in the ideal limit of instantaneous coherent pulses. Their complete hardware duration can be greater because coherent synthesis is not charged here.

## 3. Coherent control classes

**Gaussian control.** Hamiltonians are quadratic in the Majoranas, including pairing terms, with arbitrary time dependence and no locality restriction. Gaussian pulses may be inserted. Controls are integrable between pulses; finite pulse sequences and their finite-action limits are allowed as specified in the [Gaussian proof](gaussian_bound.md). An input-independent classical random seed may select a Gaussian control schedule. The output averages over that seed.

**Interacting control.** The same bath access and classical randomness are available, and coherent pulses may be arbitrary unitaries commuting with total fermion parity. In particular, a reversible permutation may rearrange occupation strings separately within their two parity sectors. Such permutations generally require nonquadratic interactions. Their synthesis cost is not estimated.

The random seed provides unital averaging, not a clean quantum subsystem. It is independent of the input, and no measurement outcomes or bath records are used. The error refers to the averaged channel after the controller's random record is ignored. Every branch obeys the same action cap; expected-action or postselected resource accounting is not used.

Let $`A_{\rm G}(n,\epsilon)`$ and $`A_{\rm I}(n,\epsilon)`$ be the infimum of these pathwise action caps over the two respective single-port classes with $`d_{\rm reset}\leq\epsilon`$.

## 4. A larger Gaussian class for the converse

The Gaussian lower bound actually holds with arbitrary linear jump operators,

```math
\begin{aligned}
L_\alpha(t)&=l_\alpha(t)^T w,&
M(t)&=\sum_\alpha l_\alpha(t)l_\alpha(t)^\dagger,\\
\Gamma(t)&=2\mathrm{Tr}M(t),&
A&=\int_0^T\Gamma(t)\,dt.
\end{aligned}
```

For $`L=\sqrt\kappa\,c_1`$, this convention gives $`\Gamma=\kappa`$. Thus the stronger converse uses the same normalization as the single-port comparison. Equal vacuum loss, attainable with that port and Gaussian permutations, saturates the state-preparation bound. Heating or other linear bath orientations cannot improve it at a fixed action.

With covariance

```math
\gamma_{ab}=\frac{i}{2}\mathrm{Tr}\rho[w_a,w_b],
```

the evolution is $`\dot\gamma=X\gamma+\gamma X^T+C`$, where $`X=K-2\mathrm{Re}M`$, $`K^T=-K`$, and $`C=4\mathrm{Im}M`$. Complete positivity gives

```math
\begin{aligned}
G&=I+i\gamma,&\dot G&=XG+GX^T+D,\\
D&=-X-X^T+iC=4M\succeq0,&\mathrm{Tr}X&=-\Gamma.
\end{aligned}
```

The normalization and covariance formalism are standard ingredients; the [related-work account](../references/RELATED_WORK.md) identifies their primary sources and separates them from the optimized action bound.

## 5. Exact state frontier and universal hierarchy

For the maximally mixed input $`\tau_n=I/2^n`$, the [Gaussian theorem](gaussian_bound.md) gives

```math
\sup_{\Phi\in\mathrm G:\,A(\Phi)\leq A}
\langle\Omega_n|\Phi(\tau_n)|\Omega_n\rangle
=\left(1-\frac12e^{-A/n}\right)^n.
```

The equality holds both for the single-port class and for its larger linear-jump extension. For $`0\lt \epsilon\lt 1-2^{-n}`$, the exact action needed for this **one input and vacuum-probability criterion** is

```math
A_{\rm G}^{\tau}(n,\epsilon)
=n\ln\frac{1}{2[1-(1-\epsilon)^{1/n}]}.
```

For looser errors the state-preparation action is zero. Universal reset is constrained by this witness, but its finite-action optimum is not identified by that equality. The [universal constructions and converse](interacting_reset.md) prove

```math
\max\{0,A_{\rm G}^{\tau}(n,\epsilon)\}
\leq A_{\rm G}(n,\epsilon)
\leq n\ln\frac{n}{\epsilon},
```

where the witness expression is interpreted as zero outside its positive domain, and

```math
\max\{0,n\ln2+\ln(1-\epsilon)\}
\leq A_{\rm I}(n,\epsilon)
\leq Cn+C_\epsilon,
\qquad C\lt 14.692.
```

Consequently, at each fixed global error,

```math
A_{\rm G}(n,\epsilon)=\Theta_\epsilon(n\ln n),\qquad
A_{\rm I}(n,\epsilon)=\Theta_\epsilon(n).
```

The [finite-size protocol](finite_size.md) improves the explicit achievable constant and supplies concrete action certificates. No optimal leading interacting constant or uniform optimal joint dependence on $`n`$ and $`\epsilon`$ is claimed.

## Reading the result

Quadratic control can rotate and redistribute Gaussian occupation defects, but complete positivity limits their product at a fixed action. Global vacuum accuracy forces each of many defects to become small. Interacting permutations instead concentrate residual uncertainty into fewer active modes, so successive cooling stages act on a shrinking register. The [interpretation](interpretation.md) explains this mechanism and the resource boundaries; the two proof pages supply its exact statements.
