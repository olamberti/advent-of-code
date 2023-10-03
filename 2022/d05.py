# Read in file:
with open("d05.txt","r") as input:  # use "input_test.txt" for test case
  text = input.read()
  text_lines = text.split("\n")
  # Determine stack number and height:
  for i, line in enumerate(text_lines):
    if line[1] == "1":  # end of box arrangement
      height = i
      number_of_stacks = int(line[-2])
      break
  # Read list of boxes:
  boxes  = []
  for n in range(number_of_stacks):
    row = []
    for h in range(height):
      box = text_lines[height -  h - 1][n * 4 + 1]
      if box.isalpha():
        row.append(box)
      else:
        break
    boxes.append(row)
  # Read list of moves (number of boxes to move, from, to):
  text_lines = text_lines[height + 2 :]
  moves = []
  for line in text_lines:
    line = line.split()
    moves.append([int(line[1]), int(line[3]), int(line[5])])

# Execute moves:
boxes_1 = [x[:] for x in boxes] # deep copy
boxes_2 = [x[:] for x in boxes] # deep copy
for move in moves:
  number_of_boxes = move[0]
  move_from = move[1]
  move_to = move[2]
  # Handle crane 9001 move:
  boxes_2[move_to - 1].extend(boxes_2[move_from - 1][-number_of_boxes:])
  # Handle crane 9000 moves and pops:
  for i in range(number_of_boxes):
    boxes_1[move_to - 1].append(boxes_1[move_from - 1][-1])
    boxes_1[move_from - 1].pop()
    boxes_2[move_from - 1].pop()
# Print result
top_row_1 = ""
top_row_2 = ""
for row in boxes_1:
  top_row_1 += row[-1]
for row in boxes_2:
  top_row_2 += row[-1]
print(top_row_1)
print(top_row_2)