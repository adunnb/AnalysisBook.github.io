---
layout: definition
title: "Injective Function"
chapter: "Sets and Functions"
link_terms: ["injective", "injection", "one-to-one"]
---

**Definition:** A [function](../D/function) $f : A \to B$ is **injective** (or **one-to-one**) if for all $a_1, a_2 \in A$:

$$f(a_1) = f(a_2) \implies a_1 = a_2$$

Equivalently, distinct inputs have distinct outputs: $a_1 \neq a_2$ implies $f(a_1) \neq f(a_2)$. An injective function is also called an **injection**.

**Example:** $f(x) = x^2$ is injective on $[0, \infty)$ but not on $\mathbb{R}$, since $f(-2) = f(2)$.

**Example:** $\sin$ is injective on $[0, \pi/2]$ but not on $[0, 2\pi]$, since $\sin(\pi/6) = \sin(5\pi/6) = \tfrac{1}{2}$.

**Example:** $r(n) = n \bmod 3$ is not injective on $\mathbb{N}$, since $r(7) = r(10) = 1$.

**Remark:** Injectivity is the **horizontal line test**: each horizontal line meets the graph at most once. Unlike surjectivity, injectivity does not depend on the codomain. Every function becomes injective when restricted to a [subset](../D/subset) of its domain containing exactly one point of each nonempty [fiber](../D/preimage). When there are infinitely many fibers, choosing such a subset uses the axiom of choice.
