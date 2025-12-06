data = [line for line in open('d06.txt')]

# Part 1
db = [row.split() for row in data[:-1]]
ops = list(data[-1].split())
p1 = 0
for i, op in enumerate(ops):
    ns = [db[n][i] for n in range(len(db))]
    p1 += eval(op.join(ns))

print(p1)

# Part 2
db, ops = data[:-1], data[-1]
p2, ns = 0, []
for c in range(len(db[0])-1, -1, -1):
    n = ''.join([db[r][c] for r in range(len(db))])
    if n.strip() == '': continue
    ns.append(n)
    if (op:= ops[c]) != ' ':
        p2 += eval(op.join(ns))
        ns = []

print(p2)