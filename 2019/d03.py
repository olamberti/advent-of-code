wires = [wire.split(',') for wire in open('d03.txt').read().splitlines()]
dirs = {'L':-1, 'R':1, 'U':1j, 'D':-1j}

def md(p):
  return int(abs(p.real) + abs(p.imag))

# P1:
wps = [{}, {}]
for i in range(2):
  w, l = 0, 0
  for part in wires[i]:
    d, s = part[0], int(part[1:])
    for _ in range(s):
      w += dirs[d]
      l += 1
      if w not in wps[i]: wps[i][w] = l

p1, p2 = 99999999, 99999999
for p in wps[0].keys() & wps[1].keys():
  p1 = min(p1, md(p))
  p2 = min(p2, wps[0][p] + wps[1][p])
print(p1)
print(p2)