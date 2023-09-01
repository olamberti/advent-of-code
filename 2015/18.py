dirs, corners = [1 - 1j, 1, 1 + 1j, 1j, - 1 + 1j, -1, -1 -1j, -1j], [0, 99, 99j, 99 + 99j]
on, off = set(), set()
for y, line in enumerate(open('18.txt').readlines()):
    for x, c in enumerate(line.strip()):
        if c == '.': off.add(x + y *1j)
        elif c == '#': on.add(x + y *1j)
on_0, off_0 = on, off

def corners_on(on, off):
    for cell in corners:
        on.add(cell)
        if cell in off:
            off.remove(cell)
    return on, off

def anim(on, off):
    new_on, new_off = set(), set()
    for cell in on:
        n = 0
        for d in dirs:
            ncell = cell + d
            if ncell in on: n += 1
        if n == 2 or n == 3: new_on.add(cell)
        else: new_off.add(cell)
    for cell in off:
        n = 0
        for d in dirs:
            ncell = cell + d
            if ncell in on: n += 1
        if n == 3: new_on.add(cell)
        else: new_off.add(cell)
    return new_on, new_off

# P1
for _ in range(100):
    on, off = anim(on, off)
print(len(on))

# P2
on, off = on_0, off_0
for _ in range(100):
    on, off = corners_on(on, off)
    on, off = anim(on, off)
on, off = corners_on(on, off)
print(len(on))