### https://adventofcode.com/2022/day/6

INPUT = "input.txt"


def part_1():
    N = 4

    with open(INPUT) as file:
        stream = file.read()

    for index in range(N, len(stream)):
        if len(set(stream[index - N : index])) == N:
            print(index)
            return


def part_2():
    N = 14

    with open(INPUT) as file:
        stream = file.read()

    for index in range(N, len(stream)):
        if len(set(stream[index - N : index])) == N:
            print(index)
            return


part_1()
part_2()
