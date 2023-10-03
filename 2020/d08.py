# Original program
prog = open('d08.txt').read().splitlines()

# Execute program:
def run(prog):
  acc, pos, vis = 0, 0, set()
  while pos not in vis:
    vis.add(pos)
    comm, val = prog[pos].split()
    if comm == 'acc': acc += int(val)
    elif comm == 'jmp':
      pos += int(val)
      if pos == len(prog): return True, acc
      continue
    if pos == len(prog) - 1: return True, acc
    pos += 1
  return False, acc

# P1:
print(run(prog)[1])

# P2:
for i, line in enumerate(prog):
  comm, val = line.split()
  if comm == 'nop':
    prog_ = prog.copy()
    prog_[i] = 'jmp ' + val
    ended, acc = run(prog_)
    if ended:
      print(acc)
      break
  elif comm == 'jmp':
    prog_ = prog.copy()
    prog_[i] = 'nop ' + val
    ended, acc = run(prog_)
    if ended:
      print(acc)
      break