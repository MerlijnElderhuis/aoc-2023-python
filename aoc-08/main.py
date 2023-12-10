from functools import reduce
import operator
import os
import re
from copy import deepcopy
from math import lcm


def read_input_lines(input_file: str) -> list[str]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = dir_path.split("/")[-1]
    print(f"Starting {dir}")
    with open(f"{dir}/{input_file}", "r") as f:
        lines = f.read().splitlines()

    return lines


instructions = None
instructions_idx = 0


def parse_input(lines):
    instructions, _, *nodes = lines
    # print(instructions)
    # print(nodes)

    nodes_dict = {}
    for nodeline in nodes:
        nodename, node_lr = nodeline.split("=")
        nodename = nodename.strip()
        node_l, node_r = re.findall("\w+", node_lr)
        # print(nodename, node_l, node_r)
        nodes_dict[nodename] = (node_l, node_r)
    return instructions, nodes_dict


def gen_instruction():
    global instructions
    global instructions_idx

    # Debug print
    # print(
    #     f"Yielding instruction {instructions[instructions_idx]}, index {instructions_idx}"
    # )

    # Save the current instruction to return
    current_instruction = instructions[instructions_idx]

    # Increment the index for the next call
    instructions_idx += 1

    # Reset the index if it reaches the end of the instructions list
    if instructions_idx >= len(instructions):
        instructions_idx = 0

    # Return the current instruction
    return current_instruction


def walk(nodes, nodes_dict):
    nodes_in = deepcopy(nodes)
    print(nodes_in)
    step_count = 0
    nodes_encountered_z = {i: {} for i, node in enumerate(nodes)}
    nodes_looped = set()
    nodes_looped_twice = set()
    nodes_encountered_z_lists = {i: {} for i, node in enumerate(nodes)}

    node_periods = {}
    node_first_encounters = {}
    print("lens")
    print(len(nodes_looped))
    print(len(nodes))
    while len(nodes_looped) != len(nodes):
        # while True:
        # or not all(
        # len(value) == len(nodes) for _, value in nodes_encountered_z.items()
        # ):
        if step_count % 100000 == 0:
            print(f"{step_count=}")
            print(f"{nodes_encountered_z=}")
            print(f"{nodes_looped=}")
        instr = gen_instruction()
        new_nodes = []

        for i, node in enumerate(nodes):
            if node == nodes_in[i] and step_count > 0:
                print(f"start node found: {node} == {nodes_in[i]}")
                nodes_looped.add(node)

            if node[-1] == "Z":
                print(f"Encountered Z {node=} in {i} {instr=} at {step_count}")
                if node in nodes_encountered_z[i]:
                    print(
                        f"Looped at {step_count}. Loop size: {step_count - nodes_encountered_z[i][node]}"
                    )

                    nodes_looped.add(node)
                    if not i in node_periods:
                        node_periods[i] = {step_count - nodes_encountered_z[i][node]}
                else:
                    nodes_encountered_z[i][node] = step_count
                    node_first_encounters[i] = step_count
                    print(f"Setting {i}, {node}, {step_count=}")

            if instr == "L":
                new_nodes.append(nodes_dict[node][0])
            if instr == "R":
                new_nodes.append(nodes_dict[node][1])

        nodes = new_nodes
        step_count += 1

    print(f"Finished with step_count {step_count}")
    print(f"Z's: {nodes_encountered_z}")
    print(f"looped: {nodes}")
    print(f"{node_periods=}")
    print(f"{node_first_encounters=}")
    print(product(list(node_first_encounters.values())))
    return step_count


def product(xs):
    return reduce(operator.mul, xs, 1)


def main_two():
    # list = [20093, 12169, 22357, 14999, 13301, 17263]
    list = [12169, 13301, 14999, 17263, 20093, 22357]
    print(lcm(*list))


def main():
    TEST = True
    if TEST:
        file_name = "test_input.txt"
    else:
        file_name = "input.txt"

    lines = read_input_lines(file_name)
    # for line in lines:
    #     print(line)
    # print("=" * 80)

    instrs, nodes_dict = parse_input(lines)
    print(f"{instrs=}")
    global instructions
    instructions = instrs

    # print(nodes_dict)
    nodes_ending_on_a = [node for node in nodes_dict.keys() if node[-1] == "A"]
    print(f"{nodes_ending_on_a=}")

    walk(nodes_ending_on_a, nodes_dict)


if __name__ == "__main__":
    # main()
    main_two()
    # print(20093*12169*22357*14999*13301*17263)
