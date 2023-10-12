import numpy as np

def g2h(grid):
    rows = [''.join(row) for row in grid.astype('str')]
    return '/'.join(rows)

def h2g(hashgrid):
    grid = [[int(c) for c in row] for row in hashgrid.split('/')]
    return np.array(grid)

# P1
convert = {}
for line in open('d21.txt').read().splitlines():
    hs = [x.replace('.','0').replace('#', '1') for x in line.split(' => ')]
    g = h2g(hs[0])
    for _ in range(4):
        h1 = g2h(g); h2 = g2h(np.flip(g, 1))
        if h1 not in convert: convert[h1] = hs[1]
        if h2 not in convert: convert[h2] = hs[1]
        g = np.rot90(g)

start = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [1, 1, 1]])

# TODO: code iterations