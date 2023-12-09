def parse_data(raw: str):
    return list(map(lambda line: list(map(lambda value: int(value.strip()),
                                          line.split())),
                    raw.splitlines()))


def derive(samples: list[int]) -> list[int]:
    return list(map(lambda samples: samples[1] - samples[0], zip(samples[:-1], samples[1:])))


def predict(line: list[int], forward: bool = True) -> int:
    derivative = line
    end_points = derivative[-1:] if forward else derivative[:1]
    while len(set(derivative := derive(derivative))) != 1:
        end_points.append(derivative[-1 * forward])
    trace = derivative[-1 * forward]
    while end_points:
        trace = end_points.pop() + trace if forward else end_points.pop() - trace
    return trace


def part_1(data: list[list[int]]) -> int:
    return sum(map(predict, data))


def part_2(data: list[list[int]]) -> int:
    return sum(map(lambda line: predict(line, False), data))


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(parse_data(raw)))
    print(part_2(parse_data(raw)))


if __name__ == "__main__":
    main()
