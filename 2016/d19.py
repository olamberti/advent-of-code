import math
n = int(open('d19.txt').read())

# P1
print(int('0b' + bin(n)[3:] + '1', 2))

# P2
t = int(pow(3, math.floor(math.log(n, 3))))
if n == t: print(n)
elif n < t * 2: print(n - t)
else: print(2 * n - 3 * t)