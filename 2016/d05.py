import hashlib
dID = open('d05.txt').read()

i, p1, p2 = 0, '', ['?']*8
while len(p1) < 8 or '?' in p2:
    hash = hashlib.md5((dID + str(i)).encode("utf-8")).hexdigest()
    if hash[:5] == '00000':
        if len(p1) < 8: p1 += hash[5]
        if hash[5] in '01234567':
            p = int(hash[5])
            if p2[p] == '?': p2[p] = hash[6]
    i += 1
print(p1)
print(''.join(p2))