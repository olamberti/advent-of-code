import hashlib
import re
salt = open('d14.txt').read()

def solve(salt, nhash = 1):
    keys, i, triplets = [], 0, {}
    while len(keys) < 64 or keys[63] + 1000 > i:
        h = salt + str(i)
        for _ in range(nhash):
            h = hashlib.md5((h).encode("utf-8")).hexdigest()
        c3 = re.findall(r'((.)\2{2})', h)
        if c3:
            if c3[0][1] in triplets: triplets[c3[0][1]].append(i)
            else: triplets[c3[0][1]] = [i]
        c5 = re.findall(r'((.)\2{4})', h)
        if c5:
            for _, c in c5:
                if c in triplets:
                    for v in triplets[c]:
                        if 0 < i - v < 1000:
                            keys.append(v)
                    triplets[c] = [i]
                    keys.sort()
        i += 1
    return keys[63]

# P1
print(solve(salt, 1))

# P2
print(solve(salt, 2017))