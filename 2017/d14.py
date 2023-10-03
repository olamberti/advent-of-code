inp, size = open('d14.txt').read(), 128

# Knothash functions from day 10
def round(c, i, ss, ls):
    for l in ls:
        if i + l <= len(c):
            c[i:i+l] = c[i:i+l][::-1]
        else:
            r = len(c[i:])
            cut = (c[i:] + c[:(i+l)-len(c)])[::-1]
            c[i:], c[:(i+l)-len(c)] = cut[:r], cut[r:]
        i = (i + l + ss) % len(c)
        ss += 1
    return c, i, ss

def knothash(s):
    # Do rounds
    c, lengths, i, ss = [i for i in range(256)], [ord(x) for x in s] + [17, 31, 73, 47, 23], 0, 0
    for _ in range(64):
        c, i, ss = round(c, i, ss, lengths)
    # Sparse hash
    dh = []
    for i in range(16):
        t = c[16 * i]
        for j in range(15): t = t ^ c[16 * i + j + 1]
        dh.append(t)
    # Convert to hexa
    res = ''
    for x in dh: res += hex(x)[2:].zfill(2)
    return res

# P1
data = set()
for i in range(size):
    bh = bin(int(knothash(inp + '-' + str(i)), 16))[2:].zfill(size)
    for j in range(size):
        if bh[j] == '1': data.add(i + j*1j)
print(len(data))

# P2
p2, grouped = 0, set()
for e in data:
    if e in grouped: continue
    p2 += 1; grouped.add(e); front = set()
    front.add(e)
    while front:
        new_front = set()
        for t in front:
            for d in [1, -1, 1j, -1j]:
                nt = t + d
                if nt in grouped or nt not in data: continue
                new_front.add(nt); grouped.add(nt)
        front = new_front
print(p2)