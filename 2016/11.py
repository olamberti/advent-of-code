import re
from itertools import combinations
from copy import deepcopy as dp
from collections import deque as dq

# Init
floors, mats = [], set()
for line in open('11.txt').read().splitlines():
    floor = []
    items = re.findall(r' (\w+|\w+-compatible) (microchip|generator)', line)
    for m, t in items:
        mat = m[0].upper() + m[1]
        floor.append(mat + t[0].upper())
        mats.add(mat)
    floors.append(floor)

def create_status(elevator, floors):
    return (elevator, tuple(tuple(f) for f in floors))

def fried(items):
    if len(items) == 0 or len(items) == 1: return False
    for item in items:
        if item[-1] == 'G': continue
        if item[-1] == 'M' and (item[:-1] + 'G') in items: continue
        for other_item in items:
            if other_item[-1] == 'G': return True
    return False

def next_statuses(status):
    res, e, floors = [], status[0], list([list(f) for f in status[1]])
    for d in [-1, 1]:
        ne, resd = e + d, []
        if ne < 0 or 3 < ne: continue
        if len(floors[0]) == 0 and ne == 0: continue
        if (len(floors[0]) == 0 and len(floors[1]) == 0) and ne == 1: continue
        items = floors[e]
        nums = [1, 2] if d == -1 else [2, 1]
        for n in nums:
            for take in combinations(items, n):
                if fried(take): continue
                nfloors = dp(floors)
                for item in take:
                    nfloors[e].remove(item)
                    nfloors[ne].append(item)
                if fried(nfloors[e]) or fried(nfloors[ne]): continue
                if d == -1 and n == 2 and resd: continue
                if d == 1 and n == 1 and resd: continue
                resd.append(create_status(ne, nfloors))
        res += resd
    return res

def cache_hash(status):
    res, pairs, e, floors = set(), {}, status[0], list([list(f) for f in status[1]])
    for mat in mats: pairs[mat] = [None, None]
    for i, floor in enumerate(floors):
        for item in floor:
            mat, t = item[:-1], item[-1]
            if t == 'M': pairs[mat][0] =  i
            else: pairs[mat][1] =  i
    res = (e, tuple([tuple(p) for p in sorted(pairs.values())]))
    return res

def min_steps(start):
    stack, cache = dq([[0, start]]), set()
    cache.add(cache_hash(start))
    while True:
        steps, status = stack.popleft()
        steps += 1
        for nstatus in next_statuses(status):
            if cache_hash(nstatus) in cache: continue
            cache.add(cache_hash(nstatus))
            if len(nstatus[1][-1]) == 2 * len(mats):
                return steps
            stack.append([steps, nstatus])

# P1
print(min_steps(create_status(0, floors)))

# P2
floors[0] += ['ElG', 'ElM', 'DiG', 'DiM']
mats.add('El'), mats.add('Di')
print(min_steps(create_status(0, floors)))