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
  Merci !

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
- Thèse de Navikkumar Modi (2014-2017), *"Machine Learning and Statistical Decision Making for Green Radio"*,
- $10$ ans d'expertise de l'équipe, notamment Christophe Moy, Yves Louët et Jacques Palicot,
- $\implies$ suite des thèses de Wassim et Navikkumar.

## Contexte thématique
- Télécommunications radio et *radio intelligente* (*"cognitive radio"*),
- Réseaux plus efficaces, plus écologiques etc,
- Réseaux avec beaucoup d'objets connectés (*"Internet of Things"*, IoT),
- Apprentissage statistique séquentiel et par renforcement, problèmes et algorithmes de *bandit*, pour résoudre les problèmes d'optimisation combinatoire dans des contextes discrets en temps et fréquence.

## Mon sujet
- *"Apprentissage statistique séquentiel pour la radio cognitive multi-joueurs"*
- Buts :
    + continuer l'étude théorique des algorithmes étudiés et des difficultés intrinsèques des problèmes considérés,
    + étendre ces travaux à différents modèles dans le cas multi-objets et grand nombre d'objets (IoT).
- Applications :
    + utiliser dynamiquement des zones vacantes du spectre radio,
    + insérer plus d'objets communiquant dans un réseau pré-existant,
    + garantir l'optimalité des solutions proposées, etc.

----

# Exemple : *Accès Opportuniste au Spectre* {.allowframebreaks}

Le problème de l'*Accès Opportuniste au Spectre* (*OSA*) consiste en :

- Il y a $K \geq 1$ canaux radio (bandes de fréquence) dans un domaine licencié, avec un temps discret synchronisé (temps et fréquence *discrets*),
- des utilisateurs, dits *primaires* (PU), paient pour utiliser les canaux, mais n'occupent pas densément le spectre,
- un autre utilisateur, dit *secondaire* (SU) veut communiquer, en accédant au canal le moins occupé,
- mais il ne doit pas déranger les PU, et il peut écouter sur *un seul* canal au début de chaque temps discret, et ne fait rien si le canal est occupé.
- Ce trafic ambiant est modélisé par des distributions, par exemple de Bernoulli $B(\mu_1),\dots,B(\mu_K)$ ($\mu_k$ moyenne d'occupation du canal $k$), en supposant les canaux *i.i.d.*,\newline
  (Le comportement des PU est supposé stationnaire)
- Bien-sûr, le SU ne connaît pas la répartition des PU a priori,
- $\implies$ le SU doit trouver le canal le moins occupé, *i.e.* *apprendre* les paramètres $\mu_k$ sous-jacents, en utilisant les échantillons aléatoires qu'il observe ($=$ *récompense*).

> C'est un problème de **décision discrète**, séquentiel (une décision après l'autre), et avec informations partielles, qui correspond à un **problème de bandit**.

----

# Un premier algorithme pour l'OSA : $\mathrm{UCB}_1$ {.allowframebreaks}

L'algorithme UCB (*Upper Confidence Bounds*), dans sa plus simple version ($\mathrm{UCB}_1$, \textcolor{gray}{[Auer et al. 2002]}) fonctionne comme ça :

- Le SU garde en mémoire le nombre de communications $t$, et $X_k(t)$ et $T_k(t)$ deux variables, pour chaque canal $1 \leq k \leq K$,
    + $T_k(t) =$ nombre d'écoute au canal (tentative d'accès),
    + $X_k(t) =$ nombre de fois que le canal $k$ a été détecté disponible $=$ somme de $T_k(t)$ échantillons venant de $B(\mu_k)$.
- L'utilisateur secondaire (SU) commence par essayer une fois chaque canal ($T_k(T) = 1$), dans un ordre arbitraire.
- Pour $t \geq K$, à chaque étape, un *indice* numérique est calculé :
  $$ g_k(t) = \underbrace{\frac{X_k(t)}{N_k(t)}}_{\text{Moyenne}\; \widehat{\mu_k}} + \underbrace{\sqrt{\alpha \frac{\log(t)}{N_k(t)}}}_{\text{"Upper Confidence Bound"}\;}$$
