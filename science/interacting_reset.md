# Universal reset by parity-preserving entropy compression

[Model and resource contract](model.md) · [Finite-size choices](finite_size.md)

An interacting controller can reset the entire unknown register with dissipation action linear in its number of modes. The construction uses the same single vacuum-loss port as the Gaussian comparison, retains every system mode, and works for inputs entangled with an arbitrary reference. It creates a constant occupation bias, reversibly concentrates the remaining uncertainty into a smaller set of modes, and repeats.

Entropy concentration followed by bath-assisted cooling is established algorithmic cooling; see [Boykin et al.](https://arxiv.org/abs/quant-ph/0106093). Controllability with one switchable amplitude-damping qubit is established by [Bergholm, Wilhelm and Schulte-Herbrüggen](https://arxiv.org/pdf/1605.06473v2), including the sequential cooling benchmark in Example 1. The proof here supplies the parity-preserving, reference-uniform construction and counts its total loss action. Its role is to attain the linear side of the Gaussian-versus-interacting reset comparison.

## 1. The statement and its resources

The register contains $`n\ge1`$ fermionic modes, with a fixed occupation basis and vacuum

```math
|\Omega_n\rangle=|0\rangle^{\otimes n}.
```

The prescribed dissipative port is

```math
L(t)=\sqrt{\kappa(t)}\,c_1,\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\},
\qquad
A=\int\kappa(t)\,dt.
```

Thus a mode exposed to action $`a`$ has occupation survival probability $`q=e^{-a}`$. A Gaussian mode permutation, a loss interval on mode 1, and the inverse permutation implement loss on any chosen existing mode. The permutations do not add to $`A`$.

The controls permitted here are arbitrary fast parity-preserving unitaries and input-independent random even Gaussian unitaries. The classical random choices are unrecorded in the required output. The Gaussian comparison receives exactly the same randomization resource. No measurement, bath-record feedback, postselection, prepared quantum workspace, or discarded system output is used. Every random branch has the stated action bound.

For the vacuum replacement channel

```math
\mathcal R_n(X)=|\Omega_n\rangle\langle\Omega_n|\,\operatorname{Tr}X,
```

write

```math
d_{\rm reset}(\Phi)=\frac12\|\Phi-\mathcal R_n\|_\diamond.
```

It suffices to prove, for every system-reference state $`\rho_{SR}`$,

```math
\frac12\left\|
(\Phi\otimes\operatorname{id}_R)(\rho_{SR})
-
|\Omega_n\rangle\langle\Omega_n|\otimes\rho_R
\right\|_1
\le\epsilon.
\tag{I1}
```

The proof uses the ordinary tensor-product reference and allows arbitrary input coherences. A restriction to physical parity-compatible inputs and references only weakens this requirement.

### Theorem I: linear action for the interacting class

Fix $`0<\epsilon<1`$. Define

```math
h=h_2(1/4),\qquad
h_2(x)=-x\log_2x-(1-x)\log_2(1-x),\qquad
\alpha=\frac{1+h}{2}<1,
```

and

```math
M_\epsilon=
\max\left\{
24,\,
\left\lceil32\ln\frac{256}{\epsilon}\right\rceil
\right\}.
```

There is an allowed protocol satisfying $`d_{\rm reset}(\Phi)\le\epsilon`$, with

```math
A\le
\frac{\ln4}{1-\alpha}\,n+
M_\epsilon\ln\frac{2M_\epsilon}{\epsilon}.
\tag{I2}
```

Conversely, every allowed protocol with $`d_{\rm reset}(\Phi)\le\epsilon`$ and a pathwise action cap $`A`$ satisfies

```math
A\ge
\max\left\{0,\ n\ln2+\ln(1-\epsilon)\right\}.
\tag{I3}
```

Consequently, at fixed global error,

```math
A_{\mathrm I}(n,\epsilon)
=\Theta_\epsilon(n).
\tag{I4}
```

The constants in (I2) are chosen for a transparent finite proof. They are not optimal. The [finite-size construction](finite_size.md) chooses the compression threshold from the active block size and gives a smaller attainable asymptotic coefficient.

Only dissipation action is optimized. In particular, the basis permutations used for compression are existence constructions; this theorem does not bound their gate count, synthesis cost, locality, coherent-control energy, or duration.

## 2. An even Gaussian twirl preserves only parity information

Consider an active block of $`m\ge1`$ modes. Let $`w_1,\ldots,w_{2m}`$ be its Majorana operators, with

```math
w_j^\dagger=w_j,\qquad
\{w_j,w_k\}=2\delta_{jk}I.
```

For every even subset $`E\subseteq\{1,\ldots,2m\}`$, let $`W_E`$ be the ordered product of its Majoranas. An overall phase is irrelevant. The channel

```math
\mathcal T_m(X)=
\frac{1}{2^{2m-1}}
\sum_{\substack{E\subseteq\{1,\ldots,2m\}\\|E|\ {\rm even}}}
W_EXW_E^\dagger
\tag{I5}
```

is a mixture of even Gaussian unitaries. Indeed, each $`W_E`$ is a product of pair-Majorana rotations because

```math
w_jw_k=\exp\left(\frac{\pi}{2}w_jw_k\right),
\qquad j\ne k.
```

These are quadratic-unitary operations, and each commutes with the block parity

```math
P_m=\prod_{j=1}^m(1-2c_j^\dagger c_j).
```

The twirl has the exact form

```math
\mathcal T_m(X)
=\frac{I}{2^m}\operatorname{Tr}X
+\frac{P_m}{2^m}\operatorname{Tr}(P_mX).
\tag{I6}
```

To see this directly, expand $`X`$ in the orthogonal Majorana-monomial basis. Conjugating a monomial $`W_F`$ by an even monomial $`W_E`$ multiplies it by $`(-1)^{|E\cap F|}`$. Averaging this character over all even subsets gives zero unless $`F`$ is empty or contains all $`2m`$ indices. These two surviving monomials are $`I`$ and $`P_m`$, up to phase. Their squared Hilbert–Schmidt norms are $`2^m`$, which gives (I6). This also proves the claim for $`m=1`$.

Applying (I6) to the system factor of an arbitrary joint state gives

```math
(\mathcal T_m\otimes\operatorname{id}_R)(\rho_{AR})
=\frac{I_A}{2^m}\otimes\rho_R
+\frac{P_m}{2^m}\otimes\Delta_R,
\qquad
\Delta_R=\operatorname{Tr}_A[(P_m\otimes I_R)\rho_{AR}].
\tag{I7}
```

Let $`\Pi_\pm=(I\pm P_m)/2`$, and set

```math
\rho_R^\pm=
\operatorname{Tr}_A[
(\Pi_\pm\otimes I_R)\rho_{AR}(\Pi_\pm\otimes I_R)].
```

These operators are positive, $`\rho_R^++\rho_R^-=\rho_R`$, and

```math
\Delta_R=\rho_R^+-\rho_R^-,
\qquad
\|\Delta_R\|_1\le
\operatorname{Tr}\rho_R^++\operatorname{Tr}\rho_R^-=1.
\tag{I8}
```

Thus the surviving coefficient is Hermitian and uniformly bounded even when the input is entangled with $`R`$. The twirl removes within-sector information and cross-parity coherence, but it does not erase the difference between the two parity-sector reference states.

Equation (I7) describes the averaged channel. The classical twirl seed is not retained as an output. No claim of reference decoupling conditioned on that seed is needed or made.

## 3. Finite loss exposure suppresses the remaining parity term

Expose each active mode to the same action $`a>0`$, and write $`q=e^{-a}`$. Denote the resulting ordered composition of single-mode loss channels by $`\mathcal L_q^{(m)}`$. On the occupation-diagonal algebra, the order is immaterial and this composition is independent bit amplitude damping.

For completeness, a diagonal system-reference state can be written

```math
\omega_{AR}=\sum_{x\in\{0,1\}^m}|x\rangle\langle x|\otimes B_x,
\qquad B_x\ge0.
```

When a jump $`c_j`$ acts on $`|x\rangle`$, its Jordan–Wigner sign appears once in the ket and once in the bra. The signs cancel in $`c_j|x\rangle\langle x|c_j^\dagger`$. The anticommutator term is also diagonal. The resulting occupation transitions are precisely $`1\to0`$, with survival probability $`q`$, and no transition from $`0`$ to $`1`$.

For a single occupation bit,

```math
\operatorname{AD}_q(I/2)=\sigma_q
=\begin{pmatrix}1-q/2&0\\0&q/2\end{pmatrix},
\qquad
\operatorname{AD}_q(Z)=qZ.
```

Both terms in (I7) lie in this diagonal algebra. Therefore the exact joint output is

```math
(\mathcal L_q^{(m)}\mathcal T_m\otimes\operatorname{id}_R)(\rho_{AR})
=\sigma_q^{\otimes m}\otimes\rho_R
+\frac{q^mP_m}{2^m}\otimes\Delta_R.
\tag{I9}
```

Using $`\|P_m\|_1=2^m`$, its distance from the independent biased-block comparison state obeys

```math
D\!\left(
(\mathcal L_q^{(m)}\mathcal T_m\otimes\operatorname{id}_R)(\rho_{AR}),
\sigma_q^{\otimes m}\otimes\rho_R
\right)
\le\frac{q^m}{2},
\qquad
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
\tag{I10}
```

The loss action for this step is exactly $`ma=m\ln(1/q)`$. Routing all modes through one port realizes it without a second dissipative resource.

## 4. Reversible compression inside each parity sector

The following stage estimate allows size-dependent choices of the bias and threshold.

### Lemma I1: one compression stage

Choose $`0<q<1`$, put $`p=q/2`$, and choose $`p<r<1/2`$. Let

```math
m'=\lceil m h_2(r)\rceil+1
```

and suppose $`m'<m`$. There is a parity-preserving basis permutation $`U_{m,r}`$ such that, for every input $`\rho_{AR}`$, the channel

```math
\mathcal S_{m,q,r}
=\operatorname{Ad}_{U_{m,r}}\circ
\mathcal L_q^{(m)}\circ\mathcal T_m
```

has an output within distance

```math
e(m,q,r)
=e^{-2m(r-p)^2}+\frac{q^m}{2}
\tag{I11}
```

of a state

```math
|0\rangle\langle0|^{\otimes(m-m')}\otimes\eta_{A'R},
\qquad
\eta_R=\rho_R.
\tag{I12}
```

It uses action $`m\ln(1/q)`$. The permutation and exposure times depend on $`m,q,r`$, and not on the input or any measurement outcome.

#### Counting good strings

Let

```math
T_{m,r}
=\{x\in\{0,1\}^m:\ |x|\le\lfloor rm\rfloor\}.
```

Its cardinality obeys

```math
|T_{m,r}|
=\sum_{j=0}^{\lfloor rm\rfloor}\binom mj
\le2^{m h_2(r)}.
\tag{I13}
```

One proof uses the binomial distribution of parameter $`r`$. For every $`j\le rm`$, monotonicity in $`j`$ gives

```math
r^j(1-r)^{m-j}
\ge r^{rm}(1-r)^{m(1-r)}
=2^{-m h_2(r)}.
```

Multiplying by $`\binom mj`$ and summing over those $`j`$ proves (I13), since their binomial probabilities sum to at most one.

Each parity sector of $`m'`$ modes contains $`2^{m'-1}`$ occupation strings. By the definition of $`m'`$,

```math
2^{m'-1}\ge2^{m h_2(r)}\ge|T_{m,r}|.
\tag{I14}
```

There is consequently enough space to inject the even good strings into
$`|0\rangle^{\otimes(m-m')}\otimes|y\rangle`$ with even $`y`$, and independently inject the odd good strings into such outputs with odd $`y`$. Complete each injection to a bijection of its full $`m`$-mode parity sector. The resulting basis permutation is unitary, commutes with $`P_m`$, and maps every good string to a zero prefix.

The extra one trash mode in $`m'=\lceil m h_2(r)\rceil+1`$ supplies the separate capacity required in both parity sectors. This construction uses only the original active modes.

#### Probability of the excluded strings

In the comparison state $`\sigma_q^{\otimes m}`$, occupation bits are independent Bernoulli variables of parameter $`p`$. For $`X\sim\operatorname{Bin}(m,p)`$,

```math
\Pr[X>\lfloor rm\rfloor]
=\Pr[X>rm]
\le e^{-2m(r-p)^2}.
\tag{I15}
```

The last inequality is the bounded-variable concentration bound of [Hoeffding, Theorem 2](https://doi.org/10.1080/01621459.1963.10500830). The equality of the two events uses that $`X`$ is integer-valued.

#### Turning a probability bound into joint trace distance

Suppose a state is diagonal on a designated prefix $`B`$, with arbitrary positive operator-valued coefficients on all other systems:

```math
\theta_{BZ}=\sum_b|b\rangle\langle b|\otimes C_b,\qquad C_b\ge0.
```

Define the analytical prefix replacement map

```math
\mathcal Q_B(\theta_{BZ})
=|0\rangle\langle0|_B\otimes\operatorname{Tr}_B\theta_{BZ}.
```

The difference $`\theta-\mathcal Q_B(\theta)`$ has block
$`-\sum_{b\ne0}C_b`$ at $`b=0`$, and block $`C_b`$ at each $`b\ne0`$. Its blocks have definite sign, so

```math
D(\theta,\mathcal Q_B(\theta))
=\sum_{b\ne0}\operatorname{Tr}C_b
=\Pr_\theta[B\ne0].
\tag{I16}
```

This is an exact joint-state identity; no assumption that $`Z`$ is classical, independent, or unentangled is used.

Apply it to

```math
\theta_{AR}
=(U_{m,r}\sigma_q^{\otimes m}U_{m,r}^\dagger)\otimes\rho_R.
```

The probability of a nonzero cold prefix is at most the excluded probability in (I15), because every good string was sent to a zero prefix. Equation (I10), unitary invariance of trace distance, and the triangle inequality then give

```math
D\!\left(
(\mathcal S_{m,q,r}\otimes\operatorname{id}_R)(\rho_{AR}),
\mathcal Q_B(\theta_{AR})
\right)
\le\frac{q^m}{2}+e^{-2m(r-p)^2}.
```

The comparison state $`\mathcal Q_B(\theta)`$ has the form (I12) and preserves $`\rho_R`$. This proves the lemma. The map $`\mathcal Q_B`$ is used only to compare states in the proof; it is not a physical operation supplied to the protocol.

## 5. Repeating the stage without losing the reference guarantee

Specialize Lemma I1 to

```math
q=\frac14,\qquad
p=\frac18,\qquad
r=\frac14,\qquad
m'=\lceil hm\rceil+1.
```

Each stage costs $`m\ln4`$ and incurs at most

```math
e_m=e^{-m/32}+\frac{4^{-m}}2.
\tag{I17}
```

If $`m\ge24`$, then

```math
m'\le hm+2\le\alpha m<m.
\tag{I18}
```

For the middle inequality it is enough that $`m\ge4/(1-h)`$. The exact value $`h=2-\tfrac34\log_2 3<5/6`$ shows that $`m\ge24`$ suffices.

Set $`m_0=n`$. While $`m_j\ge M_\epsilon`$, apply the stage to the active block and set

```math
m_{j+1}=\lceil hm_j\rceil+1.
\tag{I19}
```

Freeze its zero-prefix comparison modes and continue only on the remaining $`m_{j+1}`$ modes. All sizes, stopping decisions and dwell times are fixed before execution from $`n,\epsilon`$. No observed outcome changes the schedule.

### Why a fermionic suffix is legitimate

Choose an ordering in which already frozen modes form a prefix $`F`$, and active modes form a suffix $`A`$. On this tensor representation an active loss operator can have the form

```math
c_j=P_F\otimes\widetilde c_j.
```

An even unitary on $`A`$ acts as the identity on $`F`$. On the ideal frozen state $`|0\rangle_F`$, the parity string has eigenvalue $`+1`$; hence the actual loss channel acts exactly as the desired active-block channel on
$`|0\rangle\langle0|_F\otimes\eta_{AR}`$.

This argument does not assume tensor-local loss on an arbitrary uncooled prefix. Apply the same physical CPTP channel to the real state and the ideal comparison state; their distance cannot increase. A fixed Gaussian relabeling that puts the active block first gives an equivalent description. Routing through mode 1 and undoing that routing implements the same selected-mode loss channel.

### Induction for the accumulated error

Suppose that after $`j`$ stages the real joint state is within $`E_j`$ of

```math
\widehat\rho_j
=|0\rangle\langle0|^{\otimes(n-m_j)}\otimes\eta_{A_jR},
\qquad \eta_R=\rho_R.
```

The next physical stage contracts the previous error. On $`\widehat\rho_j`$, the active-block calculation is exact by the preceding parity-string argument. Lemma I1 supplies a new ideal state with $`n-m_{j+1}`$ zero comparison modes, unchanged reference marginal, and additional error at most $`e_{m_j}`$. Therefore

```math
E_{j+1}\le E_j+e_{m_j},
\qquad E_0=0.
\tag{I20}
```

The induction permits arbitrary correlations between the active block and the reference. Already compressed modes are retained in the output and are not used as an additional pure computational workspace. Their replacement by exact zeros occurs only in the comparison state.

## 6. Finite error, final cleanup and action

### The sum of stage errors

The active sizes decrease strictly, so each integer at least $`M_\epsilon`$ occurs at most once. Equations (I17)–(I20) give

```math
E_{\rm stages}
\le
\sum_{m=M_\epsilon}^{\infty}
\left(e^{-m/32}+\frac{4^{-m}}2\right)
=
\frac{e^{-M_\epsilon/32}}{1-e^{-1/32}}
+\frac23\,4^{-M_\epsilon}.
\tag{I21}
```

The choice of $`M_\epsilon`$ implies $`e^{-M_\epsilon/32}\le\epsilon/256`$. Also $`e^{1/32}\ge33/32`$, so
$`(1-e^{-1/32})^{-1}\le33`$. Since $`\ln4>1/32`$, one has $`4^{-M_\epsilon}\le e^{-M_\epsilon/32}`$. Thus

```math
E_{\rm stages}
\le\frac{33\epsilon}{256}+\frac{\epsilon}{384}
=\frac{101}{768}\epsilon
<\frac{\epsilon}{2}.
\tag{I22}
```

All constants here are analytical, including the floors and ceilings in the schedule.

### Cleanup of the last active block

The process terminates at an active size $`m_f<M_\epsilon`$. Twirl this remaining block and expose each of its modes to survival probability

```math
q_f=\frac{\epsilon}{2M_\epsilon}.
```

The twirled state is diagonal on the active modes, with positive operator-valued reference coefficients. For any occupation string, the probability of at least one surviving excitation is at most $`m_fq_f`$, by a union bound over its occupied positions. Averaging over the reference coefficients preserves this inequality. The exact probability-to-distance identity (I16), now with the entire active block as $`B`$, gives

```math
D\!\left(
\omega_{A_fR},
|\Omega_{m_f}\rangle\langle\Omega_{m_f}|\otimes\rho_R
\right)
\le m_fq_f
\le\frac{\epsilon}{2}.
\tag{I23}
```

The same contraction argument handles the previously accumulated error on the frozen modes. Equations (I22) and (I23) prove (I1) for every reference.

If $`n<M_\epsilon`$, no compression stage is run: this final twirl-and-loss protocol alone supplies the claimed guarantee. The construction therefore covers every $`n\ge1`$, not only the asymptotic regime.

### Pathwise action accounting

Equation (I18) implies $`m_j\le\alpha^j n`$, and hence

```math
A_{\rm stages}
=(\ln4)\sum_jm_j
\le\frac{\ln4}{1-\alpha}\,n.
\tag{I24}
```

The last block costs

```math
A_{\rm final}
=m_f\ln\frac1{q_f}
\le M_\epsilon\ln\frac{2M_\epsilon}{\epsilon}.
\tag{I25}
```

This proves (I2). The random twirl choices change neither the $`m_j`$, the compression permutations nor the dwell times. Every branch consequently obeys the same bound; an expected-action budget is not being substituted for a strict cap.

## 7. A lower bound for arbitrary coherent control

The lower bound uses only the largest eigenvalue and the normalized loss strength. It does not require the evolving state or the Hamiltonian to be Gaussian. Eigenvalue-based fast-control reductions are established in quantum control; see [Malvetti, Secs. II–III](https://arxiv.org/pdf/2403.05285). The short bound needed here is proved explicitly.

Let $`\rho(t)`$ obey

```math
\dot\rho=-i[H(t),\rho]
+\kappa(t)\left(
c_1\rho c_1^\dagger-\frac12\{c_1^\dagger c_1,\rho\}
\right),
```

and set $`\lambda(t)=\lambda_{\max}(\rho(t))`$. At a differentiability point, the upper directional derivative of the largest eigenvalue is the maximum of
$`\langle v|\dot\rho|v\rangle`$ over unit vectors in its top eigenspace. This form also covers an eigenvalue crossing; one must not select an arbitrary smooth eigenvector branch there.

For every such vector, $`\rho v=\lambda v`$, so the Hamiltonian contribution vanishes. Moreover $`\rho\le\lambda I`$, which implies

```math
\begin{aligned}
\langle v|\dot\rho|v\rangle
&=
\kappa\langle v|c_1\rho c_1^\dagger|v\rangle
-\kappa\lambda\langle v|c_1^\dagger c_1|v\rangle\\
&\le
\kappa\lambda\langle v|
(c_1c_1^\dagger-c_1^\dagger c_1)|v\rangle\\
&=
\kappa\lambda\langle v|(I-2c_1^\dagger c_1)|v\rangle
\le\kappa\lambda .
\end{aligned}
\tag{I26}
```

Thus the upper Dini derivative obeys $`D^+\lambda\le\kappa\lambda`$ on differentiable dynamical segments. For locally integrable coefficients, $`\rho`$ and its largest eigenvalue are absolutely continuous, the inequality holds almost everywhere, and integration gives

```math
\lambda_{\max}(\rho(T))
\le e^A\lambda_{\max}(\rho(0)).
\tag{I27}
```

Instantaneous unitary pulses preserve $`\lambda_{\max}`$, so they do not alter the bound. The argument also persists under limits of piecewise controls. In particular it allows arbitrary parity-preserving coherent interactions, and even remains valid if that coherent restriction is removed.

For a randomized protocol, condition on its complete input-independent classical seed. Each branch starts from the same initial state and has action at most $`A`$. Since $`\lambda_{\max}`$ is convex, averaging the final branch states preserves (I27).

Use the maximally mixed input $`\rho(0)=I/2^n`$. Then

```math
\langle\Omega_n|\Phi(I/2^n)|\Omega_n\rangle
\le\lambda_{\max}(\Phi(I/2^n))
\le2^{-n}e^A.
\tag{I28}
```

If $`d_{\rm reset}(\Phi)\le\epsilon`$, the vacuum measurement on this particular input must succeed with probability at least $`1-\epsilon`$. Therefore
$`1-\epsilon\le2^{-n}e^A`$, which proves (I3). This lower bound uses a system-only witness; the reference-uniform upper bound is what completes the stronger reset task.

## 8. Gaussian universal upper bound

The same twirl also gives a simple universal protocol using only Gaussian controls. Twirl the entire $`n`$-mode input and expose every mode equally with survival probability $`q`$. Equation (I9) gives, for arbitrary $`\rho_{SR}`$,

```math
\omega_{SR}
=\sigma_q^{\otimes n}\otimes\rho_R
+\frac{q^nP_n}{2^n}\otimes\Delta_R.
```

Its distance to vacuum replacement is bounded by

```math
\begin{aligned}
D(\omega_{SR},
|\Omega_n\rangle\langle\Omega_n|\otimes\rho_R)
&\le
1-(1-q/2)^n+\frac{q^n}{2}\\
&\le\frac{nq}{2}+\frac{q^n}{2}
\le nq .
\end{aligned}
\tag{I29}
```

Choose $`q=\epsilon/n`$, which lies in $`(0,1)`$. The resulting Gaussian protocol has

```math
d_{\rm reset}(\Phi_{\rm G})\le\epsilon,
\qquad
A_{\rm G}\le n\ln\frac n\epsilon.
\tag{I30}
```

Every conditioned branch is Gaussian. The average of those branches need not send a Gaussian input to a Gaussian state, which is why the model specifies mixtures of Gaussian control protocols explicitly.

Equation (I30) is an attainable universal-channel bound. It is not an assertion that this channel is the exact finite-action universal Gaussian optimum. Together with the separately proved maximally mixed-input Gaussian converse, it gives the matching $`\Theta_\epsilon(n\log n)`$ universal action order. Equations (I2)–(I4) show how parity-preserving interacting control removes that logarithmic factor under the same loss and randomization resources.
