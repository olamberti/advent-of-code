# Read input:
east, south = set(), set()
grid = open('25.txt', 'r').read().splitlines()
for r, row in enumerate(grid):
  for c, char in enumerate(row):
    if char == '>': east.add((r + c * 1j))
    elif char == 'v': south.add((r + c * 1j))
h, w = r + 1, c + 1
  
# Simulate movement:
step = 1
stuck = False

while not stuck:
  step += 1
  stuck = True
  
  east_ = set()
  for e in east:
    n = e.real + (e.imag + 1) % w * 1j
    if n in east or n in south:
      east_.add(e)
    else:
      east_.add(n)
  if east_ != east:
    east = east_
    stuck = False

  south_ = set()
  for s in south:
    n = (s.real + 1) % h + s.imag * 1j
    if n in east or n in south:
      south_.add(s)
    else:
      south_.add(n)
  if south_ != south:
    south = south_
    stuck = False

print(step - 1)