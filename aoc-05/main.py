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

    # print(f"{fill_order=}")

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


def map_id_rev(id, map):
    for map_entry in map:
        if id >= map_entry["dest"] and id < map_entry["dest"] + map_entry["nr"]:
            mapped_id = id + map_entry["src"] - map_entry["dest"]
            # print(f"Returning mapped id {mapped_id}")
            return mapped_id
    # print(f"Returning own id {id}")
    return id


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

    seeds, res_vars = parse_inputs(lines)

    # print(f"{seeds=}")

    seed_to_soil = res_vars[0]
    soil_to_fertilizer = res_vars[1]
    fertilizer_to_water = res_vars[2]
    water_to_light = res_vars[3]
    light_to_temperature = res_vars[4]
    temperature_to_humidity = res_vars[5]
    humidity_to_location = res_vars[6]

    print(f"{seed_to_soil=}")
    # print(f"{soil_to_fertilizer=}")
    # print(f"{fertilizer_to_water=}")
    # print(f"{water_to_light=}")
    # print(f"{light_to_temperature=}")
    # print(f"{temperature_to_humidity=}")
    # print(f"{humidity_to_location=}")

    print("=" * 80)
    # print(0, map_id(0, seed_to_soil))
    # print(1, map_id(1, seed_to_soil))
    # print(48, map_id(48, seed_to_soil))
    # print(49, map_id(49, seed_to_soil))
    # print(50, map_id(50, seed_to_soil))
    # print(51, map_id(51, seed_to_soil))

    # print("..")
    # print(96, map_id(96, seed_to_soil))
    # print(97, map_id(97, seed_to_soil))
    # print(98, map_id(98, seed_to_soil))
    # print(99, map_id(99, seed_to_soil))
    # print(100, map_id(100, seed_to_soil))

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

    seed_pairs = []
    total_seed_count = 0
    prev_seed = None
    for i, seed in enumerate(seeds):
        if i % 2 == 0:
            prev_seed = seed
        else:
            seed_pairs.append((prev_seed, seed))
            total_seed_count += seed
    print(f"{seed_pairs=}")

    # print("Total seed count: {:,}".format(total_seed_count))

    pt2_seeds = []

    # print("extending")
    min_seed = None
    seeds_traversed = 0
    seeds_traversed_last_iter = 0
    from time import time

    time_now = time()

    # for seed_pair in seed_pairs:
    #     for seed_id in range(seed_pair[0], seed_pair[0] + seed_pair[1]):
    #         seeds_traversed += 1
    #         seeds_traversed_last_iter += 1
    #         if seeds_traversed % 1000 == 0:
    #             print(f"Total: {seeds_traversed=}")
    #             print(f"This iter: {seeds_traversed_last_iter}")
    #             print(f"seeds/s: {seeds_traversed_last_iter / (time() - time_now)}")
    #             seeds_traversed_last_iter = 0
    #             time_now = time()

    #         trav_id = traverse_maps(seed_id)
    #         if min_seed is None or trav_id < min_seed:
    #             min_seed = trav_id

    #     pt2_seeds.extend(list())

    # print(f"{pt2_seeds=}")
    # print("traversing")

    # Part 1
    # print(min([traverse_maps(seed_id) for seed_id in seeds]))

    # Part 2
    # print(min([traverse_maps(seed_id) for seed_id in pt2_seeds]))
    # print(min_seed)

    def traverse_maps_rev(id) -> int:
        maps = [
            humidity_to_location,
            temperature_to_humidity,
            light_to_temperature,
            water_to_light,
            fertilizer_to_water,
            soil_to_fertilizer,
            seed_to_soil,
        ]

        cur = id
        for map in maps:
            cur = map_id_rev(cur, map)

        return cur

    # print("stats")
    # print("hum to loc")
    # print(humidity_to_location)
    # print("min hum")
    # print(sorted(humidity_to_location, key=lambda mapentry: mapentry["dest"]))
    # print("min seed")
    # print(sorted(seed_pairs, key=lambda seedpair: seedpair[0]))

    # # for map in humidity_to_location:
    # i = 2232050638
    # while True:
    #     res = traverse_maps_rev(i)

    #     for seed_pair in seed_pairs:
    #         if res >= seed_pair[0] and res < seed_pair[0] + seed_pair[1]:
    #             print(f"FOUND {i}")
    #             return

    #     print(i)
    #     i += 1

    # print(traverse_maps_rev(46))

    t_seed_pair = seed_pairs[0]
    t_map_range = seed_to_soil[1]

    t_seed_pairs = [(40, 100)]
    t_map_ranges = [t_map_range]

    print("t_seed_pair")
    print(t_seed_pair)
    print("t_map_range")
    print(t_map_range)







    print("PROCESSING seed_to_soil")
    next_step_pairs = calc_next_steps(seed_to_soil, seed_pairs)
    print("seed_to_soil RESULT")
    print(f"{next_step_pairs=}")
    print("="*60)

    print("PROCESSING soil_to_fertilizer")
    next_step_pairs = calc_next_steps(soil_to_fertilizer, next_step_pairs)
    print("soil_to_fertilizer RESULT")
    print(f"{next_step_pairs=}")
    print("="*60)

    print("PROCESSING fertilizer_to_water")
    next_step_pairs = calc_next_steps(fertilizer_to_water, next_step_pairs)
    print("fertilizer_to_water RESULT")
    print(f"{next_step_pairs=}")
    print("="*60)

    print("PROCESSING water_to_light")
    next_step_pairs = calc_next_steps(water_to_light, next_step_pairs)
    print("water_to_light RESULT")
    print(f"{next_step_pairs=}")
    print("="*60)

    print("PROCESSING light_to_temperature")
    next_step_pairs = calc_next_steps(light_to_temperature, next_step_pairs)
    print("light_to_temperature RESULT")
    print(f"{next_step_pairs=}")
    print("="*60)

    print("PROCESSING temperature_to_humidity")
    next_step_pairs = calc_next_steps(temperature_to_humidity, next_step_pairs)
    print("temperature_to_humidity RESULT")
    print(f"{next_step_pairs=}")
    print("="*60)

    print("PROCESSING humidity_to_location")
    next_step_pairs = calc_next_steps(humidity_to_location, next_step_pairs)
    print("humidity_to_location RESULT")
    print(f"{next_step_pairs=}")
    print("="*60)

    print(sorted(pair[0]for pair in next_step_pairs)[0])
    print(sorted(pair[0]for pair in next_step_pairs)[1])
    print(sorted(pair[0]for pair in next_step_pairs)[2])

