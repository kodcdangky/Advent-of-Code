def parse_data(raw: str):
    return raw.splitlines()


def part_1(data: list[str]):
    return part_2(data, 2)


# Not very space efficient but it does the job
def part_2(data: list[str], expand_factor: int):
    def count_empty(start: int, end: int, row: bool) -> int:
        from bisect import bisect

        min_indx, max_indx = min(start, end), max(start, end)
        dimen = (row and empty_rows) or empty_cols
        return bisect(dimen, max_indx) - bisect(dimen, min_indx)

    transposed_data = list("".join(row[col_indx] for row in data)
                           for col_indx in range(len(data[0])))

    empty_rows = list(row_indx for row_indx, row in enumerate(data)
                      if "#" not in row)
    empty_cols = list(col_indx for col_indx, col in enumerate(transposed_data)
                      if "#" not in col)

    galaxies = list((row_indx, col_indx)
                    for row_indx, row in enumerate(data)
                    for col_indx, char in enumerate(row)
                    if char == "#")

    return sum((abs(row - other_row) + abs(col - other_col)
                + (expand_factor - 1) * (count_empty(row, other_row, True) + count_empty(col, other_col, False)))
               for indx, (row, col) in enumerate(galaxies[:-1])
               for (other_row, other_col) in galaxies[indx + 1:])


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(parse_data(raw)))
    print(part_2(parse_data(raw), 1_000_000))


if __name__ == "__main__":
    main()
