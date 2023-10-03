import itertools

data = {}
for i, x in enumerate(open('d17.txt').readlines()):
    data[chr(i + 97)] = int(x)

p1, p2, minN = 0, 0, 999
for r in range(1, len(data) + 1):
    for combo in itertools.combinations(''.join([i for i in data.keys()]), r):
        vol = 0
        for c in combo: vol += data[c]
        if vol == 150:
            p1 += 1
            if len(combo) < minN:
                minN = len(combo)
                p2 = 1
            elif len(combo) == minN: p2 += 1        
print(p1)
print(p2)