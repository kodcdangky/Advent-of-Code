### https://adventofcode.com/2022/day/16

INPUT = "input.txt"


def floyd_warshall(valve_map: dict[str, list[str]]) -> dict[str, dict[str, int]]:
    min_dist = {valve: {} for valve in valve_map}

    for valve in valve_map:
        for other_valve in valve_map:
            min_dist[valve][other_valve] = (
                0
                if valve == other_valve
                else 1
                if other_valve in valve_map[valve][1]
                else float("inf")
            )

    for mid in valve_map:
        for origin in valve_map:
            for dest in valve_map:
                min_dist[origin][dest] = min(
                    min_dist[origin][dest],
                    min_dist[origin][mid] + min_dist[mid][dest],
                )

    return min_dist


def parse_input(input_file) -> tuple[dict[str, dict[str, int]], dict[str, int]]:
    from fnmatch import fnmatch

    with open(input_file) as file:
        valve_map: dict[str, list[int, str]] = {}
        for line in file:
            if fnmatch(line, "Valve ?? has flow rate=*; tunnels lead to valves *"):
                valve, dest = line[:-1].split("; ")

                valve = valve.split()
                valve, rate = valve[1], valve[4]

                rate = int(rate.removeprefix("rate="))

                dest = dest.removeprefix("tunnels lead to valves").strip().split(", ")

            elif fnmatch(line, "Valve ?? has flow rate=*; tunnel leads to valve *"):
                valve, dest = line[:-1].split("; ")

                valve = valve.split()
                valve, rate = valve[1], valve[4]

                rate = int(rate.removeprefix("rate="))

                dest = dest.removeprefix("tunnel leads to valve").strip()

            valve_map[valve] = [rate, dest]

    return (
        floyd_warshall(valve_map),
        {valve: valve_map[valve][0] for valve in valve_map},
    )


def part_1():
    """
    Floyd-Warshall to find shortest path between all positive pressure valves
    Search all paths possible within a 30 min constraint and find the max pressure possible
    """
    T_MINUS = 30

    def dfs_valves(
        valves_explored: list[str] = ["AA"],
        valves_remaining: set[str] = set(),
        time_remaining: int = T_MINUS,
        explored_pressure: int = 0,
    ):
        max_pressure = explored_pressure
        curr_valve = valves_explored[-1]
        for valve in filter(
            lambda valve: time_remaining - min_dist[curr_valve][valve] - 1 > 0,
            valves_remaining,
        ):
            new_time = time_remaining - min_dist[curr_valve][valve] - 1
            new_explored = valves_explored + [valve]
            max_pressure = max(
                max_pressure,
                dfs_valves(
                    new_explored,
                    valves_remaining.difference(new_explored),
                    new_time,
                    explored_pressure + valve_map[valve] * new_time,
                ),
            )
        return max_pressure

    min_dist, valve_map = parse_input(INPUT)
    return dfs_valves(
        ["AA"], set(valve for valve in valve_map if valve_map[valve] > 0), T_MINUS, 0
    )


def part_2():
    """
    Works for actual input, does not work for example.
    The version which works for example is far far too costly when used on actual input.

    Search for all possible paths like in part 1, but with a 26 min constraint
    Record pressures of all full paths (paths that has no more valves to fit/ can not fit any more valves)
    Find the largest sum of pressure between 2 exclusive paths
    """
    from itertools import product

    T_MINUS = 26

    def dfs_valves(
        valves_explored: list[str] = ["AA"],
        valves_remaining: set[str] = set(),
        time_remaining: int = T_MINUS,
        explored_pressure: int = 0,
    ):
        curr_valve = valves_explored[-1]
        pending = tuple(
            filter(
                lambda valve: time_remaining - min_dist[curr_valve][valve] - 1 > 0,
                valves_remaining,
            )
        )
        if not pending:
            return pressure.setdefault(tuple(valves_explored), explored_pressure)

        max_pressure = explored_pressure
        for valve in sorted(
            pending,
            key=min_dist[curr_valve].get,
        ):
            new_time = time_remaining - min_dist[curr_valve][valve] - 1
            new_explored = valves_explored + [valve]
            max_pressure = max(
                max_pressure,
                dfs_valves(
                    new_explored,
                    valves_remaining.difference(new_explored),
                    new_time,
                    explored_pressure + valve_map[valve] * new_time,
                ),
            )
        return max_pressure

    min_dist, valve_map = parse_input(INPUT)
    pressure = {}
    dfs_valves(
        valves_remaining=set(valve for valve in valve_map if valve_map[valve] > 0)
    )

    return max(
        pressure[ur_path] + pressure[ele_path]
        for ur_path, ele_path in product(pressure, repeat=2)
        if set(ur_path).intersection(ele_path) == {"AA"}
    )


print(f"{part_1() = }")
print(f"{part_2() = }")
