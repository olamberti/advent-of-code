with open("02.txt", "r") as input:
  text = input.read()
  data = text.splitlines()
horizontal = 0
depth = 0
aim = 0
for move in data:
  move = move.split()
  if move[0] == "forward":
    horizontal += int(move[1])
    depth += aim * int(move[1])
  elif move[0] == "up":
    aim -= int(move[1])
  elif move[0] == "down":
    aim += int(move[1])
print(horizontal * aim)
print(horizontal * depth)