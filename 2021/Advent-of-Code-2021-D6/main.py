# Exponentially growing school of fish
import datetime

def breed(txt):
    file = open(txt)
    init = file.readline().split(",")
    for i in range(len(init)):
        init[i] = int(init[i])
    file.close()

    school = [0 for i in range(9)]
    for i in init:
        school[i] += 1

    return lead1(10000000, school)

'''
def lead(day):
    count = [1]
    school = [1]

    for d in range(day):
        for i in range(len(school)):
            if school[i] == 0:
                school[i] = 6
                school.append(8)
            else:
                school[i] -= 1
        count.append(len(school))
    return count
#'''

#'''
def lead1(day, school):
    for d in range(day):
        school[7] += school[0]
        school.append(school.pop(0))
    return sum(school)
#'''
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    duration = datetime.datetime.now().timestamp()
    print(breed("input.txt"))
    print(datetime.datetime.now().timestamp() - duration)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
