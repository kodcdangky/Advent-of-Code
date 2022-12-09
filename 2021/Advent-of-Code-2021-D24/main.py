# "programming" omegalul just solve by hand


def monad(txt):
    instruction = []
    with open(txt) as file:
        for line in file:
            instruction.append(line[:-1].split(' '))
    return instruction


# kekw
'''class model_number():

    def __init__(self, number = str):
        self.number = number

    def minus1(self):
        digit = []
        while len(self.number) and self.number[-1] == '1':
            digit.append(self.number[-1])
            self.number = self.number[:-1]
        if self.number == '':
            self.number = '9999999999999'   # 13 9's
            return
        digit.append(self.number[-1])
        self.number = self.number[:-1]
        while len(digit):
            temp = digit.pop()
            if temp != '1':
                temp = str(int(temp) - 1)
            else:
                temp = '9'
            self.number += temp


def identify(instruction):
    solved = {}
    model = model_number('99999999999999')  # 14 9's
    count = 0
    while len(model.number) == 14:
        # print(model.number)
        variable = {
            'x': 0,
            'y': 0,
            'z': 0
        }

        for n in reversed(range(len(model.number))):
            if model.number[:n] in solved:
                variable['x'], variable['y'], variable['z'] = solved[model.number[:n]]
                break
        for n in range(n, len(model.number)):
            variable['w'] = int(model.number[n])
            for i in range(n * 18 + 1, (n + 1) * 18):
                match instruction[i][0]:
                    case 'add':
                        if instruction[i][2].isalpha():
                            variable[instruction[i][1]] += variable[instruction[i][2]]
                        else:
                            variable[instruction[i][1]] += int(instruction[i][2])
                    case 'mul':
                        if instruction[i][2].isalpha():
                            variable[instruction[i][1]] *= variable[instruction[i][2]]
                        else:
                            variable[instruction[i][1]] *= int(instruction[i][2])
                    case 'div':
                        if instruction[i][2].isalpha():
                            variable[instruction[i][1]] = int(variable[instruction[i][1]] / variable[instruction[i][2]])
                        else:
                            variable[instruction[i][1]] = int(variable[instruction[i][1]] / int(instruction[i][2]))
                    case 'mod':
                        if instruction[i][2].isalpha():
                            variable[instruction[i][1]] %= variable[instruction[i][2]]
                        else:
                            variable[instruction[i][1]] %= int(instruction[i][2])
                    case 'eql':
                        if instruction[i][2].isalpha():
                            variable[instruction[i][1]] = int(variable[instruction[i][1]] == variable[instruction[i][2]])
                        else:
                            variable[instruction[i][1]] = int(variable[instruction[i][1]] == int(instruction[i][2]))
            if model.number[:n + 1] not in solved:
                solved[model.number[:n + 1]] = variable['x'], variable['y'], variable['z']
        if variable['z'] == 0:
            return model.number
        model.minus1()
        count += 1
        if count % 1000000 == 0:
            print(count, '/ 22,876,792,454,961')'''


