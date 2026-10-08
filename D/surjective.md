---
layout: definition
title: "Surjective Function"
chapter: "Set Theory and Functions"
link_terms: ["surjective", "surjection"]
---

**Definition:** A [function](../D/function) $f : A \to B$ is **surjective** (or **onto**) if its [image](../D/image) is all of $B$:

$$f(A) = B$$

That is, for every $b \in B$ there exists $a \in A$ with $f(a) = b$. A surjective function is also called a **surjection**.

**Example:** $f(x) = x^2$ is surjective as a map $\mathbb{R} \to [0, \infty)$ but not as a map $\mathbb{R} \to \mathbb{R}$, since no real number maps to $-1$.

**Example:** $r(n) = n \bmod 3$ is surjective as a map $\mathbb{N} \to \{0, 1, 2\}$, but not as a map $\mathbb{N} \to \mathbb{N}_0$, since $4$ is not a value.

**Remark:** Surjectivity always refers to the specified codomain. Any function $f : A \to B$ becomes surjective when regarded as a map $A \to f(A)$.
