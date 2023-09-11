import re

r, c = [int(x) for x in re.findall(r'\d+', open('25.txt').read())]
code, i = 20151125, (r + c - 1)*(r + c) // 2 - r
print(code * pow(252533, i, 33554393) % 33554393)