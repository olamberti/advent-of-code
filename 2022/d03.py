def calc_priority(item):
  if item.isupper():
    return ord(item) - 38  # Unicode conversion for uppercase
  else:
    return ord(item) - 96  # Unicode conversion for lowercase

def find_item(comp_1, comp_2):
  items_1 = list(comp_1)
  items_2 = list(comp_2)
  for item in items_1:
    if item in items_2:
      return item

def find_badge(bags):
  items_1 = list(bags[0])
  items_2 = list(bags[1])
  items_3 = list(bags[2])
  for item in items_1:
    if item in items_2 and item in items_3:
      return item

priority = 0
badges = 0
bags = ["", "", ""]
i = 1
with open("d03.txt","r") as input:    # use "input_test.txt" for test case
  for bag_content in input:
    bag_content = bag_content.rstrip()
    bag_size = int(len(bag_content) / 2)
    comp_1 = bag_content[:bag_size]
    comp_2 = bag_content[bag_size:]
    priority += calc_priority(find_item(comp_1, comp_2))
    bags[i - 1] = bag_content
    if i == 3:
      badges += calc_priority(find_badge(bags))
      i = 0
    i += 1
print(priority)
print(badges)