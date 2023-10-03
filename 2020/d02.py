val1, val2 = 0, 0
for l in open('d02.txt'):
  r, c, p = l.split()
  r, c = [int(x) for x in r.split('-')], c[0]
  if r[0] <= p.count(c) <= r[1]: val1 += 1
  if (p[r[0] - 1] == c) ^ (p[r[1] - 1] == c): val2 += 1
print(val1)
print(val2)