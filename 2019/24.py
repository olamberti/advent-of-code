# Read input
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
space, bugs = set(), set()
for y, line in enumerate(open('24.txt').readlines()):
    for x, e in enumerate(line.strip()):
        if e =='#': bugs.add((x, y))
        else: space.add((x, y))
bugs_0, space_0 = bugs, space

# Functions
def bio(bugs):
    res = 0
    for bug in bugs:
        x, y = bug
        res += pow(2, x + 5 * y)
    return res

def p1_round(bugs, space):
    nbugs, nspace = set(), set()
    for x, y in bugs:
        cell, n = (x, y), 0
        for dx, dy in dirs:
            if (x + dx, y + dy) in bugs: n += 1
        if n == 1: nbugs.add(cell)
        else: nspace.add(cell)
    for x, y in space:
        cell, n = (x, y), 0
        for dx, dy in dirs:
            if (x + dx, y + dy) in bugs: n += 1
        if n == 1 or n == 2: nbugs.add(cell)
        else: nspace.add(cell)
    return nbugs, nspace

# P1
cache = set()
cache.add(bio(bugs))
while True:
    bugs, space = p1_round(bugs, space)
    val = bio(bugs)
    if val not in cache: cache.add(val)
    else:
        print(val)
        break

# P2
def add_lvl(space, n):
    nspace = space
    for x in range(5):
        for y in range(5):
            if x == 2 and y == 2: continue
            nspace.add((n, x, y))
    return nspace

def get_adj(cell):
    adjs = set()
    lvl, x, y = cell
    # 0 Adjacent on the same level
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if (0 <= nx < 5) and (0 <= ny < 5) and not(nx == 2 and ny == 2):
            adjs.add((lvl, nx, ny))
    # -1 Outer edge cells
    if x == 0: adjs.add((lvl - 1, 1, 2))
    if x == 4: adjs.add((lvl - 1, 3, 2))
    if y == 0: adjs.add((lvl - 1, 2, 1))
    if y == 4: adjs.add((lvl - 1, 2, 3))
    # +1 Inner edge cells
    if (x, y) == (2, 1):
        for i in range(5): adjs.add((lvl + 1, i, 0))
    if (x, y) == (1, 2):
        for i in range(5): adjs.add((lvl + 1, 0, i))
    if (x, y) == (3, 2):
        for i in range(5): adjs.add((lvl + 1, 4, i))
    if (x, y) == (2, 3):
        for i in range(5): adjs.add((lvl + 1, i, 4))
    return adjs

def p2_round(bugs, space):
    nbugs, nspace = set(), set()
    for cell in bugs:
        n = 0
        for ncell in get_adj(cell):
            if ncell in bugs: n += 1
        if n == 1: nbugs.add(cell)
        else: nspace.add(cell)
    for cell in space:
        n = 0
        for ncell in get_adj(cell):
            if ncell in bugs: n += 1
        if n == 1 or n == 2: nbugs.add(cell)
        else: nspace.add(cell)
    return nbugs, nspace

bugs, space = set(), set()
for x, y in bugs_0:
    if x == 2 and y == 2: continue
    bugs.add((0, x, y))
for x, y in space_0:
    if x == 2 and y == 2: continue
    space.add((0, x, y))
for i in [-1, 1]: space = add_lvl(space, i)
mlvl, Mlvl = -1, 1

for _ in range(200):
    bugs, space = p2_round(bugs, space)
    for lvl, x, y in bugs:
        if lvl == mlvl:
            mlvl -= 1
            space = add_lvl(space, mlvl)
        if lvl == Mlvl:
            Mlvl += 1
            space = add_lvl(space, Mlvl)

print(len(bugs))