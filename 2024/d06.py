grid = {x + y*1j: e for y, line in enumerate(open('d06.txt'))
                    for x, e in enumerate(line.strip())}
for k, v in grid.items():
    if v not in '.#':
        pos, d = k, {'>': 1, 'v': 1j, '<': -1, '^': -1j}[v]
        break

paths, cache, obstacles = set(), set(), set()
while pos in grid:
    paths.add(pos)
    if grid.get(pos + d) == '#':
        d *= 1j
    else:
        obs = pos + d
        if obs in grid and obs not in paths:
            n_pos, n_d, cache = pos, d * 1j, set()
            while n_pos in grid:
                if grid.get(n_pos + n_d) == '#' or (n_pos + n_d) == obs:
                    if (n_pos, n_d) in cache:
                        obstacles.add(obs)
                        break
                    cache.add((n_pos, n_d))
                    n_d *= 1j
                else:
                    n_pos += n_d
        pos += d

print(len(paths))
print(len(obstacles))