grid = {x + y *1j: c for y, row in enumerate(open('d20.txt'))
                     for x, c in enumerate(row.strip())}
start, = [pos for pos, c in grid.items() if c == 'S']
goal,  = [pos for pos, c in grid.items() if c == 'E']

pos, dist = start, {start: 0}
while pos != goal:
    for d in [1, -1, 1j, -1j]:
        next_pos = pos + d
        if grid[next_pos] in '.E' and next_pos not in dist:
            dist[next_pos] = dist[pos] + 1
            pos = next_pos

path, p1, p2, T = list(dist.keys()), 0, 0, 100
for d1, a in enumerate(path):
    for b in path[d1 + 3:]:
        d = int(abs(a.real - b.real) + abs(a.imag - b.imag))
        gain = dist[b] - dist[a] - d
        if d <= 2 and gain >= T: p1 += 1
        if d <= 20 and gain >= T: p2 += 1

print(p1)
print(p2)
# Slow but works, might improve it later...