---
layout: proof
title: "Algebraic Limit Theorem for Functions"
chapter: "Limits and Continuity"
---

**Theorem:** Let $f, g : A \to \mathbb{R}$ and let $c$ be a [limit point](../D/limit-point) of $A$. Suppose $\lim_{x \to c} f(x) = L$ and $\lim_{x \to c} g(x) = M$. Then:

(i) $\lim_{x \to c} (f + g)(x) = L + M$

(ii) $\lim_{x \to c} (fg)(x) = LM$

(iii) $\lim_{x \to c} (cf)(x) = cL$ for any constant $c \in \mathbb{R}$

(iv) $\lim_{x \to c} \dfrac{f}{g}(x) = \dfrac{L}{M}$, provided $M \neq 0$

**Proof:** By the [sequential characterization of functional limits](../T/sequential-limits), it suffices to verify each statement for sequences. Let $(x_n)$ be any sequence in $A$ with $x_n \neq c$ and $x_n \to c$. Then $f(x_n) \to L$ and $g(x_n) \to M$, so by the [algebra of limits](../T/algebra-limits) for sequences:

(i) $(f+g)(x_n) = f(x_n) + g(x_n) \to L + M$

(ii) $(fg)(x_n) = f(x_n)g(x_n) \to LM$

(iii) $(cf)(x_n) = cf(x_n) \to cL$

(iv) $\dfrac{f}{g}(x_n) = \dfrac{f(x_n)}{g(x_n)} \to \dfrac{L}{M}$, since $M \neq 0$

Since $(x_n)$ was arbitrary, the sequential characterization gives the result in each case.