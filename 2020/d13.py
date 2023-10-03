# Parse
lines = open('d13.txt').read().split()
t = int(lines[0])
bs = [int(x) for x in lines[1].split(',') if x.isnumeric()]

# P1
w = 0
while True:
  for b in bs:
    if (t + w) % b == 0: 
      print(b * w)
      break
  else:
    w += 1
    continue
  break

# P2
t, g = 0, []
for i, x in enumerate(lines[1].split(',')):
  if x.isnumeric(): 
    x = int(x)
    g.append([x, (x - i) % x])

def excon(a1, n1, a2, n2):
  if a1 < a2: a1, a2, n1, n2 = a2, a1, n2, n1
  q = [[a1, 1, 0], [a2, 0, 1]]
  while q[-1][0] != 0:
    d = q[-2][0] // q[-1][0]
    r = q[-2][0] - d * q[-1][0]
    a = q[-2][1] - d * q[-1][1]
    b = q[-2][2] - d * q[-1][2]
    q.append([r, a, b])
  m1, m2 = q[-2][1], q[-2][2]
  x = (n2 * m1 * a1 + n1 * m2 * a2) % (a1 * a2)
  return [a1*a2, x]
  
# P2
c = g[0]
for i in range(1, len(g)):
  c = excon(*c, *g[i])
print(c[1])