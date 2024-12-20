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

def md(a, b):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))

path, c1, c2, T = list(dist.keys()), 0, 0, 100
for d1, p1 in enumerate(path):
    for p2 in path[d1 + 3:]:
        d = md(p1, p2)
        gain = dist[p2] - dist[p1] - d
        if d <= 2 and gain >= T: c1 += 1
        if d <= 20 and gain >= T: c2 += 1

print(c1)
print(c2)
# Slow but works, might improve it later...