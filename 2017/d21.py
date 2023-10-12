import numpy as np

def g2h(grid):
    rows = [''.join(row) for row in grid.astype('str')]
    return '/'.join(rows)

def h2g(hashgrid):
    grid = [[int(c) for c in row] for row in hashgrid.split('/')]
    return np.array(grid)

convert = {}
for line in open('d21.txt').read().splitlines():
    hs = [x.replace('.','0').replace('#', '1') for x in line.split(' => ')]
    g1, g2 = h2g(hs[0]), h2g(hs[1])
    for _ in range(4):
        h1 = g2h(g1); h2 = g2h(np.flip(g1, 1))
        if h1 not in convert: convert[h1] = g2
        if h2 not in convert: convert[h2] = g2
        g1 = np.rot90(g1)

def iterate(grid):
    size = grid.shape[0]
    c = 2 if size % 2 == 0 else 3
    res, n = None, size // c
    for i in range(n):
        row = None
        for j in range(n):
            cut = g2h(grid[i*c:(i*c)+c,j*c:(j*c)+c])
            if row is None: row = convert[cut]
            else: row = np.concatenate((row, convert[cut]), 1)
        if res is None: res = row
        else: res = np.vstack((res, row))
    return res
    
img = np.array([[0, 1, 0],
                [0, 0, 1],
                [1, 1, 1]])

for i in range(18):
    img = iterate(img)
    if i + 1 == 5: print(np.sum(img))

print(np.sum(img))