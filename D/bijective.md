---
layout: definition
title: "Bijective Function"
chapter: "Set Theory and Functions"
link_terms: ["bijective", "bijection", "one-to-one correspondence"]
---

**Definition:** A [function](../D/function) $f : A \to B$ is **bijective** if it is both [injective](../D/injective) and [surjective](../D/surjective). Equivalently, every $b \in B$ has exactly one [preimage](../D/preimage) in $A$. A bijective function is also called a **bijection** or a **one-to-one correspondence**.

**Example:** Whether $f(x) = x^2$ is a bijection depends on both the domain and the codomain:

| Function | Injective? | Surjective? | Bijective? |
|---|---|---|---|
| $\mathbb{R} \to \mathbb{R}$ | no | no | no |
| $\mathbb{R} \to [0, \infty)$ | no | yes | no |
| $[0, \infty) \to [0, \infty)$ | yes | yes | yes |

**Example:** The identity $x \mapsto x$ and the map $x \mapsto 3x^3 - 2$ are bijections $\mathbb{R} \to \mathbb{R}$. For the latter, the unique preimage of $y$ is $\sqrt[3]{(y + 2)/3}$. Likewise, $\sin : [0, \pi/2] \to [0, 1]$ is a bijection.

**Remark:** A bijection has an [inverse function](../D/inverse-function). Bijections are also how the sizes of sets are compared: two sets have the same cardinality when there is a bijection between them.
