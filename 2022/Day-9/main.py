### https://adventofcode.com/2022/day/9

INPUT = "input.txt"


def day_9(notches: int) -> int:
    with open(INPUT) as file:
        instructions = map(
            lambda move: (move[0], int(move[1])),
            map(lambda line: line.split(" "), file.read().splitlines()),
        )

    visited = set()

    rope = [[0, 0] for _ in range(notches)]
    head = rope[0]
    tail = rope[-1]

    visited.add(tuple(tail))

    for move in instructions:
        axis = 0 if move[0] in ("U", "D") else 1
        direction = -1 if move[0] in ("U", "L") else 1

        for _ in range(move[1]):
            head[axis] += direction

            for prev_notch, notch in zip(rope, rope[1:]):
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
                visited.add(tuple(tail))

    return len(visited)


print(f"Part 1: {day_9(2)}")
print(f"Part 2: {day_9(10)}")
