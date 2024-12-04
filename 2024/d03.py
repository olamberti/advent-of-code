import re
input = open('d03.txt').read()

def add_muls(s):
    muls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', s)
    return sum([int(x) * int(y) for (x, y) in muls])
 
p1 = add_muls(input)
print(p1)

p2, input = 0, input.split('do()')
for s in input:
    p2 += add_muls(s.split("don't()")[0])
print(p2)