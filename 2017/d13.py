fw = {}
for line in open('d13.txt').read().splitlines(0):
    d, r = [int(x) for x in line.split(': ')]
    fw[d] = r

# P1
def getpos(r, t):
    m = t % (r - 1)
    if t // (r - 1) % 2 == 0: return m
    else: return r - m

sev = 0
for d, r in fw.items():
    if getpos(r, d) == 0: sev += r * d
print(sev)

# P2
p2 = 0
while True:
    for d, r in fw.items():
        if getpos(r, d + p2) == 0: break
    else:
        print(p2)
        break
    p2 += 1