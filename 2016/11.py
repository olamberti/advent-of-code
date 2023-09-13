import re
from itertools import combinations
from copy import deepcopy as dp
from collections import deque as dq

# Init
floors, num, mats = [], 0, set()
for line in open('11.txt').read().splitlines():
    floor = []
    items = re.findall(r' (\w+|\w+-compatible) (microchip|generator)', line)
    for m, t in items:
        mat = m[0].upper() + m[1]
        floor.append(mat + t[0].upper())
        num += 1
        mats.add(mat)
    floors.append(floor)

def create_status(elevator, floors):
    return (elevator, tuple(tuple(sorted(f)) for f in floors))

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
        ne = e + d
        if ne < 0 or 3 < ne: continue
        items = floors[e]
        for n in [1, 2]:
            for take in combinations(items, n):
                if fried(take): continue
                nfloors = dp(floors)
                for item in take:
                    nfloors[e].remove(item)
                    nfloors[ne].append(item)
                if fried(nfloors[e]) or fried(nfloors[ne]): continue
                res.append(create_status(ne, nfloors))
    return res

def status_combo(status):
    res, e, floors = set(), status[0], list([list(f) for f in status[1]])
    for m1, m2 in combinations(mats, 2):
        nfloors = [[f.replace(m1, 'XX') for f in l] for l in floors]
        nfloors = [[f.replace(m2, m1) for f in l] for l in nfloors]
        nfloors = [[f.replace('XX', m2) for f in l] for l in nfloors]
        res.add(create_status(e, nfloors))
    return res

def min_steps(start):
    stack, cache = dq([[0, start]]), set()
    cache.add(start)
    for sts in status_combo(start):
        cache.add(sts)
    while True:
        steps, status = stack.popleft()
        steps += 1
        for nstatus in next_statuses(status):
            if nstatus in cache: continue
            cache.add(nstatus)
            for nsts in status_combo(nstatus):
                cache.add(nsts)
            if len(nstatus[1][-1]) == num:
                return steps
            stack.append([steps, nstatus])

# P1
print(min_steps(create_status(0, floors)))

# P2 - TODO too slow, needs opting
floors[0] += ['ElG', 'ElM', 'DiG', 'DiM']
mats.add('El'), mats.add('Di')
print(min_steps(create_status(0, floors)))