"""day14.py
"""
key = 'ljoxqyyw'


DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_hash(name):
    data = [ord(x) for x in name] + [17, 31, 73, 47, 23]
    elts = list(range(256))
    index = 0
    skip_size = 0
    for _ in range(64):
        for n in data:
            val = elts[index]
            end = index + n
            if end > len(elts):
                end = end % len(elts)
                part = elts[index:] + elts[:end]
                part.reverse()
                elts = part[-end:] + elts[end:index] + part[:-end]
            else:
                part = elts[index:end]
                part.reverse()
                elts = elts[:index] + part + elts[end:]
            index += (n + skip_size)
            index = index % len(elts)
            skip_size += 1
            skip_size = skip_size % len(elts)
    parts = [elts[i:i+16] for i in range(0, 256, 16)]
    pieces = []
    for part in parts:
        out = part[0]
        for n in part[1:]:
            out ^= n
        pieces.append(out)
    out = [f'{x:x}' for x in pieces]
    out = [x if len(x) == 2 else '0' + x for x in out]
    out = ''.join(out)
    out = ''.join(f'{int(x, 16):04b}' for x in out)
    return out

def create_map(name):
    out = []
    m = {
        '0': '.',
        '1': '#'
    }
    for i in range(128):
        out.append(''.join(m[x] for x in get_hash(f'{name}-{i}')))
    return '\n'.join(out)

def find_groups(m):
    m = m.splitlines()
    groups = []
    all_found = set()
    for y in range(len(m)):
        for x, c in enumerate(m[y]):
            coord = (x, y)
            if c == '#' and coord not in all_found:
                filled = fill_from(coord, m)
                all_found |= filled
                groups.append(filled)
    return groups

def fill_from(coord, m):
    filled = set()
    q = [coord]
    while q:
        coord = q.pop()
        filled.add(coord)
        for d in DIRS:
            ncoord = tuple(a+b for a, b in zip(d, coord))
            x, y = ncoord
            if x >= 0 and x < len(m[0]) and y >= 0 and y < len(m):
                if ncoord not in filled and m[y][x] == '#':
                    q.append(ncoord)
    return filled



test = 'flqrgnkx'
m = create_map(key)
out = m.count('#')
print(out)

groups = find_groups(m)
print(len(groups))

