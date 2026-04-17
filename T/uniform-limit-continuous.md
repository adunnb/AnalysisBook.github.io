---
layout: proof
title: "Continuity of Uniform Limits"
chapter: "Sequences of Functions"
---

**Theorem:** Let $(f_n)$ be a sequence of [continuous](../D/continuity) functions $f_n : A \to \mathbb{R}$. If $f_n \to f$ [uniformly](../D/uniform-convergence) on $A$, then $f$ is continuous on $A$.

**Remark:** This theorem fails for pointwise convergence, as shown by the example $f_n(x) = x^n$ on $[0,1]$ in the definition of [uniform convergence](../D/uniform-convergence). Uniform convergence is precisely the condition needed to guarantee that the limit of continuous functions is continuous.

**Proof:** Let $c \in A$ and $\varepsilon > 0$. Since $f_n \to f$ uniformly, there exists $N$ such that for all $x \in A$:

$$n > N \implies \lvert f_n(x) - f(x) \rvert < \frac{\varepsilon}{3}$$

Fix any $n > N$. Since $f_n$ is continuous at $c$, there exists $\delta > 0$ such that:

$$\lvert x - c \rvert < \delta \implies \lvert f_n(x) - f_n(c) \rvert < \frac{\varepsilon}{3}$$

For all $x \in A$ with $\lvert x - c \rvert < \delta$, the [triangle inequality](../D/absolute-value) gives:

$$\lvert f(x) - f(c) \rvert \leq \lvert f(x) - f_n(x) \rvert + \lvert f_n(x) - f_n(c) \rvert + \lvert f_n(c) - f(c) \rvert < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon$$

Therefore $f$ is continuous at $c$.