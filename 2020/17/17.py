# Input parsing:
inp = open('17.txt').read().splitlines()
act3, act4 = set(), set()

for x, l in enumerate(inp):
  for y, c in enumerate(l):
    if c == '#':
      act3.add((x, y, 0))
      act4.add((x, y, 0, 0))

# NeighbourS:
def ns(p):
  res, dim = [], len(p)
  x, y, z = p[0], p[1], p[2]
  if dim == 4: w = p[3]
  for i in range(x - 1, x + 2):
    for j in range(y -1, y + 2):
      for k in range(z - 1, z + 2):
        if dim  == 3:
          if (i, j, k) == (x, y, z): continue
          res.append((i, j, k))
        else:
          for l in range(w - 1, w + 2):
            if (i, j, k, l) == (x, y, z, w): continue
            res.append((i, j, k, l))       
  return res

# BOUNDdary:
def bound(s):
  res, vis = set(), set()
  for e in s:
    for n in ns(e):
      if n in vis: continue
      elif n in s: vis.add(n)
      else:
        res.add(n)
        vis.add(n)
  return res

# Active NeighbourS:
def anc(c, a):
  an = 0
  for n in ns(c):
    if n in a: an += 1
  return an

# SIMUlate:
def simu(act, ina):
  act_, ina_ = set(), set()
  for c in act:
    if 2 <= anc(c, act) <= 3: act_.add(c)
  for c in ina:
    if anc(c, act) == 3: act_.add(c)
  ina_ = bound(act_)
  return act_, ina_

# Simulation:
ina3 = bound(act3)
ina4 = bound(act4)
  
for _ in range(6):
  act3, ina3 = simu(act3, ina3)
  act4, ina4 = simu(act4, ina4)
  
print(len(act3))
print(len(act4))