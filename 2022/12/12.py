# Read input:
with open('12.txt', 'r') as input:
  heightmap = [list(line) for line in input.read().splitlines()]

# Initialization and function definitions:
height, width = len(heightmap), len(heightmap[0])
order, new_ends = 'abcdefghijklmnopqrstuvwxyz', []
for x in range(height):
  for y in range(width):
    if heightmap[x][y] == 'S':
      start, heightmap[x][y] = [x, y], 'a'
      new_ends.append([x, y]) # for part 2
    elif heightmap[x][y] == 'E':
      end, heightmap[x][y] = [x, y], 'z'
    elif heightmap[x][y] == 'a':
      new_ends.append([x, y]) # for part 2

def get_neighbours(cell):
  X, Y = cell[0], cell[1]
  value, neighbours = heightmap[X][Y], []
  for dir in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # up, right, down and left
    X_n, Y_n = X + dir[0], Y + dir[1]
    if (height > X_n >= 0) and (width > Y_n >= 0): # neighbour is within map
      value_n = heightmap[X_n][Y_n]
      if (order.index(value_n) - order.index(value)) < 2: # neighbour is valid
        neighbours.append([X_n, Y_n])
  return neighbours

def calc_shortest_path(start_point, end_points): # Breadth First Search algortihm
  frontier, reached, is_end_reached = [start_point], [start_point], False
  steps = 0
  while not is_end_reached:
    steps += 1
    new_frontier = []
    for current_cell in frontier:
      current_neighbours = get_neighbours(current_cell)
      for elem in current_neighbours:
        if (elem not in reached) and (elem not in new_frontier):
          reached.append(elem)
          new_frontier.append(elem)
          if elem in end_points:
            is_end_reached = True
    frontier = new_frontier
  return steps
    
# Path finding for part 1:
steps_1 = calc_shortest_path(start, [end])
print(steps_1)

# Path finding for part 2:
order = order[::-1]
steps_2 = calc_shortest_path(end, new_ends)
print(steps_2)