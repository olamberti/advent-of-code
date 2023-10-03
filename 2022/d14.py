# Read and parse data
with open('d14.txt', 'r') as input:
  text = [lines.split('->') for lines in input.read().splitlines()]
data = []
for i, line in enumerate(text):
  data.append([])
  for j, coords in enumerate(line):
    x, y = int(coords.split(',')[0]), int(coords.split(',')[1])
    data[i].append((x, y))
    
# Create map:
source, rocks, sands = [500,0], set(), set()
for row in data:
  for i in range(len(row) - 1):
    x_1, y_1 = row[i][0], row[i][1]
    x_2, y_2 = row[i+1][0], row[i+1][1]
    dir_x = (x_2 - x_1) // abs(x_2 - x_1) if x_2 != x_1 else 0 
    dir_y = (y_2 - y_1) // abs(y_2 - y_1) if y_2 != y_1 else 0
    if i == 0:
      rocks.add((x_1, y_1))
    while [x_1, y_1] != [x_2, y_2]:
      x_1 += dir_x
      y_1 += dir_y
      rocks.add((x_1, y_1))
      
depth = max([rock[1] for rock in rocks])
half_floor = depth + 2

for x in range((500 - half_floor), (500 + half_floor + 1)):
  rocks.add((x, depth + 2))
x_min, x_max = min([rock[0] for rock in rocks]), max([rock[0] for rock in rocks])
y_min, y_max = min([rock[1] for rock in rocks]), max([rock[1] for rock in rocks])

# Functions:
def next_sand_pos():
  global sand, part_1, sand_1
  not_blocked = True
  while not_blocked:
    not_landed = True
    path = []
    current_pos = (source[0], source[1])
    while not_landed:
      next_pos = (current_pos[0], current_pos[1] + 1)
      if part_1:
        if current_pos[1] > depth:
          part_1 = False
          sand_1 = sand
      if next_pos not in rocks:
        if next_pos not in sands: # cell below is free
          current_pos = next_pos
          path.append(next_pos)
          continue
      next_pos = (next_pos[0] - 1, next_pos[1])
      if next_pos not in rocks:
        if next_pos not in sands: # cell below and to the left is free
          current_pos = next_pos
          path.append(next_pos)
          continue
      next_pos = (next_pos[0] + 2, next_pos[1])
      if next_pos not in rocks:
        if next_pos not in sands: # cell below and to the left is free
          current_pos = next_pos
          path.append(next_pos)
          continue
      if current_pos == (500, 0):
        not_blocked = False
      not_landed = False
      sand += 1
      sands.add(current_pos)
    if len(path) > 1:
      path.pop()
      current_pos = path[-1]
  return not_blocked
    
# Run simulation:
sand = 0
part_1 = True
next_sand_pos()
print(sand_1)
print(sand)