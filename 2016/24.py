import heapq
# Read input
walls, points, dirs = set(), {}, [1, -1, 1j, -1j]
for y, line in enumerate(open('24.txt').read().splitlines()):
    for x, c in enumerate(line):
        if c == '#': walls.add(x + y*1j)
        elif c == '0': start = x + y*1j
        if c.isnumeric(): points[x + y*1j] = int(c)

# Get distances of points of interest
dists = {}
for start, poi in points.items():
    dists[poi], steps = {}, 0
    front, seen = set(), set()
    front.add(start); seen.add(start)
    while front:
        nfront = set(); steps += 1
        for p in front:
            for d in dirs:
                np = p + d
                if np in walls or np in seen: continue
                if np in points: dists[poi][points[np]] = steps
                nfront.add(np); seen.add(np)
        front = nfront

# Priority search for shortest path
start, p1, p2 = (0, 0, [0]), 999999999, 999999999
stack = [start]
heapq.heapify(stack)
while stack:
    steps, pos, visited = heapq.heappop(stack)
    for npos, d in dists[pos].items():
        if npos in visited: continue
        nvis, nsteps = visited + [npos], steps + d
        if len(nvis) == len(points):
            p1 = min(nsteps, p1)
            p2 = min(nsteps + dists[npos][0], p2)
        heapq.heappush(stack, (nsteps, npos, nvis))
print(p1)
print(p2)