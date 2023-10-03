import heapq

# Read input
walls, paths, gates, letters = set(), set(), {}, {}
dirs = [1, 1j, -1, -1j]

for y, line in enumerate(open('d20.txt').readlines()):
    for x, c in enumerate(line):
        pos = x + y*1j
        if c == '#': walls.add(pos)
        elif c == '.': paths.add(pos)
        elif c.isalpha():
            first = True
            for d in dirs:
                if pos + d in letters:
                    first, gate = False, letters[pos + d] + c
                    if pos + 2 * d in paths: gates[pos + 2 * d] = gate
                    else: gates[pos - d] = gate
                    del letters[pos + d]
            if first: letters[x + y*1j] = c

W, L = x, y
for pos, gate in gates.items():
    if gate == 'AA': start = pos

# Create portal-to-portal map with distance costs (o = outer, i = inner)
def get_portals(start):
    out, front, visited, dist = {}, set(), set(), 0
    front.add(start)
    while front:
        dist += 1
        nfront = set()
        for pos in front:
            visited.add(pos)
            for d in dirs:
                npos = pos + d
                if (npos in walls) or (npos in visited): continue
                elif npos in gates:
                    x, y = int(npos.real), int(npos.imag)
                    if gates[npos] == 'AA': continue
                    elif gates[npos] == 'ZZ': out[gates[npos]] = dist
                    elif ((x == 2) or (x == W - 2) or (y == 2) or (y == L - 2)):
                          out[gates[npos] + '-i'] = dist + 1
                    else: out[gates[npos] + '-o'] = dist + 1
                elif npos in paths: nfront.add(npos)
        front = nfront
    return out

p2p = {}
for pos, gate in gates.items():
    if gate == 'AA' or gate == 'ZZ':
        p2p[gate] = get_portals(pos)
        continue
    x, y = int(pos.real), int(pos.imag)
    if ((x == 2) or (x == W - 2) or (y == 2) or (y == L - 2)):
          p2p[gate + '-o'] = get_portals(pos)
    else: p2p[gate + '-i'] = get_portals(pos)

# P1
stack = [(0, 'AA')]
heapq.heapify(stack)
while True:
    dist, pos = heapq.heappop(stack)
    if pos == 'ZZ':
        print(dist)
        break
    for npos, ndist in p2p[pos].items():
        heapq.heappush(stack, (dist + ndist, npos))

# P2
stack = [(0, 'AA', 0)]
heapq.heapify(stack)
while True:
    dist, pos, lvl = heapq.heappop(stack)
    if pos == 'ZZ':
        print(dist)
        break
    for npos, ndist in p2p[pos].items():
        if lvl > 0 and npos == 'ZZ': continue
        elif lvl == 0 and npos == 'ZZ': heapq.heappush(stack, (dist + ndist, npos, lvl))
        elif lvl == 0 and npos[-1] == 'i': continue
        elif npos[-1] == 'i': heapq.heappush(stack, (dist + ndist, npos, lvl - 1))
        elif npos[-1] == 'o': heapq.heappush(stack, (dist + ndist, npos, lvl + 1))