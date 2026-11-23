# Exact finite-action universal reset

[Model and resource contract](model.md) · [Gaussian state bound](gaussian_bound.md) · [Interacting frontier](interacting-frontier.md)

The input to a reset channel can occupy either parity sector and may carry quantum correlations with a reference. The [Gaussian state bound](gaussian_bound.md) starts from the maximally mixed state, which weights the two sectors equally. At finite action the sector weights matter. The initial difference between the two sector states survives as a parity term of known size, independent of the coherent controls. This gives the exact conversion from one-input vacuum probability to worst-case channel error.

## The finite-action formula

Let $`C`$ denote either control class in the [model](model.md). Let $`r_{\rm C}(n,A)`$ be the infimum of $`d_{\rm reset}`$ over its channels with pathwise action at most $`A`$, allowing the model's input-independent random control. Write $`\tau_n=I/2^n`$ and $`\Pi_0=|\Omega_n\rangle\langle\Omega_n|`$, and set

```math
F_{\rm C}(n,A)
=\sup_{\Lambda\,:\,\text{deterministic in C, action }A}
\mathrm{Tr}[\Pi_0\Lambda(\tau_n)].
```

The optimum obeys

```math
r_{\rm C}(n,A)=1-F_{\rm C}(n,A)+2^{-n}e^{-A}.
\qquad\text{(U1)}
```

For Gaussian controls the existing single-input theorem determines $`F_{\rm G}`$. Consequently, for every $`n\geq1`$ and $`A\geq0`$,

```math
r_{\rm G}(n,A)
=1-\left(1-\frac12 e^{-A/n}\right)^n+2^{-n}e^{-A}.
\qquad\text{(U2)}
```

Equation (U2) holds with either the one vacuum-loss port or the larger class of arbitrary linear jumps at the same action normalization. It is attained using only the single port, Gaussian pulses and the two input-independent randomizations described below. Equation (U1) also holds with parity-preserving interacting controls. It leaves an optimization over deterministic trajectories from the fully specified state $`\tau_n`$ in that class.

## Parity decay on each trajectory

Let $`P=\prod_{j=1}^n(1-2c_j^\dagger c_j)`$. The normalized uniform states in the even and odd sectors are $`\tau_\pm=(I\pm P)/2^n`$. Every coherent Hamiltonian or pulse in either class preserves $`P`$ under conjugation. For a linear jump $`L=l^Tw`$, the canonical anticommutation relations give $`PL=-LP`$ and $`\{L,L^\dagger\}=2\lVert l\rVert_2^2 I`$. It follows that

```math
\begin{aligned}
\mathcal D[L](P)
&=LP L^\dagger-\tfrac12\{L^\dagger L,P\}\\
&=-P(LL^\dagger+L^\dagger L)
=-2\lVert l\rVert_2^2P .
\end{aligned}
```

This identity concerns the Schrödinger-picture channel applied to the operator $`P`$. It is a statement about an initial difference of states. For several simultaneous jumps the decay rates sum to $`\Gamma(t)=2\sum_\alpha\lVert l_\alpha(t)\rVert_2^2`$, the rate used to define the action in the model. For a single port $`L=\sqrt{\kappa}\,c_1`$, one has $`\Gamma=\kappa`$. Integration, including the coherent pulses, gives

```math
\Lambda(P)=e^{-a}P,\qquad a=\int_0^T\Gamma(t)\,dt .
\qquad\text{(U3)}
```

The identity is preserved in finite-action channel limits by continuity. Since $`P|\Omega_n\rangle=|\Omega_n\rangle`$, the vacuum probabilities for the sector inputs to a deterministic trajectory are

```math
\mathrm{Tr}[\Pi_0\Lambda(\tau_\pm)]
=\mathrm{Tr}[\Pi_0\Lambda(\tau_n)]\pm 2^{-n}e^{-a}.
\qquad\text{(U4)}
```

