def parse_data(raw: str) -> tuple[tuple[int, int], ...]:
    time, dist = map(lambda part: part.split()[1:], raw.splitlines())
    return tuple(zip(map(lambda value: int(value.strip()), time),
                    map(lambda value: int(value.strip()), dist)))


def part_1(races: tuple[tuple[int, int], ...]):
    result = 1
    for time, record in races:
        for hold_dur in range(time + 1):
            speed = hold_dur
            if speed * (time - hold_dur) > record:
                result *= time + 1 - hold_dur * 2
                break
    return result - 1 and result


def part_2(races: tuple[tuple[int, int], ...]):
    time, record = zip(*races)
    time = int("".join(map(str, time)))
    record = int("".join(map(str, record)))
    return part_1(((time, record),))


def main():
    with open("input.txt") as file:
        raw = file.read()
    print(part_1(parse_data(raw)))
    print(part_2(parse_data(raw)))


if __name__ == "__main__":
    main()
