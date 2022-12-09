# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime


def run(steps):
    global template
    global rules
    init("input.txt")

    '''
    count = {
        "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0,
        "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0,
    }
    '''

    #''' getting all unique characters that "are and ever will be" and adding the initial ones
    count = {}
    for c in template:
        if count.get(c) == None:
            count.update({c: 1})
        else:
            count[c] += 1

    for pair in rules:
        result = rules[pair]
        if count.get(result) == None:
            count.update({result: 0})
    #'''

    #''' making all pairs that "are and ever will be"
    pairs = {}
    for char1 in count:
        for char2 in count:
            pair = char1 + char2
            pairs.update({pair: 0})
    #'''

    #''' load initial state into pairs{} and run, each time making a new character immediately adding them to count{}
    for i in range(1, len(template)):
        pairs[template[i - 1:i + 1]] += 1

    pairs_solved = pairs.copy() # pairs_solved{} stores answers to pairs{}, to be copied back to pairs{} at the end of each step
    for step in range(steps):
        for pair in pairs_solved:
            pairs_solved[pair] = 0

        for pair in pairs:
            ans = rules[pair]
            count[ans] += pairs[pair]
            pairs_solved[pair[0] + ans] += pairs[pair]
            pairs_solved[ans + pair[1]] += pairs[pair]

        pairs = pairs_solved.copy()
    #'''

    #''' collect count highest and lowest and print
    high = 0
    low = 10 ** 99
    for c in count:
        if high < count[c]: high = count[c]
        if low > count[c]: low = count[c]

    print(high - low)
    #'''


def init(txt):
    global template
    global rules

    file = open(txt)
    template = file.readline()[:-1]
    rules = {}
    for line in file:
        line = line[:-1]
        if line == "": continue
        line = line.split(" -> ")
        rules.update({line[0]: line[1]})
    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    d = datetime.datetime.now().timestamp()
    run(100)
    print(datetime.datetime.now().timestamp() - d)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
