import sys

if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    total_points = []
    cards = [1 for _ in lines]

    for id,line in enumerate(lines):
        ans = 0
        winning_nums, my_picks = line.split(": ")[1].split(" | ")
        winning_nums, my_picks = winning_nums.split(" "), my_picks.split(" ")
        good_picks = []
    
        for i in range(len(winning_nums)):
            if winning_nums[i] in my_picks:
                good_picks.append(winning_nums[i])

        good_picks = list(filter(None, good_picks))

        for i in range(len(good_picks)):
            cards[id + i + 1] += cards[id]
            
        ans += 2**(len(good_picks)-1) if len(good_picks) > 0 else 0
        total_points.append(ans)
    print(sum(total_points), sum(cards))
