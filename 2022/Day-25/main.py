### https://adventofcode.com/2022/day/25

INPUT = "input.txt"


def day_25():
    """Add all snafus directly.
    All snafus digit sums range from -5 to 5 in decimal number, which can be mapped out manually

    Returns:
        str: sum of all snafus in snafu
    """
    from itertools import zip_longest

    TO_INT = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    TO_SNAFU = {
        -5: "-0",
        -4: "-1",
        -3: "-2",
        -2: "=",
        -1: "-",
        0: "0",
        1: "1",
        2: "2",
        3: "1=",
        4: "1-",
        5: "10",
    }

    with open(INPUT) as file:
        snafus = file.read().splitlines()

    total = []
    for snafu in snafus:
        hold = "0"
        for idx, (snafu_term, total_term) in enumerate(
            zip_longest(reversed(snafu), total, fillvalue="0")
        ):
            term_sum = TO_SNAFU[TO_INT[snafu_term] + TO_INT[total_term] + TO_INT[hold]]
            if len(term_sum) == 2:
                try:
                    total[idx] = term_sum[1]
                except IndexError:
                    total.append(term_sum[1])
                hold = term_sum[0]
            else:
                try:
                    total[idx] = term_sum
                except IndexError:
                    total.append(term_sum)
                hold = "0"
        total.append(hold)

    return "".join(reversed(total)).lstrip("0")


print(f"{day_25() = }")
