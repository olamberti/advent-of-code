# Init
import math
pos, vel  = [], [], 
for line in open('d12.txt', 'r').read().splitlines():
  pos.append([int(x.strip('>').split('=')[1]) for x in line.split(', ')])
  vel.append([0, 0, 0])

# State function:
def state(pos, vel):
  x, y, z = [], [], []
  for i in range(len(pos)):
    x.extend([pos[i][0], vel[i][0]])
    y.extend([pos[i][1], vel[i][1]])
    z.extend([pos[i][2], vel[i][2]])
  return tuple(x), tuple(y), tuple(z)

states, found = [], []
for axis in state(pos, vel):
  states.append({axis})
  found.append(False)
  
# Simulate motion:
time, periods = 0, []

while not all(found):
  time += 1
  # Apply gravity
  for m1, p1 in enumerate(pos):
    for m2, p2 in enumerate(pos):
      if m1 == m2: continue
      for i in range(3):
        if p1[i] == p2[i]: continue
        elif p1[i] < p2[i]: vel[m1][i] += 1
        else: vel[m1][i] += -1
  # Apply velocity
  for m, v in enumerate(vel):
    for i in range(3):
      pos[m][i] += v[i]
  # Add new states and check it:
  for i, axis in enumerate(state(pos, vel)):
    if found[i] == True: continue
    if axis not in states[i]: states[i].add(axis)
    else:
      found[i] = True
      periods.append(time)
      
  if time == 1000:
    pot, kin = [sum([abs(x) for x in p]) for p in pos], [sum([abs(x) for x in v]) for v in vel]
    tot = [pot[i] * kin[i] for i in range(len(kin))]
    print(sum(tot))

# Find LCM of periods:
print(math.lcm(*periods))
  