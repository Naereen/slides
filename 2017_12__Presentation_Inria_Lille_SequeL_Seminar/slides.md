---
author:
  \textbf{Lilian Besson} \newline
  \emph{Advised by} \and Christophe Moy \and Émilie Kaufmann
smallauthor: Lilian Besson
title: Multi-Player Bandits Revisited
subtitle: Decentralized Multi-Player Multi-Arm Bandits
institute:
  PhD Student \newline
  Team SCEE, IETR, CentraleSupélec, Rennes \newline
  \& Team SequeL, CRIStAL, Inria, Lille
smallinstitute: CentraleSupélec \& Inria
date: SequeL Seminar  -  22 December 2017
smalldate: SequeL Seminar  -  22/12/17
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

# Motivation
We control some communicating devices,
they want to access to a single base station.

- Insert them in a **crowded wireless network**.
- With a protocol **slotted in both time and frequency**.

## Goal
- Maintain a **good Quality of Service**.
- **Without centralized supervision** as it costs network overhead.

## How?
- Devices can choose a different radio channel at each time \newline
  $\hookrightarrow$ learn the best one with sequential algorithm!

----

\subsection{\hfill{}1.b. Outline and references\hfill{}}

# Outline and reference
\vspace*{-15pt}

1. \invisible{Introduction}
2. Model: 3 different feedback levels
3. Decomposition and lower-bound on regret
4. Quick reminder on single-player MAB algorithms
5. Two new multi-player decentralized algorithms
6. Upper-bounds on regret for \MCTopM
7. Experimental results
8. An heuristic \Selfish, and disappointing results
9. Conclusion

. . .

\vfill{}
\begin{footnotesize}
This is based on my latest article:
\begin{itemize}
\item \emph{Multi-Player Bandits Models Revisited}, Besson \& Kaufmann. \hfill{}\texttt{arXiv:1711.02317}
\end{itemize}
\end{footnotesize}

<!-- \item \emph{Multi-Armed Bandit Learning in IoT Networks and non-stationary settings}, Bonnefoi, Besson, Moy, Kaufmann, Palicot. CrownCom 2017, -->

----

\section{\hfill{}2. Model: 3 different feedback level\hfill{}}

\subsection{\hfill{}2.a. Our model\hfill{}}

# Our model
- $K$ radio channels (\emph{e.g.}, 10)
  \hfill{} (*known*)
- Discrete and synchronized time $t\geq1$. Every time frame $t$ is:

<!-- ![Protocol](figures/protocol.eps) -->
\begin{figure}[h!]
\centering
\includegraphics[height=0.31\textheight]{figures/protocol.eps}
\caption{\small{Protocol in time and frequency, with an \textcolor{darkgreen}{\emph{Acknowledgement}}.}}
\end{figure}

## Dynamic device $=$ dynamic radio reconfiguration
- It decides **each time** the channel it uses to send **each packet**.
- It can implement simple **decision algorithm**.

----

\subsection{\hfill{}2.b. With or without sensing\hfill{}}

# Our model
## "Easy" case
- $M \leq K$ devices **always communicate** and try to access the network,
  *independently* without centralized supervision,
- Background traffic is *i.i.d.*.

## Two variants
1. *With sensing*:
    Device first senses for presence of Primary Users (background traffic), then use `Ack` to detect collisions.
    \small{Model the "classical" Opportunistic Spectrum Access problem.
    Not exactly suited for \emph{Internet of Things}, but can model ZigBee, and can be analyzed mathematically...}
    \pause
2. *Without sensing*: same background traffic, but cannot sense, so only `Ack` is used.
    \small{More suited for "IoT" networks like LoRa or SigFox}
    (Harder to analyze mathematically.)

----

\subsection{\hfill{}2.c. Notations for rewards\hfill{}}

# Notations for rewards
## *i.i.d.* background traffic
- $K$ channels, modeled as Bernoulli ($0/1$) distributions of mean $\mu_k$
  $=$ background traffic from *Primary Users*, bothering the dynamic devices,
- $M$ devices, each uses channel $A^j(t) \in \{1,\dots,K\}$ at time $t$.

## Rewards
$$r^j(t) := Y_{A^j(t),t} \times \mathbbm{1}(\overline{C^j(t)}) = \mathbbm{1}(\text{uplink \& Ack})$$

