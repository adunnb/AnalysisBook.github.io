---
layout: proof
title: "Monotone Convergence Theorem"
chapter: "Sequences and Series"
---

**Theorem:** If a sequence $(a_n)$ is [monotone](../D/monotone-sequence) and [bounded](../D/bounded-sequence), then it converges.

**Proof:** Suppose $(a_n)$ is increasing and bounded above. The other cases are analogous. Let:

$$L = \sup\{a_n : n \in \mathbb{N}\}$$

which exists by the [completeness axiom](../T/completeness-axiom) since the set is non-empty and bounded above.

Let $\varepsilon > 0$. Since $L - \varepsilon$ is not an upper bound, there exists $N \in \mathbb{N}$ such that $a_N > L - \varepsilon$. Since $(a_n)$ is increasing and $L$ is an upper bound:

$$n > N \implies L - \varepsilon < a_N \leq a_n \leq L < L + \varepsilon$$

Therefore $\lvert a_n - L \rvert < \varepsilon$ for all $n > N$, so $a_n \to L$.