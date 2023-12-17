import os

SKIP_MULTIPLIER = 1000000


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


def transpose(l):
    return ["".join(i) for i in zip(*l)]


def transpose_galaxies(l):
    return [(y, x) for (x, y) in l]


def parse_input(lines):
    coords = []

    for y in lines:
        for x in y:
            coords((x, y))


def get_expanded_input(lines):
    res = []

    for i, line in enumerate(lines):
        if not any(x == "#" for x in line):
            # print(f"Appending extra line at {i}")
            for i in range(SKIP_MULTIPLIER):
                res.append(line)
        else:
            res.append(line)

    # print(f"{res=}")
    res = transpose(res)
    # print(f"{res=}")

    res2 = []

    # print("T")
    #
    for i, line in enumerate(res):
        if not any(x == "#" for x in line):
            # print(f"Appending extra line at {i}")
            for i in range(SKIP_MULTIPLIER):
                res2.append(line)
        else:
            res2.append(line)
    return transpose(res2)


def galaxy_coords(lines):
    coords = []
    for yi, y in enumerate(lines):
        for xi, x in enumerate(y):
            if x == "#":
                coords.append((xi, yi))
    return coords


def diffs(galaxy_coords):
    # print(galaxy_coords)

    res = 0
    for a in galaxy_coords:
        for b in galaxy_coords:
            res += abs(a[0] - b[0])
            res += abs(a[1] - b[1])
    print(res // 2)


def get_expanded_galaxies(galaxies):
    g_s = sorted(galaxies, key=lambda x: x[0])
    from copy import deepcopy

    gs_in = deepcopy(g_s)
    print(f"G_S in: {gs_in}")

    g_sc = []
    prev = 0
    skipped = 0

    for x, y in g_s:
        print("=" * 11)
        print(f"CUR: {(x,y )}")
        skip = x - prev - 1
        if skip > 0:
            print(f"ADDING skip {skip}")
            skipped += skip

        moved_cur = (x + skipped * (SKIP_MULTIPLIER-1), y)
        print(f"{skip=}")
        print(f"{skipped=}")
        print(f"{moved_cur=}")
        g_sc.append(moved_cur)

        prev = x
    print("NEW''''")
    print(g_sc)

    g_sc = transpose_galaxies(g_sc)
    g_sc = sorted(g_sc, key=lambda x: x[0])

    g_sc2 = []
    prev = 0
    skipped = 0

    for x, y in g_sc:
        print("=" * 11)
        print(f"CUR: {(x,y )}")
        skip = x - prev - 1
        if skip > 0:
            print(f"ADDING skip {skip}")
            skipped += skip

        moved_cur = (x + skipped * (SKIP_MULTIPLIER-1), y)
        print(f"{moved_cur=}")
        g_sc2.append(moved_cur)

        prev = x

    g_sc2 = transpose_galaxies(g_sc2)
    print(f"IN:")
    print(f"{gs_in}")
    print("NEW")
    print(sorted(g_sc2, key=lambda x: x[0]))

    return g_sc2


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
    galaxies = galaxy_coords(lines)
    new_exp = get_expanded_galaxies(galaxies)

    # expanded_lines = get_expanded_input(lines)
    # print("OLD:")
    # old_lines = sorted(galaxy_coords(expanded_lines), key=lambda x: x[0])
    # print(old_lines)

    # print("NEW:")
    # print(new_exp)

    # for line in expanded_lines:
    #     print(line)

    # print("=" * 80)
    print("new res")
    diffs(new_exp)
    # print("old res")
    # diffs(old_lines)


if __name__ == "__main__":
    main()
