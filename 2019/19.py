from intcode import IntCode
memory = [int(x) for x in open('19.txt').read().split(',')]

# Print function:
def printmap(beam):
    MX, MY, grid = int(max([n.real for n in beam])), int(max([n.imag for n in beam])), ''
    for y in range(MY + 1):
        for x in range(MX + 1):
            if x + y*1j in beam: grid += '#'
            else: grid += '.'
        grid += '\n'
    print(grid)

# Look for starting point (first # appears other than (0,0))
beam, r = set(), 1
beam.add(0 + 0j)

while len(beam) == 1:
    for x in range(r):
        y = r - x
        prog = IntCode(memory)
        if prog.run([x, y]):
            beam.add(x + y*1j)
            start = x + y*1j
    r += 1

# Follow left and right edges of the beam until the ship fits:
x , y, p1 = int(start.real), int(start.imag), len(beam)
xL, xR, solved = x, x, False
while not solved:
    y += 1
    # Left edge
    prog = IntCode((memory))
    if prog.run([xL + 1, y]) == 1: xL += 1
    else: xL += 2
    # Right edge
    prog = IntCode((memory))
    if prog.run([xR + 2, y]) == 1: xR += 2
    else: xR += 1
    # Add points to beam and check for P1 condition
    for x in range(xL, xR + 1):
        beam.add(x + y*1j)
        if x < 50 and y < 50: p1 += 1
    # Check if ship fits:
    if (xR - xL) >= 99 and (xL + (y - 99)*1j) in beam and (xL + 99 + (y - 99)*1j) in beam:
        solved = True
        p2 = xL * 10_000 + (y - 99)
    
print(p1)
print(p2)
# printmap(beam)