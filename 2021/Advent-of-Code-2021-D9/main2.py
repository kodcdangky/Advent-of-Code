# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy

def basin(txt):
    global table
    global size
    table = [[0] * 102 for i in range(102)]
    table = init(txt, table)
    area1 = 0
    area2 = 0
    area3 = 0

    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            size = 0
            if table[i][j] == 1:
                basin_size(i, j)
                m = min(area1, area2, area3)
                if size > m:
                    if m == area1: area1 = size
                    elif m == area2: area2 = size
                    elif m == area3: area3 = size
    return area1 * area2 * area3

def basin_size(i, j):
    global table
    global size
    if table[i][j] == 0:
        return
    size += 1
    table[i][j] = 0

    basin_size(i + 1, j)
    basin_size(i - 1, j)
    basin_size(i, j + 1)
    basin_size(i, j - 1)

def init(txt, table):
    file = open(txt)
    row = 0
    for line in file:
        line = line[:-1]
        row += 1
        for i in range(1, len(line) + 1):
            if int(line[i-1]) != 9:
                table[row][i] = 1
    file.close()
    return table

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(basin("input.txt"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
