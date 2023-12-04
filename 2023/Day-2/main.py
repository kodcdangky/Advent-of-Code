def parse_data(raw: str) -> list[list[list[int]]]:
    INDEX = {"red": 0, "green": 1, "blue": 2}

    def parse_line(line: str):
        _, turns = map(lambda part: part.strip(), line.split(":"))

        parsed_line: list[list[int]] = []

        for stage in map(lambda part: part.strip(), turns.split(";")):
            pull = [0, 0, 0]
            for ball in map(lambda part: part.strip(), stage.split(",")):
                quant, color = ball.split()
                pull[INDEX[color]] = int(quant)
            parsed_line.append(pull)
        return parsed_line

    return list(map(parse_line, raw.splitlines()))


def part_1(games: list[list[list[int]]]) -> int:
    MAX_RGB = (12, 13, 14)

    def is_possible(game: tuple[int, list[list[int]]]) -> bool:
        return all(map(lambda rgb: all(color <= max_color for color, max_color in zip(rgb, MAX_RGB)), game[1]))

    return sum(indx for indx, _ in filter(is_possible, enumerate(games, start=1)))


def part_2(games: list[list[list[int]]]) -> int:
    from math import prod
    return sum(map(lambda stages: prod(map(max, zip(*stages))), games))


def main():
    with open("input.txt") as file:
        games = parse_data(file.read())
    print(part_1(games))
    print(part_2(games))


if __name__ == "__main__":
    main()
