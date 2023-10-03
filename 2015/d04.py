import hashlib

inp, p1, p2 =  open('04.txt').read(), None, None
hash, x = inp, 0
while not (p1 and p2):
    x += 1
    hash = hashlib.md5((inp + str(x)).encode("utf-8")).hexdigest()
    if hash[:5] == '00000' and not p1:
        p1 = True; print(x)
    if hash[:6] == '000000':
        p2 = True; print(x)