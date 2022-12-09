# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime

cost = {
    'a': 1,
    'b': 10,
    'c': 100,
    'd': 1000
}

reservation = {
    2: 'a',
    4: 'b',
    6: 'c',
    8: 'd'
}

outcome = {
    str([None, None, ['a', 'a'], None, ['b', 'b'], None, ['c', 'c'], None, ['d', 'd'], None, None]): 0
}


def burrow_sort(burrow):
    if outcome.get(str(burrow), 999999) != 999999:
        return outcome[str(burrow)]

    outcome[str(burrow)] = 999999

    # pulling into rooms
    for r in (2, 4, 6, 8):
        if len(burrow[r]) == 2 or any(x != reservation[r] for x in burrow[r]):
            continue

        # search left side of room
        for i in reversed(range(0, r)):
            if type(burrow[i]) is str:

                if burrow[i] != reservation[r]:
                    break
                else:
                    burrow[r].append(burrow[i]); burrow[i] = None
                    energy = burrow_sort(burrow) + cost[reservation[r]] * (abs(r - i) + (3 - len(burrow[r])))
                    burrow[i] = burrow[r].pop()
                    if outcome[str(burrow)] > energy:
                        outcome[str(burrow)] = energy
                    return outcome[str(burrow)]

            # elif type(burrow[i]) is list and len(burrow[i]) and burrow[i][-1] == reservation[r]:
            #     burrow[r].append(burrow[i].pop())
            #     energy, finished = burrow_sort(burrow)
            #     burrow[i].append(burrow[r].pop())
            #     if finished:
            #         outcome[str(burrow)] \
            #             = min(outcome[str(burrow)],
            #                   energy + cost[reservation[r]] * (abs(r - i) + 5 - len(burrow[r]) - len(burrow[i])))

        # search right side of room
        for i in range(r + 1, len(burrow)):
            if type(burrow[i]) is str:

                if burrow[i] != reservation[r]:
                    break
                else:
                    burrow[r].append(burrow[i]); burrow[i] = None
                    energy = burrow_sort(burrow) + cost[reservation[r]] * (abs(r - i) + (3 - len(burrow[r])))
                    burrow[i] = burrow[r].pop()
                    if outcome[str(burrow)] > energy:
                        outcome[str(burrow)] = energy
                    return outcome[str(burrow)]

            # elif type(burrow[i]) is list and len(burrow[i]) and burrow[i][-1] == reservation[r]:
            #     burrow[r].append(burrow[i].pop())
            #     energy, finished = burrow_sort(burrow)
            #     burrow[i].append(burrow[r].pop())
            #     if finished:
            #         outcome[str(burrow)] \
            #             = min(outcome[str(burrow)],
            #                   energy + cost[reservation[r]] * (abs(r - i) + 5 - len(burrow[r]) - len(burrow[i])))

    # pushing out of rooms
    for r in (2, 4, 6, 8):
        if len(burrow[r]) == 0 or set(burrow[r]) == {reservation[r]}:
            continue

        # pushing into left side of room
        for i in reversed(range(0, r)):
            if type(burrow[i]) is str:
                break

            elif burrow[i] is None:
                burrow[i] = burrow[r].pop()
                energy = burrow_sort(burrow) + cost[burrow[i]] * (abs(r - i) + (2 - len(burrow[r])))
                burrow[r].append(burrow[i]); burrow[i] = None
                if outcome[str(burrow)] > energy:
                    outcome[str(burrow)] = energy

        # pushing into right side of room
        for i in range(r + 1, len(burrow)):
            if type(burrow[i]) is str:
                break

            elif burrow[i] is None:
                burrow[i] = burrow[r].pop()
                energy = burrow_sort(burrow) + cost[burrow[i]] * (abs(r - i) + (2 - len(burrow[r])))
                burrow[r].append(burrow[i]); burrow[i] = None
                if outcome[str(burrow)] > energy:
                    outcome[str(burrow)] = energy

    return outcome[str(burrow)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    burrow  = [None, None, ['a', 'a'], None, ['b', 'b'], None, ['c', 'c'], None, ['d', 'd'], None, None]
    burrow0 = [None, None, ['d', 'a'], None, ['d', 'c'], None, ['a', 'b'], None, ['c', 'b'], None, None]    # my input
    burrow1 = [None, None, ['a', 'b'], None, ['d', 'c'], None, ['c', 'b'], None, ['a', 'd'], None, None]    # test
    burrow2 = [None, None, ['b', 'a'], None, ['c', 'd'], None, ['d', 'b'], None, ['a', 'c'], None, None]    # input
    burrow3 = [None, None, ['c', 'd'], None, ['c', 'b'], None, ['d', 'b'], None, ['a', 'a'], None, None]    # input
    burrow4 = [None, None, ['b', 'd'], None, ['c', 'a'], None, ['b', 'c'], None, ['a', 'd'], None, None]    # input

    duration = datetime.datetime.now().timestamp()
    print(burrow_sort(burrow0))
    print(datetime.datetime.now().timestamp() - duration)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
