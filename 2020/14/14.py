m1, m2 = {}, {}

def p1(val, mask):
  val = list(bin(val)[2:].zfill(36))
  for i, c in enumerate(mask):
    if c != 'X': val[i] = mask[i]
  return int(''.join(val), 2)

def p2(add, mask):
  add = list(bin(add)[2:].zfill(36))
  res = ['']
  for i, c in enumerate(mask):
    l = len(res)
    if c == '0':
      for j in range(l): res[j] += add[i]
    elif c == '1':
      for j in range(l): res[j] += '1'
    else:
      res_ = []
      for r in res:
        res_.append(r + '0')
        res_.append(r + '1')
      res = res_
  return [int(''.join(x), 2) for x in res]  
    
for l in open('14.txt').read().splitlines():
  c, v = l.split(' = ')
  if c == 'mask': m = v
  else:
    a, v = int(c[4:-1]), int(v)
    m1[a] = p1(v, m)
    for a in p2(a, m): m2[a] = v

def dsum(d):
  return sum([v for v in d.values()])

print(dsum(m1))
print(dsum(m2))