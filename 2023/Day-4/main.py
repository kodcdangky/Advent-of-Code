def parse_data(lines: list[str]) -> list[list[list[int]]]:
    all_tickets: list[list[list[int]]] = []
    for line in lines:
        _, details = map(lambda part: part.strip(), line.split(":"))
        winning_str, numbers_str = map(lambda part: part.strip(),
                                       details.split("|"))

        winning = list(map(lambda number: int(number.strip()),
                           winning_str.split()))
        numbers = list(map(lambda number: int(number.strip()),
                           numbers_str.split()))

        all_tickets.append([winning, numbers])
    return all_tickets


def part_1(tickets: list[list[list[int]]]) -> int:
    return sum(int(2 ** (sum(number in winning for number in numbers) - 1)) for winning, numbers in tickets)


def part_2(tickets: list[list[list[int]]]) -> int:
    tickets_quant = [1] * len(tickets)
    for indx, (winning, numbers) in enumerate(tickets):
        for other in range(indx + 1,
                           min(len(tickets), indx + 1 + sum(number in winning for number in numbers))):
            tickets_quant[other] += tickets_quant[indx]

    return sum(tickets_quant)


def main():
    with open("input.txt") as file:
        raw = file.read()
    print(part_1(parse_data(raw.splitlines())))
    print(part_2(parse_data(raw.splitlines())))


if __name__ == "__main__":
    main()
