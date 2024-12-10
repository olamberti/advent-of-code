grid = {x + y*1j : int(val) for y, line in enumerate(open('d10.txt').readlines()) for x, val in enumerate(line.strip())}
trailheads = [p for p, val in grid.items() if val == 0]

p1, p2 = 0, 0
for start in trailheads:
    target, paths = 1, {(start,)}
    while paths and target <= 9:
        new_paths = set()
        for path in paths:
            for d in [1, -1, 1j, -1j]:
                new_pos = path[-1] + d
                if new_pos in grid and grid[new_pos] == target:
                    new_paths.add((*path, new_pos))
        paths = new_paths
        target += 1
    p1 += len(set([path[-1] for path in paths]))
    p2 += len(paths)

print(p1)
print(p2)