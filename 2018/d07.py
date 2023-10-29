from copy import deepcopy as dp

reqs = {}
for line in open('d07.txt').read().splitlines():
    line = line.split()
    r, s = line[1], line[-3]
    if s not in reqs: reqs[s] = [r]
    else:
        reqs[s].append(r)
    if r not in reqs: reqs[r] = []

work = {}
for step, rs in reqs.items():
    work[step] = [dp(rs), ord(step) - ord('A') + 61]

# P1
p1 = ''
while reqs:
    pn = []
    for step, rs in reqs.items():
        if rs == []: pn.append(step)
    pn.sort()
    ns = pn[0]
    p1 = p1 + ns
    del reqs[ns]
    for s in reqs:
        if ns in reqs[s]: reqs[s].remove(ns)
print(p1)

# P2
t = 0
while work:
    workitems = []
    for step, task in work.items():
        if task[0] == []: workitems.append(step)
    workitems.sort()
    workitems = workitems[:5]
    for item in workitems:
        work[item][1] -= 1
        if work[item][1] == 0:
            del work[item]
            for s in work:
                if item in work[s][0]: work[s][0].remove(item)
    t += 1
print(t)