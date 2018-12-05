# MorpionTPE, une intelligence artificielle imbattable au morpion

## Description du package

### MorpionPy/

Version Python du Morpion avec son IA

- main.py : Fichier principal, qui lance la partie
- game.py : Class qui gère le déroulement de la partie
- player.py : Class qui gère le jeu des participants
- human.py : Class qui gère le jeu de l'humain
- computer.py : Class qui gère le jeu de l'IA

## Version d'essai en ligne

[Interpréteur Python en ligne](https://repl.it/@NathanFallet/MorpionTPE)

## Récupérer la dernière version avec le système GitHub

### Cloner le dépot :

```
cd ~/
git clone https://github.com/NathanFallet/MorpionTPE
```

Cela va créer un dossier MorpionTPE/ dans le dossier actuel, dans lequel se trouve les dossiers visibles ici.

### Obtenir les mises à jours :

```
cd ~/MorpionTPE
git pull
```

Cette commande va automatiquement mettre à jour le dossier.

## Script de la vidéo

### Introduction

L'intelligence artificielle se fonde sur l'hypothèse que le processus de pensée humaine peut être mécanisé. Cela commence dès l’antiquité mais prend une toute autre dimension avec l’arrivé des composants électroniques.

Notre intelligence artificielle sera composée d’un algorithme, c’est à dire une suite d’instructions qui seront exécutées les unes après les autres, et d’une logique statistique, qui va étudier les cas possibles de jeu afin de gagner à chaque partie.

Nous allons, dans un premier temps, construire le morpion en lui même, et ensuite y intégrer notre intelligence artificielle contre laquelle on pourra jouer.

### Construction du morpion

Le morpion est un jeu de réflexion se pratiquant à deux joueurs au tour par tour dont le but est de créer en premier un alignement de trois signes (des ronds et des croix). Il tire son origine de l’Égypte Antique où ont été retrouvées des parties datant d’environ 1300 av. J.C.

Nous allons, grâce au langage Python, créer l’algorithme du morpion en lui même. Il sera composé de plusieurs fichiers :
- game.py, qui se charge du déroulement général de la partie,
- player.py, qui correspond aux données basiques de tout joueur (signe, fonction qui permet de récupérer son jeu),
- human.py, qui est une implémentation de player.py, c’est à dire qu’il sera basé sur ce fichier en y ajoutant des fonctionnalités,
- Et main.py, qui vient mettre tout ça ensemble et lancer la partie.

Commençons par game.py. Sa première fonction est la fonction d’initialisation de l’objet. Elle crée un tableau de jeu et enregistre les joueurs données par le fichier main.py que nous verrons plus loin.

Ensuite, vient la fonction start : elle démarre la partie et gère son déroulement. Une boucle fait jouer chaque joueur chacun leur tour jusqu’à ce qu’il y aie un gagnant ou un match nul (instruction while et for). A chaque tour elle affiche le tableau de jeu actuel (fonction show, que nous verrons après), le joueur qui joue (fonction print), et récupère le coup du joueur (fonction play que nous verrons aussi après). Elle est positionnée dans une boucle pour redemander au joueur son jeu s'il n’est pas valide (case déjà prise ou n’appartenant pas au tableau. Une fois ce processus terminé, elle affiche le gagnant, ou match nul si personne ne gagne.

Continuons avec la fonction show, elle se charge de parcourir le tableau pour l’afficher avec le numéro des lignes et des colonnes.

La fonction play, qui vérifie la validité du jeu (case libre dans les limites du tableau) et applique le jeu.

Vient ensuite la fonction win, qui vérifie tout le tableau dans des boucles pour savoir si un joueur à gagner ou non. Elle est couplé avec les fonctions line, col et dia qui vérifie chacune une ligne, une colonne ou une diagonale, pour simplifier le code et éviter les répétitions.

Pour terminer la fonction full qui permet de vérifier si le tableau est plein ou pas (pour les matchs nuls).

Passons ensuite au fichier player.py. Celui ci est très simple, il définit la structure de base d’un joueur, c’est à dire un signe (X ou O), et une fonction play pour lui permettre de jouer.

Il en découle donc le fichier human.py, l’implémentation de player.py. Il vient redéfinir la fonction play de player.py, en récupérant le jeu du joueur via le clavier.

Et pour finir vient le fichier main.py qui sera le fichier qui vient lancer le morpion. Il demande au joueur de choisir une configuration de jeu (qui joue contre qui), initialise l’objet game, et appel la fonction start.

Maintenant passons à la partie intelligence artificielle de l’ordinateur, qui sera capable de “réfléchir” afin de sortir vainqueur à chaque partie, ou du moins forcer un match nul dans le cas ou il ne sera pas possible pour lui de gagner.

### Intégration de l’intelligence artificielle dans le morpion

#### Trouver une stratégie

La meilleur stratégie consiste à récupérer toutes les possibilités de jeu, les analyser une par une. Pour cela, notre intelligence artificielle va faire un arbre de possibilités. Cet arbre aura pour nombre de branches la factorielle du nombre de cases libres. Par exemple, pour 8 cases de libres, l’arbre aura environ 8! branches, soit 8 x 7 x 6 x 5 x 4  x 3 x 2 x 1, donc 40 320 branches (sachant qu'à certains moments une victoire entraine la fin d'une branche). Chaque extrémité de branche correspondra une partie terminée, à laquelle sera attribué un score. Ce score sera -1 si l’adversaire gagne, 0 si il y a match nul, ou 1 si l’intelligence artificielle gagne. Elle sélectionnera dans cette arbre la branche qui a le meilleur score.

Prenons cet exemple pour expliquer comment cette arbre se constitue. Dans cette partie, c’est au tour de l’intelligence artificielle de jouer, avec une croix. Il y a 3 cases de libres, donc 3!, c’est à dire 3 x 2 x 1 donc environ 6 possibilités à calculer.

Nous allons donc commencer par la case en haut à droite. Si notre intelligence artificielle joue dans cette case, l'ennemi a deux autres possibilités de jeu, composées d'un match nul et d'une victoire de notre intelligence artificielle. Mais comme l'ennemi peut choisir la possibilité du match nul, c'est le score 0 qui est associé à cette première branche.

Passons ensuite à la case du milieu à droite. Si elle y joue, elle gagne instantanément. C’est donc le score 1 qui est associé à cette seconde branche.

Pour finir, si elle joue dans la case en bas à droite, l’ennemie peut ensuite jouer dans la case en haut à droite et gagner. Le score -1 est donc associé à cette branche.

Une fois le score établit pour chaque case, l’intelligence artificielle prend celle avec le meilleur score et joue à cette endroit là.

Il nous reste donc à transformer cette idée de stratégie en un code fonctionnel.

#### Implémenter cette stratégie dans l’intelligence artificielle

Nous allons créer un fichier computer.py dans lequel nous allons faire une implémentation de player.py avec cette stratégie, pour permettre à l’intelligence artificielle de jouer et de gagner (ou de faire un match nul quand il n’est pas possible de gagner).

Pour commencer, nous allons redéfinir la fonction play, qui va permettre de transmettre le jeu de notre intelligence artificielle à la partie. Cette fonction va appeler une autre fonction bestMove. La fonction bestMove définit deux variables, le signe de l’ennemie et une liste de coups avec un score associés (score que nous évoquions dans notre stratégie). Ensuite, elle parcourt le tableau de jeu, et pour chaque case disponible, fait une copie du tableau dans laquelle elle va jouer et regarder le résultat. Si c’est un match nul, elle note ce coup avec le score 0, si c’est une victoire immédiate, elle le note 1, sinon elle approfondit le processus pour le coup suivant pour anticiper si le joueur ennemie pourrait gagner ensuite (et donc éviter ce cas). Une fois cette liste de coups avec leur score associé faite, elle sélectionne le coup qui a le meilleur score.

Il nous reste à rajouter dans le fichier main.py les configurations qui permettent de jouer contre notre intelligence artificielle, et elle est prête !

### Conclusion

Pour créer notre intelligence artificielle, nous avons d'abord créé un algorithme grâce à plusieurs fichiers écrit avec le language python, permettant le jeu du morpion en lui même. Enfin, nous avons imaginer notre stratégie à l'aide de l'étude de statistiques, que nous avons ensuite mis en place dans notre algorihme dans un autre fichier python.

Comme notre intelligence artificielle est plus forte qu'un humain sur le jeu du morpion, nous pourrions nous demander si, dans le futur, l'intelligence artificielle pourrait remplacer l'humanité.
