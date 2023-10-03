import numpy as np

lights_1 = np.zeros((1000, 1000), dtype=bool)
lights_2 = np.zeros((1000, 1000), dtype=int)
for line in open('d06.txt').readlines():
    line = line.strip().split(' ')
    i = line.index('through')
    x1, y1 = [int(i) for i in line[i - 1].split(',')]
    x2, y2 = [int(i) for i in line[i + 1].split(',')]
    if line[0] == 'toggle':
        lights_1[x1 : x2 + 1, y1 : y2 + 1] = np.invert(lights_1[x1 : x2 + 1, y1 : y2 + 1])
        lights_2[x1 : x2 + 1, y1 : y2 + 1] += 2
    elif line[1] == 'on':
        lights_1[x1 : x2 + 1, y1 : y2 + 1] = True
        lights_2[x1 : x2 + 1, y1 : y2 + 1] += 1
    elif line[1] == 'off':
        lights_1[x1 : x2 + 1, y1 : y2 + 1] = False
        lights_2[x1 : x2 + 1, y1 : y2 + 1] -= 1
        lights_2[np.where(lights_2 < 0)] = 0
print(lights_1.sum())
print(lights_2.sum())