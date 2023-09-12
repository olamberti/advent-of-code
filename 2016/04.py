def shift(c, n):
    return chr((ord(c) - 97 + n) % 26 + 97)

p1, p2 = 0, None
for line in open('04.txt').read().splitlines():
    line = line.strip().split('-')
    name = line[:-1]
    sID, check = line[-1].split('[')
    sID, check = int(sID), check[:-1]
    
    # P1
    chars = {}
    for c in ''.join(name):
        if c not in chars: chars[c] = 1
        else: chars[c] += 1
    chars = [(k, v) for k, v in chars.items()]
    chars.sort(key= lambda x: x[0])
    chars.sort(key= lambda x: x[1], reverse = True)
    to_check = ''
    for i in range(len(check)): to_check += chars[i][0]
    if check == to_check: p1 += sID

    # P2 (a - 97, z - 122)
    rname = ''
    for sname in name:
        for c in sname:
            rname += shift(c, sID)
        rname += ' '
    if 'northpole object' in rname:
        p2 = sID
print(p1)
print(p2)