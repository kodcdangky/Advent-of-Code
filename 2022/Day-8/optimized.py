def main():
    with open("test.txt") as f:
        forest = [line[:- 1] for line in f]
    no_row, no_col = len(forest), len(forest[0])
    score = [[1 for i in range(no_col)] for i in range(no_row)]

    def valid(row, col):
        return row >= 0 and col >= 0 and row < no_row and col < no_col

    def iterate(row, col, step):
        # step: [xstep, ystep]
        stack = [[10, 0]]
        i = 0

        while valid(row, col):

            while stack[-1][0] < int(forest[row][col]):
                stack.pop()

            score[row][col] *= i - stack[-1][1]

            stack.append([int(forest[row][col]), i])

            row, col, i = row + step[0], col + step[1], i + 1

    for i in range(no_row):
        iterate(i, 0, [0, 1])
        iterate(i, no_col - 1, [0, -1])

    for i in range(no_col):
        iterate(0, i, [1, 0])
        iterate(no_row - 1, i, [-1, 0])

    print(max([max(score[i]) for i in range(no_row)]))


main()
