grids = open('d13.txt').read().split('\n\n')

def ref_val(grid, ref1 = 0):
    for flip in range(2):
        for x in range(len(grid) - 1):
            if grid[x] == grid[x + 1]:
                p = x
                for i in range(min(p, len(grid) - 2 - p) + 1):
                    if grid[p - i] == grid[p + 1 + i]: continue
                    break
                else:
                    val = p + 1 if flip else (p + 1) * 100
                    if val == ref1: continue
                    else: return val
        grid = [''.join(row) for row in list(zip(*grid))]
    return 0

p1, p2 = 0, 0
for n, grid in enumerate(grids, 1):
    grid = grid.splitlines()
    ref1 = ref_val(grid)
    p1 += ref1

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            ref2 = 0
            if grid[r][c] == '#':
                grid[r] = grid[r][:c] + '.' +  grid[r][c + 1:]
            else:
                continue
            ref2 = ref_val(grid, ref1)
            grid[r] = grid[r][:c] + '#' +  grid[r][c + 1:]
            if ref2:
                p2 += ref2
                break
        if ref2:
            break

print(p1)
print(p2)