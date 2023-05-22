grid = []
for line in open('11.txt'):
  row = [int(num) for num in line.strip()]
  grid.append(row)

def flash(r, c):
  global total, grid
  total += 1
  for i in range(r - 1, r + 2):
    for j in range(c - 1, c + 2):
      if i == r and j == c: continue
      if (0 <= i < len(grid)) and (0 <= j < len(grid[i])):
        grid[i][j] += 1
        if grid[i][j] == 10: flash(i, j)

step, total = 0, 0
while True:
  step += 1
  
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      grid[r][c] += 1
      if grid[r][c] == 10: flash(r, c)      
  
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] > 9: grid[r][c] = 0

  if step == 100:
    print(total)  

  if sum([sum(row) for row in grid]) == 0:
    print(step)
    break