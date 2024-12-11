from collections import defaultdict

grid, walls_in_x, walls_in_y = {}, defaultdict(list), defaultdict(list)
for y, line in enumerate(open('d06.txt')):
    for x, e in enumerate(line.strip()):
        grid[x + y*1j] = e
        if e == '#':
            walls_in_x[x].append(y)
            walls_in_y[y].append(x)
        elif e not in '.#':
            pos = x + y*1j
            d = {'>': 1, 'v': 1j, '<': -1, '^': -1j}[e]

def has_loop(pos, d):
    cache = set()
    while pos in grid:
        x, y = int(pos.real), int(pos.imag)
        match d:
            case 1:   wall = min([w for w in walls_in_y[y] if w > x], default=None)
            case -1:  wall = max([w for w in walls_in_y[y] if w < x], default=None)
            case 1j:  wall = min([w for w in walls_in_x[x] if w > y], default=None)
            case -1j: wall = max([w for w in walls_in_x[x] if w < y], default=None)           
        if wall is None:
            return False
        pos = (wall - d) + y * 1j if d.real else x + (wall * 1j - d)
        d *= 1j
        if (pos, d) in cache:
            return True
        cache.add((pos, d))

seen, obs = set(), set()
while pos in grid:
    seen.add(pos)
    next_pos = pos + d
    if grid.get(next_pos) == '#':
        d *= 1j
    else:
        if next_pos in grid and next_pos not in seen:
            x, y = int(next_pos.real), int(next_pos.imag)
            walls_in_x[x].append(y), walls_in_y[y].append(x)
            if has_loop(pos, d):
                obs.add(next_pos)
            walls_in_x[x].pop(), walls_in_y[y].pop()
        pos += d

print(len(seen))
print(len(obs))