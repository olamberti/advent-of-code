from intcode import IntCode
memory = [int(x) for x in open('17.txt').read().split(',')]

# P1
prog, dirs = IntCode(memory), [1, 1j, -1, -1j]
x, y, scaff, space = 0, 0, set(), set()
while not prog.halt:
    out = prog.run()
    if out == 35:
        scaff.add(x + y*1j)
        x += 1
    elif out == 46:
        space.add(x + y*1j)
        x += 1
    elif out == 10:
        x = 0
        y += 1

p1 = 0
for s in scaff:
    for d in dirs:
        if (s + d) not in scaff: break
    else:
        p1 += int(s.real * s.imag)
print(p1)

#P2
# to be implemented... :)