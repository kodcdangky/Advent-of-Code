# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def going_down(txt):
    down = 0
    f = open(txt)
    last_depth = int(f.readline()[:-1])
    for l in f:
        depth = int(l[:-1])
        if depth > last_depth:
            down += 1
        last_depth = depth
    f.close()
    return down


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(going_down("input.txt"))
#    print(linecache.getline("input.txt", 2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
