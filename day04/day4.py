"""day4.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')

with open(dpath, 'r') as f:
    data = f.read().splitlines()

def is_valid(phrase):
    words = phrase.split()
    return len(words) == len(set(words))

def is_valid2(phrase):
    words = phrase.split()
    words = [''.join(sorted(word)) for word in words]
    return len(words) == len(set(words))

count = sum(is_valid(x) for x in data)
print(f'Part 1: {count}')

count = sum(is_valid2(x) for x in data)
print(f'Part 2: {count}')

