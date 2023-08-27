# Read input
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
space, bugs = set(), set()
for y, line in enumerate(open('24.txt').readlines()):
    for x, e in enumerate(line.strip()):
        if e =='#': bugs.add((x, y))
        else: space.add((x, y))

# Functions
def printmap(bugs):
    grid = ''
    for y in range(5):
        for x in range(5):
            if (x, y) in bugs: grid += '#'
            else: grid += '.'
        grid += '\n'
    print(grid)

def bio(bugs):
    res = 0
    for bug in bugs:
        x, y = bug
        res += pow(2, x + 5 * y)
    return res

def do_round(bugs, space):
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
    bugs, space = do_round(bugs, space)
    val = bio(bugs)
    if val not in cache: cache.add(val)
    else:
        print(val)
        break

# P2
# to be completed...