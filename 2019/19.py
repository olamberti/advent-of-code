from intcode import IntCode
memory = [int(x) for x in open('19.txt').read().split(',')]

def printmap(beam):
    MX, MY = int(max([n.real for n in beam])), int(max([n.imag for n in beam]))
    grid = ''
    for x in range(MX + 1):
        for y in range(MY + 1):
            if x + y*1j in beam: grid += '#'
            else: grid += '.'
        grid += '\n'
    print(grid)

# P1
beam, size = set(), 50
for x in range(size):
    for y in range(size):
        prog = IntCode((memory))
        if prog.run([x, y]):
            beam.add(x + y*1j)
print(len(beam))
printmap(beam)

pass
# P2
# to be implemented