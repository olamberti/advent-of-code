import re
from statistics import stdev

W, H, ps, vs = 101, 103, [], []
for line in open('d14.txt').readlines():
    x, y, dx, dy = map(int, re.findall(r'(-?\d+)', line))
    ps.append((x, y))
    vs.append((dx, dy))

def safety_factor(ps):
    q1 = len([(x, y) for x, y in ps if x < W // 2 and y < H // 2])
    q2 = len([(x, y) for x, y in ps if x > W // 2 and y < H // 2])
    q3 = len([(x, y) for x, y in ps if x < W // 2 and y > H // 2])
    q4 = len([(x, y) for x, y in ps if x > W // 2 and y > H // 2])
    return q1 * q2 * q3 * q4

def crt(a1, n1, a2, n2):
  if a1 < a2: a1, a2, n1, n2 = a2, a1, n2, n1
  q = [[a1, 1, 0], [a2, 0, 1]]
  while q[-1][0] != 0:
    d = q[-2][0] // q[-1][0]
    r = q[-2][0] - d * q[-1][0]
    a = q[-2][1] - d * q[-1][1]
    b = q[-2][2] - d * q[-1][2]
    q.append([r, a, b])
  m1, m2 = q[-2][1], q[-2][2]
  return (n2 * m1 * a1 + n1 * m2 * a2) % (a1 * a2)

minx, miny = float('inf'), float('inf')
for t in range(1, max(W, H) + 1):
    for i, (x, y) in enumerate(ps):
        ps[i] = ((x + vs[i][0]) % W, (y + vs[i][1]) % H)
    stdx, stdy = stdev([x for x, _ in ps]), stdev([y for _, y in ps])
    if stdx < minx:
        minx, rx = stdx, t
    if stdy < miny:
        miny, ry = stdy, t
    if t == 100:
        print(safety_factor(ps))
        
print(crt(W, rx, H, ry))