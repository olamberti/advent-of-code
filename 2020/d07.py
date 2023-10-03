# Input parsing:
inp = open('d07.txt').read().splitlines()
rules = {}
for line in inp:
  line = line.split(' contain ')
  bag, con = line[0], line[1]
  bag = bag.split()[0] + bag.split()[1]
  if con.split(',')[0][0].isnumeric():
    con = [[int(b.split()[0]), b.split()[1] + b.split()[2]] for b in con.split(',')]
  else: con = []
  rules[bag] = con

# Part 1
def checkbag(bag):
  con = rules[bag]
  for n, b in con:
    if b == 'shinygold' or checkbag(b): return True
  return False  

num = 0
for bag in rules:
  if bag != 'shinygold' and checkbag(bag): num += 1
print(num)

# Part 2:
def countbags(bag):
  con, num = rules[bag], 0
  for n, b in con:
    num += n + n * countbags(b)
  return num
  
print(countbags('shinygold'))