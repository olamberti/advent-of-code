from intcode import IntCode
memory = [int(x) for x in open('11.txt').read().split(',')]

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