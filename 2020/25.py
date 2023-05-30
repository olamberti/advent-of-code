sn, div = 7, 20201227
nums = [int(x) for x in open('25.txt').read().splitlines()]

loops = []
for i in range(2):
  loop, val = 0, 1
  while val != nums[i]:
    val *= sn
    val = val % div
    loop += 1
  loops.append(loop)

val = 1
for i in range(loops[0]):
  val *= nums[1]
  val = val % div
print(val)