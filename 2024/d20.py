grid = {x + y *1j: c for y, row in enumerate(open('d20.txt'))
                     for x, c in enumerate(row.strip())}
start, = [pos for pos, c in grid.items() if c == 'S']
goal,  = [pos for pos, c in grid.items() if c == 'E']

pos, path = start, {start: 0}
while pos != goal:
    for d in [1, -1, 1j, -1j]:
        next_pos = pos + d
        if grid[next_pos] in '.E' and next_pos not in path:
            path[next_pos] = path[pos] + 1
            pos = next_pos

def dist(a, b):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))

def count_best_cheats(time):
    cheats = {}
    for p1, d1 in path.items():
        for p2, d2 in path.items():
            if p1 == p2 or d2 - d1 <= 2: continue
            if dist(p1, p2) <= time:
                cheats[(p1, p2)] = d2 - d1 - dist(p1, p2)
    ans, T = 0, 100
    for x in cheats.values():
        if x >= T: ans += 1
    return ans

print(count_best_cheats(2))
print(count_best_cheats(20))
# Slow but works, might improve it later...