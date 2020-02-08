"""day20.py
"""
import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
PROGRAM = re.compile('p=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, v=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, a=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>')


class Particle:
    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def __repr__(self):
        return f'Particle(pos={self.pos}, vel={self.vel}, acc={self.acc})'

    def get_man_acc(self):
        return sum(abs(x) for x in self.acc)


with open(dpath, 'r') as f:
    data = f.read().splitlines()

particles = []
for line in data:
    r = PROGRAM.match(line)
    g = [int(x) for x in r.groups()]
    p = Particle(g[:3], g[3:6], g[6:9])

for p in particles:
    pass
