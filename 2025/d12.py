import re

*shapes, trees = open('d12.txt').read().split('\n\n')

sh = dict()
for shape in shapes:
    id = int(shape[0])
    size = shape.count('#')
    sh[id] = size

p1 = 0
for tree in trees.split('\n'):
    ns = [int(x) for x in re.findall(r'(\d+)', tree)]
    area, ps = ns[0] * ns[1], ns[2:]
    need_min = sum([p * sh[i] for i, p in enumerate(ps)])
    blocks = ns[0] // 3 * ns[1] // 3
    if area < need_min: continue
    if blocks >= sum(ps): p1 += 1

print(p1)