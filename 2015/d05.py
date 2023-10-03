def is_nice_p1(s):
    # 1st rule
    for c in ['ab', 'cd', 'pq','xy']:
        if c in s: return False
    # 2nd rule
    vowels = 0
    for c in 'aeiou':
        vowels += s.count(c)
    if vowels < 3: return False
    # 3rd rule
    for i in range(len(s) - 1):
        c1, c2 = s[i], s[i + 1]
        if c1 == c2: return True
    return False

def is_nice_p2(s):
    # 1st rule
    twice = False
    for i in range(len(s) - 1):
        c1, c2 = s[i], s[i + 1]
        for j in range(len(s) - 1):
            if abs(i - j) < 2: continue
            d1, d2 = s[j], s[j + 1]
            if c1 + c2 == d1 + d2:
                twice = True
    # 2nd rule
    repeat = False
    for i in range(len(s) - 2):
        c1, c3 = s[i], s[i + 2]
        if c1 == c3: repeat = True
    if twice and repeat: return True
    return False

p1, p2 = 0, 0
for line in open('05.txt').readlines():
    if is_nice_p1(line.strip()): p1 += 1
    if is_nice_p2(line.strip()): p2 += 1
print(p1)
print(p2)