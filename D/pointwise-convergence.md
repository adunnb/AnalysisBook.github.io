---
layout: definition
title: "Pointwise Convergence"
chapter: "Sequences of Functions"
---

**Definition:** Let $(f_n)$ be a sequence of functions $f_n : A \to \mathbb{R}$. We say $(f_n)$ **converges pointwise** to a function $f : A \to \mathbb{R}$ if for every $x \in A$:

$$\lim_{n \to \infty} f_n(x) = f(x)$$

That is, for every $x \in A$ and every $\varepsilon > 0$, there exists $N \in \mathbb{N}$ (depending on both $\varepsilon$ and $x$) such that:

$$n > N \implies \lvert f_n(x) - f(x) \rvert < \varepsilon$$

We write $f_n \to f$ pointwise on $A$.

**Remark:** The key feature of pointwise convergence is that $N$ may depend on the point $x$. At different points in $A$, the sequence may converge at very different rates. This makes pointwise convergence a relatively weak notion, and it fails to preserve many properties like continuity and integrability.