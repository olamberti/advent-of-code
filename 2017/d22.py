def read_inp():
    inf = set()
    for x, line in enumerate(open('d22.txt').read().splitlines()):
        for y, c in enumerate(line):
            if c == '#': inf.add(x + y * 1j)
    pos = x //2 + y //2 * 1j
    return inf, pos

# P1
inf, pos = read_inp()
d, ans = -1, 0

for _ in range(10_000):
    if pos in inf:
        d *= -1j
        inf.remove(pos)
    else:
        d *= 1j
        inf.add(pos)
        ans += 1
    pos += d
print(ans)

# P2:
inf, pos = read_inp()
weak, flag = set(), set()
d, ans = -1, 0

for _ in range(10_000_000):
    if pos in inf:
        d *= -1j
        inf.remove(pos); flag.add(pos)
    elif pos in weak:
        weak.remove(pos); inf.add(pos)
        ans += 1
    elif pos in flag:
        d *= -1
        flag.remove(pos)
    else:
        d *= 1j
        weak.add(pos)
    pos += d
print(ans)