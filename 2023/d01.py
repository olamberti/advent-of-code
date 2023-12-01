import re

numbers = ['one','two','three','four','five','six','seven','eight','nine']

def convert(s):
    return str(numbers.index(s) + 1) if s in numbers else s

p1, p2 = 0, 0

for line in open('d01.txt').read().splitlines():
    # Part 1
    digits = re.findall(r'\d', line)
    p1 += int(digits[0] + digits[-1])
    # Part 2
    digits = re.findall(r'(?=(\d|' + '|'.join(numbers) + '))', line)
    p2 += int(convert(digits[0]) + convert(digits[-1]))

print(p1)
print(p2)