from intcode import IntCode
memory = [int(x) for x in open('d05.txt').read().split(',')]

# P1
p1 = IntCode(memory)
while not p1.halt:
  res = p1.run(1)
print(res)

# P2
p2 = IntCode(memory)
print(p2.run(5))