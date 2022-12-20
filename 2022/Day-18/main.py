### https://adventofcode.com/2022/day/18

from ast import literal_eval

INPUT = "input.txt"

def part_1():
    """
    Check every cube, add up every side that's not covered by another cube
    """
    with open(INPUT) as file:
        cubes = set(map(literal_eval, file.read().splitlines()))

    area = 0
    for cube in cubes:
        nearby = list(cube)
        for idx in range(len(cube)):
            for offset in (-1, 1):
                nearby[idx] += offset
                area += tuple(nearby) not in cubes
                nearby[idx] -= offset
    return area


def part_2():
    """
    BFS to flood the whole thing from outside, then check every cube,
    add up every side that's covered by water
    """
    with open(INPUT) as file:
        cubes = set(map(literal_eval, file.read().splitlines()))

    bounds = [
        range(10**9, -(10**9)),
        range(10**9, -(10**9)),
        range(10**9, -(10**9)),
    ]
    for cube in cubes:
        for idx in range(len(bounds)):
            bounds[idx] = range(
                min(cube[idx] - 1, bounds[idx].start),
                max(cube[idx] + 2, bounds[idx].stop),
            )

    flooded = [(bounds[0].start, bounds[1].start, bounds[2].start)]
    for coord in flooded:
        new_coord = list(coord)

        for idx in range(len(bounds)):
            for offset in (-1, 1):
                new_coord[idx] += offset
                if all(
                    (
                        new_coord[0] in bounds[0],
                        new_coord[1] in bounds[1],
                        new_coord[2] in bounds[2],
                        (new_coord_img := tuple(new_coord)) not in cubes,
                        new_coord_img not in flooded,
                    )
                ):
                    flooded.append(new_coord_img)
                new_coord[idx] -= offset

    flooded = set(flooded)
    area = 0
    for cube in cubes:
        nearby = list(cube)

        for idx in range(len(nearby)):
            for offset in (-1, 1):
                nearby[idx] += offset
                area += tuple(nearby) in flooded
                nearby[idx] -= offset

    return area


print(f"{part_1() = }")
print(f"{part_2() = }")
