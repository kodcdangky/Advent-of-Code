### https://adventofcode.com/2022/day/23

INPUT = "input.txt"


def progress(round, elves):
    from collections import defaultdict
    from itertools import product

    MOVEMENT = ((-1, 0), (1, 0), (0, -1), (0, 1))

    progressed = False
    new_locations = defaultdict(set)
    prio_dirs = MOVEMENT[round % len(MOVEMENT) :] + MOVEMENT[: round % len(MOVEMENT)]

    for pos in elves:
        lonely = True
        free = {direction: True for direction in MOVEMENT}

        # Check if there are any surrounding elves, if yes, which directions they are blocking
        for r_offset, c_offset in product((-1, 0, 1), repeat=2):
            if r_offset or c_offset:
                if (pos[0] + r_offset, pos[1] + c_offset) in elves:
                    progressed = True
                    lonely = False
                    for direction in free:
                        if (
                            r_offset == direction[0] != 0
                            or c_offset == direction[1] != 0
                        ):
                            free[direction] = False

        if lonely:
            continue

        # If elf not lonely, record their proposed new position
        for direction in prio_dirs:
            if free[direction]:
                new_pos = pos[0] + direction[0], pos[1] + direction[1]
                new_locations[new_pos].add(pos)
                break

    # Update every new position currently with only 1 elf planned
    for new_pos in new_locations:
        if len(new_locations[new_pos]) == 1:
            elves.remove(new_locations[new_pos].pop())
            elves.add(new_pos)

    return progressed


def part_1():
    ROUNDS = 10
    ELF = "#"

    elves = set()
    with open(INPUT) as file:
        for line_idx, line in enumerate(file):
            for char_idx, char in enumerate(line[:-1]):
                if char == ELF:
                    elves.add((line_idx, char_idx))

    for round in range(ROUNDS):
        progress(round, elves)

    row_range = col_range = range(100, -100)
    for pos in elves:
        row, col = pos
        row_range = range(min(row_range.start, row), max(row_range.stop, row + 1))
        col_range = range(min(col_range.start, col), max(col_range.stop, col + 1))

    return len(row_range) * len(col_range) - len(elves)


def part_2():
    ELF = "#"

    elves = set()
    with open(INPUT) as file:
        for line_idx, line in enumerate(file):
            for char_idx, char in enumerate(line[:-1]):
                if char == ELF:
                    elves.add((line_idx, char_idx))

    round = 0
    while progress(round, elves):
        round += 1

    return round + 1


print(f"{part_1() = }")
print(f"{part_2() = }")
