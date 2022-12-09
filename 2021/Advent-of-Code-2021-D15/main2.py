# Matrix traversal
# Part 2: Dijkstra's cuz noone told me u can go up or left on this table and DP worked for part 1
import datetime


def cave(txt):
    file = open(txt)
    cavern = []
    for line in file:
        line = line[:-1]
        line_chars = []
        for c in line:
            line_chars.append(int(c))
        cavern.append(line_chars)
    file.close()

    # P.2: Extruding 5 times horizontally
    hori = len(cavern[0])
    verti = len(cavern)
    for i in range(1, 5):
        for x in range(verti):
            for y in range(hori):
                temp = cavern[x][y] + i
                if temp > 9:
                    cavern[x].append((cavern[x][y] + i) % 9)
                else:
                    cavern[x].append(cavern[x][y] + i)

    # Extruding the horizontal extrusion 5 times vertically
    hori = len(cavern[0])
    for i in range(1, 5):
        for x in range(verti):
            # layer = cavern[x]
            # for j in range(len(layer)):
            #     layer[j] = (layer[j] + 1) % 9
            # cavern.append(layer)
            cavern.append(cavern[x].copy())
            for y in range(hori):
                cavern[-1][y] = cavern[-1][y] + i
                if cavern[-1][y] > 9:
                    cavern[-1][y] %= 9

    # adding a buffer zone around the outside for Dijkstra's
    cavern.insert(0, [100000 for i in range(len(cavern[0]))])
    cavern.append([100000 for i in range(len(cavern[0]))])
    for x in range(len(cavern)):
        cavern[x].insert(0, 100000)
        cavern[x].append(100000)

    return cavern


'''
Dijkstra's: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
risk_map[][] == list of distance from source value
mini == used to look for node with lowest distance from source value
considered[][] == marks visited nodes as 1, unvisited as 0
area == size of content matrix. since considered[][] marks visited nodes as 1, if sum of all nodes in considered[][] == area, this means all nodes have been visited
OG Dijkstra's implementation is O(n^2), so for matrices it takes super long to finish (500^2 table took ~1.33 hours)
There are optimizations for Dijkstra's like the one below that works far better for this problem but honestly it's a lot of work
Dijkstra's Min Heap (adjacency list representation): https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/?ref=lbp
'''
def risk(cave):
    risk_map = [[10000 for i in range(len(cave[0]))] for i in range(len(cave))]
    risk_map[1][1] = 0
    considered = [[0 for i in range(len(cave[0]))] for i in range(len(cave))]
    area = (len(cave) - 2) * (len(cave[0]) - 2)

    while sum2d(considered) < area:
        mini = 10000
        for x in range(1, len(cave) - 1):
            for y in range(1, len(cave[0]) - 1):
                if considered[x][y] == 0 and mini > risk_map[x][y]:
                        mini = risk_map[x][y]
                        Xmin = x
                        Ymin = y
                
        considered[Xmin][Ymin] = 1
        if risk_map[Xmin - 1][Ymin] > risk_map[Xmin][Ymin] + cave[Xmin - 1][Ymin]:
            risk_map[Xmin - 1][Ymin] = risk_map[Xmin][Ymin] + cave[Xmin - 1][Ymin]

        if risk_map[Xmin + 1][Ymin] > risk_map[Xmin][Ymin] + cave[Xmin + 1][Ymin]:
            risk_map[Xmin + 1][Ymin] = risk_map[Xmin][Ymin] + cave[Xmin + 1][Ymin]

        if risk_map[Xmin][Ymin - 1] > risk_map[Xmin][Ymin] + cave[Xmin][Ymin - 1]:
            risk_map[Xmin][Ymin - 1] = risk_map[Xmin][Ymin] + cave[Xmin][Ymin - 1]

        if risk_map[Xmin][Ymin + 1] > risk_map[Xmin][Ymin] + cave[Xmin][Ymin + 1]:
            risk_map[Xmin][Ymin + 1] = risk_map[Xmin][Ymin] + cave[Xmin][Ymin + 1]

    return risk_map[-2][-2]


def sum2d(list2d):
    count = 0
    for x in range(len(list2d)):
        count += sum(list2d[x])
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    duration = datetime.datetime.now().timestamp()
    print(risk(cave("test.txt")))
    print(datetime.datetime.now().timestamp() - duration)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
