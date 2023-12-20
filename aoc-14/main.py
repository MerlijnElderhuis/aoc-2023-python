import os


def transpose(l):
    return ["".join(i) for i in zip(*l)]


def flip(l):
    res = []
    for line in l:
        rev_line = list(line)
        rev_line.reverse()
        # print(rev_line)
        res.append("".join(rev_line))
    return res

    return ["".join(list(line).reverse()) for line in l]


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


mycache = []


def move_rocks(input: list[str]):
    input_trans = transpose(input)

    res_cols = []

    for j, col in enumerate(input_trans):
        # block_rock_coords = [i for i, val in enumerate(col) if val == "#"]
        # print(f"col {j}")
        # print(block_rock_coords)

        cur_block_rock = -1
        block_map = {}

        for i, chr in enumerate(col):
            if chr == "O":
                block_map[cur_block_rock] = (
                    block_map[cur_block_rock] + 1 if cur_block_rock in block_map else 1
                )

            if chr == "#":
                cur_block_rock = i

        # print(f"{block_map=}")

        # cur_block_index = -1
        cur_block_counter = block_map.get(-1, 0)
        cur_col_index = 0
        cur_build_col = ""
        while True:
            if cur_col_index == len(col):
                break

            if cur_block_counter:
                cur_build_col += "O"
                cur_block_counter = cur_block_counter - 1
                # print()
            elif col[cur_col_index] == "#":
                cur_build_col += "#"
                cur_block_counter = block_map.get(cur_col_index, 0)
            else:
                cur_build_col += "."

            cur_col_index += 1

        # print("cur_build_col")
        # print(cur_build_col)

        res_cols.append(cur_build_col)
        # print("=" * 10)
        # print()

    # print("=" * 20)
    # print(res_cols)
    return transpose(res_cols)


def calc_score(moved_rocks):
    max_score = len(moved_rocks)
    print("max_score")
    print(max_score)

    tot = 0

    for i, rocks in enumerate(moved_rocks):
        tot += (max_score - i) * len([r for r in rocks if r == "O"])

    return tot


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

    i = 0
    from copy import deepcopy

    moved_rocks = lines
    moved_rocks = move_rocks(moved_rocks)
    for moved_rock_line in moved_rocks:
        print(moved_rock_line)

    while True:
        # print(calc_score(moved_rocks))
        print("="*10)

        for i in range(4):
            print(i)
            print("after turn, before move")
            # moved_rocks = transpose(moved_rocks)
            # moved_rocks = transpose(moved_rocks)
            moved_rocks = move_rocks(moved_rocks)
            moved_rocks = transpose(moved_rocks)
            moved_rocks = flip(moved_rocks)

            for moved_rock_line in moved_rocks:
                print(moved_rock_line)
            print()
            print("after move")

            for moved_rock_line in moved_rocks:
                print(moved_rock_line)
            pass

        print()
        for moved_rock_line in moved_rocks:
            print(moved_rock_line)
        
        pass

        # moved_rocks = flip(moved_rocks)

        # moved_rocks = move_rocks(moved_rocks)

        # print()
        # for moved_rock_line in moved_rocks:
        #     print(moved_rock_line)

        # pass

        # moved_rocks = flip(moved_rocks)
        # moved_rocks = move_rocks(moved_rocks)
        # moved_rocks = transpose(moved_rocks)
        # moved_rocks = move_rocks(moved_rocks)
        # moved_rocks = flip(moved_rocks)


        # if moved_rocks in mycache:
        # # if i > 1000:
        #     print("DONE")
        #     print(i)
        #     print(calc_score(moved_rocks))
        #     break

        # mycache.append(moved_rocks)

        # i += 1
        # if i % 100 == 0:
        #     print(i)

    # score = calc_score(moved_rocks)
    # print(score)


# def get_rocks_for_col(col):


if __name__ == "__main__":
    main()
