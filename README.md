# MorpionTPE, une intelligence artificielle imbattable au morpion

## Version d'essai en ligne

[Interpréteur Python en ligne](https://repl.it/@NathanFallet/MorpionTPE)

## Vidéo

[Voir la vidéo sur Youtube](https://youtu.be/29M3_ot8dU4)

## Script de la vidéo

### Introduction

L'intelligence artificielle se fonde sur l'hypothèse que le processus de pensée humain peut être mécanisé. Cela commence dès l’antiquité mais prend une toute autre empleur avec l’arrivé des composants électroniques au milieu des années 50.

Notre intelligence artificielle sera composée d’un algorithme, c’est à dire une suite d’instructions qui seront exécutées les unes après les autres, et d’une logique statistique, qui va étudier les cas possibles de jeu afin de gagner à chaque partie, notre intelligence artificielle ne pouvant donc jamais perdre.

Nous allons, dans un premier temps, construire le morpion en lui même, et ensuite y intégrer notre intelligence artificielle contre laquelle nous pourrons jouer.

### Construction du morpion

Le morpion est un jeu de réflexion se pratiquant à deux joueurs au tour par tour, dont le but est de créer en premier un alignement de trois signes : des ronds ou des croix. Il tire son origine de l’Égypte Antique où ont été retrouvées des parties datant d’environ 1300 av. J.C.

Nous allons, grâce au langage Python, créer l’algorithme du morpion en lui même. Il sera composé de plusieurs fichiers :
- game.py, qui se charge du déroulement général de la partie,
- player.py, qui correspond aux données basiques de tout joueur, c'est à dire son signe, la fonction qui permet jouer,
- human.py, qui est une implémentation de player.py, c’est à dire qu’il sera basé sur ce fichier en y ajoutant des fonctionnalités,
- Et main.py, qui vient mettre tout ça ensemble et lancer la partie.

Commençons par game.py. Sa première fonction est la fonction d’initialisation de l’objet. Elle crée un tableau de jeu et enregistre les joueurs données par le fichier main.py que nous verrons plus loin.

Ensuite, vient la fonction start : elle démarre la partie et gère son déroulement. Une boucle fait jouer chaque joueur chacun leur tour jusqu’à ce qu’il y aie un gagnant ou un match nul (instruction while et for). A chaque tour elle affiche le tableau de jeu actuel (la fonction show, que nous verrons après), le joueur qui joue (la fonction print), et récupère le coup du joueur (fonction play que nous verrons également après). Elle est positionnée dans une boucle pour redemander au joueur son jeu s'il n’est pas valide (case déjà prise ou n’appartenant pas au tableau). Une fois ce processus terminé, elle affiche le gagnant, ou match nul si personne ne gagne.

Continuons avec la fonction show, elle se charge de parcourir le tableau pour l’afficher avec le numéro des lignes et des colonnes.

Puis la fonction play, vérifie la validité du coup (case libre dans les limites du tableau) et l'applique.

Vient ensuite la fonction win, qui vérifie tout le tableau dans des boucles pour savoir si un joueur a gagné ou non. Elle est couplé avec les fonctions line, col et dia qui vérifient chacune une ligne, une colonne ou une diagonale, pour simplifier le code et éviter les répétitions.

Pour terminer la fonction full qui permet de vérifier si le tableau est plein ou pas (pour les matchs nuls).

Passons ensuite au fichier player.py. Celui ci est très simple, il définit la structure de base d’un joueur, c’est à dire le signe (X ou O), et une fonction play pour lui permettre de jouer.

Il en découle donc le fichier human.py, l’implémentation de player.py. Il vient redéfinir la fonction play de player.py, en récupérant le jeu du joueur via le clavier.

Et pour finir vient le fichier main.py qui sera le fichier qui vient lancer le morpion. Il demande au joueur de choisir une configuration de jeu (qui joue contre qui), initialise l’objet game, et appelle la fonction start.

Maintenant passons à la partie intelligence artificielle de l’ordinateur, qui sera capable de “réfléchir” afin de sortir vainqueur à chaque partie, ou du moins forcer un match nul dans le cas ou il ne sera pas possible pour lui de gagner.

### Intégration de l’intelligence artificielle dans le morpion

#### Trouver une stratégie

La meilleur stratégie consiste à récupérer toutes les possibilités de jeu et les analyser une par une. Pour cela, notre intelligence artificielle va faire un arbre de possibilités. Cet arbre aura pour nombre de branches la factorielle du nombre de cases libres. Par exemple, pour 8 cases, ce qui est le cas de notre morpion, l’arbre a environ 8!, soit à peu près 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1, donc environ 40 320 branches (sachant qu'à certains moments une victoire entraine la fin d'une branche). Chaque extrémité de branche correspond une partie terminée, à laquelle sera attribué un score. Ce score sera de -1 si l’adversaire gagne, 0 si il y a match nul, et 1 si l’intelligence artificielle gagne. Elle sélectionnera dans cette arbre la branche qui a le meilleur score.

Prenons cet exemple pour expliquer comment cette arbre se constitue. Dans cette partie, c’est au tour de l’intelligence artificielle de jouer, avec une croix. Il y a 3 cases de libres, et donc 3!, c’est à dire 3 x 2 x 1, vous êtes bon en maths, ça fait 6 possibilités à calculer.

Nous allons donc commencer par la case en haut à droite. Si notre intelligence artificielle joue dans cette case, l'ennemi a deux autres possibilités de jeu, composées d'un match nul et d'une victoire de notre intelligence artificielle. Comme l'ennemi peut choisir la possibilité du match nul, c'est le score 0 qui est associé à cette première branche.

Passons ensuite à la case du milieu à droite. Si elle y joue, elle gagne instantanément. C’est donc le score 1 qui sera associé à cette seconde branche.

Pour finir, si elle joue dans la case en bas à droite, l’ennemie pourra ensuite jouer dans la case en haut à droite et gagner. Le score -1 sera donc associé à cette branche.

Une fois le score établit pour chaque case, l’intelligence artificielle prendra celle avec le meilleur score et joue à cette endroit là.

Il nous reste donc à transformer cette idée de stratégie en un code fonctionnel.

#### Implémenter cette stratégie dans l’intelligence artificielle

Nous allons créer un fichier computer.py dans lequel nous allons faire une implémentation de player.py avec cette stratégie, pour permettre à l’intelligence artificielle de jouer et de gagner (ou de faire un match nul quand il n’est pas possible de gagner).

Pour commencer, nous allons redéfinir la fonction play, qui va permettre de transmettre le jeu de notre intelligence artificielle à la partie. Cette fonction va appeler une autre fonction bestMove. La fonction bestMove définit deux variables, le signe de l’ennemie et une liste de coups avec un score associés (score que nous évoquions dans notre stratégie). Ensuite, elle parcourt le tableau de jeu, et pour chaque case disponible, fait une copie du tableau dans laquelle elle va jouer et regarder le résultat. Si c’est un match nul, elle note ce coup avec le score 0, si c’est une victoire immédiate, elle le note 1, sinon elle approfondit le processus pour le coup suivant pour anticiper si le joueur ennemie pourrait gagner ensuite (et donc éviter ce cas). Une fois cette liste de coups avec leur score associé faite, elle sélectionne le coup qui a le meilleur score.

Il nous reste à rajouter dans le fichier main.py les configurations qui permettent de jouer contre notre intelligence artificielle, et elle est prête !

### Conclusion

Pour créer notre intelligence artificielle, nous avons d'abord créé un algorithme grâce à plusieurs fichiers écrit avec le language python, permettant d'écrir le jeu en lui même. Enfin, nous avons imaginé notre stratégie à l'aide de l'étude de statistiques, que nous avons ensuite mis en place dans notre algorihme dans un autre fichier python.

Comme notre intelligence artificielle est plus forte qu'un humain sur le jeu du morpion, nous pourrions nous demander si, dans le futur, l'intelligence artificielle pourra remplacer l'humanité.

### Démonstration

Donc nous allons jouer une partie contre notre intelligence artificielle, donc nous sélectionnons la configuration 2. Nous allons jouer au milieu, donc en rentrant 2, 2. On voit qu'elle joue dans le coin. Ensuite nous allons jouer dans la case du milieu à gauche, pour faire comme si on commençait une ligne, sur la ligne du milieu. On voit qu'elle joue à droite pour nous bloquer. Nous allons donc la bloquer en haut à droite, pour éviter qu'elle puisse gagner. A ce moment là, on voit qu'elle joue en bas à gauche, pour nous bloquer, mais elle a la possibilité de gagner. Donc nous on va essayer également de la bloquer, on ne va pas la laisser faire. Et donc là, il nous reste plus que la possibilité de faire un match nul, donc on termine sur un match nul.

## Synthèse personnelle

Au commencement, il fallut trouver un sujet d’étude. Comme nous ne nous connaissions pas, il fallut se concerter pour choisir un sujet nous contentant l’un, l’autre. Mais avant même de nous demander quel sera le sujet, la première chose à laquelle nous avons pensé est le format de notre production. Comme Nathan aime produire de la vidéo et s’y connait pas mal, nous avons sélectionné ce format. Nous sommes donc ensuite passé au sujet du TPE. La téléportation rencontra un certain succès, mais, en absence de TP concret, ce sujet ne fut pas retenu. Qu’importe. Durant quelques minutes nous crurent avoir trouvé le sujet idéal : l’eugénisme. Mais après quelque recherches sur le web nous nous sommes rendus compte que le sujet était trop sensible et que quelques scientifiques germaniques, bien que compétent, n’ont pu qu’effleurer l’idée de le mettre en application. Enfin, Nathan proposa un TPE sur l’intelligence artificielle. Raoul n’y voyait pas d’inconvénients, comme Nathan savait programmer avec précision. L’idée fut validée.

Après avoir déterminé le sujet, il fallait imaginer un moyen de l’illustrer. Avec un robot, si oui, quelles actions pourrait-il faire ? Très peu avec nos connaissances, et le materiel dont nous disposions. Ensuite est venu l’idée de faire une intelligence artificielle capable de reconnaitre dans quelle langue est écrite une phrase. Mais cette idée n’était pas assez convaincante, et peu pertinente. Ensuite nous avons pensé aux intelligences artificielles présentes dans les jeux vidéos, et en particulier dans le jeu du Morpion. Une intelligence artificielle capable de jouer contre nous au Morpion était une idée pertinente, et possible à réaliser à notre niveau (contrairement à d’autres jeux comme les échecs qui sont bien trop complexes pour être pris comme cas dans notre TPE). Nous avons donc choisi comme TP cette intelligence artificielle jouant au Morpion.

Il nous fallait ensuite déterminer la problématique. D’abord, nous avions pensé à “Qu’est ce que l’intelligence artificielle et quelles sont ses applications ?”. Cette problématique étant assez vague, nous avions commencé à entreprendre des recherches sur ce qu’est l’intelligence artificielle et en faire un historique. Mais nous nous sommes rendu compte, après plusieurs séances de recherches, que ce que nous faisions ne correspondait pas à la logique des TPE, mais plutôt à un exposé. Nous avons donc mis au centre notre TP, notre intelligence artificielle jouant au Morpion, et avons cherché une problématique en lien avec celui ci. Nous avons donc choisi : “En quoi notre Morpion est-il une intelligence artificielle ?”.

Pour déterminer le plan de notre TPE, nous nous sommes demandés comment allait être constitué notre Morpion. Nous avons donc trouvé deux parties : un algorithme, la partie programmation faisant tourner le jeu et l’intelligence artificielle, et les statistiques, permettant à notre algorithme d’étudier les cas de jeu et de devenir “intelligent”. Nous avions donc notre plan : l’algorithme et la logique statistique. Nous avons donc fait une vidéo reprenant ces deux partie, en expliquant la conception de notre intelligence artificielle.

Au niveau des sources, après quelque recherche sur Google, la page de Wikipédia sur l’intelligence artificielle nous a aidé à trouver une définition de ce qu’est une intelligence artificielle. C’est à peu près tout ce que nous avons trouvé d’utile sur le web pour notre TPE, le reste étant “fait-maison” par nos soins.

Nous sommes donc ensuite passés à la recherche de la stratégie de notre intelligence artificielle. Nous avions pour but de créer une intelligence artificielle imbattable à ce jeu. Cette stratégie est en fait la logique statistique permettant d’analyser les possibilités de jeu afin de gagner. Une fois cette stratégie élaborée jusqu’au moindre détail, nous sommes passés à la partie programmation. Nous avons hésité longuement sur le language avec lequel nous allions procéder, entre le Java, le Swift et le Python. Nos professeurs, étant plus adeptes au Python, nous ont conseillé le Python, que nous avons donc choisi. Nous avons donc ouvert notre joli éditeur de code, et nous avons commencé à faire quelques tests, et à écrire au fur et à mesure le cœur de notre intelligence artificielle. Après plusieurs séances de programmation et de déboggage, nous avions enfin notre petit prototype fonctionnel de Morpion imbattable.

Une fois notre intelligence artificielle terminée, il nous fallait passer à la réalisation de notre vidéo. La première étape était l’écriture du script. Nous avons repris notre plan, et nous avons expliqué chaque étape de la création du Morpion et de son intelligence artificielle. Ensuite, nous somme passés au tournage, puis au montage pendant quelques séances. Après quoi notre production finale, la vidéo, était terminée. Nous avions donc une vidéo divisée selon notre plan, qui expliquait comment nous avions procédé pour créer notre Morpion de A à Z.

Les TPE ont donc été une expérience intéressante. En effet, nous avons découvert plus précisément comment fonctionnait une intelligence artificielle, et avons pris quelques notions sur la programmation.
