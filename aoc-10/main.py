import os


lines = None


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


def transpose(l):
    return list(map(list, zip(*l)))


def get_s():
    global lines
    for xi, x in enumerate(lines):
        for yi, y in enumerate(x):
            if y == "S":
                return xi, yi


def vec_dir_map():
    return {
        "n": (0, 1),
        "w": (-1, 0),
        "e": (1, 0),
        "s": (0, -1),
    }


def coord_vec_to_dir(coord_dir):
    for nwse, coord in vec_dir_map().items():
        if coord == coord_dir:
            return nwse
    # if coord_dir == (0, 1):
    #     return "n"
    # if coord_dir == (-1, 0):
    #     return "w"
    # if coord_dir == (1, 0):
    #     return "e"
    # if coord_dir == (0, -1):
    #     return "s"


def permitted_dirs(chr):
    """
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
    """

    match chr:
        case "|":
            return ["n", "s"]
        case "-":
            return ["w", "e"]
        case "L":
            return ["n", "e"]
        case "J":
            return ["n", "w"]
        case "7":
            return ["s", "w"]
        case "F":
            return ["s", "e"]
        case "S":
            return ["n", "s", "w", "e"]
        case ".":
            return []


def rev_dir(chr):
    rev_dir_dict = {"n": "s", "e": "w", "s": "n", "w": "e"}
    return rev_dir_dict[chr]


def get_adj(coords):
    global lines
    # With diags
    # adj_coords = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

    # Without diags
    adj_coords = [(0, 1), (-1, 0), (1, 0), (0, -1)]

    if coords[0] == 0:
        adj_coords = [adj_coord for adj_coord in adj_coords if adj_coord[0] != -1]
    if coords[0] == len(lines) - 1:
        adj_coords = [adj_coord for adj_coord in adj_coords if adj_coord[0] != 1]
    if coords[1] == 0:
        adj_coords = [adj_coord for adj_coord in adj_coords if adj_coord[1] != -1]
    if coords[1] == len(lines[0]) - 1:
        adj_coords = [adj_coord for adj_coord in adj_coords if adj_coord[1] != 1]

    return [
        (
            (coords[0] + adj_coord[0], coords[1] + adj_coord[1]),
            lines[coords[0] + adj_coord[0]][coords[1] + adj_coord[1]],
        )
        for adj_coord in adj_coords
    ]


def get_connections(coords):
    char = lines[coords[0]][coords[1]]
    print(char)

def apply_dir_to_coord(coord, dir):
    return (coord)


def is_connected(coord, dir):
    coord_chr = lines[coord[0]][coord[1]]
    return dir in permitted_dirs(coord_chr)


def traverse(cur_coord, last_dir):
    cur_chr = lines[cur_coord[0]][cur_coord[1]]
    perm_dirs = permitted_dirs(cur_chr)

    rev_last_dir = rev_dir(last_dir)
    print(perm_dirs)
    print(rev_last_dir)
    perm_dirs_without_last = [dir for dir in perm_dirs if dir != rev_last_dir]
    print(perm_dirs_without_last)

    perm_connected_dirs_without_last = [dir for dir in perm_dirs_without_last if dir !=is_connected(cur_coord, dir)]





def main():
    TEST = True
    global lines
    if TEST:
        file_name = "test_input.txt"
    else:
        file_name = "input.txt"

    liness = read_input_lines(file_name)
    for line in liness:
        print(line)
    print("=" * 80)
    lines = transpose(liness)

    coords_s = get_s()
    print(coords_s)

    # get_connections((0, 2))
    print(get_adj((2, 2)))
    print(get_adj((0, 2)))
    print(get_adj((4, 4)))

    traverse(coords_s, "e")


if __name__ == "__main__":
    main()
