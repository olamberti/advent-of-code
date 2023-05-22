report = [int(x) for x in open('01.txt').read().splitlines()]

for x in report:
  if 2020 - x in report:
    print(x * (2020 - x))
    break

for i, x in enumerate(report):
  rest = report[i + 1:]
  for y in rest:
    if 2020 - x - y in rest:
      print(x * y * (2020 - x - y))
      break