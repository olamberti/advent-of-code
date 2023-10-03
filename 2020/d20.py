# Tile class:
class Tile():
  
  def __init__(self, id, pic):
    self.id = id
    self.pic = pic
    self.typ = None

  def plot(self):
    print(f'Tile {self.id}:')
    for line in self.pic: print(line)
    print('')
  
  def getedges(self):
    e, w = '', ''
    for i, line in enumerate(self.pic):
      if i == 0: n = line[:]
      elif i == len(self.pic) - 1: s = line[::-1]
      e += line[-1]
      w += line[0]
    return [n, e, s, w[::-1]]

  def flip(self):
    pic_ = []
    for line in self.pic:
      pic_.append(line[::-1])
    self.pic = pic_

  def rot90(self):
    pic_ = []
    for i in range(len(self.pic)):
      line_ = ''
      for line in self.pic: line_ += line[i]
      line_ = line_[::-1]
      pic_.append(line_)
    self.pic = pic_

  def removeborders(self):
    pic_ = []
    for i in range(1, len(self.pic) - 1):
      pic_.append(self.pic[i][1:-1])
    return pic_
      
#1 Input processing:
tiles, edges, pic = [], {}, []
for line in open('d20.txt').read().splitlines():
  psize = len(line)
  if 'Tile' in line: id = int(line.split()[1].strip(':'))
  elif line == '': continue
  else: pic.append(line)
  if len(pic) == psize:
    tile, pic = Tile(id, pic), []
    tiles.append(tile)
    for i, edge in enumerate(tile.getedges()):
      if edge in edges: edges[edge].append([id, i, False])
      else: edges[edge] = [[id, i, False]]
    tile.flip()
    for i, edge in enumerate(tile.getedges()):
      if edge in edges: edges[edge].append([id, i, True])
      else: edges[edge] = [[id, i, True]]
    tile.flip()
    
#2 Determine tile types based on edge counts:
p1 = 1
for i, tile in enumerate(tiles):
  uniq = 0
  for edge in tile.getedges():
    if len(edges[edge]) == 1: uniq += 1
  if uniq == 2:
    tiles[i].typ = 'c'
    p1 *= tile.id
  elif uniq == 1: tiles[i].typ = 's'
  else: tiles[i].typ = 'm'
print(p1)

#3 Build up grid:
grid, size = [[]], int(len(tiles) ** 0.5)

#3.1 Get first corner tile and rotate it to be top left:
for i, tile in enumerate(tiles):
  if tile.typ == 'c':
    tiles.pop(i)
    break
for _ in range(3):
  ec = []
  for edge in tile.getedges():
    ec.append(len(edges[edge]))
  if ec == [1, 2, 2, 1]: break
  else: tile.rot90()
grid[0].append(tile)

#3.2 Build up grid from left to right and from top to bottom:
r, c = 0, 1
while tiles:
  if c > 0:
    my_tile, tar = grid[r][c - 1], 3
    my_edge = my_tile.getedges()[1]
  else:
    my_tile, tar = grid[r - 1][c], 0
    my_edge = my_tile.getedges()[2]
  
  pair = edges[my_edge]
  my_id = my_tile.id
  for data in pair:
    if data[0] != my_id: id, e, f = data

  for i, tile in enumerate(tiles):
    if tile.id == id:
      if not f: tile.flip()
      while tile.getedges()[tar] != my_edge[::-1]: tile.rot90()
      grid[r].append(tile)
      tiles.pop(i)

  c = (c + 1) % size
  if c == 0:
    r += 1
    if r != size: grid.append([])

#4 Create image from grid:
bigpic, water = [], 0
for r in range(size):
  for l in range(psize - 2):
    line = ''
    for c in range(size):
      pix = grid[r][c].removeborders()[l]
      line += pix
      water += pix.count('#')
    bigpic.append(line)
img = Tile(0, bigpic)

#5 Create sea monster:
sm, sl, sh = set(), 0, 0
for r, line in enumerate(open('sea_monster.txt').read().splitlines()):
  for c, ch in enumerate(line):
    if ch == '#':
      sm.add((r, c))
      sl, sh = max(c, sl), max(r, sh)

#6 Scan the picture:
n, size, rots = 0, len(bigpic), 0
while True:
  for i in range(size - sh):
    for j in range(size - sl):
      for p in sm:
        x, y = i + p[0], j + p[1]
        if img.pic[x][y] != '#': break
      else: n += 1
  if n > 0: break
  elif rots < 4: 
    img.rot90()
    rots += 1
  else:
    img.flip()
    rots = 0
print(water - n * len(sm))