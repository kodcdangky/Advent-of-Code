# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def contest(txt):
    file = open(txt)
    scoreboard = []
    counterpart = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    for line in file:
        line = line[:-1]
        expect = []
        corr = False
        score = 0
        for c in line:
            if c == "(" or c == "[" or c == "{" or c == "<":
                expect.append(counterpart.get(c))
            elif c != expect[-1]:
                corr = True
                break
            else:
                expect.pop()
        if corr == True: continue
        while len(expect) > 0:
            score = score * 5 + counterpart.get(expect.pop())
        scoreboard.append(score)
    scoreboard.sort()
    score = scoreboard[len(scoreboard)//2]
    return score

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(contest("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
