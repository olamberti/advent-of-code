import re

def abba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]: return True
    return False

def ssl(sn, hn):
    for i in range(len(sn) - 2):
        if sn[i] == sn[i+2]:
            bab = sn[i+1] + sn[i] + sn[i+1]
            if bab in hn: return True
    return False

p1, p2 = 0, 0
for line in open('d07.txt').read().splitlines():
    parts = re.split(r'\[(\w+)\]', line)
    sn, hn = '-'.join(parts[0::2]), '-'.join(parts[1::2])
    if not abba(hn) and abba(sn): p1 += 1
    if ssl(sn, hn): p2 += 1
print(p1)
print(p2)