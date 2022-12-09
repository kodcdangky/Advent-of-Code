# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def contest(txt):
    file = open(txt)
    score = 0
    counterpart = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    for line in file:
        line = line[:-1]
        expect = []
        for c in line:
            if c == "(" or c == "[" or c == "{" or c == "<":
                expect.append(counterpart.get(c))
            elif c != expect[-1]:
                score += counterpart.get(c)
                break
            else:
                expect.pop(-1)
    return score

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(contest("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
