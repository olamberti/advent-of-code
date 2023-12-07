def strength(hand, part = 1):
    labels = 'X23456789TJQKA'
    if part == 2: hand = hand.replace('J', 'X')
    values = [labels.index(card) for  card in hand]
    counts = {card: hand.count(card) for card in labels}
    jokers = counts.pop('X')
    counts = sorted(counts.values(), reverse=True)[:2]
    counts[0] += jokers
    typ = ([1,1],[2,1],[2,2],[3,1],[3,2],[4,1],[5,0]).index(counts)
    return tuple([typ, *values])

for part in (1, 2):
    hands = []
    for line in open('d07.txt'):
        hand, bid = line.split()
        hands.append((strength(hand, part), int(bid)))
    hands = sorted(hands)
    total = 0
    for i, (_, bid) in enumerate(hands, 1):
        total += i * bid
    print(total)