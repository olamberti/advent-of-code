from intcode import IntCode
memory = [int(x) for x in open('19.txt').read().split(',')]

# P1
beam, grid, size = set(), '', 50
for x in range(size):
    for y in range(size):
        prog = IntCode((memory))
        if prog.run([x, y]):
            beam.add(x + y*1j)
            grid += '#'
        else: grid += '.'
    grid += '\n'
print(len(beam))
print(grid)

# P2
# to be implemented