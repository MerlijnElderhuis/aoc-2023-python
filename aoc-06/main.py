import os
import re


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


def parse_input(lines):
    lines_numbers = [line.split(":")[-1] for line in lines]

    lines_numbers = [re.sub(" +", " ", line.strip()) for line in lines_numbers]
    lines_numbers = [line.split(" ") for line in lines_numbers]

    games = list(map(list, zip(*lines_numbers)))
    games = [[int(record) for record in game] for game in games]

    return games


def calc_distance(time_tot, time_hold):
    time_left = time_tot - time_hold
    dist = time_left * time_hold
    return dist


def main():
    TEST = True
    if TEST:
        time_in = 71530
        distance = 940200
        file_name = "test_input.txt"
    else:
        time_in = 41_968_894
        distance = 214178911271055

    lines = read_input_lines(file_name)
    for line in lines:
        print(line)
    print("=" * 80)

    """
    Part 1
    """
    games = parse_input(lines)
    print(games)
    print("=" * 80)

    winners_count = []
    for game in games:
        time = game[0]
        record_distance = game[1]

        winners = []
        for hold_time in range(time + 1):
            if calc_distance(time, hold_time) > record_distance:
                winners.append(hold_time)
        winners_count.append(len(winners))

    tot = 1
    for winner_count in winners_count:
        tot = tot * winner_count
    print(tot)

    """
    Part 2
    """

    # How many ways to beat the `distance` in `time_in?`


5.94556058
3.6023333415

5945560
36023333

if __name__ == "__main__":
    main()
