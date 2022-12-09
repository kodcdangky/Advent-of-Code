# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def special(txt):
    file = open(txt)
    count = 0
    for line in file:
        line = line[:-1].split("|")[1].strip()
        code = line.split(" ")
        for c in code:
            if len(c) == 2 or len(c) == 4 or len(c) == 3 or len(c) == 7:
                count += 1
    file.close()
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(special("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
