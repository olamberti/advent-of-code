import re
from collections import deque as dq
from copy import deepcopy as dc

bricks = []
for line in open('d22.txt'):
    xs, ys, zs, xe, ye, ze = [int(x) for x in re.findall(r'(\d+)', line)]
    bricks.append(((xs, ys, zs), (xe, ye, ze)))

def is_under(upper, lower):
    if (upper[0][0] > lower[1][0] or upper[1][0] < lower[0][0]) or (upper[0][1] > lower[1][1] or upper[1][1] < lower[0][1]): return None
    return upper[0][2] - lower[1][2]

def drop(bricks):
    bricks.sort(key = lambda v: v[0][2])
    supports, fallen = {}, 0
    for i, brick in enumerate(bricks):
        min_dist, supports[i] = brick[0][2], []
        if brick[0][2] == 1: 
            supports[i].append(-1)
            continue
        for j, lower in enumerate(bricks[:i]):
            dist = is_under(brick, lower)
            if dist is None: continue
            if dist < min_dist:
                min_dist = dist
                supports[i] = [j]
            elif dist == min_dist:
                supports[i].append(j)
        if min_dist > 1: fallen += 1
        bricks[i] = ((brick[0][0], brick[0][1], brick[0][2] - min_dist + 1), (brick[1][0], brick[1][1], brick[1][2] - min_dist + 1))
    return bricks, supports, fallen

new_bricks, supports, f = drop(dc(bricks))
disintegrate = set(supports.keys())
for lowers in supports.values():
    if len(lowers) == 1:
        unique = lowers[0]
        if unique in disintegrate: disintegrate.remove(unique)
print(len(disintegrate))

total = 0
for brick in supports.keys():
    supp = dc(supports)
    chain = dq([brick])
    fall = 0
    while chain:
         id = chain.popleft()
         fall += 1
         for elem, lowers in supp.items():
             if id in lowers: lowers.remove(id)
             else: continue
             if len(lowers) == 0: chain.append(elem)
    total += fall - 1
print(total)