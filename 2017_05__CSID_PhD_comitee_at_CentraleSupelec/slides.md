---
author: Lilian Besson
title: CSID - 1ère année de thèse
subtitle: Comité de Suivi Individuel du Doctorant
institute:
  Équipe SCEE, IETR, CentraleSupélec, Rennes \newline
  \& Équipe SequeL, CRIStAL, Inria, Lille \newline
  \newline
  $30$ minutes
smallinstitute: MATISSE
date: 2 mai 2017
lang: french
babel-lang: french
handout: false
numbersections: true
section-titles: false
fontsize: 12pt
include-before:
  \section*{\hfill{}CentraleSupélec Rennes \& Inria Lille\hfill{}}
  \subsection*{\hfill{}Équipes {:} SCEE @ IETR \& SequeL @ CRIStAL\hfill{}}
---

# Comité de Suivi Individuel du Doctorant
- Doctorant : Lilian Besson
- Titre de la thèse : \newline
  *"Apprentissage statistique séquentiel pour la radio cognitive multi-joueurs"*
- Dates : 1er octobre $2016$ à septembre $2019$
- Encadrement :

    \begin{tabular}{lll}
    Directeur de thèse : & \textbf{Christophe Moy} & à Rennes \\
    Co-encadrante : & \textbf{Émilie Kaufmann} & à Lille \\
    \end{tabular}

. . .

- Comité de suivi : **Patrick Maillé** \& **Rémi Gribonval** \newline
  (merci !)

----

# Présentation personnelle

## Rapidement, je suis...
- Français, $23$ ans, je viens des Hautes-Alpes (Briançon),
- Normalien de l'ENS Cachan ($2011-2016$), diplômé en *mathématiques* et *informatique* (agrégation en $2014$, master MVA en $2016$).

. . .

## Avant et maintenant...
- *Avant* : stages de recherche en $2012$, $2013$, et $2016$, un an d'enseignement en $2014-15$,
- *En thèse* depuis octobre, basé à Rennes, avec un financement ministériel ("contrat doctoral spécifique normalien"),
- Passionné par l'enseignement, je souhaite *enseigner* en France en classes préparatoires après ma thèse plutôt que de rester en recherche.

----

# Contexte et sujet {.allowframebreaks}

## Historique de l'équipe SCEE sur ce sujet
- Thèse de Wassim Jouini (2008-2012), *"Contribution to learning and decision making under uncertainty for Cognitive Radio"*,
- Thèse de Navikkumar Modi (2014-2017, soutenance dans $2$ semaines), *"Machine Learning and Statistical Decision Making for Green Radio"*.

## Contexte thématique
- Télécommunications radio et *radio intelligente*,
- Apprentissage statistique séquentiel et par renforcement, problèmes et algorithmes de *bandit*
- Réseaux plus efficaces, plus écologiques etc,
- Réseaux avec beaucoup d'objets connectés (*"Internet of Things"*, IoT).

## Mon sujet
- *"Apprentissage statistique séquentiel pour la radio cognitive multi-joueurs"*
- But : suite des thèses de Wassim et Navikkumar
- Avec une plus grande dimension théorique sur les algorithmes étudiés et les difficultés intrinsèques des problèmes,
- Étendre ces travaux au cas multi-objets et grand nombre d'objets (IoT).

----

# Un premier problème : *Accès Opportuniste au Spectre* (*OSA*) {.allowframebreaks}

