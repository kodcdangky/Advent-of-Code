# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def sea_cucumber(txt):
    sea_floor = []
    with open(txt) as file:
        for line in file:
            sea_floor.append(list())
            for char in line[:-1]:
                sea_floor[-1].append(char)
    return sea_floor


def parking_space(sea_floor):
    moved = True
    step = 0
    while moved:
        step += 1
        moved = False

        for row in range(len(sea_floor)):
            just_moved = False
            temp = sea_floor[row][0]
            for column in range(len(sea_floor[row]) - 1):
                if just_moved:
                    just_moved = False
                    continue

                if sea_floor[row][column] == '>' and sea_floor[row][column + 1] == '.':
                    sea_floor[row][column] = '.'; sea_floor[row][column + 1] = '>'
                    moved = True
                    just_moved = True

            if not just_moved and sea_floor[row][-1] == '>' and temp == '.':
                sea_floor[row][-1] = '.'; sea_floor[row][0] = '>'


        for column in range(len(sea_floor[0])):
            just_moved = False
            temp = sea_floor[0][column]
            for row in range(len(sea_floor) - 1):
                if just_moved:
                    just_moved = False
                    continue

                if sea_floor[row][column] == 'v' and sea_floor[row + 1][column] == '.':
                    sea_floor[row][column] = '.'; sea_floor[row + 1][column] = 'v'
                    moved = True
                    just_moved = True

            if not just_moved and sea_floor[-1][column] == 'v' and temp == '.':
                sea_floor[-1][column] = '.'; sea_floor[0][column] = 'v'

    return step


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(parking_space(sea_cucumber("input.txt")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
