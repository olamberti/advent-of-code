from collections import defaultdict
data, updates = open('d05.txt').read().split('\n\n')

rules = defaultdict(list)
for row in data.splitlines():
    first, second = map(int, row.split('|'))
    rules[first].append(second)

def is_right(vals):
    for v in vals:
        for larger in rules[v]:
            if larger in vals and vals.index(larger) < vals.index(v):
                return False
    return True

p1, p2 = 0, 0
for row in updates.splitlines():
    update = list(map(int, row.split(',')))
    if is_right(update):
        p1 += update[len(update)//2]
    else:
        while not is_right(update):
            for v in update:
                    for larger in rules[v]:
                        if larger in update and update.index(larger) < update.index(v):
                            update.remove(v)
                            update.insert(update.index(larger), v)
        p2 += update[len(update)//2]

print(p1)
print(p2)