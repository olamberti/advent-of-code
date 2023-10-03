def part1(s):
    res, i, s = 2, 0, s[1:-1]
    while i < len(s) - 1:
        c1, c2 = s[i], s[i + 1]
        if c1 == '\\':
            if c2 == '\\' or c2 == '\"':
                res += 1
                i += 1
            elif c2 == 'x':
                res += 3
                i += 3
        i += 1
    return res

def part2(s):
    return 2 + s.count('\"') + s.count('\\')
        
p1, p2 = 0, 0
for line in open('d08.txt').readlines():
    p1 += part1(line.strip())
    p2 += part2(line.strip())
print(p1)
print(p2)