def gen_a2():
  a2 = set()
  for i in range(ord('a'), ord('z') + 1):
    a2.add(chr(i))
  return a2

q1, q2, a1, a2 = 0, 0, set(), gen_a2()
inp = open('d06.txt').read().splitlines()
for i, line in enumerate(inp, 1):
  if line != '':
    ac = set()
    for a in line:
      ac.add(a)
      a1.add(a)
    a2 = a2 & ac
  if line == '' or i == len(inp):
    q1 += len(a1)
    q2 += len(a2)
    a1, a2 = set(), gen_a2()
print(q1)
print(q2)