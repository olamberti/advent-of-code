s = set()
for l in open('d05.txt'):
  r, c = l[0:7], l[7:10]
  row, col = 0, 0
  for i, b in enumerate(r[::-1]):
    if b == 'B': row += 2 ** i
  for i, b in enumerate(c[::-1]):
    if b == 'R': col += 2 ** i
  id = row * 8 + col
  s.add(id)
print(max(s))

for x in range(min(s), max(s) + 1):
  if x not in s:
    print(x)
    break