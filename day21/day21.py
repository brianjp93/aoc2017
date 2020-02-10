"""day21.py
"""
import pathlib
import numpy as np

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')

STARTMAP = '''
.#.
..#
###
'''.strip()


class Fractal:
    def __init__(self, table):
        self.table = table
        self.m = STARTMAP

    def next(self):
        pieces = self.get_pieces()

    def find_match(self, piece):
        for i in range(4):
            piece = self.mutate(piece, 'rotate')
            if piece in self.table:
                return self.table[piece]
        piece = self.mutate(piece, 'flip')
        for i in range(4):
            piece = self.mutate(piece, 'rotate')
            if piece in self.table:
                return self.table[piece]

    def get_pieces(self):
        m = self.m.splitlines()
        out = []
        if len(m) % 2 == 0:
            for y in range(0, len(m), 2):
                lines = []
                for x in range(0, len(m), 2):
                    lines.append(m[y][x:x+2])
                    lines.append(m[y+1][x:x+2])
        elif len(m) % 3 == 0:
            for y in range(0, len(m), 3):
                lines = []
                for x in range(0, len(m), 3):
                    lines.append(m[y][x:x+3])
                    lines.append(m[y+1][x:x+3])
                    lines.append(m[y+2][x:x+3])
        out.append('\n'.join(lines))
        return out

    def mutate(self, m, mutation):
        out = []
        for line in m.splitlines():
            out.append([x for x in line])
        out = np.array(out)
        if mutation == 'flip':
            out = np.flipud(out)
        elif mutation == 'rotate':
            out = np.rot90(out)
        return '\n'.join(''.join(line) for line in out)

with open(tpath, 'r') as f:
    data = f.read().splitlines()
    table = {}
    for line in data:
        line = line.split('=>')
        p1 = line[0].strip()
        p2 = line[1].strip()
        p1 = '\n'.join(p1.split('/'))
        p2 = '\n'.join(p2.split('/'))
        table[p1] = p2

f = Fractal(table)

