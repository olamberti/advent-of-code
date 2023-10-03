data = []
for line in open('20.txt').read().splitlines():
    x, y = line.split('-')
    data.append((int(x), int(y)))
data.sort()

# P1
p1, i = 0, 0
while data[i][0] <= p1:
    p1 = data[i][1] + 1
    i += 1
print(p1)

# P2
xm, xM, p2 = 0, 4294967295, 0
for low, high in data:
    if xm <= low: p2 += low - xm
    if high > xm: xm = high + 1
if xm < xM: p2 += xM - xm
print(p2)