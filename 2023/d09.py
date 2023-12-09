def get_next(x):
    dx = [j - i for i, j in zip(x[:-1], x[1:])]
    if all(x == 0 for x in dx):
        return x[0], x[-1]
    else:
        x1, x2 = get_next(dx)
        return x[0] - x1, x[-1] + x2, 

p1, p2 = 0, 0
for line in open('d09.txt'):
    v1, v2 = get_next([int(x)  for x in line.split()])
    p1 += v2
    p2 += v1

print(p1)
print(p2)