def check_result(result, vals, p2 = False):
    combs = [vals[0]]
    for v in vals[1:]:
        new_combs = []
        for c in combs:
            a, b, c = c + v, c * v, int(str(c) + str(v))
            if a <= result: new_combs.append(a)
            if b <= result: new_combs.append(b)
            if c <= result and p2: new_combs.append(c)
        combs = new_combs
    return result in combs
    
p1, p2 = 0, 0
for line in open('d07.txt').read().splitlines():
    result, vals = line.split(': ')
    result, vals = int(result), [int(x) for x in vals.split()]
    if check_result(result, vals):
        p1 += result
    if check_result(result, vals, True):
        p2 += result

print(p1)
print(p2)