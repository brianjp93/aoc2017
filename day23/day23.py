"""day23.py
"""
import pathlib
from string import ascii_lowercase

cwd = pathlib.Path(__file__).parent.absolute()
dpath= pathlib.PurePath(cwd, 'data')

LETTERS = {l for l in ascii_lowercase}


class Duet:
    def __init__(self, data, qin=None, qout=None, registers=None, i=0):
        self.registers = {} if registers is None else registers
        self.sounds = {}
        self.last_sound = None
        self.i = i
        self.data = list(data)
        self.send_count = 0
        self.qin = [] if qin is None else qin
        self.qout = [] if qout is None else qout
        self.mul_count = 0


    def run_until_finished(self):
        while self.i < len(self.data):
            print(self.i)
            print(self.registers)
            print(self.registers.get('h', 0))
            print(self.data[self.i])
            input()
            old_h = self.registers.get('h', 0)
            out = self.run()
            # if self.registers.get('h', 0) != old_h:
            #     print(self.registers.get('h', 0))
            #     input()
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
        elif cmd == 'sub':
            reg, n = line[1:]
            if n in LETTERS:
                n = self.registers.get(n, 0)
            n = int(n)
            self.registers[reg] = self.registers.get(reg, 0) - n
        elif cmd == 'mul':
            self.mul_count += 1
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
        elif cmd == 'jnz':
            reg, n = line[1:]
            if reg in LETTERS:
                val = self.registers.get(reg, 0)
            else:
                val = int(reg)
            if val != 0:
                if n in LETTERS:
                    n = self.registers.get(n, 0)
                n = int(n)
                self.i += n
                return
        self.i += 1

with open(dpath, 'r') as f:
    data = f.read().splitlines()

# d = Duet(list(data))
# d.run_until_finished()
# print(d.mul_count)

d = Duet(list(data), registers={'a': 1, 'b': 109900, 'c': 126900, 'f': 0, 'd': 2, 'e': 109899, 'g': 62}, i=17)
d.run_until_finished()


