#!/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python

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
    size = int(input("Choisissez une taille (entre 3 et 6): "))

# Deroulement du jeu
game = Game(size)
players = [Human("X"), Computer("O")]
win = "*"

while win == "*":
    game.show()
    for player in players:
        x = y = -1
        while not game.play(x, y, player.sign):
            (x, y) = player.play(game)
        print(player.sign+" joue en "+str(x+1)+", "+str(y+1))
    win = game.win(game.table)

print("A gagne le joueur "+win)
