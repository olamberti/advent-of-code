# Read input:
walls, paths, gates, letters = set(), set(), {}, {}
dirs = [1, 1j, -1, -1j]
for y, line in enumerate(open('20.txt').readlines()):
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

def printmap(visits, level = None):
    for y in range(L):
        line = ''
        for x in range(W):
            pos = x + y * 1j
            if pos in walls: line += '#'
            elif pos in visits or (pos, level) in visits:
                line += '█'
            elif pos in paths: line += '.'
            elif pos in letters: line += letters[pos]
            else: line += ' '
        print(line)
    

# Create start, finish and portals:
portals = {}
for pos, gate in gates.items():
    if gate == 'AA': start = pos
    elif gate == 'ZZ': finish = pos
    else:
        for npos, ngate in gates.items():
            if pos == npos: continue
            elif gate == ngate:
                portals[pos] = npos
                portals[npos] = pos

# P1: Look for shortest path with BFS:
steps, front, visited = 0, set(), set()
front.add(start)
while finish not in front:
    steps += 1
    nfront = set()
    for pos in front:
        visited.add(pos)
        if pos in portals.keys(): nfront.add(portals[pos])
        for d in dirs:
            npos = pos + d
            if npos in walls: continue
            elif npos in paths: nfront.add(npos)
    front = nfront
print(steps)
# printmap(visited)

# P2: Look for shortest path with BFS including levels as third dimension:
# ... will rewrite this with a mapping and graph search, since it runs too long ...
start, finish = (start, 0), (finish, 0)
steps, front, visited = 0, set(), set()
front.add(start)

while finish not in front:
    steps += 1
    nfront = set()
    for pos, lvl in front:
        visited.add((pos, lvl))
        if pos in portals.keys():
            x, y = int(pos.real), int(pos.imag)
            if ((x == 2) or (x == W - 2) or (y == 2) or (y == L - 2)):
                if lvl > 0: nfront.add((portals[pos], lvl - 1))
            else: nfront.add((portals[pos], lvl + 1))
        for d in dirs:
            npos = pos + d
            if npos in walls: continue
            elif npos in paths: nfront.add((npos, lvl))
    front = nfront
    # printmap(visited, int(input('lvl')))
print(steps)