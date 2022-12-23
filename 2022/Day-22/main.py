### https://adventofcode.com/2022/day/22

INPUT = "input.txt"
ORIENT = ((0, 1), (1, 0), (0, -1), (-1, 0))
TURN = {
    "R": lambda orient: (orient + 1) % len(ORIENT),
    "L": lambda orient: (orient - 1) % len(ORIENT),
}
START = (0, 0)
START_ORIENT = START_SIDE = 0
WALL = "#"


def parse_instruction(instr_txt: str):
    instruction = []
    new_seg = 0
    for idx, char in enumerate(instr_txt):
        if char.isalpha():
            instruction.append(int(instr_txt[new_seg:idx]))
            instruction.append(char)
            new_seg = idx + 1
    if new_seg < len(instr_txt):
        instruction.append(int(instr_txt[new_seg:]))
    return instruction


def part_1():
    def move(
        origin: tuple[int, int],
        orient: int,
        step: int,
        board: tuple[tuple[int, str]],
    ) -> tuple[int, int]:

        row, col = origin
        r_orient, c_orient = ORIENT[orient]
        if c_orient:
            for _ in range(step):
                new_col = (col + c_orient) % len(board[row][1])

                if board[row][1][new_col] != WALL:
                    col = new_col
                else:
                    break
        else:
            for _ in range(step):
                new_row = (row + r_orient) % len(board)

                while (col + board[row][0] - board[new_row][0]) not in range(
                    len(board[new_row][1])
                ):
                    new_row = (new_row + r_orient) % len(board)

                new_col = col + board[row][0] - board[new_row][0]
                if board[new_row][1][new_col] != WALL:
                    row = new_row
                    col = new_col
                else:
                    break

        return row, col

    with open(INPUT) as file:
        board, instr_txt = file.read().split("\n\n")

    board = tuple(
        map(
            lambda line: (len(line) - len(line.lstrip()), line.lstrip()),
            board.splitlines(),
        )
    )

    instruction = parse_instruction(instr_txt)

    row, col = START
    orient = START_ORIENT
    for step in instruction:
        if isinstance(step, str):
            orient = TURN[step](orient)
        else:
            row, col = move((row, col), orient, step, board)

    return 1000 * (row + 1) + 4 * (board[row][0] + col + 1) + orient


