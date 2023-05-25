from copy import deepcopy as dp
memory = [int(x) for x in open('02.txt').read().split(',')]

class IntCode:
    def __init__(self, mem):
      self.mem = dp(mem)
      self.p = 0
      self.halt = False

    # Program run:
    def run(self):
      while not self.halt:
        # Opcode instruction
        oc = self.mem[self.p]

        # Addition or multiplication
        if oc == 1 or oc == 2:
          a, b, t = self.mem[self.p + 1 : self.p + 4]
          # Addition:
          if oc == 1: self.mem[t] = self.mem[a] + self.mem[b]
          # Multiplication:
          elif oc == 2: self.mem[t] = self.mem[a] * self.mem[b]
        self.p += 4
        if oc == 99: self.halt = True
      return self.mem[0]


# P1:
memory[1:3] = 12, 2
prog = IntCode(memory)
print(prog.run())

# P2:
res = 19690720
for a1 in range(100):
  for a2 in range(100):
    memory[1:3] = a1, a2
    prog = IntCode(memory)
    out = prog.run()
    if out == res:
      print(100 * a1 + a2)
      break
  if out == res: break