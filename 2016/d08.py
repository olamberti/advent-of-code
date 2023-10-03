import numpy as np
import re

# P1
w, h = 50, 6
screen = np.zeros((h, w))
for line in open('d08.txt').read().splitlines():
    p = [int(x) for x in re.findall(r'\d+', line)]
    if line.split()[0] == 'rect': screen[:p[1], :p[0]] = 1
    else:
        if line.split()[1] == 'column': screen[:, p[0]] = np.roll(screen[:, p[0]], p[1])
        else: screen[p[0], :] = np.roll(screen[p[0], :], p[1])
print(int(np.sum(screen)))

# P2
line = ''
for r in range(h):
    for c in range(w):
        if screen[r, c] == 1: line += '█'
        else: line += ' '
    line += '\n'
print(line)