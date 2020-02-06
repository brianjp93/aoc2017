"""day13.py
"""
import pathlib
import copy

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
test = '''
0: 3
1: 2
4: 4
6: 4
'''.strip().splitlines()


def get_firewall():
    firewall = {}
    with open(dpath, 'r') as f:
        data = f.read().splitlines()
        for line in data:
            line = line.split(':')
            val = [int(line[1]), (int(line[1]) - 1)*2, 0]
            val.append((-int(line[0])) % val[1])
            firewall[int(line[0])] = val
    return firewall

def step_scanners(firewall):
    for val in firewall.values():
        val[2] = (val[2] + 1) % val[1]
    return firewall

def get_severity(n, firewall):
    return firewall[n][0] * n

firewall = get_firewall()
MAXDIG = max(firewall.keys())

def calculate_severity(firewall):
    total_severity = 0
    for key, val in firewall.items():
        if val[2] == val[3]:
            total_severity += get_severity(key, firewall)
    return total_severity

def has_severity(firewall):
    for val in firewall.values():
        if val[2] == val[3]:
            return True
    return False


total_severity = calculate_severity(firewall)
print(f'Part 1: {total_severity}')
firewall = get_firewall()

severity = True
i = 0
while severity:
    step_scanners(firewall)
    step_scanners(firewall)
    severity = has_severity(firewall)
    i += 2

print(f'Part 2: {i}')

