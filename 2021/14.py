# Read input
from copy import deepcopy as dp

with open('14.txt') as input:
  data = input.read().splitlines()

temp, rules, pairs, elems = data[0], {}, {}, {}
for i in range(2, len(data)):
  rule = data[i].split(' -> ')
  pair, new = rule[0], rule[1]
  rules[pair], pairs[pair], elems[new] = [pair[0] + new, new + pair[1]], 0, 0

# Prepare polymer pairs:
first, last = temp[0], temp[-1]
poly = dict(pairs)
for i in range(len(temp) - 1):
  left, right = temp[i], temp[i + 1]
  poly[left + right] += 1

# Count function:
def answer(poly, elem):
  new_elem = dp(elem)
  for pair, num in poly.items():
    left, right = pair[0], pair[1]
    new_elem[left] += num
    new_elem[right] += num
  new_elem[first] += 1
  new_elem[last] += 1
  counts = [x // 2 for x in list(new_elem.values())]
  counts.sort()
  return(counts[-1] - counts[0])

# Pair insertions
for step in range(40):
  new_poly = dict(pairs)
  for pair, num in poly.items():
    for new_pair in rules[pair]:
      new_poly[new_pair] += num
  poly = dict(new_poly)
  if step + 1 == 10:
    print(answer(poly, elems))
    
print(answer(poly, elems))