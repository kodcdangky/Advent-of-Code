### https://adventofcode.com/2022/day/20

INPUT = "input.txt"

def mix(cipher, plain_pos = None):
    plain_pos = plain_pos or list(range(len(cipher)))

    for idx, cipher_int in enumerate(cipher):

        new_pos = plain_pos[idx] + cipher_int
        if new_pos % (len(cipher) - 1):
            new_pos %= len(cipher) - 1
        else:
            new_pos = new_pos <= 0 and len(cipher) - 1

        old_pos = plain_pos[idx]
        for update_idx in range(len(plain_pos)):
            plain_pos[update_idx] -= plain_pos[update_idx] > old_pos
            plain_pos[update_idx] += plain_pos[update_idx] >= new_pos

        plain_pos[idx] = new_pos

    return plain_pos


def part_1():
    THOUSANDS = 3

    with open(INPUT) as file:
        cipher = tuple(map(int, file.read().splitlines()))

    plain_pos = mix(cipher)

    return sum(
        cipher[
            plain_pos.index(
                (plain_pos[cipher.index(0)] + ((thousand + 1) * 1000)) % len(cipher)
            )
        ]
        for thousand in range(THOUSANDS)
    )


def part_2():
    KEY = 811589153
    THOUSANDS = 3
    ROUNDS = 10
    with open(INPUT) as file:
        cipher = tuple(map(lambda ciph: KEY * int(ciph), file.read().splitlines()))

    plain_pos = None
    for _ in range(ROUNDS):
        plain_pos = mix(cipher, plain_pos)

    return sum(
        cipher[
            plain_pos.index(
                (plain_pos[cipher.index(0)] + ((thousand + 1) * 1000)) % len(cipher)
            )
        ]
        for thousand in range(THOUSANDS)
    )


print(f"{part_1() = }")
print(f"{part_2() = }")
