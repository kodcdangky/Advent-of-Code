def parse_data(raw: str):
    return list(map(lambda pattern: pattern.splitlines(), raw.split("\n\n")))


def part_1(data: list[list[str]]):
    def pattern_summary(pattern: list[str]) -> int:
        def find_sym_line(pattern: list[str]) -> int:
            for indx in range(1, len(pattern)):
                if all(top == bottom
                       for top, bottom in zip(reversed(pattern[:indx]), pattern[indx:])):
                    return indx
            return 0

        transposed_pattern = list("".join(row[indx] for row in pattern)
                                  for indx in range(len(pattern[0])))
        return 100 * find_sym_line(pattern) or find_sym_line(transposed_pattern)

    return sum(pattern_summary(pattern) for pattern in data)


def part_2(data: list[list[str]]):
    def pattern_summary(pattern: list[str]) -> int:
        def find_sym_line(pattern: list[str]) -> int:
            for indx in range(1, len(pattern)):
                found = False
                for top, btm in zip(reversed(pattern[:indx]), pattern[indx:]):
                    if top != btm:
                        if (not found
                                and sum(top_char != btm_char for top_char, btm_char in zip(top, btm)) == 1):
                            found = True
                        else:
                            break
                else:
                    if found:
                        return indx
            return 0

        transposed_pattern = list("".join(row[indx] for row in pattern)
                                  for indx in range(len(pattern[0])))
        return 100 * find_sym_line(pattern) or find_sym_line(transposed_pattern)

    return sum(pattern_summary(pattern) for pattern in data)


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(parse_data(raw)))
    print(part_2(parse_data(raw)))


if __name__ == "__main__":
    main()
