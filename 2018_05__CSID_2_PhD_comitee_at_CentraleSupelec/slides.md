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
- Français, $25$ ans, je viens des Hautes-Alpes (Briançon),
- Normalien de l'ENS Cachan ($2011-2016$), diplômé en *mathématiques* et *informatique* (agrégation en $2014$, master MVA en $2016$).

. . .

## Avant et maintenant...
- *Avant* : stages de recherche en $2012$, $2013$, et $2016$, un an d'enseignement en $2014$-$2015$,
- *En thèse* depuis octobre $2016$, basé à Rennes, avec un financement ministériel ("contrat doctoral spécifique normalien"),
- Passionné par l'enseignement et la programmation, je souhaite *enseigner* l'informatique après ma thèse.

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

Avec **Émilie Kaufmann**, CR au CNRS travaillant à Inria Lille (équipe SequeL, laboratoire CRIStAL) :

- Total de $3$ *visites* de Lilian à Lille depuis septembre $2017$ ($1+2+1$ semaines)
- $4$ visites prévues (mai, juin, octobre, décembre) ($1+1+1+2$ semaines)

- *Projets en commun* : moins qu'en 1ère année (aucun ?),

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

----

# Recherches en cours et collaborations ($2/2$)

## Avec Rémi Bonnefoi (autre doctorant dans l'équipe SCEE)
Démo réalisée ensemble, présentée en juin à la conférence ICT $2018$ (St-Malo) :

- Basée sur notre article CROWNCOM $2017$,
- **"MALIN"**: **M**ulti-**A**rmed bandits **L**earning in **I**oT **N**etworks,
- Avec GNU Radio + Python + C++,
- Avec des cartes USRP (via notre TestBed),
- Rien de révolutionnaire, juste une illustration (et vérification) de nos travaux théoriques...

----

# Publications depuis le début de ma thèse {.allowframebreaks}

1. Un *article* présenté à la conférence européenne **CrownCom** $2017$ (septembre, Lisbonne) avec Rémi Bonnefoi. *Best paper award* ! Publié, mais aucune nouvelle pour la version longue... \footnote{Cf. \urlb{HAL.Inria.fr/hal-01575419}}

2. Un *article* "maths et théorie + télécom" avec Émilie Kaufmann, avec de nouvelles bornes inférieures et de meilleures bornes supérieures pour l'algorithme $\rho^{\mathrm{Rand}}$ et deux nouveaux algorithms (OSA multi-joueur décentralisé). Présenté à la conférence **ALT** $2018$ (avril, Lanzarote). Poster présenté à un atelier international à Rotterdam (fin mai). \footnote{Cf. \urlb{HAL.Inria.fr/hal-01629733}}

3. Un *article* "machine learning for télécom" exposant l'intérêt de l'agrégation d'algorithmes de bandit pour des problèmes de radio cognitive. Présenté à la conférence **IEEE WCNC** $2018$ (avril, Barcelone). \footnote{Cf. \urlb{HAL.Inria.fr/hal-01705292}}

2. Un *article* "maths et théorie" avec Émilie Kaufmann, étudiant le "doubling trick" (voir plus tard). Envoyé à la conférence **COLT** $2018$ (juillet, Stockholm). Retour pas excellent, on attends la réponse finale... Pas de lien direct avec les télécoms \footnote{Cf. \urlb{HAL.Inria.fr/hal-01736357}}

5. Ma bibliothèque d'algorithmes de bandits (simple et multi-joueurs), `SMPyBandits`, documentation `SMPyBandits.GitHub.io`, et rapport en accès libre \footnote{Cf. \urlb{perso.crans.org/besson/articles/SMPyBandits.pdf}}. Publié sur MLOSS (`MLOSS.org/software/view/710`), bientôt envoyé au JMLR MLOSS (journal en ligne). Déjà $\sim 1000$ vues en $3$ mois...

----

# Présentation de quelques résultats de recherche

Je préfère présenter un seul des travaux, le plus récent.

> **What Doubling Tricks Can and Can't Do for Multi-Armed Bandits**, Lilian Besson \& Emilie Kaufmann, Feb 2018
>
> En accès libre : `HAL.Inria.fr/hal-01736357`

----

# "Doubling trick" : rapide présentation

