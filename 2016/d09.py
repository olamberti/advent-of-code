inp = open('d09.txt').read()

def decomp(s, p2 = False):
    if '(' not in s: return len(s)
    res = 0
    while '(' in s:
        p = s.find('(')
        res += p
        s = s[p+1:]
        pe = s.find(')')
        z, t = [int(x) for x in s[:pe].split('x')]
        if p2:
            res += t * decomp(s[pe + 1: pe + z + 1], True)
        else:
            res += t * z
        s = s[pe + z + 1:]
    res += len(s)
    return res

# P1
print(decomp(inp))

# P2
print(decomp(inp, True))