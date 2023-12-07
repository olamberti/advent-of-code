def encode(hand, part2 = False):
    labels, value = 'X23456789TJQKA', []
    if part2: hand = hand.replace('J', 'X')
    counts = {card: hand.count(card) for card in labels}
    jokers = counts.pop('X')
    counts = sorted(counts.values(), reverse=True)[:2]
    counts[0] += jokers
    value.append([[1,1],[2,1],[2,2],[3,1],[3,2],[4,1],[5,0]].index(counts))
    for card in hand:
        value.append(labels.index(card))   
    return tuple(value)

hands_1, hands_2 = [], []
for line in open('d07.txt'):
    hand, bid = line.split()
    hands_1.append((encode(hand), int(bid)))
    hands_2.append((encode(hand, True), int(bid)))
hands_1 = sorted(hands_1)
hands_2 = sorted(hands_2)

p1, p2 = 0, 0
for i, (play_1, play_2) in enumerate(zip(hands_1, hands_2), 1):
    p1 += i * play_1[1]
    p2 += i * play_2[1]
print(p1)
print(p2)