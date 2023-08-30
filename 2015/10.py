num = open('10.txt').read()

def play(num):
    res, i, n = '', 0, 1
    while i < len(num):
        old = num[i]
        if i + 1 < len(num):
            new = num[i + 1]
            if old == new: n += 1
            else:
                res += str(n) + old
                n = 1
        else: res += str(n) + old
        i += 1
    return res

for i in range(50):
    num = play(num)
    if i == 39: print(len(num))
print(len(num))

# Runs slow for P2, needs an update...