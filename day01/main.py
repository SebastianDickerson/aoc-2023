import sys

def part_one(data):

    val = 0
    
    for line in data:
        v = []
        for c in line:
            if c.isdigit():
                v.append(c) 
        n = ''.join(v)
        num = n[0] + n[-1]
        val += int(num)
    print(val)

def part_two(data, replace=True):

    val = 0
    
    for line in data:
        v = []
        if replace:
            for i, c in words.items():
                line = line.replace(i, f"{i[0]}{c}{i[-1]}")
        for c in line:
            if c.isdigit():
                v.append(c) 
        n = ''.join(v)
        num = n[0] + n[-1]
        val += int(num)
    print(val)

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

    print("Lets go Buddy!")
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    part_one(lines)
    part_two(lines)

    

        
        
        