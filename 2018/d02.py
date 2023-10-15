# P1
boxes, twos, threes = set(), 0, 0
for box in open('d02.txt').read().splitlines():
    # P1
    letters, two, three = {}, False, False
    for c in box:
        if c not in letters: letters[c] = 1
        else: letters[c] += 1
    for n in letters.values():
        if n == 2: two = True
        elif n == 3: three = True
    if two: twos += 1
    if three: threes += 1
    # P2
    for b in boxes:
        diff = 0
        for i, c in enumerate(b):
            if box[i] == c: continue
            diff += 1
        if diff == 1:
            protos = []
            for i, c in enumerate(b):
                 if box[i] == c: protos.append(c)
    boxes.add(box)
print(twos * threes)
print(''.join(protos))