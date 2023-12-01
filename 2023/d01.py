import regex as re

p1, p2 = 0, 0
num2dig = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
            'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

for line in open('d01.txt').read().splitlines():
    # Part 1
    digits = re.findall(r'\d', line)
    p1 += int(digits[0] + digits[-1])
    
    # Part 2
    digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
    first = num2dig[digits[0]] if digits[0] in num2dig else digits[0]
    last = num2dig[digits[-1]] if digits[-1] in num2dig else digits[-1]
    p2 += int(first + last)

print(p1)
print(p2)