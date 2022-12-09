# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def draw(txt):
    canvas = [[0] * 1000 for i in range(1000)]
    count = 0
    file = open(txt)

    for line in file:
        line = line[:-1].split("->")
        begin = line[0].strip().split(",")
        end = line[1].strip().split(",")
        x1 = int(begin[0])
        y1 = int(begin[1])
        x2 = int(end[0])
        y2 = int(end[1])

        if x1 == x2:
            x = x1
            for y in range(min(y1, y2), max(y1, y2)+1):
                canvas[x][y] += 1
            continue

        if y1 == y2:
            y = y1
            for x in range(min(x1, x2), max(x1, x2)+1):
                canvas[x][y] += 1
            continue

        x = x1
        y = y1
        while x != x2 and y != y2:
            canvas[x][y] += 1
            x += (x2 - x1) // abs(x2 - x1)
            y += (y2 - y1) // abs(y2 - y1)
        canvas[x][y] += 1

    for x in range(1000):
        for y in range(1000):
            if canvas[x][y] > 1:
                count += 1

    file.close()
    return count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(draw("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
