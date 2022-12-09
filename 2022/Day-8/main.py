### https://adventofcode.com/2022/day/8

INPUT = "input.txt"


def part_1():
    with open(INPUT) as file:
        forest = [
            list(map(lambda tree: int(tree), row))
            for row in map(lambda row: list(row), file.read().splitlines())
        ]

    visible = len(forest) * 2 + len(forest[0]) + len(forest[-1]) - 4

    for row_indx, row in enumerate(forest[1:-1], start=1):
        for col_indx, tree in enumerate(row[1:-1], start=1):
            # In order, check up, down, left, right
            if any(
                (
                    all(
                        forest[other_row_indx][col_indx] < tree
                        for other_row_indx in range(row_indx)
                    ),
                    all(
                        forest[other_row_indx][col_indx] < tree
                        for other_row_indx in range(row_indx + 1, len(forest))
                    ),
                    all(other < tree for other in forest[row_indx][:col_indx]),
                    all(other < tree for other in forest[row_indx][col_indx + 1 :]),
                )
            ):
                visible += 1

    return visible


def part_2():
    with open(INPUT) as file:
        forest = [
            list(map(lambda tree: int(tree), row))
            for row in map(lambda row: list(row), file.read().splitlines())
        ]

    score = []
    
    for row_indx, row in enumerate(forest[1:-1], start=1):
        for col_indx, tree in enumerate(row[1:-1], start=1):
            # Check up
            for other_row_indx in range(row_indx - 1, -1, -1):
                if forest[other_row_indx][col_indx] >= tree or other_row_indx == 0:
                    view_up = abs(other_row_indx - row_indx)
                    break

            # Check down
            for other_row_indx in range(row_indx + 1, len(forest)):
                if (
                    forest[other_row_indx][col_indx] >= tree
                    or other_row_indx == len(forest) - 1
                ):
                    view_down = abs(other_row_indx - row_indx)
                    break

            # Check left
            for other_col_indx in range(col_indx - 1, -1, -1):
                if row[other_col_indx] >= tree or other_col_indx == 0:
                    view_left = abs(other_col_indx - col_indx)
                    break

            # Check right
            for other_col_indx in range(col_indx + 1, len(row)):
                if (
                    row[other_col_indx] >= tree
                    or other_col_indx == len(row) - 1
                ):
                    view_right = abs(other_col_indx - col_indx)
                    break

            score.append(view_up * view_down * view_left * view_right)

    return max(score)


print(f"{part_1() = }")
print(f"{part_2() = }")
