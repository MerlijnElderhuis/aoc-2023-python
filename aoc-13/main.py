import os


def read_input_lines(input_file: str) -> list[list[str]]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")

    lines_list = []
    with open(f"{dir}/{input_file}", "r") as f:
        blocks = f.read().split("\n\n")

        # print(blocks)
        for block in blocks:
            lines_list.append(block.splitlines())

    return lines_list


def transpose(l):
    return ["".join(i) for i in zip(*l)]


def line_with_identical_adjacement(lines):
    hor_starts = []
    ver_starts = []

    print(lines)

    for i, linei in enumerate(lines):
        iminus = i - 1
        if iminus not in [-1, len(lines)]:
            if lines[iminus] == linei:
                # print(lines[iminus])
                # print(linei)
                # print(iminus, i)
                hor_starts.append((iminus, i))

    linesT = transpose(lines)

    for i, linei in enumerate(linesT):
        iminus = i - 1
        if iminus not in [-1, len(linesT)]:
            if linesT[iminus] == linei:
                # print(iminus, i)
                ver_starts.append((iminus, i))

    return hor_starts, ver_starts


def is_perfect(line_list, start, hv):
    if hv == "v":
        line_list = transpose(line_list)

    i = 1

    while True:
        lower_i = start[0] - i

        upper_i = start[1] + i

        try:
            if lower_i == -1:
                raise IndexError

            lower = line_list[lower_i]
            upper = line_list[upper_i]

            if not lower == upper:
                print(f"RETURNING FALSE. {lower_i};{upper_i}")
                print(lower)
                print(upper)
                return False
        except IndexError:
            return True

        i += 1


def main():
    TEST = False
    if TEST:
        file_name = "test_input.txt"
    else:
        file_name = "input.txt"

    line_lists = read_input_lines(file_name)

    print(len(line_lists))
    # print(line_lists[0] == line_lists[1])
    # for line_list in line_lists:
    #     for line in line_list:
    #         print(line)
    #     print()
    # print("=" * 80)

    tot = 0

    for line_list in line_lists:
        print("=" * 10)
        for line in line_list:
            print(line)

        print()
        hor_starts, ver_starts = line_with_identical_adjacement(line_list)
        print(hor_starts)
        print(ver_starts)

        found = False
        found_list = []

        for hor_start in hor_starts:
            if is_perfect(line_list, hor_start, "h"):
                print(f"FOUND HOR START {hor_start}")
                tot += 100 * (hor_start[0] + 1)
                found_list.append(hor_start)
                found = True

        for ver_start in ver_starts:
            if is_perfect(line_list, ver_start, "v"):
                print(f"FOUND VER START {ver_starts}")
                tot += ver_start[0] + 1
                found_list.append(ver_start)
                found = True

        if not found:
            print("NOT FOUND")
        else:
            print(f"FOUND: {found_list}")

    print("tot")
    print(tot)


if __name__ == "__main__":
    main()


# Tried
# 29725 (low)
# 29791 (low)
