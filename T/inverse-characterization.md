---
layout: proof
title: "Characterization of Bijections by Inverses"
chapter: "Set Theory and Functions"
link_terms: ["characterization of bijections by inverses"]
---

**Theorem:** A [function](../D/function) $f : A \to B$ is a [bijection](../D/bijective) if and only if there exists a function $h : B \to A$ whose [compositions](../D/composition) with $f$ are identity functions:

$$h \circ f = \mathrm{id}_A, \qquad f \circ h = \mathrm{id}_B$$

In that case $h = f^{-1}$, and $f^{-1}$ is itself a bijection.

**Proof:** ($\Rightarrow$) If $f$ is a bijection, $h = f^{-1}$ satisfies both identities by the definition of the [inverse function](../D/inverse-function).

($\Leftarrow$) Suppose such an $h$ exists.

*[Injective](../D/injective):* if $f(a_1) = f(a_2)$, then $a_1 = h(f(a_1)) = h(f(a_2)) = a_2$.

*[Surjective](../D/surjective):* for $b \in B$, we have $b = f(h(b))$, so $b$ lies in the [image](../D/image) of $f$.

Thus $f$ is a bijection. For each $b$, the element $h(b)$ is a [preimage](../D/preimage) of $b$, and preimages under a bijection are unique, so $h(b) = f^{-1}(b)$.

Finally, the two identities are symmetric in $f$ and $h$. Applying the ($\Leftarrow$) direction with the roles of $f$ and $h$ swapped shows that $h = f^{-1}$ is a bijection.
