import re
import numpy as np

data = []
for line in open('d15.txt').readlines():
    data.append(re.findall(r'-?\d+', line))
data = np.array(data, dtype='int32')
data = data.T

p1, p2 = 0, 0
for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            d = 100 - a - b - c
            amm = np.array([a, b, c, d], dtype='int32')
            props = np.dot(data, amm)
            if any([x < 0 for x in props[:-1]]): score = 0
            else: score = np.prod(props[:-1])
            p1 = max(p1, score)
            if props[-1] == 500: p2 = max(p2, score)
print(p1)
print(p2)