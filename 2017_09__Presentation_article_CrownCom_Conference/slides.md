---
author:
  \textbf{Lilian Besson} \and Rémi Bonnefoi \newline
  \and Christophe Moy \and Émilie Kaufmann \and Jacques Palicot
smallauthor: Lilian Besson
title: MAB Learning in IoT Networks
subtitle: Learning helps even in non-stationary settings!
institute:
  PhD Student in France \newline
  Team SCEE, IETR, CentraleSupélec, Rennes \newline
  \& Team SequeL, CRIStAL, Inria, Lille
smallinstitute: CentraleSupélec \& Inria
date: 20-21 Sept - CROWNCOM 2017
smalldate: CROWNCOM 2017
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

A *lot* of IoT devices want to access to a gateway of base station.
# We want
- Insert them in a possibly **crowded wireless network**.
- With a protocol **slotted in time and frequency**.
- Each device has a **low duty cycle**
  (a few message per day).

. . .

## Goal
- Maintain a **good Quality of Service**.
- **Without** centralized supervision!

. . .

## How?
- Use **learning algorithms**:
  devices will learn on which frequency they should talk!

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

<!-- ![Protocolprotocol.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[height=0.35\textheight]{protocol.eps}
\caption{\small{Protocol in time and frequency, with an \emph{Acknowledgement}.}}
\end{figure}

- $D$ **dynamic** devices try to access the network *independently*
- $S=S_1+\dots+S_{N_c}$ **static** devices occupy the network : \newline
  $S_1,\dots,S_{N_c}$ in each channel
  \hfill{} (*unknown*).

----

\subsection{\hfill{}2.b. Hypotheses\hfill{}}
# Hypotheses {.allowframebreaks}
## Emission model
- Each device has the same *low* emission probability: \newline
  each step, each device sends a packet with probability $p$. \newline
  \hfill{}\small{(this gives a duty cycle proportional to $1/p$)}

## Background traffic
- Each static device uses only one channel.
- Their repartition is fixed in time.

> $\implies$ Background traffic, bothering the dynamic devices!

## Dynamic radio reconfiguration
- Each **dynamic device decides the channel it uses to send every packet**.
- It has memory and computational capacity to implement basic decision algorithm.

## Problem
- *Goal* : *maximize packet loss ratio* ($=$ number of received `Ack`)
  in a *finite-space discrete-time Decision Making Problem*.
- *Solution ?* **Multi-Armed Bandit algorithms**,
  **decentralized** and used **independently** by each device.

----

\section{\hfill{}3. Baseline algorithms\hfill{}}

\subsection{\hfill{}3.a. A naive strategy : uniformly random access\hfill{}}
# A naive strategy : uniformly random access
- **Uniformly random access**:
  dynamic devices choose uniformly their channel in the pull of $N_c$ channels.
- Natural strategy, dead simple to implement.

. . .

- Simple analysis, in term of **successful transmission probability** (for every message from dynamic devices) :

\begin{small} \begin{align*}
\mathbb{P}(\text{success}|\text{sent}) = \sum_{i=1}^{N_c} \underbrace{(1 - p / N_c)^{D-1}}_{\text{No other dynamic device}} \times \underbrace{(1-p)^{S_i}}_{\text{No static device}} \times\; \frac{1}{N_c}.
\end{align*} \end{small}

. . .

- Works fine only if all channels are similarly occupied,\newline
  but **it cannot learn** to exploit the best (more free) channels.

----

\subsection{\hfill{}3.b. Optimal centralized strategy\hfill{}}
# Optimal centralized strategy {.allowframebreaks}
- If an oracle can decide to affect $D_i$ dynamic devices to channel $i$,
  the **successful transmission probability** is:
\vspace*{-10pt}
\begin{small} \begin{align*}
\mathbb{P}(\text{success}|\text{sent}) = \sum_{i=1}^{N_c} \underbrace{(1 - p)^{D_i - 1}}_{\;\;D_i - 1 \;\text{others}\;\;} \times \underbrace{(1 - p)^{S_i}}_{\;\;\text{No static device}\;\;} \times \underbrace{ D_i / D }_{\;\;\text{Sent in channel}\; i}.
\end{align*} \end{small}

- The oracle has to solve this **optimization problem**:
\vspace*{-5pt}
\begin{small} \begin{equation*} \begin{cases}
\underset{D_1,\dots,D_{N_c}}{\arg\max}\;\;\; & \sum_{i=1}^{N_c} D_i (1 - p)^{S_i + D_i -1}\\
\text{such that}\;\;\; & \sum_{i=1}^{N_c} D_i = D \; \text{and} \; D_i \geq 0, \; \; \forall 1 \leq i \leq N_c .
\end{cases} \end{equation*} \end{small}

- We solved this quasi-convex optimization problem with *Lagrange multipliers*, only numerically.
- $\implies$ Very good performance, maximizing the transmission rate of all the $D$ dynamic devices

## But unrealistic
But **not achievable in practice**: no centralized oracle!

## Let see *realistic decentralized approaches*
$\hookrightarrow$ Machine Learning ? \newline
\hspace*{15pt}$\hookrightarrow$ Reinforcement Learning ? \newline
\hspace*{30pt} $\hookrightarrow$ *Multi-Armed Bandit* !

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
A dynamic device tries to collect *rewards* when transmitting :

- ir transmits following a Bernoulli process \newline
  (probability $p$ of transmitting at each time step $\tau$),
- chooses a channel $A(\tau) \in \{1,\dots,N_c\}$,
<!-- - if the message is successfully sent (no collision), it receives an `Ack` -->
- if `Ack` (no collision)
  \hspace*{10pt} $\implies$ reward $r_{A(\tau)} = 1$,
- if collision (no `Ack`)
  \hspace*{10pt} $\implies$ reward $r_{A(\tau)} = 0$.

. . .

## Reinforcement Learning interpretation
Maximize transmission rate $\equiv$ **maximize cumulated rewards**
$$\max_{\text{algorithm}\;A} \;\; \sum_{\tau=1}^{\text{horizon}} r_{A(\tau)}.$$

\subsection{\hfill{}4.2. Upper Confidence Bound algorithm : UCB\hfill{}}
# Upper Confidence Bound algorithm ($\mathrm{UCB}_1$)
A dynamic device keeps $\tau$ number of sent packets, $T_k(t)$ selections of channel $k$, $X_k(t)$ successful transmission in channel $k$.

1. For the first $N_c$ steps ($\tau=1,\dots,N_c$), try each channel *once*.
2. Then for the next steps $t \geq N_c$ :
    - Compute the index $g_k(\tau) := \underbrace{\frac{X_k(\tau)}{N_k(\tau)}}_{\text{Mean}\; \widehat{\mu_k}(\tau)} + \underbrace{\sqrt{\frac{\log(\tau)}{2 N_k(\tau)}}.}_{\text{Upper Confidence Bound}}$
    - Choose channel $A(\tau) = \mathop{\arg\max}\limits_{k} \; g_k(\tau)$,
    - Update $T_k(\tau+1)$ and $X_k(\tau+1)$.

\vfill{}\hfill{}\tiny{\textcolor{gray}{References: [Lai \& Robbins, 1985], [Auer et al, 2002], [Bubeck \& Cesa-Bianchi, 2012]}}

----

\subsection{\hfill{}4.3. Thompson Sampling : Bayesian index policy\hfill{}}
# Thompson Sampling : Bayesian approach
A dynamic device assumes a stochastic hypothesis on the background traffic, modeled as Bernoulli distributions.

- Rewards $r_k(\tau)$ are assumed to be *i.i.d.* samples from a Bernoulli distribution $\mathrm{Bern}(\mu_k)$.

- A **binomial Bayesian posterior** is kept on the mean availability $\mu_k$ : $\mathrm{Bin}(1 + X_k(\tau), 1 + N_k(\tau) - X_k(\tau))$.
- Starts with a *uniform prior* : $\mathrm{Bin}(1, 1) \sim \mathcal{U}([0,1])$.
  <!-- : $a_k(0),b_k(0) = 1$ -->

1. Each step $\tau \geq 1$, a sample is drawn from each posterior
  $i_k(t) \sim \mathrm{Bin}(a_k(\tau), b_k(\tau))$,
2. Choose channel $A(\tau) = \mathop{\arg\max}\limits_k \; i_k(\tau)$,
3. Update the posterior after receiving `Ack` or if collision.

<!-- + $a_k(\tau) = 1 + X_k(\tau)$ : number of successful transmissions (`Ack`), -->
<!-- + $b_k(\tau) = 1 + N_k(\tau) - X_k(\tau)$ : number of failed transmissions (collision). -->
<!-- - $\implies$ estimated empirical average :
  $$\widetilde{\mu_k}(\tau) = \frac{a_k(\tau)}{a_k(\tau) + b_k(\tau)} = \frac{1 + X_k(\tau)}{2 + N_k(\tau)} \simeq \frac{X_k(\tau)}{N_k(\tau)} = \widehat{\mu_k}(\tau).$$ -->

\vfill{}\hfill{}\tiny{\textcolor{gray}{References: [Thompson, 1935], [Kaufmann et al, 2012]}}

----

\section{\hfill{}5. Experimental results\hfill{}}

\subsection{\hfill{}5.1. Experiment setting\hfill{}}
# Experimental setting

## Simulation parameters
- $N_c = 10$ channels,
- $S + D = 10000$ devices in total,
- $p = 10^{-3}$ probability of emission,
- $\text{horizon} = 10^5$ time slots ($\simeq 100$ messages $/$ device),
- The proportion of dynamic devices $D/(S+D)$ varies,
- Various settings for $(S_1,\dots,S_{N_c})$ static devices repartition.

## What do we show
- After a short learning time, MAB algorithm are almost as efficient as the oracle solution.
- Never worse than the naive solution.
- Thompson sampling is even more efficient than UCB.

----

\subsection{\hfill{}5.2. First result: $10\%$\hfill{}}
# $10\%$ of dynamic devices

<!-- ![$10\%$ of dynamic devices](10intelligent.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[height=0.74\textheight]{10intelligent.eps}
\caption{\small{$10\%$ of dynamic devices. $7\%$ of gain.}}
\end{figure}

----

\subsection{\hfill{}5.2. First result: $20\%$\hfill{}}
# $30\%$ of dynamic devices

<!-- ![$30\%$ of dynamic devices](30intelligent.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[height=0.74\textheight]{30intelligent.eps}
\caption{\small{$30\%$ of dynamic devices.} $3\%$ of gain but not much is possible.}
\end{figure}

<!-- ----

\subsection{\hfill{}5.2. First result: $50\%$\hfill{}}
# $50\%$ of dynamic devices

\begin{figure}[h!]
\centering
\includegraphics[height=0.74\textheight]{50intelligent.eps}
\caption{\small{$50\%$ of dynamic devices.}}
\end{figure}

----

\subsection{\hfill{}5.2. First result: $100\%$\hfill{}}
# $100\%$ of dynamic devices (extreme case)

\begin{figure}[h!]
\centering
\includegraphics[height=0.74\textheight]{100intelligent.eps}
\caption{\small{$100\%$ of dynamic devices.}}
\end{figure} -->

----

\subsection{\hfill{}5.3. Growing proportion of devices dynamic devices\hfill{}}
# Dependence on $D/(S+D)$

<!-- ![Growing proportion of devices dynamic devices](perf_learning.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[height=0.65\textheight]{perf_learning.eps}
\caption{\small{\emph{Almost optimal}, for any proportion of dynamic devices, \emph{after a short learning time}. Up-to $16\%$ gain over the naive approach!.}}
\end{figure}

----

\section{\hfill{}6. Perspectives and future work\hfill{}}

\subsection{\hfill{}6.1. Perspectives\hfill{}}
# Perspectives
## Theoretical results
- MAB algorithms have performance guarantees for *stochastic settings*,
- But here the collisions cancel the *i.i.d.* hypothesis,
- Not easy to obtain guarantees in this mixed setting \newline
  (*i.i.d.* emission process, game theoretic collisions).

. . .

## Real-world experimental validation ?
- Real-world radio experiments will help to validate this. \newline
  \hspace*{40pt}\hfill{}\textcolor{gray}{In progress\dots}

----

\subsection{\hfill{}6.2. Future work\hfill{}}
# Other direction of future work
- *More realistic emission model*:
  maybe driven by number of packets in a whole day,
  instead of emission probability.

- Validate this on a *larger experimental scale*.

----

\section{\hfill{}7. Conclusion\hfill{}}
\subsection{\hfill{}Thanks!\hfill{}}
# Conclusion
## We showed numerically...
- After a learning period, MAB algorithms are almost as efficient as the oracle solution,
- Never worse than the naive solution.
- Thompson sampling is even more efficient than UCB.
- Simple algorithms are up-to $16\%$ more efficient than the naive approach, and straightforward to apply.

## But more work is still needed...
- **Theoretical guarantees** are still missing.
- Maybe study **other emission models**.
- And also implement this on **real-world radio devices**.

\hfill{} **Thanks!** *Question?*
