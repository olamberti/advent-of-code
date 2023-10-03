import re

channels = {}
for line in open('d12.txt').read().splitlines():
    data = [int(x) for x in re.findall(r'\d+', line)]
    channels[data[0]] = data[1:]

def explore(p, group):
    group.add(p)
    for e in channels[p]:
        if e in group: continue
        group = explore(e, group)
    return group

p2, seen = 0, set()
for k in channels.keys():
    if k not in seen:
        p2 += 1
        seen = explore(k, seen)
        if k == 0: print(len(seen))
print(p2)