def calc_next_steps(seed_to_soil, seed_pairs):
    next_step_pairs = []
    for seed_pair in seed_pairs:
        for map_range in seed_to_soil:
            next_step_pairs.extend(calc_output_for_seed_pair_map_range(seed_pair, map_range))
    
    
    return uniques(next_step_pairs)

    

    # t = calc_output_for_seed_pair_map_range(t_seed_pair, t_map_range)


    # print(t)


def calc_output_for_seed_pair_map_range(seed_pair, map_range):
    print("="*10)
    seed_pair_min = seed_pair[0]
    seed_pair_max = seed_pair[0] + seed_pair[1]

    print(f"{seed_pair_min=}")
    print(f"{seed_pair_max=}")

    map_range_min = map_range["src"]
    map_range_max = map_range["src"] + map_range["nr"]
    print(f"{map_range_min=}")
    print(f"{map_range_max=}")

    if seed_pair_max < map_range_min:
        print("Valt er links buiten")
        print(f"A Mapping {seed_pair} |{seed_pair_min}, {seed_pair_max}| to {[seed_pair]} based on mapper {map_range} |{map_range_min}, {map_range_max}|")
        return [seed_pair]
    if seed_pair_min > map_range_max:
        print("Valt er rechts buiten")
        print(f"B Mapping {seed_pair} |{seed_pair_min}, {seed_pair_max}| to {[seed_pair]} based on mapper {map_range} |{map_range_min}, {map_range_max}|")
        return [seed_pair]

    MAP_RANGE_DIFF = map_range["dest"] - map_range["src"]
    print(f"{MAP_RANGE_DIFF=}")
    res_list = []

    # res_lower = max(seed_pair_min, map_range_min)
    # res_upper = min(seed_pair_max, map_range_max)

    # if res_lower - seed_pair_min:
    #     print("a")
    #     res_list.append((seed_pair_min, res_lower - seed_pair_min))

    # if res_upper + map_range_diff:
    #     print("b")
    #     res_list.append((res_lower + map_range_diff, res_upper + map_range_diff))

    # if seed_pair_max - res_upper:
    #     print("c")
    #     res_list.append((res_upper, seed_pair_max - res_upper))

    if seed_pair_min < map_range_min and seed_pair_max <= map_range_max:
        # 1. 
        print("1 Deels links overlap")
        res_list.append((seed_pair_min, map_range_min - seed_pair_min))
        res_list.append((map_range_min + MAP_RANGE_DIFF, seed_pair_max - map_range_min)) # must map
        print(f"C Mapping {seed_pair} |{seed_pair_min}, {seed_pair_max}| to {res_list} based on mapper {map_range} |{map_range_min}, {map_range_max}|")
        return res_list
    

    if seed_pair_min < map_range_min and seed_pair_max > map_range_max:
        # 2. 
        print("2 Valt er helemaal overheen")
        res_list.append((seed_pair_min, map_range_min - seed_pair_min))
        res_list.append((map_range_min + MAP_RANGE_DIFF, map_range_max - map_range_min)) # must map
        res_list.append((map_range_max, seed_pair_max - map_range_max))
        print(f"C Mapping {seed_pair} |{seed_pair_min}, {seed_pair_max}| to {res_list} based on mapper {map_range} |{map_range_min}, {map_range_max}|")
        return res_list


    if seed_pair_min >= map_range_min and seed_pair_max <= map_range_max:
        # 3.  
        print("3 Valt er helemaal in")
        res_list.append((seed_pair_min + MAP_RANGE_DIFF, seed_pair_max - seed_pair_min)) # must map
        print(f"C Mapping {seed_pair} |{seed_pair_min}, {seed_pair_max}| to {res_list} based on mapper {map_range} |{map_range_min}, {map_range_max}|")
        return res_list
    

    if seed_pair_min > map_range_min and seed_pair_max <= map_range_max:
        # 4. 
        print("4 Deels rechts overlap")
        res_list.append((seed_pair_min + MAP_RANGE_DIFF, map_range_max - seed_pair_max)) # must map
        res_list.append((map_range_max, seed_pair_max - map_range_max))
        print(f"C Mapping {seed_pair} |{seed_pair_min}, {seed_pair_max}| to {res_list} based on mapper {map_range} |{map_range_min}, {map_range_max}|")
        return res_list
    


    # if seed_pair_max > map_range_max:
    #     res_list.append((seed_pair_max, seed_pair_max - map_range_max))

    print(f"C Mapping {seed_pair} |{seed_pair_min}, {seed_pair_max}| to {res_list} based on mapper {map_range} |{map_range_min}, {map_range_max}|")

    return res_list

    if seed_pair_max < map_range_min:
        return None
    if seed_pair_min > map_range_max:
        return None

def uniques(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


if __name__ == "__main__":
    main()
    # map_id(0, )
