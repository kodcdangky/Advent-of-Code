# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def risk(txt):
    table = [[10] * 102 for i in range(102)]
    table = init(txt, table)
    level = 0
    for i in range(1, 101):
        for j in range(1, 101):
            level += low(table, i, j) + 1
    return level

def init(txt, table):
    file = open(txt)
    row = 0
    for line in file:
        line = line[:-1]
        row += 1
        for i in range(1, len(line) + 1):
            table[row][i] = int(line[i-1])
    file.close()
    return table

def low(table, x, y):
    if ltu(table, x, y) and ltd(table, x, y) and ltl(table, x, y) and ltr(table, x, y):
        return table[x][y]
    return -1

def ltu(table, x, y):
    if table[x][y] < table[x-1][y]: return True
    return False

def ltd(table, x, y):
    if table[x][y] < table[x+1][y]: return True
    return False

def ltl(table, x, y):
    if table[x][y] < table[x][y-1]: return True
    return False

def ltr(table, x, y):
    if table[x][y] < table[x][y+1]: return True
    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(risk("input.txt"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
