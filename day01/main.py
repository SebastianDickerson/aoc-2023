import sys
import re

if __name__ == "__main__":

    words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five" : "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    lines = [line.rstrip() for line in sys.stdin.readlines()]
    
    def calibration(data, replace=False):
        calibration_value = 0
        for line in data:
            if replace:
                for i, c in words.items():
                    line = line.replace(i, f"{i[0]}{c}{i[-1]}")
            j = ''.join(re.findall(r"\d+", line))
            calibration_value += int(j[0] + j[-1])
        return calibration_value

    print(f"Part one: {calibration(lines)}")
    print(f"Part Two: {calibration(lines, replace=True)}")
