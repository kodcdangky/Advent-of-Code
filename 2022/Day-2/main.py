### https://adventofcode.com/2022/day/2

CHOICES = ["A", "B", "C"]


def part_1():
    TRANSLATION = {"X": "A", "Y": "B", "Z": "C"}

    score = 0
    with open("input.txt") as file:
        for line in file:
            oppo, me = line[:-1].split(" ")
            me = TRANSLATION[me]
            me_index = CHOICES.index(me)
            score += me_index + 1
            score += (
                6
                if oppo == CHOICES[me_index - 1]
                else 3
                if oppo == CHOICES[me_index]
                else 0
            )

    print(score)


def part_2():
    OUTCOMES = {"X": 0, "Y": 3, "Z": 6}

    score = 0
    with open("input.txt") as file:
        for line in file:
            oppo, outcome = line[:-1].split(" ")
            score += OUTCOMES[outcome]

            oppo_index = CHOICES.index(oppo)
            match OUTCOMES[outcome]:
                case 0:
                    score += (oppo_index - 1) % 3 + 1
                case 3:
                    score += oppo_index + 1
                case 6:
                    score += (oppo_index + 1) % 3 + 1

    print(score)


part_1()
part_2()
