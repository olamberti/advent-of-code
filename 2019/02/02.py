from copy import deepcopy as dp
memory = [int(x) for x in open('02.txt').read().split(',')]
memory_ = dp(memory)

def run(mem):
  p = 0
  while mem[p] != 99:
    inst = mem[p]
    if inst == 1 or inst == 2:
      a, b, t = mem[p+1:p+4]
      if inst == 1: mem[t] = mem[a] + mem[b]
      elif inst == 2: mem[t] = mem[a] * mem[b]
    p += 4
  return mem[0]

# P1:
memory[1:3] = 12, 2
print(run(memory))

# P2:
res = 19690720
for a1 in range(100):
  for a2 in range(100):
    memory = dp(memory_)
    memory[1:3] = a1, a2
    out = run(memory)
    if out == res:
      print(100 * a1 + a2)
      break
  if out == res: break