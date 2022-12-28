### https://adventofcode.com/2022/day/19

### Credit for solution idea (I can't read Julia anyway):
# https://www.reddit.com/r/adventofcode/comments/zpihwi/comment/j1xy1ye/
### The most obvious blind brute force idea is to explore every option with dfs,
# but this would take probably days for part 1, and even longer for part 2
### I initally looked into branch and bound dfs, but I could not for the life of me
# figure out a good enough estimation function on my own, and honestly I was super frustrated
# by the end of it, so I went to the solution megathread
### Turns out even with a decent estimation function this still takes quite long,
# and all the ideas in the link was very crucial in the end (even with them part 2 still took like nearly a minute)

INPUT = "input.txt"


def parse_input(input_file):
    from fnmatch import fnmatchcase

    blueprints = []
    with open(input_file) as file:
        for line in file:
            blueprints.append({})
            _, robots_desc = line[:-1].split(": ")

            for robo_desc in robots_desc.split("."):
                robo_desc = robo_desc.strip(". ")
                if fnmatchcase(robo_desc, "Each * robot costs *"):
                    robo_desc = robo_desc.split(" costs ")

                    robo_type = robo_desc[0].split()[1]
                    blueprints[-1][robo_type] = {}

                    for robo_cost in robo_desc[1].split(" and "):
                        quant, resource = robo_cost.split()
                        blueprints[-1][robo_type][resource] = int(quant)
    return blueprints


def get_max_geode(blueprint: dict[str, dict[str, int]], time_available: int):
    from collections import defaultdict

    ROBOTS_QUEUE = ("geode", "obsidian", "clay", "ore")

    def dfs_starcraft(
        robots: defaultdict, resources: defaultdict, skipping: set, time_remaining: int
    ):
        global max_geode

        if not time_remaining:
            max_geode = max(max_geode, resources["geode"])
            return

        new_resources = resources.copy()
        for robo in robots:
            new_resources[robo] += robots[robo]

        if (
            resources["geode"]
            + sum(new_resources["geode"] + incre for incre in range(time_remaining + 1))
            <= max_geode
        ):
            return

        new_robots = robots.copy()
        new_skipping = skipping.copy()
        for robo in ROBOTS_QUEUE:
            if (
                robo not in skipping
                and robots[robo] + 1 <= max_bots_req[robo]
                and all(
                    blueprint[robo][req] <= resources[req] for req in blueprint[robo]
                )
            ):
                new_robots[robo] += 1
                for req in blueprint[robo]:
                    new_resources[req] -= blueprint[robo][req]

                dfs_starcraft(new_robots, new_resources, set(), time_remaining - 1)

                if robo == "geode":
                    return
                else:
                    new_skipping.add(robo)

                for req in blueprint[robo]:
                    new_resources[req] += blueprint[robo][req]
                new_robots[robo] -= 1

        dfs_starcraft(robots, new_resources, new_skipping, time_remaining - 1)

    global max_geode
    max_geode = 0

    max_bots_req = defaultdict(int, geode=float("inf"))
    for robot in blueprint:
        for req in blueprint[robot]:
            max_bots_req[req] = max(max_bots_req[req], blueprint[robot][req])

    dfs_starcraft(defaultdict(int, ore=1), defaultdict(int), set(), time_available)
    return max_geode


def part_1():
    TIME_REMAINING = 24

    blueprints = parse_input(INPUT)

    return sum(
        idx * get_max_geode(blueprint, TIME_REMAINING)
        for idx, blueprint in enumerate(blueprints, start=1)
    )

    # quality = 0
    # for idx, blueprint in enumerate(blueprints, start=1):
    #     quality += idx * get_max_geode(blueprint, TIME_REMAINING)

    # return quality


def part_2():
    from math import prod

    TIME_REMAINING = 32

    blueprints = parse_input(INPUT)

    return prod(
        get_max_geode(blueprint, TIME_REMAINING) for blueprint in blueprints[:3]
    )


print(f"{part_1() = }")
print(f"{part_2() = }")
