# Read input:
with open('17.txt', 'r') as input:
  jets = input.read().strip()
jets_length = len(jets)

# Functions:
def spawn_rock(rock, height): # moves rock to the spawn position
  new_rock = [x + 2 + height*1j for x in rock]
  return new_rock

def pushed_by_jet(rock, direction, block): # wind effect
  dir = 1 if direction == '>' else -1
  new_rock = [x + dir for x in rock]
  if any([((0 > x.real) or (x.real > 6)) for x in new_rock]): # rock would hit wall
    return rock
  elif not set(new_rock).isdisjoint(block): # rock would hit block
    return rock
  else:
    return new_rock

def fall(rock, block): # gravity
    falling = True
    new_rock = [x - 1j for x in rock]
    if not set(new_rock).isdisjoint(block): # rock would hit block
      falling = False
      for piece in rock:
        blocks.add(piece)
      return None, falling
    else:
      return new_rock, falling

def printmap(rock = None): # prints map for debugging, not used
  for j in range(block_height + 8, -1, -1):  
    line = ''
    for i in range(7):
      cell = i + j*1j
      if (rock != None and cell in rock):
        next_char = '@'
      elif j == 0:
        next_char = '-'
      elif cell in blocks:
        next_char = '#'
      else:
        next_char = '.'
      line += next_char
    print(line)
      
# Initialize:                        # set such no correction for spawn rule is necessary
rocks = [[0, 1, 2, 3],               # -
        [1, 0+1j, 1+1j, 2+1j, 1+2j], # +
        [0, 1, 2, 2+1j, 2+2j],       # ⅃
        [0, 0+1j, 0+2j, 0+3j],       # |
        [0, 1, 0+1j, 1+1j]]          # □
blocks = set()
for i in range(7):  
  blocks.add(i) # spawn  floor
  
num_rocks, step, block_height = 0, 0, 0
is_rock_falling = False
  
# Part 1 - Run tetris:
data = [] # will store block height as the function of fallen rocks (index)
while num_rocks <= 2500: # to make sure we catch the pattern
  if not is_rock_falling: # new rock spawns
    falling_rock = spawn_rock(rocks[num_rocks % 5], block_height + 4)
    is_rock_falling = True
    num_rocks += 1
    data.append(block_height)
  falling_rock = pushed_by_jet(falling_rock, jets[step % jets_length], blocks) # rock is pushed by jet
  falling_rock, is_rock_falling = fall(falling_rock, blocks)  # gravity
  if not is_rock_falling: # rock came to rest
    block_height = int(max([x.imag for x in blocks]))
    if num_rocks  == 2022:
      solution_1 = block_height
  step += 1
print(solution_1)

# Part 2 - Search correlation and use it for calculation:
# Idea is that after a while the rock pattern repeats itself, which will be refelcted by the height increase
# We cut the first X rocks (cut_point) for the transient period, after we assume the pattern is periodic.
# Then try to use some sort of auto-correlation on the height difference to calculate the period.
N_rocks = 1000000000000
cut_point = 600
data_cut = data[(cut_point + 1):] 
diff = [(data_cut[i+1] - data_cut[i]) for i in range(len(data_cut) - 2)] # differential of heights
corr = 1
corr_found = False
while not corr_found:
  test = zip(diff, diff[corr:])
  if all([(x[1] - x[0]) == 0 for x in test]):
    corr_found = True
  else:
    corr += 1
diff_pattern = diff[:corr]
solution_2 = data[cut_point] + ((N_rocks - cut_point) // corr) * sum(diff_pattern) + sum(diff_pattern[:(N_rocks - cut_point) % corr])
print(solution_2)