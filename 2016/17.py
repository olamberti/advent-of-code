import hashlib

inp, dirs = open('17.txt').read(), {'U': -1j, 'D': 1j, 'L': -1, 'R': 1}

def doors_open(code):
    h, res = hashlib.md5((code).encode("utf-8")).hexdigest(), []
    for i, d in enumerate(['U', 'D', 'L', 'R']):
        if h[i] in 'bcdef': res.append(d)
    return res

front, p1 = set(), None
front.add((0, ''))

while front:
    nfront = set()
    for pos, path in front:
        for door in doors_open(inp + path):
            npos = pos + dirs[door]
            if not(0 <= npos.real < 4) or not(0 <= npos.imag < 4): continue
            npath = path + door
            if npos == 3 + 3j:
                p2 = len(npath)
                if not p1: p1 = npath
            else: nfront.add((npos, npath))
    front = nfront
print(p1)
print(p2)