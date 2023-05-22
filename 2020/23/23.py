cups= [int(x) for x in '394618527'] # example: '389125467' & own: '394618527'
chain, n = {}, len(cups)
for i, cup in enumerate(cups): chain[cup] = cups[(i + 1) % n]

def shuffle(cc, chain, n):
  pickup, nc = [], chain[cc]
  for __ in range(3):
    pickup.append(nc)
    nc = chain[nc]
  chain[cc] = nc

  dc = cc - 1 or n
  while dc in pickup: dc = dc - 1 or n
  chain[dc], chain[pickup[-1]] = pickup[0], chain[dc]
  cc = chain[cc]

  return cc, chain
  
# Part 1:
cc = cups[0]
for _ in range(100): cc, chain = shuffle(cc, chain, n)

cc, p1 = 1, ''
for i in range(1, n):
  p1 += str(chain[cc])
  cc = chain[cc]
print(p1)

# Part 2:
N = 1_000_000
for i, cup in enumerate(cups): chain[cup] = cups[(i + 1) % n]
for i in range(n + 1, N): chain[i] = i + 1
chain[cups[-1]], chain[N] = n + 1, cups[0]

cc = cups[0]
for _ in range(10_000_000): cc, chain = shuffle(cc, chain, N)

cc, p2 = 1, []
for _ in range(2):
  p2.append(chain[cc])
  cc = chain[cc]
print(p2[0] * p2[1])