import re
import numpy as np

fabric, claims = np.zeros((1000, 1000)), {}
for line in open('d03.txt').read().splitlines():
    cid, x, y, w, l = [int(x) for x in re.findall(r'(\d+)', line)]
    fabric[x:x+w,y:y+l] += 1
    claims[cid] = [x, y, w, l]

# P1
print(len(fabric[fabric > 1]))

# P2
for cid, [x, y, w, l] in claims.items():
   if np.all(fabric[x:x+w,y:y+l] == 1):
       print(cid)
       break