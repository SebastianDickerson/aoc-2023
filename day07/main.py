import sys
from collections import Counter

def rank(hand):
    part_two = True

    hand = hand.replace("T", chr(ord("9")+1))
    hand = hand.replace("J", chr(ord("9")+2)) if not part_two else hand.replace("J", "1")
    hand = hand.replace("Q", chr(ord("9")+3))
    hand = hand.replace("K", chr(ord("9")+4))
    hand = hand.replace("A", chr(ord("9")+5))

    C = Counter(hand)

    if part_two:
        for c, _ in sorted(C.items(), key=lambda x:x[1], reverse=True):
            if c != '1':
                C[c] += C['1']
                del C['1']
                break

    if list(C.values()) == [5]:
        return (10, hand)
    elif sorted(C.values()) == [1,4]:
        return (9, hand)    
    elif sorted(C.values()) == [2,3]:
        return (8, hand)
    elif sorted(C.values()) == [1,1,3]:
        return (7, hand)
    elif sorted(C.values()) == [1,2,2]:
        return (6, hand)
    elif sorted(C.values()) == [1,1,1,2]:
        return (5, hand)
    elif sorted(C.values()) == [1,1,1,1,1]:
        return (4, hand)
    else:
        assert f"{hand}, {C.values()}"

if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    hands = [line.split(" ")[0] for line in lines]
    bids = [line.split(" ")[1] for line in lines]
    hs = []

    for i, hand in enumerate(hands):
        hs.append((hand, bids[i]))
    hs = sorted(hs, key=lambda h:rank(h[0]))
    ans = 0
    for i, (h,b) in enumerate(hs):
        ans += (i+1)*int(b)
    print(ans)