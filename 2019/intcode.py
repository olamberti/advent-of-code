from copy import deepcopy as dp

class IntCode:
    def __init__(self, mem, pos = 0, base = 0, halt = False):
      if type(mem) == list:
        self.mem = {i: val for i, val in enumerate(mem)}  # convert internal memory as dictionary
      else:
        self.mem = mem
      self.pos, self.base, self.halt = pos, base, halt    # position pointer, relative base, program finished
      self.commands = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}
      self.input = []
    
    def copy(self):
      return IntCode(dp(self.mem), self.pos, self.base, self.halt)
    
    # ----- IntCode methods ------

    # Read memory:
    def read_mem(self, n):
        return self.mem[n] if n in self.mem else 0

    # Read opcode and parameter modes
    def get_inst(self, n):              
      opcode = n % 100
      n = (n - opcode) // 100
      self.pos += 1
      vals, locs = [], []
      for i in range(self.commands[opcode]):
        mode = n % 10
        n = (n - mode) // 10
        vals.append(self.get_var(mode, self.read_mem(self.pos)))
        locs.append(self.get_loc(mode, self.read_mem(self.pos)))
        self.pos += 1
      return opcode, vals, locs
    
    # Read variable parameters based on mode
    def get_var(self, mode, par):       
      if mode == 0: return self.read_mem(par)
      elif mode == 1: return par
      elif mode == 2: return self.read_mem(par + self.base)
    
    # Read target parameter based on mode
    def get_loc(self, mode, par):
      if mode == 0: return par
      elif mode == 1: return None
      elif mode == 2: return par + self.base
        
    # Program run
    def run(self, inp = [], network = False):
      if network:
        if type(inp) is list: self.input.extend(inp)
        else: self.input.append(inp)
      else:
        if type(inp) is list: self.input = inp
        else: self.input = [inp]

      while not self.halt:
        # Opcode instruction & modes
        oc, vals, locs = self.get_inst(self.mem[self.pos])

        # 1. & 2 Addition or multiplication
        if oc == 1 or oc == 2:
          if oc == 1: self.mem[locs[2]] = vals[0] + vals[1]
          elif oc == 2: self.mem[locs[2]] = vals[0] * vals[1]
        # 3. Input instruction
        elif oc == 3:
          if network and self.input == []: self.input.append(-1)
          self.mem[locs[0]] = self.input.pop(0)
          if network: return None
        # 4. Output instruction
        elif oc == 4:
          # Check if program is halt:
          if self.mem[self.pos] == 99:
            self.halt = True
          return vals[0]
        # 5. & 6. Jump
        elif oc == 5 or oc == 6:
          if oc == 5: 
            if vals[0] != 0: self.pos = vals[1] 
          elif oc == 6: 
            if vals[0] == 0: self.pos = vals[1] 
        # 7. & 8. Compare
        elif oc == 7 or oc == 8:
          if oc == 7: self.mem[locs[2]] = 1 if vals[0] < vals[1] else 0
          elif oc == 8: self.mem[locs[2]] = 1 if vals[0] == vals[1] else 0
        # 9. Change relative base
        elif oc == 9: 
          self.base += vals[0]
        # 99. Halt
        elif oc == 99: 
          self.halt = True
          return None