# one of the most surreal code writing experience ive had
# dont ask what things do they just work
# (traveling logic works for general cases, but cube assembly is made specifically just for example and input)
def part_2():
    class Side:
        def __init__(
            self, board: tuple[str], right: int, down: int, left: int, up: int
        ) -> None:
            self.board = board
            self.adjacents = (right, down, left, up)

    def cross(side: int, row: int, col: int, orient: int) -> tuple[int, ...]:
        new_side = sides[side].adjacents[orient]
        new_orient = (sides[new_side].adjacents.index(side) + 2) % 4

        if new_orient in (0, 2):
            new_col = 0 if new_orient == 0 else CUBE_EDGE - 1
            if orient in (0, 2):
                new_row = row if orient == new_orient else CUBE_EDGE - 1 - row
            else:
                new_row = (
                    col
                    if (orient, new_orient) in ((1, 2), (3, 0))
                    else CUBE_EDGE - 1 - col
                )

        else:
            new_row = 0 if new_orient == 1 else CUBE_EDGE - 1
            if orient in (1, 3):
                new_col = col if orient == new_orient else CUBE_EDGE - 1 - col
            else:
                new_col = (
                    row
                    if (orient, new_orient) in ((2, 1), (0, 3))
                    else CUBE_EDGE - 1 - row
                )

        return new_side, new_row, new_col, new_orient

    def move(
        side: int,
        origin: tuple[int, int],
        orient: int,
        step: int,
    ) -> tuple[int, ...]:

        coord = list(origin)
        row, col = coord
        facing = ORIENT[orient]
        axis = abs(facing[1])
        for _ in range(step):
            coord[axis] += facing[axis]
            if coord[axis] not in range(CUBE_EDGE):
                new_side, coord[0], coord[1], new_orient = cross(side, row, col, orient)
            else:
                new_side = side
                new_orient = orient
            if sides[new_side].board[coord[0]][coord[1]] == WALL:
                break
            else:
                side = new_side
                orient = new_orient
                row, col = coord
                facing = ORIENT[orient]
                axis = abs(facing[1])

        return side, row, col, orient

    side_maps = [[] for _ in range(6)]
    with open(INPUT) as file:
        board, instr_txt = file.read().split("\n\n")

    board = board.splitlines()
    board_map = []
    # Input cube assembly
    CUBE_EDGE = 50
    for line in board[:CUBE_EDGE]:
        line = line.strip()
        side_maps[0].append(line[:CUBE_EDGE])
        side_maps[1].append(line[CUBE_EDGE:])
    board_map.append((0, len(board[0]) - len(board[0].strip())))
    board_map.append((0, len(board[0]) - len(board[0].strip()) + CUBE_EDGE))

    for line in board[CUBE_EDGE : CUBE_EDGE * 2]:
        line = line.strip()
        side_maps[2].append(line[:CUBE_EDGE])
    board_map.append((CUBE_EDGE, len(board[CUBE_EDGE]) - len(board[CUBE_EDGE].strip())))

    for line in board[CUBE_EDGE * 2 : CUBE_EDGE * 3]:
        line = line.strip()
        side_maps[3].append(line[:CUBE_EDGE])
        side_maps[4].append(line[CUBE_EDGE:])
    board_map.append(
        (CUBE_EDGE * 2, len(board[CUBE_EDGE * 2]) - len(board[CUBE_EDGE * 2].strip()))
    )
    board_map.append(
        (
            CUBE_EDGE * 2,
            len(board[CUBE_EDGE * 2]) - len(board[CUBE_EDGE * 2].strip()) + CUBE_EDGE,
        )
    )

    for line in board[CUBE_EDGE * 3 :]:
        line = line.strip()
        side_maps[5].append(line[:CUBE_EDGE])
    board_map.append(
        (CUBE_EDGE * 3, len(board[CUBE_EDGE * 3]) - len(board[CUBE_EDGE * 3].strip()))
    )

    sides = [
        Side(tuple(side_maps[0]), 1, 2, 3, 5),
        Side(tuple(side_maps[1]), 4, 2, 0, 5),
        Side(tuple(side_maps[2]), 1, 4, 3, 0),
        Side(tuple(side_maps[3]), 4, 5, 0, 2),
        Side(tuple(side_maps[4]), 1, 5, 3, 2),
        Side(tuple(side_maps[5]), 4, 1, 0, 3),
    ]

    # Example cube assembly
    # CUBE_EDGE = 4
    # for line in board[:CUBE_EDGE]:
    #     line = line.strip()
    #     side_maps[0].append(line[:CUBE_EDGE])
    # board_map.append((0, len(board[0]) - len(board[0].strip())))

    # for line in board[CUBE_EDGE : CUBE_EDGE * 2]:
    #     line = line.strip()
    #     side_maps[1].append(line[:CUBE_EDGE])
    #     side_maps[2].append(line[CUBE_EDGE : CUBE_EDGE * 2])
    #     side_maps[3].append(line[CUBE_EDGE * 2 : CUBE_EDGE * 3])
    # board_map.append((CUBE_EDGE, len(board[CUBE_EDGE]) - len(board[CUBE_EDGE].strip())))
    # board_map.append((CUBE_EDGE, len(board[CUBE_EDGE]) - len(board[CUBE_EDGE].strip()) + CUBE_EDGE))
    # board_map.append((CUBE_EDGE, len(board[CUBE_EDGE]) - len(board[CUBE_EDGE].strip()) + CUBE_EDGE * 2))

    # for line in board[CUBE_EDGE * 2 :]:
    #     line = line.strip()
    #     side_maps[4].append(line[:CUBE_EDGE])
    #     side_maps[5].append(line[CUBE_EDGE : CUBE_EDGE * 2])
    # board_map.append((CUBE_EDGE * 2, len(board[CUBE_EDGE * 2]) - len(board[CUBE_EDGE * 2].strip())))
    # board_map.append((CUBE_EDGE * 2, len(board[CUBE_EDGE * 2]) - len(board[CUBE_EDGE * 2].strip()) + CUBE_EDGE))

    # sides = [
    #     Side(tuple(side_maps[0]), 5, 3, 2, 1),
    #     Side(tuple(side_maps[1]), 2, 4, 5, 0),
    #     Side(tuple(side_maps[2]), 3, 4, 1, 0),
    #     Side(tuple(side_maps[3]), 5, 4, 2, 0),
    #     Side(tuple(side_maps[4]), 5, 1, 2, 3),
    #     Side(tuple(side_maps[5]), 0, 1, 4, 3),
    # ]

    instruction = parse_instruction(instr_txt)

    side = START_SIDE
    row, col = START
    orient = START_ORIENT
    for step in instruction:
        if isinstance(step, str):
            orient = TURN[step](orient)
        else:
            side, row, col, orient = move(side, (row, col), orient, step)

    return (
        1000 * (board_map[side][0] + row + 1)
        + 4 * (board_map[side][1] + col + 1)
        + orient
    )


print(f"{part_1() = }")
print(f"{part_2() = }")
