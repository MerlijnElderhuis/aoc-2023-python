import re


def read_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        lines = f.read().splitlines()

    return lines


def line_to_game(line: str):
    steps = line.split(":")[-1]
    hands = steps.split(";")
    re_blue = "\d*\sblue"
    re_red = "\d*\sred"
    re_green = "\d*\sgreen"

    colours_hands = []

    for hand in hands:
        match_blue = re.findall(re_blue, hand)
        match_red = re.findall(re_red, hand)
        match_green = re.findall(re_green, hand)

        digits_blue = "".join(re.findall("\d", match_blue[0])) if match_blue else None

        digits_red = "".join(re.findall("\d", match_red[0])) if match_red else None

        digits_green = (
            "".join(re.findall("\d", match_green[0])) if match_green else None
        )
        res_green = int(digits_green) if digits_green else None
        res_blue = int(digits_blue) if digits_blue else None
        res_red = int(digits_red) if digits_red else None

        res_dict = {}
        if res_blue:
            res_dict["blue"] = res_blue
        if res_green:
            res_dict["green"] = res_green
        if res_red:
            res_dict["red"] = res_red
        colours_hands.append(res_dict)

    return colours_hands


def main():
    TEST = False
    input = "aoc-02/test_input.txt" if TEST else "aoc-02/input.txt"

    lines = read_input(input)

    games = []
    for line in lines:
        games.append(line_to_game(line))

    for game in games:
        print(f"{game=}")

    max_dict = {"red": 12, "green": 13, "blue": 14}

    tot = 0
    for i, game in enumerate(games):
        game_id = i + 1
        faulty = False
        for hand in game:
            if any(v > max_dict[k] for k, v in hand.items()):
                print(f"{game_id} FAULTY")
                faulty = True

        if not faulty:
            print(f"{game_id} succesfull.")
            tot += game_id

    print(tot)



if __name__ == "__main__":
    main()
    res = line_to_game(
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    )
