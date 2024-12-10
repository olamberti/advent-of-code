grid, trailheads = {}, set()
for y, line in enumerate(open('d10.txt').readlines()):
    for x, val in enumerate(line.strip()):
        grid[x + y*1j] = int(val)
        if val == '0':
            trailheads.add(x + y*1j)

p1, p2 = 0, 0
for start in trailheads:
    target, paths, ends = 1, {(start,)}, set()
    while paths and target <= 9:
        new_paths = set()
        for path in paths:
            for d in [1, -1, 1j, -1j]:
                new_pos = path[-1] + d
                if new_pos in grid and grid[new_pos] == target:
                        new_paths.add((*path, new_pos))
                        if target == 9:
                            ends.add(new_pos)
        paths = new_paths
        target += 1
    p1 += len(ends)
    p2 += len(paths)

print(p1)
print(p2)