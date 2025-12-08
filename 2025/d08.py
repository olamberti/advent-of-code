import math

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

data = [tuple(map(int, line.split(','))) for line in open('d08.txt')]

ds, cs = dict(), []
for i in range(len(data)):
    cs.append({data[i]})
    for j in range(i + 1, len(data)):
        ds[dist(data[i], data[j])] = {data[i], data[j]}

conn, n = sorted(ds.keys()), 0
while len(cs) > 1:
    j1, j2 = ds[conn[n]]
    n += 1
    for j, c in enumerate(cs):
        if j1 in c:
            i1 = j
            a = c
        if j2 in c:
            i2 = j
            b = c        
    if n == 1000:
        lens = sorted([len(c) for c in cs], reverse=True)
        print(math.prod(lens[:3]))
    if i1 == i2: continue
    cs[i1] = a | b
    del cs[i2]

print(j1[0] *  j2[0])