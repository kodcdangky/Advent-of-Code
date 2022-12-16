### https://adventofcode.com/2022/day/16

from fnmatch import fnmatch

INPUT = "input.txt"


def part_1():
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

    with open(INPUT) as file:
        valve_map: dict[str, list[str]] = {}
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

    min_dist = floyd_warshall(valve_map)
    activated = set()
    t_minus = 30
    current_valve = "AA"
    pressure = 0
    while t_minus > 0 and len(activated) < len(valve_map):
        while (
            nxt_best_valve := max(
                min_dist[current_valve],
                key=lambda valve: (t_minus - min_dist[current_valve][valve] - 1)
                * valve_map[valve][0],
            )
        ) in activated:
            min_dist[current_valve].pop(nxt_best_valve)

        if valve_map[nxt_best_valve][0] == 0:
            break

        t_minus -= min_dist[current_valve][nxt_best_valve] + 1
        if t_minus > 0:
            activated.add(nxt_best_valve)
            pressure += t_minus * valve_map[nxt_best_valve][0]
            current_valve = nxt_best_valve

    return pressure, activated


def part_2():
    pass


print(f"{part_1() = }")
print(f"{part_2() = }")
