input = open('d04.txt').read().splitlines()
cards, p1 = [1] * len(input), 0

for i, line in enumerate(input):
    wins, have = [set(x.split()) for x in line.split(': ')[1].split(' | ')]
    matches = len(wins & have)
    for n in range(matches):
        cards[i + 1 + n] += cards[i]
    p1 += 2 ** (matches - 1) if matches > 0 else 0

print(p1)
print(sum(cards))