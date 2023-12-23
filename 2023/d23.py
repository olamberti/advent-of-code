from collections import deque as dq

# Load input
grid = [line.strip() for line in open('d23.txt')]
slopes = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
height, width = len(grid), len(grid[0])
start, goal = (1, 0), (width - 2, height - 1)

# Build up graph by considering slopes
graph, todo = {}, dq([(1, 0)])
while todo:
    pos = todo.popleft()
    graph[pos], front, seen, steps = {}, {pos}, {pos}, 0
    while front:
        steps += 1
        new_front = set()
        for x, y in front:
            for dx, dy in slopes.values():
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= width or ny < 0 or ny >= height: continue
                if grid[ny][nx] == '#' or (nx, ny) in seen: continue
                if grid[ny][nx] in slopes.keys():
                    if (dx, dy) != slopes[grid[ny][nx]]: continue
                    if steps != 1:
                        graph[pos][(nx + dx, ny + dy)] = steps + 1
                        todo.append((nx + dx, ny + dy))
                        continue
                elif (nx, ny) == goal:
                    graph[pos][(nx, ny)] = steps
                    continue
                new_front.add((nx, ny))
                seen.add((nx, ny))
        front = new_front

# DFS to find longest path recursively
cache = set()
def dfs(pos):
    if pos == goal: return 0
    steps = -float('inf')
    cache.add(pos)
    for npos, nsteps in graph[pos].items():
        if npos not in cache:
            steps = max(steps, dfs(npos) + nsteps)
    cache.remove(pos)
    return steps

# Part 1 - Find longest path on graph
print(dfs(start))

# Part 2 - Modify graph to exclude slopes and find longest path
for pos, options in graph.items():
    for next_pos, steps in options.items():
        if next_pos in graph and pos not in graph[next_pos]:
            graph[next_pos][pos] = steps       
print(dfs(start))