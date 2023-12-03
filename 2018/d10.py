import re
import numpy as np

posis, velos = [], []
for line in open('d10.txt').read().splitlines():
    nums = [int(x) for x in re.findall(r'(-?\d+)', line)]
    posis.append([nums[0], nums[1]])
    velos.append([nums[2], nums[3]])
posis, velos = np.array(posis), np.array(velos)

def grid_size(posis, display=False):
    mx, my = min(posis[:,0]), min(posis[:,1])
    Mx, My = max(posis[:,0]), max(posis[:,1])
    posis = posis.tolist()
    if display:
        for y in range(my, My + 1):
            line = ''
            for x in range(mx, Mx + 1):
                if [x, y] in posis: line = line + '█'
                else: line = line + '.'
            print(line)
    return Mx - mx, My - my
        
def move(posis, velos, dt=1):
    posis[:,0] += velos[:,0] * dt
    posis[:,1] += velos[:,1] * dt
    return posis

time, mw, mh = 0, 1e20, 1e20
while True:
    time += 1
    posis = move(posis, velos)
    w, h = grid_size(posis)
    mw, mh = min(w, mw), min(h, mh)
    if w > mw and h > mh: break

posis = move(posis, velos, -1)
grid_size(posis, True)
print(time - 1)