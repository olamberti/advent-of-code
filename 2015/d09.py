import itertools
from collections import deque as dq

dists = {}
for line in open('d09.txt').readlines():
    line = line.strip().split(' ')
    a, b, d = line[0], line[2], int(line[-1])
    if a not in dists.keys(): dists[a] = {}
    if b not in dists.keys(): dists[b] = {}
    dists[a][b] = d
    dists[b][a] = d

p1, p2 = 1_000_000_000, 0
for route in itertools.permutations(dists.keys()):
    d = 0
    for i in range(len(route) - 1):
        d += dists[route[i]][route[i + 1]]
    if d < p1: p1 = d
    if d > p2: p2 = d
print(p1)
print(p2)