- with sensing information $Y_{k,t} \overset{\text{iid}}{\sim} \mathrm{Bern}(\mu_k)$,
- collision for device $j$ :
  $C^j(t) = \mathbbm{1}($\emph{alone on arm $A^j(t)$}$)$. \newline
  $\hookrightarrow$ joint binary reward but not from two Bernoulli!

----

\subsection{\hfill{}2.d. Different feedback levels\hfill{}}

# 3 feedback levels
$$r^j(t) := Y_{A^j(t),t} \times \mathbbm{1}(\overline{C^j(t)}) = \mathbbm{1}(\text{uplink \& Ack})$$

1. "Full feedback": observe separately $Y_{k,t}$ and $C^j(t)$, \newline
    $\hookrightarrow$ Not realistic enough, we don't study it.
    \vspace*{10pt}\pause
2. "With sensing": first observe $Y_{k,t}$ and if non-zero, observe $C^j(t)$, \newline
    $\hookrightarrow$ Models licensed protocols like ZigBee, our main focus.
    \vspace*{10pt}\pause
3. "Full feedback": observe only $Y_{k,t} \times \mathbbm{1}(\overline{C^j(t)})$, \newline
    $\hookrightarrow$ Models unlicensed protocols like LoRaWAN, harder to analyze!

But all consider the same instantaneous reward $r^j(t)$.

----

\subsection{\hfill{}2.e. Goal\hfill{}}

# Goal
## Problem
- *Goal* : *minimize packet loss ratio* ($=$ maximize nb of received `Ack`)
  in a *finite-space discrete-time Decision Making Problem*.
- *Solution ?* **Multi-Armed Bandit algorithms**,
  **decentralized** and used **independently** by each dynamic device.

. . .

## *Decentralized* reinforcement learning optimization!
- Max transmission rate $\equiv$ **max cumulated rewards**
  \hspace*{60pt} $\max\limits_{\text{algorithm}\;A} \;\; \sum\limits_{t=1}^{\text{horizon}} \sum\limits_{j=1}^M r^j_{A(t)}$.
- Each player wants to **maximize its cumulated reward**,
- With no central control, and no exchange of information,
- Only possible if : each player converges to one of the $M$ best arms,
  orthogonally (without collisions).

----

\subsection{\hfill{}2.f. Centralized regret\hfill{}}

# Centralized regret
## A measure of success
- Not the network throughput or collision probability,
- We study the **centralized regret**
  \vspace*{-5pt}
  \begin{align*}
  R_T(\boldsymbol{\mu}, M, \rho)
  &:= \E_{\mu}\left[ \sum_{t=1}^T \sum_{j=1}^M \mu_j^* -  r^j(t)\right] \\
  &:= \left(\sum_{k=1}^{M}\mu_k^*\right) T - \E_{\mu}\left[\sum_{t=1}^T\sum_{j=1}^M r^j(t)\right].
  \end{align*}

. . .

## Two directions of analysis
- Clearly $R_T = \mathcal{O}(T)$, but we want a sub-linear regret, as small as possible!
- *How good a decentralized algorithm can be in this setting?* \newline
  \hfill{} $\hookrightarrow$ **Lower Bound** on regret, for **any** algorithm !
- *How good is my decentralized algorithm in this setting?* \newline
  \hfill{} $\hookrightarrow$ **Upper Bound** on regret, for **one** algorithm !

----

\section{\hfill{}3. Lower-bound\hfill{}}

\subsection{\hfill{}3.a. Lower-bound on regret\hfill{}}

# Asymptotic Lower Bound on regret {.allowframebreaks}

## Decomposition
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
- And we lower-bound the rest (including collisions) by... $0$ : we should be able to do better!

## Theorem 1  \hfill{}\textcolor{gray}{[Besson \& Kaufmann, 2017]}
- For any uniformly efficient decentralized policy, and any non-degenerated problem  $\boldsymbol{\mu}$,
\vspace*{-10pt}
$$ \mathop{\lim\inf}\limits_{T \to +\infty} \frac{R_T(\boldsymbol{\mu}, M, \rho)}{\log(T)} \geq M \times \left( \sum_{k \in \Mworst} \frac{(\mu_M^* -  \mu_k)}{\kl(\mu_k, \mu_M^*)} \right) . $$
\footnotetext{\tiny Where $\kl(x,y) := x \log(\frac{x}{y}) + (1 - x) \log(\frac{1-x}{1-y})$ is the binary Kullback-Leibler divergence.}

