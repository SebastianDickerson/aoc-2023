import sys
import itertools
from math import lcm
from functools import reduce

def part_one(start="AAA", end="ZZZ"):
    steps = 0
    pos = start
    for i in itertools.cycle(ins):
        if pos == end:
            return True, steps
        pos = N[pos][G[i]]
        steps += 1

def part_two():
    cycles = set()
    for p in a_labels:
        pos = p
        for c, i in enumerate(itertools.cycle(ins)):
            if pos.endswith('Z'):
                cycles.add((c, pos))
                break
            pos = N[pos][G[i]]
            
    return reduce(lcm, [c for c, _ in cycles])

if __name__ == "__main__":
    ins, *nodes = [line.rstrip() for line in sys.stdin.readlines()]  
    G = dict()
    N = dict()
    G["L"] = 0
    G["R"] = 1
    a_labels = []

    for node in nodes[1:]:
        label, cords = node.split(' = ')
        N[label] = [cord.replace('(','').replace(')','') for cord in cords.split(", ")]
        if label.endswith('A'):
            a_labels.append(label)

    found = False
    while not found:
        found, ss = part_one(start="AAA", end="ZZZ")
        print(f"part one: {ss}")
        ss2 = part_two()
        print(f"part two: {ss2}")
    