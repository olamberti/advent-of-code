grid = open('d03.txt').read().splitlines()
slopes = [1, 3, 5, 7, 0.5]

t, w, l = [0] * 5, len(grid[0]), len(slopes) - 1
for i, row in enumerate(grid):
  for j, s in enumerate(slopes):
    if j == l and i % 2 != 0: continue
    pos = int((i * s) % w)
    if row[pos] == '#': t[j] += 1
print(t[1])

a = 1
for x in t: a *= x
print(a)