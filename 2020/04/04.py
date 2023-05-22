def check(e):
  f, v = e[0], e[1]

  if f == 'byr':
    if v.isnumeric() and len(v) == 4:
      v = int(v)
      if 1920 <= v <= 2002: return True

  elif f == 'iyr':
    if v.isnumeric() and len(v) == 4:
      v = int(v)
      if 2010 <= v <= 2020: return True
  
  elif f == 'eyr' and len(v) == 4:
    if v.isnumeric():
      v = int(v)
      if 2020 <= v <= 2030: return True 
        
  elif f == 'hgt':
    h, u = '', ''
    for c in v:
      if c.isnumeric(): h += c
      else: u += c
    h = int(h)
    if u == 'cm' and (150 <= h <= 193): return True
    elif u == 'in' and (59 <= h <= 76): return True

  elif f == 'hcl':
    if v[0] == '#' and len(v) == 7:
      v = v[1:]
      for c in v:
        if c in 'abcdef' or c.isnumeric(): continue
        else: break
      else: return True
        
  elif f == 'ecl':
    if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return True

  elif f == 'pid':
    if v.isnumeric() and len(v) == 9: return True

  elif f == 'cid': return True
    
  return False

ps, n, v1, v2 = [[]], 0, 0, 0
inp = open('04.txt').read().splitlines()
for i, line in enumerate(inp, 1):
  if line != '':
    p = [[e.split(':')[0], e.split(':')[1]] for e in line.split()]
    ps[n].extend(p)
  if line == '' or i == len(inp):
    f = 0
    for e in ps[n]:
      if e[0] != 'cid': f += 1
    if f == 7:
      v1 += 1
      for e in ps[n]:
        if check(e): continue
        else: break
      else: v2 += 1
    ps.append([])
    n += 1
print(v1)
print(v2)