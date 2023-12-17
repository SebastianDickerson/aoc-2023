import sys
from collections import deque

if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin.readlines()]

    for rr, row in enumerate(lines):
        for cc, ch in enumerate(row):
            if ch == 'S':
                rs = rr
                cs = cc
                break
    
    q = deque([(rs, cs)])
    seen = {(rs, cs)}

    while q:
        r, c = q.popleft()
        ch = lines[r][c]

        # check above ch
        if r > 0 and ch in "S|JL" and lines[r - 1][c] in "|7F" and (r - 1, c) not in seen:
            seen.add((r - 1, c))
            q.append((r - 1, c))
            
        # check below ch
        if r < len(lines) - 1 and ch in "S|7F" and lines[r + 1][c] in "|JL" and (r + 1, c) not in seen:
            seen.add((r + 1, c))
            q.append((r + 1, c))

        # check right of ch
        if c > 0 and ch in "S-J7" and lines[r][c - 1] in "-LF" and (r, c - 1) not in seen:
            seen.add((r, c - 1))
            q.append((r, c - 1))

        # check left of ch
        if c < len(lines[r]) - 1 and ch in "S-LF" and lines[r][c + 1] in "-J7" and (r, c + 1) not in seen:
            seen.add((r, c + 1))
            q.append((r, c + 1))

    print(len(seen) // 2)