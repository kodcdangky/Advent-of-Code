### https://adventofcode.com/2022/day/21

import operator

INPUT = "input.txt"
OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


def part_1():
    ALPHA = "root"

    def calc(job: tuple | int) -> int:
        if isinstance(job, int):
            return job

        ops, monkey_a, monkey_b = job
        return ops(calc(monkeys[monkey_a]), calc(monkeys[monkey_b]))

    with open(INPUT) as file:
        monkeys = {}
        for line in file:
            monkey, job = line[:-1].split(": ")
            if job.isdigit():
                monkeys[monkey] = int(job)
            else:
                monkey_a, ops, monkey_b = job.split()
                monkeys[monkey] = OPS[ops], monkey_a, monkey_b

    return calc(monkeys[ALPHA])


def part_2():
    ALPHA = "root"
    HUMAN = "humn"

    def calc(job: tuple | int) -> int:
        if isinstance(job, int):
            return job

        ops, monkey_a, monkey_b = job
        return ops(calc(monkeys[monkey_a]), calc(monkeys[monkey_b]))

    with open(INPUT) as file:
        monkeys = {}
        for line in file:
            monkey, job = line[:-1].split(": ")
            if job.isdigit():
                monkeys[monkey] = int(job)
            else:
                monkey_a, ops, monkey_b = job.split()
                monkeys[monkey] = OPS[ops], monkey_a, monkey_b

    trace = [HUMAN]
    while trace[-1] not in monkeys[ALPHA]:
        for monkey in monkeys:
            if isinstance(monkeys[monkey], tuple) and trace[-1] in monkeys[monkey]:
                trace.append(monkey)
                break

    child = trace.pop()
    # this line is kinda dogshit but it's the best i can think of
    other_child = set(monkeys[ALPHA][1:]).difference((child,)).pop()
    child_res = calc(monkeys[other_child])  # Special case for root

    while trace:
        parent = child
        parent_res = child_res

        ops = monkeys[parent][0]
        child = trace.pop()
        other_child = set(monkeys[parent][1:]).difference((child,)).pop()
        other_child_res = calc(monkeys[other_child])

        # I wish I can come up with a better way to code this logic
        if ops is OPS["+"]:
            child_res = parent_res - other_child_res

        elif ops is OPS["*"]:
            child_res = parent_res // other_child_res

        elif ops is OPS["-"]:
            if child == monkeys[parent][1]:
                child_res = parent_res + other_child_res

            else:
                child_res = other_child_res - parent_res

        elif ops is OPS["/"]:
            if child == monkeys[parent][1]:
                child_res = parent_res * other_child_res

            else:
                child_res = other_child_res // parent_res

    return child_res


print(f"{part_1() = }")
print(f"{part_2() = }")
