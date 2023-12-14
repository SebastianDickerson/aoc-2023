import sys
from functools import reduce

def get_next_val(line):
    if all(n == 0 for n in line):
        return 0
    else:
        diff = [line[i+1] - line[i] for i in range(len(line) - 1)]
        return line[-1] + get_next_val(diff)
    
def get_prev_val(line):
    if all(n == 0 for n in line):
        return 0
    else:
        diff = [line[i+1] - line[i] for i in range(len(line) - 1)]
        print(diff)
        return line[0] - get_prev_val(diff)

if __name__ == "__main__":
    lines = [line.rstrip().split() for line in sys.stdin.readlines()]
    res_one = 0
    res_two = 0
    for line in lines:
        line = list(map(int, line))
        res_one += get_next_val(line)
        res_two += get_prev_val(line)
    print(f"part one: {res_one}")
    print(f"part two: {res_two}")