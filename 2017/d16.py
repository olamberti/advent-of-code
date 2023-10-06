import numpy as np

moves = open('d16.txt').read().split(',')

# P1
def dance(s):
    progs = list(s)
    for move in moves:
        if move[0] == 's':
            x = int(move[1:])
            progs = progs[-x:] + progs[:-x]
        else:
            pars = move[1:].split('/')
            if move[0] == 'x':
                p1, p2 = [int(x) for x in pars]
                progs[p1], progs[p2] = progs[p2], progs[p1]
            elif move[0] == 'p':
                p1, p2 = [progs.index(x) for x in pars]
                progs[p1], progs[p2] = progs[p2], progs[p1]
    return ''.join(progs)

print(dance('abcdefghijklmnop'))

# P2