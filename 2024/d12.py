from collections import deque

grid = {x + y *1j: c for y, row in enumerate(open('d12.txt'))
                     for x, c in enumerate(row.strip())}
dirs, p1, p2 = [1, -1, 1j, -1j], 0, 0

while grid:
    pos = next(iter(grid.keys()))
    plant = grid.pop(pos)
    # Part 1
    dq, region, edges = deque([pos]), {pos}, {d: set() for d in dirs}
    while dq:
        pos = dq.popleft()
        for d in dirs:
            next_pos = pos + d
            if next_pos in grid and grid[next_pos] == plant:
                dq.append(next_pos)
                region.add(next_pos)
                grid.pop(next_pos)
            elif next_pos not in region:
                edges[d].add(next_pos)
    p1 += len(region) * sum([len(x) for x in edges.values()])
    # Part 2
    sides = 0
    for d, vals in edges.items():
        while vals:
            edge = vals.pop()
            sides += 1
            dq = deque([edge])
            while dq:
                pos = dq.popleft()
                for next_pos in (pos + d*1j, pos - d*1j):
                    if next_pos in vals:
                        dq.append(next_pos)
                        vals.remove(next_pos)
    p2 += len(region) * sides

print(p1)
print(p2)