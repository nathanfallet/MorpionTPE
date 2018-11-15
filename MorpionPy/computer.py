# Import des bibliotheques necessaires au programme
from player import *
from copy import *
from random import *

# Class Computer - Implementation de Player pour l'ordinateur
class Computer(Player):

    def play(self, game):
        return self.bestMove(game, game.table, game.size, self.sign)[0]

    # Selectionner la meilleure possibilitee de jeu
    def bestMove(self, game, table, size, sign):
        # On recupere le sign de l'adverse pour nos calculs
        other = ("X" if sign == "O" else "O")
        # On cree une liste vide pour y ajouter nos possibilitees avec leur score
        moves = list()

        # On parcours le tableau pour classer chaque possibilitee
        for x in range(size):
            for y in range(size):
                # Si la case est disponible
                if table[x][y] == "*":
                    # On fait une copie du tableau dans laquelle on joue
                    copy = deepcopy(table)
                    copy[x][y] = sign
                    # Et on recupere le resultat
                    win = game.win(copy)

                    # Si le tableau est plein et que personne ne gagne, on le grade 0
                    if win == "*" and game.full(copy):
                        score = 0
                    # Si il permet de gagner, on le grade 1
                    elif win == sign:
                        score = 1
                    # Sinon, on le grade avec l'oppose du score pour le joueur adverse
                    # pour son meilleur coup dans son jeu suivant
                    else:
                        score = 0 - self.bestMove(game, copy, size, other)[1]
                    result = ((x, y), score)

                    # Si le score est 1, on joue ce coup
                    if score == 1:
                        return result
                    # Sinon on l'ajout dans la liste avec les autres et on continue
                    moves.append(result)

        # Une fois tous les coups dans la liste, on les trie par score
        shuffle(moves)
        moves.sort(key=lambda move: move[1], reverse=True)
        # Et on joue le meilleur
        return moves[0]
