# Read input:
with open("08.txt") as input:
  data = [list(line) for line in input.read().splitlines()]
  
# Scenic score for a given direction:
def calc_score(my_tree, my_row):
  score = 1
  for i, current_tree in enumerate(my_row, 1):
    if (trees[x, y] > current_tree) and (i != len(my_row)):
      score += 1
    else:
      break
  return score

# Convert to matrix:
import numpy as np
trees = np.array(data, "int")
width, height = trees.shape

# Calculate visibility (1 if tree is visible, 0 if not) and scenic score:
visibility = np.zeros((width, height), "int")
scenic_score = np.zeros((width, height), "int")
for x in range(width):
  for y in range(height):
    # Check visibility:
    if (x == 0) or (x == width - 1) or (y == 0) or (y == height - 1):  # tree is on the edge
      visibility[x, y] = 1
      continue
    else:  # tree is not on the edge
      if (trees[x, y] > np.amax(trees[: x, y])) or (trees[x, y] > np.amax(trees[(x + 1):, y])):
        visibility[x, y] = 1
      elif (trees[x, y] > np.amax(trees[x, : y])) or (trees[x, y] > np.amax(trees[x, (y + 1) :])):
        visibility[x, y] = 1
      # Calculate scenic score:
      score_up = calc_score(trees[x, y], np.flip(trees[: x, y])) # looking up
      score_down = calc_score(trees[x, y], trees[(x + 1):, y]) # looking down
      score_left = calc_score(trees[x, y], np.flip(trees[x, : y])) # looking left
      score_right = calc_score(trees[x, y], trees[x, (y + 1) :]) # looking right
      scenic_score[x, y] = score_up * score_down * score_left * score_right

print(np.sum(visibility))
print(np.amax(scenic_score))