"""day18.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

test = '''
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
'''.strip().splitlines()


with open(dpath, 'r') as f:
    data = f.read().splitlines()

LETTERS = {l for l in 'abcdefghijklmnopqrstuvwxyz'}

class Duet:
    def __init__(self, data, qin=None, qout=None, registers=None):
        self.registers = {} if registers is None else registers
        self.sounds = {}
        self.last_sound = None
        self.i = 0
        self.data = list(data)
        self.send_count = 0
        self.qin = [] if qin is None else qin
        self.qout = [] if qout is None else qout


    def run_until_finished(self):
        while self.i < len(self.data):
            out = self.run()
            if out == 'HALT':
                break

    def run(self):
        line = self.data[self.i]
        line = line.split()
        cmd = line[0]
        if cmd == 'set':
            reg, n = line[1:]
            if n in LETTERS:
                n = self.registers.get(n, 0)
            n = int(n)
            self.registers[reg] = n
        elif cmd == 'snd':
            reg = line[1]
            freq = self.registers[reg]
            self.sounds[reg] = freq
            self.last_sound = freq
            self.send_count += 1
            self.qout.append(freq)
        elif cmd == 'add':
            reg, n = line[1:]
            if n in LETTERS:
                n = self.registers.get(n, 0)
            n = int(n)
            self.registers[reg] = self.registers.get(reg, 0) + n
        elif cmd == 'mul':
            reg, n = line[1:]
            if n in LETTERS:
                n = self.registers.get(n, 0)
            n = int(n)
            self.registers[reg] = self.registers.get(reg, 0) * n
        elif cmd == 'mod':
            reg, n = line[1:]
            if n in LETTERS:
                n = self.registers.get(n, 0)
            n = int(n)
            self.registers[reg] = self.registers.get(reg, 0) % n
        elif cmd == 'rcv':
            reg = line[1]
            if self.qin:
                self.registers[reg] = self.qin.pop(0)
            else:
                return 'HALT'
        elif cmd == 'jgz':
            reg, n = line[1:]
            if reg in LETTERS:
                val = self.registers[reg]
            else:
                val = int(reg)
            if val > 0:
                if n in LETTERS:
                    n = self.registers.get(n, 0)
                n = int(n)
                self.i += n
                return
        self.i += 1


d = Duet(data)
d.run_until_finished()


d1 = Duet(data, registers={'p': 0})
d2 = Duet(data, registers={'p': 1})

while True:
    d1.run_until_finished()
    d2.run_until_finished()
    if not d1.qout and not d2.qout:
        break
    
    d2.qin += d1.qout
    d1.qin += d2.qout
    d1.qout = []
    d2.qout = []

print(d2.send_count)
