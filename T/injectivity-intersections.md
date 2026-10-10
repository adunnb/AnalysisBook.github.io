---
layout: proof
title: "Injectivity and Intersections"
chapter: "Set Theory and Functions"
link_terms: ["injectivity and intersections"]
---

**Theorem:** A [function](../D/function) $f : X \to Y$ is [injective](../D/injective) if and only if:

$$f(A \cap B) = f(A) \cap f(B) \quad \text{for all } A, B \subseteq X$$

**Remark:** For every function the inclusion $f(A \cap B) \subseteq f(A) \cap f(B)$ holds ([Images of unions and intersections](../T/image-operations)); injectivity is exactly what makes it an equality. Two mistakes are common when proving this:

- **Cancelling $f$.** From $f(S) = f(T)$ one cannot conclude $S = T$ unless $f$ is already known to be injective, so this step cannot be used to *prove* injectivity. A constant function maps many different nonempty sets to the same singleton.
- **Using the wrong ambient set for a complement.** For injective $f$, $f(X \setminus S) = f(X) \setminus f(S)$, but in general $f(X \setminus S) \neq Y \setminus f(S)$, because $f$ need not hit every point of $Y$. For example, with $f(x) = e^x$ on $\mathbb{R}$ and $S = (0, \infty)$, we get $f(\mathbb{R} \setminus S) = (0, 1]$ while $\mathbb{R} \setminus f(S) = (-\infty, 1]$.

**Proof:** ($\Rightarrow$) Suppose $f$ is injective. The inclusion $f(A \cap B) \subseteq f(A) \cap f(B)$ holds for every function by [the image of an intersection](../T/image-operations). For the reverse inclusion, let $y \in f(A) \cap f(B)$. Then there exist $a \in A$ and $b \in B$ with:

$$f(a) = y = f(b)$$

Since $f$ is injective, $a = b$. This common point lies in $A \cap B$, so $y \in f(A \cap B)$.

($\Leftarrow$) Suppose the equality holds for all $A, B \subseteq X$, and let $x_1, x_2 \in X$ with $f(x_1) = f(x_2)$. Take $A = \{x_1\}$ and $B = \{x_2\}$. Their common [image](../D/image) value lies in $f(A) \cap f(B) = f(A \cap B)$, so $A \cap B \neq \varnothing$. Two singletons intersect only when their elements agree, so $x_1 = x_2$. Therefore $f$ is injective.
