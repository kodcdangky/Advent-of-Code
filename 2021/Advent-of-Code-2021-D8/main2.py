# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

no = [""] * 10
def init(txt):
    file = open(txt)
    add = 0
    for line in file:
        line = line[:-1].split("|")
        clue = line[0].strip().split(" ")
        code = line[1].strip().split(" ")

        for i in range(len(no)):
            no[i] = ""

        solve(clue)

        final = ""
        for st in code:
            try:
                final += match(st, no)
            except:
                print("match() didn't return a string")
                sys.exit()

        add += int(final)

    file.close()
    return add

def solve(clue):
    key = [""] * 7

    # find 1, 4, 7, 8
    for st in clue:
        if len(st) == 2:
            no[1] = st
        elif len(st) == 4:
            no[4] = st
        elif len(st) == 3:
            no[7] = st
        elif len(st) == 7:
            no[8] = st
    clue.remove(no[1])
    clue.remove(no[4])
    clue.remove(no[7])
    clue.remove(no[8])

    #key 0
    key[0] = elim(no[7], no[1])

    #find 6, key 2
    for st in clue:
        if len(st) == 6:
            k = elim(no[1], st)
            if k != "":
                key[2] = k
                no[6] = st
                clue.remove(st)
                break

    # find 5
    for st in clue:
        if len(st) == 5 and st.find(key[2]) == -1:
            no[5] = st
            clue.remove(st)
            break

    # find 9, key 4
    k = elim(no[8], no[4])
    for st in clue:
        if len(st) == 6:
            kp = elim(k, st)
            if kp != "":
                key[4] = kp
                no[9] = st
                clue.remove(st)
                break

    # find 0, 2, 3
    for st in clue:
        if len(st) == 6:
            no[0] = st
        elif st.find(key[4]) == -1:
            no[3] = st
        else:
            no[2] = st
    clue.remove(no[0])
    clue.remove(no[2])
    clue.remove(no[3])

def elim(mstr, s):
    main_string = [c for c in mstr]
    for c in s:
        try:
            main_string.remove(c)
        except:
            pass
    ms = ""
    for st in main_string:
        ms += st
    return ms

def match(s, no):
    for n in no:
        if len(s) == len(n):
            count = 0
            for c in s:
                if n.find(c) == -1:
                    break
                count += 1
            if count == len(s):
                return str(no.index(n))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(init("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
