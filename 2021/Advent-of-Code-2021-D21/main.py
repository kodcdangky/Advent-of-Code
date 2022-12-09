# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from DiracDice import *


def play1(txt):
    with open(txt) as file:
        p1 = Player(int(file.readline()[-2]))
        p2 = Player(int(file.readline()[-2]))
    game = Dirac()

    while True:
        p1.move(game.die * 3 + 3)
        game.go()
        p1.score += p1.location
        if p1.score >= 1000:
            return p2.score * game.roll

        p2.move(game.die * 3 + 3)
        game.go()
        p2.score += p2.location
        if p2.score >= 1000:
            return p1.score * game.roll


def play2(txt):
    with open(txt) as file:
        p1 = int(file.readline()[-2])
        p2 = int(file.readline()[-2])
    game_state = {}

    def dr_strange(p0, s0, p1, s1):
        if s0 >= 21:
            return 1, 0
        if s1 >= 21:
            return 0, 1
        if (p0, s0, p1, s1) in game_state:
            return game_state[(p0, s0, p1, s1)]
        this_state_outcome = (0, 0)
        for roll0 in [1, 2, 3]:
            for roll1 in [1, 2, 3]:
                for roll2 in [1, 2, 3]:
                    new_p0 = (p0 + roll0 + roll1 + roll2 - 1) % 10 + 1
                    new_s0 = s0 + new_p0

                    outcome1, outcome0 = dr_strange(p1, s1, new_p0, new_s0)
                    this_state_outcome = (this_state_outcome[0] + outcome0, this_state_outcome[1] + outcome1)
        game_state[(p0, s0, p1, s1)] = this_state_outcome
        return this_state_outcome
    return max(dr_strange(p1, 0, p2, 0))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(play2('input.txt'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
