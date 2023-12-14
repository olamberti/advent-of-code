grid = tuple(open('d14.txt').read().splitlines())
size = len(grid)

def cycle(grid):
    for _ in range(4):
        grid = tiltup(grid)
        grid = rot(grid)
    return grid

def tiltup(grid):
    grid = [''.join(row) for row in zip(*grid)]
    new_grid = []
    for row in grid:
        new_row = '#'.join([''.join(sorted(list(group), reverse=True)) for group in row.split('#')])
        new_grid.append(new_row)
    return tuple(''.join(row) for row in zip(*new_grid))

def rot(grid):
    grid = [row for row in zip(*grid)]
    return tuple(''.join(row[::-1]) for row in grid)

def beamload(grid):
    return sum(row.count('O') * (size - r) for r, row in enumerate(grid))

# Part 1
print(beamload(tiltup(grid)))

# Part 2
grids, N = [], 1_000_000_000
for step in range(1, N + 1):
    grid = cycle(grid)
    if grid in grids:
        loop_start = grids.index(grid) + 1
        print(beamload(grids[loop_start + (N - loop_start) % (step - loop_start) - 1]))
        break
    grids.append(grid)