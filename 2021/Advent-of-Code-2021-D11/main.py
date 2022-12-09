# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Part 1: total flashes after 100 steps
# Part 2: step where all flashes

import datetime


def flashes(txt):
    global flash_count
    table = [[0] * 12 for i in range(12)]

    table = init(txt, table)
    flash_count = 0
    step = 0
    while check(table) != True:
        table = turn(table)
        step += 1
    return step

# Part 2
def check(table):
    for i in range(1, 11):
        for j in range(1, 11):
            if table[i][j] != 0:
                return False
    return True

def turn(table):
    global flash_count
    mark = [[0] * 12 for i in range(12)]

    for i in range(1, 11):
        for j in range(1, 11):
            table[i][j] += 1

    flashed = True
    while flashed == True:
        flashed = False
        for i in range(1, 11):
            for j in range(1, 11):
                if table[i][j] > 9 and mark[i][j] == 0:
                    flashed = True
                    mark[i][j] = 1
                    table[i - 1][j] += 1
                    table[i - 1][j + 1] += 1
                    table[i][j + 1] += 1
                    table[i + 1][j + 1] += 1
                    table[i + 1][j] += 1
                    table[i + 1][j - 1] += 1
                    table[i][j - 1] += 1
                    table[i - 1][j - 1] += 1

    for i in range(1, 11):
        for j in range(1, 11):
            if table[i][j] > 9:
                flash_count += 1
                table[i][j] = 0

    return table

def init(txt, table):
    file = open(txt)
    row = 1
    for line in file:
        line = line[:-1]
        for i in range(1, 11):
            table[row][i] = int(line[i-1])
        row += 1
    file.close()
    return table

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    duration = datetime.datetime.now().timestamp()
    print(flashes("input.txt"))
    print(datetime.datetime.now().timestamp() - duration)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
