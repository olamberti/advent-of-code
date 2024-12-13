from collections import deque

grid = {x + y *1j: c for y, row in enumerate(open('d12.txt'))
                     for x, c in enumerate(row.strip())}
dirs, p1, p2 = [1, -1, 1j, -1j], 0, 0

while grid:
    pos = next(iter(grid.keys()))
    plant = grid.pop(pos)
    # Part 1
    dq, region, edges = deque([pos]), {pos}, set()
    while dq:
        pos = dq.popleft()
        for d in dirs:
            next_pos = pos + d
            if next_pos in grid and grid[next_pos] == plant:
                dq.append(next_pos), 
                region.add(next_pos)
                grid.pop(next_pos)
    edges = {(pos, d) for d in dirs for pos in region if pos + d not in region}
    p1 += len(region) * len(edges)
    # Part 2
    sides = len(edges - {(pos - d*1j, d) for pos, d in edges})
    p2 += len(region) * sides

print(p1)
print(p2)