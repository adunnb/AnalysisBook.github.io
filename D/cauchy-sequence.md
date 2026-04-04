---
layout: definition
title: "Cauchy Sequence"
chapter: "Sequences and Series"
---

**Definition:** A sequence $(a_n)$ of real numbers is a **Cauchy sequence** if for every $\varepsilon > 0$ there exists $N \in \mathbb{N}$ such that:

$$m, n > N \implies \lvert a_m - a_n \rvert < \varepsilon$$

**Intuition:** A Cauchy sequence is one whose terms become arbitrarily close to *each other* as the sequence progresses. Notice that $m, n$ are not specified to be consecutive, you can actually choose *any* pair from the sequence. The key insight is that this definition makes no reference to a limit, making it useful for proving convergence without knowing the limit in advance.