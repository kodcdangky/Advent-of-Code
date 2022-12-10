### https://adventofcode.com/2022/day/10

INPUT = "input.txt"


# OMEGALUL solution but I was grinding poe
def part_1():
    from fnmatch import fnmatch

    CHECK_CYCLE = (20, 60, 100, 140, 180, 220)

    with open(INPUT) as file:
        program = file.read().splitlines()

    cycle = strength = 0
    register = 1

    for instruction in program:
        if fnmatch(instruction, "noop"):
            cycle += 1

            if cycle in CHECK_CYCLE:
                strength += cycle * register

        elif fnmatch(instruction, "addx *"):
            add_value = int(instruction.split(" ")[1])

            cycle += 1
            if cycle in CHECK_CYCLE:
                strength += cycle * register

            cycle += 1
            if cycle in CHECK_CYCLE:
                strength += cycle * register

            register += add_value

    return strength


# Also OMEGALUL for same reason as part 1
def part_2():
    from fnmatch import fnmatch

    PIXEL = [".", "#"]

    with open(INPUT) as file:
        program = file.read().splitlines()

    crt = []
    sprite = 1
    cursor = -1
    for instruction in program:
        if fnmatch(instruction, "noop"):
            cursor = (cursor + 1) % 40
            crt.append(PIXEL[cursor in range(sprite - 1, sprite + 2)])

        elif fnmatch(instruction, "addx *"):
            add_value = int(instruction.split(" ")[1])

            cursor = (cursor + 1) % 40
            crt.append(PIXEL[cursor in range(sprite - 1, sprite + 2)])

            cursor = (cursor + 1) % 40
            crt.append(PIXEL[cursor in range(sprite - 1, sprite + 2)])

            sprite += add_value

    display = []
    for line_length in range(40, len(crt) + 1, 40):
        display.append("".join(crt[line_length - 40 : line_length]))

    for line in display:
        print(line)


print(f"{part_1() = }")
part_2()
