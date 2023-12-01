import regex as re

p1, p2 = 0, 0
d2n = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
       'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

for line in open('d01.txt').read().splitlines():
    # Part 1
    d1 = re.findall(r'\d', line)
    p1 += int(d1[0] + d1[-1])
    # Part 2
    d2 = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
    d21 = d2n[d2[0]] if d2[0] in d2n else d2[0]
    d22 = d2n[d2[-1]] if d2[-1] in d2n else d2[-1]
    p2 += int(d21 + d22)

print(p1)
print(p2)