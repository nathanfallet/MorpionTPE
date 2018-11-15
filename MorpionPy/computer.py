# Import des bibliotheques necessaires au programme
from player import *
from copy import deepcopy
from random import randint

# Class Computer - Implementation de Player pour l'ordinateur
class Computer(Player):

    # TODO: Corriger le bug de la boucle infinie (ecriture dans le mauvais tableau)
    def play(self, game):
        other = ("X" if self.sign == "O" else "O")
        for x in range(game.size):
            for y in range(game.size):
                if game.table[x][y] == "*":
                    copy = deepcopy(game.table)
                    copy[x][y] = self.sign
                    if game.win(copy) == self.sign:
                        return (x, y)
                    copy[x][y] = other
                    if game.win(copy) == other:
                        return (x, y)
        return (randint(0, game.size-1), randint(0, game.size-1))

    
