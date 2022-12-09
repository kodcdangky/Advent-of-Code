# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def position(txt):
    length = 0
    height = 0
    file = open(txt)
    for line in file:
        direction = line.split(" ")
        if direction[0] == "forward": length += int(direction[1])
        elif direction[0] == "down": height += int(direction[1])
        else: height -= int(direction[1])
    return length*height


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(position("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