----

\subsection{\hfill{}3.b. Illustration of the Lower Bound\hfill{}}

# Illustration of the Lower Bound on regret {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.75\textheight]{figures/main_RegretCentralized____env3-4_2092905764868974160.pdf}
\caption{\footnotesize{Any such lower-bound is very asymptotic, usually not satisfied for small horizons. We can see the importance of the collisions!}}
\end{figure}

----

\subsection{\hfill{}3.c. Sketch of the proof\hfill{}}

# Sketch of the proof {.allowframebreaks}

FIXME

----

\section{\hfill{}4. Single-player MAB algorithms : \UCB, \klUCB\hfill{}}

\subsection{\hfill{}4.a. Upper Confidence Bound algorithm : \UCB\hfill{}}

# Upper Confidence Bound algorithm ($\mathrm{UCB}_1$)
Dynamic device keep $t$ number of sent packets, $T_k(t)$ selections of channel $k$, $X_k(t)$ successful transmission in channel $k$.

1. For the first $K$ steps ($t=1,\dots,K$), try each channel *once*.
2. Then for the next steps $t > K$ :
    - Compute the index $g_k(t) := \underbrace{\frac{X_k(t)}{T_k(t)}}_{\text{Mean}\; \widehat{\mu_k}(t)} + \underbrace{\sqrt{\frac{\log(t)}{2 \; T_k(t)}},}_{\text{Upper Confidence Bound}}$
    - Choose channel $A(t) = \mathop{\arg\max}\limits_{k} \; g_k(t)$,
    - Update $T_k(t+1)$ and $X_k(t+1)$.

\vfill{}\hfill{}\tiny{\textcolor{gray}{References: [Lai \& Robbins, 1985], [Auer et al, 2002], [Bubeck \& Cesa-Bianchi, 2012]}}

----

\subsection{\hfill{}4.b. Kullback-Leibler UCB algorithm : \klUCB\hfill{}}

# Kullback-Leibler UCB algorithm ($\mathrm{kl}$-$\mathrm{UCB}$)
Dynamic device keep $t$ number of sent packets, $T_k(t)$ selections of channel $k$, $X_k(t)$ successful transmission in channel $k$.

1. For the first $K$ steps ($t=1,\dots,K$), try each channel *once*.
2. Then for the next steps $t > K$ :
    - Compute the index $g_k(t) := \sup\limits_{q \in [a, b]} \left\{ q : \mathrm{kl}(\frac{X_k(t)}{N_k(t)}, q) \leq \frac{\log(t)}{N_k(t)} \right\}$
    - Choose channel $A(t) = \mathop{\arg\max}\limits_{k} \; g_k(t)$,
    - Update $T_k(t+1)$ and $X_k(t+1)$.

$\hookrightarrow$ proved to be more efficient than \UCB,
and asymptotically optimal for single-player stochastic bandit.

\vfill{}\hfill{}\tiny{\textcolor{gray}{References: [Garivier \& Cappé, 2011], [Cappé \& Garivier \& Maillard \& Munos \& Stoltz, 2013]}}

----

\section{\hfill{}5. Multi-player decentralized algorithms: \MCTopM, \RandTopM, \Selfish{} \hfill{}}
\subsection{\hfill{}5.a. State-of-the-art MP algorithms\hfill{}}

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

\subsection{\hfill{}5.b. \RandTopM{} algorithm\hfill{}}
# The \RandTopM{} algorithm

FIXME include code, explain??

----

\subsection{\hfill{}5.c. \MCTopM{} algorithm\hfill{}}
# The \MCTopM{} algorithm

FIXME include code, explain
FIXME include figure, explain

----

\section{\hfill{}6. Regret upper-bound\hfill{}}
\subsection{\hfill{}6.a. \MCTopM-\klUCB\hfill{}}

# Regret upper-bound for \MCTopM-\klUCB

