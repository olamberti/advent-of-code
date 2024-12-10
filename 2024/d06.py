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

def is_looping(pos, d):
    cache = set()
    while pos in grid:
        x, y = int(pos.real), int(pos.imag)
        if d.real:
            if d == 1:
                wall = min([w for w in walls_in_y[y] if w > x], default=None)
            else:
                wall = max([w for w in walls_in_y[y] if w < x], default=None)
            if wall is not None:
                pos = (wall - d) + y * 1j
        if d.imag:
            if d == 1j:
                wall = min([w for w in walls_in_x[x] if w > y], default=None)
            else:
                wall = max([w for w in walls_in_x[x] if w < y], default=None)
            if wall is not None:
                pos = x + wall * 1j - d
        d *= 1j
        if wall is None:
            return False
        if (pos, d) in cache:
            return True
        cache.add((pos, d))

seen, obs = set(), set()
while pos in grid:
    seen.add(pos)
    if grid.get(pos + d) == '#':
        d *= 1j
    else:
        if (pos + d) in grid and (pos + d) not in seen:
            x, y = int(pos.real + d.real), int(pos.imag + d.imag)
            walls_in_x[x].append(y), walls_in_y[y].append(x)
            if is_looping(pos, d):
                obs.add(pos + d)
            walls_in_x[x].pop(), walls_in_y[y].pop()
        pos += d

print(len(seen))
print(len(obs))