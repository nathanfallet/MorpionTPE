# Import des bibliotheques necessaires au programme
from player import *

# Class Computer - Implementation de Player pour l'ordinateur
class Computer(Player):

    # TODO: Corriger le bug de la boucle infinie (ecriture dans le mauvais tableau)
    def play(self, game):
        print("Play for computer")
        for x in range(game.size):
            for y in range(game.size):
                print("Test for "+str(x)+", "+str(y))
                if game.table[x][y] == "*":
                    copy = list(game.table)
                    copy[x][y] = self.sign
                    if game.win(copy) == self.sign:
                        return (x, y)
        return (0, 0)