## Horizon $T$ : mieux de ne pas la connaître
- En apprentissage séquentiel, les expériences durent de $t=1$ à $t=T$ ($T =$ **horizon**),
- Pour des applications réelles, les algorithmes ne doivent pas connaître l'horizon...
- Mais beaucoup sont développés avec principalement la théorie en tête, et dépendent de la valeur de $T$ !

## But

- $\hookrightarrow$ Peut-on transformer un algorithme dépendant de $T$ et le rendre indépendant de l'horizon ?
- $\implies$ **Oui !**
- Une technique classique : "doubling trick" !

----

# Algorithme du "Doubling trick"

![](Generic_Doubling_Trick_algorithm.png)

----

# Deux "doubling" : géométrique et exponentiel

- $T_0 \in \mathbb{N}$, $(T_i)_{i\in\mathbb{N}}$ croissant et divergeante ($\to+\infty$ pour $i\to\infty$).
- "Dernier terme" : $L_T := \min\{ i \in\mathbb{N} : T_i > T\}$.

## Géométrique
- Pour un paramètre $b > 1$,
- $T_i := \lfloor T_0 b^i\rfloor$,
- $L_T = \lceil \log_b\left( \frac{T}{T_0} \right) \rceil$.

## Exponentiel
- Pour deux paramètres $a, b > 1$,
- $T_i := \lfloor \frac{T_0}{a} a^{b^i}\rfloor$,
- $L_T = \lceil \log_b\left( \log_a\left( \frac{T}{T_0/a} \right) \right) \rceil$.

----

# Regret et but
## Regret ?
- $R_T(A_T)$ mesure la performance moyenne de l'algorithme $A$ (qui peut connaître $T$), sur une expérience d'horizon $T$.
- $R_T(A) := \sum_{t=1}^T \mu^* - \mathbb{E}[\mu_{A(t)}]$ pour un problème à $K$ bras de moyennes $\mu_1,\dots,\mu_K$, $\mu^* := \arg\max_k \mu_k$ et $A(t)$ le choix de l'algorithme à l'instant $t$.

## But : conserver des bornes de regret !
- Si $A$ vérifie une borne de regret, *e.g.*, $R_T(A_T) \leq f(T)$
- Alors la version indépendante de $T$, $\mathrm{DT}(A)$, vérifie une borne similaire, avec un coût constant ou non
    + $R_T(\mathrm{DT}(A)) \leq \ell(\text{paramètres du problème}) f(T)$ : bien !
    + $R_T(\mathrm{DT}(A)) \leq \ell(\text{paramètres du problème}) g(T)$ : moins bien ! (pour $g(T) \gg f(T)$).

----

