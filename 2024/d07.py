def check_result(result, vals, p2 = False):
    if len(vals) == 1:
        return vals[0] == result
    
    last = vals[-1]

    if result % last == 0:
        if check_result(result // last, vals[:-1], p2):
            return True

    if p2 and str(result)[-len(str(last)):] == str(last):
         if check_result((result - last) // pow(10, len(str(last))), vals[:-1], p2):
            return True

    return check_result(result - last, vals[:-1], p2)  
    
p1, p2 = 0, 0
for line in open('d07.txt').readlines():
    result, vals = line.split(': ')
    result, vals = int(result), [int(x) for x in vals.split()]
    if check_result(result, vals):
        p1 += result
    if check_result(result, vals, True):
        p2 += result

print(p1)
print(p2)