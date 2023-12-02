def parse_data(raw: str):
    INDEX = {"red": 0, "green": 1, "blue": 2}

    def parse_line(line: str):
        game, turns = map(lambda part: part.strip(), line.split(":"))

        parsed_line: list[int | list[int]] = [int(game.split(" ")[1])]

        for stage in map(lambda part: part.strip(), turns.split(";")):
            pull = [0, 0, 0]
            for ball in map(lambda part: part.strip(), stage.split(",")):
                quant, color = ball.split(" ")
                pull[INDEX[color]] = int(quant)
            parsed_line.append(pull)
        return parsed_line

    return list(map(parse_line, raw.splitlines()))


def part_1(games: list[list[int | list[int]]]):
    MAX_RGB = (12, 13, 14)

    def is_possible(game: list[int | list[int]]):
        return all(map(lambda rgb: all(color <= max_color for color, max_color in zip(rgb, MAX_RGB)), game[1:]))

    return sum(map(lambda game: game[0], filter(is_possible, games)))


def part_2(games: list[list[int | list[int]]]):
    def get_power(stages: list[list[int]]) -> int:
        from math import prod
        return prod(map(max, list(zip(*stages))))

    return sum(map(get_power, map(lambda game: game[1:], games)))


def main():
    with open("input.txt") as file:
        games = parse_data(file.read())
    print(part_1(games))
    print(part_2(games))


if __name__ == "__main__":
    main()
