### https://adventofcode.com/2022/day/9

INPUT = "input.txt"


def new_board(instructions: tuple) -> tuple[list[list[bool]], list[int]]:
    edges = {"U": 0, "D": 0, "L": 0, "R": 0}
    head = [0, 0]
    for move in instructions:
        axis = 0 if move[0] in ("U", "D") else 1
        direction = -1 if move[0] in ("U", "L") else 1

        head[axis] += move[1] * direction
        if axis == 0:
            edges["U"] = min(edges["U"], head[0])
            edges["D"] = max(edges["D"], head[0])
        else:
            edges["L"] = min(edges["L"], head[1])
            edges["R"] = max(edges["R"], head[1])

    return [
        [False for _ in range(edges["L"], edges["R"] + 1)]
        for _ in range(edges["U"], edges["D"] + 1)
    ], [abs(edges["U"]), abs(edges["L"])]


def part_1() -> int:
    with open(INPUT) as file:
        instructions = tuple(
            map(
                lambda move: (move[0], int(move[1])),
                map(lambda line: line.split(" "), file.read().splitlines()),
            )
        )

    visited, head = new_board(instructions)
    tail = head.copy()

    visited[tail[0]][tail[1]] = True

    for move in instructions:
        axis = 0 if move[0] in ("U", "D") else 1
        direction = -1 if move[0] in ("U", "L") else 1

        for _ in range(move[1]):
            head[axis] += direction
            dist = head[0] - tail[0], head[1] - tail[1]

            if 2 in (abs(dist[0]), abs(dist[1])):

                if dist[0]:
                    tail[0] += dist[0] // abs(dist[0])

                if dist[1]:
                    tail[1] += dist[1] // abs(dist[1])

                visited[tail[0]][tail[1]] = True

    return sum(map(lambda row: sum(row), visited))


def part_2() -> int:
    NOTCHES = 10

    with open(INPUT) as file:
        instructions = tuple(
            map(
                lambda move: (move[0], int(move[1])),
                map(lambda line: line.split(" "), file.read().splitlines()),
            )
        )

    visited, start = new_board(instructions)

    rope = [start.copy() for _ in range(NOTCHES)]
    head = rope[0]
    tail = rope[-1]

    visited[tail[0]][tail[1]] = True

    for move in instructions:
        axis = 0 if move[0] in ("U", "D") else 1
        direction = -1 if move[0] in ("U", "L") else 1

        for _ in range(move[1]):
            head[axis] += direction

            for indx, notch in enumerate(rope[1:], start=1):
                prev_notch = rope[indx - 1]
                dist = prev_notch[0] - notch[0], prev_notch[1] - notch[1]

                # check if current notch have to move
                if 2 in (abs(dist[0]), abs(dist[1])):

                    if dist[0]:
                        notch[0] += dist[0] // abs(dist[0])

                    if dist[1]:
                        notch[1] += dist[1] // abs(dist[1])

                else:
                    break
            else:
                visited[tail[0]][tail[1]] = True

    return sum(map(lambda row: sum(row), visited))


print(f"{part_1() = }")
print(f"{part_2() = }")
