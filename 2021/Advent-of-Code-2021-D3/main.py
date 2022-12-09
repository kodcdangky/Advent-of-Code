# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def extract(txt):
    input = []
    file = open(txt)

    for line in file:
        line = line[:-1]
        input.append(line)
    file.close()

    return input


def rate(list_str):
    higher = ""
    lower = ""
    length = len(list_str[0])
    for i in range(length):
        count_0 = 0
        for b in list_str:
            if b[i] == "0":
                count_0 += 1
        if count_0 > len(list_str) - count_0:
            higher += "0"
            lower += "1"
        else:
            higher += "1"
            lower += "0"
    return int(higher, 2) * int(lower, 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(rate(extract("input.txt")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
