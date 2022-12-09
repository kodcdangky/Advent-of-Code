### https://adventofcode.com/2022/day/5
from itertools import zip_longest
from fnmatch import fnmatch

INPUT = "input.txt"


def parse_columns(lines: list):
    lines.reverse()
    cols = [[] for _ in range(len(lines[0]) // 4 + 1)]

    for line in lines[1:]:
        for index, batch in enumerate(zip_longest(*[iter(line)] * 4)):
            if batch[1] != " ":
                cols[index].append(batch[1])

    return cols


def parse_instruction(inst_line: str):
    if fnmatch(inst_line, "move * from * to *"):
        words = inst_line.split(" ")
        if all((words[1].isdigit(), words[3].isdigit(), words[5].isdigit())):
            return int(words[1]), int(words[3]) - 1, int(words[5]) - 1


def parse_input(lines: list):
    separator = lines.index("")

    cols = parse_columns(lines[:separator])
    instructions = map(parse_instruction, lines[separator + 1 :])
    return cols, instructions


def part_1():
    with open(INPUT) as file:
        cols, instructions = parse_input(file.read().splitlines())

    for inst in instructions:
        amount, source, dest = inst
        for _ in range(amount):
            cols[dest].append(cols[source].pop())

    print("".join(col[-1] for col in cols))


def part_2():
    with open(INPUT) as file:
        cols, instructions = parse_input(file.read().splitlines())

    for inst in instructions:
        amount, source, dest = inst
        cols[dest].extend(cols[source][-amount:])
        cols[source] = cols[source][:-amount]

    print("".join(col[-1] for col in cols))


part_1()
part_2()
