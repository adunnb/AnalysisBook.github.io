---
layout: proof
title: "Uniform Continuity Theorem"
chapter: "Limits and Continuity"
---

**Theorem:** If $f : [a, b] \to \mathbb{R}$ is [continuous](../D/continuity) on a closed bounded interval $[a, b]$, then $f$ is [uniformly continuous](../D/uniform-continuity) on $[a, b]$.

**Remark:** This theorem shows that on a closed bounded interval, continuity and uniform continuity coincide. The closed and bounded hypotheses are both necessary; $f(x) = x^2$ is continuous but not uniformly continuous on $\mathbb{R}$, and $f(x) = \frac{1}{x}$ is continuous but not uniformly continuous on $(0, 1]$.

**Proof:** Suppose for contradiction that $f$ is not uniformly continuous on $[a,b]$. Then there exists $\varepsilon_0 > 0$ such that for every $\delta > 0$ there exist $x, y \in [a,b]$ with $\lvert x - y \rvert < \delta$ but $\lvert f(x) - f(y) \rvert \geq \varepsilon_0$.

Taking $\delta = \frac{1}{n}$ for each $n \in \mathbb{N}$, we obtain sequences $(x_n)$ and $(y_n)$ in $[a,b]$ with:

$$\lvert x_n - y_n \rvert < \frac{1}{n} \quad \text{and} \quad \lvert f(x_n) - f(y_n) \rvert \geq \varepsilon_0$$

Since $(x_n) \subseteq [a,b]$ is bounded, by [Bolzano–Weierstrass](../T/bolzano-weierstrass) there exists a subsequence $x_{n_k} \to c \in [a,b]$. Since $\lvert x_{n_k} - y_{n_k} \rvert < \frac{1}{n_k} \to 0$, we also have $y_{n_k} \to c$.

Since $f$ is continuous at $c$:

$$f(x_{n_k}) \to f(c) \quad \text{and} \quad f(y_{n_k}) \to f(c)$$

Therefore $\lvert f(x_{n_k}) - f(y_{n_k}) \rvert \to 0$, contradicting $\lvert f(x_n) - f(y_n) \rvert \geq \varepsilon_0$.