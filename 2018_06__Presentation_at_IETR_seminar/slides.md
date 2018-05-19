---
author:
    \textbf{Lilian Besson} \newline
    \and Émilie Kaufmann
smallauthor: Lilian Besson
title:    What Doubling Tricks Can and Can’t Do for Multi-Armed Bandits
subtitle: About a well-known and under-studied technique for online reinforcement learning
institute:
    PhD Student \newline
    Team SCEE, IETR, CentraleSupélec, Rennes \newline
    \& Team SequeL, CRIStAL, Inria, Lille
smallinstitute: CentraleSupélec \& Inria
date: IETR Seminar - 15th June 2018
smalldate: 15/06/18
lang: en-US
babel-lang: english
handout: false
numbersections: true
section-titles: false
fontsize: 12pt
toc: false
include-before:
  \section*{\hfill{}CentraleSupélec Rennes \& Inria Lille\hfill{}}
  \subsection*{\hfill{}Équipes {:} SCEE @ IETR \& SequeL @ CRIStAL\hfill{}}
---

\section{\hfill{}0. Introduction and motivation\hfill{}}

\subsection{\hfill{}0.1. Title\hfill{}}

### **« What Doubling Tricks Can and Can’t Do for Multi-Armed Bandits »**

- *Date* : $15$th of June $2018$

