from functools import cache
import os


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


VALID_COUNT = 0


@cache
def check_valid(str, condition, valid_count):
    # print("IS_VALID")
    # print(f"{str=}")
    # print(f"{condition=}")
    global VALID_COUNT
    split_str = [part for part in str.split(".") if part]
    # print(f"{split_str=}")
    parts = tuple(len(part) for part in split_str)
    # print(f"{parts}=")
    is_valid = parts == condition
    # print(f"{is_valid=}")

    if is_valid:
        valid_count += 1
    return is_valid


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


def traverse(in_str, start_condition, valid_count):
    # print()
    # print("TRAVERSE")
    # print(f"{in_str}")
    # print(f"{start_condition}")
    if is_finished(in_str):
        return [in_str] if check_valid(in_str, start_condition, valid_count) else []
    else:
        next_index = in_str.index("?")
        in_str_copy1 = replace_at(copy(in_str), next_index, ".")
        in_str_copy2 = replace_at(copy(in_str), next_index, "#")

        return [
            *traverse(in_str_copy1, start_condition, valid_count),
            *traverse(in_str_copy2, start_condition, valid_count),
        ]


def unfold(line, conditions):
    res_line = []
    res_conditions = tuple(conditions * 5)

    for i in range(5):
        res_line += line
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

    valid_sum = 0
    for in_line in in_lines:
        valid_count = 0
        res = traverse(in_line[0], in_line[1], valid_count)
        print("LINE RES")
        print(in_line)
        print(res)
        valid_sum += len(res)

    print(f"{valid_sum=}")


if __name__ == "__main__":
    main()

    # is_valid(".#.##.###", (1, 2, 3))
    # is_valid("##.##.###", (1, 2, 3))
    # print("=" * 10)

    # print(traverse(".###.##.#...", (3, 2, 1)))
    # print(traverse(".###.?#.#...", (3, 2, 1)))
    # print(VALID_COUNT)
