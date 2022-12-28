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
) -> tuple[tuple[tuple[int]], tuple[int]]:
    peak, height = highest_peak(cols)
    cols[peak].extend([0] * abs(min(0, len(cols[peak]) - height - (FALL_SPACE + 1))))
    for col in cols:
        col.extend([0] * (len(cols[peak]) - len(col)))

    rock_height, base_rock = ROCKS[turn % len(ROCKS)]
    rock = []
    rock.extend((((0,) * rock_height) for _ in range(LEFT_MARGIN)))
    rock.extend(base_rock)
    rock.extend(
        (((0,) * rock_height) for _ in range(len(cols) - len(base_rock) - LEFT_MARGIN))
    )

    for col, rock_col in zip(cols, rock):
        col[height + 4 :] = rock_col

    up = len(cols[0])
    down = len(cols[0]) - rock_height
    left = LEFT_MARGIN
    right = LEFT_MARGIN + len(base_rock)

    return base_rock, (up, down, left, right)


def erase(rock: list[list[int]], bound: tuple[int], cols: list[list[int]]) -> None:
    up, down, left, right = bound
    for rock_col, col in zip(rock, range(left, right)):
        for rock_cell, row in zip(rock_col, range(down, up)):
            if rock_cell:
                cols[col][row] = 0


def draw(rock: list[list[int]], bound: tuple[int], cols: list[list[int]]) -> None:
    up, down, left, right = bound
    for rock_col, col in zip(rock, range(left, right)):
        for rock_cell, row in zip(rock_col, range(down, up)):
            cols[col][row] = rock_cell or cols[col][row]


def shift_left(
    rock: list[list[int]], bound: tuple[int], cols: list[list[int]]
) -> tuple[int]:
    up, down, left, right = bound
    erase(rock, bound, cols)

    if left == 0:
        draw(rock, bound, cols)
        return bound

    for rock_col, col in zip(rock, range(left - 1, right - 1)):
        for rock_cell, row in zip(rock_col, range(down, up)):
            if cols[col][row] + rock_cell > 1:
                draw(rock, bound, cols)
                return bound

    new_bound = up, down, left - 1, right - 1
    draw(rock, new_bound, cols)
    return new_bound


def shift_right(
    rock: list[list[int]], bound: tuple[int], cols: list[list[int]]
) -> tuple[int]:
    up, down, left, right = bound

    erase(rock, bound, cols)
    if right == len(cols):
        draw(rock, bound, cols)
        return bound

    for rock_col, col in zip(rock, range(left + 1, right + 1)):
        for rock_cell, row in zip(rock_col, range(down, up)):
            if cols[col][row] + rock_cell > 1:
                draw(rock, bound, cols)
                return bound

    new_bound = up, down, left + 1, right + 1
    draw(rock, new_bound, cols)
    return new_bound


def shift_down(rock: list[list[int]], bound: tuple[int], cols: list[list[int]]) -> bool:
    up, down, left, right = bound

    erase(rock, bound, cols)
    if down == 0:
        draw(rock, bound, cols)
        return

    for rock_col, col in zip(rock, range(left, right)):
        for rock_cell, row in zip(rock_col, range(down - 1, up - 1)):
            if cols[col][row] + rock_cell > 1:
                draw(rock, bound, cols)
                return

    new_bound = up - 1, down - 1, left, right
    draw(rock, new_bound, cols)
    return new_bound


def highest_peak(cols: list[list[int]]) -> tuple[int]:
    reversed_cols = [reversed(col) for col in cols]
    for height, all_cols in enumerate(zip(*reversed_cols), start=1):
        for indx, cell in enumerate(all_cols):
            if cell:
                return indx, len(cols[indx]) - height
    return 0, -1


def part_1():
    TURNS = 2022

    with open(INPUT) as file:
        wind = file.readline()[:-1]

    cols = [[] for _ in range(COLS)]
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

    return highest_peak(cols)[1] + 1


def part_2():
    TURNS = 1_000_000_000_000

    with open(INPUT) as file:
        wind = file.readline()[:-1]

    cols = [[] for _ in range(COLS)]
    wind_idx = 0
    states = {}
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



print(f"{part_1() = }")
print(f"{part_2() = }")
