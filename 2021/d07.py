# Read input:
with open('d07.txt', 'r') as input:
  positions = [int(x) for x in input.read().split(',')]

# Part 1 - Calculate median:
import statistics
target_1 = int(statistics.median(positions))
fuel_1 = 0
for pos in positions:
  fuel_1 += abs(target_1 - pos)
print(fuel_1)

# Part 2 - Calculate average:
avg = int(statistics.mean(positions))
targets_2 = [avg - 1, avg, avg + 1]
min_fuels = []
for target in targets_2:
  fuel_2 = 0
  for pos in positions:
    distance = abs(target - pos)
    fuel_2 += (distance * (distance + 1) ) // 2
  min_fuels.append(fuel_2)
print(min(min_fuels))