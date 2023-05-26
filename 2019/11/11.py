# Init:
memory = [int(x) for x in open('11.txt').read().split(',')]

class IntCode:
    def __init__(self, mem):
      self.mem = {i: val for i, val in enumerate(mem)}  # internal memory as dictionary
      self.pos = 0          # position pointer
      self.base = 0         # relative base
      self.halt = False     # program finished
      self.commands = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 1}
    
    # Class methods:
    
    # Read memory:
    def read_mem(self, n):
        return self.mem[n] if n in self.mem else 0

    # Read opcode and parameter modes
    def get_opcode(self, n):              
      opcode = n % 100
      n = (n - opcode) // 100
      modes = []
      for _ in range(self.commands[opcode]):
        modes.append(n % 10)
        n = (n - modes[-1]) // 10
      return opcode, modes
    
    # Read parameter based on mode
    def get_par(self, mode, par):         
      if mode == 0: return self.read_mem(par)
      elif mode == 1: return par
      elif mode == 2: return self.read_mem(par + self.base)
    
    # Read target destination based on mode
    def get_tar(self, mode, dir):
      if mode == 0: return dir
      elif mode == 2: return dir + self.base
    
    # Reads next instruction and its parameters
    def get_inst(self, pos):              
      opcode, modes = self.get_opcode(pos)
      inst = []
      for i in range(self.commands[opcode]):
        inst.append(self.read_mem(self.pos + i + 1))
      if opcode in [1, 2, 7, 8]:
        pars = [self.get_par(modes[0], inst[0]), self.get_par(modes[1], inst[1]), self.get_tar(modes[2], inst[2])]
      elif opcode in [5, 6]:
        pars = [self.get_par(modes[0], inst[0]), self.get_par(modes[1], inst[1])]
      elif opcode == 3:
        pars = [self.get_tar(modes[0], inst[0])]
      elif opcode in [4, 9]:
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
          self.mem[t] = inp.pop(0)
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
        # 9. Change relative base
        elif oc == 9: 
          a = pars[0]
          self.base += a
          self.pos += 2
        # 99. Halt
        elif oc == 99: 
          self.halt = True
          return None

# P1:
whites, visited, tile, d = set(), set(), 0, 1j
robot = IntCode(memory)

while not robot.halt:
  visited.add(tile)
  inp = 1 if tile in whites else 0
  color = robot.run([inp])
  turn = robot.run([inp])
  if color == 0 and tile in whites: whites.remove(tile)
  elif color == 1: whites.add(tile)
  if turn == 0: d *= 1j 
  elif turn == 1: d *= -1j
  tile += d
print(len(visited))

# P2:
whites, visited, tile, d = set(), set(), 0, 1j
whites.add(tile)
robot = IntCode(memory)

mx, my, Mx, My = float('inf'), float('inf'), 0, 0
while not robot.halt:
  visited.add(tile)
  mx, my = int(min(mx, tile.real)), int(min(my, tile.imag))
  Mx, My = int(max(Mx, tile.real)), int(max(My, tile.imag))
  inp = 1 if tile in whites else 0
  color = robot.run([inp])
  turn = robot.run([inp])
  if color == 0 and tile in whites: whites.remove(tile)
  elif color == 1: whites.add(tile)
  if turn == 0: d *= 1j 
  elif turn == 1: d *= -1j
  tile += d

for r in range(My, my - 1, -1):
  row = ''
  for c in range(mx, Mx + 1):
    if c + r * 1j in whites: row += '█'
    else: row += ' '
  print(row)