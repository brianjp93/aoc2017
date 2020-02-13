"""day24.py
"""
import pathlib
import copy
import time


cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')


class Moat:
    def __init__(self, components=None, pin_ends=None):
        self.components = components[:] if components else []
        self.pin_ends = copy.deepcopy(pin_ends) if pin_ends else {}

    def find_bridges(self):
        bridge = []
        used = set()
        all_allowed = set(range(len(self.components)))
        done = []
        q = [(0, [], set(all_allowed))]
        while q:
            last_pin, bridge, allowed = q.pop()
            is_found = False
            for comp_index in self.pin_ends.get(last_pin, []):
                if comp_index in allowed:
                    nallowed = set(allowed)
                    nallowed.remove(comp_index)
                    is_found = True
                    nbridge = bridge[:]
                    nbridge.append(comp_index)
                    sides = self.components[comp_index]
                    nlast_pin = sides[1] if last_pin == sides[0] else sides[0]
                    q.append((nlast_pin, nbridge, nallowed))
            if not is_found:
                done.append(bridge[:])
        done_comps = [[self.components[i] for i in done_indeces] for done_indeces in done]
        ends = []
        for l in done_comps:
            piece = []
            for comp in l:
                piece += list(comp)
            ends.append(piece)
        return ends

    def get_longest_bridges(self):
        bridges = self.find_bridges()
        max_length = max(len(x) for x in bridges)
        longest_bridges = [x for x in bridges if len(x) == max_length]
        return longest_bridges


start = time.perf_counter()
components = []
pin_ends = {}
with open(dpath, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        s1, s2 = [int(x) for x in line.strip().split('/')]
        components.append((s1, s2))
        pin_ends[s1] = pin_ends.get(s1, []) + [i]
        if s1 != s2:
            pin_ends[s2] = pin_ends.get(s2, []) + [i]


m = Moat(components, pin_ends)

all_bridges = m.find_bridges()
max_bridge = max([sum(x) for x in all_bridges])
print(f'Part 1: {max_bridge}')

longest_bridges = m.get_longest_bridges()
longest_bridge_strength = max([sum(x) for x in longest_bridges])
print(f'Part 2: {longest_bridge_strength}')

end = time.perf_counter()
print(f'Time: {(end-start):.2f}')

