"""day22.py
"""
import pathlib
import time

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')

INFECTED = '#'
CLEAN = '.'
WEAK = 'W'
FLAGGED = 'F'
FMAP = {
    (0, -1): '^',
    (0, 1): 'v',
    (1, 0): '>',
    (-1, 0): '<',
}


class Virus:
    def __init__(self, m, center):
        self.coord = center
        self.facing = (0, -1)
        self.dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
        self.m = m
        self.infected_burst_count = 0

    def next(self):
        val = self.m.get(self.coord, CLEAN)
        if val == INFECTED:
            self.turn('r')
        else:
            self.turn('l')
        self.m[self.coord] = INFECTED if val == CLEAN else CLEAN
        if self.m[self.coord] == INFECTED:
            self.infected_burst_count += 1
        self.coord = tuple(a+b for a, b in zip(self.coord, self.facing))

    def do_next(self, n):
        for i in range(n):
            self.next()

    def turn(self, d):
        index = self.dirs.index(self.facing)
        if d == 'r':
            index = (index + 1) % len(self.dirs)
            self.facing = self.dirs[index]
        elif d == 'l':
            self.facing = self.dirs[index-1]
        elif d == 'b':
            self.facing = self.dirs[index-2]

    def draw(self):
        coords = [x for x in self.m.keys()]
        xvals = [x[0] for x in coords]
        yvals = [x[1] for x in coords]
        minx = min(xvals)
        maxx = max(xvals)
        miny = min(yvals)
        maxy = max(yvals)
        out = []
        for y in range(miny, maxy+1):
            line = []
            for x in range(minx, maxx+1):
                if (x, y) == self.coord:
                    ch = FMAP[self.facing]
                else:
                    ch = self.m.get((x, y), CLEAN)
                line.append(ch)
            out.append(''.join(line))
        return '\n'.join(out)


class Virus2(Virus):

    def next(self):
        val = self.m.get(self.coord, CLEAN)
        if val == INFECTED:
            self.turn('r')
            self.m[self.coord] = FLAGGED
        elif val == CLEAN:
            self.turn('l')
            self.m[self.coord] = WEAK
        elif val == FLAGGED:
            self.turn('b')
            self.m[self.coord] = CLEAN
        elif val == WEAK:
            self.m[self.coord] = INFECTED
        if self.m[self.coord] == INFECTED:
            self.infected_burst_count += 1
        nx = self.coord[0] + self.facing[0]
        ny = self.coord[1] + self.facing[1]
        self.coord = (nx, ny)

with open(dpath, 'r') as f:
    data = f.read().splitlines()
    m = {}
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            m[(x, y)] = ch

start = time.perf_counter()
COUNT = 10000
v = Virus(dict(m), (len(line)//2, len(data)//2))
v.do_next(COUNT)
print(f'Part 1: {v.infected_burst_count}')

COUNT = 10000000
v = Virus2(dict(m), (len(line)//2, len(data)//2))
v.do_next(COUNT)
print(f'Part 2: {v.infected_burst_count}')
end = time.perf_counter()

print(f'Time: {(end-start):2f}')