## Theorem 2  \hfill{}\textcolor{gray}{[Besson \& Kaufmann, 2017]}
- If all $M$ players use \MCTopM-\klUCB,
then for any non-degenerated problem $\boldsymbol{\mu}$,
there exists a problem dependent constant $G_{M,\boldsymbol{\mu}}$
, such that the regret satisfies:
$$
  R_T(\boldsymbol{\mu}, M, \rho) \leq G_{M,\boldsymbol{\mu}} \log(T) + \smallO{\log T}.
$$

## Remarks
- Hard to prove, we had to carefully design the \MCTopM{} algorithm to conclude the proof,
- We have doubts regarding the proofs and results of all the previously proposed algorithms,
- For the suboptimal selections, we *match our lower-bound* !
- We also *minimize the number of channel switching*: interesting as it costs energy,
- Not yet possible to know what is the best possible control of collisions...

----

\subsection{\hfill{}6.b. Sketch of the proof\hfill{}}

# Sketch of the proof {.allowframebreaks}

FIXME

----

\section{\hfill{}7. Experimental results\hfill{}}
\subsection{\hfill{}7.a. Illustration of regret\hfill{}}

# Constant collisions if $M=K$ {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.75\textheight]{figures/MP__K9_M9_T10000_N200__4_algos/all_RegretCentralized____env1-1_2306423191427933958.pdf}
\caption{\footnotesize{Regret, $M=9$ players, $K=9$ arms, horizon $T=10000$, $200$ repetitions. Only \textcolor{red}{\RandTopM{}} and \textcolor{gold}{\MCTopM{}} achieve constant regret in this saturated case.}}
\end{figure}

# Illustration of regret of different algorithms {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.75\textheight]{figures/MP__K9_M6_T5000_N500__4_algos/all_RegretCentralized____env1-1_8318947830261751207.pdf}
\caption{\footnotesize{Regret, $M=6$ players, $K=9$ arms, horizon $T=5000$, against $500$ problems $\boldsymbol{\mu}$ uniformly sampled in $[0,1]^K$. \newline \textcolor{blue}{\rhoRand{}} < \textcolor{red}{\RandTopM{}} < \textcolor{darkgreen}{\Selfish{}} < \textcolor{gold}{\MCTopM{}} in most cases.}}
\end{figure}

\subsection{\hfill{}7.c. Number of collisions\hfill{}}

# Number of collisions {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.75\textheight]{figures/MP__K9_M6_T5000_N500__4_algos/all_CumNbCollisions____env1-1_8318947830261751207.pdf}
\caption{\footnotesize{Cumulated number of collisions, $M=6$ players, $K=9$ arms, horizon $T=5000$, against $500$ problems $\boldsymbol{\mu}$ uniformly sampled in $[0,1]^K$. \newline Also \textcolor{blue}{\rhoRand{}} < \textcolor{red}{\RandTopM{}} < \textcolor{darkgreen}{\Selfish{}} < \textcolor{gold}{\MCTopM{}} in most cases.}}
\end{figure}

\subsection{\hfill{}7.d. Number of arm switches\hfill{}}

# Logarithmic number of arm switches {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.75\textheight]{figures/MP__K9_M6_T5000_N500__4_algos/all_CumNbSwitchs____env1-1_8318947830261751207.pdf}
\caption{\footnotesize{Cumulated number of arm switches, $M=6$ players, $K=9$ arms, horizon $T=5000$, against $500$ problems $\boldsymbol{\mu}$ uniformly sampled in $[0,1]^K$. \newline Again \textcolor{blue}{\rhoRand{}} < \textcolor{red}{\RandTopM{}} < \textcolor{darkgreen}{\Selfish{}} < \textcolor{gold}{\MCTopM{}}, but no guarantee for \textcolor{blue}{\rhoRand{}}.}}
\end{figure}

\subsection{\hfill{}7.e. Fairness\hfill{}}

