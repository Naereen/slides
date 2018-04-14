---
author: Lilian Besson
title: CSID - 2ème année de thèse
subtitle: Comité de Suivi Individuel du Doctorant
institute:
  Équipe SCEE, IETR, CentraleSupélec, Rennes \newline
  \& Équipe SequeL, CRIStAL, Inria, Lille \newline
  \newline
  $30$ minutes
smallinstitute: E.-D. MATISSE
date: 18 mai 2018
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
  Merci !

----

# Présentation personnelle

## Rapidement, je suis...
- Français, $24$ ans, je viens des Hautes-Alpes (Briançon),
- Normalien de l'ENS Cachan ($2011-2016$), diplômé en *mathématiques* et *informatique* (agrégation en $2014$, master MVA en $2016$).

. . .

## Avant et maintenant...
- *Avant* : stages de recherche en $2012$, $2013$, et $2016$, un an d'enseignement en $2014$-$2015$,
- *En thèse* depuis octobre $2016$, basé à Rennes, avec un financement ministériel ("contrat doctoral spécifique normalien"),
- Passionné par l'enseignement et la programmation, je souhaite *enseigner* l'informatique, en classes préparatoires ou à l'université, après ma thèse plutôt que de rester en recherche ou aller dans l'industrie.

----

# Contexte et sujet {.allowframebreaks}

## Historique de l'équipe SCEE sur ce sujet
- Thèse de Wassim Jouini ($2008$-$2012$), *"Contribution to learning and decision making under uncertainty for Cognitive Radio"*,
- Thèse de Navikkumar Modi ($2014$-$2017$), *"Machine Learning and Statistical Decision Making for Green Radio"*,
- $10$ ans d'expertise de l'équipe, notamment Christophe Moy, Yves Louët et Jacques Palicot,
- $\implies$ suite des thèses de Wassim et Navikkumar.

## Contexte thématique
- Télécom radio et *radio intelligente* (*"cognitive radio"*),
- Réseaux plus efficaces, plus écologiques etc,
- Réseaux avec beaucoup d'objets connectés (*"Internet of Things"*, IoT),
- Apprentissage statistique séquentiel et par renforcement, problèmes et algorithmes de *bandit*, pour résoudre les problèmes d'optimisation combinatoire dans des contextes discrets en temps et fréquence.

----

# Double encadrement

Avec Émilie Kaufmann, CR au CNRS travaillant à Inria Lille (équipe SequeL, laboratoire CRIStAL) :

- Total de $3$ *visites* de Lilian à Lille depuis septembre $2017$ ($1+2+1$ semaines)
- $2$ visites prévues en mai et juin ($1+1$ semaines)

- *Projets en commun* : moins qu'en 1ère année,

- *Financements* : financement PEPS "BIO" du CNRS obtenu par Émilie et moi (pour $2017$), projet ANR "BADASS" (Lille), et dotation SCEE (pour $2018$).

----

# Mon sujet
- *"Apprentissage statistique séquentiel pour la radio cognitive multi-joueurs"*
- Buts :
    + continuer l'étude théorique des algorithmes étudiés et des difficultés intrinsèques des problèmes considérés,
    + étendre ces travaux à différents modèles dans le cas multi-joueurs, et grand nombre d'objets (IoT).
- Applications :
    + utiliser dynamiquement des zones vacantes du spectre radio,
    + insérer plus d'objets dans un réseau pré-existant,
    + garantir l'optimalité des solutions proposées, etc.

----

# Recherches en cours et collaborations ($1/2$)

## Avec Christophe Moy \hfill{} (aspects radio intelligente)
Notamment afin de :

- Poser le bon modèle pour les réseaux IoT,
- Vérifier en pratique (simulation et implémentation réelle) l'intérêt des algorithmes d'apprentissage (type bandit) dans le modèle classique OSA et dans de nouveau modèle multi-joueurs et IoT.

## Avec Émilie Kaufmann \hfill{} (aspects théoriques)
- Analyser les performances de différents algorithmes mono- et multi-joueurs dans différents modèles (*e.g.*, preuves de bornes supérieures sur le *regret*),
- et les difficultés intrinsèques de ces problèmes (bornes $\inf$).



