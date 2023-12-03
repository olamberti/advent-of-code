import numpy as np

GSN = int(open('d11.txt').read())
N = 300

def power(x, y):
    rid = x + 10
    plvl = str(((rid * y) + GSN) * rid)
    if len(plvl) < 3: return 0
    else: return int(plvl[-3]) - 5

grid = np.zeros((N, N), dtype=np.int8)
for x in range(N):
    for y in range(N):
        grid[x, y] = power(x + 1, y + 1)

def get_max(size):
    steps, max_pow = N + 1 - size, -9999
    kernel = np.ones((size,size), dtype=np.int8)
    for x in range(steps):
        for y in range(steps):
            pow = np.sum(np.multiply(grid[x:x+size,y:y+size], kernel))
            if pow > max_pow:
                max_pow, max_pos = pow, str(x + 1) + ',' + str(y + 1)
    return max_pow, max_pos

max_pow = 0
for s in range(1, N + 1):
    pow, pos = get_max(s)
    if pow > max_pow:
        max_pow = pow
        p2 = pos + ',' + str(s)
    if s == 3: print(pos)
    if pow < 0: break

print(p2)