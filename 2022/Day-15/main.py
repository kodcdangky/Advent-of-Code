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


# New, more clever approach. Credit: https://www.reddit.com/r/adventofcode/comments/zmfwg1/2022_day_15_part_2_seekin_for_the_beacon/
# Still quite slow but doesn't use nearly as much memory now
def part_2():
    def manhattan_dist(point_a: tuple, point_b: tuple) -> int:
        return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

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

            data.append((sensor, manhattan_dist(sensor, beacon)))

    for pri_sensor, pri_radi in data:
        pri_radi += 1
        for y in range(pri_sensor[1] - pri_radi, pri_sensor[1] + pri_radi + 1):
            if y in SEARCH_ZONE[1]:
                for x in (
                    pri_sensor[0] - abs(abs(y - pri_sensor[1]) - pri_radi),
                    pri_sensor[0] + abs(abs(y - pri_sensor[1]) - pri_radi) + 1,
                ):
                    if x in SEARCH_ZONE[0]:
                        for sec_sensor, sec_radi in data:
                            if sec_sensor != pri_sensor:
                                man_dist = manhattan_dist(sec_sensor, (x, y))
                                if man_dist <= sec_radi:
                                    break
                        else:
                            return x * 4_000_000 + y


print(f"{part_1() = }")
print(f"{part_2() = }")
