import functools
import sys
import string

def get_num(r,c,lines):
    number = ""
    while lines[r][c].isdigit():
        if lines[r][c].isdigit():
            c -= 1
    
    for i in lines[r][c+1:]:
        if not i.isdigit():
            break
        elif i.isdigit():
            number += i
    return (r, c+1, int(number))

if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    symbols = string.punctuation.replace('.', '')
    nums = []
    s = 0

    debug = set()

    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch in '*':
                # print(f"symbol: {ch}")
                bounds = [
                    (r-1,c-1),(r-1,c),(r-1,c+1),
                    (r,c-1),           (r,c+1),
                    (r+1,c-1),(r+1,c),(r+1,c+1)
                    ]
                nums = set()
                for i in bounds:
                    try:
                        if lines[i[0]][i[1]].isdigit():
                            n = get_num(i[0],i[1],lines)
                            nums.add(n)
                    except IndexError:
                        pass
                if len(nums) > 1:
                    s += functools.reduce(lambda a,b: a*b[2], nums, 1)
                
    print(sum(i[2] for i in set(nums)))
    print(s)