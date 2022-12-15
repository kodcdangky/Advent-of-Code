### https://adventofcode.com/2022/day/15

from fnmatch import fnmatch

INPUT = "input.txt"


def part_1():
    Y = 2_000_000 if INPUT == "input.txt" else 10
    with open(INPUT) as file:
        report = file.read().splitlines()

    data = []
    for line in report:
        if fnmatch(line, "Sensor at x=*, y=*: closest beacon is at x=*, y=*"):
            sensor, beacon = line.split(": ")

            sensor = sensor.removeprefix("Sensor at ").split(", ")
            sensor = (
                int(sensor[0].removeprefix("x=")),
                int(sensor[1].removeprefix("y=")),
            )

            beacon = beacon.removeprefix("closest beacon is at ").split(", ")
            beacon = (
                int(beacon[0].removeprefix("x=")),
                int(beacon[1].removeprefix("y=")),
            )

            data.append((sensor, beacon))

    visible_on_Y = set()
    for sensor, beacon in data:
        man_dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if Y in range(sensor[1] - man_dist, sensor[1] + man_dist + 1):
            visible_on_Y.update(
                range(
                    sensor[0] - abs(abs(Y - sensor[1]) - man_dist),
                    sensor[0] + abs(abs(Y - sensor[1]) - man_dist) + 1,
                )
            )

    equipment = set()
    for sensor, beacon in data:
        equipment.update((sensor, beacon))

    no_beacon = len(visible_on_Y)

    for gear in equipment:
        no_beacon -= Y == gear[1]

    return no_beacon


# Extremely slow part 2 but at least it finished, my initial approach wasn't even gonna finish within this lifetime
def part_2():
    def mergeable(range_0: range, range_1: range) -> bool:
        return any(
            (
                range_0.start in range_1,
                range_0.stop in range_1,
                range_0.stop == range_1.start,
                range_1.start in range_0,
                range_1.stop in range_0,
                range_1.stop == range_0.start,
            )
        )

    def merge(range_0: range, range_1: range) -> range:
        return range(min(range_0.start, range_1.start), max(range_0.stop, range_1.stop))

    SEARCH_ZONE = (
        (range(4_000_001), range(4_000_001))
        if INPUT == "input.txt"
        else (range(20), range(20))
    )
    with open(INPUT) as file:
        report = file.read().splitlines()

    data = []
    for line in report:
        if fnmatch(line, "Sensor at x=*, y=*: closest beacon is at x=*, y=*"):
            sensor, beacon = line.split(": ")

            sensor = sensor.removeprefix("Sensor at ").split(", ")
            sensor = (
                int(sensor[0].removeprefix("x=")),
                int(sensor[1].removeprefix("y=")),
            )

            beacon = beacon.removeprefix("closest beacon is at ").split(", ")
            beacon = (
                int(beacon[0].removeprefix("x=")),
                int(beacon[1].removeprefix("y=")),
            )

            data.append((sensor, beacon))

    visible: dict[int, list[range] | None] = {}
    filled = set()
    for sensor, beacon in data:
        man_dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        for y in range(
            max(sensor[1] - man_dist, SEARCH_ZONE[1].start),
            min(sensor[1] + man_dist + 1, SEARCH_ZONE[1].stop),
        ):
            new_range = range(
                max(
                    sensor[0] - abs(abs(y - sensor[1]) - man_dist), SEARCH_ZONE[0].start
                ),
                min(
                    sensor[0] + abs(abs(y - sensor[1]) - man_dist) + 1,
                    SEARCH_ZONE[0].stop,
                ),
            )
            if y in filled:
                continue
            if y not in visible:
                visible[y] = [new_range]
            else:
                merged = True
                while merged:
                    merged = False
                    for indx, r in zip(
                        reversed(range(len(visible[y]))), reversed(visible[y])
                    ):
                        if mergeable(r, new_range):
                            new_range = merge(visible[y].pop(indx), new_range)
                            merged = True
                if new_range == SEARCH_ZONE[0]:
                    filled.add(y)
                    del visible[y]
                else:
                    visible[y].append(new_range)

    y, (range_0, range_1) = visible.popitem()
    x = range_0.stop if range_0.stop < range_1.start else range_1.stop
    return x * 4_000_000 + y


print(f"{part_1() = }")
print(f"{part_2() = }")
