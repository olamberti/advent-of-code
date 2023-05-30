# Parsing:
rul, mes, bp = {}, [], False
for l in open('19.txt').read().splitlines():
  if l == '': bp = True
  elif bp: mes.append(l)
  else:
    k, v = l.split(': ')
    if 'a' in v: rul[k] = 'a'
    elif 'b' in v: rul[k] = 'b'
    elif '|' not in v: rul[k] = [x for x in v.split()]
    else:
      v1, v2 = v.split('|')
      rul[k] = ([x for x in v1.split()], [x for x in v2.split()])

# Build up rule 0:
def add(A, B):
  ans  = []
  for a in A:
    for b in B:
      ans.append(a + b)
  return ans  

def construct(n):
  ans, v = [''], rul[n]
  
  if isinstance(v, str):
    ans = add(ans, [v])
    
  if isinstance(v, list):
    for e in v:
      inc = construct(e)
      ans = add(ans, inc)
  
  elif isinstance(v, tuple):
      v1, v2 = v[0], v[1]
      ans1, ans2 = ans.copy(), ans.copy()
      for e in v1:
        inc = construct(e)
        ans1 = add(ans1, inc)
      for e in v2:
        inc = construct(e)
        ans2 = add(ans2, inc)
      ans = ans1 + ans2
  return ans

ch = set(construct('0'))

# P1:
tot = 0
for m in mes:
  if m in ch: tot += 1
print(tot)

# P2:
ch31, ch42 = construct('31'), construct('42')
l31, l42 = len(ch31[0]), len(ch42[0])
ch31, ch42 = set(ch31), set(ch42)

tot = 0
for m in mes:
  i, n42, n31 = 0, 0, 0
  while i < len(m) and m[i : i + l42] in ch42:
    i += l42
    n42 += 1
  while i < len(m) and m[i : i + l31] in ch31:
    i += l31
    n31 += 1
  if i == len(m) and n42 > n31 and n31 > 0: tot += 1
print(tot)  