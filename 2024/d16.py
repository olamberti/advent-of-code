from heapq import heappop, heappush

grid = {(x, y): c for y, row in enumerate(open('d16.txt'))
                  for x, c in enumerate(row.strip())}
start, = [pos for pos in grid if grid[pos] == 'S']
goal, = [pos for pos in grid if grid[pos] == 'E']

def next_steps(score, pos, d, path):
    res = []
    for dx, dy, cost in ((d[0], d[1], 1), (d[1], -d[0], 1001), (-d[1], d[0], 1001)):
        n_pos = (pos[0] + dx, pos[1] + dy)
        if grid[n_pos] == '#': continue
        res.append((score + cost, n_pos, (dx, dy), path | {n_pos}))
    return res

stack, cache = [(0, start, (1, 0), {start})], {}
best_score, best_path = float('inf'), set()

while stack:
    score, pos, d, path = heappop(stack)
    if score > best_score: break
    if (pos, d) in cache and cache[(pos, d)] < score: continue
    cache[pos, d] = score
    if pos == goal:
        best_score = score
        best_path.update(path)
    for n_score, n_pos, n_d, n_path in next_steps(score, pos, d, path):
        for c_score, c_pos, c_d, c_path in stack:
            if (c_score, c_pos, c_d) == (n_score, n_pos, n_d):
                c_path.update(n_path)
                break
            elif n_score > c_score:
                heappush(stack, (n_score, n_pos, n_d, n_path))
                break
        else: heappush(stack, (n_score, n_pos, n_d, n_path))
        
print(best_score)
print(len(best_path))