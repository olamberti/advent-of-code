max = [0, 0, 0]
with open('d01.txt','r') as calories:
  current_elf = 0
  for line in calories:
    if line != "\n":
      current_elf += int(line)
    else:
      if current_elf > max[2]:
        max[2] = current_elf
        current_elf = 0
      else:
        current_elf = 0 
      max.sort(reverse = True)
print(max[0])
print(sum(max))