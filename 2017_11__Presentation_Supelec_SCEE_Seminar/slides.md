---
author:
  \textbf{Lilian Besson} \newline
   \emph{Advised by} \and Christophe Moy \and Émilie Kaufmann
smallauthor: Lilian Besson
title: MAB Learning in IoT Networks
subtitle: Decentralized Multi-Player Multi-Arm Bandits
institute:
  PhD Student \newline
  Team SCEE, IETR, CentraleSupélec, Rennes \newline
  \& Team SequeL, CRIStAL, Inria, Lille
smallinstitute: CentraleSupélec \& Inria
date: SCEE Seminar  -  23 November 2017
smalldate: SCEE Seminar  -  23/11/17
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

# Motivation: *Internet of Things* problem
A *lot* of IoT devices want to access to a single base station.

- Insert them in a possibly **crowded wireless network**.
- With a protocol **slotted in both time and frequency**.
- Each device has a **low duty cycle**
  (a few messages per day).

. . .

## Goal
- Maintain a **good Quality of Service**.
- **Without** centralized supervision!

. . .

## How?
- Use **learning algorithms**:
  devices will learn on which frequency they should talk!

----

\subsection{\hfill{}1.b. Outline and references\hfill{}}

# Outline and references
1. Introduction and motivation
2. Model and hypotheses
3. Baseline algorithms :
   to compare against naive and efficient centralized approaches
4. Two Multi-Armed Bandit algorithms : UCB, TS
5. Experimental results
6. An easier model with theoretical results
7. Perspectives and future works

\vfill{}
\begin{footnotesize}
Main references are my recent articles (on HAL):
\begin{itemize}
\item \emph{Multi-Armed Bandit Learning in IoT Networks and non-stationary settings}, Bonnefoi, Besson, Moy, Kaufmann, Palicot. CrownCom 2017,
\item \emph{Multi-Player Bandits Models Revisited}, Besson, Kaufmann. arXiv:1711.02317,
\end{itemize}
\end{footnotesize}

----

\section{\hfill{}2. Model and hypotheses\hfill{}}

\subsection{\hfill{}2.a. First model\hfill{}}

# First model
- Discrete time $t\geq1$ and $K$ radio channels (\emph{e.g.}, 10)
  \hfill{} (*known*)

