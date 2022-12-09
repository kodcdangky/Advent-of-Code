# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def bingo(txt):
    score = 0
    turn = 0

    file = open(txt)
    line = file.readline()
    point = line.split(",")
    table = []

    for line in file:
        line = line[:-1]
        if len(line) > 0:
            line = line.split(" ")
            while "" in line:
                line.remove("")
            table.append(line)
        else:
            if len(table) == 0: continue
            else:
                mark = [[0] * 5 for i in range(5)]
                current_turn = 0
                for p in point:
                    current_turn += 1

                    for i in range(5):
                        for j in range(5):
                            if p == table[i][j]:
                                mark[i][j] = 1

                    if bingo_check(mark):
                        if current_turn <= turn: break
                        else:
                            turn = current_turn
                            score = score_calc(table, mark, p)
                            break
                table.clear()

    file.close()
    return score

def bingo_check(mark):
    for i in range(len(mark)):
        if 0 not in mark[i]:
            return True
    for j in range(len(mark[0])):
        count = 0
        for i in range(len(mark)):
            if mark[i][j] == 0: break
            else: count += 1
        if count == 5: return True
    return False

def score_calc(table, mark, p):
    score = 0
    for i in range(len(mark)):
        for j in range(len(mark[i])):
            if mark[i][j] == 0:
                score += int(table[i][j])
    return score * int(p)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(bingo("input.txt"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
