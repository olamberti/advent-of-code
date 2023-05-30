# User inputs & class definition:
my_input = '11.txt'
part = 2

class monkey():
  def __init__(self, items, operation, divisor, if_true, if_false):
    self.items, self.operation, self.divisor = items, operation, divisor
    self.if_true, self.if_false = if_true, if_false
    self.inspected = 0
  def inspect_item(self, old):
    self.inspected += 1
    new = eval(self.operation) // 3 if part == 1 else eval(self.operation) 
    return new
  def play_round(self):
    for item in self.items:
      item = self.inspect_item(item) # monkey inspection
      target = self.if_true if item % self.divisor == 0 else self.if_false # choosing target
      monkeys[target].items.append(item % smallest_common_factor) # to reduce number sizes
    self.items = []

# Input read in:
with open(my_input,'r') as input:
  text = input.read().splitlines()
pos, monkeys, divisors = 0, [], []
while pos < len(text):
  my_items = [int(x) for x in text[pos + 1][18:].split(',')]
  my_operation, my_divisor = text[pos + 2][19:], int(text[pos + 3].split()[-1])
  my_if_true, my_if_false = int(text[pos + 4].split()[-1]), int(text[pos + 5].split()[-1])
  if my_divisor not in divisors:
    divisors.append(my_divisor)
  monkeys.append(monkey(my_items, my_operation, my_divisor, my_if_true, my_if_false))
  pos += 7

# Calculate smallest common factor of divisors:
smallest_common_factor = 1
for divisor in divisors:
  smallest_common_factor = smallest_common_factor * divisor
  
# Play the rounds:
rounds = 20 if part == 1 else 10000
for round in range(rounds):
  for my_monkey in monkeys:
    my_monkey.play_round()

# Calculate scores:
inspect_numbers = []
for my_monkey in monkeys:
  inspect_numbers.append(my_monkey.inspected)
sorted_inspect_numbers = sorted(inspect_numbers)
print(f'Part {part}: {sorted_inspect_numbers[-1] * sorted_inspect_numbers[-2]}')