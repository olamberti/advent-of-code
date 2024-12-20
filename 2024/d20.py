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

def get_within_dist(pos, distance):
    front, seen, steps = {pos}, {pos: 0}, 0
    while steps < distance:
        steps += 1
        new_front = set()
        for pos in front:
            for d in [1, -1, 1j, -1j]:
                next_pos = pos + d
                if next_pos not in seen:
                    seen[next_pos] = steps
                    new_front.add(next_pos)
        front = new_front
    return {x: d for x, d in seen.items() if x in dist and d > 1}

p1, p2 = 0, 0
for a in dist:
    for b, d in get_within_dist(a, 20).items():
        if dist[b] - dist[a] - d < 100: continue
        if d <= 2: p1 += 1
        p2 += 1

print(p1)
print(p2)
# Still slow but works, might improve it further later...