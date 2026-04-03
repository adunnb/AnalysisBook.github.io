---
layout: definition
title: "Convergence of a Sequence"
chapter: "Sequences"
---

**Definition:** A sequence $(a_n)$ of real numbers **converges** to a limit $L \in \mathbb{R}$ if:

$$\forall \varepsilon > 0, \ \exists N \in \mathbb{N} \text{ such that } n > N \implies |a_n - L| < \varepsilon$$

We write $a_n \to L$ or $\displaystyle\lim_{n \to \infty} a_n = L$.

**Intuition:** No matter how small a "tolerance band" $\varepsilon$ you draw around $L$,
there is always a point in the sequence after which every term thereafter 
falls inside that band and stays there forever.