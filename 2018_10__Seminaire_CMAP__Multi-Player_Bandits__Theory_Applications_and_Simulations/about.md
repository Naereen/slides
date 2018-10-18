# Title

State of the art of Multi-Player Bandits: Theory, Applications and Simulations

# Abstract (anglais)

In this talk, I present the model of Multi-player Multi-Armed Bandits (MAB), with different feedback models and discuss possible applications to Cognitive Radio systems.
I present how we improved the state-of-the-art lower bound for the regret of any decentralized algorithms, and introduce two algorithms, RandTopM and MCTopM, that are shown to empirically outperform existing algorithms. Moreover, I provide strong theoretical guarantees for these algorithms, including a notion of asymptotic optimality in terms of the number of selections of bad arms.

I also present some results from very recent works (arxiv.org/abs/1809.08151 and arxiv.org/abs/1808.08416 and arxiv.org/abs/1808.04875), and then I show simulations to investigate the empirical performance of our proposals.

I will discuss for about a third of the talk about how the simulations are executed, to present and advertise my project SMPyBandits.
SMPyBandits is a package for numerical simulations on single-player and multi-players Multi-Armed Bandits (MAB) algorithms, written in Python (2 or 3). This library is the most complete open-source implementation of state-of-the-art algorithms tackling various kinds of sequential learning problems referred to as Multi-Armed Bandits. It is extensive, simple to use and maintain, with a clean and well documented codebase. It allows fast prototyping of experiments, with an easy configuration system and command-line options to customize experiments.

---

# Titre

État de l'art des Bandits Multi-Joueurs: théorie, applications, simulations

# Résumé (français)

Dans cet exposé, je présente le modèle des Bandits Multi-Joueurs Multi-Bras (MAB), avec différents niveaux d'informations, et je discuterai des applications possibles aux systèmes de Radio Cognitive.
Je présente comment nous avons amélioré la borne inférieure pour le regret de tout algorithme décentralisé, et je présente deux algorithmes, RandTopM et MCTopM, qui se sont avérés plus performants que les algorithmes existants de façon empirique. De plus, j'apporte de solides garanties théoriques pour ces algorithmes, y compris une notion d'optimalité asymptotique en termes de nombre de sélections de mauvais bras.

Je présente également quelques résultats de travaux très récents (arxiv.org/abs/1809.08151 et arxiv.org/abs/1808.08416 et arxiv.org/abs/1808.04875), puis je montre des simulations pour étudier la performance empirique de nos propositions.

Je discuterai pendant environ un tiers de l'exposé sur la façon dont les simulations sont exécutées, pour présenter et annoncer mon projet SMPyBandits.
SMPyBandits est un logiciel de simulation numérique sur les algorithmes MAB, écrit en Python. Cette bibliothèque est l'implémentation open-source la plus complète d'algorithmes de bandits. Elle est complète, simple à utiliser et à entretenir, avec une base de code propre et bien documentée, et permet le prototypage rapide d'expériences, avec un système de configuration facile et des options en ligne de commande pour personnaliser les expériences.

---

# References / références
- Lilian Besson, Emilie Kaufmann. Multi-Player Bandits Revisited. Algorithmic Learning Theory, Apr 2018, Lanzarote, Spain. 2018, http://www.cs.cornell.edu/conferences/alt2018/. https://hal.inria.fr/hal-01629733
- Lilian Besson. SMPyBandits: an Experimental Framework for Single and Multi-Players Multi-Arms Bandits Algorithms in Python. 2018. https://hal.inria.fr/hal-01840022
- Lilian Besson. Multi-players simulation environment, in SMPyBandits documentation, https://smpybandits.github.io/MultiPlayers.html

# Presenter / exposant
Lilian Besson, cf. https://perso.crans.org/besson/ and https://github.com/Naereen/