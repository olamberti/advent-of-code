# Read input
with open('d06.txt', 'r') as input:
  fishes = [int(x) for x in input.read().split(',')]

# Simulation:
fish_numbers = [fishes.count(x) for x in range(9)]
for day in range(256):
  fish_numbers.append(fish_numbers[0])
  fish_numbers[7] += fish_numbers[0]
  fish_numbers.pop(0)
  if day + 1 == 80:
    print(sum(fish_numbers))
print(sum(fish_numbers))    