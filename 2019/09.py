from intcode import IntCode
memory = [int(x) for x in open('09.txt').read().split(',')]

# P1:
p1 = IntCode(memory)
print(p1.run(1))

# P2:
p2 = IntCode(memory)
print(p2.run(2))