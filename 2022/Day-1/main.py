# Part 1: Find the elf who's carrying the most amount of calories
elves = []

with open("input.txt") as file:
    current_elf = 0
    for line in file:
        if line != "\n":
            current_elf += int(line[:-1])
        else:
            elves.append(current_elf)
            current_elf = 0

elves.sort()
print(elves[-1])

# Part 2: Find the total calories of the top 3 elves who're carrying the most amount of calories
print(sum(elves[-3:]))