> - Il y a $K \geq 1$ canaux radio (bandes de fréquence) dans un domaine licencié, avec un temps discret synchronisé (temps et fréquence *discrets*),
> - Des utilisateurs, dits *primaires* (PU), paient pour utiliser (plus ou moins) les canaux,
> - Un autre utilisateur, dit *secondaire* (SU) veut communiquer, en accédant au canal le moins occupé,
> - Mais il ne doit pas déranger les PU, et il peut écouter sur *un seul* canal au début de chaque temps discret, et ne fait rien si le canal est occupé,
> - Ce trafic ambiant est modélisé par des distributions de Bernoulli $B(\mu_1),\dots,B(\mu_K)$ ($\mu_k$ moyenne d'occupation du canal $k$),
> - $\implies$ L'utilisateur doit trouver le canal le moins occupé, i.e. apprendre les paramètres $\mu_k$ sous-jacents
> - C'est un problème de décision discrète, en ligne, i.e. un *problème de bandit*

----

# Un premier algorithme pour l'OSA {.allowframebreaks}

UCB1

----

# Mes objectifs et mes apports

----

# Double encadrement

Avec Émilie Kaufmann à Inria Lille (équipe SequeL, laboratoire CRIStAL) :

- $4$ *visites* de Émilie à Rennes en $2016$, $2$ en mai $2017$,

- $4$ *visites* de Lilian à Lille depuis octobre (de $3$ à $15$ jours), de $3$ semaines en juin,

- *Projets* en commun : Christophe et Émilie publient un *tutorial* à la conférence ICC'17 (Paris, fin mai), et Émilie siège dans le jury de thèse de Navikkumar Modi (mai),

- *Financements* : déplacements pris en charge en $2016$ avec les projets ANR "SoGreen" (Rennes) et "BADASS" (Lille), et depuis mars avec un financement PEPS "BIO" obtenu par Émilie et moi ($15000$€ pour $2017$).

----

# Recherches en cours et collaboration

- Avec Rémi Bonnefoi, autre doctorant dans l'équipe SCEE : papier à CrownCom blabla
- Avec Émilie Kaufmann, XXX
- Avec Christophe Moy et Émilie Kaufmann, XXX

----

# Objectifs de publication pour $2017$ et $2018$ {.allowframebreaks}

- Un *rapport de recherche* (arXiv/HAL) résumant le travail de bibliographie, d'implémentation et d'expérimentation réalisé pour mon environnement de simulation (presque terminé) et la publication en libre accès du code (pour l'instant, la documentation est déjà disponible).\newline
  Cf. \urlb{banditslilian.gforge.inria.fr/}

- Un *article* envoyé à la conférence européenne **CrownCom** $2017$ (septembre, Lisbonne, Portugal) avec Rémi Bonnefoi, suivi d'une version journal étendue (déjà terminée !),

- Un *article* "maths et théorie" avec Émilie Kaufmann, sur des résultats déjà obtenus et d'autres à terminer, FIXME sur quoi ? *Objectif* : **ICML** ou **COLT** $2018$,

- Un *article* "ingénieur" exposant l'intérêt de l'agrégation d'algorithmes de bandit pour des problèmes de radio cognitive. *Objectif* : **URSI** ou **GRESTI** $2018$,

- J'aimerai aussi faire un *survey* sur "tous" les algorithmes de bandits, en les écrivant tous avec la même structure (initialisation, choix, récompense, etc), basé sur mon code. Il y en a une douzaine pour l'aspect mono-joueur (et des dizaines de variantes) et une dizaine pour l'aspect multi-joueurs.

----

# Autres pistes de recherche ?

## Agrégation d'algorithmes de bandit

- Idée : exécuter plusieurs algorithmes similaires en parallèle, sur le même problème, et les faire voter à chaque décision dans l'espoir d'être plus efficace (et plus robuste) que si on écoute un seul algorithme,
- But : être plus efficace face à des problèmes différents, pour être plus robuste en situation réelle (e.g., où on ne sait pas un modèle de Bernoulli ou Gaussien est approprié)

- Déjà étudié par quelques chercheurs, des algorithmes existent (Exp4 en $2002$, Exp3M et ComBand à NIPS $2015$ et $2016$, variantes de *"Online Gradient Mirror Descent"*),
- J'ai redécouvert l'algorithme Exp4 (et une autre variante) en décembre, et je ne pense pas continuer dans cette direction

----

# Autres activités ($1/4$) : Formations

Pour la thèse, il faut suivre des formations :

- Scientifiques :
    + Cours de "Radio Logicielle" par Jacques Palicot, à CentraleSupélec en mai-juin $2017$ ($12$h),
    + (normalement) Présentation à la conférence CrownCom en septembre $2017$.

- Générales ou professionnelles :
    + À l'Université de Rennes 1, $9$h en février $2017$,
    + À l'Université de Lille 1, $2$h en mars $2017$.

> Encore beaucoup à suivre, l'an prochain.

----

# Autres activités ($2/4$) : Enseignements

Par passion et pour valider mon stage d'agrégation, j'enseigne :

- $24$h/an de TD/TP à l'*ENSAI*, en informatique théorique, pour le cours "Algorithmique et Calculabilité" de David Cachera\footnote{Cf. \urlb{perso.crans.org/besson/ensai-2016/}}, au niveau L3 (1ère année d'école d'ingénieur).

- $40$h/an de TD/oraux à l'*ENS de Rennes*, en informatique théorique, pour la classe de préparation à l'agrégation de maths\footnote{Cf. \urlb{perso.crans.org/besson/agreg-2016/}} (option info), au niveau M2 (3ème année d'ENS). $15$ séances d'entraînement aux oraux d'informatique (leçons et modélisation) et oraux blancs.

> J'ai obtenu la même mission pour l'année prochaine !
>
> *Note :* je souhaite enseigner en classes préparations après ma thèse.

----

# Autres activités ($3/4$) : Projets étudiant {.allowframebreaks}

J'aide quelques élèves à CentraleSupélec, surtout sur :

- la compréhension et l'implémentation des algorithmes (Python),
- l'utilisation de machines GNU/Linux et le logiciel GNU Radio Companion,
- et l'aspect "bidouillage" en général.

## Projet long depuis octobre

- Clément \& Théo : projet long sur un générateur de "trafic ambiant" aléatoire, de type IoT, avec des cartes USRP et GNU Radio (programmation en Python et `C++`). Émission et réception réaliste en temps réel, avec une modulation *QPSK*,

## Projets courts en février

- Bruno \& Jérôme \& Qingsong : projet court ($5$ semaines) sur le standard IoT *HomeEasy* (pour des "ampoules connectées"), programmation en Python et GNU Radio pour l'émission et la réception,
- Pierre, Matthieu : projet court ($5$ semaines), une webcam sur un Raspberry Pi permet de suivre le niveau de café d'une cafetière, et de réagir lorsqu'elle est vide, pleine etc (programmation Python, traitement d'image embarqué et efficace, communication web).

> Rien d'officiel ni de trop coûteux en temps pour l'instant.

## Nouveaux projets courts ($5$ semaines) en mai/juin

- Antoine \& Pierre-Jean : implémentation d'algorithmes de bandit (UCB1, Thompson Sampling etc) en Python dans GNU Radio, pour ajouter un utilisateur secondaire s'insérant dynamiquement dans le trafic généré par un projet précédent,
- Flora \& Matthias \& Quentin : implémentation des mêmes algorithmes en `C++` sur des cartes LoRa programmables, pour s'insérer dans un réseau implémentant le standard *LoRa* (modulation/démodulation et trafic ambiant déjà réalisés par un autre projet).

> J'espère en faire autant l'an prochain, selon ce qu'on propose.

----

# Autres activités variées ($4/4$)

> - Administration système pour nos machines de calcul dans l'équipe SCEE (3 *workstations*, 15 utilisateurs).
>
> - Membre du bureau de l'*Association des Doctorants et Docteurs de l'IETR*\only<2,3>{\footnote{Cf. \urlb{addi.asso.insa-rennes.fr/}}} (**ADDI**) depuis février. Une douzaine d'activités prévues dans l'année (dont la Journée des Doctorants en juillet, la galette des rois de l'IETR en janvier etc).\newline
>
> - Programmeur passionné, je contribue régulièrement à des projets personnels\only<3>{\footnote{Cf. \urlb{Bitbucket.org/lbesson} et \urlb{GitHub.com/Naereen}}} et des grands projets *open-source*, surtout en Bash, OCaml et Python (e.g., bibliothèques `joblib`, `matplotlib`, `jupyter`, `ipython` etc).\newline

----

# Conclusion \& Perspectives {.allowframebreaks}

## Une première année de thèse déjà bien avancée, avec :

- de la *recherche*, à CentraleSupélec Rennes et Inria Lille, avec mes encadrants (Christophe Moy, Émilie Kaufmann) et un autre doctorant (Rémi Bonnefoi),
- un premier article terminé, d'autres objectifs bientôt,
- des déplacements réguliers à Lille, et quelques déplacements prévus à l'étranger (COLT à Amsterdam en juillet, WriteTheDocs à Prague et CrownCom à Lisbonne en septembre).

## Mais aussi :

- de l'*enseignement*, à l'ENS de Rennes et l'ENSAI,
- des *projets étudiants*, à CentraleSupélec Rennes,
- des *formations*, à Rennes et à Lille,
- des *conférences* bientôt (COLT'17, CrownCom'17).

----

# Conclusion \& Perspectives

Et beaucoup de choses à faire pour la suite...

> *Merci ! À l'année prochaine.*
