# Input parsing:
import math, cmath   # complex number calculations
ast = set()          # set of asteroids

for y, line in enumerate(open('d10.txt', 'r').read().splitlines()):  # go through each line
  for x, elem in enumerate(line):                                   # go through each character
    if elem == '#': ast.add((x, y))                                 # if hashtag, add to asteroids
      
# P1:
ims, ang = None, {}                               # instant monitoring stations coordinates, angles with list of asteroids
for a in ast:                                     # loop through each asteroid
  angles = {}                                     # current angles
  for b in ast:                                   # loop through each asteroid again
    if b == a: continue                           # if a is the same as b we skip
    z = complex(b[0] - a[0], b[1] - a[1])         # otherwise we create the complex number z
    ph = cmath.phase(z)                           # phase of z
    if ph < 0: ph = 2 * math.pi + ph              # convert from [-pi, pi] to [0, 2pi]
    if ph >= 1.5*math.pi: ph -= 1.5*math.pi       # shift base to 270deg 1.
    else: ph += 0.5 * math.pi                     # shift base to 270deg 2.
    if ph not in angles: angles[ph] = [b]         # if we did not have this phase angle yet, create it
    else: angles[ph].append(b)                    # otherwise add asteroid to the list
  if len(angles) > len(ang): ims, ang = a, angles # if the new angle list is longer, it means we see more asteroids
    
print(len(ang))                                # print the length of angles, a.k.a. the number of visible asteroids

# P2:
def dist(a, b):                 # distance between points a & b
  return ((a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2) ** 0.5
  
tars = ang[sorted(ang)[199]]    # 200th elem in the angles (can do this, since we saw more than 200 asteroids)
md = float('inf')               # min distance from IMS
for a in tars:                  # loop through possible targets
  d = dist(ims, a)              # distance between IMS and asteroid
  if d < md: md, tar = d, a     # if the distance is smaller than the current, save new minimal distance and the target
print(tar[0] * 100 + tar[1])    # calculate part 2 answer