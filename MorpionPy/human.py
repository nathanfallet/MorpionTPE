# Import des bibliotheques necessaires au programme
from player import *

# Class Human - Implementation de Player pour le joueur
class Human(Player):

    def play(self, game):
        y = int(input("Entrer le numero de la ligne (1 a "+str(game.size)+") : "))
        x = int(input("Entrer le numero de la colonne (1 a "+str(game.size)+") : "))
        return (x-1, y-1)
