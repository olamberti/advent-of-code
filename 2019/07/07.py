# Init:
from copy import deepcopy as dp
import itertools
memory = [int(x) for x in open('07.txt').read().split(',')]

class IntCode:
    def __init__(self, mem):
      self.mem = dp(mem)
      self.p = 0
      self.halt = False
    
    # Instruction handling
    def inst(self, n):
      opcode = n % 100
      n = (n - opcode) // 100
      pars = []
      for _ in range(3):
        pars.append(n % 10)
        n = (n - pars[-1]) // 10
      return opcode, pars

    # Program run
    def run(self, inp):
      while not self.halt:
        # Opcode instruction
        oc, pars = self.inst(self.mem[self.p])

        # 1. & 2 Addition or multiplication
        if oc == 1 or oc == 2:
          p1, p2, t = self.mem[self.p + 1 : self.p + 4]
          a = p1 if pars[0] == 1 else self.mem[p1]
          b = p2 if pars[1] == 1 else self.mem[p2]
          # Addition
          if oc == 1: self.mem[t] = a + b
          # Multiplication
          elif oc == 2: self.mem[t] = a * b
          self.p += 4
        # 3. Input instruction
        elif oc == 3:
          t = self.mem[self.p + 1]
          self.mem[t] = inp.pop(0)
          self.p += 2
        # 4. Output instruction
        elif oc == 4:
          p1 = self.mem[self.p + 1]
          a = p1 if pars[0] == 1 else self.mem[p1]
          self.p += 2
          # Check if program is halt:
          if self.mem[self.p] == 99:
            self.halt = True
          return a
        # 5. & 6. Jump
        elif oc == 5 or oc == 6:
          p1, p2 = self.mem[self.p + 1 : self.p + 3]
          a = p1 if pars[0] == 1 else self.mem[p1]
          b = p2 if pars[1] == 1 else self.mem[p2]
          # Jump if true
          if oc == 5: self.p = b if a != 0 else self.p + 3
          # Jump if false
          elif oc == 6: self.p = b if a == 0 else self.p + 3
        # 7. & 8. Compare
        elif oc == 7 or oc == 8:
          p1, p2, t = self.mem[self.p + 1: self.p + 4]
          a = p1 if pars[0] == 1 else self.mem[p1]
          b = p2 if pars[1] == 1 else self.mem[p2]
          # Less than
          if oc == 7: self.mem[t] = 1 if a < b else 0
          # Equal
          elif oc == 8: self.mem[t] = 1 if a == b else 0
          self.p += 4
        # 99. Halt
        elif oc == 99: 
          self.halt = True
          return None

# P1:
val, thrust = 0, 0
phases = [0, 1, 2, 3, 4]
combos = [i for i in itertools.permutations(phases, 5)]

for combo in combos:
  val = 0
  for ph in combo:
    program = IntCode(memory)
    val = program.run([ph, val])
  thrust = max(thrust, val)
print(thrust)

# P2:
thrust = 0
phases = [5, 6, 7, 8, 9]
combos = [i for i in itertools.permutations(phases, 5)]

for combo in combos:
  amplifiers = [IntCode(memory), IntCode(memory), IntCode(memory), IntCode(memory), IntCode(memory)]
  val, first = 0, True
  while not amplifiers[-1].halt:
    for i, ph in enumerate(combo):
      if first: 
        val = amplifiers[i].run([ph, val])
      else: val = amplifiers[i].run([val])
    first = False
  thrust = max(thrust, val)
print(thrust)