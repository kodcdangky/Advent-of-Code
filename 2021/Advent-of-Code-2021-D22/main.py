# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime


def init(txt):
    instruction = []
    with open(txt) as file:
        for line in file:
            instruction.append(line[:-1])
            instruction[-1] = instruction[-1].split(' ')
            instruction[-1][-1] = zone(instruction[-1][-1])
            instruction[-1] = tuple(instruction[-1])
    return tuple(instruction)


# def intersect(coord0, coord1):
#     zone0 = zone(coord0)
#     zone1 = zone(coord1)
#
#     # if x or y or z doesn't intersect, 2 cubes don't intersect
#     if zone0[0][1] < zone1[0][0] or zone0[0][0] > zone1[0][1] \
#         or zone0[1][1] < zone1[1][0] or zone0[1][0] > zone1[1][1] \
#             or zone0[2][1] < zone1[2][0] or zone0[2][0] > zone1[2][1]:
#         return -1
#
#     # intersecting box's address is always max(opening coordinates) - min(closing coordinates)
#     x0 = max(zone0[0][0], zone1[0][0])
#     y0 = max(zone0[1][0], zone1[1][0])
#     z0 = max(zone0[2][0], zone1[2][0])
#     x1 = min(zone0[0][1], zone1[0][1])
#     y1 = min(zone0[1][1], zone1[1][1])
#     z1 = min(zone0[2][1], zone1[2][1])
#     return (x0, x1, y0, y1, z0, z1)


# def add(zone0, zone1):
#     return volume(zone0) + volume(zone1) - intersect(zone0, zone1)
#
#
# def volume(zone):
#     return abs(zone[0][1] - zone[0][0]) * abs(zone[1][1] - zone[1][0]) * abs(zone[2][1] - zone[2][0])
#
#


def zone(coord):
    coord = coord.split(',')
    for i in range(3):
        coord[i] = coord[i][2:].split('..')
        coord[i][0] = int(coord[i][0])
        coord[i][1] = int(coord[i][1]) + 1
    return coord[0][0], coord[0][1], coord[1][0], coord[1][1], coord[2][0], coord[2][1]


# def reboot(instruction):
#     core = {}
#     for i in instruction:
#         match i[0]:
#             case 'on':
#                 for x in range(i[1][0], i[1][1] + 1):
#                     for y in range(i[1][2], i[1][3] + 1):
#                         for z in range(i[1][4], i[1][5] + 1):
#                             core.setdefault((x, y, z))
#             case 'off':
#                 for x in range(i[1][0], i[1][1] + 1):
#                     for y in range(i[1][2], i[1][3] + 1):
#                         for z in range(i[1][4], i[1][5] + 1):
#                             try:
#                                 core.pop((x, y, z))
#                             except KeyError:
#                                 pass
#                             # if (x, y, z) in core:
#                             #     core.pop((x, y, z))
#     return len(core)


def reboot(instruction):

    axisX = {}
    axisY = {}
    axisZ = {}

    def aabb():
        # Axis-aligned Bounding Boxes' opening ritual
        checkpointX = {}
        checkpointY = {}
        checkpointZ = {}

        for index, i in enumerate(instruction):
            try:
                checkpointX[i[1][0]][True].append(index)
            except KeyError:
                checkpointX.update({i[1][0]: {True: [index], False: []}})
            try:
                checkpointX[i[1][1]][False].append(index)
            except KeyError:
                checkpointX.update({i[1][1]: {True: [], False: [index]}})

            try:
                checkpointY[i[1][2]][True].append(index)
            except KeyError:
                checkpointY.update({i[1][2]: {True: [index], False: []}})
            try:
                checkpointY[i[1][3]][False].append(index)
            except KeyError:
                checkpointY.update({i[1][3]: {True: [], False: [index]}})

            try:
                checkpointZ[i[1][4]][True].append(index)
            except KeyError:
                checkpointZ.update({i[1][4]: {True: [index], False: []}})
            try:
                checkpointZ[i[1][5]][False].append(index)
            except KeyError:
                checkpointZ.update({i[1][5]: {True: [], False: [index]}})

        checkpointX = dict(sorted(checkpointX.items()))
        checkpointY = dict(sorted(checkpointY.items()))
        checkpointZ = dict(sorted(checkpointZ.items()))

        checkpointX_keys = tuple(checkpointX.keys())
        last_x = checkpointX_keys[0]
        active = set(checkpointX[last_x][True])
        for x in checkpointX_keys[1:]:
            axisX.update({(last_x, x): active.copy()})
            last_x = x
            active = active.union(set(checkpointX[x][True]))
            active.difference_update(set(checkpointX[x][False]))

        checkpointY_keys = tuple(checkpointY.keys())
        last_y = checkpointY_keys[0]
        active = set(checkpointY[last_y][True])
        for y in checkpointY_keys[1:]:
            axisY.update({(last_y, y): active.copy()})
            last_y = y
            active = active.union(set(checkpointY[y][True]))
            active.difference_update(set(checkpointY[y][False]))

        checkpointZ_keys = tuple(checkpointZ.keys())
        last_z = checkpointZ_keys[0]
        active = set(checkpointZ[last_z][True])
        for z in checkpointZ_keys[1:]:
            axisZ.update({(last_z, z): active.copy()})
            last_z = z
            active = active.union(set(checkpointZ[z][True]))
            active.difference_update(set(checkpointZ[z][False]))
    aabb()

    axisX_key = tuple(axisX.keys())

    cubes_on = 0
    for x in axisX:
        for y in axisY:
            for z in axisZ:
                cube = axisX[x].intersection(axisY[y], axisZ[z])
                if len(cube) > 0:
                    cube = max(cube)
                    if instruction[cube][0] == 'on':
                        cubes_on += abs(x[0] - x[1]) * abs(y[0] - y[1]) * abs(z[0] - z[1])
        print('axisX [', axisX_key.index(x), '/', len(axisX_key), ']')

    return cubes_on


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    duration = datetime.datetime.now().timestamp()
    print(reboot(init('input.txt')))
    print(datetime.datetime.now().timestamp() - duration)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
