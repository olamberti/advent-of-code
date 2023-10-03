# Read in data:
with open('d09.txt', 'r') as input:
  data = [[int(x) for x in sublist] for sublist in [list(line) for line in input.read().splitlines()]]

# Functions:
def get_neighbours(X, Y):
  neighbours = []
  for dir in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # up, right, down and left
    X_n, Y_n = X + dir[0], Y + dir[1]
    if (height > X_n >= 0) and (width > Y_n >= 0): # neighbour is within map
      neighbours.append([X_n, Y_n])
  return neighbours
  
def is_low_point(x, y):
  is_lowest_point = True
  neighbours_to_check = get_neighbours(x, y)
  for neighbour in neighbours_to_check:
    x_n, y_n = neighbour[0], neighbour[1]
    if data[x][y] >= data[x_n][y_n]:
      is_lowest_point = False
  return is_lowest_point
  
# Find low points:
height, width = len(data), len(data[0])
total_risk_level =  0
low_points = []
for x in range(height):
  for y in range(width):
   if is_low_point(x,y):
    total_risk_level += data[x][y] + 1
    low_points.append([x, y])
print(total_risk_level)

# Find basins:
basins = []
for low_point in low_points:
  basin_size, frontier, reached = 1, [low_point], [low_point]
  while frontier != []:
    new_frontier = []
    for point in frontier:
      frontier_neighbours = get_neighbours(point[0], point[1])
      for my_neighbour in frontier_neighbours:
        x_mn, y_mn = my_neighbour[0], my_neighbour[1]
        if data[x_mn][y_mn] == 9:
          continue
        elif (my_neighbour not in reached) and (my_neighbour not in new_frontier):
          new_frontier.append(my_neighbour)
          reached.append(my_neighbour)
          basin_size += 1
    frontier = new_frontier
  basins.append(basin_size)
basins = sorted(basins)
print(basins[-1] * basins[-2] * basins[-3])