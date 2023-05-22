from copy import deepcopy as dp
program = [int(x) for x in open('05.txt').read().split(',')]
program_ = dp(program)

def run(mem, inp):
  p, res = 0, []
  while mem[p] != 99:
    # Handle instruction's opcode:
    opcode, inst = mem[p], mem[p] % 100
    opcode = (opcode - inst) // 100
    pars = []
    for _ in range(3):
      pars.append(opcode % 10)
      opcode = (opcode - pars[-1]) // 10

    # Execute instruction:
    if inst == 1 or inst == 2:
      p1, p2, t = mem[p+1:p+4]
      a = p1 if pars[0] == 1 else mem[p1]
      b = p2 if pars[1] == 1 else mem[p2]
      if inst == 1: mem[t] = a + b
      elif inst == 2: mem[t] = a * b
      p += 4
    elif inst == 3:
      t = mem[p+1]
      mem[t] = inp
      p += 2
    elif inst == 4:
      p1 = mem[p+1]
      a = p1 if pars[0] == 1 else mem[p1]
      res.append(a)
      p += 2
    elif inst == 5 or inst == 6:
      p1, p2 = mem[p+1:p+3]
      a = p1 if pars[0] == 1 else mem[p1]
      b = p2 if pars[1] == 1 else mem[p2]
      if inst == 5: p = b if a != 0 else p + 3
      elif inst == 6: p = b if a == 0 else p + 3
    elif inst == 7 or inst == 8:
      p1, p2, t = mem[p+1:p+4]
      a = p1 if pars[0] == 1 else mem[p1]
      b = p2 if pars[1] == 1 else mem[p2]
      if inst == 7: mem[t] = 1 if a < b else 0
      elif inst == 8: mem[t] = 1 if a == b else 0
      p += 4
  return res

p1 = run(program, 1)
print(p1[-1])

program = dp(program_)
p2 = run(program, 5)
print(p2[-1])