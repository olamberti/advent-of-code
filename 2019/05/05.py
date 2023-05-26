from copy import deepcopy as dp
memory = [int(x) for x in open('05.txt').read().split(',')]

class IntCode:
    def __init__(self, mem):
      self.mem = dp(mem)    # internal memory
      self.pos = 0          # position pointer
      self.halt = False     # program finished
      self.commands = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 1}
    
    # Class methods:
    
    # 1. Reads opcode and parameter modes
    def get_opcode(self, n):              
      opcode = n % 100
      n = (n - opcode) // 100
      modes = []
      for _ in range(self.commands[opcode]):
        modes.append(n % 10)
        n = (n - modes[-1]) // 10
      return opcode, modes
    
    # 2. Reads parameter based on mode
    def get_par(self, mode, par):         
      if mode == 0: return self.mem[par]
      elif mode == 1: return par
    
    # 3. Reads next instruction and its parameters
    def get_inst(self, pos):              
      opcode, modes = self.get_opcode(pos)
      inst = self.mem[self.pos + 1 : self.pos + self.commands[opcode] + 1]
      if opcode in [1, 2, 7, 8]:
        pars = [self.get_par(modes[0], inst[0]), self.get_par(modes[1], inst[1]), inst[2]]
      elif opcode in [5, 6]:
        pars = [self.get_par(modes[0], inst[0]), self.get_par(modes[1], inst[1])]
      elif opcode == 3:
        pars = [inst[0]]
      elif opcode == 4:
        pars = [self.get_par(modes[0], inst[0])]
      elif opcode == 99:
        pars = None
      return opcode, pars
        

    # Program run
    def run(self, inp):
      while not self.halt:
        # Opcode instruction & modes
        oc, pars = self.get_inst(self.mem[self.pos])

        # 1. & 2 Addition or multiplication
        if oc == 1 or oc == 2:
          a, b, t = pars[:]
          # Addition
          if oc == 1: self.mem[t] = a + b
          # Multiplication
          elif oc == 2: self.mem[t] = a * b
          self.pos += 4
        # 3. Input instruction
        elif oc == 3:
          t = pars[0]
          self.mem[t] = inp
          self.pos += 2
        # 4. Output instruction
        elif oc == 4:
          a = pars[0]
          self.pos += 2
          # Check if program is halt:
          if self.mem[self.pos] == 99:
            self.halt = True
          return a
        # 5. & 6. Jump
        elif oc == 5 or oc == 6:
          a, b = pars[:]
          # Jump if true
          if oc == 5: self.pos = b if a != 0 else self.pos + 3
          # Jump if false
          elif oc == 6: self.pos = b if a == 0 else self.pos + 3
        # 7. & 8. Compare
        elif oc == 7 or oc == 8:
          a, b, t = pars[:]
          # Less than
          if oc == 7: self.mem[t] = 1 if a < b else 0
          # Equal
          elif oc == 8: self.mem[t] = 1 if a == b else 0
          self.pos += 4
        # 99. Halt
        elif oc == 99: 
          self.halt = True
          return None

# P1
p1 = IntCode(memory)
while not p1.halt:
  res = p1.run(1)
print(res)

# P2
p2 = IntCode(memory)
print(p2.run(5))