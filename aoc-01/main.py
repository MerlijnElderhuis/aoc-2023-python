from enum import Enum


def read_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        lines = f.read().splitlines()

    return lines


def parse_digits_from_line1(line: str) -> list[str]:
    res = []
    for char in line:
        if char.isdigit():
            res.append(char)

    return res


digits_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


class Digit:
    def __init__(self, letters: str):
        self.letters = letters
        self.progress = ""

    def step(self, chr: str) -> bool:
        if chr == self.letters[len(self.progress)]:
            print(f"({self.letters}) {chr} - {self.progress}")
            self.progress += chr
            if self.done():
                self.reset()
                return True
            return False
        else:
            if self.progress:
                self.reset()
                self.step(chr)
            else:
                self.reset()
            return False

    def done(self):
        return self.progress == self.letters

    def reset(self):
        # print("resetting progress")
        self.progress = ""


def parse_digits_from_line2(line: str) -> list[str]:
    all_digits: list[str] = list(digits_map.keys())
    digits: list[Digit] = [Digit(d) for d in all_digits]

    final_res: list[str] = []

    for chr in line:
        if chr.isdigit():
            # print("Appending number")
            final_res.append(chr)

        for digit in digits:
            res = digit.step(chr)
            if res:
                print("Appending parsed number")
                final_res.append(digits_map[digit.letters])

    return final_res


# letter_between_res


def calc_calib_from_line(line: str) -> int:
    line_digits = parse_digits_from_line2(line)
    print(line)
    print(line_digits)
    first = line_digits[0]
    last = line_digits[-1]
    res_str = f"{first}{last}"

    res_int = int(res_str)
    print(res_int)
    print()
    return res_int


def test_progress():
    input_str = "sadjahsdkasthreeasdasd"
    digit = Digit("three")

    res_list = []

    for chr in input_str:
        digit.step(chr)
        if digit.done():
            print(f"Found {digit.letters}. Appending to list and resetting")
            res_list.append(digits_map[digit.letters])
            digit.reset()

    print(res_list)


def main():
    lines = read_input("input.txt")
    line_calibs = [calc_calib_from_line(line) for line in lines]
    print(sum(line_calibs))


if __name__ == "__main__":
    main()
    # test_progress()
    # res = parse_digits_from_line2("eighttwonine5fourkqtjsjthree")
    # print(res)