- *Who:* [Lilian Besson](https://GitHub.com/Naereen/slides/) , PhD Student in France, co-advised by

| *Christophe Moy* <br> @ CentraleSupélec <br>& IETR, Rennes | *Émilie Kaufmann* <br> @ Inria, Lille |
|:---:|:---:|
| ![7%](../common/LogoCS.png) ![14%](../common/LogoIETR.png) | ![12%](../common/LogoInria.jpg) |

> See our paper [`HAL.Inria.fr/hal-01736357`](https://hal.inria.fr/hal-01736357)

---

# "Doubling trick" : rapide présentation

## Horizon $T$ : mieux de ne pas la connaître !
- En apprentissage séquentiel, expériences de $t=1$ à $t=T$,
- Pour des applications réelles, les algorithmes ne doivent pas connaître l'horizon... (ex : essais cliniques, pubs en ligne, radio intelligente etc).
- Mais beaucoup sont développés avec "la théorie en tête", et dépendent de la valeur de $T$ !

. . .

## But ?

- $\hookrightarrow$ Peut-on transformer un algorithme $\mathcal{A}$ dépendant de $T$ et le rendre \alert{indépendant de l'horizon} $\mathcal{A}'$ ?
- $\implies$ **Oui !**
- Une technique classique : "doubling trick" !

---

# Algorithme du "Doubling trick"

<!-- ![](./images/Generic_Doubling_Trick_algorithm.png) -->
<!-- WARNING if not converting to LaTeX -->

<!-- FIXME how to use babel[french] here and have the keywords (Input, for, do, if, then, end) in French here ? -->
\begin{algorithm}[H]
% XXX Options
\LinesNumbered  % XXX Option to number the line
\DontPrintSemicolon
% \RestyleAlgo{boxed}
% XXX Input, data and output
\KwIn{Algorithme de bandit $\mathcal{A}$, et une suite $(T_i)_{i\in\mathbb{N}}$.}
% \KwData{Données}
% \KwResult{Résultat}
\BlankLine
% XXX Algorithme
Soit $i = 0$, et initialise l'algorithme $\mathcal{A}^{(0)} = \mathcal{A}_{T_0}$.\;
\For{$t = 1, \dots, T-1$}{
\If(\tcp*[f]{Horizon suivante $T_{i+1}$ dans la suite}){
$t > T_i$
}{
Horizon suivante : $i = i + 1$\;
Initialise $\mathcal{A}^{(i)} = \mathcal{A}_{T_i - T_{i-1}}$
\tcp*[f]{Départ à vide}
}
Joue selon $\mathcal{A}^{(i)}$ : choisit le bras $A'(t) := A^{(i)}(t - T_{i-1})$\;
Observe la récompense $r(t) = Y_{A'(t), t}$\;
Lui donner cette observation.
}
\caption{$\mathcal{A}' = \mathrm{DT}(\mathcal{A}, (T_i)_{i\in\mathbb{N}})$.}
\label{algo:DTr}
\end{algorithm}

---

# Deux "doubling" : géométrique et exponentiel

- $T_0 \in \mathbb{N}$, $(T_i)_{i\in\mathbb{N}}$ croissante et divergente
<!-- - ($\to+\infty$ pour $i\to\infty$). -->
- "Indice du dernier terme" : $L_T := \min\{ i \in\mathbb{N} : T_i > T\}$.

## Géométrique
- Pour un paramètre $b > 1$,
- $T_i := \lfloor T_0 b^i\rfloor$,
- $L_T = \lceil \log_b\left( \frac{T}{T_0} \right) \rceil = \mathcal{O}( \log(T) )$.

## Exponentiel
- Pour deux paramètres $a, b > 1$,
- $T_i := \lfloor \frac{T_0}{a} a^{b^i}\rfloor$,
- $L_T = \lceil \log_b\left( \log_a\left( \frac{T}{T_0/a} \right) \right) \rceil = \mathcal{O}( \log(\log(T)) )$.

---

# Regret et but
## Regret ?
- $R_T(\mathcal{A}_T)$ mesure la performance moyenne de l'algorithme $\mathcal{A}$ (qui peut connaître $T$), sur une expérience d'horizon $T$.
- $R_T(\mathcal{A}) := \sum_{t=1}^T \mu^* - \mathbb{E}[\mu_{A(t)}]$ pour un problème à $K$ bras de moyennes $\mu_1,\dots,\mu_K$, de meilleur bras $\mu^* := \arg\max_k \mu_k$ et si $A(t)$ est le choix de l'algorithme à l'instant $t$.

. . .

## But : *conserver* des bornes de regret !
- Si $\mathcal{A}$ vérifie une borne de regret, *e.g.*, $R_T(\mathcal{A}_T) \leq f(T)$
- Alors la version indépendante de $T$, $\mathrm{DT}(\mathcal{A})$, vérifie une borne similaire, avec une perte constante $\ell$, \alert{ou non} :
    + $R_T(\mathrm{DT}(\mathcal{A})) \leq \ell(\text{paramètres pb}) \times f(T)$ : bien !
    + $R_T(\mathrm{DT}(\mathcal{A})) \leq \ell(\text{paramètres pb}) \times g(T)$ : \alert{moins bien} ! (pour $g(T) \gg f(T)$).

---

# Types de bornes
> $c > 0$ est une constante dépendant des paramètres $\mu_1,\dots,\mu_K$ du problème, mais **pas** de $T$.

1. Regret indépendant des paramètres ("adversarial bandits")
    $$R_T(\mathcal{A}_T) \leq c \; \sqrt{T}$$

2. Regret dépendant des paramètres ("stochastic bandits")
    $$R_T(\mathcal{A}_T) \leq c \; \log(T)$$

## Forme générique
- \alert{$R_T(\mathcal{A}_T) \leq c \; (\log T)^{\delta} T^{\gamma}$}
    + $\delta=0,\gamma>0$ (adverse),
    + ou $\delta>0,\gamma=0$ (stochastique),
    + ou $\delta>0,\gamma>0$ (hybride !). E.g. : $\sqrt{T \log(T)}$.

---

# Résultats avec un "doubling" géométrique

> Avec des horizons $T_i := \lfloor T_0 b^i\rfloor$.

## Conserve bien $R_T \leq \sqrt{T}$ \hfill\Smiley
- Perte constante $\ell(b,\gamma) = \frac{b^{\gamma}(b-1)^{\gamma}}{b^{\gamma}-1} > 1$,
- $\hookrightarrow$ en connaissant $\gamma$, on choisit $b^*$ pour minimiser la perte.

## Conserve pas bien $R_T \leq \log(T)$ \hfill\Sadey
- \alert{On sait que ça ne peut pas marcher !}
- On a une borne inférieure : transforme ${(\log T)}^{\delta}$ en ${(\log T)}^{\delta\alert{+1}}$.

---

# Résultats avec un "doubling" exponentiel

> Avec des horizons $T_i := \lfloor \frac{T_0}{a} a^{b^i}\rfloor$.

## Conserve *peut-être* $R_T \leq \sqrt{T}$ \hfill\Sey
- \alert{Pas encore de borne sup ou inf convaincante},
- Transforme $\leq T^{\gamma}$ en $T^{\alert{b} \gamma}$, pas génial ($b > 1$)...
- Borne inf a la forme inverse, $\geq T^{\gamma}$ en $T^{\frac{\gamma}{\alert{b}}}$...

## Conserve bien $R_T \leq \log(T)$ \hfill\Smiley
- Perte constante $\ell(\delta, b) = \frac{b^{2\delta}}{b^{\delta}-1} > 1$ (*e.g.*, $\geq 4$ pour $\delta=1$),
- $\hookrightarrow$ en connaissant $\delta$, on choisit $b^*$ pour minimiser la perte.

---

# Illustration

![](images/main____env1-1_1217677871459230631.pdf){width=105%}

---

# Questions encore ouvertes

- Un schéma ($(T_i)_{i\in\mathbb{N}}$) intermédiaire qui conviendrait pour les trois types de bornes ?
- Une autre approche "plus intelligente" qui permettrait d'obtenir des meilleures garanties ?
- Empiriquement : choisir des paramètres ($T_0, b$ ou $T_0,a,b$) n'est pas simple, comment bien les choisir ?

## Question bonus
- \alert{Où publier cet article (refusé à COLT $2018$) ?}\newline
  $\hookrightarrow$ une revue ? (*e.g.*, JMLR)

---

# Applications de ce travail I
- Très générique !
- Donne une meilleure compréhension théorique de cette technique très utilisée depuis $\sim$ 20 ans (au moins).
- Justifie quelques articles qui utilisent le "doubling trick" sans justifier plus qu'une note de bas de page disant "on ne perd rien qu'une constante multiplicative dans le regret"...
- Donne une méthode simple pour choisir les valeurs de $T_0,b$ ou $T_0,a,b$ ($\hookrightarrow$ minimiser la perte constante $\ell$ !).

---

# Applications de ce travail II

## En radio intelligente ? Oui aussi !
1. Si on utilise un algorithme $\mathcal{A}_T$ très efficace dans son contexte, mais qui dépend de $T$ (*e.g.*, *Approximated Finite-Horizons Gittins Index*, $\mathrm{kl}$-$\mathrm{UCB}^{++}$, en bandits mono-joueur, *Musical Chair* en bandits multi-joueurs, etc),
2. Si on sait quel genre de garantie on espère (contexte stochastique, ou adverse, ou hybride),\pause
3. $\implies$ Alors on peut savoir quel "doubling trick" utiliser pour rendre son algorithme indépendant de $T$ le plus efficacement possible (on connaît $\delta,\gamma$ alors on choisit $T_0,b$ ou $T_0,a,b$ pour minimiser la perte constante $\ell$...).

---

# Une remarque qui m'intrigue

![](images/sad_paragraph_about_doubling_trick.png){width=90%}

\hfill{}\small{\textcolor{gray}{[\href{https://arxiv.org/abs/1805.05071}{Garivier et al, 2018, arXiv:1805.05071}]}}

\vspace*{10pt}

Surprenant : rien n'est prouvé ni justifié dans ce genre d'affirmations, et aucune référence n'est citée.\newline
Et les auteurs connaissent notre article...

---

\section{\hfill{}6. Conclusion\hfill{}}

\subsection{\hfill{}6.1. Summary\hfill{}}

# Conclusion (1/2)

- Online learning can be a powerful tool for Cognitive Radio, and many other real-world applications
- Many formulation exist, a simple one is the Multi-Armed Bandit
- Many algorithms exist, to tackle different situations
- It's hard to know before hand which algorithm is efficient for a certain problem…
- Online learning can also be used to select *on the run*
  which algorithm to prefer, for a specific situation!

---

\subsection{\hfill{}6.2. Summary \& Thanks\hfill{}}

# Conclusion (2/2)

- TODO
- TODO

### See our paper
[`HAL.Inria.fr/hal-01736357`](https://hal.inria.fr/hal-01736357)

### See our code for experimenting with bandit algorithms
Python library, open source at [`SMPyBandits.GitHub.io`](https://SMPyBandits.GitHub.io)

\begin{center}\begin{Huge} \Fontify{Thanks for listening ! :-)} \end{Huge}\end{center}
