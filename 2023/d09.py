def expol(x):
    dx = [j - i for i, j in zip(x[:-1], x[1:])]
    if all(x == 0 for x in dx):
        return x[0], x[-1]
    else:
        x1, x2 = expol(dx)
        return x[0] - x1, x[-1] + x2, 

results = [expol([int(x) for x in line.split()]) for line in open('d09.txt')]
print(sum([x[1] for x in results]))
print(sum([x[0] for x in results]))