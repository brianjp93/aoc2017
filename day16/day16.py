"""day16.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

with open(dpath, 'r') as f:
    data = f.read().split(',')


class Dance:
    def __init__(self, instr, program=None):
        self.instr = instr
        self.p = program if program is not None else [l for l in 'abcdefghijklmnop']
        self.i = 0
        self.run = {
            's': self.spin,
            'x': self.exchange,
            'p': self.partner
        }

    def dance(self):
        instr = self.instr[self.i]
        self.run[instr[0]]()
        self.i += 1

    def dance_until_finished(self):
        while self.i < len(self.instr):
            self.dance()
        self.i = 0

    def spin(self):
        instr = self.instr[self.i]
        spinsize = int(instr[1:])
        self.p = self.p[-spinsize:] + self.p[:-spinsize]

    def exchange(self):
        instr = self.instr[self.i]
        exch = list(map(int, instr[1:].split('/')))
        self.p[exch[0]], self.p[exch[1]] = self.p[exch[1]], self.p[exch[0]]

    def partner(self):
        instr = self.instr[self.i]
        p1, p2 = instr[1:].split('/')
        p1_index = self.p.index(p1)
        p2_index = self.p.index(p2)
        self.p[p1_index], self.p[p2_index] = self.p[p2_index], self.p[p1_index]


d = Dance(data)
d.dance_until_finished()
out = ''.join(d.p)
print(f'Part 1: {out}')


seen = {}
d = Dance(data)
i = 0
while True:
    d.dance_until_finished()
    i += 1
    out = ''.join(d.p)
    if out in seen:
        loopstart = seen[out]
        loopend = i
        break
    seen[out] = i

looplength = loopend - loopstart
dance_count = 1000000000
modded_dance_count = dance_count % looplength
seen_index = {val: key for key, val in seen.items()}
print(f'Part 2: {seen_index[modded_dance_count]}')

