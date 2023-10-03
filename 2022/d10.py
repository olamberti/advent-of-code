# Read input:
with open('d10.txt', 'r') as input:
  data = input.read().splitlines()

# Hack the program:
new_data = [item for sub in [(['noop', x] if x != 'noop' else [x]) for x in data] for item in sub]

# Execute new program:
X, cycle, cycles_to_read, signal_strengths = 1, 0, [i * 40 + 20 for i in range(6)], []
CRT_row, image = '', []
for command in new_data:
  cycle += 1
  pixel_pos, sprite = (cycle - 1) % 40, [X - 1, X, X + 1]
  CRT_row += '█' if pixel_pos in sprite else '.'
  if pixel_pos == 39:
    image.append(CRT_row)
    CRT_row = ''
  if cycle in cycles_to_read:
    signal_strengths.append(cycle * X)
  if command != 'noop':
    X += int(command.split()[1]) 
    
# Show solutions:
print(sum(signal_strengths))
print("\n".join([row for row in image]))