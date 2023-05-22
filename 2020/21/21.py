# Input parse:
foods, ings, alls = [], set(), dict()
for line in open('21.txt').read().splitlines():
  l1, l2 = line.split(' (')
  l1, l2 = l1.split(), l2.strip(')')[9:].split(', ')
  foods.append([l1, l2])
  for i in l1: ings.add(i)
  for a in l2:
    if a not in alls:
      alls[a] = set(l1)
    else:
      alls[a] = alls[a] & set(l1)
      
# Reduce allergens list:
reduced = True
while reduced:
  reduced = False
  for a, i in alls.items():
    if len(i) > 1: continue
    uni = list(i)[0]
    for a_, i_ in alls.items():
      if a_ == a: continue
      elif uni in i_:
        alls[a_].remove(uni)
        reduced = True

# Create OK ingerdients list:
goods = set()
for i in ings:
  for bads in alls.values():
    if i in bads: break
  else: goods.add(i)

# P1: count good ingerdients appearence:
p1 = 0
for good in goods:
  for food in foods:
    if good in food[0]: p1 += 1
print(p1)

# P2: produce canonical dangerous ingerdient list:
clid = []
for a, i in alls.items():
  clid.append([a, list(i)[0]])
clid.sort()
p2 = ','.join([x[1] for x in clid])
print(p2)