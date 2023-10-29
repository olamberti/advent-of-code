import numpy as np

coords, mx, my, Mx, My = [], int(1e10), int(1e10), 0, 0
for i, line in enumerate(open('d06.txt').read().splitlines()):
    x, y = [int(x) for x in line.split(', ')]
    mx, my, Mx, My = min(x, mx), min(y, my), max(x, Mx), max(y, My)
    coords.append((x, y))

def md(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

distmaps, tol = [], 10
for point in coords:
    grid = np.fromfunction(lambda i, j: md(point, (i, j)), (Mx + tol, My + tol), dtype=int)
    distmaps.append(grid)

areas = {}
for i in range(-1, len(coords)): areas[i] = 0

ccm, p2 = np.zeros((Mx + tol, My + tol)), 0
for x in range(Mx + tol):
    for y in range(My + tol):
        cp, cd, td = None, 9999, 0
        for p, grid in enumerate(distmaps):
            if grid[x, y] < cd:
                cd = grid[x, y]
                cp = p
            elif grid[x, y] == cd:
                cp = -1
            td += grid[x, y]
        ccm[x, y] = cp
        if areas[cp] >= 0:
            areas[cp] += 1
            if x == 0 or x == Mx + tol - 1 or y == 0 or y == My + tol - 1:
                areas[cp] = -1
        if td < 10_000: p2 += 1

print(max(areas.values()))    
print(p2)