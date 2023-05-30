# Read input:
y, data, online = 2000000, dict(), set()
for line in open('15.txt','r'):
  words = [word.strip(',:xy=') for word in line.strip().split()]
  x1, y1, x2, y2 = int(words[2]), int(words[3]), int(words[8]), int(words[9])
  data[(x1, y1)] = (x2, y2) # keys-sensors: values-beacons
  if y1 == y: # sensor is on line of interest
    online.add(x1)
  if y2 == y: # beacon is on line of interest
    online.add(x2)

# Functions:
def man_dist(A, B):
  x1, y1, x2, y2 = A[0], A[1], B[0], B[1]
  return abs(x1 - x2) + abs(y1 - y2)
  
def merge(intervals): # merges intervals and returns minimized result
  merged = [] # output
  intervals.sort() # sort input
  merged.append(intervals[0]) # add first element
  for i in intervals[1:]:
    if merged[-1][0] <= i[0] <= merged[-1][1]: # overlap
      merged[-1][1] = max(i[1], merged[-1][1])
    else:
      merged.append(i)
  return merged

def checkline(Y):
  inter = []
  for sensor, beacon in data.items():
    xs = sensor[0]
    r = man_dist(sensor, beacon) # Manhattan-distance radius
    l = abs(sensor[1] - Y)  # distance from the line of interest
    if l <= r: # sensor is close to the line
      x1, x2 = xs - (r - l), xs + (r - l)
      inter.append([x1, x2]) # add start and end points
  inter = merge(inter)
  return inter

# Merge intervals and substract sensors and beacons in line:
inter_1 = checkline(y)
part1 = sum([x[1] - x[0] + 1 for x in inter_1])
for point in online:
  for interval in inter_1:
    if interval[0] <= point <= interval[1]:
      part1 += -1
print(part1)

# Use edge lines: (y_pos(x)=x+ys-xs+-r+-1, y_neg(x)=x+ys+xs+-r+-1)
coeffs_1, coeffs_2 = set(), set()
for sensor, beacon in data.items():
    xs, ys, xb, yb = sensor[0], sensor[1], beacon[0], beacon[1]
    r = man_dist(sensor, beacon) # Manhattan-distance radius
    p1, p2 = ys - xs + r + 1, ys - xs - r - 1 # lines with pos. coeff.
    n1, n2 = ys + xs + r + 1, ys + xs - r - 1 # lines with neg. coeff.
    coeffs_1.add(p1)
    coeffs_1.add(p2)
    coeffs_2.add(n1)
    coeffs_2.add(n2)
for p in coeffs_1: # calculate all possible intersections points (y_pos = y_neg solutions)
  for n in coeffs_2:
    xp = (n - p) // 2 # intersection coord. x
    yp = (n + p) // 2 # intersection coord. y
    point = (xp, yp)
    if (0 <= xp <= y *2) and (0 <= yp <= y *2): # within bound
      if all(man_dist(point, sensor) > man_dist(sensor,beacon) for sensor, beacon in data.items()):
        print(xp * 4000000 + yp)