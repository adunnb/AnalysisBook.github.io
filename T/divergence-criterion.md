---
layout: proof
title: "Divergence Criterion"
chapter: "Sequences and Series"
---

**Theorem:** A sequence $(a_n)$ diverges if and only if there exists some $\varepsilon_0 > 0$ such that for every $N \in \mathbb{N}$, there exists $n > N$ with:

$$\lvert a_n - L \rvert \geq \varepsilon_0$$

for every $L \in \mathbb{R}$.

**Remark:** This is simply the negation of the [definition of convergence](../D/convergence-sequence). It is particularly useful for proving that specific sequences diverge without needing to know what limit they might converge to.

**Proof:** This follows directly by negating the definition of convergence. A sequence $(a_n)$ converges to $L$ if:

$$\forall \varepsilon > 0, \ \exists N \in \mathbb{N} \text{ such that } n > N \implies \lvert a_n - L \rvert < \varepsilon$$

Negating this statement gives: there exists $\varepsilon_0 > 0$ such that for every $N \in \mathbb{N}$, there exists $n > N$ with $\lvert a_n - L \rvert \geq \varepsilon_0$. Since this holds for every $L \in \mathbb{R}$, the sequence diverges.

**Example:** The sequence $a_n = (-1)^n$ diverges. To see this, suppose for contradiction that $a_n \to L$. Taking $\varepsilon_0 = 1$, for any $N$ we can find consecutive terms $a_n = 1$ and $a_{n+1} = -1$ beyond $N$. Then:

$$2 = \lvert 1 - (-1) \rvert = \lvert a_n - a_{n+1} \rvert \leq \lvert a_n - L \rvert + \lvert a_{n+1} - L \rvert < 1 + 1 = 2$$

a contradiction.