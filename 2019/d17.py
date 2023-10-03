from intcode import IntCode
memory = [int(x) for x in open('d17.txt').read().split(',')]

# P1
prog, dirs, draw = IntCode(memory), [1, 1j, -1, -1j], ''
x, y, scaff = 0, 0, set()
while not prog.halt:
    out = prog.run()
    if out:
        draw += chr(out)
        if out == 35:
            scaff.add(x + y*1j)
        x += 1
        if out == 10:
            x = 0
            y += 1

p1 = 0
for s in scaff:
    for d in dirs:
        if (s + d) not in scaff: break
    else:
        p1 += int(s.real * s.imag)
print(p1)
# print(draw) # printing the map - I used this to handcraft the movement logic

# P2
# Following parts are hand-crafted based on the printed map:
move = 'A,B,A,C,B,A,C,B,A,C'
A = 'L,6,L,4,R,12'
B = 'L,6,R,12,R,12,L,8'
C = 'L,6,L,10,L,10,L,6'

# From here it is general again:
memory[0], inp, vid = 2, [], 'n'
prog = IntCode(memory)
for p in [move, A, B, C, vid]:
    for e in p: inp.append(ord(e))
    inp.append(10)
while not prog.halt:
    p2 = prog.run(inp)
print(p2)