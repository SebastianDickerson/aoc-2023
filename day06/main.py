import sys
from functools import reduce
import time

def part_one(t, d):   
    ways_to_win = []
    races = zip(t, d)
    for t, d in races:
        ans = 0
        t,d = int(t), int(d)
        for i in range(0, int(t)):
            time_left = t - i
            distance_travelled = time_left * i
            if distance_travelled > d:
                ans += 1
        ways_to_win.append(ans)
    print(reduce(lambda x, y: x*y, ways_to_win))

def part_two(t, d):
    t = int("".join(t))
    d = int("".join(d))
    f = 0
    l = 0

    for i in range(0, t):
        time_left = t - i
        distance_travelled = time_left * i
        if distance_travelled > d:
            f = i
            break

    for i in range(t, 0, -1):
        time_left = t - i
        distance_travelled = time_left * i

        if distance_travelled > d:
            l = i
            break
    
    print(l-f+1)

if __name__ == "__main__":
    st = time.time()
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    t = list(filter(None, lines[0].split(": ")[1].split(' ')))
    d = list(filter(None, lines[1].split(": ")[1].split(' ')))

    part_one(t, d)
    part_two(t, d)

