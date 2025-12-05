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

# part 2 missing