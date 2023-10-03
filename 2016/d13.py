fn = int(open('13.txt').read())
dirs = [1, -1, 1j, -1j]

def isopen(z):
    x, y = int(z.real), int(z.imag)
    n = bin(x * x + 3 * x + 2 * x * y + y + y * y + fn)
    if n.count('1') % 2 == 0: return True
    return False

pos, steps = 1 + 1j, 0
front, seen = set(), set()
front.add(pos), seen.add(pos)

while 31 + 39j not in seen:
    nfront = set()
    steps += 1
    for p in front:
        for d in dirs:
            np = p + d
            if np.real < 0 or np.imag < 0 or np in seen: continue
            if isopen(np):
                nfront.add(np)
                seen.add(np)
    front = nfront
    if steps == 50: p2 = len(seen)
print(steps)
print(p2)