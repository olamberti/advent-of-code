# Read input:
import copy
with open('13.txt', 'r') as input:
  data = input.read().splitlines() 

# Comparison function (returns 1: OK, 0: no decision, -1: NOK):
def compare_items(left_item, right_item):
  left, right= copy.deepcopy(left_item), copy.deepcopy(right_item)
  if (isinstance(left, int)) and isinstance(right, int): # both are integers
    if left < right:
      return 1
    elif left > right:
      return -1
    else:
      return 0
  elif isinstance(left, list) and isinstance(right, list): # both are lists
    lengths = [len(left), len(right)]
    while 0 not in lengths: # both list have still elements
      comparison = compare_items(left[0], right[0])
      if comparison != 0: # decision was made
        return comparison
      else: # otherwise remove first elements and update lengths
        left.pop(0)
        right.pop(0)
        lengths = [len(left), len(right)]
    if (lengths[0] == 0) and (lengths[1] == 0): # both lists are empty
      return 0
    elif lengths[0] == 0: # left side run out of items
      return 1
    elif lengths[1] == 0: # right side run out of items
      return -1
  elif isinstance(left, list) and isinstance(right, int): # right one in integer
    comparison = compare_items(left, [right])
    return comparison
  elif isinstance(left, int) and isinstance(right, list): # right one in integer
    comparison = compare_items([left], right)
    return comparison

# Part 1 - Count right order pairs:
index, total_sum, number_of_pairs  = 1, 0, (len(data) + 1) // 3
packets, divider_packets = [], [ [[2]] , [[6]] ]
while index <= number_of_pairs:
  left_side, right_side = eval(data[(index * 3) - 3]), eval(data[(index * 3) - 2])
  packets.append(left_side)
  packets.append(right_side)
  if compare_items(left_side, right_side) == 1:
    total_sum += index
  index += 1
print(total_sum)

# Part 2 - Look for positions of divider packets:
pos = [1, 2]
for i, divider in enumerate(divider_packets):
  for packet in packets:
    if compare_items(packet, divider) == 1:
      pos[i] += 1
print(pos[0] * pos[1])