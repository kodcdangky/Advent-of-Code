ROUND = "O"
BLOCK = "#"
EMPTY = "."


def parse_data(raw: str):
    return list(map(lambda line: list(line), raw.splitlines()))


def tilt_verti(disc: list[list[str]], south: bool):
    for col_indx in range(len(disc[0])):
        rocks = 0
        for row_indx, row in enumerate(disc) if south else zip(reversed(range(len(disc))), reversed(disc)):
            if row[col_indx] == ROUND:
                row[col_indx] = EMPTY
                rocks += 1
            if disc[row_indx][col_indx] == BLOCK:
                for indx in range(row_indx + (-rocks * south or 1), row_indx + ((not south) * (rocks + 1))):
                    disc[indx][col_indx] = ROUND
                rocks = 0
        for indx in range(south * (len(disc) - rocks), south * len(disc) or rocks):
            disc[indx][col_indx] = ROUND


def tilt_hori(disc: list[list[str]], east: bool):
    for row in disc:
        rocks = 0
        for col_indx, rock in enumerate(row) if east else zip(reversed(range(len(row))), reversed(row)):
            if rock == ROUND:
                row[col_indx] = EMPTY
                rocks += 1
            if row[col_indx] == BLOCK:
                row[col_indx + (-rocks * east or 1):
                    col_indx + (not east) * (1 + rocks)] = [ROUND] * rocks
                rocks = 0
        row[east * (len(row) - rocks):
            east * len(row) or rocks] = [ROUND] * rocks


def score(data: list[list[str]]):
    return sum((len(data) - row_indx) * (rock == ROUND) for row_indx, row in enumerate(data) for rock in row)


def part_1(data: list[list[str]]):
    tilt_verti(data, False)
    return score(data)


def part_2(data: list[list[str]]) -> int:
    TURNS = 1_000_000_000

    def tilt(data: list[list[str]]):
        tilt_verti(data, False)  # North
        tilt_hori(data, False)  # West
        tilt_verti(data, True)  # South
        tilt_hori(data, True)  # East

    def stringify(data: list[list[str]]):
        return "\n".join(map(lambda line: "".join(line), data))

    last_hash = hash(stringify(data))
    state_map: dict[int, str] = {}
    for _ in range(TURNS):
        tilt(data)
        state_map[last_hash] = stringify(data)
        if (new_hash := hash(state_map[last_hash])) in state_map:
            cycle = [new_hash]
            while (next_hash := hash(state_map[cycle[-1]])) not in cycle:
                cycle.append(next_hash)
            return score(parse_data(state_map[cycle[(TURNS - len(state_map)) % len(cycle) - 1]]))
        last_hash = new_hash

    return score(data)


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(parse_data(raw)))
    print(part_2(parse_data(raw)))


if __name__ == "__main__":
    main()
