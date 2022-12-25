### https://adventofcode.com/2022/day/24

from collections import deque, defaultdict
from math import lcm

INPUT = "test.txt"

BLIZZ_TYPES = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
CHOICES = ((1, 0), (0, 1), (0, 0), (-1, 0), (0, -1))
START = (1, 1)
WALL = "#"

with open(INPUT) as file:
    valley = file.read().splitlines()
valley.insert(0, WALL * len(valley[0]))
valley.append(WALL * len(valley[0]))

cycle = lcm(len(valley) - 4, len(valley[0]) - 2)

states = {
    0: {
        (row_idx, col_idx): cell
        if cell == WALL
        else [cell]
        if cell in BLIZZ_TYPES
        else []
        for row_idx, row in enumerate(valley)
        for col_idx, cell in enumerate(row)
    }
}


def progress(state: dict[tuple[int], str | list]) -> dict[tuple[int], str | list]:
    """Progress the state to the next state

    Args:
        state (dict[tuple[int], str  |  list]): current blizzards state

    Returns:
        dict[tuple[int], str | list]: next blizzards state
    """
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


def shortest_path(
    start: tuple[int, int], goal: tuple[int, int], elapsed: int = 0
) -> int:
    """BFS, go through each position-state pairing at most once
    Stores all visited states for future visit

    Args:
        start (tuple[int, int]): starting row, col
        goal (tuple[int, int]): row, col of goal
        elapsed (int, optional): Time spent so far. Defaults to 0.

    Returns:
        int: final time elapsed
    """
    explore = deque([start])
    explored = set()
    paths_at_min = defaultdict(int)
    paths_at_min[elapsed] = 1

    state = states[elapsed % cycle]
    next_state = states.setdefault((elapsed + 1) % cycle, progress(state))

    while (curr_pos := explore.popleft()) != goal:
        row, col = curr_pos
        paths_at_min[elapsed] -= 1

        if (curr_pos, elapsed % cycle) not in explored:
            for choice in CHOICES:
                r_offset, c_offset = choice
                if (
                    not next_state[(next_pos := (row + r_offset, col + c_offset))]
                    and (next_pos, (elapsed + 1) % cycle) not in explored
                ):
                    explore.append(next_pos)
                    paths_at_min[elapsed + 1] += 1

            explored.add((curr_pos, elapsed % cycle))

        if paths_at_min[elapsed] == 0:
            del paths_at_min[elapsed]
            elapsed += 1
            state = next_state
            next_state = states.setdefault((elapsed + 1) % cycle, progress(state))

    return elapsed


def part_1():
    goal = len(valley) - 2, len(valley[-1]) - 2
    return shortest_path(START, goal)


def part_2():
    goal = (len(valley) - 2, len(valley[-1]) - 2)
    pass_1 = shortest_path(START, goal)
    pass_2 = shortest_path(goal, START, pass_1)
    return shortest_path(START, goal, pass_2)


print(f"{part_1() = }")
print(f"{part_2() = }")
