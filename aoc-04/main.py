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
    TEST = True
    if TEST:
        file_name = "test_input.txt"
    else:
        file_name = "input.txt"

    lines = read_input_lines(file_name)
    for line in lines:
        print(line)

    print("=" * 80)

    all_cards = lines_to_cards(lines)
    for card in all_cards:
        print(card)

    print("=" * 80)

    ### Pt1
    pts = 0
    for i, card in enumerate(all_cards):
        card_intersect = set(card[0]) & set(card[1])
        if not card_intersect:
            continue
        else:
            print(f"Found intersect on Card {i}: {len(card_intersect)}")
            pts_card = pow(2, (len(card_intersect) - 1))
            print(f"adding pts: {pts_card}")
            pts += pts_card


if __name__ == "__main__":
    main()
