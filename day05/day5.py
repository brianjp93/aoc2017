"""day5.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


with open(dpath, 'r') as f:
    data = f.read().splitlines()
    data = list(map(int, data))

p1 = list(data)
counter = 0
i = 0
while i >= 0 and i < len(p1):
    inext = i + p1[i]
    p1[i] += 1
    i = inext
    counter += 1
print(f'Part 1: {counter}')

p2 = list(data)
counter = 0
i = 0
while i >= 0 and i < len(p2):
    offset = p2[i]
    inext = i + offset
    if offset >= 3:
        p2[i] -= 1
    else:
        p2[i] += 1
    i = inext
    counter += 1

print(f'Part 2: {counter}')

