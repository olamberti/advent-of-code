# Read input:
data = []
for line in open('d25.txt', 'r'):
  data.append(line.strip())

# Define functions:
def snafu2dec(input):
  input, output = input[::-1], 0
  convert = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
  for i, char in enumerate(input):
    output += convert[char] * pow(5, i) 
  return output

def dec2snafu(input):
  output = ''
  convert = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}
  while input > 0:
    digit = input % 5
    input //= 5
    if digit <= 2:
      output = convert[digit] + output
    else:
      output = convert[digit] + output
      input += 1
  return output
      
# Calculate fuel ammount and convert it back:
fuel = sum([snafu2dec(item) for item in data])
print(dec2snafu(fuel))