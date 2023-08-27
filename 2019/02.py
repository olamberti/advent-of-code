from intcode import IntCode
memory = [int(x) for x in open('02.txt').read().split(',')]

# P1:
memory[1:3] = 12, 2
prog = IntCode(memory)
prog.run()
print(prog.mem[0])

# P2:
res = 19690720
for a1 in range(100):
  for a2 in range(100):
    memory[1:3] = a1, a2
    prog = IntCode(memory)
    prog.run()
    out = prog.mem[0]
    if out == res:
      print(100 * a1 + a2)
      break
  if out == res: break