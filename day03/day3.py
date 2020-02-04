"""day3.py
"""
SUMS = {(0, 0): 1}
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ALLDIRS = DIRS + [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def find_coord(n):
    cur_n = 1
    while (2*cur_n + 1)**2 - (6*cur_n) < n:
        cur_n += 1
    cur_n -= 1
    second = (2*cur_n + 1)**2 - (4*cur_n)
    if n <= second:
        out = abs(cur_n - (second - n))
        return (cur_n, out)
    third = (2*cur_n + 1)**2 - (2*cur_n)
    if n <= third:
        out = abs(cur_n - (third - n))
        return (cur_n, out)
    fourth = (2*cur_n + 1)**2
    if n <= fourth:
        out = abs(cur_n - (fourth - n))
        return (cur_n, out)

def get_adj(coord):
    out = []
    for d in ALLDIRS:
        ncoord = tuple(a+b for a, b in zip(coord, d))
        out.append(SUMS.get(ncoord, 0))
    return out

FINDNUM = 289326
out = find_coord(FINDNUM)
print(out)
print(f'Part 1: {sum(out)}')


coord = (0, 0)
length = 1

i = 0
found = False
while True:
    for j in range(2):
        for _ in range(length):
            d = DIRS[i % len(DIRS)]
            coord = tuple(a+b for a, b in zip(coord, d))
            SUMS[coord] = sum(get_adj(coord))
            if SUMS[coord] > FINDNUM:
                found = True
                val = SUMS[coord]
                break
        if found:
            break
        i += 1
    length += 1
    if found:
        break

print(f'Part 2: {val}')

