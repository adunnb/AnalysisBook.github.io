---
layout: definition
title: "Uniform Convergence"
chapter: "Sequences of Functions"
---

**Definition:** Let $(f_n)$ be a sequence of functions $f_n : A \to \mathbb{R}$. We say $(f_n)$ **converges uniformly** to a function $f : A \to \mathbb{R}$ on $A$ if for every $\varepsilon > 0$ there exists $N \in \mathbb{N}$ such that for all $x \in A$:

$$n > N \implies \lvert f_n(x) - f(x) \rvert < \varepsilon$$

We write $f_n \to f$ uniformly on $A$.

**Remark:** The crucial difference from [pointwise convergence](../D/pointwise-convergence) is that $N$ depends only on $\varepsilon$ and not on $x$. A single $N$ works simultaneously for all points in $A$. Uniform convergence is a much stronger condition than pointwise convergence and is precisely the condition needed to preserve continuity, integrability, and differentiability in the limit.

**Example:** The sequence $f_n(x) = x^n$ on $[0, 1]$ converges pointwise to:

$$f(x) = \begin{cases} 0 & \text{if } x \in [0, 1) \\ 1 & \text{if } x = 1 \end{cases}$$

but not uniformly, since each $f_n$ is continuous but the pointwise limit is not.