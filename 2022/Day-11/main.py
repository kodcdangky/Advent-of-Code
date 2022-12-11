### https://adventofcode.com/2022/day/11

import operator
from collections import deque
from fnmatch import fnmatch
from math import prod, lcm

INPUT = "input.txt"


# Ugly code for input parsing
def day_11(rounds, relief_factor):
    OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}


    with open(INPUT) as file:
        pack = map(
            lambda monkey: map(lambda line: line.strip(), monkey),
            map(lambda section: section.splitlines(), file.read().split("\n\n")),
        )

    monkey_info: list[dict[str, deque[int] | tuple[int, str] | list[int]] | int] = []
    for monkey in pack:
        monkey_info.append(
            {"items": deque(), "operation": (), "test": None, "test_result": [-1, -1], "inspected": 0}
        )
        monkey_no = None
        for line in monkey:
            if line.startswith("Monkey"):
                monkey_no = int(line.strip(":").split()[1])

            elif line.startswith("Starting items"):
                items = map(
                    lambda item: int(item.strip(",")), line.split(":")[1].split()
                )
                monkey_info[monkey_no]["items"].extend(items)

            elif line.startswith("Operation"):
                operation = line.split(":")[1].strip()
                if fnmatch(operation, "new = old [+,-,*,/] *"):
                    ops, value = operation.split("=")[1].split()[1:]
                    if value.isdigit():
                        monkey_info[monkey_no]["operation"] = ops, int(value)
                    elif value == "old":
                        monkey_info[monkey_no]["operation"] = ops, value

            elif line.startswith("Test"):
                test = line.split(":")[1].strip()
                if fnmatch(test, "divisible by *"):
                    monkey_info[monkey_no]["test"] = int(test.split()[2])

            elif line.startswith("If true"):
                true = line.split(":")[1].strip()
                if fnmatch(true, "throw to monkey *"):
                    target = int(true.split()[-1])
                    monkey_info[monkey_no]["test_result"][1] = target

            elif line.startswith("If false"):
                false = line.split(":")[1].strip()
                if fnmatch(false, "throw to monkey *"):
                    target = int(false.split()[-1])
                    monkey_info[monkey_no]["test_result"][0] = target

    test_lcm = lcm(*(monkey["test"] for monkey in monkey_info))

    for _ in range(rounds):
        for monkey in monkey_info:
            while monkey["items"]:
                worry = monkey["items"].popleft()
                monkey["inspected"] += 1

                ops, ops_value = monkey["operation"]
                worry = OPS[ops](worry, ops_value if type(ops_value) is int else worry) // relief_factor

                worry %= test_lcm

                target = monkey["test_result"][worry % monkey["test"] == 0]
                monkey_info[target]["items"].append(worry)

    # return list(monkey["inspected"] for monkey in monkey_info)
    return prod(sorted((monkey["inspected"] for monkey in monkey_info), reverse=True)[:2])

print(f"Part 1: {day_11(20, 3)}")
print(f"Part 2: {day_11(10000, 1)}")
