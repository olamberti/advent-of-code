import numpy as np
from scipy.ndimage import convolve

grid = np.array([[*line.strip()]for line in open('d04.txt')]) == '@'    # read grid
grid = grid.astype(np.uint8)                                            # convert to uint8         
kernel = np.array([[1, 1, 1],[1, 0, 1],[1, 1, 1]], dtype=np.uint8)      # neighbor kernel

def removable(grid):                                                    # removable rolls function              
    count = convolve(grid, kernel, mode='constant', cval= 0)            # neighbor count
    return grid & (count < 4)                                           # rolls with < 4 neighbors    

n, i = 0, 0                                                             # counter and iterator
while True:                                                             # main loop            
    gone = removable(grid)                                              # removable rolls         
    if np.sum(gone) == 0:                                               # if none removed                      
        print(n)                                                        # part2 result
        break                                                           # exit loop
    i, n = i + 1, n + np.sum(gone)                                      # update counter and iterator               
    if i == 1: print(n)                                                 # part1 result
    grid -= gone                                                        # update grid                 