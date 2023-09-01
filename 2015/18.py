import numpy as np
from scipy.ndimage import convolve
from copy import deepcopy as dp

# Read input
lights = np.zeros((100,100), dtype=np.uint8)
for x, line in enumerate(open('18.txt').readlines()):
    for y, c in enumerate(line.strip()):
        if c == '#': lights[x, y] = 1
lights_0 = dp(lights)

# Convolution for next state
kernel = np.ones((3,3), dtype=np.uint8)
kernel[1,1] = 0

def anim(grid):
    conv = convolve(grid, kernel, mode='constant', cval= 0)
    return (((grid == 1) & ((conv == 2) | (conv == 3))) | ((grid == 0) & (conv == 3))).astype(np.uint8)

# P1
for _ in range(100):
    lights = anim(lights)
print(np.sum(lights))

# P2
def set_corners(grid):
    new_lights, (mx, my) = dp(grid), grid.shape
    for x, y in [[0, 0], [0, my-1], [mx-1, 0], [mx-1,my-1]]:
        new_lights[x, y] = 1
    return new_lights

lights = dp(lights_0)
lights = set_corners(lights)
for _ in range(100):
    lights = anim(lights)
    lights = set_corners(lights)
print(np.sum(lights))