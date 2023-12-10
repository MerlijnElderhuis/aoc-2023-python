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
        "n": (0, -1),
        "w": (-1, 0),
        "e": (1, 0),
        "s": (0, 1),
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
    res = (coord[0] + vec_dir_map()[dir][0], coord[1] + vec_dir_map()[dir][1])
    # print(f"res apply dir: {res}")
    return res


def valid_coord(coord):
    return (
        coord[0] >= 0
        and coord[0] < len(lines)
        and coord[1] >= 0
        and coord[1] < len(lines[0])
    )


def is_connected(coord, dir):
    coord_chr = lines[coord[0]][coord[1]]
    return dir in permitted_dirs(coord_chr)


def traverse_one(cur_coord, last_dir):
    cur_chr = lines[cur_coord[0]][cur_coord[1]]
    # print(f"{cur_chr=}")
    dirs = permitted_dirs(cur_chr)
    # print(f"permitted_dirs {dirs}")

    rev_last_dir = rev_dir(last_dir)
    # print(dirs)
    # print(f"{rev_last_dir=}")
    dirs = [dir for dir in dirs if dir != rev_last_dir]
    # print(f"permitted_dirs without last {dirs}")
    # print(f"{dirs=}")

    # # Ensure current coord is connected outwards
    # dirs = [dir for dir in dirs if is_connected(cur_coord, dir)]
    # print(f"permitted_dirs without unconnected outwards {dirs}")
    # Ensure outwards actually exists
    dirs = [dir for dir in dirs if valid_coord(apply_dir_to_coord(cur_coord, dir))]
    # print(f"permitted_dirs without invalid outwards {dirs}")
    # Ensure outwards has link inwards
    dirs = [
        dir
        for dir in dirs
        if is_connected(apply_dir_to_coord(cur_coord, dir), rev_dir(dir))
    ]
    # print(f"permitted_dirs without invalid inwards {dirs}")

    if not len(dirs) == 1:
        raise Exception

    return apply_dir_to_coord(cur_coord, dirs[0]), dirs[0]
    # print(dirs)


def traverse_while_possible(start, last_taken, max_steps=None):
    seen = [start]
    steps = 0
    max_steps = max_steps or 20000

    cur_coord = start
    last_dir = last_taken
    while True:
        if steps >= max_steps:
            print(f"STEPS EXCEEDED {max_steps}. cur_coord: {cur_coord}")
            break

        cur_coord, last_dir = traverse_one(cur_coord=cur_coord, last_dir=last_dir)
        steps += 1
        if cur_coord in seen:
            print(f"Seen cur coord: {cur_coord}. Steps: {steps}")
            break
        seen.append(cur_coord)

    return seen, steps


def get_loop_coord_outside_clockwise(prev_dir, next_dir):
    if next_dir == "n":
        return "w"
    if next_dir == "e":
        return "n"
    if next_dir == "s":
        return "e"
    if next_dir == "w":
        return "s"


def calc_outside_for_loop_coord(loop_coords):
    loop_coords_enh = []

    for i, loop_coord in enumerate(loop_coords):
        prev_coord = loop_coords[len(loop_coords) - 1] if i == 0 else loop_coords[i - 1]
        next_coord = loop_coords[0] if i == len(loop_coords) - 1 else loop_coords[i + 1]
        print("=" * 4)
        print(loop_coord)
        print(next_coord)


        prev_dir_vec = (loop_coord[0] - prev_coord[0], loop_coord[1] - prev_coord[1])
        prev_dir_nswe = coord_vec_to_dir(prev_dir_vec)
        print(prev_dir_nswe)

        next_dir_vec = (next_coord[0] - loop_coord[0], next_coord[1] - loop_coord[1])
        next_dir_nswe = coord_vec_to_dir(next_dir_vec)
        print(next_dir_vec)
        print(next_dir_nswe)

        loop_coords_enh.append((loop_coord, get_loop_coord_outside_clockwise(prev_dir_nswe, next_dir_nswe)))
    
    return loop_coords_enh

def calc_enclosed(loop_coord_enh):
    global lines

    accum = []

    for yi, y in enumerate(lines):
        for xi, x in enumerate(y):
            coord_is_in_loop = (xi, yi) in [l[0] for l in loop_coord_enh]

            if coord_is_in_loop:
                coord_in_loop, is_outer = [l for l in loop_coord_enh if l[0] == (xi, yi)][0]
                print(f"coord in loop: {(xi, yi)}: {coord_in_loop}, {is_outer}")
            else:
                print(f"coord NOT in loop: {(xi, yi)}")
            

        break

    print(accum)


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
    # print(get_adj((2, 2)))
    # print(get_adj((0, 2)))
    # print(get_adj((4, 4)))

    # traverse_one(coords_s, "w")
    # print("=" * 80)
    # traverse_one((1,4), "e")
    # traverse_one((4,2), "n")
    print("=" * 80)

    loop_coords, steps = traverse_while_possible(coords_s, "n", max_steps=20000)

    print(loop_coords)
    print(len(loop_coords))

    loop_coord_enh = calc_outside_for_loop_coord(loop_coords)
    print(loop_coord_enh)

    calc_enclosed(loop_coord_enh)


if __name__ == "__main__":
    main()
