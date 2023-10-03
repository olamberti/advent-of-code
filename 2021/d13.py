dots, folds = set(), []

# Read input
is_dot = True
for line in open('d13.txt', 'r'):
  line = line.strip()
  if line == '':
    is_dot = False
    continue
  if is_dot:
    coords = line.split(',') 
    dots.add((int(coords[0]), int(coords[1])))
  else:
    todo = line.split()[2].split('=')
    folds.append([todo[0], int(todo[1])])

# Folding function
def fold(dir, val):
  global dots
  pos = 0 if dir == 'x' else 1
  new_dots = set()
  for dot in dots:
    if dot[pos] < val: new_dots.add(dot)
    elif dot[pos] == val: continue
    elif dot[pos] > val:
      x, y = dot
      if dir =='x':
        x = val - (x - val)
      else:
        y = val - (y - val)
      new_dots.add((x, y))
  dots = set(new_dots)

# Do folds:
for i in range(len(folds)):
  fold(*folds[i])
  if i == 0: print(len(dots))

# Print paper
mx, my = min(x for x, y in dots), min(y for x, y in dots)
Mx, My = max(x for x, y in dots), max(y for x, y in dots)

for y in range(my, My + 1):
  row = ''
  for x in range(mx, Mx + 1):
    if (x, y) in dots: row += '█'
    else: row += ' '
  print(row)