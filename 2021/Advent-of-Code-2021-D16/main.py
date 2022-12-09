# One of the simplest concept yet most challenging implementation puzzle I've ever done
import math


def hex2bin(strr):
    hex2bin_table = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    bina = ""
    for c in strr:
        bina += hex2bin_table[c.upper()]
    return bina


def bits(txt):
    data = hex2bin(open(txt).readline()[:-1])

    cursor = 0
    pending = []    # a stack; saves remaining progress of operator packets based on their length type ID
    operations = ""
    while len(data) - cursor >= 11:
        ## get packet version
        # pack_ver = int(data[cursor:cursor + 3], 2)
        cursor = cursor + 3

        # get packet type id
        pack_id = int(data[cursor:cursor + 3], 2)
        cursor = cursor + 3

        # progress all length type 0 operator packets along
        pending = len_type_0(pending, 6)

        # pack_id == 4 (literal value)
        if pack_id == 4:
            value = ""
            while True:
                value += data[cursor + 1:cursor + 5]
                cursor += 5
                pending = len_type_0(pending, 5)
                if data[cursor - 5] == "0":
                    break

            operations += str(int(value, 2))

            if pending[-1][0] == "1":
                pending = len_type_1(pending)
            while len(pending) > 0 and pending[-1][2] == "0":
                pending.pop()
                operations += ")"
            if len(pending) == 0:
                break
            operations += ", "

        # pack_id != 4 (operator packet)
        else:
            operations += operation(pack_id)
            if len(pending) > 0:
                if pending[-1][0] == "1":
                    pending = len_type_1(pending)

            len_type = data[cursor]
            if len_type == "0":
                elem_count = int(data[cursor + 1:cursor + 16], 2)
                cursor += 16
                pending = len_type_0(pending, 16)
            else:
                elem_count = int(data[cursor + 1:cursor + 12], 2)
                cursor += 12
                pending = len_type_0(pending, 12)

            # add operation length type id and elements remaining to queue
            pending.append(len_type + "," + str(elem_count))

    return eval(operations)


# write str(operations) based on packet's id
def operation(pack_id):
    op = {
        0: "add(",
        1: "multiply(",
        2: "minimum(",
        3: "maximum(",
        5: "greater(",
        6: "less(",
        7: "equal("
    }
    return op[pack_id]


# move all length type 0 operators character counts remaining by count == how much cursor had just moved
def len_type_0(pending, count):
    for i in range(len(pending)):
        if pending[i][0] == "0" and int(pending[i][2:]) >= count:
            pending[i] = "0," + str(int(pending[i][2:]) - count)
    return pending


# progress the most recent length type 1 operator
def len_type_1(pending):
    pending[-1] = "1," + str(int(pending[-1][2:]) - 1)
    return pending


def add(*args):
    return sum(args)


def multiply(*args):
    return math.prod(args)


def greater(args1, args2):
    return int(args1 > args2)


def less(args1, args2):
    return int(args1 < args2)


def equal(args1, args2):
    return int(args1 == args2)


def minimum(*args):
    return min(args)


def maximum(*args):
    return max(args)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(bits("input.txt"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
