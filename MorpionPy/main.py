#!/usr/local/bin/python3

# Jeu du morpion
# Le joueur commence a jouer en premier, l'ordinateur joue ensuite

# Import des bibliotheques necessaires au programme
from game import *
from player import *
from human import *
from computer import *

# Choix de la taille de la grille
size = 0
while size < 3 or size > 6:
    size = int(input("Choisissez une taille (entre 3 et 6) : "))

# Choix de la configuration
print("\n1 - Joueur contre joueur\n2 - Joueur contre ordinateur\n3 - Ordinateur contre joueur\n4 - Ordinateur contre ordinateur\n")
config = 0
while config < 1 or config > 4:
    config = int(input("Choisissez une configuration : "))

if config == 1:
    Game(size, Human("X"), Human("O")).start()
elif config == 2:
    Game(size, Human("X"), Computer("O")).start()
elif config == 3:
    Game(size, Computer("X"), Human("O")).start()
else:
    Game(size, Computer("X"), Computer("O")).start()
