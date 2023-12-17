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

    # print(lines)

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
                # print(f"RETURNING FALSE. {lower_i};{upper_i}")
                # print(lower)
                # print(upper)
                return False
        except IndexError:
            return True

        i += 1


def replace_at(s, i, c):
    s_list = list(s)
    s_list[i] = c
    return "".join(s_list)


def get_smudged_solution(line_list, orig_found):
    print("NEW SMUDGE ATTEMPT")
    print("BEFORE SMUDGE")
    for line in line_list:
        print(line)
    found_list = []
    tot = 0

    print(f"{orig_found=}")

    for xi, x in enumerate(line_list):
        for yi, y in enumerate(x):
            replaced_with = "#" if line_list[xi][yi] == "." else "."
            print(f"REPLACING {line_list[xi][yi]} with {replaced_with} AT ({xi}, {yi})")
            from copy import deepcopy
            line_list_copy = deepcopy(line_list)
            line_list_copy[xi] = replace_at(line_list_copy[xi], yi, replaced_with)

            print()
            for line in line_list_copy:
                print(line)

            # for line in line_list_copy:
            #     print(line)


            hor_starts, ver_starts = line_with_identical_adjacement(line_list_copy)
            print(hor_starts)
            print(ver_starts)

            for hor_start in hor_starts:
                if is_perfect(line_list_copy, hor_start, "h") and (hor_start, "h") != orig_found:
                    tot += 100 * (hor_start[0] + 1)
                    print(f"FOUND HOR ALTERNATIVE {hor_start}")
                    return tot
                    found_list.append((hor_start, "h"))
                    # orig_found = (hor_start, "h")
                    break

            for ver_start in ver_starts:
                if is_perfect(line_list_copy, ver_start, "v") and (ver_start, "v") != orig_found:
                    tot += ver_start[0] + 1
                    print(f"FOUND VER ALTERNATIVE {ver_start}")
                    return tot
                    found_list.append((ver_start, "v"))
                    # orig_found = (ver_start, "v")
                    break

    if found_list:
        print(f"{orig_found=}")
        print(f"FOUND ALTERNATIVE: {found_list}")

        return found_list[0]

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
    tot2 = 0

    smudged_not_found = []

    for lineI, line_list in enumerate(line_lists):
        print("=" * 10)
        for line in line_list:
            print(line)

        print()
        found = False
        found_list = []

        hor_starts, ver_starts = line_with_identical_adjacement(line_list)
        print(hor_starts)
        print(ver_starts)

        for hor_start in hor_starts:
            if is_perfect(line_list, hor_start, "h"):
                print(f"FOUND HOR START {hor_start}")
                tot += 100 * (hor_start[0] + 1)
                found_list.append(hor_start)
                orig_found = (hor_start, "h")

        for ver_start in ver_starts:
            if is_perfect(line_list, ver_start, "v"):
                print(f"FOUND VER START {ver_starts}")
                tot += ver_start[0] + 1
                found_list.append(ver_start)
                orig_found = (ver_start, "v")

        print(f"{orig_found=}")
        if not found:
            # print("NOT FOUND")
            pass
        else:
            print(f"FOUND: {found_list}")
        

        new_answer = get_smudged_solution(line_list, orig_found)
        if not new_answer:
            smudged_not_found.append(lineI)

        tot2 += new_answer or 0

    print("tot")
    print(tot)


    print("tot2")
    print(tot2)

    print("smudged_not_found")
    print(smudged_not_found)


if __name__ == "__main__":
    main()


# [68, 71, 83, 93]

# Tried
# PT1
# 29725 (low)
# 29791 (low)
    
# PT 2
# 30323 (low)
# 30442
    
