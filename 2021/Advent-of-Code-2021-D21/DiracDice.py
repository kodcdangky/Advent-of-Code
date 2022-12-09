class Player:

    def __init__(self, location):
        self.location = location
        self.score = 0

    def move(self, step):
        self.location += step % 10
        if self.location > 10:
            self.location %= 10


class Dirac:

    def __init__(self):
        self.roll = 0
        self.die = 1

    def go(self):
        self.roll += 3
        self.die += 3
        if self.die > 100:
            self.die %= 100
