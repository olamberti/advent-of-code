inp = int(open('03.txt').read())

# P1
sq, p = 1, 0
while sq ** 2  < inp:
    sq += 2; p += 1 + 1j
n = sq ** 2

for d in [-1, -1j, 1, 1j]:
    for _ in range(1, sq):
        if n == inp:
            print(int(abs(p.real) + abs(p.imag)))
        n -= 1; p += d

# P2
def nsum(pos, vals):
    res = 0
    for d in [1, 1-1j, -1j, -1-1j, -1, -1+1j, 1j, 1+1j]:
        np = pos + d
        if np in vals: res += vals[np]
    return res

pos, vals, i, steps, p2 = 0, {}, 0, 0, True
vals[pos] = 1
while p2:
    for d in [1, -1j, -1, 1j]:
        if i % 2 == 0: steps += 1
        for _ in range(steps):
            pos = pos + d
            vals[pos] = nsum(pos, vals)
            if vals[pos] > inp and p2:
                p2 = False
                print(vals[pos])
        i += 1