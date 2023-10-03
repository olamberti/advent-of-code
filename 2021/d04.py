# Read input:
import numpy as np
with open("d04.txt") as input:
  data = input.read().splitlines()
numbers = data[0].split(",")
data = [line.split() for line in data[2:]]
tables = []
for i in range(len(data)//6 + 1):
  tables.append(np.array(data[(i * 6) : (i * 6) + 5]))

# Draw number:
def draw_number(num):
  for table in tables:
    for i in range(5):
      for j in range(5):
        if table[i,j] == num:
          table[i,j] = "X"
    
# Check bingo:
def is_bingo():
  for table_num, table in enumerate(tables):
    for i in range(5):
      if (np.count_nonzero(table[i,:] == "X") == 5) or (np.count_nonzero(table[:,i] == "X") == 5):
        return True, table, table_num
  return False, None, None

# Calculate board score:
def calc_score(board, last_number):
  score = 0
  for x in np.nditer(board):
    if x != "X":
      score += int(x)
  score = score * int(last_number)
  return score
  
# Play:
num_bingos = 0
num_tables = len(tables)
for my_num in numbers:
  draw_number(my_num)
  bingo, winner, winner_num = is_bingo()
  while bingo:
    num_bingos += 1
    if num_bingos == 1: # first winner
      score_1 = calc_score(winner, my_num)
    elif num_bingos == num_tables: # last winner
      score_2 = calc_score(winner, my_num)
      break
    del tables[winner_num]
    bingo, winner, winner_num = is_bingo()

# Calculate score:
print(score_1)
print(score_2)