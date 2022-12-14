### https://adventofcode.com/2022/day/14

INPUT = "input.txt"


def part_1():
    SAND_ENTRANCE = (500, 0)

    with open(INPUT) as file:
        walls = map(
            lambda line: tuple(
                map(
                    lambda coord: tuple(
                        map(lambda xy: int(xy), coord.strip().split(","))
                    ),
                    line.split("->"),
                )
            ),
            file.read().splitlines(),
        )

    blocked = set()
    bottom = 0
    for wall in walls:
        for point_a, point_b in zip(wall, wall[1:]):
            (a_x, a_y), (b_x, b_y) = point_a, point_b
            bottom = max(bottom, a_y, b_y)
            if a_x == b_x:
                for y in range(a_y, b_y, (b_y - a_y) // abs(b_y - a_y)):
                    blocked.add((a_x, y))
            elif a_y == b_y:
                for x in range(a_x, b_x, (b_x - a_x) // abs(b_x - a_x)):
                    blocked.add((x, a_y))
            blocked.add(point_b)

    sand = 0
    while True:
        current_sand = SAND_ENTRANCE
        while True:
            for x in (current_sand[0], current_sand[0] - 1, current_sand[0] + 1):
                if (x, current_sand[1] + 1) not in blocked:
                    current_sand = (x, current_sand[1] + 1)
                    break
            else:
                blocked.add(current_sand)
                sand += 1
                break

            if current_sand[1] >= bottom:
                break

        if current_sand == SAND_ENTRANCE or current_sand[1] >= bottom:
            break

    return sand


def part_2():
    SAND_ENTRANCE = (500, 0)

    with open(INPUT) as file:
        walls = map(
            lambda line: tuple(
                map(
                    lambda coord: tuple(
                        map(lambda xy: int(xy), coord.strip().split(","))
                    ),
                    line.split("->"),
                )
            ),
            file.read().splitlines(),
        )

    blocked = set()
    bottom = 0
    for wall in walls:
        for point_a, point_b in zip(wall, wall[1:]):
            (a_x, a_y), (b_x, b_y) = point_a, point_b
            bottom = max(bottom, a_y, b_y)
            if a_x == b_x:
                for y in range(a_y, b_y, (b_y - a_y) // abs(b_y - a_y)):
                    blocked.add((a_x, y))
            elif a_y == b_y:
                for x in range(a_x, b_x, (b_x - a_x) // abs(b_x - a_x)):
                    blocked.add((x, a_y))
            blocked.add(point_b)

    bottom += 2

    sand = 0
    while True:
        current_sand = SAND_ENTRANCE
        while True:
            for x in (current_sand[0], current_sand[0] - 1, current_sand[0] + 1):
                if current_sand[1] + 1 < bottom and (x, current_sand[1] + 1) not in blocked:
                    current_sand = (x, current_sand[1] + 1)
                    break
            else:
                blocked.add(current_sand)
                sand += 1
                break

        if current_sand == SAND_ENTRANCE:
            break

    return sand


print(f"{part_1() = }")
print(f"{part_2() = }")
