# Interacting reset at variable accuracy

A single vacuum-loss port can reset an entire fermionic register with damping action linear in the number of modes and in the logarithm of the required accuracy. The controller arranges losses as directed transitions between occupation states. The schedules below use finite contacts and predetermined parity-preserving permutations.

Let $`\epsilon_{\rm I}^*(n,A)`$ be the optimal error denoted by $`r_{\rm I}(n,A)`$ in the [universal frontier](universal-frontier.md), namely the infimum of the half-diamond reset error over the interacting class in the [model](model.md), at pathwise action cap $`A`$. The target is vacuum replacement on all $`n`$ modes, with arbitrary inputs and arbitrary external references. Let $`A_{\rm I}(n,\epsilon)`$ be the infimal cap at error at most $`\epsilon`$. For $`n\ge 2`$ and $`0<\epsilon\le 1/2`$,

```math
A_{\rm I}(n,\epsilon)=\Theta\!\left(n+\ln\frac1\epsilon\right),
```

with absolute constants. For every fixed $`n\ge2`$,

```math
\lim_{A\to\infty}-\frac{1}{A}\ln\epsilon_{\rm I}^*(n,A)=\frac12.
```

The [exact Gaussian frontier](universal-frontier.md) gives action of order $`n\ln(n/\epsilon)`$ in the joint regime and exponent $`1/n`$ at fixed $`n\ge2`$. The fixed-size exponents therefore separate the classes at every $`n\ge3`$.

## 1. Which transitions one port can implement

For $`n\ge2`$, each occupation-parity sector contains $`m=2^{n-1}`$ states. The loss $`\mathcal D[c_1]`$ pairs every occupied-port state with the corresponding empty-port state, with the other occupations held fixed. Each pair has one even and one odd state. Exactly $`m/2`$ of the donors are even and exactly $`m/2`$ are odd, since the other $`n-1`$ occupations have equally many even and odd strings.

Call a directed perfect matching on the occupation states *balanced* when its edges join opposite parities and it has $`m/2`$ donors of each parity. Every such matching is realized on diagonal states by a parity-preserving permutation, one contact with the physical port, and the inverse permutation. Indeed, pair each desired edge with a physical edge having the same donor parity. The induced endpoint bijections within each sector define a parity-preserving unitary. Jordan–Wigner signs on physical transitions cancel on diagonal blocks.

For contact action $`a`$, an edge $`s\to t`$ updates its donor and recipient blocks by

```math
\sigma_s\longmapsto e^{-a}\sigma_s,\qquad
\sigma_t\longmapsto\sigma_t+(1-e^{-a})\sigma_s.
```

Here the blocks may be positive operators on an external reference. Prepend a finite Gaussian occupation dephasing by averaging the independent mode sign rotations $`\exp(i\pi c_j^\dagger c_j)`$. The input then has the form $`\sum_x |x\rangle\langle x|\otimes\sigma_x`$, with $`\sum_x\sigma_x=\rho_R`$. Writing $`p(x)$` for the probability that the ensuing classical schedule ends at vacuum given initial occupation $`x`$, the half-trace error of this input is

```math
\operatorname{Tr}\!\left(\sum_x (1-p(x))\sigma_x\right).
```

In fact, the error matrix has positive blocks at all nonvacuum states, and its vacuum block is minus their sum. Consequently a uniform upper bound on the classical failure probabilities is a half-diamond bound. For a schedule preceded instead by the [even Gaussian parity twirl](universal-frontier.md), only the two uniform sector inputs need be compared. The odd one has the larger failure probability by the parity decay identity. Its output is already diagonal under the schedules considered here.

## 2. Finite schedules with logarithmic graph depth

Take two identical complete-prefix $`b`$-ary trees for some integer $`b\ge2`$, each with $`m`$ vertices. A complete-prefix tree retains the first $`m`$ heap vertices in breadth-first order. Give a vertex in copy $`i\in\{0,1\}`$ parity equal to $`\mathrm{depth}+i`$ modulo two. Its twin is the corresponding vertex in the other copy. The twins have opposite parity, so the full vertex set admits a parity-respecting bijection to the occupation strings that sends the copy-zero root to vacuum. Define the rank of the vacuum to be zero and that of every other vertex to be its depth plus one. The maximum rank is at most

```math
r=1+\left\lceil\log_b m\right\rceil.
```

For a vertex at depth $`d\ge1`$, the complete prefix contains that vertex and the entire level of $`b^{d-1}`$ vertices immediately above it. Hence $`m>b^{d-1}`$, which gives the stated depth bound.

