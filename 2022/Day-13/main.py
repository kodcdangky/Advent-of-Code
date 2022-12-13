### https://adventofcode.com/2022/day/13

from ast import literal_eval

INPUT = "input.txt"


# I omega misunderstood the requirement and spent 3 hrs hating myself
# My initial understanding was that ALL the numbers in the pairs have to be in line with the left < right rule, not just the first different number pair
# After realizing that I got the star in less than 2 min, so at least my logic was correct
def part_1():
    # log = []

    def valid_pair(left, right):
        default = None

        for l, r in zip(left, right):
            # log.append(f"Comparing {l} and {r}")

            if isinstance(l, int) and isinstance(r, int):
                if l > r:
                    return False
                elif l < r:
                    return True
            else:
                if (
                    valid := valid_pair(
                        [l] if isinstance(l, int) else l,
                        [r] if isinstance(r, int) else r,
                    )
                ) is not None:
                    return valid

        if default is None:
            if len(left) < len(right):
                return True
            elif len(left) > len(right):
                return False

        return default

    with open(INPUT) as file:
        pairs = map(
            lambda line_pair: tuple(
                map(lambda line: literal_eval(line), line_pair.splitlines())
            ),
            file.read().split("\n\n"),
        )

    # indx_sum = 0
    # for indx, (left, right) in enumerate(pairs, start=1):
    #     log.append(f"{indx = }")
    #     log.append(f"Comparing {left} and {right}")
    #
    #     indx_sum += indx * (valid := valid_pair(left, right))
    #
    #     log.append(f"{valid}")
    #     if not valid:
    #         log.append(f"{len(left) = }, {len(right) = }")
    #     log.append("")
    #
    # with open("log.txt", "w") as log_file:
    #     log_file.write("\n".join(log))
    #
    # return indx_sum

    return sum(
        indx * valid_pair(left, right)
        for indx, (left, right) in enumerate(pairs, start=1)
    )


# Ended up using insertion sort and using my original recursion for part 1 as the comparison function
# I'm sure this evolution of the function is what you're supposed to do, so basically I solved part 2 during part 1 which then cost me 3 hrs :)
# Code can prob use some clean up tbh
def part_2():
    from math import prod

    DECODE_KEYS = [[[2]], [[6]]]

    def signal_gt(signal_a, signal_b) -> bool:
        default = None
        for l, r in zip(signal_a, signal_b):

            if isinstance(l, int) and isinstance(r, int):
                if l > r:
                    return True
                elif l < r:
                    return False
            else:
                if (
                    gt := signal_gt(
                        [l] if isinstance(l, int) else l,
                        [r] if isinstance(r, int) else r,
                    )
                ) is not None:
                    return gt

        if default is None:
            if len(signal_a) > len(signal_b):
                return True
            elif len(signal_a) < len(signal_b):
                return False

    def sorted_signal_list(signal_list: list[list[list, int]]) -> list[list[list, int]]:
        signal_list_copy = signal_list.copy()
        sorted_signals = [signal_list_copy.pop()]

        for indx, signal in zip(reversed(range(len(signal_list_copy))), reversed(signal_list_copy)):
            for indx_sorted, signal_sorted in enumerate(sorted_signals):
                if signal_gt(signal_sorted, signal):
                    sorted_signals.insert(indx_sorted, signal)
                    signal_list_copy.pop(indx)
                    break

        return sorted_signals

    with open(INPUT) as file:
        signals = list(map(lambda line: literal_eval(line), file.read().split()))

    signals.extend(DECODE_KEYS)

    return prod(sorted_signal_list(signals).index(key) + 1 for key in DECODE_KEYS)


print(f"{part_1() = }")
print(f"{part_2() = }")
