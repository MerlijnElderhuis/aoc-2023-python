from functools import cache
from itertools import groupby
import os


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


VALID_COUNT = 0

CHECKED_COUNT = 0


@cache
def check_valid(str, condition):
    # print("IS_VALID")
    # print(f"{str=}")
    # print(f"{condition=}")
    if has_longer_broken_substring(str, condition):
        print("L", end='', flush=True)
        return False


    global CHECKED_COUNT
    CHECKED_COUNT += 1
    if CHECKED_COUNT % 1000 == 0:
        print(".", end='', flush=True)
    split_str = [part for part in str.split(".") if part]
    # print(f"{split_str=}")
    parts = tuple(len(part) for part in split_str)
    # print(f"{parts}=")
    is_valid = parts == condition
    # print(f"{is_valid=}")

    return is_valid


def max_conseq(s):
    max = 0
    cur = 0

    for c in s:
        if c == "#":
            cur +=1
        else:
            if cur > max:
                max = cur
            cur  = 0
    return max

def has_longer_broken_substring(in_str, conditions):
    res = max_conseq(in_str)
    return res > max(conditions)

def is_finished(str):
    return "?" not in str


def replace_at(s, i, c):
    s_list = list(s)
    s_list[i] = c
    return "".join(s_list)


def parse_input(lines):
    res = []
    for line in lines:
        in_str, conditions = line.split()
        conditions = tuple(int(s) for s in conditions.split(","))
        res.append((in_str, conditions))

    return res


from copy import copy


def traverse(in_str, start_condition):
    # print()
    # print("TRAVERSE")
    # print(f"{in_str}")
    # print(f"{start_condition}")
    if is_finished(in_str):
        is_valid = check_valid(in_str, start_condition)
        if is_valid:
            print("W", sep=None)
        return [in_str] if is_valid else []
    else:
        next_index = in_str.index("?")
        in_str_copy1 = replace_at(copy(in_str), next_index, ".")
        in_str_copy2 = replace_at(copy(in_str), next_index, "#")

        return [
            *traverse(in_str_copy1, start_condition),
            *traverse(in_str_copy2, start_condition),
        ]


def unfold(line, conditions):
    res_line = ""
    res_conditions = tuple(conditions * 5)

    for i in range(5):
        res_line += line
        if i < 4:
            res_line += "?"

    return res_line, res_conditions


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

    in_lines = parse_input(lines)
    print(in_lines)

    """ Part 1
    
    # valid_sum = 0
    # for in_line in in_lines:
    #     valid_count = 0
    #     res = traverse(in_line[0], in_line[1], valid_count)
    #     print("LINE RES")
    #     print(in_line)
    #     print(res)
    #     valid_sum += len(res)

    # print(f"{valid_sum=}")
    """

    # Part 2

    valid_sum = 0
    for in_line in in_lines:
        unfolded_line, unfolded_conditions = unfold(in_line[0], in_line[1])
        print("=" * 50)
        print(f"{unfolded_line=}")
        print(f"{unfolded_conditions=}")
        # res = traverse(unfolded_line, unfolded_conditions)

        # print(res)
        # print(len(res))
        global CHECKED_COUNT
        CHECKED_COUNT = 0


if __name__ == "__main__":
    main()
    # print(unfold(".#", tuple([1])))

    # is_valid(".#.##.###", (1, 2, 3))
    # is_valid("##.##.###", (1, 2, 3))
    # print("=" * 10)

    # print(traverse(".###.##.#...", (3, 2, 1)))
    # print(traverse(".###.?#.#...", (3, 2, 1)))
    # print(VALID_COUNT)
