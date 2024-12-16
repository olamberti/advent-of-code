import heapq

grid = {(x, y): c for y, row in enumerate(open('d16.txt'))
                  for x, c in enumerate(row.strip())}
start, = [pos for pos in grid if grid[pos] == 'S']
goal, = [pos for pos in grid if grid[pos] == 'E']

def next_steps(score, pos, d):
    res = []
    for dx, dy in ((d[0], d[1]), (d[1], -d[0]), (-d[1], d[0])):
        if (dx, dy) == d: new_score = score + 1
        else: new_score = score + 1001
        n_pos = (pos[0] + dx, pos[1] + dy)
        if grid[n_pos] == '#': continue
        else: res.append((new_score, n_pos, (dx, dy)))
    return res

stack, cache = [(0, (start, (1, 0), {start}))], {}
best_score, best_path = float('inf'), set()
heapq.heapify(stack)

while stack:
    score, (pos, d, path) = heapq.heappop(stack)
    if score > best_score: break
    if (pos, d) in cache and cache[(pos, d)] < score: continue
    cache[pos, d] = score
    if pos == goal:
        best_score = score
        best_path.update(path)
    for n_score, n_pos, n_d in next_steps(score, pos, d):
        n_path = path.copy()
        n_path.add(n_pos)
        for i, (c_score, (c_pos, c_d, c_path)) in enumerate(stack):
            if n_score > c_score:
                heapq.heappush(stack, (n_score, (n_pos, n_d, n_path)))
                break
            if n_score == c_score and n_pos == c_pos and n_d == c_d:
                c_path.update(n_path)
                stack[i] = (c_score, (c_pos, c_d, c_path))
                break
        else:
            heapq.heappush(stack, (n_score, (n_pos, n_d, n_path)))
        
print(best_score)
print(len(best_path))