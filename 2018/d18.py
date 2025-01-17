grid = {}
for y, line in enumerate(open('d18.txt').readlines()):
    for x, c in enumerate(line.strip()):
        grid[(x, y)] = c
W, H = x, y

def ns(x, y):
    return [(x+dx, y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx or dy]

def step(grid):
    new_grid = {}
    for (x, y), c in grid.items():
        adj = [grid.get(n) for n in ns(x, y)]
        if c == '.':
            new_grid[(x, y)] = '|' if adj.count('|') >= 3 else '.'
        elif c == '|':
            new_grid[(x, y)] = '#' if adj.count('#') >= 3 else '|'
        elif c == '#':
            new_grid[(x, y)] = '#' if '#' in adj and '|' in adj else '.'
    return new_grid

def grid2str(grid):
    return ''.join(''.join(grid.get((x, y), '.') for x in range(W+1)) for y in range(H+1))

cache = {grid2str(grid): 0}
for i in range(1_000_000_000):
    if i == 10:
        print(list(grid.values()).count('|') * list(grid.values()).count('#'))
    grid = step(grid)
    if grid2str(grid) in cache:
        period = i - cache[grid2str(grid)]
        rem = (1_000_000_000 - i - 1) % period
        for j in range(rem):
            grid = step(grid)
        print(list(grid.values()).count('|') * list(grid.values()).count('#'))
        break
    cache[grid2str(grid)] = i