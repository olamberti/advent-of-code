def encode(hand, part2 = False):
    labels, counts, value = 'X23456789TJQKA', {}, []
    if part2: hand = hand.replace('J', 'X')
    for card in labels:
        counts[card] = hand.count(card)
    jokers = counts.pop('X')
    counts = sorted(counts.values(), reverse=True)[:2]
    counts[0] += jokers
    value.append([[1,1],[2,1],[2,2],[3,1],[3,2],[4,1],[5,0]].index(counts))
    for card in hand:
        value.append(labels.index(card))   
    return tuple(value)

ranks_1, ranks_2 = [], []
for line in open('d07.txt'):
    hand, bid = line.split()
    ranks_1.append((encode(hand), int(bid)))
    ranks_2.append((encode(hand, True), int(bid)))
ranks_1 = sorted(ranks_1)
ranks_2 = sorted(ranks_2)

p1, p2 = 0, 0
for i, item in enumerate(zip(ranks_1, ranks_2), 1):
    p1 += i * item[0][1]
    p2 += i * item[1][1]
print(p1)
print(p2)