"""day17.py
"""
OFFSET = 344


class Spinlock:
    def __init__(self, final):
        self.data = [0]
        self.i = 0
        self.n = 1
        self.final = final

    def run(self):
        while self.n <= self.final:
            self.next()

    def next(self):
        index = (self.i + OFFSET) % len(self.data)
        index += 1
        self.data.insert(index, self.n)
        self.i = index
        self.n += 1


spin = Spinlock(2017)
spin.run()
index = spin.data.index(2017)
print(f'Part 1: {spin.data[index+1]}')


running_sum = 0
last_num = None
for i in range(1, 50_000_001):
    running_sum += OFFSET
    running_sum = running_sum % i
    if running_sum == 0:
        last_num = i
    running_sum += 1

print(f'Part 2: {last_num}')

