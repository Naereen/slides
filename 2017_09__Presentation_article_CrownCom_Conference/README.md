---
author: Lilian Besson
title: MAB Learning in IoT Networks
subtitle: Learning helps even in non-stationary settings!
institute:
  PhD Students in France \newline
  Team SCEE, IETR, CentraleSupélec, Rennes \newline
  \& Team SequeL, CRIStAL, Inria, Lille \newline
smallinstitute: CROWNCOM 2017
date: 20-21 sept 2017
lang: english
babel-lang: english
handout: false
numbersections: true
section-titles: false
fontsize: 12pt
toc: false
include-before:
  \section*{\hfill{}CentraleSupélec Rennes \& Inria Lille\hfill{}}
  \subsection*{\hfill{}Team {:} SCEE @ IETR \& SequeL @ CRIStAL\hfill{}}
---

\section{\hfill{}1. Introduction and motivation\hfill{}}

\subsection{\hfill{}1.a. Objective\hfill{}}
# We want
- Insert *lots* of IoT objects in a **crowded wireless network**
- With a protocol **slotted in time and frequency**
- Each object has a **low duty cycle**
  (a few message per day)

. . .

## Goal
- Maintain a **good Quality of Service**
- **Without** centralized supervision!

. . .

## How?
- Use **learning algorithms**:
  objects will learn on which frequency they should talk!

----

\subsection{\hfill{}1.b. Outline\hfill{}}
# Outline
1. Introduction and motivation
2. Model and hypotheses
3. Baseline algorithms :
   to compare against naive and efficient centralized approaches
4. Two Multi-Armed Bandit algorithms :
   UCB, Thompson sampling
5. Experimental results
6. Perspectives and future works
7. Conclusion

----

\section{\hfill{}2. Model and hypotheses\hfill{}}

\subsection{\hfill{}2.a. Model\hfill{}}
# Model
- Discrete time $t\geq1$ and $N_c$ radio channels (\emph{e.g.}, 10)
  \hfill{} (*known*)

