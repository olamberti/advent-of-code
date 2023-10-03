def tri(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

p1, p2 = 0, 0
for i, line in enumerate(open('d03.txt').read().splitlines()):
    if i % 3 == 0: A, B, C = [], [], []
    a, b, c = [int(x) for x in line.strip().split()]
    if tri(a, b, c): p1 += 1
    A.append(a); B.append(b); C.append(c)
    if i % 3 == 2:
        if tri(*A): p2 += 1
        if tri(*B): p2 += 1
        if tri(*C): p2 += 1
        
print(p1)
print(p2)