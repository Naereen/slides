<!--
page_number: true
footer: Présentation : Directions de recherche (notamment avec Rémi) |  Date : Fin Juin 2017  |  Par : Lilian Besson
-->


# Présentation
## Directions de recherche (notamment avec Rémi)

 - Quelques directions auxquelles on a pensé
 - Expliquées rapidement ici (pas encore bcp boulot dessus)
 - Dites-nous ce que vous en pensez :
   + quelle(s) direction(s) favoriser
   + d'autres idées ?
   + dans quel ordre ?


> *Merci d'avance !*

----

# Version poster de notre article CrownCom'17

- Déjà fait !
- Disponible en ligne $\to$ [lbo.k.vu/JdD2017](http://lbo.k.vu/JdD2017) (LaTeX et [PDF](https://bitbucket.org/scee_ietr/phd-student-day-ietr-2017-bonnefoi-and-besson/downloads/poster.pdf))
  ([Bitbucket non-officiel de l'équipe SCEE](https://bitbucket.org/scee_ietr/))
- Présenté bientôt par Rémi à la Journée des Doctorants (03 juillet 2017) @ Rennes (*que j'organise*)
- (?) Présenté par Lilian au [Workshop on Decentralized Machine Learning, Optimization and Privacy (Sep 11-12, 2017)](https://team.inria.fr/magnet/workshop-on-decentralized-machine-learning-optimization-and-privacy/) @ Lille

----

# Version longue de notre article CrownCom'17 $\to$ journal !

- Ajout explication algorithmes adversariaux, notamment Exp3 (presque OK)
- Ajout simulation comparant Exp3 et un SoftMax à UCB, Thompson etc (OK)
- Preuve détaillée/rigoureuse de l'utilisation des multiplicateurs de Lagrange pour le problème d'optimisation considéré (OK)
- Simulation si les objets dynamiques :iphone: et statiques :phone: ont différents taux d'activation $p$ (ex.:iphone: plus actif que :phone:), $p_1,p_2$
- Simulation si chaque taux d'activation est différent $p_k, k \in [S+D]$ (plus compliqué) :warning: application réaliste?

----

# Version longue de notre article CrownCom'17 $\to$ journal !

- Preuve ou justification que UCB / Thompson Sampling marche dans ce cadre non-*i.i.d.* : aucune idée :warning:
- Et justification face à l'activation "discrète" : l'apprentissage de chaque objet a lieu "une fois de temps en temps" (activation $\sim \mathrm{Bern}(p_k)$), à des temps différents
- $\hookrightarrow$ *"sparse" learning* ? est-ce un truc connu ? (@Emilie?)

----

# CrownCom'17 $\to$ journal !
## Essayer avec plus de stations de base :satellite: ?

- But : ajouter une dimension **spatiale** à l'apprentissage
  *(mais les objets n'ont pas besoin de le savoir)*
- Intuition : on obtiendra des regroupements automatiques, par "clusters" autours de chaque BTS :satellite:
- Cf. discussion plus bas sur le *"capture effect"* qu'on pourrait aussi considérer (un autre modèle de collision)
- :warning: ça fera peut-être trop pour la version journal
  (on ne peut pas tripler la taille de l'article !)

----

# $\hookrightarrow$ Généraliser le regret "au cas IoT" ?

- $K$ canaux, $M \gg K$ objets, avec des taux d'activation très faibles (activation Bernoulli, moyenne $p$)
- **Collisions** : perte de récompense si des objets utilisent le même canal en même temps (modèle classique)
- $R_T$ classique est une $\mathbb{E}$ sur les récompenses ($\mathbb{E}_{\mu}$), peut-être doit-on considérer un autre regret ("sparse regret" ?)
  $\tilde{R}_T$ qui fasse aussi $\mathbb{E}$ sur les activations $\mathbb{E}_{\mu,p}$
- $\Longrightarrow$ Bornes inf / sup ?!
- *(je n'ai pas essayé pour l'instant)*

----

# Idées pour améliorer des algorithmes de bandit

1. Être plus robuste face à des environnements "lentement dynamique" (de temps en temps, les distributions des bras changent vraiment) :
   - avec une fenêtre glissante
   - autorise à se remettre en cause "après avoir convergé"
   - ex : échelle de temps d'une semaine pour des objets communiquants

2. (pas encore d'autres)

----

## Être plus robuste : *"fenêtre glissante"*
- Avec une fenêtre glissante de taille $\tau$ "moyenne", on garde une petite moyenne empirique $\hat{\mu}_k(t-\tau \ldots \tau)$ (ou variance empirique)
- Si la petite moyenne devient trop éloignée de la moyenne complète ($|\hat{\mu}_k(t-\tau \ldots t) - \hat{\mu}_k(0 \ldots \tau)| \geq \varepsilon$), on remet les statistiques internes de l'algorithmes avec la petite moyenne

- :wrench: Peut être malin, mais dur de savoir comment choisir $\tau$ et $\varepsilon$ : dépendent de la fréquence de changement (inconnue)...

----

## Être plus robuste : *"fenêtre glissante"*

> Si la distribution des bras est connue, on peut lier les deux paramètres à un seul paramètre de "confiance" (@Rémi ?)

- Facile à coder pour un algorithme basé sur $\hat{\mu}_k(t)$ et $N_k(t)$ nb sélections du bras $k$  (e.g., UCB, kl-UCB)
- Déjà testé : $\to$ [`Policies.SlidingWindowsRestart`](http://banditslilian.gforge.inria.fr/docs/Policies.SlidingWindowsRestart.html)
- Marche mal empiriquement... (*pour les valeurs essayées*, et impossible de savoir lesquelles peuvent marcher)
- Plus dur pour des algorithmes Bayésiens (demande l'historique de taille $\tau$ pour réinitialiser les posteriors avec l'historique partiel : consomme de la mémoire),
- et (je pense) impossible pour des algorithmes génériques...

----

<center><img width="100%;" src="premiers_calculs_sur_la_moyenne.png"></center>

----

# Autre idée : on/off de stations de base

> Apprentissage centralisé, doit couvrir tous les utilisateurs avec la plus faible consommation éléctrique possible...

- Suite Navik (& un peu Rémi).
- Approche combinatoire, bras = configuration des $B$ stations de base : taille espace d'état $\propto 2^B$ :boom:
- Passe pas à l'échelle avec un réseau "dense" ($B \geq 10$)
- Idée pour une approche moins coûteuse ?
  $\to$ "Bandit combinatoire" ? (@Emilie?)
- :boom: pas clair de savoir si on peut faire plus que ce qui a été fait (pas forcément intéressant)
- :warning: cadre applicatif réaliste ? (*je pense que oui*)

---

# Autre idée : *"transfert learning"* avec des algorithmes connaissant $T$

- Si l'horizon $T$ est connue, comme c'est le cas dans les utilisations de "transfer learning" (TL), ex. par Navik
- Alors autant utiliser des algorithmes qui exploitent $T$ pour être plus efficace (ex kl-UCB+ ou UCB+)
- [ApproximatedFiniteGHIndex](http://banditslilian.gforge.inria.fr/docs/Policies.ApproximatedFHGittins.html#module-Policies.ApproximatedFHGittins) semble être excellent dans ce cas (par Tor Lattimore, COLT 2016)
- Exemple : $T = 1$h ou $T = 1$ jour
- :warning: mais on a pas de **cadre applicatif** novateur ou vraiment intéressant... Idée ?! (@Christophe?)

----

# Suite projets élèves

> :boom: On doit continuer et finir les projets des élèves

*Rappels* : 2 projets longs (Théo & Clément, Jihane & Salma), 2 projets courts... Presque rien des courts, mais les longs ont donné :

- émetteur/récepteur LoRa (modulation/démodulation) réaliste
- générateur traffic "interférant" aléatoire (configurable :wrench:)
- station de base :satellite: qui écoute et détecte sur $K$ canaux
- $\Longrightarrow$ produire un beau démonstrateur avec GNU Radio pour *"MAB algorithms for real-world LoRa IoT networks"*
  + on peut en faire une démo à présenter (dans une conf' ?)
  + et un article (avec le nom des élèves mais fait par nous)

----

# Suite projets élèves

- Rémi a déjà beaucoup avancé pour la partie LoRa
 *(Jihane et Salma on fait du bon boulot)*
- On fera ensemble l'objet intelligent qui s'insère dans le réseau
- On va pouvoir connecter facilement ma "grosse" collection d'algorithmes ([banditslilian.gforge.inria.fr/docs/Policies.html](banditslilian.gforge.inria.fr/docs/Policies.html))
- On va rédiger un mini-article présentant la démo, avec Rémi, Christophe et Lilian (==et Emilie ?==), et les 4 élèves (mais on n'espère pas de l'aide de leur part)

----

# Suite projets élèves

- Démo : j'aimerai une interface graphique sexy :heart: (comme ce qu'a fait Quentin, lançable sans passer par GNU Radio)
- Contrairement à la démo ICC de Christophe, avec plusieurs algorithmes en parallèle, on veut un seul algorithme (un seul objet communiquant)
- Mais un large choix d'algorithme et de paramètre, qu'on puisse changer en cours d'expériences (en réinitialisant l'algo) 
- Ex: pour vérifier de façon intéractive que $\mathrm{UCB}_{\alpha}$ converge plus pour de petits $\alpha$, que TS est plus rapide que kl-UCB etc...

----

## Aperçu démo de Quentin : jolie interface :heart:
![test](demo_interface_quentin.png)


----

# Plusieurs stations de base (BTS :satellite:), collision selon le *"capture effect"*

> Un autre modèle de collision, plus complexe mais plus réaliste

- Plus un objet est près de la BTS, plus elle reçoit ses messages avec un SINR fort. La BTS peut décider de répondre seulement si SINR $\geq \theta$ (un certain seuil), ou juste à celui qui a le plus fort SINR (*"near-or-far" effect*)
- SNIR = $\propto P_R / (N + \sum\limits_{\text{objet}} P_{R_i})$
- A distance $d$, l'interférence est souvent modélisée $\sim d^{-\alpha}$ (pour $\alpha \in [2,5]$ selon le milieu ambiant)
- Modèle déjà implémenté ([`closerUserGetsReward`](http://banditslilian.gforge.inria.fr/docs/Environment.CollisionModels.html#Environment.CollisionModels.closerUserGetsReward)) pour une distance (comme si SNIR $\propto d$, irréaliste mais simple)

----

# Plusieurs stations de base (BTS :satellite:), collision selon le *"capture effect"*

- A faire : implémenter un modèle de collision selon le SNIR
- Mettre $\geq 2$ BTS :satellite: sur une carte 2D, répartir des objets :iphone: sur la carte, aléatoirement (comme Navik)
- Montrer que les objets convergent vers des configurations orthogonales au sein de chaque cellule, et aux frontières des cellules aussi (cf. dessin au tableau)
  + (cf. répartition des fréquences pour la télé en "*large cells network*")
- *Intuition* : ça va marcher automatiquement sans trop de soucis
- :boom: Encore le même problème : prouver des garanties théoriques sur cette réussite empirique ne sera pas facile...

----

# Fin

## ==D'autres idées ?==

## ==Discussion==


> *Merci*