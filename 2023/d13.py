grids = open('d13.txt').read().split('\n\n')

def ref_val(grid, skip = -1):
    for mul in (100, 1):
        for x in range(len(grid) - 1):
            if grid[x] == grid[x + 1]:
                for i in range(min(x, len(grid) - 2 - x) + 1):
                    if grid[x - i] != grid[x + 1 + i]: break
                else:
                    val = (x + 1) * mul
                    if val != skip: return val
        grid = [list(line) for line in zip(*grid)]
    return 0

p1, p2 = 0, 0
for n, grid in enumerate(grids, 1):
    grid = [list(line) for line in grid.splitlines()]
    v1 = ref_val(grid)
    p1 += v1

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#': grid[r][c] = '.'
            else: continue
            v2 = ref_val(grid, v1)
            grid[r][c] = '#'
            if v2:
                p2 += v2
                break
        if v2: break

print(p1)
print(p2)