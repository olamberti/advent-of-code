data = open('d16.txt').read()

def fill(a):
    b = ''.join(['0' if x == '1' else '1' for x in a[::-1]])
    return a + '0' + b

def checksum(a, n):
    while n % 2 == 0:
        b = []
        for x, y in zip(a[:n+1:2], a[1:n+1:2]):
            if x == y: b.append('1')
            else: b.append('0')
        a, n = ''.join(b), len(b)
    return a

def solve(data, space):
    while len(data) < space:
        data = fill(data)
    return checksum(data, space)

# P1
print(solve(data, 272))

# P2
print(solve(data, 35651584))