# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import fileinput


def extract(txt):
    input = []
    file = open(txt)

    for line in file:
        line = line[:-1]
        input.append(line)
    file.close()

    return input


def rate(list_str):
    higher = list_str.copy()
    lower = list_str.copy()

    length = len(higher[0])
    for i in range(length):
        if len(higher) == 1: break
        count_0 = 0
        for b in higher:
            if b[i] == "0":
                count_0 += 1
        if count_0 > len(higher) - count_0:
            for b in higher.copy():
                if b[i] == "1":
                    higher.remove(b)
                if len(higher) == 1: break
        else:
            for b in higher.copy():
                if b[i] == "0":
                    higher.remove(b)
                if len(higher) == 1: break

    for i in range(length):
        if len(lower) == 1: break
        count_0 = 0
        for b in lower:
            if b[i] == "0":
                count_0 += 1
        if count_0 > len(lower) - count_0:
            for b in lower.copy():
                if b[i] == "0":
                    lower.remove(b)
                if len(lower) == 1: break
        else:
            for b in lower.copy():
                if b[i] == "1":
                    lower.remove(b)
                if len(lower) == 1: break

    return int(higher[0] ,2) * int(lower[0], 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(rate(extract("input.txt")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
