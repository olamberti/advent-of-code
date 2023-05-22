black, dirs = set(), {'e':2, 'se':1+1j, 'ne':1-1j, 'w':-2, 'sw':-1+1j, 'nw':-1-1j}

# P1
for line in open('24.txt').read().splitlines():
  line = line.replace('e', 'e ')
  line = line.replace('w', 'w ')
  tile = 0
  for move in line.split():
    tile += dirs[move]
  if tile in black: black.remove(tile)
  else: black.add(tile)
print(len(black))

# P2
def adj(tile):
  ad = []
  for move in dirs.values(): ad.append(tile + move)
  return ad

def border(tiles):
  bord = set()
  for tile in tiles:
    for ad in adj(tile):
      if ad in tiles: continue
      else: bord.add(ad)
  return bord

white = border(black)
for _ in range(100):
  black_, white_ = set(), set()
  
  for tile in black:
    n = 0
    for ad in adj(tile):
      if ad in black: n += 1
    if n == 1 or n == 2: black_.add(tile)
  
  for tile in white:
    n = 0
    for ad in adj(tile):
      if ad in black: n += 1
    if n == 2: black_.add(tile)

  black = black_
  white = border(black)

print(len(black))