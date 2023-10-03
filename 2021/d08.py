# Read input:
with open('d08.txt', 'r') as input:
  text = input.read().splitlines()

# Function definitions:
segemnt_display = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}

def unhack(pattern):
  convert = {}
  chars = 'abcdefg'
  char_occurances = [pattern.count(char) for char in chars]
  # 1st step - identify uniquely occuring characters 
  convert[chars[char_occurances.index(6)]] = 'b'
  convert[chars[char_occurances.index(4)]] = 'e'
  convert[chars[char_occurances.index(9)]] = 'f'
  # 2nd step - identfy unique length codes
  pattern = pattern.split()
  for code in pattern:
    if len(code) == 2:
      code_1 = code
    elif len(code) == 3:
      code_7 = code
    elif len(code) == 4:
      code_4 = code
  for char in code_1:
    if char not in list(convert.keys()):
      convert[char] = 'c'
  for char in code_4:
    if char not in list(convert.keys()):
      convert[char] = 'd'
  for char in code_7:
    if char not in list(convert.keys()):
      convert[char] = 'a'
  for char in chars:
    if char not in list(convert.keys()):
      convert[char] = 'g'
  return convert

def calc_digits(output, dict):
  decoded = []
  for code in output:
    new_code = ''
    for char in code:
      new_code += dict[char]
    new_code = ''.join(sorted(new_code))
    decoded.append(new_code)
  digits = ''
  for code in decoded:
    digits += segemnt_display[code]
  return digits
  
# Conut unique lengths:
unique_digits = 0
unique_lengths = [2, 3, 4, 7]
summa = 0
for line in text:
  line = line.split('|')
  current_pattern = line[0]
  current_output = line[1].split()
  my_dict = unhack(current_pattern)
  digits = calc_digits(current_output, my_dict)
  summa += int(digits)
  for segment in current_output:
    if len(segment) in unique_lengths:
      unique_digits += 1

print(unique_digits)
print(summa)