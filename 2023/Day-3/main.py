from itertools import product


def find_numbers(lines: list[str]):
    numbers_pos: list[tuple[int, range]] = []
    for line_indx, line in enumerate(lines):
        start_indx = 0
        while start_indx < len(line):
            if line[start_indx].isdigit():
                end_indx = start_indx + 1
                while end_indx < len(line) and line[start_indx:end_indx + 1].isdigit():
                    end_indx += 1
                numbers_pos.append((line_indx, range(start_indx, end_indx)))
                start_indx = end_indx
            else:
                start_indx += 1
    return numbers_pos


def part_1(lines: list[str]):
    from string import digits

    height, width = len(lines), len(lines[0])
    numbers_pos = find_numbers(lines)

    total = 0
    for number_line, number_range in numbers_pos:
        number = int(lines[number_line][number_range.start:number_range.stop])
        for line_indx, char_indx in product(range(max(0, number_line - 1), min(height, number_line + 2)),
                                            range(max(0, number_range.start - 1), min(width, number_range.stop + 1))):
            if lines[line_indx][char_indx] not in "." + digits:
                total += number
                break
    return total


def part_2(lines: list[str]):
    from math import prod

    def find_asterisks(lines: list[str]):
        return tuple((line_indx, char_indx)
                     for line_indx, line in enumerate(lines)
                     for char_indx, char in enumerate(line)
                     if char == "*")

    height, width = len(lines), len(lines[0])
    asterisks_pos = find_asterisks(lines)
    numbers_pos = find_numbers(lines)
    total = 0
    for a_row, a_col in asterisks_pos:
        adjacents: set[tuple[int, range]] = set()
        for row, col in product(range(max(0, a_row - 1), min(height, a_row + 2)),
                                range(max(0, a_col - 1), min(width, a_col + 2))):
            for number_line, number_range in numbers_pos:
                if row == number_line and col in number_range:
                    adjacents.add((number_line, number_range))
                    break
        if len(adjacents) == 2:
            total += prod(int(lines[number_line][number_range.start:number_range.stop])
                          for number_line, number_range in adjacents)
    return total


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(raw.splitlines()))
    print(part_2(raw.splitlines()))


if __name__ == "__main__":
    main()
