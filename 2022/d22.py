# Read input:
grid = []
height, width = 0, 0

with open('d22.txt', 'r') as input:
  is_grid = True
  for line in input:
    if line == "\n": is_grid = False
    if is_grid: 
      height += 1
      width = max(width, len(line.strip('\n')))
      grid.append(line.strip('\n'))
    else: instructions = line.replace('R', ' R ').replace('L', ' L ').split()

# Add borders to map:
for r in range(height):
  if len(grid[r]) < width:
    grid[r] += (' ' * (width - len(grid[r])))
  grid[r] = ' ' + grid[r] + ' '

grid.insert(0,  ' ' * (width + 2))
grid.append(' ' * (width + 2))
  
# Initial position:
r, c, dir = 1, 1, [0, 1]
while grid[r][c] != '.': c += 1

# Move on map - Part 1:
def move(steps):
  global r, c, dir, grid
  while steps > 0:
    rn, cn = r + dir[0], c + dir[1]      
    tile = grid[rn][cn]
    
    if tile == ' ': # out of map
      if dir == [0, 1]: cn = 0
      elif dir == [0, -1]: cn = width + 1
      elif dir == [1, 0]: rn = 0
      elif dir == [-1, 0]: rn = height + 1
      
      while grid[rn][cn] == ' ': rn, cn = rn + dir[0], cn + dir[1]
      tile = grid[rn][cn]
      
    if tile == '#': break # hit a wall
    elif tile == '.': # valid step
      r, c = rn, cn
      steps += -1
      continue

def turn(rot):
  if(rot) == 'L': dir[0], dir[1] = -dir[1], dir[0]
  elif(rot) == 'R': dir[0], dir[1] = dir[1], -dir[0]

for command in instructions:
  if command.isnumeric(): move(int(command))
  else: turn(command)

# Calculate part 1 answer:
def calc_result(r, c, dir):
  if dir == [0, 1]: face = 0
  elif dir == [1, 0]: face = 1
  elif dir == [0, -1]: face = 2
  elif dir == [-1, 0]: face = 3
  return r * 1000 + c * 4 + face
print(calc_result(r, c, dir))

#############################################################################

# Initial position for part 2:
r, c, dir = 1, 1, [0, 1]
while grid[r][c] != '.': c += 1
  
# Move on map - part 2:
r, c, dir = 1, 1, [0, 1]
while grid[r][c] != '.': c += 1

def move_cube(steps):
  global r, c, dir, grid
  while steps > 0:
    rn, cn = r + dir[0], c + dir[1]      
    tile = grid[rn][cn]
    dr, dc = dir[0], dir[1]
    
    if tile == ' ': # out of map
      if (rn == 0) and (50 < cn <= 100): # from side 1 top to side 6 left
        dir = [0, 1]
        rn, cn = cn + 100, 1
      elif (rn == 0) and (100 < cn <= 150): # from side 2 top to side 6 bottom
        dir = [-1, 0]
        rn, cn = 200, cn - 100
      elif (0 < rn <= 50) and (cn == 50): # from side 1 left to side 4 left
        dir = [0, 1]
        rn, cn = 151 - rn, 1
      elif (0 < rn <= 50) and (cn == 151): # from side 2 right to side 5 right
        dir = [0, -1]
        rn, cn = 151 - rn, 100
      elif (50 < rn <= 100) and (cn == 50): # from side 3 left to side 4 top
        dir = [1, 0]
        rn, cn = 101, rn - 50
      elif (rn == 51) and (100 < cn <= 150): # from side 2 bottom to side 3 right
        dir = [0, -1]
        rn, cn = cn - 50, 100
      elif (50 < rn <= 100) and (cn == 101): # from side 3 right to side 2 bottom
        dir = [-1, 0]
        rn, cn = 50, rn + 50
      elif (rn == 100) and (0 < cn <= 50): # from side 4 top to side 3 left
        dir = [0, 1]
        rn, cn = cn + 50, 51
      elif (100 < rn <= 150) and (cn == 0): # from side 4 left to side 1 left
        dir = [0, 1]
        rn, cn = 151 - rn, 51
      elif (100 < rn <= 150) and (cn == 101): # from side 5 right to side 2 right
        dir = [0, -1]
        rn, cn = 151 - rn, 150
      elif (rn == 151) and (50 < cn <= 100): # from side 5 bottom to side 6 right
        dir = [0, -1]
        rn, cn = cn + 100, 50
      elif (150 < rn <= 200) and (cn == 0): # from side 6 left to side 1 top
        dir = [1, 0]
        rn, cn = 1, rn - 100
      elif (150 < rn <= 200) and (cn == 51): # from side 6 right to side 5 bottom
        dir = [-1, 0]
        rn, cn = 150, rn - 100
      elif (rn == 201) and (0 < cn <= 50): # from side 6 bottom to side 2 top:
        dir = [1, 0]
        rn, cn = 1, cn + 100

      tile = grid[rn][cn]
      
    if tile == '#':
      dir[0], dir[1] = dr, dc # reset direction
      break
    elif tile == '.':
      r, c = rn, cn
      steps += -1
      continue

for command in instructions:
  if command.isnumeric(): move_cube(int(command))
  else: turn(command)

# Calculate part 2 answer:
def calc_result(r, c, dir):
  if dir == [0, 1]: face = 0
  elif dir == [1, 0]: face = 1
  elif dir == [0, -1]: face = 2
  elif dir == [-1, 0]: face = 3
  return r * 1000 + c * 4 + face
print(calc_result(r, c, dir))