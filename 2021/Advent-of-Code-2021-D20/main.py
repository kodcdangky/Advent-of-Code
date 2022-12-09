# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def init(txt):
    floor_map = []
    with open(txt) as file:
        algo = file.readline()[:-1]
        file.readline()
        for line in file:
            floor_map.append(line[:-1])
    return algo, floor_map


def lit_count(txt, enhance_count):
    initial = init(txt); algo = initial[0]; floor_map = initial[1]

    match algo[0]:
        case '.':
            for i in range(enhance_count):
                floor_map = enhance(buffer(floor_map, '.'), algo)
        case '#':
            for i in range(enhance_count):
                if i % 2 == 0:
                    floor_map = enhance(buffer(floor_map, '.'), algo)
                else:
                    floor_map = enhance(buffer(floor_map, '#'), algo)

    count = 0
    for i in range(len(floor_map)):
        for j in floor_map[i]:
            if j == '#':
                count += 1
    return count


def enhance(floor_map, algo):
    floor_new_map = []
    for i in range(1, len(floor_map) - 1):
        strr = ''
        for j in range(1, len(floor_map[i]) - 1):
            bina = binary(floor_map[i - 1][j - 1], floor_map[i - 1][j], floor_map[i - 1][j + 1],
                          floor_map[i][j - 1],     floor_map[i][j],     floor_map[i][j + 1],
                          floor_map[i + 1][j - 1], floor_map[i + 1][j], floor_map[i + 1][j + 1])
            strr += algo[int(bina, 2)]
        floor_new_map.append(strr)
    return floor_new_map


def binary(*chars):
    strr = ''
    for c in chars:
        match c:
            case '.':
                strr += '0'
            case '#':
                strr += '1'
    return strr


def buffer(floor_map, c):
    for i in range(len(floor_map)):
        floor_map[i] = c + c + floor_map[i] + c + c

    strr = ''
    for i in range(len(floor_map[0])):
        strr += c

    floor_map.insert(0, strr)
    floor_map.insert(0, strr)

    floor_map.append(strr)
    floor_map.append(strr)

    return floor_map


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(lit_count('input.txt', 100))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
