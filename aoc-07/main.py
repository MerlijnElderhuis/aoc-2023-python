from dataclasses import dataclass
from enum import Enum
from itertools import groupby
import os
from functools import total_ordering
import copy

def test_order():
    # print(Card('a') == Card('a'))
    print(Card("2") == Card("2"))
    print(Card("2") < Card("3"))
    print(Card("a") < Card("k"))
    print(Card("a") > Card("K"))


def test_hand_property():
    print("hand")
    print(HandProperty.five_kind > HandProperty.four_kind)
    print(HandProperty.high_card > HandProperty.four_kind)


def test_hand():
    print(
        Hand([Card("3"), Card("3"), Card("2"), Card("2"), Card("3")])
        > Hand([Card("3"), Card("3"), Card("2"), Card("2"), Card("2")])
    )


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


@total_ordering
@dataclass
class Card:
    sym: str

    def __init__(self, sym: str):
        self.sym = sym.lower()

    def __lt__(self, other):
        if self.sym == "j" and other.sym == "j":
            return False
        if self.sym == "j" and not other.sym == "j":
            return True
        if self.sym != "j" and other.sym == "j":
            return False
        if self.sym.isdigit() and not other.sym.isdigit():
            return True
        elif not self.sym.isdigit() and not other.sym.isdigit():
            ordering = ["a", "k", "q", "t"]
            return ordering.index(self.sym) > ordering.index(other.sym)
        else:
            return self.sym < other.sym

    def __eq__(self, other):
        return self.sym == other.sym


@total_ordering
@dataclass
class HandProperty(Enum):
    five_kind = 1
    four_kind = 2
    full_house = 3
    three_kind = 4
    two_pair = 5
    one_pair = 6
    high_card = 7

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.name)


@dataclass
@total_ordering
class Hand:
    cards: list[Card]
    hand_property: HandProperty

    def __init__(self, cards: list[Card]):
        assert len(cards) == 5
        self.cards = cards
        self.hand_property = max(
            self.calc_hand_property(cards_poss) for cards_poss in self.hand_perms(cards)
        )

    def __repr__(self):
        return f"{[card.sym for card in self.cards]} | {self.hand_property}"

    @classmethod
    def hand_perms(cls, cards_in: list[Card]):
        if Card("j") not in cards_in:
            return [cards_in]
        else:
            # gen perms
            print(f"input {cards_in}")
            card_perms = []
            cards_in_len = copy.deepcopy(cards_in)
            j_count = [card for card in cards_in_len if card == Card("j")]
            print(len(j_count))
            for i in j_count:
                cards_in_tmp = copy.deepcopy(cards_in)
                cards_in_tmp.remove(Card("j"))
                for sym in ["2", "3", "4", "5", "6", "7", "8", "9", "j", "t", "q", "k", "a"]:
                    cards_in_tmp_copy = copy.deepcopy(cards_in_tmp)
                    cards_in_tmp_copy.append(Card(sym))
                    card_perms.append(cards_in_tmp_copy)


            for card_perm in card_perms:
                print(f"Generated perm {card_perm}")
            return card_perms

    @classmethod
    def from_stringlist(cls, card_strings: list[str]):
        return cls([Card(card_str) for card_str in card_strings])

    @classmethod
    def calc_hand_property(cls, cards: list[Card]):
        cards_grouped = {}
        for (
            key,
            values,
        ) in groupby(iterable=sorted(cards)):
            cards_grouped[key.sym] = list(values)

        if len(cards_grouped) == 1:
            return HandProperty.five_kind
        if len(cards_grouped) == 2:
            if max([len(values) for values in cards_grouped.values()]) == 4:
                # if max(len(cards_grouped.values())) == 4:
                return HandProperty.four_kind
            else:
                return HandProperty.full_house
        if len(cards_grouped) == 3:
            if max([len(values) for values in cards_grouped.values()]) == 3:
                return HandProperty.three_kind
            else:
                return HandProperty.two_pair
        if len(cards_grouped) == 4:
            return HandProperty.one_pair

        # default
        return HandProperty.high_card

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if self.hand_property != other.hand_property:
            return self.hand_property < other.hand_property
        else:
            cards_zipped = zip(self.cards, other.cards)
            for self_card, other_card in cards_zipped:
                if self_card != other_card:
                    print(f"checking cards {self_card, other_card}")
                    return self_card < other_card


def parse_input(lines) -> list[tuple[Hand, int]]:
    hands_bets = []
    for line in lines:
        card_strings, bet = line.split()
        hands_bets.append((Hand.from_stringlist(card_strings), int(bet)))

    return hands_bets


def main():
    TEST = True
    if TEST:
        file_name = "test_input.txt"
    else:
        file_name = "input.txt"

    lines = read_input_lines(file_name)
    for line in lines:
        print(line)
    print("=" * 80)

    hands_bets = parse_input(lines)

    # hands_bets_sorted = sorted(hands_bets, key=lambda x: x[0], reverse=True)
    hands_bets.sort(key=lambda x: x[0], reverse=True)

    for hand in hands_bets:
        print(str(hand))

    res = 0
    for i, (hand, bet) in enumerate(hands_bets):
        multiplier = len(hands_bets) - i
        res += bet * multiplier

    print(res)


if __name__ == "__main__":
    # test_hand_property()
    # test_hand()
    # print(Hand.from_stringlist(["8", "2", "8", "2", "8"]))

    hand1 = Hand.from_stringlist(["2", "2", "2", "2", "8"])
    hand2 = Hand.from_stringlist(["a", "7", "7", "7", "7"])

    # print(Hand.from_stringlist(strs) < Hand.from_stringlist(strs1))
    # print('Card("a") > Card("t")')
    # print(Card("a") > Card("t"))
    # print(Card("t") > Card("j"))
    hand3 = Hand.from_stringlist(["t", "t", "t", "t", "6"])
    hand4 = Hand.from_stringlist(["a", "8", "8", "8", "8"])
    # hand5 = Hand.from_stringlist(["8", "a", "a", "8", "8"])
    # hand6 = Hand.from_stringlist(["a", "a", "8", "8", "8"])
    # hand7 = Hand.from_stringlist(["a", "a", "a", "8", "8"])

    # hands = [hand3, hand1, hand2, hand4, hand5, hand6, hand7]
    hands = [hand1, hand2, hand3, hand4]
    # print(hands)
    hands_orig = [hand1, hand2, hand3, hand4]

    # print(hand1 > hand2)
    # print(hand2 > hand3)
    # print(hand3 > hand4)

    # print(hands)
    # print(sorted(hands, reverse=True))

    # hands.sort()
    # for hand in hands:
    #     print(hand)

    # print("hands == hands_orig")
    # print(hands == hands_orig)

    # print(hand7 > hand6)
    main()
