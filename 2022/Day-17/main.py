### https://adventofcode.com/2022/day/17

INPUT = "input.txt"
COLS = 7
LEFT_MARGIN = 2
FALL_SPACE = 3
ROCKS = (
    (1, ((1,), (1,), (1,), (1,))),
    (3, ((0, 1, 0), (1, 1, 1), (0, 1, 0))),
    (3, ((1, 0, 0), (1, 0, 0), (1, 1, 1))),
    (4, ((1, 1, 1, 1),)),
    (2, ((1, 1), (1, 1))),
)


def spawn_rock(
    turn: int, cols: list[list[int]]
) -> tuple[tuple[tuple[int, ...]], tuple[int, ...]]:
    rock_height, rock = ROCKS[turn % len(ROCKS)]
    height = highest_peak(cols) + FALL_SPACE + rock_height
    for col in cols:
        col.extend([0] * (height - len(col)))

    up = height
    down = height - rock_height
    left = LEFT_MARGIN
    right = LEFT_MARGIN + len(rock)

    for col_idx, rock_col in zip(range(left, right), rock):
        for row_idx, rock_cell in zip(range(down, up), rock_col):
            cols[col_idx][row_idx] = rock_cell

    return rock, (up, down, left, right)


def erase(
    rock: tuple[tuple[int, ...]], bound: tuple[int, ...], cols: list[list[int]]
) -> None:
    up, down, left, right = bound
    for col_idx, rock_col in zip(range(left, right), rock):
        for row_idx, rock_cell in zip(range(down, up), rock_col):
            if rock_cell:
                cols[col_idx][row_idx] = 0


def draw(
    rock: tuple[tuple[int, ...]], bound: tuple[int, ...], cols: list[list[int]]
) -> None:
    up, down, left, right = bound
    for col_idx, rock_col in zip(range(left, right), rock):
        for row_idx, rock_cell in zip(range(down, up), rock_col):
            cols[col_idx][row_idx] = rock_cell or cols[col_idx][row_idx]


def shift_left(
    rock: tuple[tuple[int, ...]], bound: tuple[int, ...], cols: list[list[int]]
) -> tuple[int, ...]:
    up, down, left, right = bound
    if left == 0:
        return bound

    erase(rock, bound, cols)

    for col_idx, rock_col in zip(range(left - 1, right - 1), rock):
        for row_idx, rock_cell in zip(range(down, up), rock_col):
            if cols[col_idx][row_idx] + rock_cell > 1:
                draw(rock, bound, cols)
                return bound

    new_bound = up, down, left - 1, right - 1
    draw(rock, new_bound, cols)
    return new_bound


def shift_right(
    rock: tuple[tuple[int, ...]], bound: tuple[int, ...], cols: list[list[int]]
) -> tuple[int, ...]:
    up, down, left, right = bound
    if right == len(cols):
        return bound

    erase(rock, bound, cols)

    for col_idx, rock_col in zip(range(left + 1, right + 1), rock):
        for row_idx, rock_cell in zip(range(down, up), rock_col):
            if cols[col_idx][row_idx] + rock_cell > 1:
                draw(rock, bound, cols)
                return bound

    new_bound = up, down, left + 1, right + 1
    draw(rock, new_bound, cols)
    return new_bound


def shift_down(
    rock: tuple[tuple[int, ...]], bound: tuple[int, ...], cols: list[list[int]]
) -> None | tuple[int, ...]:
    up, down, left, right = bound
    if down == 0:
        return

    erase(rock, bound, cols)

    for col_idx, rock_col in zip(range(left, right), rock):
        for row_idx, rock_cell in zip(range(down - 1, up - 1), rock_col):
            if cols[col_idx][row_idx] + rock_cell > 1:
                draw(rock, bound, cols)
                return

    new_bound = up - 1, down - 1, left, right
    draw(rock, new_bound, cols)
    return new_bound


