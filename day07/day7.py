"""day7.py
"""
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()
dpath = pathlib.PurePath(cwd, 'data')
test = '''
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
'''.strip().splitlines()

def get_structure(data):
    tree = {}
    for line in data:
        line = line.split('->')
        name, weight = line[0].split()
        weight = weight.strip(')').strip('(')
        val = [int(weight), []]
        if len(line) > 1:
            val[1] = [x.strip() for x in line[1].split(',')]
        tree[name] = val
    return tree

def get_root(data):
    keys =  set(data.keys())
    for val in data.values():
        keys -= set(val[1])
    return list(keys)[0]

def get_total_weight(tree):
    return sum(x[0] for x in tree.values())

def get_weight(tree, node):
    if len(tree[node]) == 3:
        pass
    else:
        children = tree[node][1]
        tree[node].append(sum(get_weight(tree, child) for child in children) + tree[node][0])
    return tree[node][2]

def is_balanced(tree, node):
    children = tree[node][1]
    if not children:
        return True
    else:
        weights = [get_weight(tree, child) for child in children]
        if set(weights) == 1:
            return True
        else:
            return False


with open(dpath, 'r') as f:
    data = f.read().splitlines()

tree = get_structure(data)
root = get_root(tree)
print(f'Part 1: {root}')

get_weight(tree, root)

q = [(root, None)]
while q:
    node, parent = q.pop(0)
    children = tree[node][1]
    weights = [tree[x][2] for x in children]
    if len(set(weights)) == 1:
        nweights = [tree[x][2] for x in tree[parent][1]]
        print(nweights)
    for child in children:
        if weights.count(tree[child][2]) == 1:
            q.append((child, node))

out = tree['mdbtyw']
print(out)

