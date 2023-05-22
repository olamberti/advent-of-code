# Init:
from copy import deepcopy as dp
import itertools
program = [int(x) for x in open('07.txt').read().split(',')]
program_ = dp(program)

# Running the program:
def run(mem, p, input):
  i = 0
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
      mem[t] = input[i]
      i += 1
      p += 2
    elif inst == 4:
      p1 = mem[p+1]
      a = p1 if pars[0] == 1 else mem[p1]
      p += 2
      return a, p
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
  return input[-1], -1

# P1:
val, thrust = 0, 0
phases = [0, 1, 2, 3, 4]
combos = [i for i in itertools.permutations(phases, 5)]

for combo in combos:
  val = 0
  for ph in combo:
    program = dp(program_)
    val, pointer = run(program, 0, [ph, val])
  thrust = max(thrust, val)
print(thrust)

# P2:
val, thrust = 0, 0
phases = [5, 6, 7, 8, 9]
combos = [i for i in itertools.permutations(phases, 5)]

for combo in combos:
  modules = [dp(program_), dp(program_), dp(program_), dp(program_), dp(program_)]
  pointers = [0] * 5
  val, start = 0, True
  while pointers[-1] != -1:
    for i, ph in enumerate(combo):
      if start: val, pointers[i] = run(modules[i], pointers[i], [ph, val])
      else: val, pointers[i] = run(modules[i], pointers[i], [val])
    start = False
  thrust = max(thrust, val)
print(thrust)