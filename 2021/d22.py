# Read input:
steps = []                                                                            # storing procedure steps
for line in open('d22.txt', 'r').read().splitlines():                                 # iterate through input data
  command, coords = line.split()                                                      # on/off, coordinates
  x, y, z = [c[2:].split('..') for c in coords.split(',')]                            # read coordinate pairs
  x, y, z = [int(x[0]), int(x[1])], [int(y[0]), int(y[1])], [int(z[0]), int(z[1])]    # convert them to integers
  steps.append((command, x, y, z))                                                    # store them in steps
  
# Part 1:
def get_range(n):                                   # returns the range according to part 1
  return range(max(n[0], -50), min(n[1], 50) + 1)   # range part between -50 to 50
  
cubes = set()                                       # storing 1x1x1 cubes
for step in steps:                                  # iterate through rebbot sequence steps
  comm = step[0]                                    # on / off
  x, y, z = step[1], step[2], step[3]               # cube ranges
  for i in get_range(x):                            # iterate through x
    for j in get_range(y):                          # iterate through y
      for k in get_range(z):                        # iterate through z
        if comm == 'on' and (i, j, k) not in cubes: # if turning on
          cubes.add((i, j, k))                      # add cube
        elif comm == 'off' and (i, j, k) in cubes:  # if turning off
          cubes.discard((i, j, k))                  # remove cube
print(len(cubes))                                   # print final volume

# Cube class definition:
class Cuboid():                                                        # cuboid class to handle cuboids
  def __init__(self, x1, x2, y1, y2, z1, z2):                          # input: two opposite corners
    self.x1, self.y1, self.z1 = min(x1, x2), min(y1, y2), min(z1, z2)  # 1st vertice
    self.x2, self.y2, self.z2 = max(x1, x2), max(y1, y2), max(z1, z2)  # 2nd vertice
    self.vol = ((x2 - x1) + 1) * ((y2 - y1) + 1) * ((z2 - z1) + 1)     # volume

  def __iter__(self):                               # iterate function of class
    yield self.x1
    yield self.x2
    yield self.y1
    yield self.y2
    yield self.z1
    yield self.z2
    
  def __eq__(self, other):                          # equality check of class
    return isinstance(other, Cuboid) and tuple(self)==tuple(other)
    
  def __ne__(self, other):                          # non-equality check of class
    return not (self==other)                        # opposite of equality
  
  def __repr__(self):                               # print function of class
    return type(self).__name__+repr(tuple(self))    # print type + coordinates
    
  def intersect(self, other):                       # intersection of two cuboids
    s, o = self, other                              # cuboids to check
    x1 = max(s.x1, o.x1)                            # lower boundary in x
    x2 = min(s.x2, o.x2)                            # upper boundary in x
    y1 = max(s.y1, o.y1)                            # lower boundary in y
    y2 = min(s.y2, o.y2)                            # upper boundary in y
    z1 = max(s.z1, o.z1)                            # lower boundary in z
    z2 = min(s.z2, o.z2)                            # upper boundary in z
    if x1 <= x2 and y1 <= y2 and z1 <= z2:          # if boundary is valid
      return Cuboid(x1, x2, y1, y2, z1, z2)         # return intersection
    else: return None                               # no intersection
  __and__ = intersect

  def subtract(self, other):                        # subtraction function
    s, o = self, other                              # input cuboids
    inter = s&o                                     # intersection of the two cuboids
    results = []                                    # result list of cuboids to return
    
    if not inter:                                   # there is no intersection
      results.append(self)                          # add only original cuboid t othe list
    
    elif inter != self:                             # intersection is not the original cuboid
      xs, ys, zs = [s.x1], [s.y1], [s.z1]           # x, y and z coordinates for the new cuboids
      if s.x1 < o.x1 <= s.x2:
        xs.append(o.x1 - 1)
        xs.append(o.x1)
      if s.x1 <= o.x2 < s.x2:
        xs.append(o.x2)
        xs.append(o.x2 + 1)
      if s.y1 < o.y1 <= s.y2:
        ys.append(o.y1 - 1)
        ys.append(o.y1)
      if s.y1 <= o.y2 < s.y2:
        ys.append(o.y2)
        ys.append(o.y2 + 1)
      if s.z1 < o.z1 <= s.z2:
        zs.append(o.z1 - 1)
        zs.append(o.z1)
      if s.z1 <= o.z2 < s.z2:
        zs.append(o.z2)
        zs.append(o.z2 + 1)
      xs.append(s.x2)
      ys.append(s.y2)
      zs.append(s.z2)

      for i in range(len(xs)//2):                  # iterate through x pairs
        xm, xM = xs[2*i], xs[2*i + 1]            
        for j in range(len(ys)//2):                # iterate through y pairs
          ym, yM = ys[2*j], ys[2*j + 1]
          for k in range(len(zs)//2):              # iterate through z pairs
            zm, zM = zs[2*k], zs[2*k + 1]          
            c = Cuboid(xm, xM, ym, yM, zm, zM)     # generate cuboid
            if c != inter:                         # if it is not in the intersection
              results.append(c)                    # add it to the results           
    return results                                 # return list of cubes
  __sub__ = subtract

# Part 2:
cuboids = []                                        # list of cuboids turned on

for step in steps:                                  # loop through reboot sequence steps
  new_cuboids = []
  comm = step[0]                                    # on / off
  x, y, z = step[1], step[2], step[3]               # cube ranges
  cc = Cuboid(*x, *y, *z)                           # generate current cube
  for c in cuboids:                                 # loop through cuboids
    res = c - cc                                    # subtract new cuboid from the current list
    for r in res:                                   # loop through the result
      new_cuboids.append(r)                         # add result to new list
  if comm == 'on': new_cuboids.append(cc)           # add current cube to the list too
  cuboids = new_cuboids.copy()                      # copy nem cuboids

vol = 0                # total volume
for c in cuboids:      # loop through cuboids
  vol += c.vol         # increase volume
print(vol)             # print volume