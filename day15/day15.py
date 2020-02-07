"""day15.py
"""
ASTART = 722
BSTART = 354
AMULT = 16807
BMULT = 48271
BIGMOD = 2147483647


class Generator:
    def __init__(self, mult_factor, start):
        self.mult_factor = mult_factor
        self.start = start
        self.n = start

    def next(self):
        self.n = (self.n * self.mult_factor) % BIGMOD

    def next_div(self, div):
        self.next()
        while self.n % div != 0:
            self.next()

def is_16_match(n1, n2):
    n1 = f'{n1:b}'[-16:]
    n2 = f'{n2:b}'[-16:]
    return n1 == n2


count = 0
gena = Generator(AMULT, ASTART)
genb = Generator(BMULT, BSTART)
LOOPS = 40_000_000
for i in range(LOOPS):
    gena.next()
    genb.next()
    if is_16_match(gena.n, genb.n):
        count += 1
print(f'Part 1: {count}')


count = 0
gena = Generator(AMULT, ASTART)
genb = Generator(BMULT, BSTART)
LOOPS = 5_000_000
for i in range(LOOPS):
    gena.next_div(4)
    genb.next_div(8)
    if is_16_match(gena.n, genb.n):
        count += 1
print(f'Part 2: {count}')

