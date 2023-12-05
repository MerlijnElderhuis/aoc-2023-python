import re


def read_input_lines(input_file: str) -> list[str]:
    root = "aoc-03"
    with open(f"{root}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


def is_symbol(char: str) -> bool:
    if char.isdigit():
        return False
    else:
        return char != "."


def is_adjacent(coordA, coordB):
    return coordA[0] in [coordB[0] - 1, coordB[0], coordB[0] + 1] and coordA[1] in [
        coordB[1] - 1,
        coordB[1],
        coordB[1] + 1,
    ]


def write_num_to_list(result_list, num_accum, i, j):
    j_list = list(range(j - len(num_accum), j))
    result_list.append((num_accum, [(j_l, i) for j_l in j_list]))


def numbers_from_lines(lines: list[str]):
    number_results = []

    num_accum = ""
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isdigit():
                num_accum += char
            else:
                if num_accum:
                    print(f"Writing {num_accum} to list INLINE")
                    write_num_to_list(number_results, num_accum, i, j)
                    num_accum = ""

        if num_accum:
            print(f"Writing {num_accum} to list ENDLINE")
            write_num_to_list(number_results, num_accum, i, j)
            num_accum = ""

    return number_results


def symbol_coords_from_lines(lines: list[str]):
    symbols = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if is_symbol(char):
                symbols.append((char, (j, i)))
    return symbols


def main():
    TEST = False
    if TEST:
        file_name = "test_input.txt"
    else:
        file_name = "input.txt"

    input_lines = read_input_lines(file_name)
    print("=" * 80)
    nums_from_lines = numbers_from_lines(input_lines)
    for num_from_lines in nums_from_lines:
        print(num_from_lines)

    symbol_coords = symbol_coords_from_lines(input_lines)
    print(symbol_coords)

    nums_to_sum = []
    for num_str, num_coords in nums_from_lines:
        for num_coord in num_coords:
            if any(
                is_adjacent(num_coord, sym_coord)
                for (symbol, sym_coord) in symbol_coords
            ):
                print(f"appending {num_str}")
                nums_to_sum.append(num_str)
                break

    nums_ints = [int(num) for num in nums_to_sum]
    print(sum(nums_ints))


if __name__ == "__main__":
    main()
