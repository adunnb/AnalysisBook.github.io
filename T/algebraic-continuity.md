---
layout: proof
title: "Algebraic Continuity Theorem"
chapter: "Limits and Continuity"
---

**Theorem:** Let $f, g : A \to \mathbb{R}$ be [continuous at a point](../D/continuity) $c \in A$. Then:

(i) $f + g$ is continuous at $c$

(ii) $fg$ is continuous at $c$

(iii) $cf$ is continuous at $c$ for any constant $c \in \mathbb{R}$

(iv) $\dfrac{f}{g}$ is continuous at $c$, provided $g(c) \neq 0$

**Proof:** Let $(x_n)$ be any sequence in $A$ with $x_n \to c$. Since $f$ and $g$ are continuous at $c$, the [sequential characterization of continuity](../D/continuity) gives $f(x_n) \to f(c)$ and $g(x_n) \to g(c)$. The result then follows in each case from the [algebra of limits](../T/algebra-limits):

(i) $(f+g)(x_n) = f(x_n) + g(x_n) \to f(c) + g(c) = (f+g)(c)$

(ii) $(fg)(x_n) = f(x_n)g(x_n) \to f(c)g(c) = (fg)(c)$

(iii) $(cf)(x_n) = cf(x_n) \to cf(c) = (cf)(c)$

(iv) $\dfrac{f}{g}(x_n) = \dfrac{f(x_n)}{g(x_n)} \to \dfrac{f(c)}{g(c)} = \dfrac{f}{g}(c)$, since $g(c) \neq 0$

Since $(x_n)$ was arbitrary, $f+g$, $fg$, $cf$, and $\frac{f}{g}$ are all continuous at $c$.