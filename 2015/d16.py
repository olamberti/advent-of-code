import re

clue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
        'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

def checkline(line, part2 = False):
    for elem in re.findall(r'\w+: \d+',line.strip()):
        item, n = elem.split(': ')[0], int(elem.split(': ')[1])
        if part2 and item in ['cats', 'trees']:
            if not(n > clue[item]): return False
        elif part2 and item in ['pomeranians', 'goldfish']:
           if not(n < clue[item]): return False
        elif clue[item] != n: return False
    return True

p1, p2 = 0, 0
for i, line in enumerate(open('16.txt').readlines()):
    if checkline(line): p1 = i + 1
    if checkline(line, True): p2 = i + 1
    if p1 and p2: break

print(p1)
print(p2)