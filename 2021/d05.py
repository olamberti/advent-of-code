# Start-up definitions and data read
import numpy as np
with open('d05.txt', 'r') as input:
  text = input.read().splitlines()

data = []
for line in text:
  line = line.split()
  coord_1 = line[0].split(",")
  coord_2 = line[2].split(",")
  data.append([int(coord_1[0]), int(coord_1[1]), int(coord_2[0]), int(coord_2[1])])

def draw_line(diagram, line):
  X1, Y1, X2, Y2 = line[0], line[1], line[2], line[3]
  dir = [X2 - X1, Y2 - Y1]
  steps = max([abs(cor) for cor in dir])
  if dir[0] != 0:
    dir[0] = dir[0] // abs(dir[0])
  if dir[1] != 0:
    dir[1] = dir[1] // abs(dir[1])
  for n in range(steps + 1):
    diagram[X1 + n * dir[0]][Y1 + n * dir[1]] += 1
  return diagram
  
# Process data:
size = max([max(sub) for sub in data]) + 1
dia_1 = np.zeros((size, size))
dia_2 = np.zeros((size, size))
for line in data:
  x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
  draw_line(dia_2, line)
  if (x1 == x2) or (y1 == y2):
    draw_line(dia_1, line)

# Count intersections:
intersections_1 = np.count_nonzero(dia_1 > 1)
intersections_2 = np.count_nonzero(dia_2 > 1)
print(intersections_1)
print(intersections_2)