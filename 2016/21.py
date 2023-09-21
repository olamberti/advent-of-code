inst = open('21.txt').read().splitlines()

def swappos(s, x, y):
    s[x], s[y] = s[y], s[x]
    return s

def swaplet(s, a, b):
    ia, ib = s.index(a), s.index(b)
    s[ia], s[ib] = s[ib], s[ia]
    return s

def rot(s, x):
    return s[x:] + s[:x]

def rotpos(s, a):
    ia = s.index(a)
    s = rot(s, -1)
    s = rot(s, -ia)
    if ia >= 4: s = rot(s, -1)
    return s

def rev(s, x, y):
    p = s[x:y+1]
    return s[:x] + p[::-1] + s[y+1:]

def move(s, x, y):
    p = s.pop(x)
    s.insert(y, p)
    return s

# P1
pw1 = [c for c in 'abcdefgh']
for line in inst:
    line = line.split()
    if line[0] == 'move': pw1 = move(pw1, int(line[2]), int(line[5]))
    elif line[0] == 'reverse': pw1 = rev(pw1, int(line[2]), int(line[4]))
    elif line[0] == 'swap':
        if line[1] == 'position': pw1 = swappos(pw1, int(line[2]), int(line[5]))
        if line[1] == 'letter': pw1 = swaplet(pw1, line[2], line[5])
    elif line[0] == 'rotate':
        if line[1] == 'left': pw1 = rot(pw1, int(line[2]))
        elif line[1] == 'right': pw1 = rot(pw1, -int(line[2]))
        elif line[1] == 'based': pw1 = rotpos(pw1, line[-1])
print(''.join(pw1))

# P2:
pw2 = [c for c in 'fbgdceah']
# TODO: reverse engineer functions and go backwards