<!-- ![Protocol](crowncom/protocol.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[height=0.35\textheight]{crowncom/protocol.eps}
\caption{\small{Protocol in time and frequency, with an \textcolor{darkgreen}{\emph{Acknowledgement}}.}}
\end{figure}

- $D$ **dynamic** devices try to access the network *independently*
- $S=S_1+\dots+S_{K}$ **static** devices occupy the network : \newline
  $S_1,\dots,S_{K}$ in each channel
  \hfill{} (*unknown*)

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
- It has memory and computational capacity to implement simple **decision algorithm**.

## Problem
- *Goal* : *minimize packet loss ratio* ($=$ maximize number of received `Ack`)
  in a *finite-space discrete-time Decision Making Problem*.
- *Solution ?* **Multi-Armed Bandit algorithms**,
  **decentralized** and used **independently** by each device.

----

\section{\hfill{}3. Baseline algorithms\hfill{}}

\subsection{\hfill{}3.a. A naive strategy : uniformly random access\hfill{}}

# A naive strategy : uniformly random access
- **Uniformly random access**:
  dynamic devices choose uniformly their channel in the pull of $K$ channels.
- Natural strategy, dead simple to implement.

- Simple analysis, in term of **successful transmission probability** (for every message from dynamic devices) :

\begin{small} \begin{align*}
\mathbb{P}(\text{success}|\text{sent}) = \sum_{i=1}^{K} \underbrace{(1 - p / K)^{D-1}}_{\text{No other dynamic device}} \times \underbrace{(1-p)^{S_i}}_{\text{No static device}} \times\; \frac{1}{K}.
\end{align*} \end{small}

. . .

## No learning
- Works fine only if all channels are similarly occupied,\newline
  but **it cannot learn** to exploit the best (more free) channels.

----

\subsection{\hfill{}3.b. Optimal centralized strategy\hfill{}}

# Optimal centralized strategy {.allowframebreaks}
- If an oracle can decide to affect $D_i$ dynamic devices to channel $i$,
  the **successful transmission probability** is:
\vspace*{-10pt}
\begin{small} \begin{align*}
\mathbb{P}(\text{success}|\text{sent}) = \sum_{i=1}^{K} \underbrace{(1 - p)^{D_i - 1}}_{\;\;D_i - 1 \;\text{others}\;\;} \times \underbrace{(1 - p)^{S_i}}_{\;\;\text{No static device}\;\;} \times \underbrace{ D_i / D }_{\;\;\text{Sent in channel}\; i}.
\end{align*} \end{small}

- The oracle has to solve this **optimization problem**:
\vspace*{-5pt}
\begin{small} \begin{equation*} \begin{cases}
\underset{D_1,\dots,D_{K}}{\arg\max}\;\;\; & \sum_{i=1}^{K} D_i (1 - p)^{S_i + D_i -1}\\
\text{such that}\;\;\; & \sum_{i=1}^{K} D_i = D \; \text{and} \; D_i \geq 0, \; \; \forall 1 \leq i \leq K .
\end{cases} \end{equation*} \end{small}

- We solved this quasi-convex optimization problem with *Lagrange multipliers*, only numerically.
- $\implies$ Very good performance, maximizing the transmission rate of all the $D$ dynamic devices

## But unrealistic
But **not achievable in practice**: no centralized control and no oracle!

## Now let see *realistic decentralized approaches*
$\hookrightarrow$ Machine Learning ? \newline
\hspace*{30pt}$\hookrightarrow$ Reinforcement Learning ? \newline
\hspace*{60pt} $\hookrightarrow$ *Multi-Armed Bandit* !

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

- it transmits following a Bernoulli process \newline
  (probability $p$ of transmitting at each time step $t$),
- chooses a channel $A(\tau) \in \{1,\dots,K\}$,
    * if `Ack` (no collision)
      \hspace*{10pt} $\implies$ reward $r_{A(\tau)} = 1$,
    * if collision (no `Ack`)
      \hspace*{10pt} $\implies$ reward $r_{A(\tau)} = 0$.

<!-- - if the message is successfully sent (no collision), it receives an `Ack` -->

## Reinforcement Learning interpretation
Maximize transmission rate $\equiv$ **maximize cumulated rewards**
$$\max_{\text{algorithm}\;A} \;\; \sum_{\tau=1}^{\text{horizon}} r_{A(\tau)}.$$

----

\subsection{\hfill{}4.2. Upper Confidence Bound algorithm : UCB\hfill{}}

# Upper Confidence Bound algorithm ($\mathrm{UCB}_1$)
Dynamic device keep $\tau$ number of sent packets, $T_k(\tau)$ selections of channel $k$, $X_k(\tau)$ successful transmission in channel $k$.

1. For the first $K$ steps ($\tau=1,\dots,K$), try each channel *once*.
2. Then for the next steps $t > K$ :
    - Compute the index $g_k(\tau) := \underbrace{\frac{X_k(\tau)}{T_k(\tau)}}_{\text{Mean}\; \widehat{\mu_k}(\tau)} + \underbrace{\sqrt{\frac{\log(\tau)}{2 T_k(\tau)}},}_{\text{Upper Confidence Bound}}$
    - Choose channel $A(\tau) = \mathop{\arg\max}\limits_{k} \; g_k(\tau)$,
    - Update $T_k(\tau+1)$ and $X_k(\tau+1)$.

\vfill{}\hfill{}\tiny{\textcolor{gray}{References: [Lai \& Robbins, 1985], [Auer et al, 2002], [Bubeck \& Cesa-Bianchi, 2012]}}

----

\subsection{\hfill{}4.3. Thompson Sampling : Bayesian index policy\hfill{}}

# Thompson Sampling : Bayesian approach
A dynamic device assumes a stochastic hypothesis on the background traffic, modeled as Bernoulli distributions.

- Rewards $r_k(\tau)$ are assumed to be *i.i.d.* samples from a Bernoulli distribution $\mathrm{Bern}(\mu_k)$.

- A **binomial Bayesian posterior** is kept on the mean availability $\mu_k$ : $\mathrm{Bin}(1 + X_k(\tau), 1 + T_k(\tau) - X_k(\tau))$.
- Starts with a *uniform prior* : $\mathrm{Bin}(1, 1) \sim \mathcal{U}([0,1])$.

1. Each step $\tau \geq 1$, draw a sample from each posterior
  $i_k(\tau) \sim \mathrm{Bin}(a_k(\tau), b_k(\tau))$,
2. Choose channel $A(\tau) = \mathop{\arg\max}\limits_k \; i_k(\tau)$,
3. Update the posterior after receiving `Ack` or if collision.


\vfill{}\hfill{}\tiny{\textcolor{gray}{References: [Thompson, 1933], [Kaufmann et al, 2012]}}

----

\section{\hfill{}5. Experimental results\hfill{}}

\subsection{\hfill{}5.1. Experiment setting\hfill{}}

# Experimental setting

## Simulation parameters
- $K = 10$ channels,
- $S + D = 10000$ devices **in total**.
  Proportion of dynamic devices $D/(S+D)$ varies,
- $p = 10^{-3}$ probability of emission, for all devices,
- Horizon $= 10^6$ time slots, \hfill{} ($\simeq 1000$ messages $/$ device)
- Various settings for $(S_1,\dots,S_{K})$ static devices repartition.

## What do we show \hfill{} (for static $S_i$)
- After a short learning time, MAB algorithms are almost as efficient as the oracle solution !
- Never worse than the naive solution.
- Thompson sampling is more efficient than UCB.
- Stationary alg. outperform adversarial ones (UCB $\gg$ Exp3).

----

\subsection{\hfill{}5.2. First result: $10\%$\hfill{}}

# $10\%$ of dynamic devices

<!-- ![$10\%$ of dynamic devices](crowncom/10intelligent.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[height=0.74\textheight]{crowncom/10intelligent.eps}
\caption{\small{$10\%$ of dynamic devices. $7\%$ of gain.}}
\end{figure}

----

\subsection{\hfill{}5.2. First result: $20\%$\hfill{}}

# $30\%$ of dynamic devices

<!-- ![$30\%$ of dynamic devices](crowncom/30intelligent.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[height=0.74\textheight]{crowncom/30intelligent.eps}
\caption{\small{$30\%$ of dynamic devices. $3\%$ of gain but not much is possible.}}
\end{figure}

----

\subsection{\hfill{}5.3. Growing proportion of devices dynamic devices\hfill{}}

# Dependence on $D/(S+D)$

<!-- ![Growing proportion of devices dynamic devices](crowncom/perf_learning.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[height=0.65\textheight]{crowncom/perf_learning.eps}
\caption{\small{\emph{Almost optimal}, for any proportion of dynamic devices, \emph{after a short learning time}. Up-to $16\%$ gain over the naive approach!}}
\end{figure}

----

\section{\hfill{}6. An easier model\hfill{}}

# Section 6

\begin{center}
A brief presentation of a different approach...

Theoretical results for an easier model
\end{center}

----

\subsection{\hfill{}6.1. Presentation of the model\hfill{}}

# An easier model

## Easy case
- $M \leq K$ dynamic devices **always communicating** ($p=1$).
- Still interesting: many mathematical and experimental results!

. . .

## Two variants
- *With sensing*: Device first senses for presence of Primary Users (background traffic), then use `Ack` to detect collisions.
    \small{Model the "classical" Opportunistic Spectrum Access problem. Not exactly suited for IoT networks like LoRa or SigFox, can model ZigBee, and can be analyzed mathematically...}

    \hfill{}{\small{\textcolor{gray}{(\emph{cf} Wassim's and Navik's theses, 2012, 2017)}}}
- *Without sensing*: like our IoT model but smaller scale. Still very hard to analyze mathematically.

----

\subsection{\hfill{}6.2. Notations\hfill{}}

# Notations for this second model

## Notations
- $K$ channels, modeled as Bernoulli ($0/1$) distributions of mean $\mu_k$
  $=$ background traffic from *Primary Users*,
- $M$ devices use channel $A^j(t) \in \{1,\dots,K\}$ at each time step,
- Reward: $r^j(t) := Y_{A^j(t),t} \times \mathbbm{1}(\overline{C^j(t)}) = \mathbbm{1}($uplink \& `Ack`$)$
    + with sensing information $Y_{k,t} \sim \mathrm{Bern}(\mu_k)$,
    + collision for device $j$
      $C^j(t) = \mathbbm{1}($\emph{alone on arm $A^j(t)$}$)$.

. . .

## Goal : *decentralized* reinforcement learning optimization!
- Each player wants to **maximize its cumulated reward**,
- With no central control, and no exchange of information,
- Only possible if : each player converges to one of the $M$ best arms,
  orthogonally (without collisions)

----

\subsection{\hfill{}6.2. Centralized regret\hfill{}}

# Centralized regret
## New measure of success
- Not the network throughput or collision probability,
- Now we study the **centralized regret**
  \vspace*{-5pt}
  $$ R_T(\boldsymbol{\mu}, M, \rho) := \left(\sum_{k=1}^{M}\mu_k^*\right) T - \E_{\mu}\left[\sum_{t=1}^T\sum_{j=1}^M r^j(t)\right]. $$

. . .

## Two directions of analysis
- Clearly $R_T = \mathcal{O}(T)$, but we want a sub-linear regret
- *What is the best possible performance of a decentralized algorithm in this setting?* \newline
  \hfill{} $\hookrightarrow$ **Lower Bound** on regret for **any** algorithm !
- *Is this algorithm efficient in this setting?* \newline
  \hfill{} $\hookrightarrow$ **Upper Bound** on regret for **one** algorithm !

----

\subsection{\hfill{}6.3. Lower Bound on regret\hfill{}}

# Asymptotic Lower Bound on regret {.allowframebreaks}

For any algorithm, decentralized or not, we have
\vspace*{-20pt}
\begin{small}\begin{align*}
R_T(\boldsymbol{\mu}, M, \rho) &= \sum_{k \in \Mworst} (\mu_M^* -  \mu_k) \E_{\mu}[T_k(T)] \\
&+ \sum_{k \in \Mbest} (\mu_k -  \mu_M^*) (T - \E_{\mu}[T_k(T)]) + \sum_{k=1}^{K} \mu_k \E_{\mu}[\mathcal{C}_k(T)].
\end{align*}\end{small}

## Small regret can be attained if...
1. Devices can quickly identify the bad arms $\Mworst$, and not play them too much
   (*number of sub-optimal selections*),
2. Devices can quickly identify the best arms, and most surely play them
   (*number of optimal non-selections*),
3. Devices can use orthogonal channels
   (*number of collisions*).

## Lower-bounds
- The first term $\E_{\mu}[T_k(T)]$,
  for sub-optimal arms selections, is lower-bounded,
  using technical information theory tools
  (Kullback-Leibler divergence, entropy),
- And we lower-bound collisions by... $0$ : hard to do better!

## Theorem 1  \hfill{}\textcolor{gray}{[Besson \& Kaufmann, 2017]}
- For any uniformly efficient decentralized policy, and any non-degenerated problem  $\boldsymbol{\mu}$,
\vspace*{-10pt}
$$ \mathop{\lim\inf}\limits_{T \to +\infty} \frac{R_T(\boldsymbol{\mu}, M, \rho)}{\log(T)} \geq M \times \left( \sum_{k \in \Mworst} \frac{(\mu_M^* -  \mu_k)}{\kl(\mu_k, \mu_M^*)} \right) . $$
\footnotetext{\tiny Where $\kl(x,y) := x \log(\frac{x}{y}) + (1 - x) \log(\frac{1-x}{1-y})$ is the binary Kullback-Leibler divergence.}

----

# Illustration of the Lower Bound on regret {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.75\textheight]{alt/figures/main_RegretCentralized____env3-4_2092905764868974160.pdf}
\caption{\footnotesize{Any such lower-bound is very asymptotic, usually not satisfied for small horizons. We can see the importance of the collisions!}}
\end{figure}

----

\subsection{\hfill{}6.4. Algorithms\hfill{}}

# Algorithms for this easier model

## Building blocks : separate the two aspects
1. **MAB policy** to learn the best arms (use sensing $Y_{A^j(t),t}$),
2. **Orthogonalization scheme** to avoid collisions (use $C^j(t)$).

. . .

## Many different proposals for *decentralized* learning policies
- Recent: \MEGA{} and \MusicalChair{}, \hfill{}{\tiny \textcolor{gray}{[Avner \& Mannor, 2015], [Shamir et al, 2016]}}
- State-of-the-art: **RhoRand policy** and variants, \hfill{}{\tiny \textcolor{gray}{[Anandkumar et al, 2011]}}
- **Our proposals**: \hfill{}{\tiny \textcolor{gray}{[Besson \& Kaufmann, 2017]}}
    + With sensing: \RandTopM{} and \MCTopM{} are sort of mixes between RhoRand and \MusicalChair{}, using UCB indexes or more efficient index policy (\klUCB),
    + Without sensing: \Selfish{} use a UCB index directly on the reward $r^j(t)$ : like the first IoT model !

----

# Illustration of different algorithms {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.75\textheight]{alt/figures/MP__K9_M6_T5000_N500__4_algos/all_RegretCentralized____env1-1_8318947830261751207.pdf}
\caption{\footnotesize{Regret, $M=6$ players, $K=9$ arms, horizon $T=5000$, against $500$ problems $\boldsymbol{\mu}$ uniformly sampled in $[0,1]^K$. \newline \textcolor{blue}{\rhoRand{}} < \textcolor{red}{\RandTopM{}} < \textcolor{darkgreen}{\Selfish{}} < \textcolor{gold}{\MCTopM{}} in most cases.}}
\end{figure}

----

\subsection{\hfill{}6.5. Regret upper-bound\hfill{}}

# Regret upper-bound for \MCTopM-\klUCB

## Theorem 2  \hfill{}\textcolor{gray}{[Besson \& Kaufmann, 2017]}
- If all $M$ players use \MCTopM-\klUCB,
then for any non-degenerated problem $\boldsymbol{\mu}$,
<!-- there exists a problem dependent constant $G_{M,\boldsymbol{\mu}}$ -->
<!-- , such that the regret satisfies: -->
$$
  R_T(\boldsymbol{\mu}, M, \rho) \leq G_{M,\boldsymbol{\mu}} \log(T) + \smallO{\log T}.
$$

## Remarks
- Hard to prove, we had to carefully design the \MCTopM{} algorithm to conclude the proof,
<!-- - We have doubts regarding the proofs and results of all the previously proposed algorithms, -->
- For the suboptimal selections, we *match our lower-bound* !
- We also *minimize the number of channel switching*: interesting as it costs energy,
- Not yet possible to know what is the best possible control of collisions...

----

\subsection{\hfill{}6.6. Problems with \Selfish\hfill{}}

# In this model
The \Selfish{} decentralized approach = device don't use sensing, just learn on the receive acknowledgement,

- Like our first IoT model,
- It works fine in practice!
- Except... when it fails drastically!
- In small problems with $M$ and $K = 2$ or $3$, we found small probability of failures (*i.e.*, linear regret), and this prevents from having a generic upper-bound on regret for \Selfish. Sadly...

----

# Illustration of failing cases for $\mathrm{Selfish}$ {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.60\textheight]{alt/figures/MP__K3_M2_T5000_N1000__4_algos/all_HistogramsRegret____env1-1_5016720151160452442.pdf}
\caption{\footnotesize{Regret for $M=2$ players, $K=3$ arms, horizon $T=5000$, $1000$ repetitions and $\boldsymbol{\mu} = [0.1, 0.5, 0.9]$. Axis $x$ is for regret (different scale for each), and \textcolor{darkgreen}{\Selfish{}} have a small probability of failure ($17$ cases of $R_T \geq T$, out of $1000$). The regret for the three other algorithms is very small for this ``easy'' problem.}}
\end{figure}

----

\section{\hfill{}7. Perspectives and future work\hfill{}}

\subsection{\hfill{}7.1. Perspectives\hfill{}}

# Perspectives
## Theoretical results
- MAB algorithms have guarantees for *i.i.d. settings*,
- But here the collisions cancel the *i.i.d.* hypothesis,
- Not easy to obtain guarantees in this mixed setting \newline
  (*i.i.d.* emissions process, ``game theoretic'' collisions).
- For OSA devices (always emitting), we obtained strong theoretical results,
- But harder for IoT devices with low duty-cycle...

## Real-world experimental validation ?
- Radio experiments will help to validate this.
  \hspace*{40pt}\hfill{}\textcolor{red}{Hard !}

----

\subsection{\hfill{}7.2. Future work\hfill{}}

# Other directions of future work
- *More realistic emission model*:
  maybe driven by number of packets in a whole day,
  instead of emission probability.

- Validate this on a *larger experimental scale*.

- Extend the theoretical analysis to the large-scale IoT model,
  first with sensing (*e.g.*, models ZigBee networks),
  then without sensing (*e.g.*, LoRaWAN networks).

- And also conclude the Multi-Player OSA analysis (remove hypothesis that objects know $M$, allow arrival/departure of objects, non-stationarity of background traffic etc)

----

\section{\hfill{}7. Conclusion\hfill{}}
\subsection{\hfill{}7.3 Thanks!\hfill{}}

# Conclusion {.allowframebreaks}
## We showed
- Simple Multi-Armed Bandit algorithms, used in a Selfish approach by IoT devices in a crowded network, help to quickly learn the best possible repartition of dynamic devices in a fully decentralized and automatic way,
- For devices with sensing, smarter algorithms can be designed, and analyze carefully.
- Empirically, even if the collisions break the *i.i.d* hypothesis, stationary MAB algorithms (UCB, TS, \klUCB) outperform more generic algorithms (adversarial, like Exp3).

## But more work is still needed...
- **Theoretical guarantees** are still missing for the IoT model, and can be improved (slightly) for the OSA model.
- Maybe study **other emission models**.
- Implement this on **real-world radio devices** (\textcolor{rouge}{\emph{TestBed}}).

## **Thanks!**
\begin{center}\begin{Large}
\emph{Any question?}
\end{Large}\end{center}
