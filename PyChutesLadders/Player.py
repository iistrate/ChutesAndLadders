class Player(object):
    PLAYER_TYPES = dict(PLAYER1 = 1, ENEMY = 2)
    """Player, Enemy common class"""
    def __init__(self, type):
        self._type = type
        self._x = 0
        self._y = 0
        self._oldX = 0
        self._oldY = 0

    def __rep__(self):
        if self._type == PLAYER_TYPES['ENEMY']:
            rep = "A"
        else:
            rep = "P"
        return rep

    def setX(self, x):
        self._x = x
    def setY(self, y):
        self._y = y
    def setType(self, t):
        self._type = t
    def setPosition(self, p):
        if self.getX + p < 10:
            self._x += p
        else:
            self._x = ((self._x + p)  % 10)
            self._y += 1

    
    @property
    def getX(self):
        return self._x
    @property
    def getY(self):
        return self._y
    @property
    def getOldX(self):
        return self._oldX
    @property
    def getOldY(self):
        return self._oldY
    @property
    def getType(self):
        return self._type