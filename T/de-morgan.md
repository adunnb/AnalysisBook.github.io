---
layout: proof
title: "De Morgan's Laws"
chapter: "Sets and Functions"
link_terms: ["De Morgan's laws", "De Morgan's law"]
---

**Theorem:** For any sets $A$, $B$, $C$:

$$A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$$

$$A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C)$$

In particular, if $B, C$ lie in an ambient set $U$, then $(B \cup C)^c = B^c \cap C^c$ and $(B \cap C)^c = B^c \cup C^c$.

**Remark:** In words, the [complement](../D/set-difference) of a [union](../D/union-intersection) is the intersection of the complements, and vice versa. The same proof works for any [indexed family](../D/indexed-family): $A \setminus \bigcup_\alpha B_\alpha = \bigcap_\alpha (A \setminus B_\alpha)$ and $A \setminus \bigcap_\alpha B_\alpha = \bigcup_\alpha (A \setminus B_\alpha)$.

**Proof of the first law:** We prove equality by [two inclusions](../D/subset).

($\subseteq$) Let $x \in A \setminus (B \cup C)$. Then $x \in A$ and $x \notin B \cup C$, so $x \notin B$ and $x \notin C$. Hence $x \in A \setminus B$ and $x \in A \setminus C$, so $x \in (A \setminus B) \cap (A \setminus C)$.

($\supseteq$) Let $x \in (A \setminus B) \cap (A \setminus C)$. Then $x \in A$, $x \notin B$, and $x \notin C$. Therefore $x \notin B \cup C$, so $x \in A \setminus (B \cup C)$.

**Proof of the second law:** For any $x$:

$$\begin{aligned}
x \in A \setminus (B \cap C) &\iff x \in A \text{ and not both } x \in B,\ x \in C \\
&\iff (x \in A \text{ and } x \notin B) \text{ or } (x \in A \text{ and } x \notin C) \\
&\iff x \in (A \setminus B) \cup (A \setminus C)
\end{aligned}$$

The [complement](../D/set-difference) forms follow by taking $A = U$.
