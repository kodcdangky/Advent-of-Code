# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime


def get_scanners(txt):
    scanners = []
    with open(txt) as file:
        for line in file:
            if line[0:3] == '---':
                scanners.append([])
            elif line[0] == '\n':
                continue
            else:
                scanners[-1].append(line[:-1])
                scanners[-1][-1] = scanners[-1][-1].split(',')
                scanners[-1][-1][0] = int(scanners[-1][-1][0])
                scanners[-1][-1][1] = int(scanners[-1][-1][1])
                scanners[-1][-1][2] = int(scanners[-1][-1][2])
    return scanners

def manhattan_distance(beacon0, beacon1):
    return abs(beacon0[0] - beacon1[0]) + abs(beacon0[1] - beacon1[1]) + abs(beacon0[2] - beacon1[2])

def construct_distances(scanner):
    distances = []
    for beacon0 in scanner:
        distances.append([])
        for beacon1 in scanner:
            distances[-1].append(manhattan_distance(beacon0, beacon1))
    return distances


def construct_relative_locations(scanner):

    def relative_location():
        return beacon1[0] - beacon0[0], beacon1[1] - beacon0[1], beacon1[2] - beacon0[2]

    locations = []
    for beacon0 in scanner:
        locations.append([])
        for beacon1 in scanner:
            locations[-1].append(relative_location())
    return locations


scanners_pos = {(0, 0, 0)}  # part 2
def merge(scanner0, scanner):
    scanner_og = []
    for i in scanner:
        scanner_og.append(i.copy())

    def reorient():
        intersect = intersection()
        if len(intersect) < 12:
            for orientation in range(23):   # refer to scanners-orientations.txt; orientation + 2 == line number on txt
                match orientation:
                    case 0:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][0]
                            scanner[beacon][1] = scanner_og[beacon][2]
                            scanner[beacon][2] = -scanner_og[beacon][1]
                    case 1:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][0]
                            scanner[beacon][1] = -scanner_og[beacon][1]
                            scanner[beacon][2] = -scanner_og[beacon][2]
                    case 2:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][0]
                            scanner[beacon][1] = -scanner_og[beacon][2]
                            scanner[beacon][2] = scanner_og[beacon][1]
                    case 3:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][1]
                            scanner[beacon][1] = -scanner_og[beacon][0]
                            scanner[beacon][2] = scanner_og[beacon][2]
                    case 4:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][2]
                            scanner[beacon][1] = -scanner_og[beacon][0]
                            scanner[beacon][2] = -scanner_og[beacon][1]
                    case 5:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][1]
                            scanner[beacon][1] = -scanner_og[beacon][0]
                            scanner[beacon][2] = -scanner_og[beacon][2]
                    case 6:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][2]
                            scanner[beacon][1] = -scanner_og[beacon][0]
                            scanner[beacon][2] = scanner_og[beacon][1]
                    case 7:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][0]
                            scanner[beacon][1] = -scanner_og[beacon][1]
                            scanner[beacon][2] = scanner_og[beacon][2]
                    case 8:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][0]
                            scanner[beacon][1] = -scanner_og[beacon][2]
                            scanner[beacon][2] = -scanner_og[beacon][1]
                    case 9:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][0]
                            scanner[beacon][1] = scanner_og[beacon][1]
                            scanner[beacon][2] = -scanner_og[beacon][2]
                    case 10:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][0]
                            scanner[beacon][1] = scanner_og[beacon][2]
                            scanner[beacon][2] = scanner_og[beacon][1]
                    case 11:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][1]
                            scanner[beacon][1] = scanner_og[beacon][0]
                            scanner[beacon][2] = scanner_og[beacon][2]
                    case 12:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][2]
                            scanner[beacon][1] = scanner_og[beacon][0]
                            scanner[beacon][2] = -scanner_og[beacon][1]
                    case 13:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][1]
                            scanner[beacon][1] = scanner_og[beacon][0]
                            scanner[beacon][2] = -scanner_og[beacon][2]
                    case 14:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][2]
                            scanner[beacon][1] = scanner_og[beacon][0]
                            scanner[beacon][2] = scanner_og[beacon][1]
                    case 15:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][2]
                            scanner[beacon][1] = scanner_og[beacon][1]
                            scanner[beacon][2] = scanner_og[beacon][0]
                    case 16:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][1]
                            scanner[beacon][1] = scanner_og[beacon][2]
                            scanner[beacon][2] = scanner_og[beacon][0]
                    case 17:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][2]
                            scanner[beacon][1] = -scanner_og[beacon][1]
                            scanner[beacon][2] = scanner_og[beacon][0]
                    case 18:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][1]
                            scanner[beacon][1] = -scanner_og[beacon][2]
                            scanner[beacon][2] = scanner_og[beacon][0]
                    case 19:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][2]
                            scanner[beacon][1] = scanner_og[beacon][1]
                            scanner[beacon][2] = -scanner_og[beacon][0]
                    case 20:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][1]
                            scanner[beacon][1] = scanner_og[beacon][2]
                            scanner[beacon][2] = -scanner_og[beacon][0]
                    case 21:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = -scanner_og[beacon][2]
                            scanner[beacon][1] = -scanner_og[beacon][1]
                            scanner[beacon][2] = -scanner_og[beacon][0]
                    case 22:
                        for beacon in range(len(scanner)):
                            scanner[beacon][0] = scanner_og[beacon][1]
                            scanner[beacon][1] = -scanner_og[beacon][2]
                            scanner[beacon][2] = -scanner_og[beacon][0]
                intersect = intersection()
                if len(intersect) >= 12:
                    return intersect
            else:
                return False
        else:
            return intersect

    locations0 = construct_relative_locations(scanner0)
    def intersection():
        locations = construct_relative_locations(scanner)

        intersect = []
        for l0 in range(len(locations0)):
            for l in range(len(locations)):
                if len(set(locations[l]).intersection(locations0[l0])) >= 12:
                    intersect.append((scanner0[l0], scanner[l]))
                    break
        return intersect

    intersect = reorient()
    if not intersect:
        return scanner0, False

    scanner_pos = intersect[0][0][0] - intersect[0][1][0], intersect[0][0][1] - intersect[0][1][1], intersect[0][0][2] - intersect[0][1][2]

    # part 2
    global scanners_pos
    scanners_pos.add(scanner_pos)

    for pair in intersect:
        scanner.remove(pair[1])
    for beacon in scanner:
        scanner0.append([scanner_pos[0] + beacon[0], scanner_pos[1] + beacon[1], scanner_pos[2] + beacon[2]])
    return scanner0, True


def beacon_count(scanners):
    merged = [False for _ in range(len(scanners))]
    merged[0] = True
    while False in merged:
        for scanner in range(1, len(scanners)):
            if not merged[scanner]:
                scanners[0], merged[scanner] = merge(scanners[0], scanners[scanner])
    print(len(scanners[0]), 'beacons in total')

    # part 2
    global scanners_pos
    scanners_pos = tuple(scanners_pos)
    longest_cab_ride = 0
    for scanner0 in scanners_pos:
        for scanner1 in scanners_pos:
            distance = manhattan_distance(scanner0, scanner1)
            if longest_cab_ride < distance:
                longest_cab_ride = distance
    print('Largest Manhattan distance between two scanners:', longest_cab_ride)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    duration = datetime.datetime.now().timestamp()
    beacon_count(get_scanners('input.txt'))
    print(datetime.datetime.now().timestamp() - duration)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
