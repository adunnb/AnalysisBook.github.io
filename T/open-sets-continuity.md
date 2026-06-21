---
layout: proof
title: "Characterization of Continuity via Open Sets"
chapter: "Limits and Continuity"
---

**Theorem:** A function $f : \mathbb{R} \to \mathbb{R}$ is [continuous](../D/continuity) on $\mathbb{R}$ if and only if $f^{-1}(O)$ is [open](../D/open-set) for every open set $O \subseteq \mathbb{R}$.

**Remark:** This theorem restates continuity entirely in terms of open sets, with no mention of $\varepsilon$ and $\delta$. It is the starting point for defining continuity on more general spaces where there is no notion of distance, only a notion of open sets.

**Proof:**

**($\Rightarrow$)** Suppose $f$ is continuous on $\mathbb{R}$. Let $O \subseteq \mathbb{R}$ be open and let $x \in f^{-1}(O)$, so $f(x) \in O$. Since $O$ is open, there exists $\varepsilon > 0$ such that $V_\varepsilon(f(x)) \subseteq O$. Since $f$ is continuous at $x$, there exists $\delta > 0$ such that:

$$\lvert y - x \rvert < \delta \implies \lvert f(y) - f(x) \rvert < \varepsilon$$

That is, $f(V_\delta(x)) \subseteq V_\varepsilon(f(x)) \subseteq O$, so $V_\delta(x) \subseteq f^{-1}(O)$. Since $x \in f^{-1}(O)$ was arbitrary, every point of $f^{-1}(O)$ has a neighborhood contained in $f^{-1}(O)$, so $f^{-1}(O)$ is open.

**($\Leftarrow$)** Suppose $f^{-1}(O)$ is open for every open set $O \subseteq \mathbb{R}$. Let $c \in \mathbb{R}$ and $\varepsilon > 0$. The set $V_\varepsilon(f(c))$ is open, so $f^{-1}(V_\varepsilon(f(c)))$ is open and contains $c$. Therefore there exists $\delta > 0$ such that $V_\delta(c) \subseteq f^{-1}(V_\varepsilon(f(c)))$, which means:

$$\lvert x - c \rvert < \delta \implies f(x) \in V_\varepsilon(f(c)) \implies \lvert f(x) - f(c) \rvert < \varepsilon$$

So $f$ is continuous at $c$. Since $c \in \mathbb{R}$ was arbitrary, $f$ is continuous on $\mathbb{R}$.
