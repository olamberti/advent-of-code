from itertools import product
from collections import deque as dq

p1, p2 = 0, 0
for row in open('d10.txt').read().splitlines():
    dia, *buttons, jolts = row.split()
    dia = [1 if c == '#' else 0 for c in dia[1:-1]]
    buttons = [tuple(map(int,x[1:-1].split(','))) for x in buttons]
    jolts = [int(x) for x in jolts[1:-1].split(',')]
    nm, nb = len(dia), len(buttons)

    # Part 1
    pmin = nb
    for pressed in product((0, 1), repeat=nb):
        lights = [0] * nm
        for i, p in enumerate(pressed):
            if p == 0: continue
            for id in buttons[i]: lights[id] = 1 - lights[id]
        if lights == dia:
            pmin = min(sum(pressed), pmin)
    p1 += pmin

    # Part 2
    # BFS - Too slow for real input yet, only works for example...
    q, cache = dq([[0] * nb]), set()
    while q:
        pressed = q.popleft()
        if tuple(pressed) in cache: continue
        cache.add(tuple(pressed))

        js = [0] * nm
        for i, p in enumerate(pressed):
            if p == 0: continue
            for id in buttons[i]: js[id] += p
        if js == jolts:
            p2 += sum(pressed)
            break
        else:
            for i in range(nb):
                new_pr = pressed[:]
                new_pr[i] += 1
                q.append(new_pr)

print(p1)
print(p2)