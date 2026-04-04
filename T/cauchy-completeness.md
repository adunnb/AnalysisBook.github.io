---
layout: proof
title: "Completeness via Cauchy Sequences"
chapter: "Sequences and Series"
---

**Theorem:** The real numbers $\mathbb{R}$ are **complete** in the sense that every [Cauchy sequence](../D/cauchy-sequence) in $\mathbb{R}$ converges to a limit in $\mathbb{R}$.

**Remark:** This theorem is an equivalent formulation of the [completeness axiom](../T/completeness-axiom). It shows that completeness can be characterized entirely in terms of sequences, without reference to upper bounds or suprema. This sequential characterization of completeness can be more convenient to use in practice.

In contrast, the rational numbers $\mathbb{Q}$ are not complete in this sense. The sequence:

$$a_n = \left(1 + \frac{1}{n}\right)^n$$

is Cauchy in $\mathbb{Q}$ but converges to $e \notin \mathbb{Q}$.

**Proof:** This follows immediately from the [Cauchy criterion for convergence](../T/cauchy-criterion), which establishes that a sequence converges if and only if it is Cauchy. Since every Cauchy sequence converges and its limit is a real number, $\mathbb{R}$ is complete.