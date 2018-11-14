# Class Game - Gestion du tableau de jeu

class Game:

    # Initialisation du tableau de jeu
    def __init__(self, size):
        self.size = size
        self.table = [["*" for x in range(size)] for y in range(size)]

    # Affichage du tableau
    def show(self):
        line = "  "
        for x in range(self.size):
            line += str(x+1)
        print(line)
        for y in range(self.size):
            line = str(y+1)+" "
            for x in range(self.size):
                line += self.table[x][y]
            print(line)

    # Change la valeur d'une case si libre
    def play(self, x, y, player):
        if(self.table[x][y] == "*"):
            self.table[x][y] = player
            return True
        return False

    # Regarde si un joueur a gagne
    def win(self):
        for i in range(self.size):
            line = self.line(self.table, i)
            if line != "*":
                return line
            col = self.col(self.table, i)
            if col != "*":
                return col
        for i in range(2):
            dia = self.dia(self.table, i)
            if dia != "*":
                return dia
        return "*"

    # Verifie une ligne
    def line(self, table, y):
        player = table[0][y]
        changed = False
        for x in range(self.size):
            if table[x][y] != player:
                changed = True
        if changed:
            return "*"
        return player

    # Verifie une colonne
    def col(self, table, x):
        player = table[x][0]
        changed = False
        for y in range(self.size):
            if table[x][y] != player:
                changed = True
        if changed:
            return "*"
        return player

    # Verifie une diagonale
    # TODO: deuxième diagonale
    def dia(self, table, d):
        player = table[0][0]
        changed = False
        for x in range(self.size):
            if table[x][x] != player:
                changed = True
        if changed:
            return "*"
        return player
