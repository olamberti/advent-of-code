# Create grid:
emp, occ = set(), set()
dirs = [-1 - 1j, -1, -1 + 1j, -1j, 1j, 1 - 1j, 1, 1 + 1j]
for r, line in enumerate(open('d11.txt').read().splitlines()):
  for c, char in enumerate(line):
    if char == 'L': emp.add(r + c * 1j)

def printmap():
  for i in range(r + 1):
    p = ''
    for j in range(c + 1):
      if i + j * 1j in occ: p += '#'
      elif i + j * 1j in emp: p += 'L'
      else: p += '.'
    print(p)
  print(' ')  
      
# P1 rules:
def nextround_p1(emp, occ):
  emp_, occ_ = set(), set()
  for s in emp:
    for d in dirs:
      if s + d in occ: 
        emp_.add(s)
        break
    else: occ_.add(s)
  for s in occ:
    t = 0
    for d in dirs:
      if s + d in occ: t += 1
    if t >= 4: emp_.add(s)
    else: occ_.add(s)
  return emp_, occ_

# P1 sim.:
emp_1, occ_1 = emp, occ
while True:
  old = occ_1
  emp_1, occ_1 = nextround_p1(emp_1, occ_1)
  if old == occ_1:
    break
print(len(occ_1))

# P2 rules:
def nextround_p2(emp, occ):
  emp_, occ_ = set(), set()
  for s in emp:
    for d in dirs:
      n = s + d
      while n not in occ and n not in emp and 0 <= n.real <= r and 0 <= n.imag <= c: 
        n += d
      if n in occ: 
        emp_.add(s)
        break
    else: occ_.add(s)
  for s in occ:
    t = 0
    for d in dirs:
      n = s + d 
      while n not in occ and n not in emp and 0 <= n.real <= r and 0 <= n.imag <= c:
        n += d
      if n in occ: t += 1
    if t >= 5: emp_.add(s)
    else: occ_.add(s)
  return emp_, occ_

# P2 sim:
emp_2, occ_2 = emp, occ
while True:
  old = occ_2
  emp_2, occ_2 = nextround_p2(emp_2, occ_2)
  if old == occ_2:
    break
print(len(occ_2))