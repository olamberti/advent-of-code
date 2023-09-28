from copy import deepcopy as dp

# P1
inp = open('10.txt').read()
c, lengths = [i for i in range(256)], [int(x) for x in inp.split(',')]

def round(c, i, ss, ls):
    for l in ls:
        if i + l <= len(c):
            c[i:i+l] = c[i:i+l][::-1]
        else:
            l1 = len(c[i:])
            cut = (c[i:] + c[:(i+l)-len(c)])[::-1]
            c[i:], c[:(i+l)-len(c)] = cut[:l1], cut[l1:]
        i = (i + l + ss) % len(c)
        ss += 1
    return c, i, ss

c, _, _ = round(c, 0, 0, lengths)
print(c[0] * c[1])

# P2 - TODO: find and correct bug
def knothash(s):
    c, lengths, i, ss = [i for i in range(256)], [ord(x) for x in s] + [17, 31, 73, 47, 23], 0, 0
    for _ in range(64):
        c, i, ss = round(c, i, ss, lengths)

    dh = []
    for i in range(16):
        t = c[16 * i]
        for j in range(15): t = t ^ c[16 * i + j]
        dh.append(t)
    
    res = ''
    for x in dh:
        res += hex(x)[2:].zfill(2)
    return res

print(knothash('AoC 2015'))