# Init:
memlist = [int(x) for x in open('11.txt').read().split(',')]
memory = {i: val for i, val in enumerate(memlist)}

def run(mem, p, base, inp):
  res = []
  
  # Read memory:
  def rmem(n):
    return mem[n] if n in mem else 0

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
      p1, p2, p3 = mem[p+1], mem[p+2], mem[p+3]
      if pars[0] == 0: a = rmem(p1)
      elif pars[0] == 1: a = p1
      elif pars[0] == 2: a = rmem(p1 + base)
      if pars[1] == 0: b = rmem(p2)
      elif pars[1] == 1: b = p2
      elif pars[1] == 2: b = rmem(p2 + base)
      if pars[2] == 0: t = p3
      elif pars[2] == 2: t = p3 + base
      if inst == 1: mem[t] = a + b
      elif inst == 2: mem[t] = a * b
      p += 4
      
    elif inst == 3:
      p3 = mem[p+1]
      if pars[0] == 0: t = p3
      elif pars[0] == 2: t = p3 + base
      mem[t] = inp
      p += 2
    elif inst == 4:
      p1 = mem[p+1]
      if pars[0] == 0: a = rmem(p1)
      elif pars[0] == 1: a = p1
      elif pars[0] == 2: a = rmem(p1 + base)
      res.append(a)
      p += 2
    elif inst == 5 or inst == 6:
      p1, p2 = mem[p+1], mem[p+2]
      if pars[0] == 0: a = rmem(p1)
      elif pars[0] == 1: a = p1
      elif pars[0] == 2: a = rmem(p1 + base)
      if pars[1] == 0: b = rmem(p2)
      elif pars[1] == 1: b = p2
      elif pars[1] == 2: b = rmem(p2 + base)
      if inst == 5: p = b if a != 0 else p + 3
      elif inst == 6: p = b if a == 0 else p + 3
    elif inst == 7 or inst == 8:
      p1, p2, p3 = mem[p+1], mem[p+2], mem[p+3]
      if pars[0] == 0: a = rmem(p1)
      elif pars[0] == 1: a = p1
      elif pars[0] == 2: a = rmem(p1 + base)
      if pars[1] == 0: b = rmem(p2)
      elif pars[1] == 1: b = p2
      elif pars[1] == 2: b = rmem(p2 + base)
      if pars[2] == 0: t = p3
      elif pars[2] == 2: t = p3 + base
      if inst == 7: mem[t] = 1 if a < b else 0
      elif inst == 8: mem[t] = 1 if a == b else 0
      p += 4
    elif inst == 9:
      p1 = mem[p+1]
      if pars[0] == 0: a = rmem(p1)
      elif pars[0] == 1: a = p1
      elif pars[0] == 2: a = rmem(p1 + base)
      base += a
      p += 2

    if len(res) == 2:
      return res, p, base
  
  return res, -1, -1

# P1:
whites, tile, d = set(), 0, 1j

visited, p, base = set(), 0, 0
while True:
  visited.add(tile)
  inp = 1 if tile in whites else 0
  res, p, base = run(memory, p, base, inp)
  if p == -1: break
  if res[0] == 0 and tile in whites: whites.remove(tile)
  elif res[0] == 1: whites.add(tile)
  if res[1] == 0: d *= 1j 
  elif res[1] == 1: d *= -1j
  tile += d
print(len(visited))

# P2:
memory = {i: val for i, val in enumerate(memlist)}
whites, tile, d = set(), 0, 1j
whites.add(tile)

visited, p, base = set(), 0, 0
mx, my, Mx, My = float('inf'), float('inf'), 0, 0
while True:
  visited.add(tile)
  mx, my = int(min(mx, tile.real)), int(min(my, tile.imag))
  Mx, My = int(max(Mx, tile.real)), int(max(My, tile.imag))
  inp = 1 if tile in whites else 0
  res, p, base = run(memory, p, base, inp)
  if p == -1: break
  if res[0] == 0 and tile in whites: whites.remove(tile)
  elif res[0] == 1: whites.add(tile)
  if res[1] == 0: d *= 1j 
  elif res[1] == 1: d *= -1j 
  tile += d

for r in range(My, my - 1, -1):
  row = ''
  for c in range(mx, Mx + 1):
    if c + r * 1j in whites: row += '█'
    else: row += ' '
  print(row)