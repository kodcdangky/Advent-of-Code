### https://adventofcode.com/2022/day/4

INPUT = "input.txt"


def part_1():
    with open(INPUT) as file:
        pairs = map(lambda pair: pair.split(","), file.read().splitlines())

    count = 0
    for pair in pairs:
        elf_0 = tuple(map(lambda sect: int(sect), pair[0].split("-")))
        elf_1 = tuple(map(lambda sect: int(sect), pair[1].split("-")))

        if any(
            (
                elf_0[0] >= elf_1[0] and elf_0[1] <= elf_1[1],
                elf_1[0] >= elf_0[0] and elf_1[1] <= elf_0[1],
            ),
        ):
            count += 1

    print(count)


def part_2():
    with open(INPUT) as file:
        pairs = map(lambda pair: pair.split(","), file.read().splitlines())

    count = 0
    for pair in pairs:
        elf_0 = tuple(map(lambda sect: int(sect), pair[0].split("-")))
        elf_1 = tuple(map(lambda sect: int(sect), pair[1].split("-")))

        if any(
            (
                elf_1[0] <= elf_0[0] <= elf_1[1],
                elf_1[0] <= elf_0[1] <= elf_1[1],
                elf_0[0] <= elf_1[0] <= elf_0[1],
                elf_0[0] <= elf_1[1] <= elf_0[1],
            )
        ):
            count += 1

    print(count)


part_1()
part_2()
