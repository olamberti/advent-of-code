inp = [int(x) for x in open('d01.txt').read()]

# P1
p1, p2 = 0, 0
d, m = len(inp) // 2, len(inp)
for i in range(len(inp)):
    if inp[i] == inp[(i + 1) % m]: p1 += inp[i]
    if inp[i] == inp[(i + d) % m]: p2 += inp[i]
print(p1)
print(p2)