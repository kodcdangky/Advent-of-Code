def parse_data(raw: str):
    return raw.strip("\n").split(",")


def reindeer_hash(seq: str):
    r_hash = 0
    for char in seq:
        r_hash = ((r_hash + ord(char)) * 17) % 256
    return r_hash


def part_1(data: list[str]):
    return sum(reindeer_hash(seq) for seq in data)


def part_2(data: list[str]):
    boxes: list[dict[str, int]] = [{} for _ in range(256)]
    for instruction in data:
        if "=" in instruction:
            label, focal = instruction.split("=")
            boxes[reindeer_hash(label)][label] = int(focal)
        elif "-" in instruction:
            label = instruction.split("-")[0]
            boxes[reindeer_hash(label)].pop(label, None)

    return sum(box_indx * sum(lens_indx * box[lens]
                              for lens_indx, lens in enumerate(box, start=1))
               for box_indx, box in enumerate(boxes, start=1))


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(parse_data(raw)))
    print(part_2(parse_data(raw)))


if __name__ == "__main__":
    main()