<!-- ![Protocolsrc/protocol.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[width=0.40\textwidth]{src/protocol.eps}
\caption{Protocol in time and frequency, with an \emph{Acknowledgement}.}
\end{figure}

- $D$ *dynamic* devices try to access the network independently
- $S=S_1+\dots+S_{N_c}$ *static* devices also use the network :
  $S_1,\dots,S_{N_c}$ in each channel
  \hfill{} (*unknown*).

----

\subsection{\hfill{}2.b. Hypotheses\hfill{}}
# Hypotheses {.allowframebreaks}
## Emission model
- Each device has the same *low* emission probability: \newline
  each step, each device sends a packet with probability $p$. \newline
  \small{(this gives a duty cycle proportional to $1/p$)}

## Background traffic
- Each static device use only one channel.
- Their repartition is fixed in time.

> $\implies$ Background traffic, bothering the dynamic devices!

## Dynamic radio reconfiguration
- Each dynamic device decides the channel it uses to send every packet.
- It has memory and computational capacity to implement basic decision algorithm.

## Problem
- *Goal* : *maximize communication* ($=$ number of received `Ack`)
  in a *finite-space discrete-time Decision Making Problem*.
- *Solution ?* **Multi-Armed Bandit algorithms**,
  **decentralized** and used **independently** by each device.

----

\section{\hfill{}3. Baseline algorithms\hfill{}}

\subsection{\hfill{}3.a. A naive strategy : uniformly random access\hfill{}}
# A naive strategy : uniformly random access
- Uniformly random access:
  dynamic devices choose uniformly their channel in the pull of $N_c$ channels.
- Natural strategy, dead simple to implement.

. . .

- Simple analysis, in term of **successful transmission probability**:

\begin{small} \begin{align*}
\mathbb{P}(\text{success}|\text{sent}) = \sum_{i=1}^{N_c} \underbrace{(1 - p / N_c)^{D-1}}_{\text{No other dynamic device}} \times \underbrace{(1-p)^{S_i}}_{\text{No static device}} \times\; \frac{1}{N_c}.
\end{align*} \end{small}

. . .

- Works fine only if all channels are similarly occupied,\newline
  but **it cannot learn** to exploit the best channels (more free).

----

\subsection{\hfill{}3.b. Optimal centralized strategy\hfill{}}
# Optimal centralized strategy {.allowframebreaks}
- If an oracle can decide to affect $D_i$ dynamic devices to channel $i$,
  the **successful transmission probability** is:
\begin{small} \begin{align*}
\mathbb{P}(\text{success}|\text{sent}) = \sum_{i=1}^{N_c} \underbrace{(1 - p)^{D_i - 1}}_{\;\;D_i - 1 \;\text{others}\;\;} \times \underbrace{(1 - p)^{S_i}}_{\;\;\text{No static device}\;\;} \times \underbrace{ D_i / D }_{\;\;\text{Sent in channel}\; i}.
\end{align*} \end{small}

- The oracle wishes to solve this **optimization problem**:
\vspace*{-10pt}
\begin{small} \begin{subequations} \begin{align*}
\underset{D_1,\dots,D_{N_c}}{\arg\max}\; & \sum_{i=1}^{N_c} D_i (1 - p)^{S_i + D_i -1}\\
\text{such that}\;\; & \sum_{i=1}^{N_c} D_i = D \; \text{and} \; & D_i \geq 0 \qquad \forall 1 \leq i \leq N_c .
\end{align*} \end{subequations} \end{small}

- We solved this quasi-convex optimization problem with *Lagrange multipliers*
- $\implies$ Very good performance, maximizing the transmission rate of all the $D$ dynamic devices

## But unrealistic
But **not achievable in practice**: no centralized oracle!

<!-- ---

\subsection{\hfill{}3.c. Greedy approximation of the centralized strategy\hfill{}}
# Greedy approximation
- Still very efficient
- More reasonable
- But still unachievable: this is a *baseline* -->

----

\section{\hfill{}4. Two Multi-Armed Bandit algorithms : UCB, TS\hfill{}}

\subsection{\hfill{}4.1. Multi-Armed Bandit formulation\hfill{}}
# Multi-Armed Bandit formulation
For a dynamic device, it collects *rewards* :

- at each time step $\tau$ when it needs to communicate
- chooses a channel $A(\tau) \in \{1,\dots,N_c\}$
<!-- - if the message is successfully sent (no collision), it receives an `Ack` -->
- if `Ack` (no collision)
  \hfill{} $\implies$ reward $r_{A(\tau)} = 1$
- if collision (no `Ack`)
  \hfill{} $\implies$ reward $r_{A(\tau)} = 0$

## Goal
Maximize transmission rate $\equiv$ **maximize cumulated rewards**
$$\sum_{\tau=1}^{\dots} r_{A(\tau)}.$$

\subsection{\hfill{}4.2. Upper Confidence Bound algorithm : UCB\hfill{}}
# Upper Confidence Bound algorithm ($\mathrm{UCB}_1$) {.allowframebreaks}
A dynamic device keeps $\tau$ number of sent packets, $T_k(t)$ selections of channel $k$, $X_k(t)$ successful transmission in channel $k$.

1. For the first $N_c$ steps ($\tau=1,\dots,N_c$), try each channel *once*.
2. Then for the next steps $t \geq N_c$ :
    \begin{small}
    $$ g_k(\tau) := \underbrace{\frac{X_k(\tau)}{N_k(\tau)}}_{\text{Mean}\; \widehat{\mu_k}(\tau)} + \underbrace{\sqrt{\frac{\log(\tau)}{2 N_k(\tau)}}}_{\text{Upper Confidence Bound}\;} $$
    \end{small}
    - Choose channel $A(\tau) = \mathop{\arg\max}\limits_{k} g_k(\tau)$,
    - Update $T_k(\tau+1)$, $X_k(\tau+1)$.

\hfill{}\tiny{\textcolor{gray}{[Lai \& Robbins, 1985], [Auer et al, 2002], [Bubeck \& Cesa-Bianchi, 2012]}}

----

\subsection{\hfill{}4.3. Thompson Sampling : Bayesian index policy\hfill{}}
# Thompson Sampling {.allowframebreaks}

"*Thompson Sampling*" est une approche Bayésienne :

- Le SU suppose que les $\mu_1,\dots,\mu_k$ ont été tiré selon un processus aléatoire, modélisé par un a posteriori ("*posterior*"), e.g., une distribution Binomiale $\mathrm{Bin}(a_k(t),b_k(t))$ qui évolue à chaque étape.

- D'abord un a priori uniforme : $a_k(0),b_k(0) = 1$ ("*flat prior*"),

- Ensuite, à chaque étape $t$, le SU tire *un* échantillon de chaque distribution a posteriori, et le canal $A(t)$ ayant l'échantillon le plus grand est utilisé ($=$ le plus probable d'être libre pour communiquer) :
    $$ A(t) = \mathop{\arg\max}\limits_k i_k(t) \;\;\text{avec}\; i_k(t) \sim \mathrm{Bin}(a_k(t), b_k(t)).$$