- Le canal maximisant cet indice est choisi ($A(t) = \arg\max g_k(t)$), et s'il est libre, le SU transmet,
- $T_k(t)$, $X_k(t)$ et $t$ sont mis à jour,

> $\alpha > 0$ est un paramètre, contrôlant le compromis entre *exploration* et *exploitation*. $\alpha \geq \frac{1}{2}$ apporte des garanties théorique sur l'efficacité de $\mathrm{UCB}_1$.

----

# Mes objectifs et mes apports

FIXME

> considérer ton apport sous 2 angles : multi-joueurs et passage de l'OSA à l'IoT (donc d'abords OSA et multi-joueurs et les sujets intéressants que ça soulève, puis IoT et multi-joueurs et ce qu'on imagine pour l'instant comme sujets intéressants mais on verra par la suite)

----

# Double encadrement

Avec Émilie Kaufmann, CR au CNRS travaillant à Inria Lille (équipe SequeL, laboratoire CRIStAL) :

- $4$ *visites* de Émilie à Rennes en $2016$, $2$ en mai $2017$,

- $4$ *visites* de Lilian à Lille depuis octobre (de $3$ à $15$ jours), de $3$ semaines en juin,

- *Projets en commun* : Christophe et Émilie publient un *tutorial* à la conférence ICC'17 (Paris, fin mai), et Émilie siège dans le jury de thèse de Navikkumar Modi (mai),

- *Financements* : déplacements pris en charge en $2016$ avec les projets ANR "SoGreen" (Rennes) et "BADASS" (Lille), et depuis mars avec un financement PEPS "BIO" du CNRS obtenu par Émilie et moi ($15000$€ pour $2017$).

----

# Recherches en cours et collaborations ($1/2$)

## Avec Christophe Moy (aspect radio intelligente)
Notamment afin de :

- Poser le bon modèle pour les réseaux IoT,
- Vérifier en pratique (simulation et implémentation réelle) l'intérêt des algorithmes d'apprentissage (type bandit) dans le modèle classique OSA et dans de nouveau modèle multi-joueurs et IoT.

## Avec Émilie Kaufmann (aspect théorique)
- Analyser les performances de différents algorithmes mono- et multi-joueurs dans différents modèles (*e.g.*, preuves de bornes supérieures sur le *regret*),
- et les difficultés intrinsèques de ces problèmes (bornes $\inf$).

----

# Regret d'un algorithme de bandit {.plain}

Le *regret* $R_T^{\mathcal{A}}$ sert à quantifier la perte en *récompense*, après $T$ étapes, entre la meilleure solution et l'algorithme $\mathcal{A}$.

\only<1>{
Par exemple, en \emph{OSA} classique, si $\mu_1 > \mu_2 \geq \dots \geq \mu_K$, alors :
$$ R_T^{\mathrm{UCB}_1} := \mu_1 T - \sum_{t=1}^{T} r_{A(t)}(t), $$
où la récompense du canal $k$ est tirée selon sa loi : $r_k(t) \sim B(\mu_k)$.
}

. . .

On veut montrer des bornes de ce genre :

> - *inférieure* : pour n'importe quel problème $\mu$ d'un certain type, il existe une constante telle que pour tout algorithme $\mathcal{A}$
    $$\lim\inf_{T} \frac{R_T^{\mathcal{A}}}{\log T} \geq C_{\inf}(K, \mu, \dots).$$
> - *supérieure* : pour n'importe quel problème $\mu$ d'un certain type, et pour tel algorithme, il existe une constante telle que
    $$\lim\sup_{T} \frac{R_T^{\mathcal{A}}}{\log T} \leq C_{\sup}(K, \mu, \dots).$$

\only<4>{$\mathcal{A}$ est \emph{optimal} pour cette famille de problème si $C_{\inf}(K, \mu, \dots) = C_{\sup}(K, \mu, \dots)$.}

----

# Recherches en cours et collaborations ($2/2$)

## Avec Rémi Bonnefoi (autre doctorant dans l'équipe SCEE)
Nous étudions l'efficacité et la robustesse de l'utilisation d'algorithmes de bandits utilisés par de nombreux objets "intelligents" dans un réseau de type IoT.

- S'il n'y a plus de PU mais que des SU, l'apprentissage est-il toujours efficace ?
- Est-il encore utile si tous les objets sont dynamiques ?
- Est-il optimal, et à quelle vitesse converge-t-il ?

----

# Autres pistes de recherche ? {.plain}

## Agrégation d'algorithmes de bandit

- Idée : exécuter plusieurs algorithmes similaires en parallèle, sur le même problème, et les faire voter à chaque décision dans l'espoir d'être plus efficace (et plus robuste),
- But : être plus efficace face à des problèmes différents, pour être plus robuste en situation réelle (*e.g.*, où on ne sait pas un modèle de Bernoulli ou Gaussien est approprié).

- Déjà étudié par quelques chercheurs, des algorithmes existent (Exp4 en $2002$, Exp3M et ComBand à NIPS $2015$ et $2016$, variantes de *"Online Gradient Mirror Descent"*),
- j'ai redécouvert l'algorithme Exp4 (et une autre variante) en décembre,
- mais je ne pense pas continuer longtemps dans cette direction : le problème semble (quasiment) résolu par les derniers travaux publié en décembre $2016$.

----

# Autres pistes de recherche ? {.plain}

## Exemple
![aggregating_bandits.png](aggregating_bandits.png)

----

# Objectifs de publication pour $2017$ et $2018$ {.allowframebreaks}

1. Un *rapport de recherche* (arXiv/HAL) résumant le travail de bibliographie, d'implémentation et d'expérimentation réalisé pour mon environnement de simulation (presque terminé) et la publication en libre accès du code (pour l'instant, la documentation est déjà disponible).\newline
  Cf. \urlb{banditslilian.gforge.inria.fr/}

2. Un *article* envoyé à la conférence européenne **CrownCom** $2017$ (septembre, Lisbonne, Portugal) avec Rémi Bonnefoi, suivi d'une version journal étendue (déjà terminée !),

3. Un *article* "maths et théorie" avec Émilie Kaufmann, sur des résultats déjà obtenus et d'autres à terminer, avec de nouvelles bornes inférieures et de meilleures bornes supérieures pour l'algorithme $\rho^{\mathrm{Rand}}$ (OSA multi-joueur décentralisé). *Objectif* : **ICML** ou **COLT** $2018$,

4. Un *article* "ingénieur" exposant l'intérêt de l'agrégation d'algorithmes de bandit pour des problèmes de radio cognitive. *Objectif* : **URSI** ou **GRESTI** $2018$,

5. J'aimerai aussi faire un *survey* sur "tous" les algorithmes de bandits, en les écrivant tous avec la même structure (initialisation, choix, récompense, etc), basé sur mon environnement de simulation. Il y en a une douzaine pour l'aspect mono-joueur (et beaucoup de variantes), et une quinzaine pour l'aspect multi-joueurs, et je les ai tous implémenté et documenté sous une même organisation logique (approche objet).

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

- $24$h/an de TD/TP à l'*ENSAI*, en informatique théorique\footnote{Cf. \urlb{perso.crans.org/besson/ensai-2016/}}, pour le cours "Algorithmique et Calculabilité" de David Cachera, au niveau L3 (1ère année d'école d'ingénieur).

- $40$h/an de TD/oraux à l'*ENS de Rennes*, en informatique théorique, pour la classe de préparation à l'agrégation de maths\footnote{Cf. \urlb{perso.crans.org/besson/agreg-2016/}} (option info), au niveau M2 (3ème année d'ENS). $15$ séances d'entraînement aux oraux d'informatique (leçons et modélisation) et oraux blancs.

> J'ai obtenu la même mission pour les deux prochaines années !
>
> *Note :* je souhaite enseigner en prépa' après ma thèse.

----

# Autres activités ($3/4$) : Projets étudiant {.allowframebreaks}

J'aide quelques élèves pour des projets étudiants, à CentraleSupélec, surtout sur :

- la compréhension et l'implémentation des algorithmes (`C++`, Python),
- l'utilisation de machines GNU/Linux et le logiciel GNU Radio Companion (pilotage de carte radio "USRP" par ordinateur),
- et l'aspect "bidouillage" en général.

## Projet long depuis octobre

- Clément \& Théo : projet long sur un générateur de "trafic ambiant" aléatoire, de type IoT, avec des cartes USRP et GNU Radio (programmation en Python et `C++`). Émission et réception réaliste en temps réel, avec une modulation *QPSK*,

> Rien d'officiel ni de trop coûteux en temps pour l'instant.

> J'espère en faire autant l'an prochain, selon ce qu'on propose.

## Projets courts en février

- Bruno \& Jérôme \& Qingsong : projet court ($5$ semaines) sur le standard IoT *HomeEasy* (pour des "ampoules connectées"), programmation en Python et GNU Radio pour l'émission et la réception,
- Pierre, Matthieu : projet court ($5$ semaines), une webcam sur un Raspberry Pi permet de suivre le niveau de café d'une cafetière, et de réagir lorsqu'elle est vide, pleine etc (programmation Python, traitement d'image embarqué et efficace, communication web).

## Nouveaux projets courts ($5$ semaines) en mai/juin

- Antoine \& Pierre-Jean : implémentation d'algorithmes de bandit (UCB1, Thompson Sampling etc) en Python dans GNU Radio, pour ajouter un utilisateur secondaire s'insérant dynamiquement dans le trafic généré par un projet précédent,
- Flora \& Matthias \& Quentin : implémentation des mêmes algorithmes en `C++` sur des cartes LoRa programmables, pour s'insérer dans un réseau implémentant le standard *LoRa* (modulation/démodulation et trafic ambiant déjà réalisés par un autre projet).

----

# Autres activités variées ($4/4$)

> - Administration système pour nos machines de calcul dans l'équipe SCEE (3 *workstations*, 15 utilisateurs).
>
> - Membre du bureau de l'*Association des Doctorants et Docteurs de l'IETR*\only<2,3>{\footnote{Cf. \urlb{addi.asso.insa-rennes.fr/}}} (**ADDI**) depuis février. Une douzaine d'activités prévues dans l'année (dont la Journée des Doctorants en juillet, la galette des rois de l'IETR en janvier etc).
>
> - Programmeur passionné, j'essaie de contribuer régulièrement à des projets personnels\only<3>{\footnote{Cf. \urlb{Bitbucket.org/lbesson} et \urlb{GitHub.com/Naereen}}} et des grands projets *open-source*, surtout en Bash, OCaml et Python (*e.g.*, bibliothèques `matplotlib`, `jupyter`, `ipython` etc).

----

# Commentaires personnels {.allowframebreaks}

## Points positifs
Tout se passe globalement très bien :

- J'apprécie le co-encadrement et les déplacements à Lille,
- Content d'être venu vivre à Rennes, l'environnement est agréable et sain,
- Mon sujet me correspond, je touche à des aspects variés,
- Je suis libre d'organiser mon temps de travail comme je veux,
- Mes activités d'enseignement me plaisent beaucoup,
- Nos recherches avancent plutôt bien dans les différentes directions,
- Et on ne manque pas de pistes pour continuer.

## Points moins positifs
- Je sais et je constate que je ne suis pas passionné par la recherche,
- J'ai du mal à rester motivé longtemps sur des questions théoriques,
- Manque de motivation envers le système des publications (IEEE etc).

----

# Conclusion \& Perspectives {.allowframebreaks}

## Une première année de thèse déjà bien avancée, avec :

- De la *recherche*, à CentraleSupélec Rennes et Inria Lille, avec mes encadrants (Christophe Moy, Émilie Kaufmann) et un autre doctorant (Rémi Bonnefoi),
- un premier *article* terminé,
- d'autres *objectifs* bientôt,
- des *visites* régulières à Lille.

## Mais aussi :

- De l'*enseignement*, à l'ENS de Rennes et l'ENSAI,
- des *projets étudiants*, à CentraleSupélec Rennes,
- des *formations*, scientifiques et générales à Rennes et à Lille,
- quelques (toutes petites) responsabilités dans l'équipe SCEE et à l'IETR,
- et quelques *conférences* prévues à l'étranger (COLT à Amsterdam en juillet, WriteTheDocs à Prague et CrownCom à Lisbonne en septembre).

----

# Merci

À peine $7$ mois de thèse.

Et beaucoup de choses à faire pour la suite...

\vfill{}

> *Merci !*

> *À l'année prochaine.*
