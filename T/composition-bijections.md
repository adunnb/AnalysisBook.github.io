---
layout: proof
title: "Composition of Injections, Surjections, and Bijections"
chapter: "Sets and Functions"
link_terms: ["composition of injections, surjections, and bijections"]
---

**Theorem:** Let $f : A \to B$ and $g : B \to C$, and consider their [composition](../D/composition) $g \circ f$.

1. If $f$ and $g$ are [injective](../D/injective), then $g \circ f$ is injective.
2. If $f$ and $g$ are [surjective](../D/surjective), then $g \circ f$ is surjective.
3. If $f$ and $g$ are [bijective](../D/bijective), then $g \circ f$ is bijective.

**Proof of (1):** Suppose $g(f(a_1)) = g(f(a_2))$. Since $g$ is injective, $f(a_1) = f(a_2)$. Since $f$ is injective, $a_1 = a_2$.

**Proof of (2):** Let $c \in C$. Since $g$ is surjective, there exists $b \in B$ with $g(b) = c$. Since $f$ is surjective, there exists $a \in A$ with $f(a) = b$. Then $(g \circ f)(a) = g(b) = c$.

**Proof of (3):** Combine (1) and (2).
