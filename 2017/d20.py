import re

ps, maL, p1 = {}, 999, None
for i, line in enumerate(open('d20.txt').read().splitlines()):
    vals = [int(x) for x in re.findall(r'(-?\d+)', line)]
    p, v, a = vals[0:3], vals[3:6], vals[6:9]
    ps[i], aL = [p, v, a], sum([abs(x) for x in a])

def update():
    for ind, val in ps.items():
        [p, v, a] = val
        for i in range(3):
            v[i] += a[i]
            p[i] += v[i]
        ps[ind] = [p, v, a]

for _ in range(1000):
    update()

# TODO: not finished yet