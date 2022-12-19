### https://adventofcode.com/2022/day/18

from ast import literal_eval

INPUT = "test.txt"


def part_1():
    with open(INPUT) as file:
        cubes = set(map(literal_eval, file.read().splitlines()))

    area = 0
    clusters = [[cubes.pop()]]
    for cluster in clusters:
        for cube in cluster:
            new_cube = list(cube)
            for idx in range(len(cube)):
                for offset in (-1, 1):
                    new_cube[idx] += offset
                    if (new_cube_img := tuple(new_cube)) in cubes:
                        cluster.append(new_cube_img)
                        cubes.remove(new_cube_img)

                    new_cube[idx] -= offset
        if cubes:
            clusters.append([cubes.pop()])

        for cube in cluster:
            area += 6
            new_cube = list(cube)
            for idx in range(len(cube)):
                for offset in (-1, 1):
                    new_cube[idx] += offset
                    if tuple(new_cube) in cluster:
                        area -= 1
                    new_cube[idx] -= offset

    return area


def part_2():
    with open(INPUT) as file:
        cubes = set(map(literal_eval, file.read().splitlines()))

    area = 0
    clusters = [[cubes.pop()]]
    for cluster in clusters:
        for cube in cluster:
            new_cube = list(cube)

            for idx in range(len(cube)):
                for offset in (-1, 1):
                    new_cube[idx] += offset

                    for other_offset in (-1, 0, 1):
                        new_cube[idx - 1] += other_offset
                        if (new_cube_img := tuple(new_cube)) in cubes:
                            cluster.append(new_cube_img)
                            cubes.remove(new_cube_img)
                        new_cube[idx - 1] -= other_offset

                    new_cube[idx] -= offset

        for cube in cluster:
            area += 6
            new_cube = list(cube)
            for idx in range(len(cube)):
                for offset in (-1, 1):
                    new_cube[idx] += offset
                    if tuple(new_cube) in cluster:
                        area -= 1
                    new_cube[idx] -= offset

        if cubes:
            clusters.append([cubes.pop()])

    return area


print(f"{part_1() = }")
print(f"{part_2() = }")
