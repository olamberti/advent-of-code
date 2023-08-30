from itertools import groupby as gb
num = open('10.txt').read()

def lookandsay(s):
    return ''.join([str(sum(1 for _ in g)) + k for k, g in gb(s)])

for i in range(50):
    num = lookandsay(num)
    if i == 39: print(len(num))
print(len(num))