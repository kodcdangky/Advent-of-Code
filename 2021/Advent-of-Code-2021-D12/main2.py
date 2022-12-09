# Fuck tree traversal

def paths(txt):
    global node
    global nodeS
    global path
    global count
    global permit

    node = ["start", "end"]
    nodeS = [0, 0]
    init(txt)

    count = 0
    permit = [0 for i in range(len(node))]
    findpaths(0)
    return count


def findpaths(location):
    global node
    global nodeS
    global path
    global count
    global permit

    if node[location] == "end":
        count += 1
        return

    if nodeS[location] == 0:
        nodeS[location] = -1
    elif nodeS[location] == -1:
        if permit[location] == 0 and sum(permit) == 0:
            permit[location] = 1
        else:
            return

    for dest in range(1, len(node)):
        if path[location][dest] == 1:
                findpaths(dest)

    if nodeS[location] == -1:
        if permit[location] == 1:
            permit[location] = 0
        else:
            nodeS[location] = 0


def init(txt):
    global node
    global nodeS
    global path
    file = open(txt)

    for line in file:
        line = line[:-1].split("-")
        try:
            i = node.index(line[0])
        except:
            i = -1
        if i == -1:
            node.insert(-1, line[0])
            if node[-2].islower():
                nodeS.insert(-1, 0)
            else: nodeS.insert(-1, 1)

        try:
            j = node.index(line[1])
        except:
            j = -1
        if j == -1:
            node.insert(-1, line[1])
            if node[-2].islower():
                nodeS.insert(-1, 0)
            else: nodeS.insert(-1, 1)

    path = [[0 for i in range(len(node))] for i in range(len(node))]
    file.seek(0)
    for line in file:
        line = line[:-1].split("-")
        i = node.index(line[0])
        j = node.index(line[1])
        path[i][j] = 1
        path[j][i] = 1

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(paths("input.txt"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
