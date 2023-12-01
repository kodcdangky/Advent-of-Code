def parse_1(line: str) -> int:
    from string import digits

    def filter_find(digit: str) -> int:
        return (line.find(digit) + 1 or len(line) + 1) - 1

    return int(line[min(map(filter_find, digits))] + line[max(map(line.rfind, digits))])


def parse_2(line: str) -> int:
    DIGIT_CHAR = {
        "one": "1", "1": "1",
        "two": "2", "2": "2",
        "three": "3", "3": "3",
        "four": "4", "4": "4",
        "five": "5", "5": "5",
        "six": "6", "6": "6",
        "seven": "7", "7": "7",
        "eight": "8", "8": "8",
        "nine": "9", "9": "9",
    }

    def filter_find(substr: str) -> int:
        return (line.find(substr) + 1 or len(line) + 1) - 1

    return int(DIGIT_CHAR[min(DIGIT_CHAR.keys(), key=filter_find)] + DIGIT_CHAR[max(DIGIT_CHAR.keys(), key=line.rfind)])


def main():
    # Part 1
    with open("input.txt") as file:
        print(sum(map(parse_1, file.read().splitlines())))

    # Part 2
    with open("input.txt") as file:
        print(sum(map(parse_2, file.read().splitlines())))


if __name__ == "__main__":
    main()
