import Tile

class Board(object):
    """A board of tiles"""
    def __init__(self):
        self._board = [[]]
        self._boardCopy = [[]]
        counter = 0
        for i in range(0, 10):
            self._board.append([])
            self._boardCopy.append([])
            for j in range(0, 10):
                counter += 1
                self._board[i].append(Tile.Tile(counter).setBlank)
                self._boardCopy[i].append(Tile.Tile(counter).setBlank)
    def __str__(self):
        rep = ""
        for i in range(0, 10):
            for j in range(0, 10):
                if self._board[i][j].hasCPU == False and self._board[i][j].hasPlayer == False:  
                    if self._board[i][j].getNr() < 10 and self._board[i][j].getNr() != 1:
                        rep += "<" + "0" + str(self._board[i][j].getNr()) + ">"
                    elif self._board[i][j].getNr() == 1:
                        rep += "THUG"
                    elif self._board[i][j].getNr() == 100:
                        rep += "BOSS"
                    else: rep +="<" + str(self._board[i][j].getNr()) + ">"
                elif self._board[i][j].hasCPU == True and self._board[i][j].hasPlayer == True:
                    rep += "<PC>"
                elif self._board[i][j].hasPlayer == True:
                    rep += "<P->"
                elif self._board[i][j].hasCPU == True:
                    rep += "<0C>"
            rep += "\n"
        return rep
    def getTile(self, row, col):
        return self._board[row][col].getNr()
    def setTile(self, row, col, nr):
        self._board[row][col] = nr

    def Move(self, player):
        px = player.getX
        py = player.getY
        self._board[py][px].setPlayer()
