# Read input
cons = {}

for line in open('12.txt', 'r'):
  ab = line.strip().split('-')
  a, b = ab[0], ab[1]
  if a not in cons: cons[a] = []
  if b not in cons: cons[b] = []
  if b != 'start': cons[a].append(b)
  if a != 'start': cons[b].append(a)

# Part 1
paths = []

def explore(path):
  caves = path.split('-')
  pos = caves[-1]
  for cave in cons[pos]:
    if cave == 'end': paths.append(path + '-end')
    elif cave.isupper(): explore(path + '-' + cave)
    elif cave.islower and cave not in path: explore(path + '-' + cave)

explore('start')
print(len(paths))

# Part 2
paths = []

def explore2(path, twice):
  caves = path.split('-')
  pos = caves[-1]
  for cave in cons[pos]:
    if cave == 'end': paths.append(path + '-end')
    elif cave.isupper(): explore2(path + '-' + cave, twice)
    elif cave.islower and cave not in path: explore2(path + '-' + cave, twice)
    elif cave.islower and not twice: explore2(path + '-' + cave, True)

explore2('start', False)
print(len(paths))