# Input:
ran, tic, prt = {}, [], 1

for lin in open('16.txt').read().splitlines():
  if lin == '': 
    prt += 1
    continue
  if prt == 1:
    key, r = lin.split(': ')
    r = r.split(' or ')
    r1, r2 = [int(x) for x in r[0].split('-')], [int(x) for x in r[1].split('-')]
    ran[key] = [range(r1[0], r1[1] + 1), range(r2[0], r2[1] + 1)]
  elif prt == 2:
    if 'your' in lin: continue
    own = [int(x) for x in lin.split(',')]
  elif prt == 3:
    if 'nearby' in lin: continue
    tic.append([int(x) for x in lin.split(',')])

# P1 - eliminate invalid tickets
tot, vt = 0, []
for t in tic:
  valid = True
  for v in t:
    ok = False
    for r1, r2 in ran.values():
      if v in r1 or v in r2:
        ok = True
        break
    if not ok: 
      tot += v
      valid = False
  if valid: vt.append(t)
vt.append(own)
print(tot)

# P2.1 - collect possible fields for each position
pfs = [[] for _ in range(len(ran))]
for f in ran:
  r1, r2 = ran[f]
  for j in range(len(ran)):
    ok = True
    for t in vt:
      if t[j] not in r1 and t[j] not in r2:
        ok = False
        break
    if ok:
      pfs[j].append(f)
    continue
    
# P2.2 - identify fields by elimination
fs = [None for _ in range(len(ran))]
found = set()
while None in fs:
  for i, pf in enumerate(pfs):
    if len(pf) == 1:
      fs[i] = pf[0]
      found.add(pf[0])
    else:
      for p in pf:
        if p in found: pf.remove(p)

# P2.3 - calculate answer:
tot = 1
for i, f in enumerate(fs):
  if 'departure' in f: tot *= own[i]
print(tot)