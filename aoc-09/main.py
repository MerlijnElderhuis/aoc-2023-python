import os
from operator import sub
from itertools import accumulate


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


def parse_lines(lines):
    return [[int(num_str) for num_str in line.split()] for line in lines]


def calc_diff(num_list):
    res = []
    rest = num_list
    while True:
        # print("="*10)
        # print(res)
        # print(rest)
        el1, *rest = rest
        if rest == []:
            return res

        res.append(rest[0] - el1)


def diffs_for_line(num_list):
    res_lists = [num_list]

    next_diff = num_list
    while True:
        next_diff = calc_diff(next_diff)
        res_lists.append(next_diff)
        if all(n == 0 for n in next_diff):
            break

    return res_lists


def extrapolate(diff_lists):
    cur = 0
    for cur_list in reversed(diff_lists):
        cur = cur_list[0] - cur

    return cur


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
    print()

    num_lines = parse_lines(lines)

    res = 0
    for num_list in num_lines:
        diffs_lines = diffs_for_line(num_list)
        ex = extrapolate(diffs_lines)
        res += ex

    print(res)


if __name__ == "__main__":
    main()
