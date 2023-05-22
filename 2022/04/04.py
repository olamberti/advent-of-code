def read_line(line):
  line = line.strip().split(",")
  elf_1 = line[0].split("-")
  elf_2 = line[1].split("-")
  elf_1_low = int(elf_1[0])
  elf_1_high = int(elf_1[1])
  elf_2_low = int(elf_2[0])
  elf_2_high = int(elf_2[1])
  return [elf_1_low, elf_1_high, elf_2_low, elf_2_high]

def full_contains(a1, a2, b1, b2):
  return ((a1 <= b1) and (a2 >= b2)) or ((a1 >= b1) and (a2 <= b2))

def overlaps(a1, a2, b1, b2):
  return ((a1 < b1) and (a2 < b1)) or ((a1 > b2) and (a2 > b2))
  
count_contains = 0
count_overlaps = 0
with open("04.txt","r") as input:    # use "input_test.txt" for test_case
  for line in input:
    pairs = read_line(line)
    if full_contains(*pairs):
      count_contains += 1
    if not overlaps(*pairs):
      count_overlaps += 1
print(count_contains)
print(count_overlaps)