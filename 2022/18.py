# Init:
directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
lava, lava_faces = set(), dict()                     # lave cells and lave faces with number of occurance
mx = my = mz = float('inf')                          # lower bounds of volume
Mx = My = Mz = -float('inf')                         # upper bounds of volume

# Read input, add lava cell and count face occurances:
for line in open('18.txt'):
  x, y, z = cell = tuple(map(int, line.split(',')))  
  lava.add(cell)
  mx, my, mz = min(mx,x), min(my,y), min(mz,z)
  Mx, My, Mz = max(Mx,x), max(My,y), max(Mz,z)

  for dx, dy, dz in directions:
    face = (x + dx / 2, y + dy / 2, z + dz / 2)      # face coordinates
    if face not in lava_faces: lava_faces[face] = 1  # new face occurance
    else: lava_faces[face] += 1                      # face appeared again

surface = list(lava_faces.values()).count(1)         # count faces that only appear once
print(surface)

# Water simulation around lava drop:
mx, my, mz = mx - 1, my - 1, mz - 1
Mx, My, Mz = Mx + 1, My + 1, Mz + 1

start = (mx, my, mz)                                 # starting point for water flow
water, frontier = set(), set()                       # water cells and water front
water.add(start)
frontier.add(start)
exterior_surface = 0                                 # exterior surface of lava

while len(frontier):                                 # runs until there is a water front
  new_frontier = set()                               # new water front
  for x, y, z in frontier:  

    for dx, dy, dz in directions:
      nx, ny, nz = cell = (x + dx, y + dy, z + dz)   # new potential cell
      if not (mx <= nx <= Mx and my <= ny <= My and mz <= nz <= Mz):
        continue                                     # cell not within bounds
      if cell in water:                                     
        continue                                     # cell is a water piece                                         
      if cell in lava:                                                 
        exterior_surface += 1                        # cell is a lave peice, exterior surface of lava found
        continue
      water.add(cell)
      new_frontier.add(cell) 
      
  frontier = new_frontier

print(exterior_surface)