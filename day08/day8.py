"""day8.py
"""
import pathlib
import re

MAXVAL = 0
cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
register = {}
program = re.compile('([a-z]+) (inc|dec) (-?[0-9]+) if ([a-z]+) ([<>=!]+) (-?[0-9]+)')
test = '''
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''.strip().splitlines()

def handle_command(line):
    global MAXVAL
    r = program.match(line)
    g = r.groups()
    var1 = g[0]
    var2 = g[3]
    updown = g[1]
    offset = int(g[2])
    condition = g[4]
    var3 = int(g[5])
    conditions = {
        '>': register.get(var2, 0) > var3,
        '<': register.get(var2, 0) < var3,
        '>=': register.get(var2, 0) >= var3,
        '<=': register.get(var2, 0) <= var3,
        '==': register.get(var2, 0) == var3,
        '!=': register.get(var2, 0) != var3,
    }
    if conditions[condition]:
        if updown == 'inc':
            register[var1] = register.get(var1, 0) + offset
        elif updown == 'dec':
            register[var1] = register.get(var1, 0) - offset
        if register[var1] > MAXVAL:
            MAXVAL = register[var1]


with open(dpath, 'r') as f:
    data = f.read().splitlines()

for line in data:
    handle_command(line)
largest = max(x for x in register.values())
print(f'Part 1: {largest}')

print(f'Part 2: {MAXVAL}')

