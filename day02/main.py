import sys
from collections import defaultdict

if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin.readlines()]

    possible_games = 0
    max_score = 0

    for line in lines:
        ok = True
        cubes = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        V = defaultdict(int)

        game = line.split(":")[0]
        cubes_current = cubes.copy()
        for s in line.split(":")[1].split(";"):
            for c in s.strip().split(", "):
                num, color = c.split(" ")
                V[color] = max(V[color], int(num))
                if int(num) > cubes_current[color]:
                    ok = False
        score = 1
        for v in V.values():
            score *= v
        max_score += score
        if ok:
            possible_games += int(game.split(" ")[1])

    print(possible_games)
    print(max_score)
    