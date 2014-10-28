from random import randint

class Spinner:
    def __init__(self):
        self._value = 0
    def __str__(self):
        rep = "<{}>".format(self._value)
        return rep
    def spin(self):
        self._value = randint(1, 6)
        return self._value