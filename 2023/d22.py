import re
from collections import deque as dq

# Load input
bricks = []
for line in open('d22.txt'):
    bricks.append([int(x) for x in re.findall(r'(\d+)', line)])

# Function that checks overlap in x & y dimensions and gives the z distance if there is any
def is_under(upper, lower): 
    if (max(upper[0], lower[0]) > min(upper[3], lower[3]) or max(upper[1], lower[1]) > min(upper[4], lower[4])):
        return None
    return upper[2] - lower[5]

# Let bricks fall and store which bricks they fell on
bricks.sort(key = lambda v: v[2])
supports = {}
for i, brick in enumerate(bricks):
    min_dist, supports[i] = brick[2], set()
    if brick[2] == 1: continue
    for j, lower in enumerate(bricks[:i]):
        dist = is_under(brick, lower)
        if dist is None: continue
        if dist < min_dist:
            min_dist = dist
            supports[i] = {j}
        elif dist == min_dist:
            supports[i].add(j)
    brick[2] += 1 - min_dist
    brick[5] += 1 - min_dist

# Part 1
disintegrate = set(supports.keys())
for lowers in supports.values():
    if len(lowers) == 1:
        disintegrate -= lowers
print(len(disintegrate))

# Part 2
total = 0
for i, brick in enumerate(bricks):
    chain = dq(j for j, supps in supports.items() if i in supps and len(supps) == 1)
    fallen = set(chain)
    fallen.add(i)
    while chain:
        drop = chain.popleft()
        for sus, supps in supports.items():
            if sus in fallen or len(supps) == 0: continue
            if supps.issubset(fallen):
                chain.append(sus)
                fallen.add(sus)
    total += len(fallen) - 1
print(total)