# P1:
total = sum([int(x) // 3 - 2 for x in open('01.txt').read().splitlines()])
print(total)

# P2:
total = 0
def fuel(mass):
  return mass // 3 - 2

for mass in open('01.txt').read().splitlines():
  f = fuel(int(mass))
  while f > 0:
    total += f
    f = fuel(f)
print(total)