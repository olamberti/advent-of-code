import heapq

def dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2

boxes = [tuple(map(int, line.split(','))) for line in open('d08.txt')]
dists, circuits = [], []
for i in range(len(boxes)):
    circuits.append({boxes[i]})
    for j in range(i + 1, len(boxes)):
        heapq.heappush(dists, (dist(boxes[i], boxes[j]), (i, j)))

n = 0
while len(circuits) > 1:
    n += 1
    _, (j1, j2) = heapq.heappop(dists)
    for j, c in enumerate(circuits):
        if boxes[j1] in c:
            i1 = j
            a = c
        if boxes[j2] in c:
            i2 = j
            b = c       
    if n == 1000:
        lens = sorted([len(c) for c in circuits], reverse=True)
        print(lens[0] * lens[1] * lens[2])
    if i1 == i2: continue
    circuits[i1] = a | b
    del circuits[i2]

print(boxes[j1][0] * boxes[j2][0])