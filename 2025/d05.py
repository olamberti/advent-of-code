ranges, ids = open('d05.txt').read().split('\n\n')
ranges = [tuple(map(int, r.split('-'))) for r in ranges.split('\n')]
ids = [int(i) for i in ids.split('\n')]

p1 = 0
for id in ids:
    for r in ranges:
        if r[0] <= id <= r[1]:
            p1 += 1
            break
print(p1)

merged = []
ranges.sort()
for r in ranges:
    if not merged or merged[-1][1] < r[0]:
        merged.append(r)
    else:
        merged[-1] = (merged[-1][0], max(merged[-1][1], r[1]))

p2 = 0
for m in merged:
    p2 += m[1] - m[0] + 1
print(p2)