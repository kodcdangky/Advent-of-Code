# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def position(txt):
    length = 0
    depth = 0
    aim = 0
    file = open(txt)
    for line in file:
        direction = line.split(" ")
        value = int(direction[1])
        if direction[0] == "down": aim += value
        elif direction[0] == "up": aim -= value
        else:
            length += value
            depth += aim * value
    return length*depth


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(position("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
