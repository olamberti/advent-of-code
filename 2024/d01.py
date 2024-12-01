left, right = [], []

for line in open('d01.txt').read().splitlines():
    left_num, right_num = [int(x) for x in line.split()]
    left.append(left_num)
    right.append(right_num)

left.sort()
right.sort()

total_distance, similarity = 0, 0
for i in range(len(left)):
    total_distance += abs(left[i] - right[i])
    similarity += left[i] * right.count(left[i])

print(total_distance)
print(similarity)