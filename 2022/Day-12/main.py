### https://adventofcode.com/2022/day/12

# Input reading can be better tbh

INPUT = "input.txt"

from string import ascii_lowercase

TRANSLATION = {letter: height for height, letter in enumerate(ascii_lowercase)}
TRANSLATION["S"] = TRANSLATION[ascii_lowercase[0]]
TRANSLATION["E"] = TRANSLATION[ascii_lowercase[-1]]


def next_step(origin: tuple, step: tuple) -> tuple:
    return origin[0] + step[0], origin[1] + step[1]


def valid(origin: tuple, dest: tuple, height_map: tuple[tuple[int]]) -> bool:
    return (
        dest[0] in range(len(height_map))
        and dest[1] in range(len(height_map[dest[0]]))
        and height_map[dest[0]][dest[1]] <= height_map[origin[0]][origin[1]] + 1
    )


def manhattan_dist(origin: tuple, dest: tuple) -> int:
    return abs(dest[0] - origin[0]) + abs(dest[1] - origin[1])


def part_1():
    with open(INPUT) as file:
        height_map = tuple(
            map(
                lambda line: tuple(map(lambda char: TRANSLATION[char], line)),
                file.read().splitlines(),
            )
        )
        file.seek(0, 0)
        start = end = None
        for row, line in enumerate(file.read().splitlines()):
            if "S" in line:
                start = row, line.index("S")
            if "E" in line:
                end = row, line.index("E")
            if start and end:
                break

    openings = {start}
    min_cost = {start: 0}
    heuristics = {start: manhattan_dist(start, end)}

    while openings:
        best_lead = min(
            openings, key=lambda opening: min_cost[opening] + heuristics[opening]
        )
        openings.remove(best_lead)

        for step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dest = next_step(best_lead, step)

            if valid(best_lead, dest, height_map):
                dest_cost = min_cost[best_lead] + 1

                if dest_cost < min_cost.get(dest, float("inf")):
                    min_cost[dest] = dest_cost

                    if dest not in heuristics:
                        heuristics[dest] = manhattan_dist(dest, end)

                    openings.add(dest)

    return min_cost[end]


def part_2():
    with open(INPUT) as file:
        height_map = tuple(
            map(
                lambda line: tuple(map(lambda char: TRANSLATION[char], line)),
                file.read().splitlines(),
            )
        )
        file.seek(0, 0)
        end = None
        for row, line in enumerate(file.read().splitlines()):
            if "E" in line:
                end = row, line.index("E")
                break

    openings = set(
        (row_indx, cell_indx)
        for row_indx, row in enumerate(height_map)
        for cell_indx, cell in enumerate(row)
        if cell == 0
    )
    min_cost = {start: 0 for start in openings}
    heuristics = {start: manhattan_dist(start, end) for start in openings}

    while openings:
        best_lead = min(
            openings, key=lambda opening: min_cost[opening] + heuristics[opening]
        )
        openings.remove(best_lead)

        for step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dest = next_step(best_lead, step)

            if valid(best_lead, dest, height_map):
                dest_cost = min_cost[best_lead] + 1

                if dest_cost < min_cost.get(dest, float("inf")):
                    min_cost[dest] = dest_cost

                    if dest not in heuristics:
                        heuristics[dest] = manhattan_dist(dest, end)

                    openings.add(dest)

    return min_cost[end]


print(f"{part_1() = }")
print(f"{part_2() = }")
