def parse_data(raw: str):
    return list(map(lambda line: list(line), raw.splitlines()))


def part_1(data: list[list[str]]):
    return part_2(data, 2)


# Not very time or space efficient but it does the job
def part_2(data: list[list[str]], expand_factor: int):
    def count_empty_rows(start_row: int, end_row: int) -> int:
        min_row, max_row = min(start_row, end_row), max(start_row, end_row)
        return sum("#" not in data[row] for row in range(min_row + 1, max_row + 1))

    def count_empty_cols(start_col: int, end_col: int) -> int:
        min_col, max_col = min(start_col, end_col), max(start_col, end_col)
        return sum("#" not in transposed_data[col] for col in range(min_col + 1, max_col + 1))

    transposed_data = list(list(row[col_indx] for row in data)
                           for col_indx, _ in enumerate(data[0]))

    galaxies = list((row_indx, col_indx)
                    for row_indx, row in enumerate(data)
                    for col_indx, char in enumerate(row)
                    if char == "#")

    return sum((abs(row - other_row) + abs(col - other_col)
                + (expand_factor - 1) * (count_empty_rows(row, other_row) + count_empty_cols(col, other_col)))
               for indx, (row, col) in enumerate(galaxies[:-1])
               for (other_row, other_col) in galaxies[indx + 1:])


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(parse_data(raw)))
    print(part_2(parse_data(raw), 1_000_000))


if __name__ == "__main__":
    main()
