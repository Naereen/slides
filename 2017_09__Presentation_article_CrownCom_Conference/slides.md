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
toc: false
include-before:
  \section*{\hfill{}CentraleSupélec Rennes \& Inria Lille\hfill{}}
  \subsection*{\hfill{}Team {:} SCEE @ IETR \& SequeL @ CRIStAL\hfill{}}
---

\section{\hfill{}1. Introduction and motivation\hfill{}}

\subsection{\hfill{}Objective\hfill{}}
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

\subsection{\hfill{}Outline\hfill{}}
# Outline
1. Introduction and motivation
2. Model and hypotheses
3. Baseline algorithms
4. Two learning algorithms : UCB, TS
5. Experimental results
6. Perspectives and future work
7. Conclusion

---

\section{\hfill{}2. Model and hypotheses\hfill{}}

\subsection{\hfill{}Model\hfill{}}
# Model
- Blabla
- Blabla
- Blabla

![Protocol](src/protocol.eps)

---

\subsection{\hfill{}Hypotheses\hfill{}}
# Hypotheses
- Blabla
- Blabla
- Blabla

---

\section{\hfill{}3. Baseline algorithms\hfill{}}

\subsection{\hfill{}Uniformly random access: naive strategy\hfill{}}
# Naive strategy
- Uniformly random access
- Natural strategy, dead simple to implement
- Works fine only if all channels are similarly occupied (background traffic)

---

\subsection{\hfill{}Optimal centralized strategy\hfill{}}
# Optimal centralized strategy
- Very efficient
- But not achievable in practice

---

\subsection{\hfill{}Greedy approximation of the centralized strategy\hfill{}}
# Greedy approximation
- Still very efficient
- More reasonable
- But still unachievable: this is a *baseline*

---

\section{\hfill{}4. Two learning algorithms : UCB, TS\hfill{}}

\subsection{\hfill{}Upper Confidence Bound algorithm : UCB\hfill{}}
# Upper Confidence Bound algorithm
- Smart

---

\subsection{\hfill{}Thompson Sampling : Bayesian index policy\hfill{}}
# Thompson Sampling
- Smart

---

\section{\hfill{}5. Experimental results\hfill{}}

\subsection{\hfill{}Experiment setting\hfill{}}
# Experimental setting
- What do we want to show
- Wnat we implemented
- Simulation parameters

---

\subsection{\hfill{}First result: $10\%$\hfill{}}
# First result: $10\%$ of dynamic devices

![$10\%$ of dynamic devices](src/10intelligent.eps)

---

\subsection{\hfill{}First result: $20\%$\hfill{}}
# $30\%$ of dynamic devices

![$30\%$ of dynamic devices](src/30intelligent.eps)

---

\subsection{\hfill{}First result: $50\%$\hfill{}}
# $50\%$ of dynamic devices

![$50\%$ of dynamic devices](src/50intelligent.eps)

---

\subsection{\hfill{}First result: $100\%$\hfill{}}
# $100\%$ of dynamic devices

![$100\%$ of dynamic devices](src/100intelligent.eps)

---

\subsection{\hfill{}More and more dynamic devices\hfill{}}
# More and more dynamic devices

![More and more dynamic devices](src/perf_learning.eps)

---

\section{\hfill{}6. Perspectives and future work\hfill{}}

\subsection{\hfill{}Perspectives\hfill{}}
# Perspectives
## Theoretical results
- This
- and this
- and this

## Real-world experimental validation
- In progress

---

\subsection{\hfill{}Future work\hfill{}}
# Future work
- We need to do this
- and that
- and it will be awesome

---

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