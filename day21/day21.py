"""day21.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

STARTMAP = '''
.#.
..#
###
'''.strip()


class Fractal:
    def __init__(self, table):
        self.table = table
        self.m = STARTMAP


with open(dpath, 'r') as f:
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
print(f.m)

