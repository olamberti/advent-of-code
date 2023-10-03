# Read data
with open("d03.txt", "r") as input:
  data = input.read().splitlines()

# Decimal calculator
def decimal(num):
  ans = 0
  power = 0
  num.reverse()
  for i in num:
    ans += i * pow(2,power)
    power += 1
  return ans

# Find gamma and epsilon ratings
def find_gamma(lst):
  count = [0 for x in lst[0]]
  length = len(lst)
  for line in lst:
    for i, char in enumerate(line):
      if char == "1":
        count[i] += 1
  gamma = [int(2 * x / length) for x in count]
  epsilon = [abs(x - 1) for x in gamma]
  return gamma, epsilon

# Find oxygen rating
oxygen = data
pos = 0
while len(oxygen) != 1:
  new_oxygen = []
  new_gamma, new_epsilon = find_gamma(oxygen)
  for elem in oxygen:
    if int(elem[pos]) == new_gamma[pos]:
      new_oxygen.append(elem)
  oxygen = new_oxygen
  pos += 1
oxygen = [int(x) for x in oxygen[0]]

# Find CO2 rating  
co2 = data
pos = 0
while len(co2) != 1:
  new_co2 = []
  new_gamma, new_epsilon = find_gamma(co2)
  for elem in co2:
    if int(elem[pos]) == new_epsilon[pos]:
      new_co2.append(elem)
  co2 = new_co2
  pos += 1
co2 = [int(x) for x in co2[0]]

# Solution
gamma_1, epsilon_1 = find_gamma(data)
solution_1 = decimal(gamma_1) * decimal(epsilon_1)
solution_2 = decimal(oxygen) * decimal(co2)
print(solution_1)
print(solution_2)