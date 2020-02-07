"""day19.py
"""
import pathlib
from string import ascii_lowercase

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
LETTERS = set([l for l in ascii_lowercase.upper()])
ALLOWED = set(['-', '+', '|']) | LETTERS


class Route:
    def __init__(self, fname):
        self.m = {}
        self.start = None
        self.process(fname)

    def process(self, fname):
        with open(fname, 'r') as f:
            data = f.read().splitlines()
        for y, line in enumerate(data):
            for x, ch in enumerate(line):
                self.m[(x, y)] = ch
                if y == 0 and ch == '|':
                    self.start = (x, y)

    def follow_path(self):
        count = 1
        found = []
        coord = self.start
        facing = (0, 1)
        coord = tuple(a+b for a, b in zip(coord, facing))
        while self.m.get(coord, ' ') in ALLOWED:
            ch = self.m[coord]
            if ch in LETTERS:
                found.append(ch)
            elif ch in '+':
                facing = self.find_next(coord, facing)
            coord = tuple(a+b for a, b in zip(coord, facing))
            count += 1
        return found, count

    def find_next(self, coord, facing):
        for d in DIRS:
            ncoord = tuple(a+b for a, b in zip(d, coord))
            if self.m.get(ncoord, ' ') in ALLOWED and (-d[0], -d[1]) != facing:
                return d

r = Route(dpath)
found, count = r.follow_path()
print(''.join(found))
print(count)

