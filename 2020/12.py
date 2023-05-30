d = {'E':1, 'W':-1, 'N':1j, 'S':-1j, 'R':-1j, 'L':1j}

def nav(pos, ref, com, val, prt):
  if com in 'RL': ref *= d[com] ** (val // 90)
  elif com == 'F': pos += val * ref
  elif prt == 1: pos += val * d[com]
  else: ref += val * d[com]
  return pos, ref

p1, f, p2, wp = 0, 1, 0, 10 + 1j
for i in open('12.txt'):
  c, v = i[0], int(i[1:])
  p1, f  = nav(p1, f, c, v, 1)
  p2, wp = nav(p2, wp, c, v, 2)

print(int(abs(p1.real) + abs(p1.imag)))
print(int(abs(p2.real) + abs(p2.imag))) 