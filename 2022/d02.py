# Rock: A, X | Paper: B, Y | Scissors: C, Z
convert_elf = {"A": "R", "B": "P", "C": "S"}
convert_player = {"X": "R", "Y": "P", "Z": "S"}
convert_result = {"X": 0, "Y": 3, "Z": 6}
point_table = {"R": 1, "P": 2, "S": 3}
winner = {"R": "P","P": "S","S": "R"}
looser = {player: elf for elf, player in winner.items()}

def calc_score_1(elf, player):
  score = point_table[player]
  if winner[elf] == player:
    score += 6
  elif elf == player:
    score += 3
  return score
  
def calc_score_2(elf, result):
  score = result
  if result == 6:
    player = winner[elf]
  elif result == 3:
    player = elf
  else:
    player = looser[elf]
  score += point_table[player]
  return score

total_score_1 = 0
total_score_2 = 0
with open("d02.txt","r") as input:  # use "input_test.txt" for the test case
  for line in input:
    elf = convert_elf[line[0]]   
    player = convert_player[line[2]]
    result = convert_result[line[2]]
    total_score_1 += calc_score_1(elf,player)
    total_score_2 += calc_score_2(elf,result)
print(total_score_1)
print(total_score_2)