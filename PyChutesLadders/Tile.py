class Tile(object):
    """A GAME TILE"""
    def __init__(self, nr):
        self._nr = nr
        self._hasPlayer = False
        self._hasCPU = False

    def __str__(self):
        if self._nr in range(0, 10):
            rep = "<0{}>".format(self._nr)
        else:
            rep = "<{}>".format(self._nr)

    def getNr(self):
        return self._nr

    def setPlayer(self):
        self._hasPlayer = True
    def setCPU(self):
        self._hasCPU = True
    def setBlank(self):
        self._hasCPU = False
        self._hasPlayer = False

    @property
    def hasPlayer(self):
        return self._hasPlayer
    @property
    def hasCPU(self):
        return self._hasCPU