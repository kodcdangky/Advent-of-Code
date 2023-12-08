def parse_data(raw: str) -> tuple[tuple[int, ...], dict[str, tuple[str, ...]]]:
    lines = raw.splitlines()
    path = tuple(map(lambda char: int(char == "R"), lines[0]))

    dirs: dict[str, tuple[str, ...]] = {}
    for line in lines[2:]:
        src, fork = map(lambda part: part.strip(), line.split("="))
        dirs[src] = tuple(
            map(lambda dest: dest.strip(), fork[1:-1].split(","))
        )

    return path, dirs


def part_1(data: tuple[tuple[int, ...], dict[str, tuple[str, ...]]], src: str = "AAA", dest_suff: str = "ZZZ") -> int:
    from itertools import cycle

    path, dirs = data
    pos = src
    for step, turn in enumerate(cycle(path), start=1):
        pos = dirs[pos][turn]
        if pos.endswith(dest_suff):
            return step

    raise Exception("How did we get here?")


def part_2(data: tuple[tuple[int, ...], dict[str, tuple[str, ...]]]) -> int:
    from math import lcm

    return lcm(*map(lambda start: part_1(data, start, "Z"),
                    filter(lambda pos: pos.endswith("A"), data[1].keys())))


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(parse_data(raw)))
    print(part_2(parse_data(raw)))


if __name__ == "__main__":
    main()