Use $`k=b+1`$ edge colors on each tree, with the same coloring in both copies. Color the child edges of each vertex with distinct colors that differ from the parent edge color. There are at most $`b`$ children, so this is possible. Orient each tree edge from child to parent. In a given color with $`h`$ edges per copy, the two copies together have $`h`$ donors of each parity. Complete the matching for that color by pairing all remaining vertices with their twins. There are $`m-2h`$ such twin pairs, an even number. Orient half of those pairs from odd to even and half from even to odd. When the roots are unpaired in the color, assign their edge from the odd root to vacuum. Then there are at least two unpaired twin pairs, and the required donor balance is possible. The total number of donors is $`h+(m-2h)/2=m/2`$ of each parity, as required for one port contact.

Every transfer lowers rank or keeps it constant, and the vacuum is absorbing. Run all $`k`$ colors once in a fixed order, giving action $`a`$ to each contact. If no rank decrease has occurred so far in the sweep, any earlier twin transfer kept the heap index unchanged. The two copies agree on the parent color at that index. At that contact a nonroot vertex therefore has probability $`p=1-e^{-a}`$ to take its parent edge. The odd root can move to vacuum on a color absent from the root's tree edges, which exists because the root has at most $`b`$ children. Thus, conditional on any history before a sweep, a nonvacuum state lowers rank with probability at least $`p`$.

This conditional bound gives a coupling to $`M`$ independent Bernoulli trials of parameter $`p`$. At each sweep, generate its rank-decrease indicator using a fresh uniform variable and the conditional probability given the previous history. If this variable is at most $`p`$, the rank decreases or the state is already at vacuum. After $`r`$ such successes, the state is at vacuum. Using the occupation dephasing from Section 1, the resulting protocol has

```math
A=kMa,\qquad
\epsilon_{\rm I}^*(n,kMa)\le\Pr\{\operatorname{Bin}(M,1-e^{-a})<r\}.
```

For instance, $`a=\ln 2`$ gives $`\mathbb E[2^{-\operatorname{Bin}(M,1/2)}]=(3/4)^M`$. The error is at most $`2^r(3/4)^M`$. With $`b=2`$, we can use $`r=n`$ and take

```math
M=\left\lceil\frac{n\ln 2+\ln(1/\epsilon)}{\ln(4/3)}\right\rceil,
\qquad A=3M\ln 2.
```

This schedule uses exactly $`3M`$ loss contacts. Its action bound holds for every random seed used in the initial dephasing.

### Fixed-error coefficient

For $`b=4`$, use $`k=5`$, $`r=1+\lceil(n-1)/2\rceil`$, and $`a=n^{-1/2}`$. At fixed $`0<\epsilon<1`$, choose

```math
M=\left\lceil\frac{r+C_\epsilon\sqrt r}{1-e^{-a}}\right\rceil
```

with $`C_\epsilon>1/\sqrt\epsilon`$. For large enough $`n`$, Chebyshev's inequality bounds the binomial lower-tail probability by $`\epsilon`$. Indeed, the variance is at most the mean, which is $`r+C_\epsilon\sqrt r+O(1)`$. Since $`a/(1-e^{-a})=1+O(a)`$, the action is at most $`(5/2)n+O_\epsilon(\sqrt n)`$, with $`O_\epsilon(n^{3/2})`$ port contacts. The coefficient $`5/2`$ is an achievable upper bound. The [entropy-compression schedule](finite_size.md) provides another finite construction to compare at any specified size and error.

## 3. Converse from no loss jumps

Take the initial maximally mixed odd state $`\tau_-=(I-P)/2^n`$, where $`P`$ is total parity. In the expansion of a deterministic Lindblad evolution into jump and no-jump terms, the latter has the form $`K\tau_-K^\dagger`$. Between instantaneous pulses the no-jump propagator is generated by

```math
-iH(t)-\tfrac12\kappa(t)c_1^\dagger c_1.
```

It preserves both parity sectors, as do the pulses. Denote its restriction to the odd sector by $`K_-`$. There the port occupation operator has rank and trace $`m/2`$, and Liouville's determinant formula gives

```math
|\det K_-|^2=\exp(-a m/2),\qquad a=\int\kappa(t)\,dt\le A.
```

Hamiltonian evolution and unitary pulses contribute only determinant phases. For a conjugated port the same formula holds because parity-preserving conjugation leaves the sector trace unchanged. Applying arithmetic–geometric mean to the eigenvalues of $`K_-^\dagger K_-`$ yields

```math
\operatorname{Tr}(K\tau_-K^\dagger)
=\frac1m\operatorname{Tr}(K_-^\dagger K_-)
\ge |\det K_-|^{2/m}
=e^{-a/2}.
```

