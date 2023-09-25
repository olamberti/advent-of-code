inp = int(open('03.txt').read())

# P1
def p1(inp):
    sq, p = 1, 0
    while sq ** 2  < inp:
        sq += 2; p += 1 + 1j
    n = sq ** 2

    for d in [-1, -1j, 1, 1j]:
        for _ in range(1, sq):
            if n == inp:
                return int(abs(p.real) + abs(p.imag))
            n -= 1; p += d
print(p1(inp))

# P2
def nsum(pos, vals):
    res = 0
    for d in [1, 1-1j, -1j, -1-1j, -1, -1+1j, 1j, 1+1j]:
        np = pos + d
        if np in vals: res += vals[np]
    return res

def p2(inp):
    pos, vals, i, steps = 0, {}, 0, 0
    vals[pos] = 1
    while True:
        for d in [1, -1j, -1, 1j]:
            if i % 2 == 0: steps += 1
            for _ in range(steps):
                pos = pos + d
                vals[pos] = nsum(pos, vals)
                if vals[pos] > inp:
                    return vals[pos]
            i += 1
print(p2(inp))