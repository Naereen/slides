---
author: Lilian Besson
title: MAB Learning in IoT Networks
subtitle: Learning helps even in non-stationary settings!
institute:
  Team SCEE, IETR, CentraleSupélec, Rennes \newline
  \& Team SequeL, CRIStAL, Inria, Lille \newline
  \newline
  $15$ minutes
smallinstitute: CROWNCOM 2017
date: 20 sept 2017
lang: english
babel-lang: english
handout: false
numbersections: true
section-titles: false
fontsize: 12pt
toc: true
include-before:
  \section*{\hfill{}CentraleSupélec Rennes \& Inria Lille\hfill{}}
  \subsection*{\hfill{}Team {:} SCEE @ IETR \& SequeL @ CRIStAL\hfill{}}
---

\section{Introduction}

\subsection{Objective}
# We want
- Insert *lots* of IoT objects in a **crowded wireless network**
- With a protocol **slotted in time and frequency**
- Each object has a **low duty cycle**
  (a few message per day)

. . .

## Goal
- Maintain a **good Quality of Service**
- **Without centralized supervision!**

. . .

## How?
- Use **learning algorithms**:
  objects will learn on which frequency they should talk!

---

\subsection{Outline}
# Outline
1. Introduction and motivation
2. Model and hypotheses
3. Baseline algorithms
4. Two learning algorithms : UCB, TS
5. Experimental results
6. Perspectives and future work
7. Conclusion

---

\section{Model and hypotheses}

\subsection{Model}
# Model
- Blabla
- Blabla
- Blabla

![Protocol](src/protocol.eps)

---

\subsection{Hypotheses}
# Hypotheses
- Blabla
- Blabla
- Blabla

---

\section{Baseline algorithms}

\subsection{Uniformly random access: naive strategy}
# Naive strategy
- Uniformly random access
- Natural strategy, dead simple to implement
- Works fine only if all channels are similarly occupied (background traffic)

---

\subsection{Optimal centralized strategy}
# Optimal centralized strategy
- Very efficient
- But not achievable in practice

---

\subsection{Greedy approximation of the centralized strategy}
# Greedy approximation
- Still very efficient
- More reasonable
- But still unachievable: this is a *baseline*

---

\section{Two learning algorithms : UCB, TS}

\subsection{Upper Confidence Bound algorithm : UCB}
# Upper Confidence Bound algorithm
- Smart

---

\subsection{Thompson Sampling : Bayesian index policy}
# Thompson Sampling
- Smart

---

\section{Experimental results}

\subsection{Experiment setting}
# Experimental setting
- What do we want to show
- Wnat we implemented
- Simulation parameters

---

\subsection{First result: $10\%$}
# First result: $10\%$ of dynamic devices

![$10\%$ of dynamic devices](src/10intelligent.eps)

---

\subsection{First result: $20\%$}
# $30\%$ of dynamic devices

![$30\%$ of dynamic devices](src/30intelligent.eps)

---

\subsection{First result: $50\%$}
# $50\%$ of dynamic devices

![$50\%$ of dynamic devices](src/50intelligent.eps)

---

\subsection{First result: $100\%$}
# $100\%$ of dynamic devices

![$100\%$ of dynamic devices](src/100intelligent.eps)

---

\subsection{More and more dynamic devices}
# More and more dynamic devices

![More and more dynamic devices](src/perf_learning.eps)

---

\section{Perspectives and future work}

\subsection{Perspectives}
# Perspectives
## Theoretical results
- This
- and this
- and this

## Real-world experimental validation
- In progress

---

\subsection{Future work}
# Future work
- We need to do this
- and that
- and it will be awesome

---

\section{Conclusion}
\subsection{Thanks!}
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