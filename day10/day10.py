"""day10.py
"""
data = '212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164'
data = list(map(int, data.split(',')))
elts = list(range(256))

index = 0
skip_size = 0

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

print(f'Part 1: {elts[0] * elts[1]}')


data = '212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164'
data = [ord(x) for x in data] + [17, 31, 73, 47, 23]
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
out = [x if len(x) == 2 else '0'+x for x in out]
out = ''.join(out)
print(f'Part 2: {out}')