# Fairness {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.75\textheight]{figures/MP__K9_M6_T5000_N500__4_algos/all_FairnessSTD____env1-1_8318947830261751207.pdf}
\caption{\footnotesize{Measure of fairness among player. All $4$ algorithms seem fair \textbf{in average}, but none is fair on a single run. It's quite hard to achieve both effiency and single-run fairness!}}
\end{figure}

----

\section{\hfill{}8. An heuristic \Selfish\hfill{}}
\subsection{\hfill{}8.a. Problems with \Selfish\hfill{}}

# The \Selfish{} heuristic {.allowframebreaks}
The \Selfish{} decentralized approach = device don't use sensing, just learn on the receive acknowledgement.

## Works fine...
- More suited to model IoT networks,
- Use less information, and don't know the value of $M$: we expect \Selfish{} to not have stronger guarantees.
- It works fine in practice!

## *But why would it work?*
- Sensing was *i.i.d.* so using \UCB{} to learn the $\mu_k$ makes sense,
- But collisions are not *i.i.d.*,
- Adversarial algorithms are more appropriate here,
- But empirically, \Selfish{} with \UCB{} or \klUCB{} works much better than, *e.g.*, \ExpThree...

## Works fine...
- Except... when it fails drastically!
- In small problems with $M$ and $K = 2$ or $3$, we found small probability of failures (*i.e.*, linear regret), and this prevents from having a generic upper-bound on regret for \Selfish. Sadly...

----

\subsection{\hfill{}8.b. Failing cases for \Selfish\hfill{}}
# Illustration of failing cases for $\mathrm{Selfish}$ {.plain}

\begin{figure}[h!]
\centering
\includegraphics[height=0.65\textheight]{figures/MP__K3_M2_T5000_N1000__4_algos/all_HistogramsRegret____env1-1_5016720151160452442.pdf}
\caption{\footnotesize{Regret for $M=2$ players, $K=3$ arms, horizon $T=5000$, $1000$ repetitions and $\boldsymbol{\mu} = [0.1, 0.5, 0.9]$. Axis $x$ is for regret (different scale for each), and \textcolor{darkgreen}{\Selfish{}} have a small probability of failure ($17/1000$ cases of $R_T \gg \log T$). The regret for the three other algorithms is very small for this "easy" problem.}}
\end{figure}

----

\section{\hfill{}9. Conclusion\hfill{}}
\subsection{\hfill{}9.a. Perspectives\hfill{}}

# Perspectives
## *Wait, what was the problem ?*
- MAB algorithms have guarantees for *i.i.d. settings*,
- But here the collisions cancel the *i.i.d.* hypothesis...
- Not easy to obtain guarantees in this mixed setting \newline
  (*i.i.d.* emissions process, "game theoretic" collisions).

## Theoretical results
- With sensing ("OSA"), we obtained strong results: a lower-bound, and an order-optimal algorithm,
- But without sensing ("IoT"), it is harder... our heuristic \Selfish{} usually works but can fail!

----

\subsection{\hfill{}9.b. Future work\hfill{}}

# Other directions of future work

## Conclude the Multi-Player OSA analysis
- Remove hypothesis that objects know $M$,
- Allow arrival/departure of objects,
- Non-stationarity of background traffic etc

- *More realistic emission model*:
  maybe driven by number of packets in a whole day,
  instead of emission probability.

## Extend to more objects $M > K$
- Extend the theoretical analysis to the large-scale IoT model,
  first with sensing (*e.g.*, models ZigBee networks),
  then without sensing (*e.g.*, LoRaWAN networks).

----

\subsection{\hfill{}9.c. Thanks!\hfill{}}

# Conclusion {.allowframebreaks}

- In a wireless network with an *i.i.d.* background traffic in $K$ channels,
- $M$ devices can use both sensing and acknowledgement feedback, to learn the most free channels and to find orthogonal configurations.

## We showed
- Decentralized bandit algorithms can solve this problem,
- We have a lower-bound for any decentralized algorithm,
- And we proposed an order-optimal algorithm, based on \klUCB{} and an improved Musical Chair scheme, \MCTopM

## But more work is still needed...
- **Theoretical guarantees** are still missing for the "IoT" model (without sensing), and can be improved (slightly) for the "OSA" model (with sensing).
- Maybe study **other emission models**...
- Implement and test this on **real-world radio devices** \newline
  \hspace*{20pt} $\hookrightarrow$ demo (in progress) for the ICT $2018$ conference!

## **Thanks!**
\begin{center}\begin{Large}
\emph{Any question or idea ?}
\end{Large}\end{center}
