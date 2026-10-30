# A deterministic protocol for finite registers

The fixed-parameter construction in [interacting reset](interacting_reset.md) makes the linear scaling transparent. Its numerical prefactor is intentionally loose. A threshold depending on the current active size gives better explicit action bounds while using exactly the same allowed operations.

The rule below depends only on $`n`$, the desired error $`\epsilon`$, and a chosen constant loss survival $`q`$. It never observes the input or a bath record. Every random branch therefore has exactly the same sequence of sizes and damping exposures.

## 1. Choose the next active block

Fix $`q\in(0,1)`$ and put $`p=q/2`$. For the current active size $`m`$, define

```math
\delta_m=\frac{\epsilon}{4m(m+1)},\qquad
k_m=\left\lceil pm+\sqrt{\frac m2\ln\frac1{\delta_m}}\right\rceil,
\qquad r_m=\frac{k_m}{m}.
```

If $`r_m\lt 1/2`$, propose the trash size

```math
m'=\left\lceil m h_2(r_m)\right\rceil+2,
\qquad
h_2(r)=-r\log_2r-(1-r)\log_2(1-r).
```

The extra two modes provide more capacity than the one extra mode sufficient in the compression lemma. Perform a stage only when

```math
r_m\lt \frac12,\qquad m'\lt m,\qquad \frac{q^m}{2}\leq\delta_m.
```

At a stage, twirl the active block by even Gaussian unitaries, give each mode loss survival $`q`$, and use a parity-preserving permutation to put every occupation string of weight at most $`k_m`$ into a zero prefix and the $`m'`$ trash modes. Freeze the prefix and repeat on the trash. If a stage condition fails, proceed to final cleanup.

## 2. Global error certificate

For $`X\sim\mathrm{Binomial}(m,p)`$, the chosen threshold gives

```math
\Pr(X\gt k_m)
\leq\exp[-2m(r_m-p)^2]
\leq\delta_m.
```

The parity/reference residue from the twirl followed by loss is at most $`q^m/2\leq\delta_m`$. The [one-stage lemma](interacting_reset.md) therefore gives error at most $`2\delta_m`$. All active sizes are distinct positive integers, so

```math
\sum_{\rm stages}2\delta_m
\leq\frac\epsilon2\sum_{m=1}^{\infty}\frac1{m(m+1)}
=\frac\epsilon2.
```

If $`m_f`$ modes remain, twirl that block and damp every mode with survival

```math
q_f=\frac{\epsilon}{2m_f}.
```

Its reset error is at most $`m_fq_f=\epsilon/2`$, including references. Contractivity and the stage induction prove that the complete channel has half-diamond error at most $`\epsilon`$. The action is explicitly

```math
A_{\rm comp}(n,\epsilon;q)
=\ln(1/q)\sum_{\rm stages}m
+m_f\ln\frac{2m_f}{\epsilon}.
```

The interacting class also contains the Gaussian universal protocol, so the smaller of this bound and $`n\ln(n/\epsilon)`$ is always an achievable interacting upper bound.

## 3. A smaller asymptotic coefficient

At fixed $`q`$ and $`\epsilon`$, as $`m\to\infty`$,

```math
r_m=p+O\!\left(\sqrt{\frac{\ln m}{m}}\right),\qquad
\frac{m'}m\longrightarrow h_2(p)\lt 1.
```

All three stage conditions hold for sufficiently large $`m`$. For every $`\eta\gt 0`$ with $`h_2(p)+\eta\lt 1`$, the large stages contract by at least that fixed factor. The remaining small sizes and final cleanup contribute a finite term depending on $`\epsilon,q,\eta`$, but not on the original $`n`$. Summing the large geometric series gives

```math
\limsup_{n\to\infty}\frac{A_{\rm comp}(n,\epsilon;q)}n
\leq\frac{\ln(1/q)}{1-h_2(q/2)}.
```

To justify the limit, first take the limsup with fixed $`\eta`$, obtaining the denominator $`1-h_2(p)-\eta`$, and only then let $`\eta`$ decrease to zero. This is an attainable coefficient for this construction, not a converse or an optimum over interacting protocols. The lower bound remains $`\ln2`$ at leading order.

The examples use $`q=1/5`$. Thus the asymptotic achievable coefficient is $`\ln5/[1-h_2(1/10)]`$, about $`3.03`$. Threshold rounding and the cleanup block are included in every finite-size evaluation; the asymptotic coefficient is not substituted for a finite-register bound.

## 4. Reproduction and interpretation

Run:

```bash
python verification/finite_protocol.py
python verification/plot_action_scaling.py
```

The first command records all integer thresholds, active sizes, stage exposures and analytical error bounds in [finite_protocol.json](../verification/results/finite_protocol.json). The second generates the figure and the numerical table linked in the [verification guide](../verification/README.md). These are floating-point evaluations of an analytical construction, with explicit inequality checks; they are not an interval-arithmetic proof or a search for the optimal interacting controller.

The plotted Gaussian lower curve is already necessary on the maximally mixed witness. The Gaussian upper curve guarantees universal reset. The interacting upper curve is a concrete universal protocol. Wherever the latter lies below the Gaussian lower curve, these explicit finite-register bounds certify an advantage under the common action accounting. Its magnitude is not a gate-duration or energy-saving claim.
