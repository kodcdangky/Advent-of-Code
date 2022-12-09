# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


def count(txt):
    # initializing paper's initial state and folding guide
    file = open(txt)

    guide = []
    global edgeX; edgeX = 0
    global edgeY; edgeY = 0

    for line in file:
        line = line[:-1]
        if line == "": break
        line = line.split(",")
        if edgeX < int(line[0]): edgeX = int(line[0])
        if edgeY < int(line[1]): edgeY = int(line[1])
    edgeX += 1
    edgeY += 1

    paper = [[0 for i in range(edgeX)] for i in range(edgeY)]
    file.seek(0)
    for line in file:
        line = line[:-1]
        if line == "": break
        line = line.split(",")
        paper[int(line[1])][int(line[0])] = 1

    for line in file:
        line = line[:-1].split(" ")
        guide.append(line[-1].split("="))
        guide[-1][-1] = int(guide[-1][-1])

    file.close()

    # folding
    for i in range(len(guide)):
        paper = fold(paper, guide[i])

    '''# counting
    count = 0
    for x in range(edgeX):
        for y in range(edgeY):
            if paper[y][x] == 1:
                count += 1
    return count
    '''

    # drawing
    for y in range(edgeY):
        for x in range(edgeX):
            if paper[y][x] == 1:
                print("#", end = "")
            else:
                print(" ", end = "")
        print("")


    return

def fold(paper, guide):
    global edgeX
    global edgeY
    p = paper

    # fold right-side left
    if guide[0] == "x":
        for x in range(guide[1] + 1, edgeX):
            mirror = guide[1] - (x - guide[1])
            for y in range(edgeY):
                p[y][mirror] = max(p[y][x], p[y][mirror])
        edgeX = guide[1]

    # fold bottom up
    else:
        for y in range(guide[1] + 1, edgeY):
            mirror = guide[1] - (y - guide[1])
            for x in range(edgeX):
                p[mirror][x] = max(p[y][x], p[mirror][x])
        edgeY = guide[1]

    return p


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(count("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
