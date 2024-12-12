grid = {x + y *1j: c for y, row in enumerate(open('d12.txt'))
                     for x, c in enumerate(row.strip())}
p1, p2, dirs = 0, 0, [1, -1, 1j, -1j]
while grid:
    pos = next(iter(grid.keys()))
    plant = grid.pop(pos)

    front, region, edges = {pos}, {pos}, {d: set() for d in dirs}
    while front:
        new_front = set()
        for pos in front:
            for d in dirs:
                next_pos = pos + d
                if next_pos in grid and grid[next_pos] == plant:
                    new_front.add(next_pos), region.add(next_pos)
                    grid.pop(next_pos)
                elif next_pos not in region:
                    edges[d].add(next_pos)
        front = new_front
    p1 += len(region) * sum([len(x) for x in edges.values()])

    sides = 0
    for d, vals in edges.items():
        seen = set()
        for edge in vals:
            if edge in seen:
                continue
            seen.add(edge)
            sides += 1
            front = {edge}
            while front:
                new_front = set()
                for pos in front:
                    for next_pos in (pos + d * 1j, pos - d * 1j):
                        if next_pos in seen:
                            continue
                        seen.add(next_pos)
                        if next_pos in vals:
                            new_front.add(next_pos)
                front = new_front
    p2 += len(region) * sides

print(p1)
print(p2)