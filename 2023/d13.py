def ref_val(grid, mismatch = 0):
    for w in (100, 1):
        for x in range(1, len(grid)):
            top = grid[:x][::-1]
            bottom = grid[x:]
            if sum(sum(a != b for a, b in zip(t, b)) for t, b in zip(top, bottom)) == mismatch:
                return w * x
        grid = [list(line) for line in zip(*grid)]
    return 0

p1, p2 = 0, 0
for grid in open('d13.txt').read().split('\n\n'):
    grid = [list(line) for line in grid.splitlines()]
    p1 += ref_val(grid)
    p2 += ref_val(grid, 1)

print(p1)
print(p2)