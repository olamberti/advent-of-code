import heapq

grid = [[int(x) for x in line.strip()] for line in open('d17.txt')]
height, width = len(grid), len(grid[0])

def next_states(heatloss, pos, d, straight, part1):
    states = []
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if dx == -d[0] and dy == -d[1]: continue
        n_straight = straight + 1 if (dx, dy) == d else 1
        if part1:
            if n_straight > 3: continue
        else:
            if n_straight > 10: continue
            elif straight < 4 and (dx, dy) != d: continue
        nx, ny = pos[0] + dx, pos[1] + dy
        if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
        n_heatloss = heatloss + grid[ny][nx]
        states.append((n_heatloss, (nx, ny), (dx, dy), n_straight))
    return states

def solve(part1):
    s1, s2 = ((0,0), (1,0), 0), ((0,0), (0,1), 0)
    stack, seen = [(0, *s1), (0, *s2)], {s1, s2}
    heapq.heapify(stack)

    while stack:
        heatloss, pos, d, straight = heapq.heappop(stack)
        if pos == (width - 1, height - 1):
            if part1 or (not part1 and straight >= 4):
                return heatloss
        for n_heatloss, n_pos, n_d, n_straight in next_states(heatloss, pos, d, straight, part1):
            if (n_pos, n_d, n_straight) in seen: continue
            seen.add((n_pos, n_d, n_straight))
            heapq.heappush(stack, (n_heatloss, n_pos, n_d, n_straight))

print(solve(True))
print(solve(False))