# kekl
def identify(i):
    '''
    def solve(x, y, z, w, index):
        for i in range(index * 18 + 1, (index + 1) * 18):
            match instruction[i][0]:
                case 'add':
                    exec(instruction[i][1] + ' += ' + instruction[i][2])
                case 'mul':
                    exec(instruction[i][1] + ' *= ' + instruction[i][2])
                case 'div':
                    exec(instruction[i][1] + ' = ' + 'int(' + instruction[i][1] + ' / ' + instruction[i][2] + ')')
                case 'mod':
                    exec(instruction[i][1] + ' %= ' + instruction[i][2])
                case 'eql':
                    exec(instruction[i][1] + ' = ' + 'int(' + instruction[i][1] + ' == ' + instruction[i][2] + ')')
        return x, y, z

    for w0 in reversed(range(1, 10)):
        temp = int(int(int(i[5][2]) == w0) == 0)
        z0 = (w0 + int(i[15][2])) * temp

        for w1 in reversed(range(1, 10)):
            temp = int(int(z0 % 26 + int(i[23][2]) == w1) == 0)
            z1 = int(z0 / int(i[22][2])) * ((25 + temp) * temp + 1) + ((w1 + int(i[33][2])) * temp)

            for w2 in reversed(range(1, 10)):
                temp = int(int(z1 % 26 + int(i[41][2]) == w2) == 0)
                z2 = int(z1 / int(i[40][2])) * ((25 + temp) * temp + 1) + ((w2 + int(i[51][2])) * temp)

                for w3 in reversed(range(1, 10)):
                    temp = int(int(z2 % 26 + int(i[59][2]) == w3) == 0)
                    z3 = int(z2 / int(i[58][2])) * ((25 + temp) * temp + 1) + ((w3 + int(i[69][2])) * temp)

                    for w4 in reversed(range(1, 10)):
                        temp = int(int(z3 % 26 + int(i[77][2]) == w4) == 0)
                        z4 = int(z3 / int(i[76][2])) * ((25 + temp) * temp + 1) + ((w4 + int(i[87][2])) * temp)

                        for w5 in reversed(range(1, 10)):
                            temp = int(int(z4 % 26 + int(i[95][2]) == w5) == 0)
                            z5 = int(z4 / int(i[94][2])) * ((25 + temp) * temp + 1) + ((w5 + int(i[105][2])) * temp)

                            for w6 in reversed(range(1, 10)):
                                temp = int(int(z5 % 26 + int(i[113][2]) == w6) == 0)
                                z6 = int(z5 / int(i[112][2])) * ((25 + temp) * temp + 1) + ((w6 + int(i[123][2])) * temp)

                                for w7 in reversed(range(1, 10)):
                                    temp = int(int(z6 % 26 + int(i[131][2]) == w7) == 0)
                                    z7 = int(z6 / int(i[130][2])) * ((25 + temp) * temp + 1) + ((w7 + int(i[141][2])) * temp)

                                    for w8 in reversed(range(1, 10)):
                                        temp = int(int(z7 % 26 + int(i[149][2]) == w8) == 0)
                                        z8 = int(z7 / int(i[148][2])) * ((25 + temp) * temp + 1) + ((w8 + int(i[159][2])) * temp)

                                        for w9 in reversed(range(1, 10)):
                                            temp = int(int(z8 % 26 + int(i[167][2]) == w9) == 0)
                                            z9 = int(z8 / int(i[166][2])) * ((25 + temp) * temp + 1) + ((w9 + int(i[177][2])) * temp)

                                            for w10 in reversed(range(1, 10)):
                                                temp = int(int(z9 % 26 + int(i[185][2]) == w10) == 0)
                                                z10 = int(z9 / int(i[184][2])) * ((25 + temp) * temp + 1) + ((w10 + int(i[195][2])) * temp)

                                                for w11 in reversed(range(1, 10)):
                                                    temp = int(int(z10 % 26 + int(i[203][2]) == w11) == 0)
                                                    z11 = int(z10 / int(i[202][2])) * ((25 + temp) * temp + 1) + ((w11 + int(i[213][2])) * temp)

                                                    for w12 in reversed(range(1, 10)):
                                                        temp = int(int(z11 % 26 + int(i[221][2]) == w12) == 0)
                                                        z12 = int(z11 / int(i[220][2])) * ((25 + temp) * temp + 1) + ((w12 + int(i[231][2])) * temp)

                                                        for w13 in reversed(range(1, 10)):
                                                            temp = int(int(z12 % 26 + int(i[239][2]) == w13) == 0)
                                                            z13 = int(z12 / int(i[238][2])) * ((25 + temp) * temp + 1) + ((w13 + int(i[249][2])) * temp)
                                                            if z13 == 0:
                                                                return str(w0) + str(w1) + str(w2) + str(w3) + str(w4)\
                                                                       + str(w5) + str(w6) + str(w7) + str(w8) + str(w9)\
                                                                       + str(w10) + str(w11) + str(w12) + str(w13)

                                    print(str(w0) + '.' + str(w1) + str(w2) + str(w3) + str(w4) + str(w5) + str(w6)
                                          + str(w7) + ' * 10^13')
'''




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(identify(monad('input.txt')))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
