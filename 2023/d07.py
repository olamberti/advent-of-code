from collections import defaultdict

labels = ['23456789TJQKA', 'J23456789TQKA']

def encode(hand, p2 = False):
    counts, id, js = defaultdict(int), [], 0
    if not p2:
        for card in hand:
            counts[card] += 1
            id.append(labels[0].index(card))
        counts = sorted(counts.values(), reverse=True)
    if p2:
        for card in hand:
            if card == 'J': js += 1
            else:
                counts[card] += 1
            id.append(labels[1].index(card))
        if js == 5: counts = [5, 0]
        else:
            counts = sorted(counts.values(), reverse=True)
            counts[0] += js
    if counts[0] == 5: id =  [7] + id
    elif counts[0] == 4: id =  [6] + id
    elif counts[0] == 3 and counts[1] == 2: id =  [5] + id
    elif counts[0] == 3 and counts[1] == 1: id =  [4] + id
    elif counts[0] == 2 and counts[1] == 2: id =  [3] + id
    elif counts[0] == 2 and counts[1] == 1: id =  [2] + id
    else: id =  [1] + id
    return tuple(id)

ranks_1, ranks_2, bids = [], [], {}
for line in open('d07.txt').read().splitlines():
    hand, bid = line.split()
    bids[hand] = int(bid)
    ranks_1.append((encode(hand), hand))
    ranks_2.append((encode(hand, True), hand))

ranks_1 = sorted(ranks_1)
ranks_2 = sorted(ranks_2)

p1, p2 = 0, 0
for i, item in enumerate(zip(ranks_1, ranks_2), 1):
    p1 += i * bids[item[0][1]]
    p2 += i * bids[item[1][1]] 
print(p1)
print(p2)