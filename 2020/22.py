from copy import deepcopy as dp

# Input parsing:
cards, p = [[], []], 0
for line in open('22.txt').read().splitlines():
  if line == '': p += 1
  elif line.isnumeric(): cards[p].append(int(line))

# Functions:
def state(cards):
  return(tuple(cards[0]), tuple(cards[1]))

def play(cards, rc):
  mem = set()
  while len(cards[0]) > 0 and len(cards[1]) > 0:
    if state(cards) in mem: return 0
    else: mem.add(state(cards))
    a, b = cards[0].pop(0), cards[1].pop(0)
    if rc and a <= len(cards[0]) and b <= len(cards[1]):
      new_cards = [dp(cards[0][:a]), dp(cards[1][:b])]
      w = play(new_cards, rc)
      if w: cards[1].extend([b, a])
      else: cards[0].extend([a, b])
    else:
      if a > b: cards[0].extend([a, b])
      else: cards[1].extend([b, a])
  return 1 if len(cards[0]) == 0 else 0
  
# P1 - Play regular game:
cards_ = dp(cards)
winner = play(cards_, 0)
score_1 = sum([x * i for i, x in enumerate(cards_[winner][::-1], 1)])
print(score_1)

# P2 - Play recursive combat:
winner = play(cards, 1)
score_2 = sum([x * i for i, x in enumerate(cards[winner][::-1], 1)])
print(score_2)