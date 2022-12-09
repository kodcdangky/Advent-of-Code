# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import linecache

def going_down(txt):
    down = 0
    line_no = 1
    with open(txt) as file:
        for _ in file:
            line_no += 1        # number of lines in txt
    last_3_depth = int(linecache.getline(txt, 1)) + int(linecache.getline(txt, 2)) + int(linecache.getline(txt, 3))
    for i in range(4, line_no):
        current_3_depth = int(linecache.getline(txt, i-2)) + int(linecache.getline(txt, i-1)) + int(linecache.getline(txt, i))
        if current_3_depth > last_3_depth:
            down += 1
        last_3_depth = current_3_depth
    return down

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(going_down("input.txt"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
