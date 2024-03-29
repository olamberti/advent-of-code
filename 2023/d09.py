def expol(x):
    if not any(x): return 0
    return x[-1] + expol([j - i for i, j in zip(x, x[1:])])

data = [[int(n) for n in line.split()] for line in open('d09.txt')]
print(sum([expol(x) for x in data]))
print(sum([expol(x[::-1]) for x in data]))