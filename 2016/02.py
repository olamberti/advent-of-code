import numpy as np
moves = {'U':-1,'D':1,'L':-1,'R':1}

# P1
keypad = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
r, c, code = 1, 1, ''
for line in open('02.txt').read().splitlines():
    line = line.strip()
    for m in line:
        if m == 'L' or m == 'R':
            c += moves[m]
            if c < 0: c = 0
            elif c > 2: c = 2
        elif m == 'U' or m == 'D':
            r += moves[m]
            if r < 0: r = 0
            elif r > 2: r = 2
    code += str(keypad[r][c])
print(code)

# P2
keypad = np.array([[0, 0, 1, 0, 0],
                   [0, 2, 3, 4, 0],
                   [5, 6, 7, 8, 9],
                   [0,10,11,12, 0],
                   [0, 0,13, 0, 0]])
r, c, code, hex = 1, 1, '', {10:'A',11:'B',12:'C',13:'D'}
for line in open('02.txt').read().splitlines():
    line = line.strip()
    for m in line:
        if m == 'L' or m == 'R':
            c += moves[m]
            if c < 0: c = 0
            elif c > 4: c = 4
            elif keypad[r][c] == 0: c -= moves[m]
        elif m == 'U' or m == 'D': 
            r += moves[m]
            if r < 0: r = 0
            elif r > 4: r = 4
            elif keypad[r][c] == 0: r -= moves[m]
    if keypad[r][c] < 10: code += str(keypad[r][c])
    else: code += hex[keypad[r][c]]
print(code)