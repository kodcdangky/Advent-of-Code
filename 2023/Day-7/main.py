CARDS_1 = {
    "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10,
    "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

CARDS_2 = CARDS_1.copy()
CARDS_2["J"] = 1


class Hand:
    def __init__(self, cards: list[int], wildcard: int | None = None) -> None:
        self.cards = cards
        self.wildcard = wildcard
        self.rank = self.__hand_rank()

    def __hand_rank(self) -> int:
        """Give rank to this hand. The higher the rank the better the hand.
        6 means Five of a kind
        5 means Four of a kind
        4 means Full house (Three of a kind + a pair)
        3 means Three of a kind
        2 means Two pairs
        1 means One pair
        0 means High card (Nothing)

        Returns:
            int: This hand's rank
        """
        from collections import Counter

        counter = Counter(self.cards)
        wildcards_present = self.wildcard and counter[self.wildcard]
        match len(set(self.cards)):
            # Five of a kind
            case 1:
                return 6
            # Four of a kind / Full house
            case 2:
                return 6 if wildcards_present else 5 if max(counter.values()) == 4 else 4
            # Three of a kind / Two pairs
            case 3:
                if max(counter.values()) == 3:
                    return 5 if wildcards_present else 3
                else:
                    return 5 if wildcards_present == 2 else 4 if wildcards_present == 1 else 2
            # One pair
            case 4:
                return 3 if wildcards_present else 1
            # High card
            case _:
                return 1 if wildcards_present else 0

    def _lexi_compare(self, other) -> int:
        for card, other_card in zip(self.cards, other.cards):
            if card != other_card:
                return card - other_card
        return 0

    def __gt__(self, other):
        return self.rank > other.rank or (self.rank == other.rank and self._lexi_compare(other) > 0)

    def __lt__(self, other):
        return self.rank < other.rank or (self.rank == other.rank and self._lexi_compare(other) < 0)

    def __eq__(self, other):
        return self.__hand_rank() == other.__hand_rank() and self._lexi_compare == 0


def parse_data(raw: str, cards: dict[str, int], wildcard_sym: str | None = None) -> list[tuple[Hand, int]]:
    hands: list[tuple[Hand, int]] = []
    wildcard = None if not wildcard_sym else cards[wildcard_sym]
    for line in raw.splitlines():
        symbols, value = line.split()
        hands.append(
            (Hand(list(map(lambda symbol: cards[symbol], symbols)), wildcard),
             int(value))
        )
    return hands


def part_1(data: list[tuple[Hand, int]]):
    return sum(indx * value
               for indx, (_, value) in enumerate(sorted(data,
                                                        key=lambda hand_value: hand_value[0]), start=1))


def part_2(data: list[tuple[Hand, int]]):
    return sum(indx * value
               for indx, (_, value) in enumerate(sorted(data,
                                                        key=lambda hand_value: hand_value[0]), start=1))


def main():
    with open("input.txt") as file:
        raw = file.read()

    print(part_1(parse_data(raw, CARDS_1)))
    print(part_2(parse_data(raw, CARDS_2, "J")))


if __name__ == "__main__":
    main()
