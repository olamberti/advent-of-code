# Input:
data = open('21.txt', 'r').read().splitlines()
pos = [int(data[0][-1]), int(data[1][-1])]  # starting positions
table = [x for x in range(1, 11)]

# P1 - Play game with deterministic die:
score = [0, 0]                              # starting scores
nr, p = 0, 0                                # number of rolls, player ID
die = [x for x in range(1, 101)]            # die rolls in order 1-100

while True:
  p = p % 2                                 # current players ID (0 or 1)
  roll = 0                                  # total roll value
  for r in range(3):                        # repeat 3 times (rolls)
    roll += die[nr % 100]                   # roll value
    nr += 1                                 # roll number
  pos[p] = table[(pos[p] - 1 + roll) % 10]  # increase player postion
  score[p] += pos[p]                        # increase player score
  if max(score) >= 1000: break              # check if player has won
  p += 1                                    # switch players

print(min(score) * nr)

# P2 - Play game with quantum die:
pos = [int(data[0][-1]), int(data[1][-1])]      # reset starting positions
cache = {}                                      # stores number of wins for a given state

def q_roll():                                   # all possible quantum rolls
  return [i + j + k for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3]]
  
def get_wins(p0, p1, s0 = 0, s1 = 0):           # calculates wins for a given state
  
  s = (p0, p1, s0, s1)                          # game state
  if s in cache:                                # if state is in cashe
    return cache[s]                             # return cache value

  wins = [0, 0]                                 # number of wins per player
  
  for roll in q_roll():                         # all possible rolls
    p0N = table[(p0 - 1 + roll) % 10]           # increase player postion
    s0N = s0 + p0N                              # increase player score
    if s0N >= 21:                               # if player wins
      wins[0] += 1                              # increase win count by 1
    else:                                       # no win yet
      dw = get_wins(p1, p0N, s1, s0N)           # recursion with player switch
      wins[0] += dw[1]                          # increase p0 wins, care for switch
      wins[1] += dw[0]                          # increase p1 wins, care for switch
  
  cache[s] = wins
  return wins
    
w = get_wins(*pos)
print(max(w))