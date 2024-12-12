grid = {x + y *1j: c for y, row in enumerate(open('d12.txt'))
                     for x, c in enumerate(row.strip())}

p1, p2 = 0, 0
while grid:
    pos = next(iter(grid.keys()))
    plant = grid.pop(pos)

    front, region, edges = {pos}, {pos}, []
    while front:
        new_front = set()
        for pos in front:
            for d in [1, -1, 1j, -1j]:
                next_pos = pos + d
                if next_pos in grid and grid[next_pos] == plant:
                    new_front.add(next_pos)
                    region.add(next_pos)
                    grid.pop(next_pos)
                elif next_pos not in region:
                    edges.append(set((pos + 0.5*(d + d*1j), pos + 0.5*(d - d*1j))))
        front = new_front
    p1 += len(region) * len(edges)

    sides = 0
    while edges:
        a, b = edges.pop()
        s, sv = b, a - b
        while a != s:
            v = a - b
            next_pos = [edge for edge in edges if a in edge]
            if len(next_pos) == 1:
                c, d = next_pos[0]
                edges.remove(next_pos[0])
            else:
                for i in range(len(next_pos)):
                    c, d = next_pos[i]
                    if not ((c - d) == v or (d - c) == v):
                        edges.remove(next_pos[i])
                        break
            a, b = d if a == c else c, a
            if v != a - b:
                sides += 1
            nv = a - b
        if nv != sv:
            sides += 1
    p2 += len(region) * sides

print(p1)
print(p2)