# Recherches en cours et collaborations ($2/2$)

## Avec Rémi Bonnefoi (autre doctorant dans l'équipe SCEE)
- Demo ICT $2018$

## Avec XXX XXX (doctorant à Inria Grenoble)
- XXX

----

# Publications depuis le début de ma thèse {.allowframebreaks}

1. Un *article* présenté à la conférence européenne **CrownCom** $2017$ (septembre, Lisbonne) avec Rémi Bonnefoi. *Best paper award* ! Aucune nouvelle pour la version longue... `HAL.Inria.fr/hal-01575419`

2. Un *article* "maths et théorie" avec Émilie Kaufmann, avec de nouvelles bornes inférieures et de meilleures bornes supérieures pour l'algorithme $\rho^{\mathrm{Rand}}$ et deux nouveaux algorithms (OSA multi-joueur décentralisé). Présenté à la conférence **ALT** $2018$ (avril, Lanzarote). Poster présenté à un atelier international à Rotterdam (fin mai). `HAL.Inria.fr/hal-01629733`

3. Un *article* "télécom" exposant l'intérêt de l'agrégation d'algorithmes de bandit pour des problèmes de radio cognitive. Présenté à la conférence **IEEE WCNC** $2018$ (avril, Barcelone). `HAL.Inria.fr/hal-01705292`

2. Un *article* "maths et théorie" avec Émilie Kaufmann, étudiant le "doubling trick" (voir plus tard). Envoyé à la conférence **COLT** $2018$ (juillet, Stockholm). Retour pas excellent... `HAL.Inria.fr/hal-01736357`

5. Ma bibliothèque d'algorithmes de bandits (simple et multi-joueurs), `SMPyBandits`, documentation `SMPyBandits.GitHub.io`, et rapport en accès libre `perso.crans.org/besson/articles/SMPyBandits.pdf`. Publié sur MLOSS (`MLOSS.org/software/view/710`), bientôt envoyé au JMLR MLOSS (journal en ligne). Déjà ~ 1000 vues en 3 mois.

----

# Présentation de quelques résultats de recherche {.allowframebreaks}

> Article sur le "Doubling Trick"

MATHS

MATHS

MATHS

MATHS

----

# Objectifs de recherche pour $2018$ {.allowframebreaks}

1. J'aimerai aussi faire un *survey* sur "tous" les algorithmes de bandits, en les écrivant tous avec la même structure (initialisation, choix, récompense, etc), basé sur mon environnement de simulation. Il y en a une trentaine pour l'aspect mono-joueur (et beaucoup de variantes), et une quinzaine pour l'aspect multi-joueurs, et je les ai tous implémenté et documenté sous une même organisation logique (approche objet). Pas sûr d'où publier ça si je l'écris...

2. Un algorithme générique pour s'adapter à des récompenses bornées dans un intervalle inconnu.

3. Un algorithme générique pour s'adapter à des problèmes avec $K$ bras mais seulement $s < K$ ayant des moyennes positives (bandits parcimonieux, "sparse").

4. Travailler encore un peu sur les bandits multi-joueurs, notamment pour : découvrir le nombre de joueurs, autoriser

----

# Présentation de quelques directions de recherches

----

# Autres activités

Mais aussi...

----

# Autres activités ($1/4$) : Formations

Pour la thèse, il faut suivre des formations...
J'ai presque tout fait des $72$ heures exigées. Il me reste :

- Scientifiques :
    + Présentations à des conférences et ateliers,
    + Présentation à la Journée des Doctorants de l'IETR en juin,

- Générales ou professionnelles :
    + À l'Université de Rennes 1, mais peu sont proposés...
    + Formations internes (GouTP) à CentraleSupélec Rennes ? Pas sûr que "ça passe"...

> Encore quelques heures à faire, ce sera bouclé d'ici octobre !

----

# Autres activités ($2/4$) : Enseignements

Par passion et pour (espérer) valider mon stage d'agrégation, j'enseigne :

