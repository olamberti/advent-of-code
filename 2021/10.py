pairs = {'(':')', '[':']', '{':'}', '<':'>'}
values = {')':3, ']':57, '}':1197, '>':25137}

total, scores = 0, []

for line in open('10.txt', 'r').read().splitlines():
  stack = []
  for c in line:
    if c in pairs: stack.append(c)
    elif c == pairs[stack[-1]]: stack.pop()
    else:
      total += values[c]
      break
  else:
    score = 0
    for c in stack[::-1]:
      score *= 5
      score += ')]}>'.find(pairs[c]) + 1
    scores.append(score)
    
print(total)
scores.sort()
print(scores[len(scores) // 2])