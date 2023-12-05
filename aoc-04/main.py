from functools import lru_cache
import os


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


def lines_to_cards(lines):
    card_per_line = []
    for i, line in enumerate(lines):
        cardinfo = line.split(":")[-1]
        cardinfo = cardinfo.strip()
        cardinfo = cardinfo.replace("  ", " ")

        cardsplit = cardinfo.split("|")
        numbers1 = cardsplit[0].strip()
        numbers2 = cardsplit[1].strip()

        card_per_line.append(
            (
                [int(num) for num in numbers1.split(" ")],
                [int(num) for num in numbers2.split(" ")],
            )
        )
    return card_per_line


def main():
    TEST = False
    if TEST:
        file_name = "test_input.txt"
    else:
        file_name = "input.txt"

    lines = read_input_lines(file_name)
    for line in lines:
        print(line)

    print("=" * 80)

    all_cards = lines_to_cards(lines)
    all_cards_dict = {i: card for i, card in enumerate(all_cards)}

    for card in all_cards:
        print(card)

    print("=" * 80)

    ### Pt1
    pts_1 = 0
    for i, card in enumerate(all_cards):
        card_intersect = set(card[0]) & set(card[1])
        if not card_intersect:
            continue
        else:
            print(f"Found intersect on Card {i}: {len(card_intersect)}")
            pts_card = pow(2, (len(card_intersect) - 1))
            print(f"adding pts: {pts_card}")
            pts_1 += pts_card

    def calc_card_res(card_nr: int) -> int:
        card = all_cards_dict[card_nr]
        card_intersect = set(card[0]) & set(card[1])
        return len(card_intersect)

    all_card_count = 0

    @lru_cache(300)
    def calc_for_card(card_nr: int):
        print(".")
        nonlocal all_card_count
        card_res = calc_card_res(card_nr)
        int_res = card_res
        print(f"Card {card_nr} has {card_res} results.")
        for i in list(range(0, card_res)):
            target_card_nr = card_nr + i + 1
            # print(f"Adding {target_card_nr}")
            int_res += calc_for_card(target_card_nr)

        return int_res

    tot = 0
    for card_nr in all_cards_dict.keys():
        tot += calc_for_card(card_nr)

    pts_2 = tot + len(all_cards)

    print("Part 1")
    print(pts_1)
    print("Part 2")
    print(pts_2)


if __name__ == "__main__":
    main()
