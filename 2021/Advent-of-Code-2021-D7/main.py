# I feel filthy having wrote this code

def shortest(txt):
    file = open(txt)
    line = file.readline()
    file.close()

    min_dist = 10 ** 99
    init = line.split(",")
    mark = [0] * 10000
    for i in init:
        if mark[int(i)] == 1:
            continue
        dist = 0
        mark[int(i)] = 1
        for j in init:
            dist += seq_sum(abs(int(i) - int(j)))
        if dist < min_dist:
            min_dist = dist
    return min_dist

def seq_sum(n):
    return sum(range(n+1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(shortest("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
