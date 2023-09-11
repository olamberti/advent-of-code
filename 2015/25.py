import re
R, C = [int(x) for x in re.findall(r'\d+', open('25.txt').read())]

r, c, code = 1, 1, 20151125

while not(r == R and c == C):
    r , c = r - 1, c + 1
    if r == 0: r, c = c, 1
    code = code * 252533 % 33554393
print(code)