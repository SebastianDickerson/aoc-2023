import sys

def part_one():
    seeds, *blocks = [line for line in sys.stdin.read().split('\n\n')]
    seeds = list(map(int, seeds.split(':')[1].split()))
    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        for x in seeds:
            for a, b, c in ranges:
                if b <= x < b + c:
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new 
    return min(seeds)

def part_two():
    inp, *blocks = [line for line in sys.stdin.read().split('\n\n')]
    inp = list(map(int, inp.split(':')[1].split()))
    seeds = []

    for i in range(0, len(inp), 2):
        seeds.append((inp[i], inp[i] + inp[i+1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(seeds) > 0:
            s,e = seeds.pop()
            for a, b, c in ranges:
                os = max(s,b)
                oe = min(e,b+c)
                if os < oe:
                    new.append((os-b+a,oe-b+a))
                    if os > s:
                        seeds.append((s,os))
                    if e > oe:
                        seeds.append((oe,e))
                    break
            else:
                new.append((s,e))
        seeds = new
    return min(seeds)[0]

if __name__ == "__main__":
    print(f"Day one: {part_one()}")
    print(f"Day two: {part_one()}")
    