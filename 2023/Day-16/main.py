from enum import Enum

EMPTY = "."

MIRROR = "/"
MIRROR_ALT = "\\"

SPLIT_H = "-"
SPLIT_V = "|"


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


UP = Direction.UP
DOWN = Direction.DOWN
LEFT = Direction.LEFT
RIGHT = Direction.RIGHT


def parse_data(raw: str):
    return raw.splitlines()


def simulate_light(grid: list[str], start: tuple[int, int], heading: Direction):
    from collections import deque

    def append_beam(beams_next: dict[Direction, deque[tuple[int, int]]],
                    row: int, col: int, direction: Direction):
        beams_next[direction].append(
            (row + direction.value[0], col + direction.value[1])
        )

    width, height = len(grid[0]), len(grid)
    energized: set[tuple[int, int]] = set()
    beams_next: dict[Direction, deque[tuple[int, int]]] = {UP: deque(), DOWN: deque(),
                                                           LEFT: deque(),  RIGHT: deque()}
    beams_next[heading].append(start)

    while any(beams_next.values()):
        for direction in filter(lambda direction: beams_next[direction], beams_next):
            row, col = beams_next[direction].popleft()
            if row in range(width) and col in range(height):
                # Empties and Mirrors can be considered indiscriminately as the
                # only true repeat beams through them are caused by splitters
                # merging, which is prevented when coming across splitters
                if grid[row][col] == EMPTY:
                    append_beam(beams_next, row, col, direction)

                elif grid[row][col] in (MIRROR, MIRROR_ALT):
                    if grid[row][col] == MIRROR:
                        dir_group = ((UP, RIGHT) if direction in (UP, RIGHT)
                                     else (DOWN, LEFT))
                    else:
                        dir_group = ((UP, LEFT) if direction in (UP, LEFT)
                                     else (DOWN, RIGHT))

                    next_direction = dir_group[not dir_group.index(direction)]
                    append_beam(beams_next, row, col, next_direction)

                # Splitters are only considered if they aren't already energized,
                # as any beam energizing a splitter initially automatically
                # energizes all paths leading from that splitter immediately
                elif (row, col) not in energized:
                    if grid[row][col] == SPLIT_H:
                        if direction in (UP, DOWN):
                            append_beam(beams_next, row, col, LEFT)
                            append_beam(beams_next, row, col, RIGHT)
                        else:
                            append_beam(beams_next, row, col, direction)

                    elif grid[row][col] == SPLIT_V:
                        if direction in (LEFT, RIGHT):
                            append_beam(beams_next, row, col, UP)
                            append_beam(beams_next, row, col, DOWN)
                        else:
                            append_beam(beams_next, row, col, direction)

                energized.add((row, col))

    return len(energized)


def part_1(data: list[str]):
    return simulate_light(data, (0, 0), RIGHT)


def part_2(data: list[str]):
    borders = (
        ((0, col) for col in range(len(data[0]))),
        ((row, len(data[0]) - 1) for row in range(len(data))),
        ((len(data) - 1, col) for col in range(len(data[0]))),
        ((row, 0) for row in range(len(data)))
    )
    headings = (DOWN, LEFT, UP, RIGHT)

    # if grid is rectangle, using zip_longest(*borders, fillvalue=(-1, -1))
    # then filtering out (-1, -1) as a starting value in simulate_light would be needed
    return max(simulate_light(data, start, heading)
               for starts in zip(*borders)
               for start, heading in zip(starts, headings))


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(parse_data(raw)))
    print(part_2(parse_data(raw)))


if __name__ == "__main__":
    main()
