def check(num):
    if all(n in (1, 2, 3) for n in num) or all(n in (-1, -2, -3) for n in num):
        return True
    return False

p1, p2= 0, 0

for line in open('d02.txt').read().splitlines():
    nums = [int(x) for x in line.split()]
    diffs = set([nums[i] - nums[i-1] for i in range(1, len(nums))])
    if check(diffs):
        p1 += 1
        p2 += 1
        continue
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        diffs = set([new_nums[i] - new_nums[i-1] for i in range(1, len(new_nums))])
        if check(diffs):
            p2 += 1
            break
    
print(p1)
print(p2)