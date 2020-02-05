"""day6.py
"""
data = '5 1 10 0 1 7 13 14 3 12 8 10 7 12 0 6'
data = [int(x) for x in data.split()]
dlen = len(data)

def get_max(data):
    val = -float('inf')
    index = None
    for i, d in enumerate(data):
        if d > val:
            val = d
            index = i
    return val, index

def redistribute(data, index):
    dlen = len(data)
    val = data[index]
    data[index] = 0
    complete = val // dlen
    extra = abs(val) % dlen
    sign = abs(val) // val
    for i in range(dlen):
        data[i] += complete
    for i in range(extra):
        data[(i+index+1) % dlen] += sign

seen = {}

i = 0
while True:
    out = ','.join(str(x) for x in data)
    if out in seen:
        loop_length = i - seen[out]
        break
    else:
        seen[out] = i
    val, index = get_max(data)
    redistribute(data, index)
    i += 1

print(f'Part 1: {i}')
print(f'Part 2: {loop_length}')

