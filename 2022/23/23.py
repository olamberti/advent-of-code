# Read input:
elves = set()
for x, line in enumerate(open('23.txt'), 1):
  for y, char in enumerate(line, 1):
    if char == '#': elves.add(x + y * 1j)

# Initialization:
neighbours = [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j]
poles = {-1: [-1 - 1j, -1, -1 + 1j],   # north
          1: [1 - 1j, 1, 1 + 1j],      # south
        -1j: [-1 - 1j, -1j, 1 - 1j],   # west
         1j: [-1 + 1j, 1j, 1 + 1j]}    # east
moves = [-1, 1, -1j, 1j]
    
# Dance 10 rounds:
step = 0
while True:
  proposals, invalid = set(), set()
  
  for elf in elves:
    if all(elf + dir not in elves for dir in neighbours):
      continue
    for move in moves:
      if all(elf + dir not in elves for dir in poles[move]):
        plan = elf + move
        if plan not in proposals: proposals.add(plan)
        elif plan not in invalid: invalid.add(plan)
        break

  new_elves = set(elves)
  
  for elf in elves:
    if all(elf + dir not in elves for dir in neighbours):
      continue
    for move in moves:  
      if all(elf + dir not in elves for dir in poles[move]):
        plan = elf + move
        if plan not in invalid:
          new_elves.remove(elf)
          new_elves.add(plan)
        break
  
  moves.append(moves.pop(0))
  step += 1
        
  # Part 2:
  if new_elves == elves:
    print(step)
    break
    
  elves = new_elves        
  
  # Part 1:
  if step == 10:
    mx = int(min([elf.real for elf in elves]))
    my = int(min([elf.imag for elf in elves]))
    Mx = int(max([elf.real for elf in elves]))
    My = int(max([elf.imag for elf in elves]))
    solution_1 = (Mx - mx + 1) * (My - my + 1) - len(elves)
    print(solution_1)