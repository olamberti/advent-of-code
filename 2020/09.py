# Inputs
q = [int(x) for x in open('09.txt').read().splitlines()]
l = 25

# P1
i, ok = 0, True
while ok:
  ok = False
  p, x = q[i : i + l], q[i + l]
  for i1 in range(l - 1):
    for i2 in range(i1 + 1, l):
      p1, p2 = p[i1], p[i2]
      if p1 + p2 == x:
        ok = True  
        break
    if ok: break
  i += 1
inv = x
print(inv)

# P2
cut = q.index(inv) + 1
q, i, done = q[:cut], 0, False
while not done:
  q_, t = q[i:], []
  for x in q_:
    t.append(x)
    if sum(t) == inv:
      done = True
      break
    elif sum(t) > inv:
      break
  i += 1
print(min(t) + max(t))