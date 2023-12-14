from collections import deque as dq

grid = [list(line) for line in open('d14.txt').read().splitlines()]
size = len(grid)

def cycle(grid):
    for d in ('N', 'W', 'S', 'E'):
        grid = tilt(grid, d)
    return grid

def id(grid):
    rounds = set()
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == 'O': rounds.add((x, y))
    return rounds

def tilt(grid, d):
    if d == 'N': grid = [list(line) for line in zip(*grid)]
    elif d == 'S': grid = [list(line[::-1]) for line in zip(*grid)]
    elif d == 'W': pass
    elif d == 'E': grid = [line[::-1] for line in grid]

    new_grid = []
    for col in grid:
        new_col = ''
        rounds = dq([i for i, r in enumerate(col) if r == 'O'])
        squares = dq([i for i, r in enumerate(col) if r == '#'])
        for i in range(len(col)):
            if i in squares:
                new_col += '#'
                squares.popleft()
            elif rounds and (not squares or rounds[0] < squares[0]):
                new_col += 'O'
                rounds.popleft()
            else:
                new_col += '.'
        new_grid.append(list(new_col))
    
    if d == 'N': new_grid = [line for line in zip(*new_grid)]
    elif d == 'S': new_grid = [line[::-1] for line in zip(*new_grid[::-1])][::-1]
    elif d == 'W': pass
    elif d == 'E': new_grid = [line[::-1] for line in new_grid]
    return new_grid

def northload(rounds):
    load = 0
    for x, y in rounds:
        load += size - y
    return load

# Part 1
print(northload(id(tilt(grid, 'N'))))

# Part 2
seen, N = [], 1_000_000_000
for step in range(1, N + 1):
    grid = cycle(grid)
    if id(grid) in seen:
        s_loop = seen.index(id(grid)) + 1
        loop = step - s_loop
        rem = (N - s_loop) % loop
        break
    seen.append(id(grid))
print(northload(seen[s_loop + rem - 1]))