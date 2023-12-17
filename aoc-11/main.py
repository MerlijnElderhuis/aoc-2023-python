import os


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


def transpose(l):
    return ["".join(i) for i in zip(*l)]


def parse_input(lines):
    coords = []

    for y in lines:
        for x in y:
            coords((x, y))


def get_expanded_input(lines):
    res = []

    for i, line in enumerate(lines):
        if not any(x == "#" for x in line):
            print(f"Appending extra line at {i}")
            res.append(line)
        res.append(line)

    print(f"{res=}")
    res = transpose(res)
    print(f"{res=}")

    res2 = []

    print("T")

    for i, line in enumerate(res):
        if not any(x == "#" for x in line):
            print(f"Appending extra line at {i}")
            res2.append(line)
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
    print(galaxy_coords)

    res = 0
    for a in galaxy_coords:
        for b in galaxy_coords:
            res += abs(a[0] - b[0])
            res += abs(a[1] - b[1])
    print(res // 2)


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

    expanded_lines = get_expanded_input(lines)

    for line in expanded_lines:
        print(line)

    print("=" * 80)
    galaxies = galaxy_coords(expanded_lines)
    diffs(galaxies)


if __name__ == "__main__":
    main()
