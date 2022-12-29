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
    for height, row in enumerate(zip(*reversed_cols), start=1):
        for col_idx, cell in enumerate(row):
            if cell:
                return col_idx, len(cols[col_idx]) - height
    return 0, -1


def is_plane(cols: list[list[int]]) -> bool:
    reversed_cols = [reversed(col) for col in cols]
    for row in zip(*reversed_cols):
        if set(row) == {1}:
            return True
        elif set(row) == {0, 1}:
            return False


def part_1():
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

    return highest_peak(cols)[1]


def part_2():
    def inverse_bfs(cols: list[list[int]]):
        if len(cols[0]) <= highest_peak(cols)[1] + 1:
            for col in cols:
                col.append(0)

        c_bound = range(len(cols))
        r_bound = range(len(cols[0]))

        flooded = [(0, len(cols[0]) - 1)]
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
        peak = highest_peak(cols)[1]
        top_shape = tuple(tuple(col[abyss : peak + 1]) for col in cols)
        return abyss, top_shape

    TURNS = 10**12
    FIRST_STATE = (0, 0, (1,) * 7)

    with open(INPUT) as file:
        wind = file.readline()[:-1]

    cols = [[1] for _ in range(COLS)]
    wind_idx = 0
    states = {}
    top_shape = (1,) * 7
    abyss = 0
    for turn in range(TURNS):
        state = turn % len(ROCKS), wind_idx, top_shape
        if state in states:
            new_abyss, wind_idx, top_shape = states[state]
            abyss += new_abyss
            cols = list(map(list, top_shape))
        else:
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
            states[state] = new_abyss, wind_idx, top_shape

            if new_abyss:
                abyss += new_abyss
                cols = list(map(list, top_shape))
        if turn != 0 and state == FIRST_STATE:
            print(f"CYCLE FOUND!: AT TURN {turn} FROM 0")
            return
        if turn % 10**9 == 0:
            print(f"{turn} * 10**9")

    return highest_peak(cols)[1] + abyss


print(f"{part_1() = }")
print(f"{part_2() = }")