The control-independent parity mode is established in fermionic open-system theory. See [Schulenborg et al., Eq. (5)](https://arxiv.org/abs/1508.06145) for the interaction-independent mode in a reservoir-coupled system and [Bruch et al., Eq. (32)](https://doi.org/10.21468/SciPostPhys.11.3.053) for the propagator identity in the wide-band setting. Equation (U3) derives the corresponding identity directly for this controlled Markovian generator and its action convention. The operational step below uses that identity to compare a specific state-preparation task with a universal channel task.

## Lower bound for any pathwise-capped protocol

A deterministic trajectory of action $`a\leq A`$ can spend the remaining action on vacuum loss through the same port. The loss adjoint sends the vacuum projector to

```math
\Pi_0+(1-e^{-(A-a)})|1_1,0_{\ne1}\rangle\langle 1_1,0_{\ne1}|.
```

This operator is at least $`\Pi_0`$, so padding cannot decrease the mixed-input vacuum probability. The argument also applies to the enlarged Gaussian class, which contains the vacuum port. Thus $`F_{\rm C}(n,A)`$ upper-bounds the probability from $`\tau_n`$ for every branch with action $`a\leq A`$.

Now test a randomized channel $`\Phi=\mathbb E\Lambda`$ on $`\tau_-`$. The vacuum test has failure probability at most the trace distance from vacuum, and this trace distance is at most $`d_{\rm reset}(\Phi)`$. By (U4),

```math
\begin{aligned}
d_{\rm reset}(\Phi)
&\geq 1-\mathrm{Tr}[\Pi_0\Phi(\tau_-)]\\
&=1-\mathrm{Tr}[\Pi_0\Phi(\tau_n)]+2^{-n}\mathbb E[e^{-a}]\\
&\geq 1-F_{\rm C}(n,A)+2^{-n}e^{-A}.
\end{aligned}
\qquad\text{(U5)}
```

The action constraint is used branch by branch. The input $`\tau_-`$ is a physical state of definite odd parity and requires no reference.

## Matching channel with an arbitrary reference

Take any deterministic allowed trajectory $`\Lambda`$ of action $`A`$. Prepend the [even Gaussian twirl](interacting_reset.md#2-an-even-gaussian-twirl-preserves-only-parity-information) $`\mathcal T_n`$. Its projectors are $`Q_\pm=(I\pm P)/2`$. For any system-reference state $`\rho_{SR}`$,

```math
\begin{aligned}
(\mathcal T_n\otimes\mathrm{id}_R)(\rho_{SR})
&=\tau_+\otimes R_++\tau_-\otimes R_-,\\
R_\pm&=\mathrm{Tr}_S[(Q_\pm\otimes I_R)\rho_{SR}(Q_\pm\otimes I_R)].
\end{aligned}
```

Here $`R_\pm\succeq0`$ and $`R_++R_-=\rho_R`$. The two positive operators may have different support and need not commute. The twirl costs no loss action and uses the permitted input-independent randomness.

Append occupation dephasing $`\mathcal D_{\rm occ}`$, implemented by independently choosing whether to apply $`\exp(i\pi c_j^\dagger c_j)`$ on each mode with probability $`1/2`$. These are even Gaussian pulses. Averaging kills each matrix element between unequal occupation strings and preserves $`\Pi_0`$ and its probability. Set $`\sigma_\pm=\mathcal D_{\rm occ}\Lambda(\tau_\pm)`$. Each $`\sigma_\pm`$ is diagonal in the occupation basis, so

```math
\frac12\lVert \sigma_\pm-\Pi_0\rVert_1=1-\mathrm{Tr}[\Pi_0\Lambda(\tau_\pm)].
```

The composed channel $`\widetilde\Lambda=\mathcal D_{\rm occ}\Lambda\mathcal T_n`$ satisfies

```math
\begin{aligned}
\frac12\lVert (\widetilde\Lambda\otimes\mathrm{id}_R)(\rho_{SR})
-\Pi_0\otimes\rho_R\rVert_1
&\leq\sum_{s\in\{+,-\}}\mathrm{Tr}(R_s)\,
        [1-\mathrm{Tr}(\Pi_0\Lambda(\tau_s))]\\
&\leq 1-\mathrm{Tr}[\Pi_0\Lambda(\tau_-)] .
\end{aligned}
\qquad\text{(U6)}
```

The last inequality uses (U4) and the sum of the two reference weights being one. The input $`\tau_-`$ attains this bound, so a reference cannot increase the error of the composed channel. Taking the supremum of the mixed-input vacuum probability over $`\Lambda`$ proves (U1), even if that supremum is only approached.

## Gaussian attainment and endpoints

The [Gaussian state theorem](gaussian_bound.md#6-exact-fidelity-bound) gives

```math
F_{\rm G}(n,A)=\left(1-\tfrac12e^{-A/n}\right)^n.
```

Its maximizing trajectory exposes each mode to equal action $`A/n`$, routing the modes through the one vacuum port in sequence. On $`\tau_n`$, this leaves independent occupations of probability $`e^{-A/n}/2`$, establishing saturation of the vacuum probability. Prepending the parity twirl and appending occupation dephasing as above attains (U2) uniformly over all inputs and references. The theorem optimizes the averaged channel under the stated random-control resource.

At $`A=0`$ both classes have error one, because an odd state remains in the odd sector. At positive finite action the Gaussian error strictly decreases, and tends to zero as $`A\to\infty`$. For $`0<\epsilon<1`$ the exact Gaussian action threshold is the unique finite positive solution of $`r_{\rm G}(n,A)=\epsilon`$.

For one and two modes, the two control classes have the same frontier:

```math
r_{\rm I}(1,A)=r_{\rm G}(1,A)=e^{-A},\qquad
r_{\rm I}(2,A)=r_{\rm G}(2,A)=e^{-A/2}.
```

For one mode, each parity sector is one-dimensional. For two modes, the six quadratic Majorana generators are traceless on each two-dimensional parity block: their Hilbert–Schmidt traces against $`I`$ and $`P`$ vanish. They are linearly independent and span all pairs of traceless anti-Hermitian operators on the two blocks. Gaussian controls therefore realize arbitrary determinant-one rotations independently on those blocks. Each remaining block phase acts trivially on a parity-block-diagonal state under conjugation. The state $`\tau_n`$ is block diagonal, and coherent even controls and the loss segments preserve that property. Thus interacting controls offer no additional mixed-input trajectories on these small registers at the same action. Equation (U1) lifts the equality to both channel frontiers.
