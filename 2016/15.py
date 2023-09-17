import re

discs = []
for line in open('15.txt').read().splitlines():
    p = [int(x) for x in re.findall(r'(\d+)', line)]
    discs.append((p[1], -(p[0] + p[3]) % p[1]))

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

def chrt(rems):
   r = rems[0]
   for i in range(1, len(discs)): r = excon(*r, *rems[i])
   return r

# P1
print(chrt(discs)[1])

# P2
discs.append((11, -(len(discs) + 1) % 11))
print(chrt(discs)[1])