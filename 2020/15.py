inp = [int(x) for x in open('15.txt').read().split(',')]
last, mem = inp[-1], {x: [None, i] for i, x in enumerate(inp, 1)}

t = len(inp)
while t < 30_000_000:
  t += 1
     
  last = 0 if not mem[last][0] else mem[last][1] - mem[last][0]

  if last in mem:
    mem[last][0] = mem[last][1]
    mem[last][1] = t
  else:
    mem[last] = [None, t]

  if t == 2020: print(last)
    
print(last)