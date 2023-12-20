import os
import sys


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")

    input_file = f"{dir}/{input_file}"
    if len(sys.argv) > 1:
        print("using ARGV")
        input_file = str(sys.argv[1])
    with open(input_file, "r") as f:
        lines = f.read().splitlines()

    return lines


def process_pt2(ss):
    d = {i: [] for i in range(256)}

    for s in ss:
        if "=" in s:
            label, lens_str = s.split("=")

            box_nr = myhashhash(label)

            cur_entries = [
                (i, entry) for i, entry in enumerate(d[box_nr]) if entry[0] == label
            ]
            if not cur_entries:
                d[box_nr].append((label, lens_str))
            else:
                d[box_nr][cur_entries[0][0]] = (label, lens_str)

        if "-" in s:
            label = s.split("-")[0]
            box_nr = myhashhash(label)

            d[box_nr] = [entry for entry in d[box_nr] if entry[0] != label]

    print(d)

    sum = 0

    for box_number, lenses in d.items():
        for i, lens in enumerate(lenses):
            box_val = 1 + box_number
            lens_slot_val = i + 1
            lens_val = int(lens[1])
            print(f"Adding {box_val=}, {lens_slot_val}, {lens_val}: ")
            sum += box_val * lens_slot_val * lens_val

    print(sum)


def main():
    TEST = False
    if TEST:
        file_name = "test_input.txt"
    else:
        file_name = "input.txt"

    lines = read_input_lines(file_name)
    # for line in lines:
    #     print(line)
    print("=" * 80)

    strings = lines[0].split(",")
    # print(strings)

    mysum = 0
    for s in strings:
        mysum += myhashhash(s)
    print(mysum)

    print("=" * 40)

    res = process_pt2(strings)


def myhashhash(s):
    cur = 0

    for chr in s:
        ascii_val = ord(chr)
        cur += ascii_val
        cur *= 17
        cur %= 256
    return cur


if __name__ == "__main__":
    main()
