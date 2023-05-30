# Read input:
blizzards = (set(), set(), set(), set())           # storing the four different blizz types '^v<>'
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (0, 0))  # corresponding movement directions

height, width = 0, 0
for r, line in enumerate(open('24.txt', 'r')):
  line = line.strip()
  height += 1
  width = len(line)    
  for c, char in enumerate(line):
    if char in '^v<>':
      blizzards['^v<>'.find(char)].add((r - 1, c - 1))
      
height, width = height - 2, width - 2
      
# Route finding with BFS:
start, end = (-1, 0), (height, width - 1) 
time, level, out = 0, 1, False
front = set()
front.add((-1, 0, 0))

while not out:
  reset = False
  time += 1
  
  # Calculate new blizzard positions
  new_blizzards = (set(), set(), set(), set())
  for i, typ in enumerate(blizzards):                
    for blizz in typ:
      dr, dc = dirs[i]
      new_blizzards[i].add(((blizz[0] + dr) % height, (blizz[1] + dc) % width))
  blizzards = new_blizzards

  new_front = set()
  # Check possible moves on the front:
  for r, c, t in front:
    for dr, dc in dirs:
      nr = r + dr    # new row
      nc = c + dc    # new column

      # Check goal condition:
      if (nr, nc) == end and level == 1:
        print(time)
        front = set()
        front.add((height, width - 1, time))
        reset = True
      elif (nr, nc) == start and level == 2:
        front = set()
        front.add((-1, 0, time))
        reset = True
      elif (nr, nc) == end and level == 3:
        print(time)
        out = True
        
      # Check if we are on map:
      if (nr < 0 or nc < 0 or nr >= height or nc >= width) and (nr, nc) not in (start, end):
        continue

      # Check if there is no blizzard on the tile:
      clear = True
      for group in blizzards:
        if (nr, nc) in group:
          clear = False
          break
      if clear:
        new_front.add((nr, nc, time))
          
  if reset: level += 1
  else: front = new_front