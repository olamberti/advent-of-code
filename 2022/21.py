def make_yell(name):
  if type(monkeys[name]) != str:
    return monkeys[name]
  else:
    m1, op, m2 = [monkeys[name].split()[i] for i in range(3)]
    n1, n2 = str(make_yell(m1)), str(make_yell(m2))
    return eval(n1 + op + n2)

# Read in data:
monkeys = {}
for line in open('21.txt'):
  name, yell = line.split(':')[0], line.split(':')[1].strip()
  if yell.isnumeric(): monkeys[name] = int(yell)
  else: monkeys[name] = yell

# Part 1:
solution_1 = round(make_yell("root"))
print(solution_1)

# Part 2:
monkey_1, monkey_2 = [monkeys['root'].split()[i] for i in [0, 2]]
y1 = make_yell(monkey_1) - make_yell(monkey_2)

dx = solution_1 * 10
x1 = monkeys['humn']
monkeys['humn'] = x1 + dx
y2 = make_yell(monkey_1) - make_yell(monkey_2)

shift = - (y1 * dx) / (y2 - y1)
solution_2 = round(x1 + shift)
print(solution_2)