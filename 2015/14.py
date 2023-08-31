import re

# Read input
data = {}
for line in open('14.txt').readlines():
    data[line.split(' ')[0]] = [int(x) for x in re.findall(r'\d+', line)]

def dist(par, t):
    v, tv, tr = par
    return (v * tv) * (t // (tv + tr)) + v * min(t % (tv + tr), tv)

# P1
t = 2503
dists = [dist(p, t) for p in data.values()]
print(max(dists))

# P2
points = [0 for _ in range(len(data))]
for ti in range(1,t + 1):
    dists = [dist(p, ti) for p in data.values()]
    dM = max(dists)
    for i, d in enumerate(dists):
        if d == dM: points[i] += 1
print(max(points))