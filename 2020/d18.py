def calc(line, p):
  
  l = len(line)
  while '(' in line:
    i1, n = line.index('('), 1
    for i2 in range(i1 + 1, l):
        if line[i2] == '(': n += 1
        elif line[i2] == ')':
          n -= 1
          if n == 0: break
    v = calc(line[i1 + 1: i2], p)
    line = line.replace(line[i1: i2 + 1], str(v))
    l = len(line)

  if p == 1:
    res, op = 0, '+'
    for c in line.split():
      if c.isnumeric():
        v = int(c)
        if op == '+': res += v
        else: res *= v
      else: op = c

  elif p == 2:
    while '+' in line:
      lp = line.split()
      i = lp.index('+')
      a, b = int(lp[i - 1]), int(lp[i + 1])
      v = a + b
      lp.pop(i-1)
      lp.pop(i-1)
      lp.pop(i-1)
      lp.insert(i - 1, str(v))
      line = ' '.join(lp)
      l = len(line)

    res, op = 0, '+'
    for c in line.split():
      if c.isnumeric():
        v = int(c)
        if op == '+': res += v
        else: res *= v
      else: op = c
        
  return res
  
# P1:
p1, p2 = 0, 0
for l in open('d18.txt').read().splitlines():
  p1 += calc(l, 1)
  p2 += calc(l, 2)
print(p1)
print(p2)