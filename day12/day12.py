"""day12.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


pipes = {}
with open(dpath, 'r') as f:
    data = f.read().splitlines()
    for line in data:
        line = line.split('<->')
        n1 = int(line[0])
        pipes[n1] = [int(x) for x in line[1].split(',')]


def get_connections(n):
    seen = set([n])
    q = [n]
    while q:
        n = q.pop(0)
        seen.add(n)
        for child in pipes[n]:
            if child not in seen:
                q.append(child)
    return seen

zero_connections = get_connections(0)
print(f'Part 1: {len(zero_connections)}')


group_count = 0
all_keys = set(pipes.keys())
while all_keys:
    group_count += 1
    group = get_connections(all_keys.pop())
    all_keys -= group
print(f'Part 2: {group_count}')