The full output includes this positive term entirely in the odd sector. All other jump terms are positive, so measuring vacuum gives reset error at least $`e^{-A/2}`$. The expansion is a mathematical decomposition of the averaged channel. The controller observes no jump record. The bound holds for every seed with cap $`A`$, so averaging preserves it. Continuity extends the bound to limits of admitted protocols at uniform cap.

Together with the [spectral inflow bound](interacting_reset.md#7-a-lower-bound-for-arbitrary-coherent-control), this gives

```math
A_{\rm I}(n,\epsilon)\ge
\max\left\{n\ln 2+\ln(1-\epsilon),\ 2\ln(1/\epsilon)\right\}.
```

For $`n\ge2`$ and $`0<\epsilon\le1/2`$, the first term is at least $`(n/2)\ln 2`$. The finite tree schedule proves the matching joint order. At $`n=1`$, parity-preserving controls cannot mix the two one-dimensional sectors, and the occupied input survives with probability $`e^{-A}`$. Initial dephasing and one contact attain that error.

## 4. Two matchings attain the fixed-size exponent

Label the $`2m`$ cycle vertices $`0,\ldots,2m-1`$ with alternating parities, beginning with vacuum at $`0`$. Both paths of length $`m`$ from the even vertex $`m`$ to $`0`$ are oriented from $`m`$ toward $`0`$. Color the edges alternately with two colors. Each color is a directed perfect matching. On the path from vertex $`m`$ through vertex $`1`$, an edge with consecutive labels $`j,j+1`$ has donor $`j+1`$. On the other path, with labels taken modulo $`2m`$, the donor is $`j`$. Each path has $`m/2`$ edges of either color, and the same color has donors of opposite parity on the two paths. Both colors are therefore balanced and realizable with the same port.

Rank is the cycle distance to vacuum. Every transfer lowers rank by one, and each nonvacuum vertex has a downward edge among the two contacts. Prepend occupation dephasing and repeat both colors for $`M`$ sweeps with fixed action $`a>0`$ per contact. The preceding sweep argument gives

```math
\begin{aligned}
\epsilon_{\rm I}^*(n,2Ma)
&\le \Pr\{\operatorname{Bin}(M,1-e^{-a})<m\} \\
&= e^{-Ma}\sum_{j=0}^{m-1}\binom{M}{j}(e^a-1)^j.
\end{aligned}
```

The binomial coefficient is zero for $`j>M`$. At fixed $`n`$ and $`a`$, the sum is at most polynomial in $`M`$ of degree $`m-1`$. For a general cap $`A`$, choose $`M=\lfloor A/(2a)\rfloor`$, so the achievable error is $`O_{n,a}(A^{m-1}e^{-A/2})`$ as $`A\to\infty`$. The no-jump converse matches the exponent. The cycle depth grows exponentially with $`n`$, which is why the previous section uses the tree for a bound uniform in size and error.

### Exact three-mode separation at finite action

Use the even Gaussian parity twirl and the following two contacts, in order.

| Contact | Directed edges |
| --- | --- |
| First | $`1\to0,\ 3\to2,\ 4\to5,\ 6\to7`$ |
| Second | $`2\to1,\ 4\to3,\ 5\to6,\ 7\to0`$ |

Give each contact action $`\ln 2`$ and repeat this sweep 16 times. Acting on the uniform odd population, each contact sends half of each donor to its recipient. The final occupation weights, in order of vertex labels, have the following common-denominator representation:

```math
\frac{1}{2^{34}}
\big(17169645568,\ 4521984,\ 524288,\ 65536,\ 0,\ 65536,\ 1048576,\ 3997696\big).
```

These integers follow by starting with numerator one at each odd label over denominator four. At each contact, double the common denominator, keep each donor numerator, and replace each recipient numerator by twice its old value plus the old donor numerator. By the parity reduction, the uniform odd input is worst even with an arbitrary external reference. The exact half-diamond error of the protocol is $`39/65536`$. At the same action $`A=32\ln 2`$, the Gaussian frontier gives a strictly larger error:

```math
\frac{39}{65536}<1-(1-2^{-12})^3<\epsilon_{\rm G}^*(3,32\ln 2).
```

The second comparison uses $`e^{-A/3}/2>2^{-12}`$ in the Gaussian formula. The first compares rational numbers directly.

## 5. Resource scope

The graph vertices label occupation strings of the original register. Each matching uses the original single loss port, with no extra quantum carrier. The initial dephasing or parity twirl uses input-independent classical randomness, and the controller retains no random seed as part of the output. All loss action is charged pathwise. Each schedule is open loop and uses no measurements, bath feedback, postselection, or supplied pure modes. The model grants ideal-fast parity-preserving basis permutations. Their synthesis, locality, duration, and energetic cost are outside the action comparison.
