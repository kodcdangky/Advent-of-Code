### https://adventofcode.com/2022/day/16

from fnmatch import fnmatch

INPUT = "test.txt"


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
    T_MINUS = 30

    def dfs_valves(
        valves_explored: list[str],
        valves_remaining: set[str],
        time_remaining: int,
        explored_pressure: int,
    ):
        if tuple(valves_explored) not in pressure:
            pressure[tuple(valves_explored)] = explored_pressure

        curr_valve = valves_explored[-1]
        for valve in sorted(
            valves_remaining,
            key=min_dist[curr_valve].get,
        ):
            if (new_time := time_remaining - min_dist[curr_valve][valve] - 1) > 0:
                new_explored = valves_explored + [valve]
                if tuple(new_explored) not in pressure:
                    dfs_valves(
                        new_explored,
                        valves_remaining.difference(new_explored),
                        new_time,
                        explored_pressure + valve_map[valve] * new_time,
                    )
                pressure[tuple(valves_explored)] = max(
                    pressure[tuple(new_explored)],
                    pressure[tuple(valves_explored)],
                )
            else:
                break

    min_dist, valve_map = parse_input(INPUT)
    pressure = {}
    dfs_valves(
        ["AA"], set(valve for valve in valve_map if valve_map[valve] > 0), T_MINUS, 0
    )

    return pressure[("AA",)]


def part_2():
    T_MINUS = 26

    def dfs_valves(
        valves_explored: list[str] = ["AA"],
        old_explored: list[str] | None = None,
        valves_remaining: set[str] = set(),
        time_remaining: int = T_MINUS,
        explored_pressure: int = 0,
    ):
        path = (
            tuple(valves_explored)
            if not old_explored
            else (tuple(old_explored), tuple(valves_explored))
        )
        if path not in pressure:
            pressure[path] = explored_pressure

        curr_valve = valves_explored[-1]
        for valve in sorted(
            valves_remaining,
            key=min_dist[curr_valve].get,
        ):
            if (new_time := time_remaining - min_dist[curr_valve][valve] - 1) > 0:
                new_explored = valves_explored + [valve]
                child_path = (
                    tuple(new_explored)
                    if not old_explored
                    else (tuple(old_explored), tuple(new_explored))
                )
                if child_path not in pressure:
                    dfs_valves(
                        new_explored,
                        old_explored,
                        valves_remaining.difference(new_explored),
                        new_time,
                        explored_pressure + valve_map[valve] * new_time,
                    )

                pressure[path] = max(pressure[child_path], pressure[path])
            else:
                break

        if not old_explored:
            child_path = (path, ("AA",))
            if child_path not in pressure:
                dfs_valves(
                    old_explored=valves_explored,
                    valves_remaining=valves_remaining,
                    explored_pressure=explored_pressure,
                )
            pressure[path] = max(pressure[path], pressure[child_path])

    min_dist, valve_map = parse_input(INPUT)
    pressure = {}
    dfs_valves(
        valves_remaining=set(valve for valve in valve_map if valve_map[valve] > 0)
    )

    return pressure[("AA",)]


print(f"{part_1() = }")
print(f"{part_2() = }")
