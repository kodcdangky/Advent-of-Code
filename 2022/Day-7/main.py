### https://adventofcode.com/2022/day/7

INPUT = "input.txt"


def part_1():
    def inspect_folder(root):
        current_size = 0
        for name in root:
            if type(root[name]) is dict:
                dir_stack.append(name)
                sizes["/".join(dir_stack)] = inspect_folder(root[name])
                current_size += sizes["/".join(dir_stack)]
                dir_stack.pop()
            else:
                current_size += root[name]
        return current_size

    with open(INPUT) as file:
        terminal = file.read().splitlines()

    if terminal[0] != "$ cd /":
        raise Exception("'cd /' must be called")

    root = {}
    dir_stack = []
    cd = root

    line_no = 1
    while line_no < len(terminal):
        line = terminal[line_no].split(" ")
        if line[0] == "$":
            match line[1]:
                case "cd":
                    match line[2]:
                        case "/":
                            dir_stack.clear()
                            cd = root

                        case "..":
                            dir_stack.pop()
                            cd = root
                            for folder in dir_stack:
                                cd = cd[folder]

                        case _:
                            dir_stack.append(line[2])
                            cd = cd[line[2]]

                    line_no += 1

                case "ls":
                    inspect = line_no + 1

                    while (inspect < len(terminal) and
                           not terminal[inspect].startswith("$")):
                        inspect_line = terminal[inspect].split(" ")

                        if inspect_line[0] == "dir":
                            if inspect_line[1] not in cd:
                                cd[inspect_line[1]] = {}
                        else:
                            cd[inspect_line[1]] = int(inspect_line[0])
                        inspect += 1

                    line_no = inspect

        else:
            raise Exception("Reading non-command line")

    sizes = {}
    dir_stack = ["root"]
    sizes["root"] = inspect_folder(root)
    print(f"Part 1: {sum(sizes[folder] for folder in sizes if sizes[folder] <= 100000)}")

    return sizes



def part_2():
    TOTAL = 70_000_000
    REQUIRED = 30_000_000
    IN_USE = part_1()
    AVAILABLE = TOTAL - IN_USE["root"]

    for size in sorted(IN_USE.values()):
        if size >= REQUIRED - AVAILABLE:
            print(f"Part 2: {size}")
            return

part_1()
part_2()
