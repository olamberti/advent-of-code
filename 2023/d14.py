grid = [list(row) for row in open('d14.txt').read().splitlines()]
size = len(grid)

def cycle(grid):
    for _ in range(4):
        grid = tiltup(grid)
        grid = rot(grid)
    return grid

def tiltup(grid):
    move = [0 for _ in range(len(grid[0]))]
    for r, row in enumerate(grid):
        for c, item in enumerate(row):
            if item == '#': move[c] = 0
            elif item == '.': move[c] += 1
            elif move[c] != 0:
                grid[r - move[c]][c] = 'O'
                grid[r][c] = '.'
    return grid

def rot(grid):
    return [list(row[::-1]) for row in zip(*grid)]

def beamload(grid):
    return sum(row.count('O') * (size - r) for r, row in enumerate(grid))

def id(grid):
    return tuple(tuple(line) for line in grid)

# Part 1
print(beamload(tiltup(grid)))

# Part 2
grids, N = [], 1_000_000_000
for step in range(1, N + 1):
    grid = cycle(grid)
    grid_hash = id(grid)
    if grid_hash in grids:
        loop_start = grids.index(grid_hash) + 1
        print(beamload(grids[loop_start + (N - loop_start) % (step - loop_start) - 1]))
        break
    grids.append(id(grid))