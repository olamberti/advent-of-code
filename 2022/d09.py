# Read input:
with open("d09.txt","r") as input:
  data = input.read().splitlines()
  
# Dictionary and functions:
directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

def add_vectors(v1, v2):
  return [v1[0] + v2[0], v1[1] + v2[1]]

def sub_vectors(v1, v2):
  return [v1[0] - v2[0], v1[1] - v2[1]]
  
def move_rope(rope, dir):
  rope[0] = add_vectors(rope[0], dir)
  for i in range(len(rope) - 1):
    head = rope[i]
    tail = rope[i + 1]
    diff = sub_vectors(head, tail)
    if (abs(diff[0]) <= 1) & (abs(diff[1]) <= 1): # head remained close
      continue
    elif (diff[0] == 0): # head is only vertically away
      rope[i+1] = add_vectors(rope[i+1],[0, diff[1]//abs(diff[1])])
    elif (diff[1] == 0): # head is only horizontally away
      rope[i+1] = add_vectors(rope[i+1], [diff[0]//abs(diff[0]), 0])
    else: # tail needs to do a vertical step
      rope[i+1] = add_vectors(rope[i+1], [diff[0]//abs(diff[0]), diff[1]//abs(diff[1])])
  return rope

# Simulate movement
my_rope = [[0, 0] for i in range(10)]
position_1 = []
position_2 = []
position_1.append(my_rope[1])
position_2.append(my_rope[9])
for command in data:
  command = command.split()
  direction = directions[command[0]]
  steps = int(command[1])
  for step in range(steps):
    my_rope = move_rope(my_rope, direction)
    if my_rope[1] not in position_1:
      position_1.append(my_rope[1])
    if my_rope[9] not in position_2:
      position_2.append(my_rope[9])
print(len(position_1))
print(len(position_2))