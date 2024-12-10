grid = {x + y*1j : int(val) for y, line in enumerate(open('d10.txt'))
                            for x, val in enumerate(line.strip())}
target, paths, = 1, [(p, ) for p, val in grid.items() if val == 0]

while target <= 9 and paths:
    new_paths = set()
    for path in paths:
        for d in [1, -1, 1j, -1j]:
            new_pos = path[-1] + d
            if new_pos in grid and grid[new_pos] == target:
                new_paths.add((*path, new_pos))
    paths = new_paths
    target += 1

print(len(set([(path[0], path[-1]) for path in paths])))
print(len(paths))