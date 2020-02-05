"""day9.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


class Stream:
    def __init__(self, data):
        self.data = [x for x in data]
        self.scores = []
        self.garbage_count = 0
        self.process()

    def process(self):
        self.ignore()
        self.remove_garbage()
        self.ignore_commas()
        self.get_score()

    def ignore(self):
        i = 0
        while i < len(self.data):
            if self.data[i] in '!':
                del self.data[i:i+2]
            else:
                i += 1

    def ignore_commas(self):
        i = 0
        while i < len(self.data):
            if self.data[i] in ',':
                del self.data[i]
            else:
                i += 1

    def remove_garbage(self):
        while True:
            start, end = self.find_garbage()
            if start is not None and end is not None:
                del self.data[start: end+1]
                self.garbage_count += (end - start - 1)
            else:
                break

    def find_garbage(self):
        istart = 0
        while istart < len(self.data):
            if self.data[istart] == '<':
                break
            istart += 1
        iend = istart
        while iend < len(self.data):
            if self.data[iend] == '>':
                break
            iend += 1
        if istart == iend:
            istart = iend = None
        return istart, iend

    def find_next_open(self, i):
        while i < len(self.data):
            if self.data[i] == '{':
                return i
            else:
                i += 1
        return i

    def find_match(self, i):
        count = 1
        self.scores.append(1)
        while i < len(self.data):
            c = self.data[i]
            if c == '{':
                count += 1
                self.scores.append(count)
            elif c == '}':
                count -= 1
            if count == 0:
                return i
            i += 1
        return i

    def get_score(self):
        i = 0
        while i < len(self.data):
            i = self.find_next_open(i)
            print(f'Found next open bracket at {i}')
            if i+1 < len(self.data):
                i = self.find_match(i + 1) + 1
                print(f'Found match at {i-1}')
            else:
                break


with open(dpath, 'r') as f:
    data = f.read().strip()
stream = Stream(data)
score_sum = sum(stream.scores)
print(f'Part 1: {score_sum}')
print(f'Part 2: {stream.garbage_count}')

