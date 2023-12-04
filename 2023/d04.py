input = open('d04.txt').read().splitlines()
numbers, p1, p2 = [1] * len(input), 0, 0

for i, line in enumerate(input):
    wins, have = [set(x.split()) for x in line.split(': ')[1].split(' | ')]
    matches = len(wins & have)
    for n in range(matches):
        numbers[i + 1 + n] += numbers[i]
    p1 += 2 ** (matches - 1) if matches > 0 else 0
    p2 += numbers[i]

print(p1); print(p2)