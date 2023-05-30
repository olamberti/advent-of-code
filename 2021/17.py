# Read input
import math
data = open('17.txt', 'r').read().split()
x = [int(n) for n in data[2].strip('x=,').split('..')]
y = [int(n) for n in data[3].strip('y=,').split('..')]
mx, Mx, my, My = min(x), max(x), min(y), max(y)

# PART 1:
Mvy = abs(my) - 1           # maximum allowed vy velocity
h = (Mvy * (Mvy + 1)) // 2  # maximum reached height
print(h)

# PART 2:
mvy = my                                                # minimum vy to reach target area
mvx = int(0.5 * (math.sqrt(8 * mx + 1)  - 1)) + 1       # minimum vx to reach target area
Mvx = Mx                                                # maximum vx to reach target area
good = set()

for sx in range(mvx, Mvx + 1):
  for sy in range(mvy, Mvy + 1):
    pos = 0 + 0 * 1j
    vx, vy = sx, sy
    while pos.real <= Mx and pos.imag >= my:             # not over the target area
      pos += vx + vy * 1j                                # next position
      if mx <= pos.real <= Mx and my <= pos.imag <= My:  # in target area
        good.add((sx, sy))
        break
      if vx > 0: vx += -1
      vy += -1     
print(len(good))