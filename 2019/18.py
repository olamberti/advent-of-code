from collections import deque
from copy import deepcopy as dp
import heapq

# Read input
walls, paths, keys, doors = set(), set(), {}, {}
dirs = [1, 1j, -1, -1j]

for y, line in enumerate(open('18.txt').readlines()):
    for x, e in enumerate(line.strip()):
        if e == '#': walls.add(x + y*1j)
        elif e == '.': paths.add(x + y*1j)
        elif e == '@':
            paths.add(x + y*1j)
            start = x + y*1j
        elif e.islower(): keys[x + y*1j] = e
        elif e.isupper(): doors[x + y*1j] = e

# Create key-to-key distances with doors in the way with BFS
def get_keys(st):
    front, visited, out = {}, {}, {}
    front[st] = (0, set())
    while front:
        nfront = {}
        for p, [dist, ds] in front.items():
            visited[p] = [dist, ds]    
            for d in dirs:
                np, nds, ndist = p + d, dp(ds), dist + 1
                if np in walls or np in visited.keys(): continue
                elif np in doors.keys(): nds.add(doors[np])
                elif np in keys.keys(): out[keys[np]] = [ndist, nds]
                nfront[np] = (ndist, nds)
        front = nfront
    return out

k2k = {}
k2k['@'] = get_keys(start)
for pos, key in keys.items():
    k2k[key] = get_keys(pos)

# P1
p1 = float('inf')
stack, cache = [(0, '@', frozenset())], set()
heapq.heapify(stack)

while stack:
    dist, pos, mykeys = heapq.heappop(stack)
    if (pos, mykeys) in cache: continue
    if len(mykeys) == len(keys):
        if dist < p1: p1 = dist
        continue
    for npos, [ndist, locks] in k2k[pos].items():
        if npos in mykeys: continue
        if locks and not all([door.lower() in mykeys for door in locks]): continue
        nkeys = set(mykeys)
        nkeys.add(npos)
        nkeys = frozenset(nkeys)
        heapq.heappush(stack, (dist + ndist, npos, nkeys))
    cache.add((pos, mykeys))
print(p1)

# P2
# to be implemented