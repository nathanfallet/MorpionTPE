# Class Game - Gestion du tableau de jeu
class Game:

    # Initialisation du tableau de jeu
    def __init__(self, size, player1, player2):
        self.size = size
        self.table = [["*" for x in range(size)] for y in range(size)]
        self.player1 = player1
        self.player2 = player2

    # Deroulement de la partie
    def start(self):
        win = "*"
        while win == "*" and not self.full(self.table):
            for player in [self.player1, self.player2]:
                if not self.full(self.table) and win == "*":
                    self.show()
                    print("Au tour de "+player.sign+" de jouer !")
                    x = y = -1
                    while not self.play(x, y, player.sign):
                        (x, y) = player.play(self)
                    print(player.sign+" joue ligne "+str(y+1)+", colonne "+str(x+1))
                    win = self.win(self.table)
        self.show()
        if win == "*":
            print("Match nul !")
            return
        print(win+" remporte la partie !")

    # Affichage du tableau
    def show(self):
        print("")
        line = "  "
        for x in range(self.size):
            line += str(x+1)+" "
        print(line)
        for y in range(self.size):
            line = str(y+1)+" "
            for x in range(self.size):
                line += self.table[x][y]+" "
            print(line)
        print("")

    # Change la valeur d'une case si libre
    def play(self, x, y, player):
        if x >= 0 and x < self.size and y >= 0 and y < self.size and self.table[x][y] == "*":
            self.table[x][y] = player
            return True
        return False

    # Regarde si un joueur a gagne
    def win(self, table):
        for i in range(self.size):
            line = self.line(table, i)
            if line != "*":
                return line
            col = self.col(table, i)
            if col != "*":
                return col
        for i in range(2):
            dia = self.dia(table, i)
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
    def dia(self, table, d):
        i = (0 if d == 0 else self.size-1)
        player = table[i][0]
        changed = False
        for x in range(self.size):
            i = (x if d == 0 else self.size-1-x)
            if table[i][x] != player:
                changed = True
        if changed:
            return "*"
        return player

    def full(self, table):
        for x in range(self.size):
            for y in range(self.size):
                if table[x][y] == "*":
                    return False
        return True
