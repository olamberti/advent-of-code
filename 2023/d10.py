# Read input
ns, we, ne, nw, sw, se = set(), set(), set(), set(), set(), set()
dirs =  {'e':1, 's':1j, 'w':-1, 'n':-1j}

input = open('d10.txt')

eggs = set()
for y, line in enumerate(input):
    for x, c in enumerate(line.strip()):
        eggs.add(x + y*1j)
        if c == '|': ns.add(x + y*1j)
        elif c == '-': we.add(x + y*1j)
        elif c == 'L': ne.add(x + y*1j)
        elif c == 'J': nw.add(x + y*1j)
        elif c == '7': sw.add(x + y*1j)
        elif c == 'F': se.add(x + y*1j)
        elif c == 'S': start = x + y*1j

width, height = x + 1, y + 1
big_width, big_height = 2 * width, 2 * height

def get_next(pos, face):
    new_pos = pos + dirs[face]
    if face == 'e':
        if new_pos in we: new_face = 'e'
        elif new_pos in nw: new_face = 'n'
        elif new_pos in sw: new_face = 's'
    elif face == 's':
        if new_pos in ns: new_face = 's'
        elif new_pos in ne: new_face = 'e'
        elif new_pos in nw: new_face = 'w'
    elif face == 'w':
        if new_pos in we: new_face = 'w'
        elif new_pos in ne: new_face = 'n'
        elif new_pos in se: new_face = 's'
    elif face == 'n':
        if new_pos in ns: new_face = 'n'
        elif new_pos in sw: new_face = 'w'
        elif new_pos in se: new_face = 'e'    
    return new_pos, new_face

front, loop, steps = set(), set(), 0
for face, d in dirs.items():
    new_pos = start + d
    if face == 'e' and (new_pos in we or new_pos in nw or new_pos in sw):
        front.add((start, face))
    elif face == 's' and (new_pos in ns or new_pos in nw or new_pos in ne):
        front.add((start, face))
    elif face == 'w' and (new_pos in we or new_pos in ne or new_pos in se):
        front.add((start, face))
    elif face == 'n' and (new_pos in ns or new_pos in sw or new_pos in se):
        front.add((start, face))
loop.add(start)
eggs.remove(start)

big_loop = set()
big_loop.add(2*start)

while True:
    new_front = set()
    for pos, face in front:
        new_pos, new_face = get_next(pos, face)
        if new_pos in loop: continue
        loop.add(new_pos)
        eggs.remove(new_pos)
        big_loop.add(2 * pos + dirs[face])
        big_loop.add(2 * new_pos)
        new_front.add((new_pos, new_face))
    if new_front:
        front = new_front
        steps += 1
    else:
        big_loop.add(2 * pos + dirs[face])
        break
print(steps)

def printbig():
    for j in range(big_height):
        row = ''
        for i in range(big_width):
            if i + j*1j in big_loop: row += '#'
            else: row += '.'
        print(row)

not_egg = 0
front, seen = set(), set()
front.add(-1-1j)

while front:
    new_front = set()
    for pos in front:
        for d in [1, 1j, -1, -1j]:
            new_pos = pos + d
            if new_pos.real < -1 or new_pos.real > big_width + 1: continue
            elif new_pos.imag < -1 or new_pos.imag > big_height + 1: continue
            elif new_pos in big_loop or new_pos in seen: continue
            new_front.add(new_pos)
            seen.add(new_pos)
            if (new_pos / 2) in eggs: eggs.remove((new_pos / 2))
    front = new_front
print(len(eggs))