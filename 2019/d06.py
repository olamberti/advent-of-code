orbits = {}
for line in open('d06.txt').read().splitlines():
  p1, p2 = line.split(')')
  orbits[p2] = p1

# P1
tot = 0
for pos in orbits:
  while pos != 'COM':
    pos = orbits[pos]
    tot += 1
print(tot)

# P2
y, pos = set(), 'YOU'
while pos != 'COM':
  pos = orbits[pos]
  y.add(pos)

s, pos = set(), 'SAN'
while pos != 'COM':
  pos = orbits[pos]
  s.add(pos)
  
print(len((y - s) | (s - y)))