### https://adventofcode.com/2022/day/3

from string import ascii_letters

INPUT = "input.txt"
PRIORITY = list(ascii_letters)


def part_1():
    with open(INPUT) as file:
        rucksacks = file.read().splitlines()

    # prio_sum = 0
    # for sack in rucksacks:
    #     common_item = set(sack[: len(sack) // 2]).intersection(sack[len(sack) // 2 :])

    #     if len(common_item) != 1:
    #         raise ValueError
    #     else:
    #         prio_sum += PRIORITY.index(common_item.pop()) + 1

    prio_sum = sum(
        PRIORITY.index(
            set(sack[: len(sack) // 2]).intersection(sack[len(sack) // 2 :]).pop()
        )
        + 1
        for sack in rucksacks
    )

    print(prio_sum)


def part_2():
    MEMBER_COUNT = 3

    with open(INPUT) as file:
        rucksacks = file.read().splitlines()

    # prio_sum = 0
    # for group in zip(*[iter(rucksacks)] * MEMBER_COUNT, strict=True):
    #     common_item = set(group[0]).intersection(*group[1:])

    #     if len(common_item) != 1:
    #         raise ValueError
    #     else:
    #         prio_sum += PRIORITY.index(common_item.pop()) + 1

    prio_sum = sum(
        PRIORITY.index(set(group[0]).intersection(*group[1:]).pop()) + 1
        for group in zip(*[iter(rucksacks)] * MEMBER_COUNT, strict=True)
    )

    print(prio_sum)


part_1()
part_2()
