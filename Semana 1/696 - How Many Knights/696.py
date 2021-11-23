from pilha import Pilha

#value if a tile is safe
safe = 0
#value if a tile has a knight on it
knight = 1
#value if a tile can be attacked by a knight
danger = 2

class Board:
    tiles = []
    
    def __init__(self, Rows, Columns):
        self.Rows = Rows
        self.Columns = Columns
        self.startTiles()
    
    def startTiles(self):
        for i in range(self.Rows):
            aux = []
            for j in range(Columns):
                aux.append(0)
            self.tiles.append(aux)
            
    def showBoard(self):
        print(self.tiles)

    def fillDangerTiles(self, row, column):
        if(row + 2 > self.Rows)

Rows, Columns = input().split(" ")

Rows = int(Rows)
Columns = int(Columns)

board = Board(Rows, Columns)

board.showBoard()


