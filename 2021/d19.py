# Read input:
data = []
for line in open('d19.txt', 'r'):
  line = line.strip()
  if 'scanner' in line:          # if we have a new scanner
    i = int(line.split()[2])     # read scanner id
    data.append(set())           # add new sensor set to data
  elif line == '': continue
  else:
    data[i].add(tuple([int(x) for x in line.split(',')]))  # add beacon to sensor set

# Functions:
def allrots(s):             # calculates all 24 orientation permutations of sensor data
  r = []
  for _ in range(3):        # permutations of coordinates
    for _ in range(2):      # swapping directions of current x and y
      for _ in range(4):    # rotating around current x by 90 deg
        r.append(s)
        s = {(x, -z, y) for x, y, z in s}
      s = {(-x, -y, z) for x, y, z in s}
    s = {(-y, z, -x) for x, y, z in s}
  return r

def add(a, b):  # adds vectors: a + b
  return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
  
def sub(a, b):  # subtracts vectors: a - b
  return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def intersect(s1, s2):                  # checks if two sensors s1 and s2 intersect
  for s2 in allrots(s2):                # check for all rotations in s2
    for b1 in s1:                       # for all beacon in s1
      for b2 in s2:                     # for all beacon in s2
        off = sub(b1, b2)               # offset of b1 and b2
        c = {add(b, off) for b in s2}   # shit sensors in s2 with offset
        if len(s1 & c) >= 12:           # if intersection is bigger than 12
          return (c, off)               # return the rotated sensor set and their offset

def man_dist(a, b):  # Manhattan distance of two points
  return(sum([abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2])]))
  
# Explore sensors and beacons
b = set(data[0])                   # explored beacons
s = [(0, 0, 0)]                    # explored sensors
queue = data[1:]                   # queue other sensors into data

while queue:                       # while queue is not empty
  i = intersect(b, queue[0])       # intersect current
  if i:                            # if we had intersection
    i, off = i                     # unpack intersection
    b |= i                         # unite the two sets
    s.append(off)
    queue.pop(0)                   # remove sensor from queue
  else:
    queue.append(queue.pop(0))     # otherwise add sensor to the end of queue

print(len(b))

# Calculate maximum Manhattan distance
md = 0
for s1 in s:
  for s2 in s:
    md = max(md, man_dist(s1, s2))

print(md)