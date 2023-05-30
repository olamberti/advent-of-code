# Init:
w, t = 25, 6
sif = [int(x) for x in open('08.txt').read()]

# Create layers and picture:
pic = [[2 for x in range(w)] for y in range(t)]
layers, M = [], w * t

while sif:
  layer, pixels = [], [0, 0, 0]
  for y in range(t):
    row = []
    for x in range(w):
      d = sif.pop(0)
      row.append(d)
      pixels[d] += 1
      if pic[y][x] == 2 and d != 2: pic[y][x] = d
    layer.append(row)
  layers.append(layer)
  if pixels[0] < M:
    M = pixels[0]
    n1, n2 = pixels[1], pixels[2]

print(n1 * n2)

for r in pic:
  row = ''
  for c in r: row += '█' if c == 1 else ' '
  print(row)