def highest_peak(cols: list[list[int]]) -> int:
    reversed_cols = (reversed(col) for col in cols)
    for idx_from_top, row in enumerate(zip(*reversed_cols)):
        if 1 in set(row):
            return len(cols[0]) - idx_from_top
    raise Exception("highest_peak() did not return a value")


def day_17(turns):
    def inverse_bfs(cols: list[list[int]]):
        if len(cols[0]) <= highest_peak(cols) + 1:
            for col in cols:
                col.append(0)

        c_bound = range(len(cols))
        r_bound = range(len(cols[0]))

        flooded: list[tuple[int, int]] = [(0, len(cols[0]) - 1)]
        bottom = len(cols[0]) - 1
        for coord in flooded:
            for offset in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                col = coord[0] + offset[0]
                row = coord[1] + offset[1]

                if (
                    col in c_bound
                    and row in r_bound
                    and not cols[col][row]
                    and (col, row) not in flooded
                ):
                    flooded.append((col, row))
                    bottom = min(bottom, row)

        return bottom

    def inverse(flood_btm: int, cols: list[list[int]]) -> tuple[int, tuple[tuple[int]]]:
        abyss = max(0, flood_btm - 1)
        top_shape = tuple(tuple(col[abyss : highest_peak(cols) + 1]) for col in cols)
        return abyss, top_shape

    with open(INPUT) as file:
        wind = file.readline()[:-1]

    cols = [[1] for _ in range(COLS)]
    wind_idx = 0
    top_shape = (1,) * 7
    abyss = 0
    cycle_detector = {}
    next_state = 0, 0, top_shape
    peak = []
    for turn in range(turns):
        state = next_state
        # spawn new rock
        rock, rock_bound = spawn_rock(turn, cols)

        # rock falling
        while True:
            direction = wind[wind_idx]
            wind_idx = (wind_idx + 1) % len(wind)
            rock_bound = (
                shift_left(rock, rock_bound, cols)
                if direction == "<"
                else shift_right(rock, rock_bound, cols)
            )
            if not (rock_bound := shift_down(rock, rock_bound, cols)):
                break

        new_abyss, top_shape = inverse(inverse_bfs(cols), cols)

        if new_abyss:
            abyss += new_abyss
            cols = list(map(list, top_shape))

        peak.append(highest_peak(cols) + abyss - 1)

        next_state = (turn + 1) % len(ROCKS), wind_idx, top_shape
        cycle_detector[state] = (turn, next_state)

        if next_state in cycle_detector:
            cycle_start = cycle_detector[next_state][0]
            cycle_len = turn - (cycle_start - 1)
            cycle_peak_gain = (
                peak[turn] - peak[cycle_start - 1] if cycle_start > 0 else peak[turn]
            )
            cycle_count = (turns - cycle_start) // cycle_len
            cycle_final_pos = (turns - cycle_start) % cycle_len + cycle_start

            # Honestly not sure why a -1 is required here
            # as I think I've prevented off-by-one error
            # in one of the previous step but it is how it is
            return cycle_peak_gain * cycle_count + peak[cycle_final_pos] - 1

    return highest_peak(cols) + abyss - 1


print(f"Part 1: {day_17(2022)}")
print(f"Part 2: {day_17(10**12)}")


# Legacy code, is faster for part 1 but astronomically slower for part 2 (probably years)
"""def part_1():
    TURNS = 2022

    with open(INPUT) as file:
        wind = file.readline()[:-1]

    cols = [[1] for _ in range(COLS)]
    wind_idx = 0
    for turn in range(TURNS):
        # spawn new rock
        rock, rock_bound = spawn_rock(turn, cols)

        # rock falling
        while True:
            direction = wind[wind_idx]
            wind_idx = (wind_idx + 1) % len(wind)
            rock_bound = (
                shift_left(rock, rock_bound, cols)
                if direction == "<"
                else shift_right(rock, rock_bound, cols)
            )
            if not (rock_bound := shift_down(rock, rock_bound, cols)):
                break

    return highest_peak(cols) - 1
print(f"{part_1() = }")"""
