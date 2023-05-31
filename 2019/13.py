from intcode import IntCode
memory = [int(x) for x in open('13.txt').read().split(',')]

# P1:
game = IntCode(memory)
blocks = 0
while not game.halt:
  x = game.run()
  y = game.run()
  tileID = game.run()
  if tileID == 2: blocks += 1
print(blocks)

# P2:
memory[0] = 2
game = IntCode(memory)
joystick, padX, ballX = 1, None, None
while not game.halt:
  if padX and ballX:
    if padX == ballX: joystick = 0
    elif padX < ballX: joystick = 1
    else: joystick = -1
  x = game.run(joystick)
  y = game.run(joystick)
  tileID = game.run(joystick)
  if tileID == 4: ballX = x
  elif tileID == 3: padX = x
  elif x == -1 and y == 0: score = tileID
print(score)