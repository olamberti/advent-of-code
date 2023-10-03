import re

inp, nodes = open('d22.txt').read().splitlines(), {}
for line in inp[2:]:
    p = [int(x) for x in re.findall(r'\d+', line)[:4]]
    nodes[(p[0], p[1])] = [p[2], p[3]]
    if p[3] == 0: empty = (p[0], p[1])
xM, yM = p[0], p[1]

# P1
p1, blocks = 0, set()
for key, vals in nodes.items():
    if key == empty: continue
    elif vals[1] > nodes[empty][0]: blocks.add(key)
    else: p1 += 1
print(p1)

# P2
pos, front, seen, steps = empty, set(), set(), 0
front.add(pos); seen.add(pos)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while (xM - 1, 0) not in seen:
    nfront = set(); steps += 1
    for x, y in front:
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not(0 <= nx <= xM and 0 <= ny <= yM): continue
            np = (nx, ny)
            if np in blocks or np in seen: continue
            nfront.add(np); seen.add(np)
    front = nfront
print(steps + 1 + 5 * (xM - 1))