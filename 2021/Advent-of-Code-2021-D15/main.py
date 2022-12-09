# Matrix traversal
# Part 1: Dynamic programming worked
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
    return cavern
'''
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

    # P.2: Extruding the horizontal extrusion 5 times vertically
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
'''




def risk(cave):
    risk_map = [[10000 for i in range(len(cave[0]))] for i in range(len(cave))]
    risk_map[0][0] = 0

    for x in range(1, len(cave)):
        risk_map[x][0] = risk_map[x - 1][0] + cave[x][0]
        
    for y in range(1, len(cave[0])):
        risk_map[0][y] = risk_map[0][y - 1] + cave[0][y]
        
    for x in range(1, len(cave)):
        for y in range(1, len(cave[0])):
            risk_map[x][y] = min(risk_map[x - 1][y], risk_map[x][y - 1]) + cave[x][y]
            
    return risk_map[-1][-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    duration = datetime.datetime.now().timestamp()
    print(risk(cave("input.txt")))
    print(datetime.datetime.now().timestamp() - duration)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
