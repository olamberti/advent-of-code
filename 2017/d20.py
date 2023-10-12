import re
from copy import deepcopy as dp

ps, maL = {}, 999
for i, line in enumerate(open('d20.txt').read().splitlines()):
    vals = [int(x) for x in re.findall(r'(-?\d+)', line)]
    p, v, a = vals[0:3], vals[3:6], vals[6:9]
    ps[i], aL = [p, v, a], sum([abs(x) for x in a])
    maL = min(aL, maL)

# P1:
def update(p, v, a):
    for i in range(3):
        v[i] += a[i]
        p[i] += v[i]
    return p, v, a

def tick(particles):
    for pid, vec in particles.items():
        particles[pid] = update(*vec)

def md(p):
    return sum([abs(x) for x in p])

slows = {}
for pid, vec in ps.items():
    if sum([abs(x) for x in vec[2]]) == maL: slows[pid] = dp(vec)

for _ in range(100):
    tick(slows)

mind = 99999999999999
for pid, vec in slows.items():
    d = md(vec[0])
    if d < mind:
        mind = d
        p1 = pid
print(p1)

# P2
def collide(particles):
    posis = {}
    for pid, vec in particles.items():
        pos = tuple(vec[0])
        if pos in posis: posis[pos].append(pid)
        else: posis[pos] = [pid]
    for pids in posis.values():
        if len(pids) > 1:
            for pid in pids: del particles[pid]

for _ in range(100):
    tick(ps)
    collide(ps)
print(len(ps))