# Types de bornes
> $c$ est une constante muette, $c > 0$, dépendant des paramètres $K,\mu_1,\dots,mu_K$ du problème (et de l'algorithme), mais indépendante de $T$.

## Indépendant des paramètres
- $R_T(A_T) \leq c \sqrt{T}$

## Dépendant des paramètres
- $R_T(A_T) \leq c \log(T)$

## Forme générique
- $R_T(A_T) \leq c (\log T)^{\delta} T^{\gamma}$
    + $\delta=0,\gamma>0$ (adverse),
    + ou $\delta>0,\gamma=0$ (stochastique),
    + ou $\delta>0,\gamma>0$ (hybride!).

----

# Résultats avec un "doubling" géométrique

## Conserve bien $R_T \leq \sqrt{T}$
- Perte constante $\ell(b,\gamma) = \frac{b^{\gamma}(b-1)^{\gamma}}{b^{\gamma}-1} > 1$.

## Conserve pas bien $R_T \leq \log(T)$
- On sait que ça ne peut pas marcher !
- On a une borne inférieure : transforme ${(\log T)}^{\delta}$ en ${(\log T)}^{\delta}$.

----

# Résultats avec un "doubling" exponentiel

## Conserve *peut-être* $R_T \leq \sqrt{T}$
- Pas encore de borne sup ou inf convainte
- Transforme $\leq T^{\gamma}$ en $T^{b \gamma}$, pas top...
- Borne inf a la forme inverse, $\geq T^{\gamma}$ en $T^{\frac{\gamma}{b}}$...

## Conserve bien $R_T \leq \log(T)$
- Perte constante $\ell(\delta, b) = \frac{b^{2\delta}}{b^{\delta}-1} > 1$ ($> 4$ pour $\delta=1$).

----

# Questions encore ouvertes

- Un schéma intermédiaire qui conviendrait pour les trois types de bornes ?
- Une autre approche "plus intelligente" qui permettrait d'obtenir des meilleures garanties ?
- Empiriquement : choisir des paramètres ($T_0, b$ ou $T_0,a,b$) n'est pas simple, comment bien les choisir ?

## Question bonus
- Où publier cet article ?

----

# Applications de ce travail
- Très générique !
- Donne une meilleure compréhension théorique de cette technique très utilisée depuis $\sim$ 20 ans (au moins).
- Justifie un nombre déraisonnable d'articles qui utilisent le "doubling trick" sans justifier plus qu'une note de bas de page disant "on perd une constante"...

## En radio intelligente ? Oui aussi !
1. Si Alice utilise un algorithme $A_T$ très efficace dans son contexte, mais qui dépend de $T$ (*e.g.*, *Approximated Finite-Horizons Gittins Index* en bandits simple joueur, *Musical Chair* en bandits multi-joueurs, etc),
2. Si elle sait quel genre de garantie elle espère (contexte stochastique, ou adverse, ou hybride),
3. Alors elle peut savoir quel "doubling trick" utiliser pour rendre son algorithme indépendant de $T$ le plus efficacement possible (on connaît $\delta,\gamma$ alors on choisit $T_0,b$ ou $T_0,a,b$ pour minimiser la perte constante $\ell$...).

----

# Objectifs de recherche pour $2018$ {.allowframebreaks}

1. J'aimerai aussi faire un *survey* sur "tous" les algorithmes de bandits, en les écrivant tous avec la même structure (initialisation, choix, récompense, etc), basé sur mon environnement de simulation. Il y en a une trentaine pour l'aspect mono-joueur (et beaucoup de variantes), et une quinzaine pour l'aspect multi-joueurs, et je les ai tous implémenté et documenté sous une même organisation logique (approche objet). Pas sûr d'où publier ça si je l'écris...

2. Un algorithme générique pour s'adapter à des récompenses bornées dans un intervalle inconnu.

3. Un algorithme générique pour s'adapter à des problèmes avec $K$ bras mais seulement $s < K$ ayant des moyennes positives (bandits parcimonieux, "sparse").

4. Travailler encore un peu sur les bandits multi-joueurs, notamment pour : découvrir le nombre de joueurs, autoriser

----

# Présentation de quelques directions de recherches

> Discussion sur des idées de directions...

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

- Quelques petits projets pour faciliter l'utilisation des Notebooks Jupyter avec le langage OCaml (utilisé en option info en prépa et pour l'agrég). \footnote{Cf. \urlb{GitHub.com/Naereen/fix-iocaml-notebook-exports-to-pdf} et \urlb{GitHub.com/Naereen/Jupyter-NBConvert-OCaml}}

- Module Python et Julia pour calculer la complexité de Lempel-Ziv sur des chaînes binaires. \footnote{Cf. \urlb{GitHub.com/Naereen/Lempel-Ziv_Complexity}} Environ 500 téléchargements.

- Un peu de traitement d'images et de programmation web pour une application web qui créée une police manuscrite "personnelle" à partir d'un échantillon d'écriture manuscrite. {\Fontify{Fontify}} \footnote{Cf. \urlb{GitHub.com/Naereen/Fontify}}

- Formation et expérimentations en apprentissage par renforcement profond ("deep reinforcement learning") pour apprendre à jouer à un jeu vidéo à partir des pixels de l'écran. Exemple avec des jeux ATARI (classique) et NES (dont un Mario qui n'a jamais été traité comme ça avant). Encore en cours (c'est pas simple). \footnote{Cf. \urlb{GitHub.com/Naereen/gym-nes-mario-bros}}

- Implémentation pédagogique d'un sous-ensemble du langage Prolog, en OCaml, pour mes élèves d'agrég. \footnote{Cf. \urlb{GitHub.com/Naereen/Tiny-Prolog-in-OCaml}}

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

\begin{center}\begin{Huge} {\Fontify{Merci !}}\end{Huge}\end{center}

> *À l'année prochaine... pour la soutenance !?*
