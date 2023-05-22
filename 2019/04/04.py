r, p1, p2 = [int(x) for x in open('04.txt').read().split('-')], 0, 0

def check_p1(x):
  x = str(x)
  inc, doub = 1, 0
  for i in range(len(x) - 1):
    if x[i] > x[i + 1]:
      inc = 0
      break
    if x[i] == x[i + 1]: doub = 1
  return inc and doub

def check_p2(x):
  x, s = str(x), set([c for c in str(x)])
  inc, doub = 1, 0
  for i in range(len(x) - 1):
    if x[i] > x[i + 1]:
      inc = 0
      break
  else:
    for c in s:
      if x.count(c) == 2:
        doub = 1
        break
  return inc and doub

for x in range(r[0], r[1] + 1):
  p1 += check_p1(x)
  p2 += check_p2(x)
print(p1)
print(p2)