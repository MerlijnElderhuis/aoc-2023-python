import os


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


def parse_inputs(lines):
    lines.append("")
    seeds = lines[0]
    seeds = [int(s) for s in seeds.split(":")[-1].strip().split(" ")]

    line_nr = 1

    seed_to_soil = None
    soil_to_fertilizer = None
    fertilizer_to_water = None
    water_to_light = None
    light_to_temperature = None
    temperature_to_humidity = None
    humidity_to_location = None

    fill_order = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    ]

    fill_nr = 0
    prev_line = None
    acc = []

    while line_nr < len(lines):
        cur_line = lines[line_nr]
        print(cur_line)

        if not cur_line:
            pass

        if cur_line and not prev_line:
            # arrived title. Should continue
            pass

        if cur_line and prev_line:
            # start adding to acc
            acc.append(cur_line)

        if not cur_line and prev_line:
            # fill add, reset, move up fill_nr
            fill_order[fill_nr] = acc
            acc = []
            fill_nr += 1

        prev_line = cur_line
        line_nr += 1

    print(f"{fill_order=}")

    res_vars = []

    for var in fill_order:
        res = []
        for var_line in var:
            dest, src, nr = tuple(var_line.split(" "))
            res.append({"dest": int(dest), "src": int(src), "nr": int(nr)})

        res_vars.append(res)

    print(f"{res_vars=}")
    return seeds, res_vars


def map_id(id, map):
    for map_entry in map:
        if id >= map_entry["src"] and id < map_entry["src"] + map_entry["nr"]:
            return id + map_entry["dest"] - map_entry["src"]
    return id


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

    seeds, res_vars = parse_inputs(lines)

    print(f"{seeds=}")

    seed_to_soil = res_vars[0]
    soil_to_fertilizer = res_vars[1]
    fertilizer_to_water = res_vars[2]
    water_to_light = res_vars[3]
    light_to_temperature = res_vars[4]
    temperature_to_humidity = res_vars[5]
    humidity_to_location = res_vars[6]

    print(f"{seed_to_soil=}")
    print(f"{soil_to_fertilizer=}")
    print(f"{fertilizer_to_water=}")
    print(f"{water_to_light=}")
    print(f"{light_to_temperature=}")
    print(f"{temperature_to_humidity=}")
    print(f"{humidity_to_location=}")

    print("=" * 80)
    print(0, map_id(0, seed_to_soil))
    print(1, map_id(1, seed_to_soil))
    print(48, map_id(48, seed_to_soil))
    print(49, map_id(49, seed_to_soil))
    print(50, map_id(50, seed_to_soil))
    print(51, map_id(51, seed_to_soil))

    print("..")
    print(96, map_id(96, seed_to_soil))
    print(97, map_id(97, seed_to_soil))
    print(98, map_id(98, seed_to_soil))
    print(99, map_id(99, seed_to_soil))
    print(100, map_id(100, seed_to_soil))

    def traverse_maps(id) -> int:
        maps = [
            seed_to_soil,
            soil_to_fertilizer,
            fertilizer_to_water,
            water_to_light,
            light_to_temperature,
            temperature_to_humidity,
            humidity_to_location,
        ]

        cur = id
        for map in maps:
            cur = map_id(cur, map)

        return cur

    print(min([traverse_maps(seed_id) for seed_id in seeds]))


if __name__ == "__main__":
    main()
    # map_id(0, )
