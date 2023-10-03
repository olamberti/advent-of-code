chars = [{}, {}, {}, {}, {}, {}, {}, {}]
for line in open('d06.txt').read().splitlines():
    for i, c in enumerate(line.strip()):
        if c not in chars[i]: chars[i][c] = 1
        else: chars[i][c] += 1

p1, p2 = '', ''
for d in chars:
    p1 += sorted([(v, k) for k, v in d.items()], reverse=True)[0][1]
    p2 += sorted([(v, k) for k, v in d.items()])[0][1]
print(p1)
print(p2)