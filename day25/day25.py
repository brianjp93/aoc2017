"""day25.py
"""
STEPS = 12481997


class Turing:
    def __init__(self):
        self.state = 'a'
        self.i = 0
        self.tape = {}
        self.methods = {
            'a': self.methoda,
            'b': self.methodb,
            'c': self.methodc,
            'd': self.methodd,
            'e': self.methode,
            'f': self.methodf
        }
        self.steps = 0

    def run(self):
        self.methods[self.state]()
        self.steps += 1

    def run_until(self, step):
        while self.steps != step:
            self.run()

    def get(self):
        return self.tape.get(self.i, 0)

    def checksum(self):
        return sum(self.tape.values())

    def methoda(self):
        val = self.get()
        if val == 0:
            self.tape[self.i] = 1
            self.i += 1
            self.state = 'b'
        else:
            self.tape[self.i] = 0
            self.i -= 1
            self.state = 'c'

    def methodb(self):
        val = self.get()
        if val == 0:
            self.tape[self.i] = 1
            self.i -= 1
            self.state = 'a'
        else:
            self.tape[self.i] = 1
            self.i += 1
            self.state = 'd'

    def methodc(self):
        val = self.get()
        if val == 0:
            self.tape[self.i] = 0
            self.i -= 1
            self.state = 'b'
        else:
            self.tape[self.i] = 0
            self.i -= 1
            self.state = 'e'

    def methodd(self):
        val = self.get()
        if val == 0:
            self.tape[self.i] = 1
            self.i += 1
            self.state = 'a'
        else:
            self.tape[self.i] = 0
            self.i += 1
            self.state = 'b'

    def methode(self):
        val = self.get()
        if val == 0:
            self.tape[self.i] = 1
            self.i -= 1
            self.state = 'f'
        else:
            self.tape[self.i] = 1
            self.i -= 1
            self.state = 'c'

    def methodf(self):
        val = self.get()
        if val == 0:
            self.tape[self.i] = 1
            self.i += 1
            self.state = 'd'
        else:
            self.tape[self.i] = 1
            self.i += 1
            self.state = 'a'


t = Turing()
t.run_until(STEPS)
checksum = t.checksum()
print(f'Part 1: {checksum}')

