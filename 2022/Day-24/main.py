### https://adventofcode.com/2022/day/24

# TODO: Refactor this shit cuz wtf is this

INPUT = "input.txt"


def part_1():
    def progress(state: dict[tuple[int], str | list]) -> dict[tuple[int], str | list]:
        next_state = {
            (row_idx, col_idx): cell if cell == WALL else []
            for row_idx, row in enumerate(valley)
            for col_idx, cell in enumerate(row)
        }
        for coord in state:
            if isinstance(state[coord], list):
                row, col = coord
                for blizz in state[coord]:
                    r_offset, c_offset = BLIZZ_TYPES[blizz]
                    new_coord = (
                        (row - 2 + r_offset) % (len(valley) - 4) + 2,
                        (col - 1 + c_offset) % (len(valley[row]) - 2) + 1,
                    )
                    next_state[new_coord].append(blizz)
        return next_state

    from collections import deque, defaultdict
    from math import lcm

    BLIZZ_TYPES = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    CHOICES = ((1, 0), (0, 1), (0, 0), (-1, 0), (0, -1))
    START = (1, 1)
    WALL = "#"

    with open(INPUT) as file:
        valley = file.read().splitlines()

    valley.insert(0, WALL * len(valley[0]))
    valley.append(WALL * len(valley[0]))
    goal = (len(valley) - 2, len(valley[-1]) - 2)
    cycle = lcm(len(valley) - 4, len(valley[0]) - 2)
    state = {
        (row_idx, col_idx): cell
        if cell == WALL
        else [cell]
        if cell in BLIZZ_TYPES
        else []
        for row_idx, row in enumerate(valley)
        for col_idx, cell in enumerate(row)
    }
    next_state = progress(state)
    states = {0: state, 1: next_state}
    minute = 0
    explore = deque([START])
    explored = set()
    paths_at_min = defaultdict(int)
    paths_at_min[0] = 1

    while (curr_pos := explore.popleft()) != goal:
        row, col = curr_pos
        paths_at_min[minute] -= 1

        if (curr_pos, minute % cycle) not in explored:
            for choice in CHOICES:
                r_offset, c_offset = choice
                if (
                    not next_state[(next_pos := (row + r_offset, col + c_offset))]
                    and (next_pos, (minute + 1) % cycle) not in explored
                ):
                    explore.append(next_pos)
                    paths_at_min[minute + 1] += 1

            explored.add((curr_pos, minute % cycle))

        if paths_at_min[minute] == 0:
            del paths_at_min[minute]
            minute += 1
            state = next_state
            next_state = states.setdefault((minute + 1) % cycle, progress(state))

    return minute


def part_2():
    def progress(state: dict[tuple[int], str | list]) -> dict[tuple[int], str | list]:
        next_state = {
            (row_idx, col_idx): cell if cell == WALL else []
            for row_idx, row in enumerate(valley)
            for col_idx, cell in enumerate(row)
        }
        for coord in state:
            if isinstance(state[coord], list):
                row, col = coord
                for blizz in state[coord]:
                    r_offset, c_offset = BLIZZ_TYPES[blizz]
                    new_coord = (
                        (row - 2 + r_offset) % (len(valley) - 4) + 2,
                        (col - 1 + c_offset) % (len(valley[row]) - 2) + 1,
                    )
                    next_state[new_coord].append(blizz)
        return next_state

    from collections import deque, defaultdict
    from math import lcm

    BLIZZ_TYPES = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    CHOICES = ((1, 0), (0, 1), (0, 0), (-1, 0), (0, -1))
    START = (1, 1)
    WALL = "#"

    with open(INPUT) as file:
        valley = file.read().splitlines()

    valley.insert(0, WALL * len(valley[0]))
    valley.append(WALL * len(valley[0]))
    goal = (len(valley) - 2, len(valley[-1]) - 2)
    cycle = lcm(len(valley) - 4, len(valley[0]) - 2)
    state = {
        (row_idx, col_idx): cell
        if cell == WALL
        else [cell]
        if cell in BLIZZ_TYPES
        else []
        for row_idx, row in enumerate(valley)
        for col_idx, cell in enumerate(row)
    }
    next_state = progress(state)
    states = {0: state, 1: next_state}
    minute = 0

    explore = deque([START])
    explored = set()
    paths_at_min = defaultdict(int)
    paths_at_min[0] = 1

    while (curr_pos := explore.popleft()) != goal:
        row, col = curr_pos
        paths_at_min[minute] -= 1

        if (curr_pos, minute % cycle) not in explored:
            for choice in CHOICES:
                r_offset, c_offset = choice
                if (
                    not next_state[(next_pos := (row + r_offset, col + c_offset))]
                    and (next_pos, (minute + 1) % cycle) not in explored
                ):
                    explore.append(next_pos)
                    paths_at_min[minute + 1] += 1

            explored.add((curr_pos, minute % cycle))

        if paths_at_min[minute] == 0:
            del paths_at_min[minute]
            minute += 1
            state = next_state
            next_state = states.setdefault((minute + 1) % cycle, progress(state))

    explore = deque([goal])
    explored = set()
    paths_at_min = defaultdict(int)
    paths_at_min[minute] = 1

    while (curr_pos := explore.popleft()) != START:
        row, col = curr_pos
        paths_at_min[minute] -= 1

        if (curr_pos, minute % cycle) not in explored:
            for choice in reversed(CHOICES):
                r_offset, c_offset = choice
                if (
                    not next_state[(next_pos := (row + r_offset, col + c_offset))]
                    and (next_pos, (minute + 1) % cycle) not in explored
                ):
                    explore.append(next_pos)
                    paths_at_min[minute + 1] += 1

            explored.add((curr_pos, minute % cycle))

        if paths_at_min[minute] == 0:
            del paths_at_min[minute]
            minute += 1
            state = next_state
            next_state = states.setdefault((minute + 1) % cycle, progress(state))

    explore = deque([START])
    explored = set()
    paths_at_min = defaultdict(int)
    paths_at_min[minute] = 1

    while (curr_pos := explore.popleft()) != goal:
        row, col = curr_pos
        paths_at_min[minute] -= 1

        if (curr_pos, minute % cycle) not in explored:
            for choice in CHOICES:
                r_offset, c_offset = choice
                if (
                    not next_state[(next_pos := (row + r_offset, col + c_offset))]
                    and (next_pos, (minute + 1) % cycle) not in explored
                ):
                    explore.append(next_pos)
                    paths_at_min[minute + 1] += 1

            explored.add((curr_pos, minute % cycle))

        if paths_at_min[minute] == 0:
            del paths_at_min[minute]
            minute += 1
            state = next_state
            next_state = states.setdefault((minute + 1) % cycle, progress(state))

    return minute


print(f"{part_1() = }")
print(f"{part_2() = }")
