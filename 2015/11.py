pw = open('11.txt').read()

def inc(c):
    return chr((ord(c) - 96) % 26 + 97)

def next_pass(pw):
    if pw == 'z': return 'a'
    pw = pw[:-1] + inc(pw[-1])
    if pw[-1] == 'a': pw = next_pass(pw[:-1]) + pw[-1]
    return pw

def check(pw):
    # Rule 1
    if 'i' in pw or 'o' in pw or 'l' in pw: return False
    # Rule 2
    stop = True
    for i in range(97,121):
        if (chr(i) + chr(i + 1) + chr(i + 2)) in pw: stop = False
    if stop: return False
    # Rule 3
    i, double = 0, 0
    while i < len(pw) - 1:
        c1, c2 = pw[i], pw[i + 1]
        if c1 == c2:
            double += 1
            i += 1
        i += 1
    if double < 2: return False
    return True

# P1
p1, p2 = False, False
while not (p1 and p2):
    if check(pw):
        print(pw)
        if p1 and not p2: p2 = True
        if not p1: p1 = True
    pw = next_pass(pw)