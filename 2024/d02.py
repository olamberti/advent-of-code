def is_safe(vals):
    return vals <= {1, 2, 3} or vals <= {-1, -2, -3}

p1, p2= 0, 0

for line in open('d02.txt').read().splitlines():
    nums = [int(x) for x in line.split()]
    diffs = set([nums[i] - nums[i-1] for i in range(1, len(nums))])
    if is_safe(diffs):
        p1 += 1
        p2 += 1
        continue
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        diffs = set([new_nums[i] - new_nums[i-1] for i in range(1, len(new_nums))])
        if is_safe(diffs):
            p2 += 1
            break
    
print(p1)
print(p2)