- $24$h/an de TD/TP à l'*ENSAI*, en informatique théorique\footnote{Cf. \urlb{perso.crans.org/besson/ensai-2017/}}, pour le cours "Algorithmique et Calculabilité" de David Cachera, au niveau L3 (2ème année d'école d'ingénieur).

- $48$h/an de TD/oraux à l'*ENS de Rennes*, en informatique théorique, pour la classe de préparation à l'agrégation de maths\footnote{Cf. \urlb{perso.crans.org/besson/agreg-2017/}} (option info), au niveau M2 (3ème année d'ENS). $15$ séances d'entraînement aux oraux d'informatique (leçons et modélisation), TP de programmation, et oraux blancs.

> J'ai obtenu la même mission pour $2019$.
>
> Plus un éventuel poste de PRAG à l'ENS de Rennes pour continuer ensuite... A suivre !

----

# Autres activités variées ($3/4$)

- Administration système pour nos machines de calcul dans l'équipe SCEE (3 "*workstations*", 15 utilisateurs).

- En charge des "GouTP", nos formations internes à SCEE (et aux autres équipes du bâtiment), base mensuelle. $5$ formations depuis le lancement en janvier $2017$. Franc succès !

- Programmeur passionné, j'essaie de contribuer régulièrement à des projets personnels\footnote{Cf. \urlb{Bitbucket.org/lbesson} et \urlb{GitHub.com/Naereen}} et des grands projets *open-source*, surtout en Bash, OCaml et Python (*e.g.*, bibliothèques `matplotlib`, `jupyter`, `ipython` etc).

----

# Exemples de projets personnels en $2017-18$ ($4/4$) {.allowframebreaks}

- Quelques petits projets pour faciliter l'utilisation des Notebooks Jupyter avec le langage OCaml (utilisé en option info en prépa et pour l'agrég). `GitHub.com/Naereen/fix-iocaml-notebook-exports-to-pdf` et `GitHub.com/Naereen/Jupyter-NBConvert-OCaml`

- Module Python et Julia pour calculer la complexité de Lempel-Ziv sur des chaînes binaires. `GitHub.com/Naereen/Lempel-Ziv_Complexity`. Environ 500 téléchargements.

- Un peu de traitement d'images et de programmation web pour une application web qui créée une police manuscrite "personnelle" à partir d'un échantillon d'écriture manuscrite. {\Fontify Fontify} `GitHub.com/Naereen/Fontify`

- Formation et expérimentations en apprentissage par renforcement profond ("deep reinforcement learning") pour apprendre à jouer à un jeu vidéo à partir des pixels de l'écran. Exemple avec des jeux ATARI (classique) et NES (dont un Mario qui n'a jamais été traité comme ça avant). Encore en cours (c'est pas simple). `GitHub.com/Naereen/gym-nes-mario-bros`

- Implémentation pédagogique d'un sous-ensemble du langage Prolog, en OCaml, pour mes élèves d'agrég. `GitHub.com/Naereen/Tiny-Prolog-in-OCaml`

----

# Conclusion \& Perspectives

----

# Conclusion \& Perspectives {.allowframebreaks}

## Une première moitié de thèse efficace

- De la *recherche*, à CentraleSupélec Rennes et Inria Lille, avec mes encadrants (Christophe Moy, Émilie Kaufmann) et un autre doctorant (Rémi Bonnefoi),
- $5$ *articles* terminés, dont $3$ publiés et présentés (uniquement des conférences),
- d'autres *objectifs* bientôt,
- des *visites* régulières à Lille.

## Mais aussi pour $2019$...

- La même charge d'*enseignement*, à l'ENS de Rennes et l'ENSAI,
- encore quelques heures de *formations* (générales) à Rennes,
- et quelques *conférences* prévues à l'étranger (ICT à St-Malo en juin, COLT à Stockholm en juillet ? AISTATS à Okinawa en avril $2019$ ?).

----

# Merci

Déjà la moitié de ma thèse.

Et beaucoup de choses à faire pour la suite...

\vfill{}

\begin{center}\begin{Huge} {\Fontify Merci !} \end{Huge}\end{center}

> *À l'année prochaine... pour la soutenance !?*
