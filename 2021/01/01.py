with open("01.txt") as input:
  text = input.read()
data = [int(x) for x in text.splitlines()]
number_of_increase = 0
number_of_avg_increase = 0
for i in range(len(data) - 1):
  if data[i] < data[i + 1]:
    number_of_increase += 1
  if (i < len(data) - 3) and (data[i] < data[i + 3]):
    number_of_avg_increase += 1
print(number_of_increase)
print(number_of_avg_increase)