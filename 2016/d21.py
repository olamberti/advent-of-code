from copy import deepcopy as dp
inst = open('d21.txt').read().splitlines()

def swappos(s, x, y):
    s[x], s[y] = s[y], s[x]
    return s

def swaplet(s, a, b):
    ia, ib = s.index(a), s.index(b)
    s[ia], s[ib] = s[ib], s[ia]
    return s

def rot(s, x, r = False):
    if r: x *= -1
    return s[x:] + s[:x]

def rotpos(s, a, r = False):
    if r:
        ori = dp(s)
        while rotpos(dp(s), a) != ori:
            s = rot(s, 1)
        return s
    ia = s.index(a)
    s = rot(s, -1)
    s = rot(s, -ia)
    if ia >= 4: s = rot(s, -1)
    return s

def rev(s, x, y):
    p = s[x:y+1]
    return s[:x] + p[::-1] + s[y+1:]

def move(s, x, y, r = False):
    if r: x, y = y, x
    p = s.pop(x)
    s.insert(y, p)
    return s

def scramble(pw, inst, r = False):
    pw = [c for c in pw]
    for line in inst:
        line = line.split()
        if line[0] == 'move': pw = move(pw, int(line[2]), int(line[5]), r)
        elif line[0] == 'reverse': pw = rev(pw, int(line[2]), int(line[4]))
        elif line[0] == 'swap':
            if line[1] == 'position': pw = swappos(pw, int(line[2]), int(line[5]))
            if line[1] == 'letter': pw = swaplet(pw, line[2], line[5])
        elif line[0] == 'rotate':
            if line[1] == 'left': pw = rot(pw, int(line[2]), r)
            elif line[1] == 'right': pw = rot(pw, -int(line[2]), r)
            elif line[1] == 'based': pw = rotpos(pw, line[-1], r)
    return (''.join(pw))

# P1
p1 = 'abcdefgh'
print(scramble(p1, inst))

# P2:
p2 = 'fbgdceah'
print(scramble(p2, inst[::-1], True))