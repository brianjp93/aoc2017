"""day20.py
"""
import pathlib
import re

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
tpath = pathlib.PurePath(cwd, 'test')
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

    def next(self):
        self.vel = [a+b for a, b in zip(self.vel, self.acc)]
        self.pos = [a+b for a, b in zip(self.pos, self.vel)]


def remove_collisions(particles):
    positions = {}
    for p in particles:
        key = tuple(p.pos)
        positions[key] = positions.get(key, []) + [p]
    nparticles = []
    for plist in positions.values():
        if len(plist) == 1:
            nparticles.append(plist[0])
    return nparticles


with open(dpath, 'r') as f:
    data = f.read().splitlines()

particles = []
for line in data:
    r = PROGRAM.match(line)
    g = [int(x) for x in r.groups()]
    p = Particle(g[:3], g[3:6], g[6:9])
    particles.append(p)


top_acc_man = min(p.get_man_acc() for p in particles)
print(top_acc_man)
top_particles = [(i, p) for i, p in enumerate(particles) if p.get_man_acc() == top_acc_man]
print(top_particles)


i = 0
while True:
    if i % 10_000 == 0:
        print(f'Loop: {i}')
        print(len(particles))
    positions = {}
    for p in particles:
        p.next()
        key = tuple(p.pos)
        positions[key] = positions.get(key, []) + [p]
    particles = []
    for plist in positions.values():
        if len(plist) == 1:
            particles.append(plist[0])
    i += 1

