---
layout: proof
title: "Cauchy Criterion for Uniform Convergence"
chapter: "Sequences of Functions"
---

**Theorem:** A sequence of functions $(f_n)$ with $f_n : A \to \mathbb{R}$ converges [uniformly](../D/uniform-convergence) on $A$ if and only if for every $\varepsilon > 0$ there exists $N \in \mathbb{N}$ such that for all $x \in A$:

$$m, n > N \implies \lvert f_m(x) - f_n(x) \rvert < \varepsilon$$

**Proof:**

**($\Rightarrow$)** Suppose $f_n \to f$ uniformly on $A$. Let $\varepsilon > 0$. There exists $N \in \mathbb{N}$ such that for all $x \in A$:

$$n > N \implies \lvert f_n(x) - f(x) \rvert < \frac{\varepsilon}{2}$$

For all $m, n > N$ and all $x \in A$, the [triangle inequality](../D/absolute-value) gives:

$$\lvert f_m(x) - f_n(x) \rvert \leq \lvert f_m(x) - f(x) \rvert + \lvert f_n(x) - f(x) \rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

**($\Leftarrow$)** Suppose the Cauchy condition holds. For each fixed $x \in A$, the sequence $(f_n(x))$ is a [Cauchy sequence](../D/cauchy-sequence) in $\mathbb{R}$ and therefore converges by the [Cauchy criterion](../T/cauchy-criterion). Define $f(x) = \lim_{n \to \infty} f_n(x)$, so $f_n \to f$ pointwise.

It remains to show the convergence is uniform. Let $\varepsilon > 0$ and choose $N$ from the Cauchy condition. For all $n > N$ and all $x \in A$, fix $m > N$ and take the limit as $m \to \infty$ in:

$$\lvert f_m(x) - f_n(x) \rvert < \varepsilon$$

Since $f_m(x) \to f(x)$:

$$\lvert f(x) - f_n(x) \rvert \leq \varepsilon$$

Since this holds for all $x \in A$, $f_n \to f$ uniformly on $A$.