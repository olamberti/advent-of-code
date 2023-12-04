input = open('d04.txt').read().splitlines()
numbers, p1, p2 = [1] * len(input), 0, 0

for i, line in enumerate(input):
    wins, have = line.split(': ')[1].split(' | ')
    matches = len(set(wins.split()) & set(have.split()))
    score = pow(2, matches - 1) if matches > 0 else 0
    for c in range(1, matches + 1):
        if i + c < len(numbers): numbers[i + c] += numbers[i]
    p1 += score
    p2 += numbers[i]

print(p1)
print(p2)