"""day11.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

DIRS = {
    'n': (0, 2),
    'ne': (1, 1),
    'se': (1, -1),
    's': (0, -2),
    'sw': (-1, -1),
    'nw': (-1, 1)
}

def shortest_dist(target):
    x, y = target
    if abs(y) < abs(x):
        pathlength = abs(x)
    else:
        diff = abs(y) - abs(x)
        pathlength = diff + abs(x)
    return pathlength

with open(dpath, 'r') as f:
    data = f.read().strip().split(',')

coord = (0, 0)
MAXDIST = 0
for d in data:
    coord = tuple(a+b for a, b in zip(coord, DIRS[d]))
    dist = shortest_dist(coord)
    if dist > MAXDIST:
        MAXDIST = dist

target = tuple(coord)
dist = shortest_dist(target)
print(f'Part 1: {dist}')
print(f'Part 2: {MAXDIST}')

