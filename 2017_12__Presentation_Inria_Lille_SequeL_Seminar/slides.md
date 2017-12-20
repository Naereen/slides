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
- **With no centralized control** as it costs network overhead.

## How?
- Devices can choose a different radio channel at each time
  \hook learn the best one with sequential algorithm!

----

\subsection{\hfill{}1.b. Outline and references\hfill{}}

# Outline \uncover<2>{and reference}
\vspace*{-15pt}

1. \invisible{Introduction}
2. Our model: $3$ different feedback levels
3. Decomposition and lower bound on regret
4. Quick reminder on single-player MAB algorithms
5. Two new multi-player decentralized algorithms
6. Upper bounds on regret for \MCTopM
7. Experimental results
8. An heuristic (\Selfish), and disappointing results
9. Conclusion

. . .

\vfill{}
\begin{footnotesize}
This is based on our latest article:
\begin{itemize}
\item \emph{"Multi-Player Bandits Models Revisited"}, Besson \& Kaufmann. \hspace*{90pt}\texttt{\textcolor{blue}{\href{https://arXiv.org/abs/1711.02317}{arXiv:1711.02317}}}
\end{itemize}
\end{footnotesize}

<!-- \item \emph{Multi-Armed Bandit Learning in IoT Networks and non-stationary settings}, Bonnefoi, Besson, Moy, Kaufmann, Palicot. CrownCom 2017, -->

----

\section{\hfill{}2. Our model: $3$ different feedback level\hfill{}}

\subsection{\hfill{}2.a. Our model\hfill{}}

# Our model
- $K$ radio channels (\eg, 10)
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
- It can implement a simple **decision algorithm**.

----

\subsection{\hfill{}2.b. With or without sensing\hfill{}}

# Our model
## "Easy" case
- $M \leq K$ devices **always communicate** and try to access the network,
  *independently* without centralized supervision,
- Background traffic is \iid.

## Two variants : with or without *sensing*
1. *With sensing*:
    Device first senses for presence of Primary Users (background traffic), then use `Ack` to detect collisions.
    \begin{quote}
    \small{Model the "classical" Opportunistic Spectrum Access problem.
    Not exactly suited for \emph{Internet of Things}, but can model ZigBee, and can be analyzed mathematically...}
    \end{quote}
    \pause
2. *Without sensing*: same background traffic, but cannot sense, so only `Ack` is used.
    \small{More suited for "IoT" networks like LoRa or SigFox}
    (Harder to analyze mathematically.)

----

\subsection{\hfill{}2.c. Notations for rewards\hfill{}}

# Notations for rewards
## \iid{} background traffic
- $K$ channels, modeled as Bernoulli ($0/1$) distributions of mean $\mu_k$
  $=$ background traffic from *Primary Users*, bothering the dynamic devices,
- $M$ devices, each uses channel $A^j(t) \in \{1,\dots,K\}$ at time $t$.

## Rewards
$$r^j(t) := Y_{A^j(t),t} \alert{\times} \mathbbm{1}(\overline{C^j(t)}) = \mathbbm{1}(\text{uplink \alert{\&} Ack})$$

- with sensing information $\forall k, \;\; Y_{k,t} \overset{\text{iid}}{\sim} \mathrm{Bern}(\mu_k) \in \{0, 1\}$,
- collision for device $j$ :
  $C^j(t) = \mathbbm{1}($\emph{alone on arm $A^j(t)$}$)$.
  \hook \alert{joint} binary reward **but not** from two Bernoulli!

----

\subsection{\hfill{}2.d. Different feedback levels\hfill{}}

# 3 feedback levels
\only<1>{$$r^j(t) := \textcolor{red}{Y_{A^j(t),t}} \times \textcolor{blue}{\mathbbm{1}(\overline{C^j(t)})}$$}
\only<2>{$$r^j(t) := \textcolor{RougeFort}{Y_{A^j(t),t}} \times \textcolor{Rouge}{\mathbbm{1}(\overline{C^j(t)})}$$}
\only<3>{$$r^j(t) := \textcolor{Violet}{Y_{A^j(t),t} \times \mathbbm{1}(\overline{C^j(t)})}$$}
\only<4>{$$\alert{r^j(t)} := Y_{A^j(t),t} \times \mathbbm{1}(\overline{C^j(t)})$$}

1. "Full \textcolor<1>{red}{feed}\textcolor<1>{blue}{back}": observe both \textcolor<1>{red}{$Y_{A^j(t),t}$} \emph{and} \textcolor<1>{blue}{$C^j(t)$} separately,
    \hook Not realistic enough, we don't focus on it.
    \vspace*{10pt}\pause
2. \textcolor<2>{RougeFort}{"Sensing"}: first observe $\textcolor<2>{RougeFort}{Y_{A^j(t),t}}$, \emph{then} $\textcolor<2>{Rouge}{C^j(t)}$ only if $\textcolor<2>{RougeFort}{Y_{A^j(t),t}} \neq 0$,
    \hook Models licensed protocols (ex. ZigBee), our main focus.
    \vspace*{10pt}\pause
3. \textcolor<3>{Violet}{"No sensing"}: observe only the joint $\textcolor<3>{Violet}{Y_{A^j(t),t} \times \mathbbm{1}(\overline{C^j(t)})}$,
    \hook Unlicensed protocols (ex. LoRaWAN), harder to analyze !

\uncover<4>{\begin{quote}But all consider the same instantaneous \alert{reward $r^j(t)$}.\end{quote}}

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
  \hspace*{0.25\textwidth}$\max\limits_{\text{algorithm}\;A} \;\; \sum\limits_{t=1}^{T} \sum\limits_{j=1}^M r^j_{A(t)}$.
- Each player wants to **maximize its cumulated reward**,
- With no central control, and no exchange of information,
- Only possible if : each player converges to one of the $M$ best arms,
  orthogonally (without collisions).

----

\subsection{\hfill{}2.f. Centralized regret\hfill{}}

# Centralized regret
## A measure of success
- Not the network throughput or collision probability,
- We study the **centralized** (expected) **regret**:

\begin{small}\vspace*{-20pt}
  $$R_T(\boldsymbol{\mu}, M, \rho)
  := \E_{\mu}\left[ \sum_{t=1}^T \sum_{j=1}^M \mu_j^* -  r^j(t)\right]
  \pause= \left(\sum_{k=1}^{M}\mu_k^*\right) T - \E_{\mu}\left[\sum_{t=1}^T\sum_{j=1}^M r^j(t)\right]$$
\end{small}\vspace*{-10pt}

. . .

## Two directions of analysis
- Clearly $R_T = \mathcal{O}(T)$, but we want a sub-linear regret, as small as possible!
- *How good a decentralized algorithm can be in this setting?*
  \hook{} **Lower Bound** on regret, for **any** algorithm !
- *How good is my decentralized algorithm in this setting?*
  \hook{} **Upper Bound** on regret, for **one** algorithm !

----

\section{\hfill{}3. Lower bound\hfill{}}

# Lower bound

1. Decomposition of regret in $3$ terms,\vspace*{15pt}
2. Asymptotic lower bound of one term,\vspace*{15pt}
3. And for regret,\vspace*{15pt}
4. Sketch of proof,\vspace*{15pt}
5. Illustration

----

\subsection{\hfill{}3.a. Lower bound on regret\hfill{}}

# Decomposition on regret

## Decomposition
For any algorithm, decentralized or not, we have
\vspace*{-20pt}
\begin{small}\begin{align*}
R_T(\boldsymbol{\mu}, M, \rho) &= \alert<2>{\sum_{k \in \Mworst} (\mu_M^* -  \mu_k) \E_{\mu}[T_k(T)]} \\
&+ \alert<3>{\sum_{k \in \Mbest} (\mu_k -  \mu_M^*) \left(T - \E_{\mu}[T_k(T)]\right)} + \alert<4>{\sum_{k=1}^{K} \mu_k \E_{\mu}[\mathcal{C}_k(T)]}.
\end{align*}\end{small}
\vspace*{-10pt}

## Small regret can be attained if...
\pause

1. Devices can quickly identify the bad arms $\Mworst$, and not play them too much
   (\alert<2>{\emph{number of sub-optimal selections}}),\pause
2. Devices can quickly identify the best arms, and most surely play them
   (\alert<3>{\emph{number of optimal non-selections}}),\pause
3. Devices can use orthogonal channels
   (\alert<4>{\emph{number of collisions}}).

# Asymptotic Lower Bound on regret I

## Lower bounds
- The first term for sub-optimal arms selections
  is lower bounded asymptotically,
  $$\forall j,k,\; \mathop{\lim\inf}\limits_{T \to +\infty} \frac{\E_{\mu}[T_k^j(T)]}{\log T} \geq \frac{1}{\kl(\mu_k, \mu_M^*)},$$
  using technical information theory tools
  (Kullback-Leibler divergence, entropy),
- And we lower bound the rest (including collisions) by... $0$\newline
  $\left(T - \E_{\mu}[T_k(T)]\right) \geq 0$, $\E_{\mu}[\mathcal{C}_k(T)] \geq 0$
  : we should be able to do better!

# Asymptotic Lower Bound on regret II

## Theorem 1  \hfill{}\textcolor{gray}{[Besson \& Kaufmann, 2017]}
- For any uniformly efficient decentralized policy, and any non-degenerated problem  $\boldsymbol{\mu}$,
\vspace*{-10pt}
$$ \mathop{\lim\inf}\limits_{T \to +\infty} \frac{R_T(\boldsymbol{\mu}, M, \rho)}{\log(T)} \geq M \times \left( \sum_{k \in \Mworst} \frac{(\mu_M^* -  \mu_k)}{\kl(\mu_k, \mu_M^*)} \right) . $$
\footnotetext{\tiny Where $\kl(x,y) := x \log(\frac{x}{y}) + (1 - x) \log(\frac{1-x}{1-y})$ is the \emph{binary} Kullback-Leibler divergence.}

\pause

## Remarks
- Centralized \emph{multiple-play} lower bound is the same without the $M$ multiplicative factor...
  \hook "price of non-coordination" $= M =$ nb of player?
- Improved state-of-the-art lower bound, but still not perfect: collisions should also be controlled!

----

\subsection{\hfill{}3.b. Illustration of the Lower Bound\hfill{}}

# Illustration of the Lower Bound on regret {.plain}

\begin{figure}[h!]
\includegraphics[height=0.80\textheight]{figures/main_RegretCentralized____env3-4_2092905764868974160.pdf}
\caption{\footnotesize{Any such lower bound is very asymptotic, usually not satisfied for small horizons. We can see the importance of the collisions!}}
\end{figure}

----

\subsection{\hfill{}3.c. Sketch of the proof\hfill{}}

# Sketch of the proof

- Like for single-player bandit, focus on $\E_{\mu}[T_k^j(T)]$ expected number of selections of any sub-optimal arm $k$.
- Same information-theoretic tools, using a "change of law" lemma.
- Improving the state-of-the-art because of our decomposition, not because of a new tool.

> \strut\hfill$\hookrightarrow$ See our paper for details!

----

\section{\hfill{}4. Single-player MAB algorithms : \UCB, \klUCB\hfill{}}

# Single-player MAB algorithms

1. Upper Confidence Bound algorithm : \UCB,\vspace*{15pt}
2. Kullback-Leibler UCB algorithm : \klUCB

----

\subsection{\hfill{}4.a. Upper Confidence Bound algorithm : \UCB\hfill{}}

# Upper Confidence Bound algorithm ($\mathrm{UCB}_1$)
Dynamic device keep $t$ number of sent packets, $T_k(t)$ selections of channel $k$, $X_k(t)$ successful transmission in channel $k$.

1. For the first $K$ steps ($t=1,\dots,K$), try each channel *once*.
2. Then for the next steps $t > K$ :
    - Compute the index $g_k(t) := \underbrace{\frac{X_k(t)}{T_k(t)}}_{\text{Mean}\; \widehat{\mu_k}(t)} + \underbrace{\sqrt{\frac{\log(t)}{2 \; T_k(t)}},}_{\text{Upper Confidence Bound}}$
    - Choose channel $A(t) = \mathop{\arg\max}\limits_{k} \; g_k(t)$,
    - Update $T_k(t+1)$ and $X_k(t+1)$.

\citationref{References: [Lai \& Robbins, 1985], [Auer et al, 2002], [Bubeck \& Cesa-Bianchi, 2012]}

----

\subsection{\hfill{}4.b. Kullback-Leibler UCB algorithm : \klUCB\hfill{}}

# Kullback-Leibler UCB algorithm ($\mathrm{kl}$-$\mathrm{UCB}$)
Dynamic device keep $t$ number of sent packets, $T_k(t)$ selections of channel $k$, $X_k(t)$ successful transmission in channel $k$.

1. For the first $K$ steps ($t=1,\dots,K$), try each channel *once*.
2. Then for the next steps $t > K$ :
    - Compute the index $g_k(t) := \sup\limits_{q \in [a, b]} \left\{ q : \mathrm{kl}(\frac{X_k(t)}{N_k(t)}, q) \leq \frac{\log(t)}{N_k(t)} \right\}$
    - Choose channel $A(t) = \mathop{\arg\max}\limits_{k} \; g_k(t)$,
    - Update $T_k(t+1)$ and $X_k(t+1)$.

\pause\alert<2>{\emph{Why bother?}} \klUCB{} is proved to be more efficient than \UCB{},
and asymptotically optimal for single-player stochastic bandit.

\citationref{References: [Garivier \& Cappé, 2011], [Cappé \& Garivier \& Maillard \& Munos \& Stoltz, 2013]}

----

\section{\hfill{}5. Multi-player decentralized algorithms\hfill{}}

# Multi-player decentralized algorithms

1. Common building blocks of previous algorithms,\vspace*{15pt}
2. First proposal: \RandTopM,\vspace*{15pt}
3. Second proposal: \MCTopM,\vspace*{15pt}
4. Algorithm and illustration.

----

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
    + *With sensing*: \RandTopM{} and \MCTopM{} are sort of mixes between RhoRand and \MusicalChair{}, using UCB indexes or more efficient index policy (\klUCB),
    + *Without sensing*: \Selfish{} use a UCB index directly on the reward $r^j(t)$.

----

----

\subsection{\hfill{}5.b. \MCTopM{} algorithm\hfill{}}
# The \MCTopM{} algorithm

FIXME include code, explain
FIXME include figure, explain

----

# The \MCTopM{} algorithm {.plain}

% \vspace*{-5pt}  % XXX remove if problem
\begin{small}  % XXX remove if problem
  \begin{figure}[h!]
      % \begin{framed}  % XXX remove if problem
      \begin{small}  % XXX remove if problem
      \centering
      % Documentation at http://mirror.ctan.org/tex-archive/macros/latex/contrib/algorithm2e/doc/algorithm2e.pdf if needed
      % Or https://en.wikibooks.org/wiki/LaTeX/Algorithms#Typesetting_using_the_algorithm2e_package
      % \removelatexerror% Nullify \@latex@error % Cf. http://tex.stackexchange.com/a/82272/
      \begin{algorithm}[H]
          % XXX Options
          % \LinesNumbered  % XXX Option to number the line
          % \RestyleAlgo{boxed}
          % XXX Input, data and output
          % \KwIn{$K$ and policy $P^j$ for arms set $\{1,\dots,K\}$\;}
          % \KwData{Data}
          % \KwResult{Result}
          % XXX Algorithm
              Let $A^j(1) \sim \mathcal{U}(\{1,\dots,K\})$ and $C^j(1)=\mathrm{False}$ and $s^j(1)=\mathrm{False}$ \\
              \For{$t = 0, \dots, T-1$}{
                   \uIf(\tcp*[f]{transition $(3)$ or $(5)$}){
                      $A^j(t) \notin \TopM(t)$}
                    {
                      $A^j(t+1) \sim \mathcal{U} \left(\TopM(t) \cap \left\{k : g_k^j(t-1) \leq g^j_{A^j(t)}(t-1)\right\}\right)$
                      \tcp*[f]{not empty} \\
                      % \tcp*[f]{randomly switch on an arm that had smaller UCB at $t-1$}
                      $s^j(t+1) = \mathrm{False}$
                      \tcp*[f]{aim at an arm with a smaller UCB at $t-1$}
                    }
                    \uElseIf(\tcp*[f]{collision and not fixed}){
                        $C^j(t)$ \emph{and} $\overline{s^j(t)}$}
                      {
                        $A^j(t+1) \sim \mathcal{U} \left(\TopM(t)\right)$
                        \tcp*[f]{transition $(2)$} \\
                        $s^j(t+1) = \mathrm{False}$
                    }
                    \Else(\tcp*[f]{transition $(1)$ or $(4)$}){
                      $A^j(t+1) = A^j(t)$ \tcp*[f]{stay on the previous arm} \\
                      $s^j(t+1) = \mathrm{True}$ \tcp*[f]{become or stay fixed on a ``chair''}
                    }
                  Play arm $A^j(t+1)$, get new observations (sensing and collision), \\
                  Compute the indices $g^j_k(t+1)$ and set $\TopM(t+1)$ for next step.
              }
              \caption{The \MCTopM{} decentralized learning policy (for a fixed underlying index policy $g^j$).}
          \label{algo:MCTopM}
      \end{algorithm}
      \end{small}  % XXX remove if problem
      % \end{framed}  % XXX remove if problem
  \end{figure}
\end{small}  % XXX remove if problem
\vspace*{-5pt}  % XXX remove if problem

----

# The \MCTopM{} algorithm {.plain}

\begin{figure}[h!]
  \begin{tikzpicture}[>=latex',line join=bevel,scale=2.5]
      %
      \node (start) at (1.5,0.30) {$(0)$ Start $t=0$};
      \node (notfixed) at (1,0) [draw,rectangle,thick] {Not fixed, $\overline{s^j(t)}$};
      \node (fixed) at (0,0) [draw,rectangle,thick] {Fixed, $s^j(t)$};
      %
      \draw [black,->] (start) -> (notfixed.20);
      \draw [color=cyan,thick,->] (notfixed) to[bend right] node[midway,above,text width=5cm,text centered,black] {\small $(1)$ $\overline{C^j(t)}, A^j(t) \in \TopM(t)$} (fixed);
      \path [color=blue,thick,->] (notfixed) edge[loop right] node[right,text width=4cm,text badly centered,black] {\small $(2)$  $C^j(t), A^j(t) \in \TopM(t)$} (1);
      \path [color=red,thick,->] (notfixed) edge[loop below] node[below,text centered,black] {\small $(3)$  $A^j(t) \notin \TopM(t)$} (1);
      \path [color=darkgreen,thick,->] (fixed) edge[loop left] node[left,text width=2.9cm,text badly centered,black] {\small $(4)$ $A^j(t) \in \TopM(t)$} (fixed);
      \draw [color=red,thick,->] (fixed) to[bend right] node[midway,below,text centered,black] {\small $(5)$  $A^j(t) \notin \TopM(t)$} (notfixed);
      %
  \end{tikzpicture}
  \caption{\small Player $j$ using $\mathrm{MCTopM}$, represented as ``state machine'' with $5$ transitions.
  Taking one of the five transitions means playing one round of the Algorithm~\ref{algo:MCTopM}, to decide $A^j(t+1)$ using information of previous steps.}
  \label{fig:StateMachineAlgorithm_MCTopM}
\end{figure}

----

\section{\hfill{}6. Regret upper bound\hfill{}}

# Regret upper bound

1. Theorem,\vspace*{15pt}
2. Idea of the proof.

----

\subsection{\hfill{}6.a. \MCTopM-\klUCB\hfill{}}

# Regret upper bound for \MCTopM-\klUCB

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
- For the suboptimal selections, we *match our lower bound* !
- We also *minimize the number of channel switching*: interesting as it costs energy,
- Not yet possible to know what is the best possible control of collisions...

----

\subsection{\hfill{}6.b. Sketch of the proof\hfill{}}

# Sketch of the proof

1. Bound the expected number of collisions by $M$ times the nb of collisions for non-sitted players,
2. Bound the expected number of \textcolor{red}{transitions of type $(3)$ and $(5)$}, by $\bigO{\log T}$ using the \klUCB{} indexes and the forced choice of the algorithm XXX,
3. Bound the expected length of a sequence in the non-sitted state by a constant,
4. So most of the times ($\bigO{T - \log T}), players are sitted, and no collision happens when they are all sitted!

> See our paper for details!

----

\section{\hfill{}7. Experimental results\hfill{}}

# Experimental results

Experiments on Bernoulli problems $\boldsymbol{\mu}\in[0,1]^K$.

1. Illustration of regret for a single problem and $M = K$,\vspace*{15pt}
2. Illustration of regret for uniformly sampled problems and $M < K$,\vspace*{15pt}
3. Collisions,\vspace*{15pt}
4. Arm switches,\vspace*{15pt}
5. Fairness.

----

\subsection{\hfill{}7.a. Illustration of regret\hfill{}}

# Constant regret if $M=K$ {.plain}

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

\section{\hfill{}8. An heuristic, \Selfish\hfill{}}

# An heuristic, \Selfish

For the harder feedback model without sensing.

1. Explaining the heuristic,\vspace*{15pt}
2. Problems with \Selfish,\vspace*{15pt}
5. Illustration of failure cases.

----

\subsection{\hfill{}8.a. Problems with \Selfish\hfill{}}

# The \Selfish{} heuristic {.allowframebreaks}
The \Selfish{} decentralized approach = device don't use sensing, just learn on the receive acknowledgement.

## Works fine...
- More suited to model IoT networks,
- Use less information, and don't know the value of $M$: we expect \Selfish{} to not have stronger guarantees.
- It works fine in practice!

## *But why would it work?*
- Sensing was \iid{} so using \UCB{} to learn the $\mu_k$ makes sense,
- But collisions are not \iid,
- Adversarial algorithms are more appropriate here,
- But empirically, \Selfish{} with \UCB{} or \klUCB{} works much better than, \eg, \ExpThree...

## Works fine...
- Except... when it fails drastically!
- In small problems with $M$ and $K = 2$ or $3$, we found small probability of failures (\ie, linear regret), and this prevents from having a generic upper bound on regret for \Selfish. Sadly...

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
- But here the collisions cancel the \iid{} hypothesis...
- Not easy to obtain guarantees in this mixed setting \newline
  (\iid{} emissions process, "game theoretic" collisions).

## Theoretical results
- With sensing ("OSA"), we obtained strong results: a lower bound, and an order-optimal algorithm,
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
  first with sensing (\eg, models ZigBee networks),
  then without sensing (\eg, LoRaWAN networks).

----

\subsection{\hfill{}9.c. Thanks!\hfill{}}

# Conclusion {.allowframebreaks}

- In a wireless network with an \iid{} background traffic in $K$ channels,
- $M$ devices can use both sensing and acknowledgement feedback, to learn the most free channels and to find orthogonal configurations.

## We showed
- Decentralized bandit algorithms can solve this problem,
- We have a lower bound for any decentralized algorithm,
- And we proposed an order-optimal algorithm, based on \klUCB{} and an improved Musical Chair scheme, \MCTopM

## But more work is still needed...
- **Theoretical guarantees** are still missing for the "IoT" model (without sensing), and can be improved (slightly) for the "OSA" model (with sensing).
- Maybe study **other emission models**...
- Implement and test this on **real-world radio devices**
  \hook demo (in progress) for the ICT $2018$ conference!

## **Thanks!**
\begin{center}\begin{Large}
\emph{Any question or idea ?}
\end{Large}\end{center}