- Selon la détection des PU sur le canal $k = A(t)$, l'a posteriori est mis à jour :
    + $a_k(t) = 1 + X_k(t)$ : nombre de transmissions réussies,
    + et $b_k(t) = 1 + N_k(t) - X_k(t)$ : nombre de transmissions échouées.
- $\implies$ moyenne empirique estimée :
  $$\widetilde{\mu_k}(t) = \frac{a_k(t)}{a_k(t) + b_k(t)} = \frac{1 + X_k(t)}{2 + N_k(t)} \simeq \frac{X_k(t)}{N_k(t)} = \widehat{\mu_k}(t).$$

> Un algorithme historique (\textcolor{gray}{[Thompson, 1935]}), très simple, mais qui marche très bien (prouvé optimal pour différents types de problème).

\hfill{}\small{\textcolor{gray}{[Thompson, 1935]}}

----

\section{\hfill{}5. Experimental results\hfill{}}

\subsection{\hfill{}5.1. Experiment setting\hfill{}}
# Experimental setting
- What do we want to show
- Wnat we implemented
- Simulation parameters

----

\subsection{\hfill{}5.2. First result: $10\%$\hfill{}}
# First result: $10\%$ of dynamic devices

![$10\%$ of dynamic devices](src/10intelligent.eps)

----

\subsection{\hfill{}5.2. First result: $20\%$\hfill{}}
# $30\%$ of dynamic devices

![$30\%$ of dynamic devices](src/30intelligent.eps)

----

\subsection{\hfill{}5.2. First result: $50\%$\hfill{}}
# $50\%$ of dynamic devices

![$50\%$ of dynamic devices](src/50intelligent.eps)

----

\subsection{\hfill{}5.2. First result: $100\%$\hfill{}}
# $100\%$ of dynamic devices \hfill{} Extreme case

![$100\%$ of dynamic devices](src/100intelligent.eps)

----

\subsection{\hfill{}5.3. Growing proportion of devices dynamic devices\hfill{}}
# Growing proportion of devices dynamic devices

![Growing proportion of devices dynamic devices](src/perf_learning.eps)

----

\section{\hfill{}6. Perspectives and future work\hfill{}}

\subsection{\hfill{}6.1. Perspectives\hfill{}}
# Perspectives
## Theoretical results
- This
- and this
- and this

## Real-world experimental validation
- In progress

----

\subsection{\hfill{}6.2. Future work\hfill{}}
# Future work
- We need to do this
- and that
- and it will be awesome

----

\section{\hfill{}7. Conclusion\hfill{}}
\subsection{\hfill{}Thanks!\hfill{}}
# Conclusion
- We proved this...

## Success story
- It works very well
- Simple algorithms gives up-to $16\%$ gain compared to naive approach
- And almost optimal efficiency after a short learning time

## More work is needed
- Theoretical guarantees are still missing
- And also real-world validation


\hfill{} **Thanks!** *Question?*